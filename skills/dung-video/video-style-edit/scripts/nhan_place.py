#!/usr/bin/env python3
"""VỊ TRÍ NGƯỜI cho mọi cảnh 'nhan' và 'bocuc' (David chốt 2026-11-07, nâng 08/11: nhiều người + ai đang nói): nhan_place.py <dự án>
Đọc check/faces/faces.json (face_place.sh: mọi mặt, 2 khung/giây, có độ mở miệng m) + scenes.js
→ motion/src/mat.js, mỗi cảnh:
   cx, cy, w, h, l, r  = mặt NGƯỜI ĐANG NÓI (hoặc người props.bam) — render_preview.py zoom dồn vào người này
   nguoi: [{cx, cy, w, h, l, r, t, b, noi, uoc?}]  = MỌI người trong khung, trái → phải (uoc = máy không thấy rõ mặt
          trong cảnh, vd quay nghiêng → lấy chỗ ngồi quen của người đó; người vẫn ở đó, graphic vẫn phải tránh)
   vung: {l, r, t, b}  = vùng chứa mọi mặt
Số người = số mặt hay gặp trong một khung (≥ 30% khung); gom chỗ ngồi bằng k-means theo bề ngang (máy quay đứng yên).
Có từ 2 người: tự chạy pyannote (podcast-style-edit/scripts/diarize.py, venv ~/.venvs/pyannote) → check/ai_noi.json, rồi
ghép giọng với người: trong mỗi lượt nói, người có miệng cử động nhiều nhất (so với mức thường của chính người đó) được phiếu.
Thiếu pyannote → người nói = mặt lớn nhất (như cũ). Cảnh không thấy mặt → giữa khung hơi cao.
Graphic đọc file này qua src/lib/cho.js — không đè, không làm mờ bất kỳ ai; không con số vị trí cố định."""
import json, os, subprocess, sys, statistics as st
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load

P = os.path.expanduser(sys.argv[1])
fj = f'{P}/check/faces/faces.json'
F = json.load(open(fj)) if os.path.exists(fj) else []
STEP = 0.5
med = lambda v: sorted(v)[len(v) // 2]
pct = lambda v, q: sorted(v)[min(len(v) - 1, int(len(v) * q))]
cxf = lambda f: f['x'] + f['w'] / 2

# 1. Số người = số mặt hay gặp nhất trong một khung (có ở ≥ 30% khung); gom vị trí ngang bằng k-means một chiều
cnt = [sum(1 for f in fr if f['w'] > 0.03) for fr in F]
K = max([k for k in range(1, 6) if sum(1 for c in cnt if c >= k) >= 0.3 * len(F)] or [1])
allc = sorted(cxf(f) for fr in F for f in fr if f['w'] > 0.03)
centers = [allc[int((i + 0.5) * len(allc) / K)] for i in range(K)] if allc else []
for _ in range(20):
    g = [[] for _ in centers]
    for c in allc: g[min(range(K), key=lambda i: abs(c - centers[i]))].append(c)
    centers = [med(x) if x else centers[i] for i, x in enumerate(g)]
who = lambda f: min(range(len(centers)), key=lambda i: abs(cxf(f) - centers[i])) if centers else 0

def box(b):
    return {'cx': round(med([cxf(f) for f in b]), 4), 'cy': round(med([f['y'] + f['h'] / 2 for f in b]), 4),
            'w': round(med([f['w'] for f in b]), 4), 'h': round(med([f['h'] for f in b]), 4),
            'l': round(pct([f['x'] for f in b], 0.1), 4), 'r': round(pct([f['x'] + f['w'] for f in b], 0.9), 4),
            't': round(pct([f['y'] for f in b], 0.1), 4), 'b': round(pct([f['y'] + f['h'] for f in b], 0.9), 4)}
_all = {}
for fr in F:
    for f in fr:
        if f['w'] > 0.03: _all.setdefault(who(f), []).append(f)
GLOBAL = {i: box(b) for i, b in _all.items()}

# 2. Giọng → người (pyannote + cử động miệng)
spk2p = {}
aj = f'{P}/check/ai_noi.json'
V = f'{P}/davinci/media/video_goc.mp4'
DIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../podcast-style-edit/scripts/diarize.py')
PY = os.path.expanduser('~/.venvs/pyannote/bin/python')
if len(centers) > 1 and os.path.exists(V) and os.path.exists(PY) and (not os.path.exists(aj) or os.path.getmtime(V) > os.path.getmtime(aj)):
    wav = f'{P}/check/tieng16k.wav'
    try:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', V, '-ac', '1', '-ar', '16000', wav], check=True,
                       env=dict(os.environ, PATH='/opt/homebrew/bin:' + os.environ.get('PATH', '')))
        subprocess.run([PY, DIA, wav, aj, str(len(centers))], check=True)
    except Exception as e:
        print('⚠ pyannote lỗi — người nói = mặt lớn nhất:', e)
    finally:
        if os.path.exists(wav): os.remove(wav)
