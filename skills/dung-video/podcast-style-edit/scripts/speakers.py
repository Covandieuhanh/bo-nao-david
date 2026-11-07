#!/usr/bin/env python3
"""Ai đang nói: speakers.py <dự án> [số người; bỏ trống hoặc 0 = tự đếm]
CÁCH CHÍNH (07/11/2026): pyannote speaker-diarization-3.1 (diarize.py, venv ~/.venvs/pyannote) — tách người theo dấu vân giọng,
tự đếm số người; mỗi đoạn lời nhận người có thời gian trùng nhiều nhất, độ chắc = tỉ lệ trùng. Thiếu venv / mô hình / lỗi → cách dự phòng dưới.
DỰ PHÒNG: chia lời thành từng đoạn theo chỗ ngắt (words.srt, nghỉ ≥ 0,35 s), đo đặc trưng giọng mỗi đoạn (cao độ, phổ mel, kênh trái/phải
nếu thu stereo tách người) → gom 2 nhóm (k-means) → motion/src/speakers.js {count, turns:[{start,end,spk}]} + check/speakers.md
(mỗi đoạn: người, độ chắc, lời). Người nói đầu tiên = 0. Đoạn '?' (độ chắc thấp) → đọc lời để quyết, sửa speakers.js.
Đây là ước đoán theo giọng: hai giọng cùng giới, cùng âm sắc dễ lẫn — luôn đọc lại bảng."""
import json, os, re, subprocess, sys
import numpy as np

P = os.path.expanduser(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 0
SR = 16000
def srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+) --> (\d+):(\d+):(\d+)[,.](\d+)\s*\n(.*)", b, re.S)
        if m:
            g = [int(x) for x in m.groups()[:8]]
            out.append((g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000, g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000, m.group(9).strip()))
    return out

words = [w for w in srt(os.path.join(P, "check/goc/words.srt")) if w[2]]
chunks, cur = [], []
for w in words:
    if cur and (w[0] - cur[-1][1] >= 0.35 or cur[-1][1] - cur[0][0] >= 8):
        chunks.append(cur); cur = []
    cur.append(w)
if cur: chunks.append(cur)
segs = [(c[0][0], c[-1][1], " ".join(x[2] for x in c)) for c in chunks if c[-1][1] - c[0][0] >= 0.15]

