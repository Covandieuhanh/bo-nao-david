# Đề xuất cắt cho video gốc: de-xuat-lam-sach.py <dự án> <thời lượng>
# Đọc kiem-tra/lam-sach/{moc-tung-tu.srt, ban-chep-loi.srt, am-luong.txt, khoang-lang.txt} → diem-cat.json + diem-cat.md
#   ok=true : thừa đầu/cuối (cắt chắc chắn)
#   ok=false: câu có thể là nói lại (cần Claude đọc moc-tung-tu.srt rồi xác nhận bằng cách đổi thành true);
#   NHỊP (David chốt 2026-11-04): video ≤ 3 phút cắt khoảng lặng ≥ 0,45 s còn 0,24 s + tiếng đệm "ờ/ừm/ơ" (jump cut kiểu kênh lớn);
#   video > 3 phút chỉ cắt lặng ≥ 1,2 s còn 0,5 s, giữ tiếng đệm (TH-1 — học video dài Việt top). Tham số 3
#   `tu-nhien` = kiểu cũ (chỉ liệt kê lặng ≥ 3 s, không cắt). Lời chào/vẫy tay cuối vẫn giữ (nằm sau chữ cuối).
import difflib, json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mo-dun")); import ho_so as hoso   # tham số: san-xuat-video/ho-so
HS = hoso.load('lam-video')

P, DUR = sys.argv[1], float(sys.argv[2])
NATURAL = len(sys.argv) > 3 and sys.argv[3] == "tu-nhien"
O = os.path.join(P, "kiem-tra", "lam-sach")
HEAD_PAD, TAIL_PAD = 0.3, 0.5          # chừa trước câu đầu / sau câu cuối
GAP_KEEP_A, GAP_KEEP_B = 0.2, 0.25     # chừa sau từ trước / trước từ sau trong khoảng lặng
MIN_CUT = 0.5                          # cắt ngắn hơn thì bỏ qua (cắt nhiều mối quá vụn)

def srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+) --> (\d+):(\d+):(\d+)[,.](\d+)\n(.*)", b, re.S)
        if not m: continue
        g = [int(x) for x in m.groups()[:8]]
        out.append(dict(s=g[0]*3600+g[1]*60+g[2]+g[3]/1000, e=g[4]*3600+g[5]*60+g[6]+g[7]/1000, t=m.group(9).strip()))
    return out

loud = [int(l.split()[1]) for l in open(os.path.join(O, "am-luong.txt")) if l.strip()]
thr = float(open(os.path.join(O, "nguong.txt")).read())
def voiced(s, e):  # có tiếng thật trong [s,e] — chặn từ Whisper bịa ra lúc im lặng
    w = loud[int(s / .5): int(e / .5) + 1]
    return bool(w) and max(w) > thr

words = [w for w in srt(os.path.join(O, "moc-tung-tu.srt")) if re.search(r"\w", w["t"]) and voiced(w["s"], w["e"])]
sents = [s for s in srt(os.path.join(O, "ban-chep-loi.srt")) if voiced(s["s"], s["e"])]
if not words:
    sys.exit("Không thấy lời nói thật — kiểm tra lại video/âm thanh")

cuts = []
def add(a, b, why, ok, text=""):
    if b - a >= MIN_CUT: cuts.append(dict(start=round(a, 2), end=round(b, 2), why=why, ok=ok, text=text))

first, last = words[0]["s"], words[-1]["e"]
add(0, first - HEAD_PAD, "thừa đầu", True, "câu đầu: " + (sents[0]["t"] if sents else ""))
add(last + TAIL_PAD, DUR, "thừa cuối", True, "câu cuối: " + (sents[-1]["t"] if sents else ""))

if NATURAL:   # kiểu cũ: khoảng lặng rất dài chỉ liệt kê, mặc định giữ
    for l in open(os.path.join(O, "khoang-lang.txt")):
        v = l.split()
        if not v: continue
        a, b = float(v[0]), float(v[1]) if len(v) > 1 else DUR
        if a < first or b > last: continue
        if b - a >= 3: add(a + GAP_KEEP_A, b - GAP_KEEP_B, f"lặng {b - a:.1f}s (giữ)", False)
