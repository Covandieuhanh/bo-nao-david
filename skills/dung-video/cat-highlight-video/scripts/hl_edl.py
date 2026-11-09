# Viết sẵn kịch bản dựng game show cho highlight NGƯỜI NÓI: hl_edl.py <dự án highlight> <dự án montage> [mã phương án]
# Đầu vào: <H>/phuong-an.json (câu nguyên văn + mốc nguồn đã soát bằng loud_check), <H>/check/goc/words.srt (mốc từ),
# <E>/motion/public/clips/c1.mp4 = video gốc (new_montage.sh <tên> <H>/nguon.*). Mỗi câu có thể có:
#   "tone": "lang" | "soi" (mặc định soi) · "zoom": true (dồn khung chậm suốt câu — cú chốt) · "cta": true (câu dùng cho màn chốt)
# Ghi <E>/motion/src/edl.js: RAW = các câu CẮT CỨNG (David chốt 2026-11-04, chuẩn kênh lớn), khoảng lặng trong câu rút còn
# 0,24 s (pauses.py), đoạn con xen kẽ phóng 1,08× (jump cut); --tua = kiểu cũ có đoạn `jump` 0,4 s chip ⏩ + thanh tập gốc.
# SUBS = phụ đề (giây timeline) theo đúng chữ
# của câu (chia dòng ≤ 7 chữ, ngắt ở dấu phẩy; mốc lấy từ words.srt đã bù độ lệch Whisper), TONE + MUSIC.tracks theo tông,
# CTA = câu kêu gọi cuối (nguyên văn), HL = {src_duration}, ENDCARD = thẻ cuối dẫn về bản đầy đủ khi phuong-an.json có
# "endcard": {"title": "<tên tập gốc>", "speaker": "<tên người nói gốc>"} (chữ của bản gốc). OVERLAYS để trống cho Claude thêm (pow, action…).
import difflib, json, os, re, subprocess, sys, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../khoi")); import hoso   # tham số: dung-video/ho-so
_HS = hoso.load('highlight')
PUNCH = hoso.get(_HS, 'phong_xen_ke', 1.08)

_a = [x for x in sys.argv[1:] if not x.startswith('--')]
H, E = (os.path.expanduser(a) for a in _a[:2]); OID = _a[2] if len(_a) > 2 else None
JUMP, PRE, POST = 0.4, 0.04, 0.08
MUSIC = {'soi': 'soi-1', 'lang': 'lang-1'}           # bài mặc định của kênh (assets/music của skill)
# cân mức các bài về cùng ~ −15 LUFS (đo ebur128 60 s đầu: soi-1 −10,3 · soi-2 −9,1 · lang-1 −15,2 · lang-2 −19,7)
GAIN = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../ho-so/chung.json'), encoding='utf-8'))['nhac']['muc']   # mức cân từng bài: MỘT nguồn ở hồ sơ chung

plan = json.load(open(os.path.join(H, 'phuong-an.json'), encoding='utf-8'))
opt = next(o for o in plan['options'] if OID is None or o['id'] == OID)
pieces = opt['pieces']
clip = os.path.join(E, 'motion/public/clips/c1.mp4')
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip],
                           capture_output=True, text=True).stdout)

def ts(x):
    h, m, s = x.replace(',', '.').split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
words = []
for blk in open(os.path.join(H, 'check/goc/words.srt'), encoding='utf-8').read().split('\n\n'):
    l = blk.strip().split('\n')
    if len(l) >= 3 and l[2].strip():
        a, b = l[1].split(' --> '); words.append((ts(a), ts(b), l[2].strip()))
norm = lambda w: unicodedata.normalize('NFC', re.sub(r'[^\w]', '', w.lower()))

