# Viết kịch bản dựng VLOG DÀI nhiều clip từ bảng giữ/bỏ: danh-sach-cat-vlog.py <dự án>
# Đầu vào <P>/ke-hoach.json (Claude viết sau khi xem lời + hình từng clip, nhieu-doan-video.md 2c):
# {
#   "show": {"name": "NÚI ÔNG KÉT", "tag": "HÀNH HƯƠNG"},                       # dòng góc trên (hud)
#   "teaser": {"clip": "c15", "from": 0.0, "to": 3.5, "text": "câu nói"},     # khoảnh khắc đắt nhất mở đầu (bỏ trống = không có)
#   "title": {"clip": "c12", "from": 0, "eyebrow": "…", "l1": "…", "l2": "…", "sub": "…"},
#   "fix": {"núi Kép": "núi Két", …},                                          # sửa chính tả phụ đề (regex, không phân biệt hoa thường)
#   "drop_sub": ["cụm chữ", …],                                                # dòng phụ đề chứa cụm này = nghe không rõ → bỏ
#   "doan-video": [{"c": "c1", "from": 0.3, "to": 34.0, "drop": [[a, b]], "tone": "soi" | "lang",
#              "place": {"eyebrow": "…", "place": "…", "sub": "…"},          # thẻ địa điểm khi tới nơi mới (tuỳ chọn)
#              "mute_sub": [[a, b]], "fast": false, "skip": true, "vol": 0, "note": "…"}, …],   # vol: nhân âm lượng clip (0 = tắt — clip có nhạc sẵn, vd. flycam TikTok)  # bỏ phụ đề đoạn nghe không rõ · fast=false: không tua
#                                                                               # skip: bỏ cả clip · note: lý do (vào báo cáo)
#   "intro": {"kind": 1 | 2, "shots": [{"c": "c23", "at": 16.9, "len": 1.2, "voice": "câu nguyên văn"}, …]},
#            # MỞ ĐẦU kiểu vlog gần đây của kênh mẫu (nhieu-doan-video.md 2d): đoạn GHÉP cảnh đắt nhất cả chuyến (số cảnh theo chất liệu —
#            # chỉ cảnh thật sự khác nhau, không cố định độ dài) trên nhạc
#            # sôi động, thẻ tiêu đề nằm ngay trên đoạn ghép. voice = giữ tiếng thật + phụ đề (1–2 cảnh, nguyên văn), còn lại câm.
#            # kind 1: ghép TRƯỚC rồi tới lời chào (mặc định, đoạn ghép đứng đầu video).
#            # kind 2: lời chào TRƯỚC — tách clip chào làm hai mục trong "doan-video" và đặt {"montage": true} giữa hai mục, ngay sau câu
#            #         chốt kiểu "Let's go / xin được bắt đầu".
#            # "nhac": "intro-soi" (mặc định) | "intro-lang" — Claude chọn theo nội dung chuyến. Cảnh câm không ghi len = 2 phách
#            # của bài (≈ 1,06 s) và nhạc được canh để mọi mối cắt cảnh câm rơi đúng phách.
#            # Có intro thì "teaser" bỏ qua (câu then chốt đặt thành cảnh voice đầu tiên) và "title" không còn đứng riêng.
#   "fx": [                                                                     # HIỆU ỨNG theo lời (mốc = giây trong clip gốc)
#     {"type": "pow", "c": "c3", "at": 130.5, "len": 2.4, "text": "CHỮ TRÍCH LỜI"},   # chữ to nhấn ý (≤ 4 chữ, nguyên văn)
#     {"type": "chips", "c": "c3", "items": [["SỐNG THỌ", 206.0], ["ÍT BỆNH", 207.5]], "len": 4},   # danh sách hiện theo lời
#     {"type": "action", "c": "c3", "at": 246.0, "len": 4.5, "quote": "câu hành động **nhấn**", "done": 248.5},   # thẻ toàn cảnh
#     {"type": "diagram", "c": "c3", "at": 60.0, "len": 5, "mode": "tang|vong|moc|cot|luoi|tu-thanh|anh", "label": "…", "items": [{"at": 60.5, "value": "108", "label": "LÃNH ĐẠO"}]},   # sơ đồ nói thay lời / ảnh khung bo góc (khối 07)
#     {"type": "illus", "c": "c3", "at": 82.0, "len": 4, "mode": "flow", "items": [["footsteps", 82.5, "ĐI BỘ"], ["heart", 84.0, "SỐNG THỌ"]], "label": "HARUKU"},
#       # illus = CẢNH MINH HOẠ toàn màn hình (khối 07, bố cục tự cân): toàn màn hình, phụ đề vẫn chạy, nhãn ≤ 3 chữ trích lời;
#       # mode single · flow · vs (item thứ 4 = true/false) · count ("num": {"to": 15, "at": 83, "unit": "PHÚT"}) · list
#     {"type": "scene", "c": "c3", "at": 82.0, "len": 6, "icons": [["fruit", 84.5], ["tree", 92.0]], "quote": "câu nguyên văn **nhấn**"}],   # (cũ — có câu trích dài)
#     # scene = cảnh minh hoạ VẼ toàn màn hình (biểu tượng bieu-tuong.jsx vẽ dần đúng lúc nhắc + câu nguyên văn), 3–4 cảnh/video                      
#   # Mật độ ~1 hiệu ứng / 15–20 s, chữ CHỈ trích nguyên văn, đặt đúng mốc nói (nhieu-doan-video.md 2d) — vlog chủ yếu nói chuyện
#   # mà không có fx thì người xem chỉ thấy phụ đề suốt (người dùng chỉ ra 2026-11-04, vlog Haruku).
#   "cta": {"text": "…", "kind": "comment"}
# }
# Tự làm: cắt theo from/to trừ drop · đoạn KHÔNG LỜI ≥ 4 s (theo moc-tung-tu.srt) tua 1,8× tiếng nhỏ — giữ cảm giác hành trình mà vẫn có
# nhịp · phụ đề từ moc-tung-tu.srt (≤ 9 chữ/dòng, ngắt ở dấu câu/khoảng lặng), bỏ câu Whisper bịa đặt ("Hãy subscribe…") · thẻ địa điểm 3 s ·
# TONE + MUSIC.tracks theo tông từng clip (nhạc cố định của kênh) · tiếng whoosh ở chuyển chặng. Ghi <P>/chuyen-dong/src/danh-sach-cat.js +
# <P>/kiem-tra/cat-vlog.md (nguồn → video, đoạn bỏ, đoạn tua).
# SOÁT HÌNH (người dùng chỉ ra 2026-11-04: giữ 18 s cuối c13 vì có lời hỏi đường — hình vẫn trong túi rồi lật ngang/lộn ngược):
#   ⚠ in cảnh báo khi đoạn giữ chạm đoạn hỏng của khung-loi.py (kiem-tra/cN/khung-loi.txt) — hình hỏng thì BỎ kể cả có lời;
#   ghi kiem-tra/cac-doan/<cN>_<k>.jpg = 1 khung/giây của từng đoạn giữ → Claude XEM HẾT trước khi render (bắt hình lật/xoay/quay loạn,
#   thứ không dò được bằng độ sáng), sửa ke-hoach.json rồi chạy lại.
import difflib, json, math, os, re, shutil, subprocess, sys

