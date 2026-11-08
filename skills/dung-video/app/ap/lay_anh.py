#!/usr/bin/env python3
"""ẢNH MINH HOẠ — bước sau khi Claude chọn ảnh: lay_anh.py <dự án> <W>
W/chon-anh.json {"chon": {"01": 3, "02": -1}} → openverse.py fetch các ảnh được chọn → motion/public/photos/<key>.jpg.
Ảnh -1 (không có ảnh tốt) → bỏ `photo` khỏi scenes.js, cảnh giữ biểu tượng dự phòng. Ghi nguon-anh.txt (dán vào mô tả bài đăng)."""
import json, os, re, subprocess, sys
from pathlib import Path
P, W = Path(sys.argv[1]), Path(sys.argv[2])
S = Path(__file__).resolve().parents[2] / "video-style-edit/scripts"
chon = json.loads((W / "chon-anh.json").read_text())["chon"]
lay = {k: v for k, v in chon.items() if isinstance(v, int) and v >= 0}
q = json.loads((P / "images/queries.json").read_text())
bo = [a["key"] for a in q if a["key"] not in lay]   # Claude không chọn / -1 → giữ biểu tượng
if lay:
    (P / "images/picks.json").write_text(json.dumps(lay))
    subprocess.run(["python3", "-I", str(S / "openverse.py"), "fetch", str(P), str(P / "images/picks.json")], check=True)
    bo += [k for k in lay if not (P / f"motion/public/photos/{k}.jpg").exists()]
f = P / "motion/src/scenes.js"; s = f.read_text(encoding="utf-8")
i = s.index("export const SCENES = ") + len("export const SCENES = "); j = s.index("\n];", i) + 2
bo_ten = {f"{k}.jpg" for k in bo}
def go(o):   # bỏ ảnh không lấy được, giữ biểu tượng dự phòng
    if isinstance(o, list): return [go(x) for x in o]
    if isinstance(o, dict): return {k: go(v) for k, v in o.items() if not (k == "photo" and v in bo_ten)}
    return o
f.write_text(s[:i] + json.dumps(go(json.loads(s[i:j])), ensure_ascii=False, indent=1) + s[j:], encoding="utf-8")
cr = P / "images/credits.tsv"
if cr.exists():
    dong = [l.split("\t", 1)[1] for l in cr.read_text().splitlines() if l.split("\t")[0] in lay and l.strip()]
    (P / "nguon-anh.txt").write_text("Nguồn ảnh:\n" + "\n".join("- " + d for d in dong) + "\n", encoding="utf-8")
print(f"lấy {len(lay) - len([k for k in bo if k in lay])} ảnh · bỏ {len(bo)} (giữ biểu tượng)")
