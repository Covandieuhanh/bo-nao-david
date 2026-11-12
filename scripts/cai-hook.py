"""Ghi hook vào ~/.claude/settings.json để đồng bộ 2 chiều bộ não với GitHub:
- SessionStart: kéo bản mới từ GitHub về (sync.sh --keo)
- SessionEnd: đẩy thay đổi lên (hook-sync.sh, chạy nền)
- PostToolUse + Stop: hộp thư phiên, lời David qua Telegram vào đúng phiên (scripts/so-nho/hop-thu-phien.py)
- PreToolUse: cổng duyệt việc rủi ro cho phiên việc toàn quyền (scripts/so-nho/cong-duyet.py)
- SessionEnd (thứ hai): ghi tín hiệu tự học (scripts/tu-hoc/ghi-tin-hieu.py)
- PermissionRequest: duyệt từ xa qua Telegram khi David vắng (scripts/so-nho/duyet-tu-xa.py)
Chạy lại nhiều lần không bị trùng. Dùng: python3 -I scripts/cai-hook.py <đường dẫn repo>"""
import json, os, sys
repo = os.path.abspath(sys.argv[1])
p = os.path.expanduser("~/.claude/settings.json")
cfg = json.load(open(p)) if os.path.exists(p) else {}
hooks = cfg.setdefault("hooks", {})
can = {
    "SessionStart": (f'bash "{repo}/scripts/sync.sh" --keo >/dev/null 2>&1 || true', '/scripts/sync.sh" --keo'),
    "SessionEnd": (f'bash "{repo}/scripts/hook-sync.sh"', '/scripts/hook-sync.sh"'),
}
# Duyệt từ xa qua Telegram (bot Sổ nhớ): David vắng thì yêu cầu duyệt và câu hỏi chuyển lên Telegram, chờ tối đa 30 phút.
can["PermissionRequest"] = (f'python3 -I "{repo}/scripts/so-nho/duyet-tu-xa.py"', '/scripts/so-nho/duyet-tu-xa.py"')
# Hộp thư phiên: lời David gửi qua bot Telegram cho một phiên đang mở, đưa vào sau mỗi bước (PostToolUse) hoặc khi xong lượt (Stop).
can["PostToolUse"] = (f'python3 -I "{repo}/scripts/so-nho/hop-thu-phien.py"', '/scripts/so-nho/hop-thu-phien.py"')
can["Stop"] = (f'python3 -I "{repo}/scripts/so-nho/hop-thu-phien.py"', '/scripts/so-nho/hop-thu-phien.py"')
# Cổng duyệt cho phiên việc toàn quyền giao qua Telegram (chỉ bật khi TELEGRAM_VIEC=1): việc rủi ro hỏi David qua Telegram.
can["PreToolUse"] = (f'python3 -I "{repo}/scripts/so-nho/cong-duyet.py"', '/scripts/so-nho/cong-duyet.py"')
# Tự học: cuối phiên ghi tín hiệu (lời David sửa, skill dùng, lỗi) cho skill tu-hoc, không gọi AI.
can["SessionEnd#tu-hoc"] = (f'python3 -I "{repo}/scripts/tu-hoc/ghi-tin-hieu.py"', '/scripts/tu-hoc/ghi-tin-hieu.py"')
cho = {"PermissionRequest": 1800, "PreToolUse": 1800}
for khoa, (cmd, dau) in can.items():
    su_kien = khoa.split("#")[0]
    ds = hooks.setdefault(su_kien, [])
    if not any(dau in h.get("command", "") for g in ds for h in g.get("hooks", [])):
        g = {"hooks": [{"type": "command", "command": cmd, "timeout": cho.get(su_kien, 30)}]}
        if su_kien in ("PermissionRequest", "PostToolUse", "PreToolUse"): g["matcher"] = "*"
        ds.append(g)
    print(f"Hook {su_kien}: {cmd}")
json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=2)