P = os.path.expanduser(sys.argv[1])
plan = json.load(open(os.path.join(P, 'ke-hoach.json'), encoding='utf-8'))
FAST_GAP, FAST_RATE, FAST_VOL, EDGE = 4.0, 1.8, 0.35, 0.6
FPS = 30
fr = lambda s: round(s * FPS) / FPS
BAD = re.compile(r'subscribe|Ghiền Mì Gõ|La La School|bỏ lỡ những video|theo dõi và hẹn gặp lại', re.I)
GAIN = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../ho-so-thuong-hieu/chung.json'), encoding='utf-8'))['nhac']['muc']   # mức cân từng bài: MỘT nguồn ở hồ sơ chung
# Bài cho đoạn ghép mở đầu (assets/music, chọn 2026-11-04 theo chất intro vlog kênh mẫu): (nhịp s, pha phách đầu s) đo bằng onset
#   intro-soi = Upbeat (alex-morgan) — chuyến vui, du lịch · intro-lang = Inspiring Documentary (AtlasAudio) — hành hương, từ thiện, ý nghĩa
BEAT = {'intro-soi': (0.530, 0.015), 'intro-lang': (0.530, 0.040)}
BRAND = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../thu-vien-tai-nguyen/thuong-hieu.json'), encoding='utf-8'))
SFXDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../assets/hieu-ung-am-thanh')
MUSDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../cat-doan-noi-bat/assets/nhac')
intro_mus = None
MUS = {'soi': 'soi-1', 'lang': 'lang-1'}
# ke-hoach.json "tuyen" (hồ sơ chung nhac.tuyen, David chốt 08/11: chọn nhạc theo nội dung từ cả kho) → bài đầu của tuyến cho đoạn sôi;
# "nhac": {"soi": "<bài>", "lang": "<bài>"} chỉ định thủ công
_TY = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../ho-so-thuong-hieu/chung.json'), encoding='utf-8'))['nhac']['tuyen']
if plan.get('tuyen') in _TY and _TY[plan['tuyen']]['bai']:
    MUS['soi'] = _TY[plan['tuyen']]['bai'][0]
MUS.update(plan.get('nhac') or {})

def ts(x):
    h, m, s = x.replace(',', '.').split(':'); return int(h) * 3600 + int(m) * 60 + float(s)
def srt(path):
    out = []
    if not os.path.exists(path): return out
    for blk in open(path, encoding='utf-8').read().split('\n\n'):
        l = blk.strip().split('\n')
        if len(l) >= 3 and l[2].strip():
            a, b = l[1].split(' --> '); out.append((ts(a), ts(b), ' '.join(l[2:]).strip()))
    return out
def dur_of(c):
    for l in open(os.path.join(P, 'clips.tsv'), encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0] == c: return float(f[3].rstrip('s'))
    raise SystemExit(f'không thấy {c} trong clips.tsv')