def sub_lines(p):
    toks = p['text'].split()
    ww = [w for w in words if p['start'] - 1.5 <= w[0] <= p['end'] + 0.5]
    sm = difflib.SequenceMatcher(None, [norm(t) for t in toks], [norm(w[2]) for w in ww], autojunk=False)
    t = [None] * len(toks)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): t[a + k] = ww[b + k][0]
    known = [(i, x) for i, x in enumerate(t) if x is not None]
    if not known: known = [(0, p['start'])]
    off = p['start'] - known[0][1]                      # Whisper kéo chữ đầu sớm/muộn → bù cả câu theo mốc đã soát
    span = p['end'] - p['start']
    for i in range(len(toks)):                           # chữ không khớp: nội suy theo vị trí
        if t[i] is None:
            prv = max((k for k in known if k[0] < i), default=(0, known[0][1] - 0.0), key=lambda k: k[0])
            nxt = min((k for k in known if k[0] > i), default=(len(toks), p['end'] - off), key=lambda k: k[0])
            t[i] = prv[1] + (nxt[1] - prv[1]) * (i - prv[0]) / max(1, nxt[0] - prv[0])
    t = [min(p['end'] - 0.3, max(p['start'], x + off)) for x in t]
    # chia dòng theo cụm nghĩa (David chốt 2026-11-08: cụm trọn ý ~5–8 chữ, không nhịp 3 chữ). Quy hoạch động: mỗi dòng 3–10 chữ
    # (gần 6–7 chữ là đẹp), chỗ ngắt tốt nhất là hết câu / sau dấu phẩy, kế đó là trước từ nối; ngắt giữa cụm khác bị phạt nặng.
    # Không ngắt giữa cụm cố định ("rất là"). Dòng > 8 chữ thì ShortLine chia đều 2 cụm.
    CONJ = {'thì', 'mà', 'để', 'nhưng', 'nên', 'hay', 'từ', 'và', 'là', 'không', 'các', 'sẽ', 'trong', 'của', 'với', 'đó', 'khi', 'nếu'}
    LIEN = {'rất', 'cũng', 'chính', 'đó', 'là', 'của', 'các', 'những', 'một', 'cái', 'được', 'bị', 'tự', 'đối', 'câu', 'về', 'mặt'}   # không ngắt NGAY SAU các chữ này
    n = len(toks)
    def cut_cost(i):   # giá ngắt SAU chữ i
        if i == n - 1: return 0
        w, nx = toks[i], toks[i + 1]
        if w[-1] in '.?!' or (len(nx) > 1 and nx[0].isupper()): return 0
        if w[-1] in ',;:': return 0.5
        if norm(w) in LIEN: return 9
        if norm(nx) in CONJ: return 1.5
        return 8
    best = [0.0] + [float('inf')] * n; prev = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - 10), j):
            L = j - i
            c = best[i] + cut_cost(j - 1) + 0.12 * (L - 6.5) ** 2 + (8 if L < 3 and j < n else 0)
            if c < best[j]: best[j], prev[j] = c, i
    lines, j = [], n
    while j > 0: lines.insert(0, list(range(prev[j], j))); j = prev[j]
    out = []
    for j, ln in enumerate(lines):
        a = t[ln[0]]; b = t[lines[j + 1][0]] if j + 1 < len(lines) else p['end']
        out.append((a, max(a + 0.4, b), ' '.join(toks[k] for k in ln).rstrip(',')))
    return out

