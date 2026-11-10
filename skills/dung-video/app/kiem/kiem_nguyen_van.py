"""Chữ trên màn hình là nguyên văn lời (luat-chung 1) — soát lại scenes.js sau mọi lần sửa tay."""
import sys as _s_, os as _o_; _s_.path.insert(0, _o_.path.dirname(_o_.path.abspath(__file__)))   # python -I không tự thấy _chung.py
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ap"))
import loi, canh_js
P = sys.argv[1]
import os as _os
from _chung import loai, edl
if loai(P) == "ghep":   # clip ghép: chữ lớp phủ + màn chốt phải có trong lời (SUBS) quanh lúc hiện, hoặc trong cả lời
    E = edl(P); T = []
    for s_ in E.get("SUBS", []):
        tk = loi.chuan(s_["text"]); d_ = (s_["end"] - s_["start"]) / max(1, len(tk))
        T += [(s_["start"] + i * d_, s_["start"] + (i + 1) * d_, k) for i, k in enumerate(tk)]
    ds = [(o.get("start", 0), o.get("end", 1e9), o) for o in E.get("OVERLAYS", []) if o.get("type") != "hud"]
    if E.get("CTA"): ds.append((0, 1e9, {"text": E["CTA"]["text"].replace("**", "")}))
    sai = [f"«{t}»" for a, b, o in ds for t in canh_js.chu_tren_man(o)
           if loi.co_trong_loi(t, T, a, b) < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0) < 0.85]
    print(f"{len(ds)} lớp chữ · " + ("mọi chữ nguyên văn" if not sai else "không nguyên văn: " + "; ".join(sai))); sys.exit(1 if sai else 0)
if not _os.path.exists(P + "/motion/src/scenes.js"): print("không áp dụng cho loại video này"); sys.exit(0)
s = Path(P + "/motion/src/scenes.js").read_text(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ap")); import canh_js
S = canh_js.canh(P); T = loi.tu(P + "/check/goc/words.srt"); sai = []
import os
SUA = frozenset(t for x in (json.load(open(P + "/check/app-sua-chu.json")) if os.path.exists(P + "/check/app-sua-chu.json") else [])
                for t in loi.chuan(x.get("dung", "")))
for c in S:
    for t in canh_js.chu_tren_man(c["props"]):
        if loi.co_trong_loi(t, T, c["start"], c["end"], them=SUA) < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0, them=SUA) < 0.85: sai.append(f"{c['id']}: «{t}»")
print(f"{len(S)} cảnh · " + ("mọi chữ nguyên văn" if not sai else "không nguyên văn: " + "; ".join(sai))); sys.exit(1 if sai else 0)
