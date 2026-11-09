"""Âm thanh bản cuối so với bản sạch (khối 17 bước 9): tiếng rè (dải > 12 kHz) SO VỚI giọng không tăng quá 1 dB — cao hơn hẳn = âm
thanh bị hạ bit ở đâu đó (xem gotchas). Đo tương đối vì bản cuối được kéo cả bài về −14 LUFS (giọng nhỏ kéo lên, luật âm lượng chung):
kéo lên 10 dB thì rè cũng lên 10 dB, không phải lỗi (báo nhầm 09/11/2026 ở img-2888, spa-thuy-moc-huong). Mức −14 LUFS do kiem_am_luong lo."""
import re, subprocess, sys
P = sys.argv[1]
import os as _os
if not _os.path.exists(P + "/motion/src/project.js"): print("không áp dụng cho loại video này (clip ghép)"); sys.exit(0)
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
tang = (rb - b) - (ra - a)   # rè so với giọng: bản cuối trừ bản sạch
print(f"âm lượng {a:.1f} → {b:.1f} dB (kéo {b - a:+.1f}) · rè so với giọng {ra - a:.1f} → {rb - b:.1f} dB ({tang:+.1f})")
sys.exit(0 if tang <= 1.0 else 1)
