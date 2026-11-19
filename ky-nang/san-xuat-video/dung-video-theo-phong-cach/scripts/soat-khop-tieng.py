#!/usr/bin/env python3
"""SOÁT PHỤ ĐỀ KHỚP TIẾNG (khối 03 + 17, 19/11/2026) — trước render, đo mỗi dòng phụ đề có hiện đúng lúc người nói nói câu đó không.
  soat-khop-tieng.py <video|tiếng> <phu-de.json> [--tu GIÂY] [--den GIÂY] [--sua <ra.json>]
phu-de.json = [[vào, ra, chữ], …] cùng trục giây với file tiếng. Ghi <phu-de>.khop.md (bảng lệch) + mã thoát 1 nếu có dòng lệch > 3 s.
--sua: ghi bản mốc mới (giữ nguyên chữ) — chỉ thay dòng lệch > 3 s, còn lại giữ (mốc chép lời cũng sai ±1–2 s, không tốt hơn bản đã soát).

Vì sao: tập "Marketing là nỗi đau và nhu cầu" (18–19/11) — phụ đề đã soát chữ kỹ nhưng lệch tới 14 s ở chỗ lời người kia chen vào mà
không có phụ đề; soát chữ không bắt được, phải render lại bản 11 phút. Cách đo:
- Chép lời lại theo KHÚC 20 s (bước 15 s, hai lượt lệch nhau 7,5 s), không dùng ngữ cảnh → không bị vòng lặp ảo giác của bản dài.
- Thử bản gốc trước; dính câu ảo "Hãy subscribe cho kênh…" (whisper hay bịa ở chỗ quán ồn) thì thử bản lọc dải tiếng, rồi bản tăng âm.
  Lọc trước không tốt hơn: ở tập trên, bản lọc ảo giác nhiều hơn bản gốc.
- Mỗi mốc lấy từ khúc không ảo giác có tâm gần nhất; ghép chữ phụ đề với chữ chép lại (difflib) → lệch của từng dòng."""
import argparse, difflib, glob, json, os, re, shutil, statistics as st, subprocess, sys, tempfile, unicodedata

ap = argparse.ArgumentParser()
ap.add_argument('nguon'); ap.add_argument('phude')
ap.add_argument('--tu', type=float, default=None); ap.add_argument('--den', type=float, default=None)
ap.add_argument('--sua', default=None); ap.add_argument('--model', default=os.path.expanduser('~/whisper-models/ggml-large-v3-turbo.bin'))
A = ap.parse_args()
norm = lambda s: re.sub(r'[^\w]', '', unicodedata.normalize('NFC', s.lower()))
S = json.load(open(A.phude))
if not S: sys.exit('phụ đề rỗng')
a0 = A.tu if A.tu is not None else max(0, S[0][0] - 2); a1 = A.den if A.den is not None else S[-1][1] + 2
S = [list(x) for x in S if a0 - 0.05 <= x[0] < a1]
tmp = tempfile.mkdtemp(prefix='khop-tieng-')
ff = shutil.which('ffmpeg') or '/opt/homebrew/bin/ffmpeg'; wc = shutil.which('whisper-cli') or '/opt/homebrew/bin/whisper-cli'

def chep(a):
    f = os.path.join(tmp, f'{a:.2f}')
    for af in ('anull', 'highpass=f=150,lowpass=f=3900', 'volume=2,highpass=f=100'):
        subprocess.run([ff, '-v', 'error', '-y', '-ss', f'{a:.2f}', '-t', '20', '-i', A.nguon, '-ac', '1', '-ar', '16000', '-af', af, f + '.wav'])
        subprocess.run([wc, '-m', A.model, '-l', 'vi', '-np', '-mc', '0', '-ml', '1', '-sow', '-ojf', '-of', f, '-f', f + '.wav'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try: d = json.load(open(f + '.json'))
        except Exception: continue
        if not any('subscribe' in t['text'].lower() for t in d['transcription']):
            return [(a + t['offsets']['from'] / 1000, a + t['offsets']['to'] / 1000, norm(t['text'])) for t in d['transcription'] if norm(t['text'])]
    return None   # cả ba bản đều ảo giác → bỏ khúc

CH = {}
for base in (a0, a0 + 7.5):
    a = base
    while a < a1:
        r = chep(a)
        if r is not None: CH[a] = r
        a += 15
shutil.rmtree(tmp, ignore_errors=True)
best = lambda t: min((c for c in CH if c <= t < c + 20), key=lambda c: abs(t - (c + 10)), default=None)
W = sorted(w for c, ws in CH.items() for w in ws if best(w[0]) == c)

sw, own = [], []
for k, (_, _, t) in enumerate(S):
    for w in t.split():
        if norm(w): sw.append(norm(w)); own.append(k)
sm = difflib.SequenceMatcher(None, sw, [w[2] for w in W], autojunk=False); hit = {}
for b in sm.get_matching_blocks():
    for j in range(b.size): hit[b.a + j] = W[b.b + j]
rows, lech = [], []
for k, (a, b, t) in enumerate(S):
    idx = [i for i, o in enumerate(own) if o == k]; m = [i for i in idx if i in hit]
    if len(m) < max(1, 0.6 * len(idx)): continue
    s = hit[m[0]][0] - 0.22 * (m[0] - idx[0]); d = s - a
    rows.append((k, a, s, d, t))
    if abs(d) > 3: lech.append((k, a, s, d, t))
md = [f'# Phụ đề khớp tiếng — {os.path.basename(A.phude)} ({a0:.0f}–{a1:.0f} s)',
      f'{len(S)} dòng · đo được {len(rows)} · lệch trung vị {st.median([r[3] for r in rows]) if rows else 0:+.2f} s · '
      f'lệch 1,5–3 s: {sum(1 for r in rows if 1.5 < abs(r[3]) <= 3)} (sai số chép lời, nghe lại nếu dồn một chỗ) · **lệch > 3 s: {len(lech)}**', '',
      '| giây phụ đề | giây nghe được | lệch | chữ |', '|---|---|---|---|']
md += [f'| {a:.2f} | {s:.2f} | {d:+.2f} | {t} |' for _, a, s, d, t in rows if abs(d) > 1.5]
out = os.path.splitext(A.phude)[0] + '.khop.md'
open(out, 'w', encoding='utf-8').write('\n'.join(md) + '\n'); print('\n'.join(md[:3])); print(out)
if A.sua:
    N = [list(x) for x in S]
    for k, a, s, d, t in lech:
        dur = N[k][1] - N[k][0]; N[k][0] = round(s, 2); N[k][1] = round(s + dur, 2)
    N.sort(key=lambda x: x[0])
    for i in range(len(N) - 1): N[i][1] = round(min(max(N[i][1], N[i][0] + 0.7), N[i + 1][0]), 2)
    json.dump(N, open(A.sua, 'w'), ensure_ascii=False, indent=0); print('→', A.sua, f'(thay {len(lech)} dòng)')
sys.exit(1 if lech else 0)
