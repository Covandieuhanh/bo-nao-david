# Dò đoạn HỎNG trong các clip của dự án ghép: khung-loi.py <dự án> [c1 c2 …]
# Mỗi 0,5 s đo độ sáng (YAVG) và độ tương phản (YHIGH − YLOW) trên bản thu nhỏ.
#   TÚI/CHE  tương phản < 60 (khung một màu: trong túi, ngón tay che ống kính, áp vào người). Ngưỡng 30 cũ bỏ sót túi màu hồng
#            (c13 vlog leo núi: 20–39); clip quay thường không khung nào dưới 60 (đo 10 clip 2026-11-04).
#   Khoảng hỏng cách nhau < 1 s gộp làm một.
#   TỐI      YAVG < 28
#   (Không dò RUNG theo YDIF: selfie vừa đi vừa quay thì 2 khung cách 0,5 s luôn khác nhau → gắn nhầm ~90% clip — vlog leo núi
#   2026-11-03. Rung/nhoè soát bằng mắt trên half_XX.jpg.)
# Ghi check/cN/bad.txt (từng khoảng ≥ 1 s + lý do) và in bảng tổng. Chỉ là gợi ý: đoạn có lời/cảm xúc vẫn giữ (multi-clip.md 2c) —
# đối chiếu loud.txt + transcript + half_XX.jpg trước khi bỏ. KHÔNG dò được hình lật ngang/lộn ngược/quay loạn (vừa rút máy khỏi
# túi) → tờ soát check/segs/ của danh-sach-cat-vlog.py. Hình hỏng thì bỏ kể cả có lời.
import os, re, subprocess, sys

P = os.path.expanduser(sys.argv[1])
ids = sys.argv[2:] or sorted((d for d in os.listdir(os.path.join(P, 'check')) if re.fullmatch(r'c\d+', d)), key=lambda x: int(x[1:]))
STEP = 0.5

def stats(clip):
    out = subprocess.run(['ffmpeg', '-v', 'error', '-i', clip, '-vf', 'fps=2,scale=270:-2,signalstats,metadata=print:file=-',
                          '-f', 'null', '-'], capture_output=True, text=True).stdout
    rows, cur = [], {}
    for l in out.splitlines():
        if l.startswith('frame:'):
            if cur: rows.append(cur)
            cur = {}
        m = re.match(r'lavfi\.signalstats\.(YAVG|YLOW|YHIGH|YDIF)=([\d.]+)', l)
        if m: cur[m.group(1)] = float(m.group(2))
    if cur: rows.append(cur)
    return rows

def tag(r):
    if r.get('YHIGH', 255) - r.get('YLOW', 0) < 60: return 'TÚI/CHE'
    if r.get('YAVG', 255) < 28: return 'TỐI'
    return None

total_bad = 0.0
print(f"{'clip':5} {'dài':>6}  đoạn hỏng (≥ 1 s)")
for cid in ids:
    clip = os.path.join(P, 'motion/public/clips', cid + '.mp4')
    rows = stats(clip)
    tags = [tag(r) for r in rows]
    runs, i = [], 0
    while i < len(tags):
        if tags[i]:
            j = i
            while j + 1 < len(tags) and tags[j + 1]: j += 1
            a, b = i * STEP, (j + 1) * STEP
            if b - a >= 1.0:
                why = max(set(t for t in tags[i:j + 1] if t), key=tags[i:j + 1].count)
                runs.append((a, b, why))
            i = j + 1
        else: i += 1
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < 1.0: merged[-1] = (merged[-1][0], r[1], merged[-1][2])
        else: merged.append(r)
    runs = merged
    dur = len(rows) * STEP
    bad = sum(b - a for a, b, _ in runs); total_bad += bad
    with open(os.path.join(P, 'check', cid, 'bad.txt'), 'w') as f:
        for a, b, w in runs: f.write(f'{a:.1f}-{b:.1f} {w}\n')
    s = ' · '.join(f'{a:.1f}–{b:.1f} {w}' for a, b, w in runs) or '—'
    print(f'{cid:5} {dur:6.1f}  {s}' + (f'   ({bad / dur:.0%})' if runs else ''))
print(f'Tổng hỏng gợi ý: {total_bad:.0f} s')
