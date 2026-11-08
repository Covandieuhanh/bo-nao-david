"""Âm lượng bản cuối theo chuẩn chung: cả bài −14 LUFS (±1,5)."""
import re, subprocess, sys
f = sys.argv[1] + "/video-final.mp4"
r = subprocess.run(["ffmpeg", "-nostats", "-i", f, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
if not m: print("không đo được (chưa có video-final.mp4?)"); sys.exit(1)
i = float(m[-1]); print(f"{i:.1f} LUFS (chuẩn −14 ±1,5)"); sys.exit(0 if abs(i + 14) <= 1.5 else 1)
