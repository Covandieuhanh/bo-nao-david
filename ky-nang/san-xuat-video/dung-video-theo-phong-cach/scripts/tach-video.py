# TÁCH MỘT BUỔI NÓI DÀI THÀNH NHIỀU VIDEO THEO HƯỚNG (references/tach-theo-huong.md):  python3 -I tach-video.py <ke-hoach-tach.json>
# Đầu vào: dự án gốc đã làm sạch + chép lời đã soát (tu-lieu/video-goc.mp4 + chuyen-dong/src/phu-de.js) và file kế hoạch:
#   {"nguon": "~/Movies/tap-X/2-ban-day-du", "dem": 0.12,
#    "video": {"<tên>": {"doan": [[giây_đầu, giây_cuối], …], "topic": "MAY ĐO", "tuyen": "kien_thuc", "ytEnd": 20}, …}}
#   Mốc lấy đúng đầu / cuối câu trong phụ đề dự án gốc (cắt giữa hai câu, không cắt giữa từ).
# Mỗi video: cắt + nối các đoạn (đệm `dem` giây, fade âm 50 ms ở điểm nối) → tao-du-an.sh <tên> → ghi du-an.js (topic, tuyen, ytEnd),
# phu-de.js (lấy từ phụ đề gốc, dời mốc theo đoạn cắt — không chép lời lại), canh.js khung sẵn hàm g() (viết mốc theo video GỐC, g() đổi
# sang mốc video đã cắt), ke-hoach-canh.md khung, kiem-tra/tach-video.json (lưu lại đúng kế hoạch đã dùng).
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from _chung import ma_hoa_h264, node_env

SKILL = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
KH = json.load(open(sys.argv[1], encoding='utf-8'))
P0 = os.path.expanduser(KH['nguon'])
SRC = os.path.join(P0, 'tu-lieu', 'video-goc.mp4')
DEM = float(KH.get('dem', 0.12))
TAM = os.path.expanduser('~/Movies/tai-ve/tach-' + os.path.basename(os.path.dirname(P0.rstrip('/'))))
os.makedirs(TAM, exist_ok=True)

s = open(os.path.join(P0, 'chuyen-dong/src/phu-de.js'), encoding='utf-8').read()
s = s[s.index('export default') + len('export default'):].strip().rstrip(';')
SUBS = json.loads(re.sub(r'(\b(?:start|end|text)\b)\s*:', r'"\1":', s))

CANH = '''// Kịch bản cảnh — tap-{ten}: tách từ {goc} (tach-video.py, kiem-tra/tach-video.json).
// Mốc viết theo VIDEO GỐC (dễ đối chiếu phụ đề gốc); g() đổi sang mốc video đã cắt. Mỗi cảnh ghi nguồn kho (huong-dan-lua-chon.md bước 4d).
import project from './du-an.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

const DOAN = {doan}.map(([a, b]) => [a - {dem}, b + {dem}]);
const g = (t) => {{
  let off = 0;
  for (const [a, b] of DOAN) {{ if (t <= b) return +(off + Math.max(0, t - a)).toFixed(3); off += b - a; }}
  return +off.toFixed(3);
}};
// Cảnh tự vẽ trong chỗ trống thật (rieng/duong-may.jsx): ve('id', giây_gốc_đầu, giây_gốc_cuối, {{kieu, …, at: g(giây_gốc)}})
const O = {{x: 0.305, y: 0.062, w: 0.41, h: 0.168}};   // đo lại chỗ trống của video này (khung đầu / giữa / cuối)
const ve = (id, a, b, props) => ({{id, type: 've', start: g(a), end: g(b), props: {{ve: 'DuongMay', o: O, giuPhuDe: true, ...props}}}});
const tg = (f, at, v) => ({{f, at: g(at), v}});

export const SCENES = [
];

export const COVER = null;
export const STAGE = null;
export const TOPICS = [];
export const CHAPTERS = [];
export const GHI_CHU = [];
export const GHI_CHU_O = null;
export const SIDES = null;
'''

