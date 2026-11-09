#!/usr/bin/env python3
"""TỜ HÌNH cho bước Claude duyệt hình (highlight, vlog): to_hinh.py <video> <ra.jpg> [số khung, mặc định 24]
Cắt khung trải đều cả video (bỏ 3% đầu/cuối), ghép lưới 6 cột, ghi mốc giây lên từng khung."""
import os, subprocess, sys
from pathlib import Path
v, ra = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 24
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v], capture_output=True, text=True, env=env).stdout)
tmp = Path(ra).with_suffix(".tmp"); tmp.mkdir(parents=True, exist_ok=True)
for i in range(n):
    t = d * (0.03 + 0.94 * i / max(1, n - 1))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", v, "-frames:v", "1", "-vf",
                    f"scale=360:-2,drawtext=text='{t:.1f}s':x=8:y=8:fontsize=22:fontcolor=white:box=1:boxcolor=black@0.6", str(tmp / f"{i:03d}.jpg")], env=env)
fs = sorted(tmp.glob("*.jpg"))
if not fs:   # ffmpeg Homebrew có thể thiếu drawtext → bỏ chữ mốc
    for i in range(n):
        t = d * (0.03 + 0.94 * i / max(1, n - 1))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", v, "-frames:v", "1", "-vf", "scale=360:-2", str(tmp / f"{i:03d}.jpg")], env=env)
    fs = sorted(tmp.glob("*.jpg"))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "1", "-i", str(tmp / "%03d.jpg"), "-vf", "tile=6x" + str((len(fs) + 5) // 6), "-frames:v", "1", ra], env=env)
for f in fs: f.unlink()
tmp.rmdir(); print(f"{len(fs)} khung → {ra}")
