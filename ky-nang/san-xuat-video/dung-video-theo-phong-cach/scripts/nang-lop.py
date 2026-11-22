#!/usr/bin/env python3
"""NÂNG KHUNG (người dùng chốt): nhân vật/vật chính nằm thấp (nửa dưới khung dọc) → đẩy hình lên để người nằm trong vùng an toàn,
không bị phụ đề/thanh nút nền tảng che. Đáy hở lấp bằng chính hình đó làm mờ.

  nang-lop.py <dự án ghép>            → chuyen-dong/src/nang-lop.js  {idĐoạn: {y, s}} + kiem-tra/khuon-mat/lift.md   (chế độ ghép; chuong-trinh.jsx tự đọc)
  nang-lop.py <dự án 1 video> apply   → nung vào tu-lieu/video-goc.mp4 (giữ bản trước là video-goc-truoc-nang.mp4)
                                     + kiem-tra/khuon-mat/lift.md; chạy sau 3a/3b, TRƯỚC 3c và vi-tri-khuon-mat.sh
  nang-lop.py <dự án 1 video>         → chỉ in kế hoạch (không nung)

Luật tính (khung 1080×1920): tâm mặt nên ở ~800 px, cằm không xuống quá 1240 (trên dải phụ đề 1280), đỉnh đầu không lên quá 230.
  y = max(tâm − 800, cằm − 1240), làm tròn 10 px, < 80 px thì bỏ; tối đa 400 px. Cần hơn 400 → phóng thêm s (≤ 1,25×, gốc
  phóng ở mép trên). Không thấy mặt (đoạn quay đồ vật, cầu thang…) → không tự nâng; đặt tay `lift: {y: 200}` trong danh-sach-cat.js.
"""
import json, os, re, subprocess, sys
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.realpath(__file__)))
from _chung import ma_hoa_h264   # bộ mã hoá theo máy (Mac / NVIDIA / CPU)

P = Path(sys.argv[1]).expanduser()
MODE = sys.argv[2] if len(sys.argv) > 2 else 'plan'
W, H = 1080, 1920
TARGET, CHIN_MAX, TOP_MIN, MAX_Y, MAX_S = 800, 1240, 230, 400, 1.25
SKILL = Path(__file__).resolve().parent.parent
BIN = SKILL / 'scripts/do-mat.sh'   # Vision trên Mac, YuNet + MediaPipe ở máy khác (cùng định dạng)
ENV = {**os.environ, 'PATH': '/opt/homebrew/bin:' + os.environ.get('PATH', '')}


def detect(video, out):
    """Mặt 2 khung/giây → out (list theo khung, mỗi khung list {x,y,w,h} chuẩn hoá, gốc trên-trái). Có rồi thì dùng lại."""
    if out.exists() and out.stat().st_mtime >= video.stat().st_mtime:
        return json.loads(out.read_text())
    d = out.with_suffix('')
    subprocess.run(['rm', '-rf', str(d)], check=True); d.mkdir(parents=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vf', 'fps=2,scale=360:-2', '-q:v', '5',
                    str(d / 'f_%05d.jpg')], check=True, env=ENV)
    subprocess.run(['zsh', str(BIN), str(d), str(out)], check=True, env=ENV)
    subprocess.run(['rm', '-rf', str(d)], check=True)
    return json.loads(out.read_text())


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))]


def need(frames):
    """frames: list khung (mỗi khung list mặt). Trả (y, s, ghi chú) hoặc None khi không đủ mặt."""
    boxes = [max(fs, key=lambda f: f['w'] * f['h']) for fs in frames if fs]   # mặt to nhất = nhân vật chính
    if len(boxes) < max(2, 0.25 * len(frames)):
        return None
    cy = pct([(f['y'] + f['h'] / 2) * H for f in boxes], .7)
    chin = pct([(f['y'] + 1.06 * f['h']) * H for f in boxes], .9)
    top = pct([(f['y'] - 0.4 * f['h']) * H for f in boxes], .1)
    y = max(cy - TARGET, chin - CHIN_MAX, 0)
    y = min(y, max(0, top - TOP_MIN))
    s = 1.0
    if y > MAX_Y:                       # phần thiếu bù bằng phóng (gốc trên): điểm cy → s·cy − MAX_Y
        s = min(MAX_S, (TARGET + MAX_Y) / cy)
        y = MAX_Y
    y = int(round(y / 10) * 10)
    if y < 80 and s == 1.0:
        y = 0
    return y, round(s, 3), f'tâm mặt {cy:.0f} · cằm {chin:.0f} · đỉnh đầu {top:.0f}'


