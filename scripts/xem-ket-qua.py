# Trang xem kết quả (David 13/11/2026: "xem được đầy đủ mọi kết quả của từng video làm ra").
# Chỉ ĐỌC, không dựng, không tốn token. Gom mỗi tập từ bốn nguồn rồi trả một trang web:
#   1. ~/Movies/tap-*                     — đang làm trên Mac (mới nhất)
#   2. Drive Sao-luu-mac/Movies/tap-*, vlog/* — dự án đã xong: thumbnail, phat-hanh.md, dang-bai.md, lời từng clip, số liệu
#   3. Drive Video-xong/                  — thành quả video giao David
#   4. ~/Movies/_so-danh-muc/danh-muc.md  — kết luận lọc, điểm, kênh, lịch, trạng thái
#   python3 scripts/xem-ket-qua.py            → http://localhost:8765 (mở luôn trình duyệt; --khong-mo để không mở)
# Mỗi tập: bản dài (video, thumbnail, bài phát hành, chương), clip ngắn (video, lời clip, bài đăng), kế hoạch, số liệu.
import html, http.server, os, re, socketserver, sys, time, urllib.parse, webbrowser

H0 = os.path.expanduser("~")
DRIVE = os.path.join(H0, "Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi")
ROOTS = {  # id → (thư mục, nhãn)
    "mac": (os.path.join(H0, "Movies"), "Mac · đang làm"),
    "luu": (os.path.join(DRIVE, "Sao-luu-mac/Movies"), "Drive · dự án"),
    "xong": (os.path.join(DRIVE, "Video-xong"), "Drive · Video-xong"),
}
DANH_MUC = os.path.join(H0, "Movies/_so-danh-muc/danh-muc.md")
PORT = int(os.environ.get("PORT", 8765))
VID, IMG = (".mp4", ".mov", ".m4v"), (".jpg", ".jpeg", ".png", ".webp")
ALIAS = {"dung-mua-nhung-thu-ma-ban-thich": "dung-mua-thu-ban-thich"}   # cùng một tập, hai tên thư mục
TEN = {  # tên hiển thị gọn
    "ban-ca-ngay": "Bận cả ngày mà không ra kết quả", "cuoc-goi-hop-tac": "Cuộc gọi hợp tác", "giao-dich-hang-hoa": "Lý do chọn giao dịch hàng hoá",
    "di-trainer": "Trainer cho người làm trainer", "muc-tieu-su-menh": "Mục tiêu và sứ mệnh", "thi-lai-dai-hoc": "Thi lại 4 lần đại học",
    "su-tap-trung": "Sự tập trung", "cuoc-song-giau-co": "Cuộc sống giàu có", "dung-mua-thu-ban-thich": "Đừng mua những thứ bạn thích",
    "5-nguyen-tac-tien": "5 nguyên tắc quản lý tiền", "di-bo-hang-ngay": "Đi bộ hằng ngày", "thoi-quen-nho": "Thói quen nhỏ (phơi nắng)",
    "vong-dong-xu": "Vòng đồng xu cổ", "nang-luc": "Năng lực (thumbnail)", "vlog-the-view-vung-tau": "Vlog The View Vũng Tàu",
    "vlog-nhan-xe-vf3": "Vlog nhận xe VF3", "vlog-mieu-ba-cam": "Vlog Miếu Bà Cam",
}
BO = {"check", "motion", "images", "src", "node_modules", "ref", "davinci", "1-goc", "9-luu-cu", "sheets", "thumbs", "public"}

# ---------- đọc ----------
def ls(p):
    try: return sorted(f for f in os.listdir(p) if not f.startswith("."))
    except OSError: return []

def isf(p): return os.path.isfile(p)

