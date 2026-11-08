"""Âm thanh bản cuối so với bản sạch (khối 17 bước 9): âm lượng giọng chênh ≤ 0,5 dB (đo đoạn trước màn kết, có nhạc nền ~23 dB dưới
giọng nên chênh nhỏ), tiếng rè (dải > 12 kHz) chênh ≤ 1 dB — cao hơn hẳn = âm thanh bị hạ bit ở đâu đó (xem gotchas)."""
import re, subprocess, sys
P = sys.argv[1]
dur = float(re.search(r"duration: *([\d.]+)", open(P + "/motion/src/project.js", encoding="utf-8").read()).group(1))
def do(f, loc):
    r = subprocess.run(["ffmpeg", "-nostats", "-t", f"{dur:.2f}", "-i", f, "-vn", "-af", loc, "-f", "null", "-"], capture_output=True, text=True).stderr
    return r
def mean(f): m = re.findall(r"mean_volume: (-?[\d.]+) dB", do(f, "volumedetect")); return float(m[-1]) if m else None
def re_(f): m = re.findall(r"RMS level dB: (-?[\d.]+|-inf)", do(f, "highpass=f=12000,astats=measure_perchannel=none")); return float(m[-1]) if m and m[-1] != "-inf" else -120.0
g, c = P + "/davinci/media/video_goc.mp4", P + "/video-final.mp4"
import os
if not os.path.exists(g): print("không còn bản sạch (đã dọn tập) — bỏ qua"); sys.exit(0)
a, b = mean(g), mean(c)
if a is None or b is None: print("không đo được"); sys.exit(1)
ra, rb = re_(g), re_(c)
print(f"âm lượng gốc {a:.1f} dB → bản cuối {b:.1f} dB · tiếng rè {ra:.1f} → {rb:.1f} dB")
sys.exit(0 if rb - ra <= 1.0 else 1)
