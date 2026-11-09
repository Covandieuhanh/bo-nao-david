"""Bản cuối không ngắn hơn bản sạch (không mất lời khi ghép)."""
import re, subprocess, sys
P = sys.argv[1]
import os as _os
if not _os.path.exists(P + "/motion/src/project.js"): print("không áp dụng cho loại video này (clip ghép)"); sys.exit(0)
d = float(re.search(r"duration: *([\d.]+)", open(P + "/motion/src/project.js", encoding="utf-8").read()).group(1))
r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", P + "/video-final.mp4"], capture_output=True, text=True)
try: v = float(r.stdout.strip())
except ValueError: print("chưa có video-final.mp4"); sys.exit(1)
print(f"bản cuối {v / 60:.1f} phút · bản sạch {d / 60:.1f} phút"); sys.exit(0 if v >= d - 0.5 else 1)
