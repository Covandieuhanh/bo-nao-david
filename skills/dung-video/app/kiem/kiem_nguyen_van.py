"""Chữ trên màn hình là nguyên văn lời (luat-chung 1) — soát lại scenes.js sau mọi lần sửa tay."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ap"))
import loi, ap_canh
P = sys.argv[1]
import os as _os
if not _os.path.exists(P + "/motion/src/scenes.js"): print("không áp dụng cho loại video này (clip ghép)"); sys.exit(0)
s = Path(P + "/motion/src/scenes.js").read_text(encoding="utf-8")
i = s.index("export const SCENES = ") + len("export const SCENES = "); j = s.index("\n];", i) + 2
S = json.loads(s[i:j]); T = loi.tu(P + "/check/goc/words.srt"); sai = []
import os
SUA = frozenset(t for x in (json.load(open(P + "/check/app-sua-chu.json")) if os.path.exists(P + "/check/app-sua-chu.json") else [])
                for t in loi.chuan(x.get("dung", "")))
for c in S:
    for t in ap_canh.chu_tren_man(c["props"], []):
        if loi.co_trong_loi(t, T, c["start"], c["end"], them=SUA) < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0, them=SUA) < 0.85: sai.append(f"{c['id']}: «{t}»")
print(f"{len(S)} cảnh · " + ("mọi chữ nguyên văn" if not sai else "không nguyên văn: " + "; ".join(sai))); sys.exit(1 if sai else 0)
