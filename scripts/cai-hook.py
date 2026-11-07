"""Ghi hook SessionEnd vào ~/.claude/settings.json để tự đẩy bộ não lên GitHub khi phiên kết thúc. Chạy lại nhiều lần không bị trùng.
Dùng: python3 -I scripts/cai-hook.py <đường dẫn repo>"""
import json, os, sys
repo = os.path.abspath(sys.argv[1])
cmd = f'bash "{repo}/scripts/hook-sync.sh"'
p = os.path.expanduser("~/.claude/settings.json")
cfg = json.load(open(p)) if os.path.exists(p) else {}
ds = cfg.setdefault("hooks", {}).setdefault("SessionEnd", [])
if not any(h.get("command", "").endswith('/scripts/hook-sync.sh"') for g in ds for h in g.get("hooks", [])):
    ds.append({"hooks": [{"type": "command", "command": cmd}]})
json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=2)
print("Hook SessionEnd:", cmd)
