#!/usr/bin/env python3
"""Ghi nhật ký văn bản theo nguồn và phiên, ngoài Git. Dùng Python 3.9+ trên macOS/Linux/WSL."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import sys
import uuid

HOME_STATE = Path.home() / ".bo-nao-david"
REPO = Path(__file__).resolve().parents[2]
# Chỉ lọc các dạng nhận diện được. Nhật ký vẫn là dữ liệu của tài khoản.
SECRET = re.compile(
    r"(?i)\b(?:sk-[\w-]{20,}|gh[pousr]_[\w]{20,}|github_pat_[\w_]{20,}|"
    r"AIza[\w-]{30,}|AKIA[A-Z0-9]{16}|xox[baprs]-[\w-]{10,}|"
    r"eyJ[\w-]+\.eyJ[\w-]+\.[\w-]+|\d{8,10}:[\w-]{30,})\b"
    r"|(?im:^\s*(?:set-cookie|cookie|authorization)\s*:[^\r\n]+)"
    r"|(?i:bearer\s+)[\w./+=-]{8,}"
    r"|(?im:(?:password|passwd|token|secret|api[_-]?key|cookie|otp|cccd)[\"']?\s*[:=]\s*[\"']?(?:bearer\s+)?[^\s,;\"']+)"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?(?:-----END [A-Z ]*PRIVATE KEY-----|\Z)"
    r"|(?i:data:(?:image|video|audio)/[^\s,]+,)[^\s\"']+"
)
PRIVATE_FILE = re.compile(r"(?i)(?:^|[/\\\s])(?:\.env(?:\.[\w-]+)?|id_rsa|id_ed25519)(?=$|[/\\\s\"'])")
SENSITIVE_KEYS = {
    "password", "passwd", "token", "access_token", "refresh_token", "api_key", "apikey",
    "secret", "client_secret", "authorization", "cookie", "set_cookie", "otp", "cccd",
}
MEDIA = {"image", "input_image", "output_image", "image_url", "audio", "input_audio",
         "output_audio", "video", "document", "file", "input_file", "output_file"}
INTERNAL = {"thinking", "redacted_thinking", "reasoning", "analysis"}
HOOKS = {
    "claude-code": ("SessionStart", "UserPromptSubmit", "PreToolUse", "PostToolUse",
                    "PostToolUseFailure", "Stop", "SessionEnd"),
    "codex": ("SessionStart", "UserPromptSubmit", "PreToolUse", "PostToolUse",
              "Interrupt", "Stop", "SessionEnd"),
}


def safe(value):
    """Giữ dữ liệu nguồn và đánh dấu phần bảo vệ hoặc phương tiện nhị phân."""
    if isinstance(value, str):
        return SECRET.sub("[đã loại giá trị được bảo vệ hoặc dữ liệu đa phương tiện]", value)
    if isinstance(value, list):
        return [safe(item) for item in value]
    if not isinstance(value, dict):
        return value
    kind = value.get("type")
    if isinstance(kind, str) and (kind in INTERNAL or value.get("channel") == "analysis" or value.get("phase") == "analysis"):
        return {"type": kind, "nhat_ky": "đã loại nội dung suy luận nội bộ"}
    if isinstance(kind, str) and kind in MEDIA:
        return {**{k: safe(value[k]) for k in ("type", "id", "file_id", "name", "mime_type", "path")
                   if k in value}, "nhat_ky": "chỉ ghi tham chiếu, không sao chép phương tiện"}
    if any(isinstance(value.get(k), str) and PRIVATE_FILE.search(value[k])
           for k in ("file_path", "path", "command")):
        return {"nhat_ky": "đã loại nội dung thao tác với tệp cấu hình bí mật"}
    result = {}
    for key, item in value.items():
        normalized = key.lower().replace("-", "_")
        if normalized in SENSITIVE_KEYS or normalized in INTERNAL or normalized == "encrypted_content":
            result[key] = "[đã loại]"
        elif normalized in MEDIA:
            result[key] = "[chỉ ghi tham chiếu phương tiện]"
        else:
            result[key] = safe(item)
    return result


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode()


def private_open(path, flags):
    return os.open(path, flags | getattr(os, "O_NOFOLLOW", 0), 0o600)


@contextmanager
def locked(path):
    with os.fdopen(private_open(path, os.O_RDWR | os.O_CREAT), "r+b") as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        yield file


def store_root():
    selected = Path(os.environ.get("DAVID_NHAT_KY_DIR", str(HOME_STATE / "nhat-ky")))
    root = selected.expanduser().resolve()
    if root == REPO or REPO in root.parents or any((p / ".git").exists() for p in (root, *root.parents)):
        raise ValueError("Thư mục nhật ký phải nằm ngoài kho Git.")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    return root


def device_id():
    HOME_STATE.mkdir(parents=True, exist_ok=True, mode=0o700)
    with locked(HOME_STATE / "thiet-bi") as file:
        current = file.read().decode().strip()
        if not re.fullmatch(r"[0-9a-f]{32}", current):
            current = uuid.uuid4().hex
            file.seek(0)
            file.write(current.encode())
            file.truncate()
            file.flush()
            os.fsync(file.fileno())
    return current


def last_event(file):
    """Đọc dòng cuối đã ghi trọn và loại phần dòng cuối dở sau khi bị ngắt."""
    end = file.seek(0, os.SEEK_END)
    data = b""
    while end and data.count(b"\n") < 2:
        start = max(0, end - 8192)
        file.seek(start)
        data = file.read(end - start) + data
        end = start
    last_newline = data.rfind(b"\n")
    valid_end = end + last_newline + 1
    file.seek(0, os.SEEK_END)
    if file.tell() != valid_end:
        file.truncate(valid_end)
    if valid_end == 0:
        return {}
    previous = data.rfind(b"\n", 0, last_newline)
    return json.loads(data[previous + 1:last_newline])


def collect(source, session, hook, transcript=None, text=None, coverage="hook", import_digest=None, work_id=None):
    device = device_id()
    source_key = hashlib.sha256(source.encode()).hexdigest()[:12]
    session_key = hashlib.sha256((session if import_digest is None else session + ":" + import_digest).encode()).hexdigest()[:24]
    folder = store_root() / device / source_key
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = folder / (session_key + ".jsonl")
    with locked(path) as log:
        last = last_event(log)
        cursor = last.get("vi_tri_nguon", 0)
        generation = last.get("dot_nguon", 0)
        sequence = last.get("thu_tu", 0)

        def append(kind, payload):
            nonlocal sequence
            sequence += 1
            log.seek(0, os.SEEK_END)
            log.write(encoded({
                "phien_ban": 1, "su_kien": f"{device}:{source_key}:{session_key}:{sequence}",
                "thu_tu": sequence, "nguon": source, "phien": session, "thiet_bi": device,
                "may": socket.gethostname(), "viec": work_id, "luc_ghi": datetime.now(timezone.utc).isoformat(),
                "loai": kind, "vi_tri_nguon": cursor, "dot_nguon": generation,
                "du_lieu": safe(payload),
            }))

        if transcript and transcript.is_file():
            with transcript.open("rb") as incoming:
                limit = os.fstat(incoming.fileno()).st_size
                if limit < cursor:
                    cursor = 0
                    generation += 1
                    append("nguon_bat_dau_lai", {"ly_do": "Nguyên bản ngắn hơn vị trí đã ghi."})
                incoming.seek(cursor)
                while cursor < limit:
                    line = incoming.readline(limit - cursor)
                    if not line or (not line.endswith(b"\n") and coverage != "nhap-jsonl"):
                        break
                    cursor += len(line)
                    try:
                        entry = json.loads(line)
                    except (ValueError, UnicodeError):
                        append("dong_nguon_khong_doc_duoc", {"so_byte": len(line)})
                        continue
                    append("lich_su_nguon", entry)
            recorded = "da_doc_den_vi_tri_nguon"
        elif text is not None:
            if cursor == 0:
                cursor = len(text.encode())
                append("van_ban_nguon", text)
            recorded = "van_ban_nhap"
        else:
            recorded = "khong_co_tep_nguon"
        # Mỗi điểm gọi ghi một sự kiện riêng, kể cả khi nguồn chưa kịp cập nhật lịch sử.
        if coverage == "hook" or not last:
            append("moc_ghi", {"muc_bao_phu": recorded, "su_kien_ung_dung": hook})
        log.flush()
        os.fsync(log.fileno())
    return path


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="action", required=True)
    hook = commands.add_parser("hook")
    hook.add_argument("source", choices=HOOKS)
    ingest = commands.add_parser("nhap")
    ingest.add_argument("file", type=Path)
    ingest.add_argument("--nguon", required=True)
    ingest.add_argument("--phien", required=True)
    ingest.add_argument("--van-ban", action="store_true")
    ingest.add_argument("--viec")
    options = cli.parse_args()
    if options.action == "hook":
        payload = json.load(sys.stdin)
        session = payload.get("session_id")
        if not isinstance(session, str) or not session:
            raise ValueError("Ứng dụng không cung cấp mã phiên.")
        filename = payload.get("transcript_path")
        collect(options.source, session, payload, Path(filename) if filename else None,
                work_id=os.environ.get("DAVID_NHAT_KY_VIEC"))
    else:
        source = options.file.expanduser().resolve(strict=True)
        mode = "nhap-van-ban" if options.van_ban else "nhap-jsonl"
        # Gắn mã nội dung vào bản nhập để nhập lại cùng dữ liệu không tạo dòng trùng.
        digest = hashlib.sha256()
        with source.open("rb") as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b""):
                digest.update(chunk)
        print(collect(options.nguon, options.phien, {}, None if options.van_ban else source,
                      source.read_text(encoding="utf-8") if options.van_ban else None,
                      mode, hashlib.sha256((mode + ":" + digest.hexdigest()).encode()).hexdigest(), options.viec))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        # Công cụ có thể hiện stderr cho AI. Chỉ in loại lỗi, không in dữ liệu nguồn.
        print(f"Nhật ký chưa ghi được ({type(error).__name__}). Kiểm vị trí lưu và định dạng nguồn.", file=sys.stderr)
        sys.exit(1)