def montage():
    edl = P / 'chuyen-dong/src/danh-sach-cat.js'
    js = f"import('file://{edl}').then(m => console.log(JSON.stringify(m.SEGS)))"
    segs = json.loads(subprocess.run(['node', '--input-type=module', '-e', js], capture_output=True, text=True,
                                     check=True, env=ENV).stdout)
    out, rows = {}, []
    for s in segs:
        why = None
        if 'cite' in s:
            why = 'trích dẫn (khung bo góc, không nâng)'
        elif s.get('fit'):
            why = 'nền mờ sẵn'
        elif s.get('grade') == 'title':
            why = 'nền tiêu đề'
        elif s.get('lift'):
            why = f"đặt tay y {s['lift'].get('y', 0)} · s {s['lift'].get('s', 1)}"
        if why:
            rows.append((s['id'], '—', why)); continue
        clip = P / f"chuyen-dong/public/doan-video/{s['clip']}.mp4"
        fr = detect(clip, P / f"kiem-tra/khuon-mat/{s['clip']}.json")
        a, b = s['from'], s['from'] + (0 if s.get('freeze') else s['dur'] * s['rate'])
        sub = [fr[i] for i in range(len(fr)) if a - 0.25 <= i / 2 <= b + 0.25] or fr[int(a * 2):int(a * 2) + 1]
        r = need(sub)
        if not r:
            rows.append((s['id'], '0', 'không thấy mặt → nâng tay nếu vật chính nằm thấp')); continue
        y, sc, note = r
        if y or sc > 1:
            out[s['id']] = {'y': y, **({'s': sc} if sc > 1 else {})}
        rows.append((s['id'], f'{y}' + (f' · ×{sc}' if sc > 1 else ''), note))
    (P / 'chuyen-dong/src/nang-lop.js').write_text(
        '// Nâng khung từng đoạn {idĐoạn: {y: px đẩy lên, s: phóng}} — tự sinh bởi scripts/nang-lop.py; đặt tay: `lift` trong danh-sach-cat.js\n'
        f'export default {json.dumps(out, ensure_ascii=False)};\n')
    report(rows)


def single():
    v = P / 'tu-lieu/video-goc.mp4'
    src = P / 'tu-lieu/video-goc-truoc-nang.mp4'
    base = src if src.exists() else v                       # chạy lại → tính từ bản chưa nâng
    w, h = map(int, subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height',
                                    '-of', 'csv=p=0', str(base)], capture_output=True, text=True, env=ENV).stdout.strip().split(','))
    if (w, h) != (W, H):
        sys.exit(f'chỉ nâng khung dọc {W}×{H} (video {w}×{h})')
    fr = detect(base, P / 'kiem-tra/khuon-mat/lift_faces.json')
    # Cửa sổ 4 s: một mức nâng mỗi cửa sổ (bậc 100 px) → gộp cửa sổ cùng mức; đổi mức trượt 0,6 s (không giật)
    win, levels = 8, []
    for i in range(0, len(fr), win):
        r = need(fr[i:i + win])
        levels.append(min(MAX_Y, int(round((r[0] if r else 0) / 100) * 100)))
    for i in range(1, len(levels) - 1):                     # bỏ cửa sổ lẻ loi (1 cửa sổ khác hẳn hai bên)
        if levels[i - 1] == levels[i + 1] != levels[i]:
            levels[i] = levels[i - 1]
    runs = []
    for i, L in enumerate(levels):
        t = i * win / 2
        if runs and runs[-1][1] == L:
            continue
        runs.append((t, L))
    rows = [(f'{t:.1f}s', str(L), '') for t, L in runs]
    report(rows)
    if all(L == 0 for _, L in runs):
        print('không cần nâng'); return
    if MODE != 'apply':
        return
    ramp = 0.6
    expr, prev = '0', 0
    for t, L in runs:
        if L != prev:
            t0 = max(0, t - ramp / 2)
            expr += f'+({L - prev})*clip((t-{t0:.2f})/{ramp},0,1)'
            prev = L
    if not src.exists():
        v.rename(src)
    fc = (f"[0:v]split[a][b];[a]scale={W}:{H},boxblur=30:2,eq=brightness=-0.08[bg];"
          f"[bg][b]overlay=x=0:y='-({expr})':eval=frame,format=yuv420p[v]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-filter_complex', fc, '-map', '[v]', '-map', '0:a?',
                    *ma_hoa_h264('20M'), '-c:a', 'copy', '-movflags', '+faststart', str(v)],
                   check=True, env=ENV)
    print('đã nung →', v)


def report(rows):
    md = P / 'kiem-tra/khuon-mat/lift.md'
    md.parent.mkdir(parents=True, exist_ok=True)
    md.write_text('# Nâng khung\n\n| Đoạn / mốc | Nâng (px) | Ghi chú |\n|---|---|---|\n'
                  + ''.join(f'| {a} | {b} | {c} |\n' for a, b, c in rows))
    print(md.read_text())


(montage if (P / 'chuyen-dong/src/danh-sach-cat.js').exists() else single)()