def minus(a, b, cuts):
    parts = [(a, b)]
    for x, y in sorted(cuts):
        parts = [q for (p0, p1) in parts for q in ((p0, min(p1, x)), (max(p0, y), p1)) if q[1] - q[0] > 0.25]
    return parts
def fixtxt(t, cap=True):
    for k, v in plan.get('fix', {}).items(): t = re.sub(k, v, t, flags=re.I)
    return t[:1].upper() + t[1:] if t and cap else t
DROP = re.compile('|'.join(map(re.escape, plan.get('drop_sub', []))), re.I) if plan.get('drop_sub') else None
norm = lambda w: re.sub(r'[^\w]', '', w.lower())
CONJ = {'thì', 'mà', 'để', 'nhưng', 'nên', 'hay', 'và', 'là', 'của', 'với', 'cho', 'từ', 'vì', 'khi', 'nếu', 'rồi', 'còn', 'cũng',
        'này', 'đây', 'đó', 'ở', 'mọi', 'các', 'chúng', 'bây', 'tức', 'ví', 'giống', 'như'}
END_BAD = {'nhưng', 'và', 'thì', 'là', 'mà', 'của', 'trong', 'một', 'cái', 'rất', 'các', 'những', 'để', 'cho', 'với', 'từ', 'khi',
           'nếu', 'vì', 'bởi', 'sẽ', 'đã', 'đang', 'được', 'như', 'hay', 'thật', 'tất', 'đúng', 'có', 'ví', 'tức', 'giống', 'nên'}

raw, subs, tones, overlays, sfx, report = [], [], [], [], [], []
acc = 0.0
def add(seg, tone):
    global acc
    d = seg.get('freeze') or (seg['to'] - seg['from']) / seg.get('rate', 1)
    seg['_start'] = acc; raw.append(seg); tones.append((acc, acc + fr(d), tone)); acc += fr(d)
    return seg

INTRO = plan.get('intro')
tz = None if INTRO else plan.get('teaser')
if tz:
    add({'id': 'teaser', 'clip': tz['clip'], 'from': tz['from'], 'to': tz['to'], 'vol': 1}, 'soi')
    overlays.append(f"  {{type: 'teaserTag', start: 0, end: segEnd('teaser')}},")
    if tz.get('text'):                                    # câu nói trong đoạn mở đầu (nguyên văn) — phụ đề cả đoạn
        subs.append(f"  ['teaser', {tz['from']:.2f}, {tz['to']:.2f}, {json.dumps(tz['text'], ensure_ascii=False)}, []],")
tt = plan.get('title')
def emit_montage():
    # đoạn ghép mở đầu: cảnh câm chạy trên nhạc intro, cảnh `voice` giữ tiếng thật; tiêu đề nằm trên dải cảnh câm (không chồng phụ đề)
    global intro_mus
    m0 = acc; quiet = []
    mus = INTRO.get('nhac', 'intro-soi'); beat, phase = BEAT[mus]
    for i, s in enumerate(INTRO['shots']):
        sid = f'm{i + 1}'; ln = s.get('len', 1.2 if s.get('voice') else round(2 * beat, 3))
        if not s.get('voice'):
            if quiet and abs(quiet[-1][1] - acc) < 1e-6: quiet[-1][1] = acc + fr(ln)
            else: quiet.append([acc, acc + fr(ln)])
        add({'id': sid, 'clip': s['c'], 'from': s['at'], 'to': round(s['at'] + ln, 3), 'vol': 1 if s.get('voice') else 0}, 'intro')
        if s.get('voice'):
            subs.append(f"  [{json.dumps(sid)}, {s['at']:.2f}, {s['at'] + ln:.2f}, {json.dumps(fixtxt(s['voice']), ensure_ascii=False)}, []],")
    # nhạc intro vào từ đầu đoạn ghép; điểm vào bài chọn sao cho một phách rơi đúng đầu dải cảnh câm đầu tiên → mọi mối cắt 2 phách khớp nhịp
    q0 = quiet[0][0] if quiet else m0
    off = phase + beat * math.ceil((q0 - m0 - phase) / beat) - (q0 - m0)
    intro_mus = {'f': mus, 'from': round(off, 3), 'loud': [[round(x, 2), round(y, 2)] for x, y in quiet]}
    if tt:
        q = max(quiet, key=lambda r: r[1] - r[0]) if quiet else [m0, acc]   # dải cảnh câm dài nhất
        overlays.append(f"  {{type: 'title', over: true, start: {q[0] + 0.1:.2f}, end: {min(q[1], q[0] + 3.3):.2f}, eyebrow: {json.dumps(tt.get('eyebrow', ''), ensure_ascii=False)}, "
                        f"l1: {json.dumps(tt['l1'], ensure_ascii=False)}, l2: {json.dumps(tt['l2'], ensure_ascii=False)}, sub: {json.dumps(tt.get('sub', ''), ensure_ascii=False)}}},")
        sfx.append(f"  {{f: '{BRAND['sting'][:-4]}', at: {q[0]:.2f}, v: {BRAND['stingVol']}}},")   # tiếng ký hiệu kênh ở tiêu đề (cả 4 loại)
    return acc
