#!/usr/bin/env python3
"""ÁP MỐC CLAUDE CHỌN cho các câu máy không chắc: ap_chon_moc.py <dự án highlight> <chon-moc.json> [--kiem]"""
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import json, sys
from pathlib import Path
H, kp = Path(sys.argv[1]), sys.argv[2]; kiem = "--kiem" in sys.argv
f = H / "phuong-an.json"; pa = json.loads(f.read_text(encoding="utf-8")); kh = json.loads(Path(kp).read_text(encoding="utf-8")); loi = []
op = {o["id"]: o for o in pa["options"]}
for x in kh.get("sua", []):
    o = op.get(x.get("id")); i = x.get("cau", 0) - 1
    if not o or not 0 <= i < len(o["pieces"]): loi.append(f"không có câu {x.get('cau')} của clip {x.get('id')}"); continue
    p = o["pieces"][i]
    for k in ("start", "end"):
        if x.get(k) is not None and abs(x[k] - p[k]) > 3: loi.append(f"{x['id']} câu {i + 1}: {k} {x[k]} lệch quá 3 s so với mốc hiện tại {p[k]}")
    if x.get("start") is not None and x.get("end") is not None and x["end"] <= x["start"]: loi.append(f"{x['id']} câu {i + 1}: end ≤ start")
for l in loi: print("✗", l)
if loi: sys.exit(1)
if kiem: sys.exit(0)
for x in kh.get("sua", []):
    p = op[x["id"]]["pieces"][x["cau"] - 1]
    for k in ("start", "end"):
        if x.get(k) is not None: p[k] = round(x[k], 2)
f.write_text(json.dumps(pa, ensure_ascii=False, indent=1), encoding="utf-8"); print(f"Áp {len(kh.get('sua', []))} mốc Claude chọn")