else:
    # Khoảng lặng ngắn theo độ lớn 0,05 s (cùng ngưỡng kiem-am-luong.py của highlight): video ngắn (≤ 3 phút) ≥ 0,45 s → rút còn
    # 0,24 s. VIDEO DÀI (> 3 phút, David duyệt TH-1 2026-11-04 — 7/10 video dài nói trước camera Việt top gần như không jump cut):
    # chỉ lặng ≥ 1,2 s → rút còn 0,5 s, KHÔNG cắt tiếng đệm — giữ nhịp trò chuyện tự nhiên.
    LONG = DUR > hoso.get(HS, 'cat_lang.nguong_dai_s', 180)
    _c = hoso.get(HS, 'cat_lang.dai' if LONG else 'cat_lang.ngan', {})
    GMIN, GKEEP = _c.get('min_s', 0.45), _c.get('giu_s', 0.12)
    CUT_FILL = _c.get('cat_tieng_dem', not LONG)
    L5 = [tuple(map(float, l.split())) for l in open(os.path.join(O, "am-luong-05.txt")) if l.strip()]
    lv = sorted(v for _, v in L5); p10, p50 = lv[len(lv) // 10], lv[len(lv) // 2]
    thr5 = p10 + 0.35 * (p50 - p10)
    q = None
    for i, (t, v) in enumerate(L5 + [(DUR, 99)]):
        if v < thr5 and first + 0.2 < t < last - 0.2:
            q = t if q is None else q; continue
        if q is not None and t - q >= GMIN:
            cuts.append(dict(start=round(q + GKEEP, 2), end=round(t - GKEEP, 2), why=f"lặng {t - q:.1f}s", ok=True, text=""))
        q = None
    # Tiếng đệm đứng riêng (Whisper chép được): cắt cả từ, chừa 0,05 s hai bên
    FILL = {"ờ", "ơ", "ừm", "ừ m", "ưm", "ầm", "ậm", "hmm", "um", "uh", "ờm"}
    for w in (words if CUT_FILL else []):   # hồ sơ: cat_tieng_dem
        if re.sub(r"[^\w ]", "", w["t"].lower()).strip() in FILL and w["e"] - w["s"] >= 0.15:
            cuts.append(dict(start=round(w["s"] - 0.05, 2), end=round(w["e"] + 0.05, 2), why="tiếng đệm", ok=True, text=w["t"]))

# Nói lại: hai câu liền nhau (trong 25 s) giống nhau, hoặc câu ngắn bỏ dở là phần đầu của câu sau
norm = lambda t: re.sub(r"[^\w\s]", " ", t.lower()).split()
for i, a in enumerate(sents):
    for b in sents[i + 1: i + 3]:
        if b["s"] - a["s"] > 25: break
        x, y = norm(a["t"]), norm(b["t"])
        if not x or not y: continue
        r = difflib.SequenceMatcher(None, x, y).ratio()
        if r >= .6 or (len(x) >= 2 and y[:min(len(x), 4)] == x[:4]) or (len(x) >= 3 and x[:3] == y[:3]):
            add(a["s"] - 0.1, b["s"] - 0.15, f"có thể nói lại ({r:.0%} giống)", False, f"«{a['t']}» → «{b['t']}»")
            break

# VIDEO DÀI KHÔNG CẮT GÌ (David chốt 2026-11-05, quy-tac-chung 2): chỉ liệt kê, mặc định giữ hết
if DUR > hoso.get(HS, 'cat_lang.nguong_dai_s', 180):
    for c in cuts: c["ok"] = False

cuts.sort(key=lambda c: c["start"])
data = dict(orient=[], zoom="none", cuts=cuts)
dst = os.path.join(O, "diem-cat.json")
if os.path.exists(dst):   # đã có bản Claude chỉnh tay → không ghi đè
    dst = os.path.join(O, "cuts.new.json")
json.dump(data, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

mmss = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
md = ["| # | Từ | Đến | Dài | Lý do | Áp | Nội dung |", "|---|---|---|---|---|---|---|"]
for k, c in enumerate(cuts, 1):
    md.append(f"| {k} | {mmss(c['start'])} | {mmss(c['end'])} | {c['end'] - c['start']:.1f}s | {c['why']} | "
              f"{'✓' if c['ok'] else '?'} | {c['text']} |")
sure = sum(c["end"] - c["start"] for c in cuts if c["ok"])
maybe = sum(c["end"] - c["start"] for c in cuts if not c["ok"])
md.append(f"\nChắc chắn: −{sure:.1f}s · cần xác nhận: −{maybe:.1f}s · gốc {DUR:.1f}s")
open(os.path.join(O, "diem-cat.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print("\n".join(md[-1:]), "→", dst)