class Tap:
    def __init__(s, key):
        s.key, s.src, s.mtime = key, [], 0
        s.dai_vid, s.thumbs, s.dai_txt = [], [], []        # (root, rel)
        s.clips = {}                                       # chữ cái → {"vid": [...], "txt": [...]}
        s.hl_txt, s.khac = [], []
        s.danh_muc = []
    def add(s, lst, root, rel):
        p = os.path.join(ROOTS[root][0], rel)
        try: size = os.path.getsize(p); s.mtime = max(s.mtime, os.path.getmtime(p))
        except OSError: return
        chu = rel.lower().endswith((".md", ".txt"))   # chữ: trùng tên là trùng (giữ nguồn đọc trước = mới hơn); video, ảnh: trùng dung lượng
        for i, (r, x) in enumerate(lst):
            if (os.path.basename(x) == os.path.basename(rel)) if chu else (os.path.getsize(os.path.join(ROOTS[r][0], x)) == size):
                if os.path.basename(rel).startswith("thumbnail"): lst[i] = (root, rel)   # ảnh David đã chọn thắng bản trùng
                return
        lst.append((root, rel))
    def clip(s, k): return s.clips.setdefault(k.upper(), {"vid": [], "txt": []})

def scan_project(t, root, rel):
    """Một thư mục dự án kiểu tap-x/{2-ban-dai,3-highlight} hoặc phẳng (vlog/x, edit-…)."""
    base = os.path.join(ROOTS[root][0], rel)
    t.src.append(ROOTS[root][1])
    dai = os.path.join(rel, "2-ban-dai") if os.path.isdir(os.path.join(base, "2-ban-dai")) else None
    if not dai and not os.path.isdir(os.path.join(base, "3-highlight")): dai = rel          # dự án phẳng
    for sub in ([dai] if dai else []) + [os.path.join(rel, d) for d in ls(base) if d not in ("2-ban-dai", "3-highlight") and d not in BO and os.path.isdir(os.path.join(base, d))]:
        b = os.path.join(ROOTS[root][0], sub)
        for f in ls(b):
            r = os.path.join(sub, f); fl = f.lower()
            if fl.endswith(VID) and ("final" in fl or sub != rel): t.add(t.dai_vid, root, r)
            elif fl.endswith(IMG) and "@160" not in fl and sub != rel: t.add(t.thumbs, root, r)
            elif fl.endswith((".md", ".txt")) and fl not in ("nguon-anh.txt", "loai.txt", "style.md", "quy-trinh.md"): t.add(t.dai_txt, root, r)
        ph = os.path.join(b, "phat-hanh")
        for f in ls(ph):
            r = os.path.join(sub, "phat-hanh", f); fl = f.lower()
            if fl.endswith(VID): t.add(t.dai_vid, root, r)
            elif fl.endswith(IMG) and "@160" not in fl: t.add(t.thumbs, root, r)
            elif fl.endswith((".md", ".txt")): t.add(t.dai_txt, root, r)
    hl = os.path.join(rel, "3-highlight"); hb = os.path.join(ROOTS[root][0], hl)
    for f in ls(hb):
        r = os.path.join(hl, f); m = re.match(r"clip-([a-z])$", f, re.I)
        if m:
            for g in ls(os.path.join(hb, f)):
                if g.lower().endswith(VID): t.add(t.clip(m.group(1))["vid"], root, os.path.join(r, g))
        elif f.lower().endswith((".md",)): t.add(t.hl_txt, root, r)
    for f in ls(os.path.join(hb, "cat")):
        m = re.match(r"([A-Z])\.md$", f)
        if m: t.add(t.clip(m.group(1))["txt"], root, os.path.join(hl, "cat", f))

def scan_xong(t, rel):
    t.src.append(ROOTS["xong"][1]); base = os.path.join(ROOTS["xong"][0], rel)
    if isf(base): return t.add(t.dai_vid, "xong", rel)
    for d in ls(base):
        for f in ls(os.path.join(base, d)):
            r = os.path.join(rel, d, f); fl = f.lower(); m = re.match(r"clip-([a-z])\.", fl)
            if d == "highlight" and m and fl.endswith(VID): t.add(t.clip(m.group(1))["vid"], "xong", r)
            elif fl.endswith(VID): t.add(t.dai_vid, "xong", r)
            elif fl.endswith(IMG) and "@160" not in fl: t.add(t.thumbs, "xong", r)
            elif fl.endswith((".md", ".txt")): t.add(t.dai_txt, "xong", r)

