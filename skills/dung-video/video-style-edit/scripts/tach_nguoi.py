"""TÁCH NGƯỜI cho cảnh cần lớp người riêng (khối 07, David chốt 10/11/2026): tach_nguoi.py <dự án>
Cảnh 'chusau' (chữ sau người, bóng người) cần một lớp người trong suốt đặt TRÊN chữ. Script này cắt người khỏi nền từng khung
(Vision của macOS, tach_nguoi.swift) → motion/public/nguoi/<id>/00000.png… và ghi số khung vào motion/src/nguoi.js.
Chạy sau khi viết scenes.js và sau mỗi lần sửa mốc cảnh 'chusau'. Không zoom (`nhan` zoom) chồng lên cảnh này: lớp người sẽ lệch.
"""
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from _common import load

P = os.path.abspath(os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else '.'))
M = os.path.join(P, 'motion')
HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.expanduser('~/.cache/dung-video/tach_nguoi')
SRC = os.path.join(HERE, 'tach_nguoi.swift')
if not os.path.exists(BIN) or os.path.getmtime(SRC) > os.path.getmtime(BIN):
    os.makedirs(os.path.dirname(BIN), exist_ok=True)
    subprocess.run(['swiftc', '-O', SRC, '-o', BIN], check=True)

d = load(P)
fps = d['project'].get('fps', 30)
goc = os.path.join(M, 'public', 'goc.mp4')
CAN = ('chusau',)
scenes = [s for s in d['scenes'] if s.get('type') in CAN]
out = {}
for s in scenes:
    o = os.path.join(M, 'public', 'nguoi', s['id'])
    shutil.rmtree(o, ignore_errors=True)
    end = s['end'] + 1.0   # dư 1 s cho phần giữ cảnh sau chữ cuối (giu.js)
    r = subprocess.run([BIN, goc, str(s['start']), str(end), str(fps), o], capture_output=True, text=True, check=True)
    out[s['id']] = int(r.stdout.strip().splitlines()[-1])
    print(f"{s['id']}: {out[s['id']]} khung")
with open(os.path.join(M, 'src', 'nguoi.js'), 'w') as f:
    f.write('// Số khung lớp người đã tách cho từng cảnh (scripts/tach_nguoi.py) — tự sinh, đừng sửa tay\n')
    f.write('export default ' + json.dumps(out, ensure_ascii=False) + ';\n')
if not scenes: print('không có cảnh cần tách người')
