#!/usr/bin/env python3
"""SOÁT HÌNH VLOG: ap_soat_hinh.py <dự án> <soat-hinh.json> — Claude đã xem check/segs/*.jpg (1 khung/giây mỗi đoạn giữ) và chỉ ra
đoạn hình hỏng (lật/xoay/quay loạn — thứ máy không dò được) → thêm vào `drop` của clip trong plan.json → chạy lại vlog_edl.py."""
import json, subprocess, sys
from pathlib import Path
from hl_chung import S, ENV
P = Path(sys.argv[1]); kh = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
f = P / "plan.json"; plan = json.loads(f.read_text(encoding="utf-8")); n = 0
for b in kh.get("bo", []):
    for x in plan.get("clips", []):
        if x.get("c") == b["c"] and not x.get("montage"):
            x.setdefault("drop", []).append([b["from"], b["to"]]); x["note"] = (x.get("note", "") + f" · bỏ {b['from']}–{b['to']}: {b.get('ly_do', '')}").strip(" ·"); n += 1
            break
f.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Bỏ thêm {n} đoạn hình hỏng")
if n: subprocess.run(["python3", "-I", str(S / "vlog_edl.py"), str(P)], env=ENV, check=True)