def load(ch):
    raw = subprocess.run(["/opt/homebrew/bin/ffmpeg", "-v", "error", "-i", os.path.join(P, "davinci/media/audio.wav"), "-ac", str(ch),
                          "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch)
st = load(2); mono = st.mean(1)
# Mel filterbank (24 dải) cho khung 25 ms, bước 10 ms
NF, HOP = 512, 160
mel = lambda f: 2595 * np.log10(1 + f / 700); imel = lambda m: 700 * (10 ** (m / 2595) - 1)
pts = imel(np.linspace(mel(80), mel(7600), 26)); bins = np.floor((NF + 1) * pts / SR).astype(int)
fb = np.zeros((24, NF // 2 + 1))
for i in range(24):
    a, b, c = bins[i], bins[i + 1], bins[i + 2]
    fb[i, a:b] = (np.arange(a, b) - a) / max(1, b - a); fb[i, b:c] = (c - np.arange(b, c)) / max(1, c - b)
win = np.hanning(400)

def feats(a, b):
    x = mono[int(a * SR):int(b * SR)]
    if len(x) < 800: x = np.pad(x, (0, 800 - len(x)))
    fr = np.lib.stride_tricks.sliding_window_view(x, 400)[::HOP] * win
    spec = np.abs(np.fft.rfft(fr, NF)) ** 2
    e = spec.sum(1); keep = e > np.percentile(e, 40)          # bỏ khung lặng/hơi thở
    lm = np.log(spec[keep] @ fb.T + 1e-9)
    # cao độ: tự tương quan trên khung có tiếng, 70–350 Hz
    f0 = []
    for f in fr[keep][::3]:
        ac = np.correlate(f, f, "full")[399:]; lo, hi = SR // 350, SR // 70
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]: f0.append(SR / k)
    s = st[int(a * SR):int(b * SR)]
    lr = np.log((s[:, 0] ** 2).mean() + 1e-9) - np.log((s[:, 1] ** 2).mean() + 1e-9) if len(s) else 0.0
    return np.concatenate([lm.mean(0) - lm.mean(), [np.log(np.median(f0)) if f0 else np.nan, lr]])

F = np.array([feats(a, b) for a, b, _ in segs])
F[:, -2] = np.where(np.isnan(F[:, -2]), np.nanmedian(F[:, -2]), F[:, -2])
Z = (F - F.mean(0)) / (F.std(0) + 1e-6)
Z[:, -2] *= 2.5                                               # cao độ là dấu hiệu mạnh nhất
Z[:, -1] *= 3.0 if np.abs(F[:, -1]).max() > 1.5 else 0.0      # thu stereo tách người → kênh là dấu hiệu chắc chắn
w = np.array([b - a for a, b, _ in segs])

def pyannote():
    py = os.path.expanduser("~/.venvs/pyannote/bin/python")
    if not os.path.exists(py): return None
    src = os.path.join(P, "check/goc/audio16k.wav")
    if not os.path.exists(src): src = os.path.join(P, "davinci/media/audio.wav")
    out = os.path.join(P, "check/pyannote.json")
    r = subprocess.run([py, "-I", os.path.join(os.path.dirname(os.path.abspath(__file__)), "diarize.py"), src, out, str(N)],
                       capture_output=True, text=True)
    if r.returncode or not os.path.exists(out):
        print("pyannote lỗi → dùng cách dự phòng:", (r.stderr or r.stdout).strip().splitlines()[-1:]); return None
    d = json.load(open(out)); n = max(1, d["count"])
    lab, conf = np.zeros(len(segs), int), np.zeros(len(segs))
    for i, (a, b, _) in enumerate(segs):
        ov = np.zeros(n)
        for t in d["turns"]: ov[t["spk"]] += max(0.0, min(b, t["end"]) - max(a, t["start"]))
        lab[i] = int(ov.argmax()); conf[i] = ov.max() / max(b - a, 1e-6) if ov.sum() else 0.0
    order = list(dict.fromkeys(lab)); lab = np.array([order.index(x) for x in lab])
    print(f"pyannote: {len(order)} người"); return len(order), lab, np.clip(conf, 0, 1)

DIA = pyannote()
if DIA:
    N, lab, conf = DIA
    N = max(N, 1)
elif N <= 0:
    N = 2                                                     # dự phòng không tự đếm được → mặc định 2 người
if DIA:
    pass
elif N <= 1:
    lab, conf = np.zeros(len(segs), int), np.ones(len(segs))
else:
    best = None
    rng = np.random.default_rng(0)
    for _ in range(20):
        C = Z[rng.choice(len(Z), N, replace=False)]
        for _ in range(50):
            d = ((Z[:, None, :] - C[None]) ** 2).sum(2); l = d.argmin(1)
            C = np.array([np.average(Z[l == j], 0, w[l == j]) if (l == j).any() else C[j] for j in range(N)])
        cost = (d.min(1) * w).sum()
        if best is None or cost < best[0]: best = (cost, l, d)
    _, lab, d = best
    ds = np.sort(d, 1); conf = 1 - ds[:, 0] / (ds[:, 1] + 1e-9)
    # làm mượt: đoạn ngắn < 1 s, kẹp giữa hai đoạn cùng người, độ chắc thấp → theo hai bên
    for i in range(1, len(lab) - 1):
        if lab[i - 1] == lab[i + 1] != lab[i] and w[i] < 1.0 and conf[i] < 0.5: lab[i] = lab[i - 1]
    order = list(dict.fromkeys(lab)); lab = np.array([order.index(x) for x in lab])   # người nói đầu = 0

turns = []
for (a, b, _), s in zip(segs, lab):
    if turns and turns[-1]["spk"] == int(s) and a - turns[-1]["end"] < 1.5: turns[-1]["end"] = round(b, 2)
    else: turns.append({"start": round(a, 2), "end": round(b, 2), "spk": int(s)})
# Mốc từ của Whisper hay trôi qua khoảng lặng ở chỗ đổi người (đã gặp: lệch ~2 s) → dời ranh giới đổi người vào khoảng lặng
# thật dài nhất trong ±2,5 s (đo năng lượng 20 ms: dưới phân vị 15 + 6 dB, kéo dài ≥ 0,3 s)
hop = SR // 50; k = len(mono) // hop
edb = 10 * np.log10((mono[:k * hop].reshape(k, hop) ** 2).mean(1) + 1e-12)
quiet = edb < np.percentile(edb, 15) + 6
sil, i0 = [], None
for i, q in enumerate(np.append(quiet, False)):
    if q and i0 is None: i0 = i
    elif not q and i0 is not None:
        if i - i0 >= 15: sil.append((i0 / 50, i / 50))
        i0 = None
for t0, t1 in zip(turns, turns[1:]):
    if t0["spk"] == t1["spk"]: continue
    b = (t0["end"] + t1["start"]) / 2
    near = [(e - a, (a + e) / 2) for a, e in sil if abs((a + e) / 2 - b) <= 2.5]
    if near:
        _, m = max(near)
        t0["end"] = round(min(t0["end"], m) if m < t0["end"] else m - 0.05, 2)
        t1["start"] = round(m + 0.05, 2)
        t0["end"] = round(min(t0["end"], t1["start"] - 0.05), 2)
open(os.path.join(P, "motion/src/speakers.js"), "w").write(
    "// Lượt nói (podcast) — tự sinh bởi podcast-style-edit/scripts/speakers.py, Claude sửa lại theo nội dung\n"
    f"export default {{count: {N}, turns: [\n" + ",\n".join(f"  {json.dumps(t)}" for t in turns) + "\n]};\n")
fmt = lambda s: f"{int(s // 60)}:{s % 60:04.1f}"
rows = [f"| {fmt(a)}–{fmt(b)} | {s}{'' if c >= 0.25 or N <= 1 else ' ?'} | {c:.2f} | {t[:90]} |" for (a, b, t), s, c in zip(segs, lab, conf)]
open(os.path.join(P, "check/speakers.md"), "w").write("| Thời gian | Người | Độ chắc | Lời |\n|---|---|---|---|\n" + "\n".join(rows) + "\n")
share = [round(float(w[lab == j].sum() / w.sum() * 100)) for j in range(N)]
print(f"{len(segs)} đoạn · {len(turns)} lượt · tỉ lệ nói {share}% · không chắc: {int((conf < 0.25).sum()) if N > 1 else 0}")