def danh_muc():
    """Bảng sổ danh mục → [(dict cột, các khoá tập nhắc tới)]."""
    try: lines = open(DANH_MUC, encoding="utf-8").read().split("\n")
    except OSError: return []
    rows, hdr = [], None
    for l in lines:
        if not l.startswith("|"): hdr = None if not l.strip() else hdr; continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if hdr is None: hdr = cells; continue
        if set("".join(cells)) <= set("-: "): continue
        row = dict(zip(hdr, cells)); txt = l
        keys = set(re.findall(r"tap-([a-z0-9-]+[a-z0-9])", txt))
        for grp in re.findall(r"tap-\{([^}]+)\}", txt): keys |= set(grp.split(","))
        for v in re.findall(r"vlog/([a-z0-9-]+)", txt): keys.add("vlog-" + v)
        if "The View" in txt: keys.add("vlog-the-view-vung-tau")
        if "VF3" in txt: keys.add("vlog-nhan-xe-vf3")
        if "Miếu Bà Cam" in txt: keys.add("vlog-mieu-ba-cam")
        rows.append((row, {ALIAS.get(k, k) for k in keys}))
    return rows

def nhom(key):
    if key.startswith(("thu-", "mau-")) or "-thu-" in key or key.startswith("edit-"): return "Bản thử"
    return ""

def tap_all():
    taps = {}
    def get(k): k = ALIAS.get(k, k); return taps.setdefault(k, Tap(k))
    for root in ("mac", "luu"):
        R = ROOTS[root][0]
        for d in ls(R):
            if d.startswith("tap-") and os.path.isdir(os.path.join(R, d)): scan_project(get(d[4:]), root, d)
            elif d == "edit-cong-viec-dien-thoai-chuan-skill": scan_project(get(d), root, d)
        for v in ls(os.path.join(R, "vlog")):
            p = os.path.join(R, "vlog", v)
            if os.path.isdir(p) and not v.startswith("_") and re.fullmatch(r"[a-z0-9-]+", v) and (isf(os.path.join(p, "video-final.mp4")) or os.path.isdir(os.path.join(p, "phat-hanh"))):
                scan_project(get("vlog-" + v), root, os.path.join("vlog", v))
    X = ROOTS["xong"][0]
    for d in ls(X):
        if d.startswith("tap-"): scan_xong(get(d[4:]), d)
        elif d in ("vlog", "video-tu-quay"):
            for f in ls(os.path.join(X, d)):
                if f.lower().endswith(VID): scan_xong(get((d + "-" if d == "vlog" else "tu-quay-") + os.path.splitext(f)[0]), os.path.join(d, f))
    for row, keys in danh_muc():
        for k in keys:
            if k in taps: taps[k].danh_muc.append(row)
    out = [t for t in taps.values() if t.dai_vid or t.thumbs or t.dai_txt or any(c["vid"] or c["txt"] for c in t.clips.values())]
    return sorted(out, key=lambda t: -t.mtime)

# ---------- hiển thị ----------
def inline(l):
    l = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", l)
    l = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<i>\1</i>", l)
    l = re.sub(r"`(.+?)`", r"<code>\1</code>", l)
    return re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target=_blank>\1</a>', l)

