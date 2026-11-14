#!/usr/bin/env python3
"""Sóng âm: envelope.py <dự án> → motion/src/envelope.js {fps, v: [0–1 mỗi khung]} (độ lớn tiếng theo khung video, đã làm mượt)."""
import json, os, subprocess, sys
import numpy as np
P = os.path.expanduser(sys.argv[1]); FPS = 30; SR = 48000
raw = subprocess.run(["/opt/homebrew/bin/ffmpeg", "-v", "error", "-i", os.path.join(P, "davinci/media/audio.wav"), "-ac", "1", "-ar", str(SR),
                      "-f", "f32le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32); n = SR // FPS
k = len(x) // n
rms = np.sqrt((x[:k * n].reshape(k, n) ** 2).mean(1) + 1e-12)
db = 20 * np.log10(rms)
lo, hi = np.percentile(db, 10), np.percentile(db, 97)
v = np.clip((db - lo) / max(1e-6, hi - lo), 0, 1) ** 1.4
out = np.zeros_like(v); a = 0.0
for i, t in enumerate(v):            # lên nhanh, xuống chậm — sóng không giật
    a = t if t > a else a * 0.82 + t * 0.18
    out[i] = a
open(os.path.join(P, "motion/src/envelope.js"), "w").write(
    "// Độ lớn tiếng theo khung (podcast, sóng âm) — tự sinh bởi dung-podcast/scripts/envelope.py\n"
    f"export default {{fps: {FPS}, v: {json.dumps([round(float(t), 2) for t in out], separators=(',', ':'))}}};\n")
print(f"envelope.js {len(out)} khung")
