#!/usr/bin/env python3
"""In "ranh" nếu app Claude không có phiên nào hoạt động trong N phút qua (mặc định 30), để mở lại app không cắt ngang việc đang làm.
Đọc lastActivityAt trong các file phiên app (chỉ đọc mốc giờ). Dùng: python3 -I app-ranh.py [phút]"""
import glob, json, os, sys, time
phut = int(sys.argv[1]) if len(sys.argv) > 1 else 30
moi = 0
for f in glob.glob(os.path.expanduser("~/Library/Application Support/Claude/claude-code-sessions/*/*/local_*.json")):
    try:
        if time.time() - os.path.getmtime(f) > 86400:
            continue
        d = json.load(open(f, encoding="utf-8"))
        moi = max(moi, (d.get("lastActivityAt") or 0) / 1000, os.path.getmtime(f))
    except (OSError, ValueError):
        pass
print("ranh" if time.time() - moi > phut * 60 else "ban")