if os.path.exists(aj) and len(centers) > 1:
    turns = json.load(open(aj))['turns']
    def act(t):
        ms = {i: [] for i in range(len(centers))}
        for k in range(int(t['start'] / STEP), min(len(F), int(t['end'] / STEP) + 1)):
            for f in F[k]: ms[who(f)].append(f['m'] / max(f['h'], 1e-3))
        return {i: st.pstdev(v) for i, v in ms.items() if len(v) > 2}
    acts = [(t, act(t)) for t in turns]
    base = {i: (med([a[i] for _, a in acts if i in a]) or 1e-6) for i in range(len(centers))}
    votes = {}
    for t, a in acts:
        if len(a) < 2: continue
        win = max(a, key=lambda i: a[i] / base[i])
        votes.setdefault(t['spk'], [0] * len(centers))[win] += t['end'] - t['start']
    # mỗi giọng nhận người mà nó "nghiêng" về nhiều nhất so với các giọng khác
    for s, v in votes.items():
        tot = sum(v) or 1
        spk2p[s] = max(range(len(v)), key=lambda i: v[i] / tot - sum(votes[o][i] / (sum(votes[o]) or 1) for o in votes if o != s) / max(1, len(votes) - 1))
    print('giọng → người:', spk2p, '· tâm người:', [round(c, 2) for c in centers])

    def speaker(a, b):
        dur = {}
        for t in turns:
            o = min(b, t['end']) - max(a, t['start'])
            if o > 0: dur[spk2p.get(t['spk'], 0)] = dur.get(spk2p.get(t['spk'], 0), 0) + o
        return max(dur, key=dur.get) if dur else None
else:
    speaker = lambda a, b: None

# 3. Từng cảnh
scenes = [s for s in load(P)['scenes'] if s.get('type') in ('nhan', 'bocuc', 've', 'chusau')]   # 've' = cảnh tự vẽ (AI tự tránh người bằng lib/cho.js)
res = {}
for s in scenes:
    by = {}
    n = 0
    for k in range(int(s['start'] / STEP), min(len(F), int(s['end'] / STEP) + 1)):
        n += 1
        for f in F[k]:
            if f['w'] > 0.03: by.setdefault(who(f), []).append(f)
    people = []
    for i in range(len(centers)):
        b = by.get(i, [])
        if len(b) >= 0.3 * n: people.append({'i': i, **box(b)})
        elif i in GLOBAL: people.append({'i': i, **GLOBAL[i], 'uoc': True})   # máy không thấy rõ mặt (quay nghiêng) — người vẫn ngồi đó
    if not people:
        res[s['id']] = {'cx': 0.5, 'cy': 0.42, 'w': 0.18, 'h': 0.3, 'khong_mat': True}; continue
    at = (s.get('props') or {}).get('at')
    a, b = (at, min(s['end'], at + 2.5)) if at is not None else (s['start'], s['end'])
    sp = speaker(a, b)
    main = next((p for p in people if p['i'] == sp), None) or max(people, key=lambda p: p['w'] * p['h'])
    bam = (s.get('props') or {}).get('bam')          # graphic nói về một người cụ thể (vd thẻ tên khách) → bám người đó
    if bam in ('trai', 'phai'): main = people[0] if bam == 'trai' else people[-1]
    for p in people: p['noi'] = p is main
    res[s['id']] = {**{k: main[k] for k in ('cx', 'cy', 'w', 'h', 'l', 'r')},
                    'nguoi': [{k: v for k, v in p.items() if k != 'i'} for p in people],
                    'vung': {'l': min(p['l'] for p in people), 'r': max(p['r'] for p in people),
                             't': min(p['t'] for p in people), 'b': max(p['b'] for p in people)}}
open(f'{P}/motion/src/mat.js', 'w').write(
    "// Mọi người trong từng cảnh + người đang nói — tự sinh bởi scripts/nhan_place.py, toạ độ 0–1\n"
    "export default " + json.dumps(res, ensure_ascii=False, indent=1) + ";\n")
for k, v in res.items():
    ng = v.get('nguoi', [])
    print(f"{k}: {len(ng)} người · nói: {'trái' if ng and ng[0].get('noi') and len(ng) > 1 else ('phải' if len(ng) > 1 else '-')}")