TUA = '--tua' in sys.argv                            # kiểu cũ: đoạn jump 0,4 s có chip ⏩ + thanh tập gốc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pauses
raw, subs, tones, acc, nseg = [], [], [], 0.0, 0
fr = lambda s: round(s * 30) / 30
for i, p in enumerate(pieces):
    a, b = max(0, p['start'] - PRE), min(dur, p['end'] + POST)
    if i and TUA:
        q = pieces[i - 1]
        raw.append(f"  {{id: 'j{i}', clip: 'c1', from: {min(dur, q['end'] + POST) - 0.04:.2f}, freeze: {JUMP}, vol: 0, jump: {{from: {q['end']:.2f}, to: {p['start']:.2f}}}}},")
        tones.append((acc, acc + JUMP, p.get('tone', 'soi'))); acc += fr(JUMP)
    # cắt cứng + cắt khoảng lặng trong câu (David chốt 2026-11-04, chuẩn kênh lớn); mỗi đoạn con xen kẽ phóng 1,0 / 1,08 để mối
    # cắt thành cú "đẩy máy" (jump cut kiểu Ali Abdaal / Hormozi). Câu `zoom` (cú chốt) giữ nguyên một đoạn, dồn chậm 1 → 1,12.
    parts = [(a, b)] if p.get('zoom') else pauses.split(H, a, b)
    # CẢNH PHẢN ỨNG (David duyệt 2026-11-04, HL-3): "react": {"at": <giây nguồn ngay sau cụm đắt>, "from": <giây nguồn có mặt người
    # nghe/khán giả>, "len": 0.8–1.5} → hình người nghe đè lên, TIẾNG người nói vẫn chạy (audio của đoạn chính)
    rc = p.get('react')
    if rc:
        L = float(rc.get('len', 1.2)); np_ = []
        for x, y in parts:
            if x < rc['at'] < y - 0.2:
                np_ += [(x, rc['at']), ('R', rc['at'], min(y, rc['at'] + L)), (min(y, rc['at'] + L), y)]
            else: np_.append((x, y))
        parts = [q for q in np_ if q[0] == 'R' or q[1] - q[0] > 0.1]
    segmap = []
    for k, part in enumerate(parts):
        if part[0] == 'R':                                # đoạn phản ứng: hình nguồn khác, tiếng của câu đang nói
            _, at, en = part; sid = f"p{i + 1}r"
            raw.append(f"  {{id: '{sid}', clip: 'c1', from: {rc['from']:.2f}, to: {rc['from'] + en - at:.2f}, vol: 0, audio: {{clip: 'c1', from: {at:.2f}, vol: 1}}}},   // phản ứng")
            segmap.append((at, en, acc)); tones.append((acc, acc + fr(en - at), p.get('tone', 'soi'))); acc += fr(en - at)
            continue
        x, y = part
        sid = f"p{i + 1}" + ('' if k == 0 else 'bcdefghijklmnopqrstuvwxyz'[k - 1])
        if p.get('zoom'): z = ", zoomIn: [1, 1.12, 0.5, 0.38]"
        else: z = f", zoomIn: [{PUNCH}, {PUNCH}, 0.5, 0.38]" if nseg % 2 else ''
        nseg += 1
        extra = (", grade: 'lang'" if p.get('tone') == 'lang' else '') + z
        note = f"   // {p.get('role', '')} {int(p['start'] // 60)}:{p['start'] % 60:05.2f} «{p['text'][:50]}…»" if k == 0 else ''
        raw.append(f"  {{id: '{sid}', clip: 'c1', from: {x:.2f}, to: {y:.2f}, vol: 1{extra}}},{note}")
        segmap.append((x, y, acc)); tones.append((acc, acc + fr(y - x), p.get('tone', 'soi'))); acc += fr(y - x)
    def tl(src):                                         # giây nguồn → giây timeline (rơi vào khoảng đã cắt → đầu đoạn kế)
        for x, y, t0 in segmap:
            if src <= y: return t0 + max(0.0, src - x)
        x, y, t0 = segmap[-1]; return t0 + (y - x)
    for x, y, txt in sub_lines(p):
        st, en = tl(x), tl(y)
        subs.append(f"  {{start: {st:.2f}, end: {max(st + 0.4, en):.2f}, text: {json.dumps(txt, ensure_ascii=False)}, hl: []}},")
# gộp tông liền nhau
tr = []
for a, b, k in tones:
    if tr and tr[-1][2] == k: tr[-1][1] = b
    else: tr.append([a, b, k])
# Luật 4 (David chốt 08/11): màn chốt CHỈ khi có câu kêu gọi / giao việc nguyên văn (cta hoặc KEUGOI); không có → kết ở câu chốt ý,
# lặng 1 s rồi thẻ cuối — trước đây luôn lấy câu cuối làm màn chốt (lỗi 09/11/2026, app dựng video)
cta = next((p for p in reversed(pieces) if p.get('cta')), next((p for p in reversed(pieces) if p.get('role') == 'KEUGOI'), None))
moc_cuoi = cta or pieces[-1]
if cta and len(cta.get('cta_text') or cta['text']) > 55:   # màn chốt ≤ 55 ký tự (SKILL.md) — câu dài tràn đè phụ đề (lỗi 08/11/2026)
    print(f"⚠ câu màn chốt {len(cta['text'])} ký tự > 55: ghi \"cta_text\" (vế trọn ý, nguyên văn) vào câu đó trong phuong-an.json")

ec = plan.get('endcard') or {}
endcard = 'null' if not ec.get('title') else json.dumps({'title': ec['title'], 'speaker': ec.get('speaker', ''), 'schedule': ec.get('schedule', ''), 'clip': 'c1',
    'at': round(min(dur - 0.1, moc_cuoi['start'] + 0.5), 2), 'len': 1.8}, ensure_ascii=False)
# Thẻ tít mở đầu (luật 7) + TÍT GHIM suốt clip (HL-1): phuong-an.json option "tit": "<tít ≤ 8 chữ>", "pin": false để tắt ghim
tit = opt.get('tit', '')
tit_lines = ''
if tit:
    tit_lines = (f"  {{type: 'pow', start: 0, end: 2.5, text: {json.dumps(tit.upper(), ensure_ascii=False)}, keep: true}},   // thẻ tít mở, neo vùng ngực ngay trên phụ đề để không che mặt (08/11/2026) · khung 0,3 s = ảnh bìa đề xuất\n"
                 + (f"  {{type: 'pinTitle', start: 2.5, end: TOTAL - 4, text: {json.dumps(tit, ensure_ascii=False)}}},   // tít ghim\n" if opt.get('pin', hoso.get(_HS, 'tit_ghim', False)) else ''))