def md(s):
    """Markdown tối giản → HTML: tiêu đề, gạch đầu dòng, danh sách số, bảng, đậm, nghiêng, mã, đoạn."""
    out, tbl = [], []
    def flush():
        if not tbl: return
        rows = [r for r in tbl if not set("".join(r)) <= set("-: ")]
        h = "".join(f"<th>{inline(c)}</th>" for c in rows[0]) if rows else ""
        b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
        out.append(f"<div class=tw><table><tr>{h}</tr>{b}</table></div>"); tbl.clear()
    for l in html.escape(s, quote=False).split("\n"):
        if l.lstrip().startswith("|"): tbl.append([c.strip() for c in l.strip().strip("|").split("|")]); continue
        flush()
        m = re.match(r"^(#{1,4}) (.*)", l)
        if m: out.append(f"<h{len(m.group(1)) + 2}>{inline(m.group(2))}</h{len(m.group(1)) + 2}>")
        elif re.match(r"^\s*[-*] ", l): out.append(f"<div class=li>• {inline(l.lstrip()[2:])}</div>")
        elif re.match(r"^\s*\d+[.)] ", l): out.append(f"<div class=li>{inline(l.strip())}</div>")
        elif l.strip(): out.append(f"<p>{inline(l)}</p>")
    flush()
    return "\n".join(out)

def url(root, rel): return f"/f/{root}/" + urllib.parse.quote(rel)
def esc(s): return html.escape(str(s))
def ten(t): return TEN.get(t.key, t.key.replace("-", " ").capitalize())
def nguon(root, rel): return f'<span class=src title="{esc(ROOTS[root][0] + "/" + rel)}">{esc(ROOTS[root][1])}</span>'

def read(root, rel):
    try: return open(os.path.join(ROOTS[root][0], rel), encoding="utf-8").read()
    except Exception: return ""

def trong(txt):
    """Mẫu số liệu chưa điền?"""
    return "<tên video>" in txt or not re.search(r"\|[^|\n]*\|\s*[^|\s][^|\n]*\|", txt.split("## Sau 7 ngày")[-1].split("\n", 3)[-1])

def nhan_vid(n):
    n = n.lower()
    if "xem" in n or "dien-thoai" in n: return "Bản nhẹ xem điện thoại"
    if "khong-teaser" in n: return "Bản không teaser"
    return "Bản cuối"

def fig_vid(root, rel):
    p = os.path.join(ROOTS[root][0], rel); n = os.path.basename(rel); sz = os.path.getsize(p) / 1e6
    ngay = time.strftime("%d/%m %H:%M", time.localtime(os.path.getmtime(p)))
    return (f'<figure><video controls preload=none poster="/poster/{root}/{urllib.parse.quote(rel)}" src="{url(root, rel)}"></video>'
            f'<figcaption><b>{nhan_vid(n)}</b> · {esc(n)} · {sz:.0f} MB · {ngay} · {nguon(root, rel)} · <a href="{url(root, rel)}" download>tải</a></figcaption></figure>')

def fig_img(root, rel):
    n = os.path.basename(rel); chon = n.lower().startswith("thumbnail")
    return (f'<figure class="{"chon" if chon else ""}"><a href="{url(root, rel)}" target=_blank><img loading=lazy src="{url(root, rel)}"></a>'
            f'<figcaption>{"<b>David đã chọn</b> · " if chon else ""}{esc(n)} · {nguon(root, rel)}</figcaption></figure>')

NHAN_TXT = {"phat-hanh.md": "Bài phát hành (tiêu đề, mô tả, chương, bình luận ghim)", "chuong.txt": "Chương YouTube", "dang-bai.md": "Bài đăng clip ngắn",
            "ke-hoach-dang.md": "Kế hoạch đăng", "ke-hoach-canh.md": "Kế hoạch cảnh", "ke-hoach-cat.md": "Kế hoạch cắt clip", "ke-hoach-ghep.md": "Kế hoạch ghép",
            "so-lieu.md": "Số liệu sau khi đăng"}

def doc(root, rel, mo=False):
    f = os.path.basename(rel); txt = read(root, rel)
    if not txt.strip(): return ""
    nhan = NHAN_TXT.get(f, f)
    if f == "so-lieu.md" and trong(txt): return f'<div class=note>{nhan}: chưa điền (điền sau 7 ngày từ ảnh số liệu).</div>'
    nd = f"<pre>{esc(txt)}</pre>" if f.endswith(".txt") else f"<div class=md>{md(txt)}</div>"
    return (f'<details{" open" if mo else ""}><summary>{esc(nhan)} <small>{esc(f)} · {nguon(root, rel)}</small>'
            f'<button class=copy onclick="cp(event,this)">chép</button></summary>{nd}</details>')