for ten, v in KH['video'].items():
    doan = [tuple(x) for x in v['doan']]
    parts = [(max(0.0, a - DEM), b + DEM) for a, b in doan]
    subs, t = [], 0.0
    for (a, b), (a0, b0) in zip(doan, parts):
        for x in SUBS:
            if x['end'] > a + 0.05 and x['start'] < b - 0.05:
                subs.append({'start': round(max(a0, x['start']) - a0 + t, 2), 'end': round(min(b0, x['end']) - a0 + t, 2), 'text': x['text']})
        t += b0 - a0
    fl, cat = [], ''
    for i, (a, b) in enumerate(parts):
        fl.append(f'[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,'
                  f'afade=t=in:d=0.05,afade=t=out:st={b - a - 0.06:.3f}:d=0.06[a{i}]')
        cat += f'[v{i}][a{i}]'
    fl.append(f'{cat}concat=n={len(parts)}:v=1:a=1[v][a]')
    mp4 = os.path.join(TAM, ten + '.mp4')
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', SRC, '-filter_complex', ';'.join(fl), '-map', '[v]', '-map', '[a]',
                    *ma_hoa_h264('20M'), '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', mp4], check=True, env=node_env())
    P = os.path.expanduser(f'~/Movies/tap-{ten}/2-ban-day-du')
    if os.path.exists(P):
        sys.exit(f'{P} đã có — đổi tên video hoặc tự xoá dự án cũ trước (không tự xoá dự án của David)')
    subprocess.run(['zsh', os.path.join(SKILL, 'scripts/tao-du-an.sh'), mp4, '', ten], check=True, env=node_env(), stdout=subprocess.DEVNULL)
    src = os.path.join(P, 'chuyen-dong/src')
    dur = re.search(r'duration: ([\d.]+)', open(os.path.join(src, 'du-an.js'), encoding='utf-8').read()).group(1)
    them = ''.join(f", {k}: {json.dumps(v[k], ensure_ascii=False)}" for k in ('topic', 'tuyen', 'ytEnd') if k in v)
    open(os.path.join(src, 'du-an.js'), 'w', encoding='utf-8').write(
        f"// Thông số video gốc (tách từ {P0} — tach-video.py); topic/tuyen/ytEnd lấy từ kiem-tra/tach-video.json\n"
        f"export default {{fpsNum: 60000, fpsDen: 1001, width: 1920, height: 1080, duration: {dur}, source: 'video-goc.mp4'{them}}};\n")
    # fps/khung lấy đúng từ dự án gốc
    goc = open(os.path.join(P0, 'chuyen-dong/src/du-an.js'), encoding='utf-8').read()
    for k in ('fpsNum', 'fpsDen', 'width', 'height'):
        m = re.search(rf'{k}: (\d+)', goc)
        if m:
            p = os.path.join(src, 'du-an.js'); c = open(p, encoding='utf-8').read()
            open(p, 'w', encoding='utf-8').write(re.sub(rf'{k}: \d+', f'{k}: {m.group(1)}', c, count=1))
    open(os.path.join(src, 'phu-de.js'), 'w', encoding='utf-8').write(
        f'// Phụ đề lấy từ {P0} (đã soát chữ, khớp tiếng), dời mốc theo các đoạn cắt (tach-video.py)\nexport default '
        + re.sub(r'"(start|end|text)":', r'\1:', json.dumps(subs, ensure_ascii=False, indent=1)) + ';\n')
    open(os.path.join(src, 'canh.js'), 'w', encoding='utf-8').write(
        CANH.format(ten=ten, goc=P0, doan=json.dumps([list(x) for x in doan]), dem=DEM))
    open(os.path.join(P, 'ke-hoach-canh.md'), 'w', encoding='utf-8').write(
        f"# Kế hoạch cảnh — tap-{ten}\n\nTách từ {P0}: đoạn (giây video gốc) {doan}. Dài {float(dur):.1f} s.\n\n"
        "## Chẩn đoán (thiet-ke-bo-cuc/huong-dan-lua-chon.md)\nYêu cầu: …\nKhuôn: …\nLoại: …\nHình: …\nThẩm mỹ: …\nTiết chế: …\nĐổi hiệu ứng: …\nNguồn kho: …\n")
    os.makedirs(os.path.join(P, 'kiem-tra'), exist_ok=True)
    json.dump({'nguon': KH['nguon'], 'dem': DEM, 'video': {ten: v}}, open(os.path.join(P, 'kiem-tra/tach-video.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'{ten}: {float(dur):.1f} s · {len(subs)} dòng phụ đề · {P}')
