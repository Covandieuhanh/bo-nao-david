#!/usr/bin/env python3
"""Cài lịch app Claude từ repo vào tài khoản app đang mở (thư mục phiên app ghi gần nhất).
Mỗi việc trong lich-app.json: lời giao lấy ở loi-giao/<id>.md (nối tắt vào ~/.claude/scheduled-tasks/<id>/SKILL.md), giờ theo cronExpression.
Id trong 'bo' thì gỡ khỏi app. Chạy lại bao nhiêu lần cũng được. Dùng: python3 -I cai-lich-app.py [--tat-ca]
--tat-ca: cài vào mọi tài khoản app trên máy (mặc định chỉ tài khoản đang mở)."""
import glob, json, os, sys, time

GOC = os.path.dirname(os.path.abspath(__file__))
NAO = os.path.dirname(os.path.dirname(GOC))
H = os.path.expanduser("~")
cfg = json.load(open(os.path.join(GOC, "lich-app.json"), encoding="utf-8"))

thu_muc = sorted(glob.glob(os.path.join(H, "Library/Application Support/Claude/claude-code-sessions/*/*/")), key=os.path.getmtime, reverse=True)
if not thu_muc:
    print("Chưa có tài khoản app Claude nào trên máy."); sys.exit(0)
if "--tat-ca" not in sys.argv:
    thu_muc = thu_muc[:1]

for v in cfg["viec"]:
    d = os.path.join(H, ".claude/scheduled-tasks", v["id"]); os.makedirs(d, exist_ok=True)
    dich, nguon = os.path.join(d, "SKILL.md"), os.path.join(GOC, "loi-giao", v["id"] + ".md")
    if os.path.islink(dich) or os.path.exists(dich):
        if os.path.realpath(dich) != os.path.realpath(nguon):
            os.remove(dich)
    if not os.path.exists(dich):
        os.symlink(nguon, dich)

for tm in thu_muc:
    p = os.path.join(tm, "scheduled-tasks.json")
    try:
        d = json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        d = {"scheduledTasks": []}
    ds = [t for t in d.get("scheduledTasks", []) if t.get("id") not in cfg["bo"]]
    co = {t["id"]: t for t in ds}
    for v in cfg["viec"]:
        t = co.get(v["id"])
        if not t:
            t = {"id": v["id"], "enabled": True, "createdAt": int(time.time() * 1000), "permissionMode": "auto", "permissionModeCarried": True}
            ds.append(t)
        t.update(displayName=v["displayName"], cronExpression=v["cronExpression"], cwd=NAO,
                 filePath=os.path.join(H, ".claude/scheduled-tasks", v["id"], "SKILL.md"))
    d["scheduledTasks"] = ds
    json.dump(d, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("Đã cài lịch app:", ", ".join(t["id"] + " " + t["cronExpression"] for t in ds), "→", tm.split("claude-code-sessions/")[1])