if INTRO and INTRO.get('kind', 1) == 1 and not any(k.get('montage') for k in plan['doan-video']):
    hud_from = emit_montage()
elif tt and not INTRO:
    add({'id': 'title', 'clip': tt['clip'], 'from': tt.get('from', 0), 'to': tt.get('from', 0) + 2.8, 'vol': 0, 'grade': 'title'}, 'soi')
    overlays.append(f"  {{type: 'title', start: segStart('title'), end: segEnd('title'), eyebrow: {json.dumps(tt.get('eyebrow', ''), ensure_ascii=False)}, "
                    f"l1: {json.dumps(tt['l1'], ensure_ascii=False)}, l2: {json.dumps(tt['l2'], ensure_ascii=False)}, sub: {json.dumps(tt.get('sub', ''), ensure_ascii=False)}}},")
    sfx += ["  {f: 'whoosh', at: segStart('title') - 0.25, v: 0.8},", "  {f: 'boom', at: segStart('title'), v: 0.9},",
            "  {f: 'sting', at: segStart('title') + 0.05, v: 0.55},"]
if not INTRO: hud_from = acc

src_total = kept_total = 0.0
LOWER, PROPER, PAIR = set(), set(), {}                             # từ thường · tên riêng (viết hoa ở GIỮA dòng: Nhật Bản, Haruku…)
for k in plan['doan-video']:
    if k.get('montage'): continue
    for _, _, t in srt(os.path.join(P, 'kiem-tra', k['c'], 'ban-chep-loi.srt')):
        ws = re.findall(r'\w+', t)
        LOWER |= {w for w in ws if w.islower()}
        PROPER |= {w for w in ws[1:] if w[:1].isupper()}
        lw = [w.lower() for w in ws]
        for i in range(len(lw) - 1): PAIR[(lw[i], lw[i + 1])] = PAIR.get((lw[i], lw[i + 1]), 0) + 1
# cặp chữ lặp ≥ 2 lần trong lời (bí mật, đi bộ, sức khỏe, sắp xếp…) ≈ từ ghép → không ngắt dòng giữa hai chữ
COMPOUND = {k for k, v in PAIR.items() if v >= 2 and not (k[0] in END_BAD and k[1] in CONJ)}
for v in plan.get('fix', {}).values():                  # chữ đã sửa tay (phạm trù, bộ môn…) cũng là từ ghép
    vw = [norm(w) for w in v.split()]; COMPOUND |= {(vw[i], vw[i + 1]) for i in range(len(vw) - 1)}