hoso.dump('highlight', os.path.join(E, 'motion/src/hoso.json'))   # khung dựng đọc hồ sơ highlight (cỡ phụ đề nhịp chữ…)
tpl = open(os.path.join(E, 'motion/src/edl.js'), encoding='utf-8').read()
head = tpl[:tpl.index('const RAW = [')]
_endmid = tpl.index('// TS(src)') if '// TS(src)' in tpl else tpl.index('// ===== Phụ đề')   # chạy lại nhiều lần không nhân đôi khối TS
mid = tpl[tpl.index('let acc = 0;'):_endmid]
src = f"""{head}// Viết bởi cat-highlight-video/scripts/hl_edl.py từ {H}/phuong-an.json (phương án {opt['id']}) — Claude chỉnh tiếp.
const RAW = [
{chr(10).join(raw)}
];

{mid}// TS(src): giây trong video gốc → giây timeline (lớp phủ đặt theo lời: TS(<mốc từ trong words.srt>)) — rơi vào khoảng lặng đã cắt → đầu đoạn kế
const PIECES = SEGS.filter((s) => !s.freeze);
export const TS = (src) => {{
  for (const s of PIECES) if (src <= s.to) return s.start + Math.max(0, src - s.from);
  const s = PIECES[PIECES.length - 1]; return s.start + s.dur;
}};

// ===== Phụ đề (giây timeline) — chữ đúng câu nguyên văn trong phuong-an.json; hl = từ khoá tô cam =====
export const SUBS = [
{chr(10).join(subs)}
];
// Video ngắn: phụ đề cụm 5–8 chữ, cỡ bằng chữ thẻ (subStyle.js ShortLine, David chốt 2026-11-08)
export const SHORT = true;

// ===== Lớp đồ hoạ (pow · action · pointer …) — Claude thêm theo nội dung; chữ CHỈ lấy nguyên văn từ lời nói =====
export const OVERLAYS = [
  {{type: 'hud', start: 0, end: TOTAL - 4, name: {json.dumps((opt.get('topic') or plan.get('topic') or ec.get('title') or '').upper(), ensure_ascii=False)}}},   // dấu kênh ● DAVID │ chủ đề (nhận diện chung)
{tit_lines}];

export const SFX = [
  // không tiếng ký hiệu đầu clip: highlight vào lời ngay giây 0 (David chốt 06/11/2026)
];

export const TONE = {json.dumps([[round(a, 2), round(b, 2), k] for a, b, k in tr])};
export const MUSIC = {{base: 0.2, duck: 0.09, loud: 0.3, loudRanges: [],
  tracks: TONE.map(([a, b, k]) => ({{f: k === 'lang' ? '{MUSIC['lang']}' : '{MUSIC['soi']}', a, b, gain: k === 'lang' ? {GAIN[MUSIC['lang']]} : {GAIN[MUSIC['soi']]}}}))}};

// Màn chốt: câu kêu gọi NGUYÊN VĂN của người nói (luật highlight). kind: 'comment' | 'save' | 'follow' | 'share'
export const CTA = {('{text: ' + json.dumps(cta.get('cta_text') or cta['text'], ensure_ascii=False) + ", kind: 'save'}") if cta else 'null'};

export const HL = {{src_duration: {dur:.2f}, bar: {'true' if TUA else 'false'}}};   // bar: thanh của cả tập gốc (chỉ kiểu --tua)

// Thẻ cuối ~1,8 s sau màn chốt: "Bản đầy đủ trên kênh …" + tên tập gốc + người nói gốc — không nút phát, không chữ tự viết
export const ENDCARD = {endcard};
"""
open(os.path.join(E, 'motion/src/edl.js'), 'w', encoding='utf-8').write(src)
print(f"edl.js: {len(pieces)} câu → {nseg} đoạn (cắt cứng{' + tua' if TUA else ''}), ~{acc:.1f} s · tông {tr}"
      + (" · thẻ cuối +1,8 s" if ec.get('title') else " · ⚠ chưa có thẻ cuối: thêm \"endcard\": {\"title\": <tên tập gốc>} vào phuong-an.json"))
