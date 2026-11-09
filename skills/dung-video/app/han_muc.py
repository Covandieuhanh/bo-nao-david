#!/usr/bin/env python3
"""HẠN MỨC CLAUDE CÒN LẠI (David muốn 09/11/2026: chỉ dùng app vẫn tự cân đối được).
Claude Code chạy ngầm (`--output-format stream-json --verbose`) gửi kèm sự kiện `rate_limit_event` — % đã dùng của khung 5 giờ và
7 ngày + giờ mở lại. App lưu bản mới nhất vào ~/Movies/_app/_han-muc.json; giao diện đọc file này.
  python3 -I han_muc.py lam-moi   → hỏi lại bằng một câu rất nhỏ (haiku, không công cụ, gần như 0 token)
Không đọc mật khẩu / token đăng nhập; chỉ đọc con số Claude Code tự in ra."""
import json, os, subprocess, sys, time
from pathlib import Path

KHO = Path(os.path.expanduser("~/Movies/_app")); F = KHO / "_han-muc.json"


def ghi(su_kien):
    """su_kien = dict của dòng rate_limit_event. Chỉ giữ phần cần hiện."""
    info = su_kien.get("rate_limit_info") or {}
    win = info.get("unifiedWindows") or {}
    if not win and info.get("rateLimitType"):
        win = {info["rateLimitType"]: info}
    if not win:
        return
    d = {k: {"dung": round(float(v.get("utilization", 0)) * 100), "mo_lai": v.get("resetsAt"), "trang_thai": v.get("status")}
         for k, v in win.items() if k in ("five_hour", "seven_day")}
    if not d:
        return
    KHO.mkdir(parents=True, exist_ok=True)
    tmp = F.with_suffix(".tmp"); tmp.write_text(json.dumps({"luc": int(time.time()), **d}, ensure_ascii=False)); os.replace(tmp, F)


def doc_dong(dong):
    """Đọc một dòng stream-json; gặp rate_limit_event thì ghi. Trả dict của dòng (hoặc None)."""
    try:
        d = json.loads(dong)
    except ValueError:
        return None
    if d.get("type") == "rate_limit_event":
        ghi(d)
    return d


def doc():
    try:
        return json.loads(F.read_text())
    except Exception:
        return None


def lam_moi():
    sys.path.insert(0, str(Path(__file__).parent)); import goi_ai
    r = subprocess.run([goi_ai.tim_claude(), "-p", "--model", "haiku", "--output-format", "stream-json", "--verbose", "--tools", "",
                        "--setting-sources", "", "--no-session-persistence"], input="Trả lời đúng một chữ: ok",
                       capture_output=True, text=True, timeout=90, cwd=str(KHO), env=goi_ai.ENV)
    for dong in r.stdout.splitlines():
        doc_dong(dong)
    return doc()


if __name__ == "__main__":
    if sys.argv[1:] == ["lam-moi"]:
        print(json.dumps(lam_moi(), ensure_ascii=False))
    else:
        print(json.dumps(doc(), ensure_ascii=False))