warn, sheets, seen, cnt = [], [], set(), {}
for k in plan['doan-video']:
    if k.get('montage'):                                   # kind 2: đoạn ghép chen sau câu chào
        hud_from = emit_montage(); continue
    c, tone = k['c'], k.get('tone', 'soi')
    D = dur_of(c)
    if c not in seen: src_total += D; seen.add(c)         # một clip tách làm hai mục (kind 2) chỉ tính nguồn một lần
    a, b = max(0.0, k.get('from', 0.3)), min(D, k.get('to', D - 0.3))
    keep = [] if k.get('skip') else minus(a, b, k.get('drop', []))      # skip: bỏ cả clip (trùng / hỏng) — vẫn tính vào tổng nguồn
    words = [w for w in srt(os.path.join(P, 'kiem-tra', c, 'moc-tung-tu.srt'))]
    bad = [(x, y) for x, y, t in srt(os.path.join(P, 'kiem-tra', c, 'ban-chep-loi.srt')) if BAD.search(t)]
    mute = k.get('mute_sub', [])
    words = [w for w in words if not any(x - 0.2 <= w[0] <= y + 0.2 for x, y in bad + [tuple(m) for m in mute])]
    raw_lines = [(la, lb, t) for la, lb, t in srt(os.path.join(P, 'kiem-tra', c, 'ban-chep-loi.srt'))
                 if not BAD.search(t) and not any(la < y and lb > x for x, y in [tuple(m) for m in mute])]
    # Whisper ngắt dòng giữa câu ("…bây giờ sẽ là quá / Trình hành hương…") → nối các dòng chưa có dấu kết câu thành một câu,
    # chữ đầu dòng nối hạ chữ thường nếu nó là từ thường (có xuất hiện viết thường ở đâu đó trong lời)
    lines = []
    for la, lb, t in raw_lines:
        if lines and not re.search(r'[.?!…]$', lines[-1][2]) and la - lines[-1][1] < 0.6:
            w0, rest = (t.split(' ', 1) + [''])[:2]
            sep = ' '
            if re.sub(r'\W', '', w0) in PROPER: pass                     # tên riêng giữa câu → giữ hoa
            elif w0.lower() in LOWER: w0 = w0.lower()                     # từ thường bị Whisper viết hoa đầu dòng → hạ
            elif w0[:1].isupper(): sep = '. '                             # hoa, không phải tên riêng → câu mới
            # (vd "Chúc mừng một ngày tốt lành / Gần đây thì…" — trước 2026-11-04 bị nối thành "…tốt lành Gần đây")
            lines[-1] = (lines[-1][0], lb, (lines[-1][2] + sep + w0 + (' ' + rest if rest else '')).strip())
        else: lines.append((la, lb, t))
    try: badr = [tuple(float(v) for v in l.split()[0].split('-')) + (l.split()[1],)
                 for l in open(os.path.join(P, 'kiem-tra', c, 'khung-loi.txt'), encoding='utf-8') if l.strip()]
    except FileNotFoundError: badr = []
    for p0, p1 in keep:
        for x, y, why in badr:
            if min(p1, y) - max(p0, x) >= 0.5:
                warn.append(f"{c} giữ {p0:.1f}–{p1:.1f} chạm đoạn hỏng {x:.1f}–{y:.1f} {why}")
        sheets.append((c, p0, p1))
    first = True; n = cnt.get(c, 0)
    for p0, p1 in keep:
        # đoạn không lời ≥ 4 s → tua (trừ khi fast=false)
        ws = [w for w in words if p0 <= w[0] < p1]
        slow = []
        if k.get('fast', True):
            gaps, last = [], p0
            for w in ws:
                if w[0] - last >= FAST_GAP: gaps.append((last + 0.4, w[0] - 0.4))
                last = max(last, w[1])
            if p1 - last >= FAST_GAP: gaps.append((last + 0.4, p1))
            slow = [(x, y) for x, y in gaps if y - x >= FAST_GAP - 0.8]
        cur = p0
        pieces = []
        for x, y in slow:
            if x - cur > 0.25: pieces.append((cur, x, False))
            pieces.append((x, y, True)); cur = y
        if p1 - cur > 0.25: pieces.append((cur, p1, False))
        for x, y, fast in pieces:
            n += 1; cnt[c] = n; sid = f'{c}_{n}'
            seg = {'id': sid, 'clip': c, 'from': round(x, 2), 'to': round(y, 2), 'vol': round((FAST_VOL if fast else 1) * k.get('vol', 1), 3)}
            if fast: seg['rate'] = FAST_RATE
            if tone == 'lang' and not fast: seg['grade'] = 'lang'
            add(seg, tone); kept_total += (y - x) / (FAST_RATE if fast else 1)
            if first and k.get('place'):
                pl = k['place']
                overlays.append(f"  {{type: 'location', start: segStart('{sid}') + 0.3, end: segStart('{sid}') + 3.3, eyebrow: {json.dumps(pl.get('eyebrow', 'ĐIỂM TIẾP THEO'), ensure_ascii=False)}, "
                                f"place: {json.dumps(pl['place'], ensure_ascii=False)}, sub: {json.dumps(pl.get('sub', ''), ensure_ascii=False)}}},")
                if tone == 'soi': sfx.append(f"  {{f: 'whoosh', at: segStart('{sid}') + 0.1, v: 0.5}},")
            first = False
            if fast: continue
            # phụ đề: theo CÂU của ban-chep-loi.srt (có dấu câu), câu dài chia thành dòng ≤ 9 chữ cân nhau, ngắt sau dấu câu / trước
            # từ nối; mốc chia theo số ký tự trong câu (mốc từng chữ Whisper không có dấu câu → ngắt lủng củng "…này bây / Giờ sẽ…")
            for la, lb, text in lines:
                if lb <= x or la >= y: continue
                toks = fixtxt(text, cap=False).split()            # sửa chính tả TRƯỚC khi chia (tên riêng không bị tách đôi)
                # mốc TỪNG CHỮ: khớp chữ của câu với moc-tung-tu.srt (difflib), chữ không khớp nội suy. Chữ rơi ngoài đoạn giữ thì bỏ —
                # trước 2026-11-04 cả câu được giữ theo tỉ lệ ký tự nên tràn chữ của đoạn đã cắt ("…tốt lành thật ra", "David xin chào…")
                ww = [w for w in words if la - 0.6 <= w[0] <= lb + 0.3]
                sm = difflib.SequenceMatcher(None, [norm(t) for t in toks], [norm(w[2]) for w in ww], autojunk=False)
                st = [None] * len(toks); en = [None] * len(toks)
                for i0, j0, n0 in sm.get_matching_blocks():
                    for q in range(n0): st[i0 + q], en[i0 + q] = ww[j0 + q][0], ww[j0 + q][1]
                kn = [i for i in range(len(toks)) if st[i] is not None]
                for i in range(len(toks)):
                    if st[i] is None:
                        pv = max((k for k in kn if k < i), default=None); nx = min((k for k in kn if k > i), default=None)
                        t0 = st[pv] if pv is not None else la; t1 = st[nx] if nx is not None else lb
                        i0 = pv if pv is not None else -1; i1 = nx if nx is not None else len(toks)
                        st[i] = t0 + (t1 - t0) * (i - i0) / max(1, i1 - i0); en[i] = st[i] + 0.2
                keep_i = [i for i in range(len(toks)) if x - 0.05 <= st[i] < y - 0.05]
                if not keep_i: continue
                toks = [toks[i] for i in keep_i]; st = [st[i] for i in keep_i]; en = [en[i] for i in keep_i]
                nl = max(1, -(-len(toks) // 9)); size = len(toks) / nl   # nl, không dùng n (n = số đếm đoạn → trùng id)
                def score(t, t0):
                    # chỗ ngắt: khoảng ngừng giọng nói > sau dấu câu > trước từ nối; dòng KHÔNG kết bằng từ đệm/nối ("nhưng | mà",
                    # "rất | là", "trong | đó"); cấm tách tên riêng
                    sc = -abs(t - t0) * 0.6 + min(2.5, max(0.0, st[t] - en[t - 1]) * 6)
                    if re.search(r'[,.?!…]$', toks[t - 1]): sc += 3
                    if norm(toks[t]) in CONJ: sc += 1.5
                    if norm(toks[t - 1]) in END_BAD: sc -= 3
                    if (norm(toks[t - 1]), norm(toks[t])) in COMPOUND: sc -= 4
                    if toks[t - 1][:1].isupper() and toks[t][:1].isupper(): sc -= 6
                    return sc
                cuts = []
                for q in range(1, nl):
                    t0 = round(q * size)
                    cand = [t for t in range(t0 - 4, t0 + 5) if 2 <= t <= len(toks) - 2 and (not cuts or t > cuts[-1] + 1)]
                    cuts.append(max(cand, key=lambda t: score(t, t0)) if cand else t0)
                bounds = [0] + cuts + [len(toks)]
                for q in range(len(bounds) - 1):
                    part = toks[bounds[q]:bounds[q + 1]]
                    if not part: continue
                    t_a = st[bounds[q]]
                    t_b = st[bounds[q + 1]] if bounds[q + 1] < len(toks) else min(y, max(lb, en[-1]))
                    t_a, t_b = max(x, t_a), min(y, t_b)
                    if t_b - t_a < 0.3: continue
                    txt = fixtxt(' '.join(part).strip(' ,'), cap=(q == 0 or re.search(r'[.?!…]$', toks[bounds[q] - 1] if bounds[q] else '')))
                    if DROP and DROP.search(txt): continue        # câu nghe không rõ → bỏ phụ đề, không đoán (plan.drop_sub)
                    subs.append(f"  [{json.dumps(sid)}, {t_a:.2f}, {t_b:.2f}, {json.dumps(txt, ensure_ascii=False)}, []],")
    report.append(f"| {c} | {D:.1f} | {'BỎ CẢ CLIP' if k.get('skip') else f'{a:.1f}–{b:.1f}'} | {', '.join(f'{x:.0f}–{y:.0f}' for x, y in k.get('drop', [])) or '—'} | {tone} | {k.get('note', '')} |")

# ===== HIỆU ỨNG theo lời (plan.fx) — mốc giây trong clip gốc → đoạn chứa mốc đó (bỏ đoạn tua) =====
def seg_at(c, t):
    for sg in raw:
        if sg['clip'] == c and not sg['id'].startswith('m') and sg['from'] - 0.01 <= t < sg['to'] and sg.get('rate', 1) == 1: return sg
    warn.append(f"fx: {c} {t:.1f} không nằm trong đoạn giữ (hoặc nằm trong đoạn tua) → bỏ"); return None
for fx in plan.get('fx', []):
    ty, c = fx['type'], fx['c']
    if ty == 'zoom' and False:   # không zoom vào / ra (13/11/2026 — David: không thẩm mỹ)
        sg = seg_at(c, fx['at'])
        if sg: sg.setdefault('zoom', []).append({'at': fx['at'], 's': fx.get('s', 1.12), 'x': fx.get('x', 0.5), 'y': fx.get('y', 0.32), 'len': fx.get('len', 0.5), 'hold': fx.get('hold', 2.5)})
        continue
    t0 = fx['at'] if ty != 'chips' else fx['items'][0][1] - 0.3
    sg = seg_at(c, t0)
    if not sg: continue
    st = f"T('{sg['id']}', {t0:.2f})"; en = f"{st} + {fx.get('len', 2.4)}"
    if ty == 'pow':
        overlays.append(f"  {{type: 'pow', start: {st}, end: {en}, text: {json.dumps(fx['text'], ensure_ascii=False)}}},")
        sfx.append(f"  {{f: 'pop', at: {st}, v: 0.5}},")
    elif ty == 'chips':
        its = ', '.join(f"[{json.dumps(t, ensure_ascii=False)}, T('{sg['id']}', {a:.2f})]" for t, a in fx['items'])
        overlays.append(f"  {{type: 'chips', start: {st}, end: {st} + {fx.get('len', 4)}, items: [{its}]}},")
        sfx += [f"  {{f: 'ding{min(4, i + 1)}', at: T('{sg['id']}', {a:.2f}), v: 0.4}}," for i, (t, a) in enumerate(fx['items'])]
    elif ty == 'scene':                                    # cảnh minh hoạ vẽ: icons [[tên, giây clip]] + câu nguyên văn
        ics = ', '.join(f"[{json.dumps(nm)}, T('{sg['id']}', {a:.2f})]" for nm, a in fx['icons'])
        overlays.append(f"  {{type: 'scene', start: {st}, end: {en}, icons: [{ics}], quote: {json.dumps(fx['quote'], ensure_ascii=False)}, flow: {json.dumps(fx.get('flow', True))}}},")
        sfx.append(f"  {{f: 'whoosh', at: {st}, v: 0.45}},")
    elif ty == 'illus':                                    # CẢNH MINH HOẠ 2 TRẠNG THÁI (khối 07): items [[icon, giây clip, nhãn?, good?]] + label ≤ 3 chữ
        its = ', '.join('{' + f"icon: {json.dumps(it[0])}, at: T('{sg['id']}', {it[1]:.2f})" + (f", label: {json.dumps(it[2], ensure_ascii=False)}" if len(it) > 2 and it[2] else '')
                        + (f", good: {json.dumps(it[3])}" if len(it) > 3 else '') + '}' for it in fx['items'])
        nm = fx.get('num'); num = (f", num: {{to: {nm['to']}, from: {nm.get('from', 0)}, at: T('{sg['id']}', {nm['at']:.2f}), unit: {json.dumps(nm.get('unit', ''), ensure_ascii=False)}}}" if nm else '')
        overlays.append(f"  {{type: 'illus', start: {st}, end: {en}, mode: {json.dumps(fx.get('mode', 'single'))}, items: [{its}], label: {json.dumps(fx.get('label', ''), ensure_ascii=False)}{num}}},")
        sfx.append(f"  {{f: 'whoosh', at: {st}, v: 0.4}},")
    elif ty == 'diagram':                                  # SƠ ĐỒ NÓI THAY LỜI (khối 07, 2026-11-05): items [{at: giây clip, value?, label, sub?, upto?, photo?, credit?, icon?}]
        def _it(it):
            kv = [f"at: T('{sg['id']}', {it['at']:.2f})"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in it.items() if k != 'at']
            return '{' + ', '.join(kv) + '}'
        its = ', '.join(_it(it) for it in fx['items'])
        overlays.append(f"  {{type: 'diagram', start: {st}, end: {en}, mode: {json.dumps(fx.get('mode', 'tang'))}, items: [{its}], label: {json.dumps(fx.get('label', ''), ensure_ascii=False)}, total: {int(fx.get('total', 0))}}},")
        sfx.append(f"  {{f: 'whoosh', at: {st}, v: 0.4}},")
    elif ty == 'action':
        overlays.append(f"  {{type: 'action', start: {st}, end: {en}, quote: {json.dumps(fx['quote'], ensure_ascii=False)}, doneAt: T('{sg['id']}', {fx.get('done', fx['at'] + 2):.2f})}},")
        sfx.append(f"  {{f: 'whoosh', at: {st}, v: 0.5}},")

# gộp tông → nhạc
tr = []
for a, b, k in tones:
    if tr and tr[-1][2] == k: tr[-1][1] = b
    else: tr.append([a, b, k])
cta = plan.get('cta', {'text': '', 'kind': 'comment'})
# MỨC NHẠC KHI CÓ LỜI theo độ to GIỌNG thật của video (người dùng chỉ ra 2026-11-04: vlog Haruku giọng −32 LUFS, mức cố định
# duck 0,08 → nhạc chỉ dưới giọng ~5 dB, lấn lời). Bài đã cân gain về ~−15,5 LUFS → duck = nhạc thấp hơn giọng SPEECH_GAP LU.
SPEECH_GAP = BRAND['musicGapVlogLU']
def lufs(c):
    out = subprocess.run(['ffmpeg', '-nostats', '-i', os.path.join(P, 'chuyen-dong/public/doan-video', c + '.mp4'), '-af', 'ebur128', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', out)
    return float(m[-1]) if m else -23.0
used = [(k['c'], k.get('to', dur_of(k['c'])) - k.get('from', 0)) for k in plan['doan-video'] if k.get('c') and not k.get('skip')]
speech = 10 * math.log10(sum(d * 10 ** (lufs(c) / 10) for c, d in used) / max(1e-6, sum(d for _, d in used)))
duck = round(min(0.08, 10 ** ((speech - SPEECH_GAP + 15.5) / 20)), 3)
base = round(min(0.2, duck * 1.6), 3)                     # chỗ ngừng nói: nhạc nhích lên nhẹ (×2,5 nghe dập dình)
tracks = []
for x, y, k in tr:
    f = intro_mus['f'] if k == 'intro' else MUS['lang'] if k == 'lang' else MUS['soi']
    tracks.append({'f': f, 'a': round(x, 2), 'b': round(y, 2), 'gain': GAIN[f], **({'from': intro_mus['from']} if k == 'intro' else {})})
last = next((s_ for s_ in reversed(raw) if not s_['id'].startswith('m')), raw[-1])
endcard = {'title': plan.get('show', {}).get('name', ''), 'speaker': BRAND['name'], 'clip': last['clip'], 'at': round(max(last['from'], last['to'] - 1.0), 2),
           'len': BRAND['endcardLen'] + (plan.get('ytEnd') or 0), 'play': False, 'yt': plan.get('ytEnd') or 0, 'schedule': plan.get('schedule', '')}   # ytEnd: màn kết YouTube 15–20 s
st_dst = os.path.join(P, 'chuyen-dong/public/hieu-ung-am-thanh', BRAND['sting'])
if not os.path.exists(st_dst): shutil.copy(os.path.join(SFXDIR, BRAND['sting']), st_dst)
for f in {t['f'] for t in tracks}:                       # chép bài cần dùng vào dự án (nhạc cố định của kênh)
    dst = os.path.join(P, 'chuyen-dong/public/hieu-ung-am-thanh', f + '.mp3')
    if not os.path.exists(dst): shutil.copy(os.path.join(MUSDIR, f + '.mp3'), dst)
tpl = open(os.path.join(P, 'chuyen-dong/src/danh-sach-cat.js'), encoding='utf-8').read()
head = tpl[:tpl.index('const RAW = [')]
mid = tpl[tpl.index('let acc = 0;'):tpl.index('// ===== Phụ đề')]
rawjs = ',\n'.join('  ' + json.dumps({k: v for k, v in s.items() if not k.startswith('_')}, ensure_ascii=False) for s in raw)
show = plan.get('show', {})
src = f"""{head}// Viết bởi dung-video-theo-phong-cach/scripts/danh-sach-cat-vlog.py từ ke-hoach.json — sửa ke-hoach.json rồi chạy lại (không sửa tay file này).
const RAW = [
{rawjs}
];

{mid}// ===== Phụ đề (moc-tung-tu.srt, đã sửa chính tả theo plan.fix) =====
const SUB = [
{chr(10).join(subs)}
];
export const SUBS = SUB.map(([id, a, b, text, hl]) => ({{start: T(id, a), end: T(id, b), text, hl}}));

export const OVERLAYS = [
  {{type: 'hud', start: {hud_from:.2f}, end: TOTAL - 4, name: {json.dumps(show.get('name', ''), ensure_ascii=False)}, tag: {json.dumps(show.get('tag', ''), ensure_ascii=False)}}},
{chr(10).join(overlays)}
];

export const SFX = [
{chr(10).join(sfx)}
];

export const TONE = {json.dumps([[round(a, 2), round(b, 2), k] for a, b, k in tr])};
// giọng ≈ {speech:.1f} LUFS → nhạc dưới giọng ~{SPEECH_GAP} LU
export const MUSIC = {{base: {base}, duck: {duck}, loud: 0.3, loudRanges: {json.dumps(intro_mus['loud'] if intro_mus else [])},
  tracks: {json.dumps(tracks)}}};

export const CTA = {json.dumps(cta, ensure_ascii=False)};
export const HL = null;

// Thẻ cuối nhận diện (cả 4 loại video): chủ đề + tên kênh, sau màn chốt CTA
export const ENDCARD = {json.dumps(endcard, ensure_ascii=False)};
"""
open(os.path.join(P, 'chuyen-dong/src/danh-sach-cat.js'), 'w', encoding='utf-8').write(src)
md = [f"# Cắt vlog — nguồn {src_total / 60:.1f} phút → video {acc / 60:.1f} phút ({acc / src_total:.0%})", "",
      "| Clip | Dài (s) | Giữ | Bỏ | Tông | Ghi chú |", "|---|---|---|---|---|---|"] + report
if warn: md += ["", "## ⚠ Đoạn giữ chạm hình hỏng (khung-loi.py) — bỏ, hoặc xem tờ soát và ghi lý do giữ vào note", ""] + [f"- {w}" for w in warn]
open(os.path.join(P, 'kiem-tra', 'cat-vlog.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
SD = os.path.join(P, 'kiem-tra', 'cac-doan'); os.makedirs(SD, exist_ok=True)
for f in os.listdir(SD): os.remove(os.path.join(SD, f))
for i, (c, p0, p1) in enumerate(sheets):
    n = max(1, int(p1 - p0))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{p0:.2f}', '-to', f'{p1:.2f}', '-i', os.path.join(P, 'chuyen-dong/public/doan-video', c + '.mp4'),
                    '-vf', f'fps=1,scale=120:-2,tile=10x{(n + 9) // 10}', '-frames:v', '1', os.path.join(SD, f'{i:03d}_{c}_{p0:.0f}-{p1:.0f}.jpg')])
for w in warn: print('⚠', w)
# MỐC CHỤP SOÁT: cuối mỗi lớp chữ (lúc mọi mục đã hiện — danh sách dài nhất ở cuối, 2026-11-04 chụp đầu chips nên sót lỗi đè)
_t = subprocess.run(['node', '-e', "import('./src/danh-sach-cat.js').then(m=>console.log(m.OVERLAYS.filter(o=>o.type!=='hud').map(o=>(o.end-0.25).toFixed(2)).join(' ')))"],
                    cwd=os.path.join(P, 'chuyen-dong'), capture_output=True, text=True).stdout.strip()
if _t: print(f"chụp soát (BẮT BUỘC trước render, xem hết): cd {P}/chuyen-dong && node anh-tinh.mjs {_t}")
print(f"nhạc: giọng {speech:.1f} LUFS → duck {duck} · base {base}")
print(f"danh-sach-cat.js: {len(raw)} đoạn ({sum(1 for s in raw if s.get('rate', 1) > 1)} đoạn tua), {len(subs)} dòng phụ đề · nguồn {src_total:.0f} s → {acc:.0f} s ({acc / src_total:.0%}) · tông {len(tr)} khoảng")