def sort_txt(lst):
    order = list(NHAN_TXT)
    return sorted(lst, key=lambda x: order.index(os.path.basename(x[1])) if os.path.basename(x[1]) in order else 99)

def status_card(t):
    if not t.danh_muc: return '<div class=note>Chưa có dòng trong sổ danh mục.</div>'
    out = ""
    for r in t.danh_muc:
        cells = "".join(f"<div><span>{esc(k)}</span>{inline(esc(v))}</div>" for k, v in r.items() if v and k not in ("Tài nguyên",))
        out += f'<div class=status><div class=res>{inline(esc(r.get("Tài nguyên", "")))}</div><div class=kv>{cells}</div></div>'
    return out

def page_tap(t):
    b = f'<a class=back href="/">← Tất cả video</a><h1>{esc(ten(t))}</h1><div class=meta>tap-{esc(t.key)} · nguồn: {esc(" · ".join(dict.fromkeys(t.src)))}</div>'
    b += "<h2>Trạng thái</h2>" + status_card(t)
    if t.dai_vid or t.thumbs or t.dai_txt:
        b += "<h2>Bản dài</h2>"
        if t.dai_vid: b += '<div class=grid>' + "".join(fig_vid(*v) for v in t.dai_vid) + "</div>"
        if t.thumbs: b += '<h3>Thumbnail</h3><div class="grid sm">' + "".join(fig_img(*v) for v in sorted(t.thumbs, key=lambda x: not os.path.basename(x[1]).startswith("thumbnail"))) + "</div>"
        for x in sort_txt(t.dai_txt): b += doc(*x, mo=os.path.basename(x[1]) == "phat-hanh.md")
    if t.clips or t.hl_txt:
        b += f"<h2>Clip ngắn <small>{len(t.clips)} clip</small></h2>"
        for x in sort_txt(t.hl_txt): b += doc(*x, mo=os.path.basename(x[1]) == "dang-bai.md")
        b += '<div class=clips>'
        for k in sorted(t.clips):
            c = t.clips[k]
            b += f'<section class=clip><h3>Clip {k}</h3>'
            b += "".join(fig_vid(*v) for v in c["vid"]) or '<div class=note>Chưa có video cuối (đang dựng).</div>'
            for x in c["txt"]: b += doc(*x).replace(f">{esc(os.path.basename(x[1]))}<", ">Lời clip, bốn câu chọn ý<", 1)
            b += "</section>"
        b += "</div>"
    return b

def card(t):
    th = sorted(t.thumbs, key=lambda x: not os.path.basename(x[1]).startswith("thumbnail"))[0] if t.thumbs else None
    v = (t.dai_vid + [x for k in sorted(t.clips) for x in t.clips[k]["vid"]])[:1]
    img = (f'<img loading=lazy src="{url(*th)}">' if th else f'<img loading=lazy src="/poster/{v[0][0]}/{urllib.parse.quote(v[0][1])}">' if v
           else f'<div class=ph>{esc(ten(t)[:1])}</div>')
    tt = t.danh_muc[-1].get("Trạng thái", "") if t.danh_muc else ""
    kl = t.danh_muc[-1].get("Kết luận", "") if t.danh_muc else ""
    n = f'{len(t.dai_vid)} bản dài · {len(t.clips)} clip · {len(t.thumbs)} ảnh · {"có" if any(os.path.basename(x[1]) in ("phat-hanh.md", "dang-bai.md") for x in t.dai_txt + t.hl_txt) else "chưa có"} bài đăng'
    return (f'<a class=card href="/?tap={urllib.parse.quote(t.key)}">{img}<div class=ci><b>{esc(ten(t))}</b><small>{esc(n)}</small>'
            f'{f"<em>{inline(esc(kl))}</em>" if kl else ""}{f"<span>{inline(esc(tt))}</span>" if tt else ""}</div></a>')

