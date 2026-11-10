"""Bản cuối không ngắn hơn bản sạch (không mất lời khi ghép)."""
import sys as _s_, os as _o_; _s_.path.insert(0, _o_.path.dirname(_o_.path.abspath(__file__)))   # python -I không tự thấy _chung.py
import re, subprocess, sys
P = sys.argv[1]
import os as _os
from _chung import loai, edl
if loai(P) == "ghep":   # clip ghép: phải đủ dòng thời gian của kịch bản ghép (TOTAL), không mất đoạn khi render
    d = float(edl(P)["TOTAL"])
elif _os.path.exists(P + "/motion/src/project.js"):
    d = float(re.search(r"duration: *([\d.]+)", open(P + "/motion/src/project.js", encoding="utf-8").read()).group(1))
else:
    print("không áp dụng cho loại video này"); sys.exit(0)
r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", P + "/video-final.mp4"], capture_output=True, text=True)
try: v = float(r.stdout.strip())
except ValueError: print("chưa có video-final.mp4"); sys.exit(1)
print(f"bản cuối {v:.1f} s · cần ≥ {d:.1f} s"); sys.exit(0 if v >= d - 0.5 else 1)
