"""Ghi hook vào ~/.claude/settings.json để đồng bộ 2 chiều bộ não với GitHub:
- SessionStart: kéo bản mới từ GitHub về (sync.sh --keo)
- SessionEnd: đẩy thay đổi lên (hook-sync.sh, chạy nền)
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
for su_kien, (cmd, dau) in can.items():
    ds = hooks.setdefault(su_kien, [])
    if not any(dau in h.get("command", "") for g in ds for h in g.get("hooks", [])):
        ds.append({"hooks": [{"type": "command", "command": cmd, "timeout": 30}]})
    print(f"Hook {su_kien}: {cmd}")
json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=2)