def page_home(taps):
    b = "<h1>Kết quả video</h1><div class=meta>Gom từ Mac (đang làm), Drive dự án, Drive Video-xong và sổ danh mục. Bấm một video để xem đủ: bản dài, thumbnail, bài đăng, từng clip.</div>"
    b += '<input id=q placeholder="Tìm video…" oninput="loc(this.value)">'
    for g in ("", "Bản thử"):
        ts = [t for t in taps if nhom(t.key) == g]
        if ts: b += f'<h2>{g or "Video"} <small>{len(ts)}</small></h2><div class=cards>' + "".join(card(t) for t in ts) + "</div>"
    return b

CSS = """
:root{--bg:#141418;--card:#1e1e24;--card2:#26262e;--tx:#eee;--dim:#9a9aa5;--ac:#ff7a2f;--bd:#2e2e38}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.6 -apple-system,system-ui,sans-serif}
main{max-width:1200px;margin:0 auto;padding:22px 16px 60px} a{color:var(--ac)} h1{margin:0 0 4px;font-size:26px}
h2{color:var(--ac);font-size:18px;margin:30px 0 12px;border-bottom:1px solid var(--bd);padding-bottom:6px} h2 small,summary small{color:var(--dim);font-weight:400;font-size:13px}
h3{font-size:15px;margin:16px 0 8px} .meta{color:var(--dim);font-size:13px} .back{display:inline-block;margin-bottom:10px;text-decoration:none}
#q{width:100%;max-width:360px;margin-top:14px;padding:9px 12px;border-radius:8px;border:1px solid var(--bd);background:var(--card);color:var(--tx);font-size:15px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.card{background:var(--card);border-radius:12px;overflow:hidden;text-decoration:none;color:var(--tx);display:flex;flex-direction:column;border:1px solid transparent}
.card:hover{border-color:var(--ac)} .card img,.ph{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;background:#000}
.ph{display:flex;align-items:center;justify-content:center;font-size:48px;color:var(--ac);background:var(--card2)}
.ci{padding:10px 12px;display:flex;flex-direction:column;gap:3px} .ci small{color:var(--dim);font-size:12px} .ci em{font-style:normal;font-size:13px} .ci span{color:var(--dim);font-size:12px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px} .grid.sm{grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}
figure{margin:0;background:var(--card);border-radius:10px;overflow:hidden} video,figure img{width:100%;display:block;max-height:560px;background:#000;object-fit:contain}
figcaption{padding:7px 10px;color:var(--dim);font-size:12px;word-break:break-all} .src{color:var(--dim);border:1px solid var(--bd);border-radius:4px;padding:0 4px}
details{background:var(--card);border-radius:10px;padding:10px 16px;margin-top:12px} summary{cursor:pointer;color:var(--ac);display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.copy{margin-left:auto;background:var(--card2);color:var(--tx);border:1px solid var(--bd);border-radius:6px;padding:2px 10px;cursor:pointer;font-size:12px}
.md p{margin:6px 0} .md .li{margin:2px 0 2px 8px} code{color:var(--ac)} pre{white-space:pre-wrap;font:13px/1.6 ui-monospace,monospace;margin:8px 0}
.tw{overflow-x:auto} table{border-collapse:collapse;margin:8px 0;font-size:13px} td,th{border:1px solid var(--bd);padding:4px 8px;text-align:left;vertical-align:top}
.note{color:var(--dim);font-size:13px;background:var(--card);border-radius:8px;padding:8px 12px;margin-top:10px}
.status{background:var(--card);border-radius:10px;padding:12px 16px;margin-bottom:10px} .res{font-weight:600;margin-bottom:8px}
.kv{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:8px 16px;font-size:14px} .kv span{display:block;color:var(--dim);font-size:12px}
.clips{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px} .clip{background:var(--card2);border-radius:12px;padding:4px 12px 12px}
.clip video{max-height:620px} figure.chon{outline:2px solid var(--ac)} .clip details{background:var(--card)}
"""
JS = """function cp(e,b){e.preventDefault();e.stopPropagation();const t=b.closest('details').querySelector('.md,pre').innerText;
navigator.clipboard.writeText(t).then(()=>{b.textContent='đã chép';setTimeout(()=>b.textContent='chép',1500)})}
function loc(q){q=q.toLowerCase();document.querySelectorAll('.card').forEach(c=>c.style.display=c.innerText.toLowerCase().includes(q)?'':'none')}"""

