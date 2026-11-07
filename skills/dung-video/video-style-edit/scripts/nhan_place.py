#!/usr/bin/env python3
"""Vị trí mặt cho cảnh ĐIỂM NHẤN TRÊN NGƯỜI (type 'nhan' — David chốt 2026-11-07): nhan_place.py <dự án>
Đọc check/faces/faces.json (face_place.sh, 2 khung/giây, toạ độ 0–1 tính từ góc trên trái) + scenes.js
→ motion/src/mat.js {<id>: {cx, cy, w, h}} = mặt lớn nhất, trung vị trong suốt cảnh.
Nhan.jsx đọc file này để đặt chữ / biểu tượng cạnh mặt; render_preview.py đọc để zoom dồn đúng vào mặt.
Cảnh không thấy mặt → giữa khung hơi cao (0.5, 0.42)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load

P = os.path.expanduser(sys.argv[1])
scenes = [s for s in load(P)["scenes"] if s.get("type") == "nhan"]
fj = os.path.join(P, "check/faces/faces.json")
frames = json.load(open(fj)) if os.path.exists(fj) else []
STEP = 0.5
med = lambda v: sorted(v)[len(v) // 2]
res = {}
for s in scenes:
    boxes = []
    for i in range(int(s["start"] / STEP), min(len(frames), int(s["end"] / STEP) + 1)):
        if frames[i]: boxes.append(max(frames[i], key=lambda f: f["w"] * f["h"]))
    if boxes:
        res[s["id"]] = {"cx": round(med([b["x"] + b["w"] / 2 for b in boxes]), 4), "cy": round(med([b["y"] + b["h"] / 2 for b in boxes]), 4),
                        "w": round(med([b["w"] for b in boxes]), 4), "h": round(med([b["h"] for b in boxes]), 4),
                        # khoảng mặt xê dịch trong cả cảnh (selfie vừa đi vừa quay): mép trái 10%, mép phải 90% → chữ đặt ngoài khoảng này
                        "l": round(sorted(b["x"] for b in boxes)[len(boxes) // 10], 4),
                        "r": round(sorted(b["x"] + b["w"] for b in boxes)[min(len(boxes) - 1, len(boxes) * 9 // 10)], 4)}
    else:
        res[s["id"]] = {"cx": 0.5, "cy": 0.42, "w": 0.18, "h": 0.3, "khong_mat": True}
open(os.path.join(P, "motion/src/mat.js"), "w").write(
    "// Mặt người nói trong từng cảnh điểm nhấn (type 'nhan') — tự sinh bởi scripts/nhan_place.py, toạ độ 0–1\n"
    "export default " + json.dumps(res, ensure_ascii=False, indent=1) + ";\n")
print(f"điểm nhấn trên người: {len(res)} cảnh" + "".join(f" · {k} (không thấy mặt)" for k, v in res.items() if v.get("khong_mat")))
