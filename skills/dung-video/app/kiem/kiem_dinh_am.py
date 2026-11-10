"""Đỉnh âm thật của bản cuối ≤ hồ sơ nhac.dinh_dB (−1,5 dB) — chuẩn chung khối 09. Loudnorm một lượt + nén AAC từng cho đỉnh
−1,0 dB mà các phép đo cũ không bắt (vlog thử 10/11/2026). Áp mọi loại video."""
import sys as _s_, os as _o_; _s_.path.insert(0, _o_.path.dirname(_o_.path.abspath(__file__)))   # python -I không tự thấy _chung.py
import re, subprocess, sys
from _chung import ENV, HS, final
f = final(sys.argv[1])
if not f: print("chưa có video-final.mp4"); sys.exit(1)
r = subprocess.run(["ffmpeg", "-nostats", "-i", str(f), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True, env=ENV)
m = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", r.stderr)
if not m: print("không đo được đỉnh"); sys.exit(1)
tp = -120.0 if m[-1] == "-inf" else float(m[-1]); lim = HS["nhac"].get("dinh_dB", -1.5)
print(f"đỉnh thật {tp:.1f} dBTP (chuẩn ≤ {lim})"); sys.exit(0 if tp <= lim + 0.1 else 1)