def page(sel):
    taps = tap_all(); t = next((x for x in taps if x.key == sel), None)
    body = page_tap(t) if t else page_home(taps)
    title = f"{ten(t)} · Kết quả video" if t else "Kết quả video"
    return (f'<!doctype html><html lang=vi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
            f"<title>{esc(title)}</title><style>{CSS}</style><main>{body}</main><script>{JS}</script></html>")

# ---------- máy chủ ----------
CACHE = os.path.join(H0, "Library/Caches/xem-ket-qua")

def poster(p):
    """Khung hình đại diện cho video (ffmpeg, giây 3), lưu đệm theo tên + dung lượng + giờ sửa."""
    import hashlib, subprocess
    st = os.stat(p); out = os.path.join(CACHE, hashlib.md5(f"{p}{st.st_size}{st.st_mtime}".encode()).hexdigest() + ".jpg")
    if not isf(out):
        os.makedirs(CACHE, exist_ok=True)
        for ss in ("3", "0"):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", ss, "-i", p, "-frames:v", "1", "-vf", "scale=640:-2", out], timeout=120)
            if isf(out): break
    return out if isf(out) else p
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path.startswith(("/f/", "/poster/")):
            kind, rid, rel = u.path[1:].split("/", 2) if u.path.count("/") > 2 else ("", "", "")
            if rid not in ROOTS: return self.send_error(404)
            base = os.path.realpath(ROOTS[rid][0]); p = os.path.realpath(os.path.join(base, urllib.parse.unquote(rel)))
            if not p.startswith(base + os.sep) or not os.path.isfile(p): return self.send_error(404)
            return self.send_file(poster(p) if kind == "poster" else p)
        try: b = page(urllib.parse.parse_qs(u.query).get("tap", [""])[0]).encode()
        except Exception as e: b = f"<pre>Lỗi đọc kết quả: {esc(e)}</pre>".encode()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
        self.wfile.write(b)
    def send_file(self, p):   # có Range để tua video (Safari bắt buộc)
        size = os.path.getsize(p); a, b = 0, size - 1
        m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range", ""))
        if m:
            if m.group(1): a = int(m.group(1)); b = min(int(m.group(2)), size - 1) if m.group(2) else size - 1
            else: a = max(0, size - int(m.group(2)))
            self.send_response(206); self.send_header("Content-Range", f"bytes {a}-{b}/{size}")
        else: self.send_response(200)
        self.send_header("Content-Type", self.guess_type(p)); self.send_header("Accept-Ranges", "bytes"); self.send_header("Content-Length", b - a + 1)
        self.end_headers()
        with open(p, "rb") as f:
            f.seek(a); left = b - a + 1
            try:
                while left > 0:
                    c = f.read(min(1 << 20, left))
                    if not c: break
                    self.wfile.write(c); left -= len(c)
            except (BrokenPipeError, ConnectionResetError): pass

class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True; allow_reuse_address = True

if __name__ == "__main__":
    srv = S(("127.0.0.1", PORT), H)
    print(f"Trang xem kết quả: http://localhost:{PORT}")
    if "--khong-mo" not in sys.argv: webbrowser.open(f"http://localhost:{PORT}")
    srv.serve_forever()
