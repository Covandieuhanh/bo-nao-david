# Trang xem kết quả (David 13/11/2026: "xem được đầy đủ mọi kết quả của từng video làm ra").
# Chỉ ĐỌC, không dựng, không tốn token. Gom mỗi tập từ bốn nguồn rồi trả một trang web:
#   1. ~/Movies/tap-*                     — đang làm trên Mac (mới nhất)
#   2. Drive sao-luu-mac/video/tap-*, vlog/* — dự án đã xong: thumbnail, phat-hanh.md, dang-bai.md, lời từng clip, số liệu
#   3. Drive thanh-pham/                  — thành quả video giao David
#   4. ~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md  — kết luận lọc, điểm, kênh, lịch, trạng thái
#   python3 tu-dong-hoa/xem-ket-qua.py            → http://localhost:8765 (mở luôn trình duyệt; --khong-mo để không mở)
# Giao diện (David 13/11/2026: "xem được video và ảnh bìa ngay khi mở, giảm thao tác, file ấn mới xem"): mỗi tập một hàng
# bìa · bản dài · clip phát ngay tại chỗ; bài đăng, kế hoạch, lời clip, số liệu ẩn sau nút "Tài liệu", bấm mở khung xem có nút chép.
import html, http.server, os, re, socketserver, sys, time, urllib.parse, webbrowser

H0 = os.path.expanduser("~")
DRIVE = os.path.join(H0, "Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi")
ROOTS = {  # id → (thư mục, nhãn)
    "mac": (os.path.join(H0, "Movies"), "Mac · đang làm"),
    "luu": (os.path.join(DRIVE, "sao-luu-mac/video"), "Drive · dự án"),
    "xong": (os.path.join(DRIVE, "thanh-pham"), "Drive · thanh-pham"),
    "bai": (os.path.join(H0, "Documents/1-nghe-nghiep/bai-dang"), "Bài đăng Facebook cá nhân"),
}
DANH_MUC = os.path.join(H0, "Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md")
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
BO = {"kiem-tra", "chuyen-dong", "hinh-anh", "src", "node_modules", "tai-lieu-tham-khao", "tu-lieu", "1-goc", "9-luu-cu", "bang-anh", "anh-nho", "public"}

# ---------- đọc ----------
def ls(p):
    try: return sorted(f for f in os.listdir(p) if not f.startswith("."))
    except OSError: return []

def isf(p): return os.path.isfile(p)

class Tap:
    def __init__(s, key):
        s.key, s.src, s.mtime = key, [], 0
        s.dai_vid, s.anh_nho, s.dai_txt = [], [], []        # (root, rel)
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
    """Một thư mục dự án kiểu tap-x/{2-ban-day-du,3-doan-noi-bat} hoặc phẳng (vlog/x, edit-…)."""
    base = os.path.join(ROOTS[root][0], rel)
    t.src.append(ROOTS[root][1])
    dai = os.path.join(rel, "2-ban-day-du") if os.path.isdir(os.path.join(base, "2-ban-day-du")) else None
    if not dai and not os.path.isdir(os.path.join(base, "3-doan-noi-bat")): dai = rel          # dự án phẳng
    for sub in ([dai] if dai else []) + [os.path.join(rel, d) for d in ls(base) if d not in ("2-ban-day-du", "3-doan-noi-bat") and d not in BO and os.path.isdir(os.path.join(base, d))]:
        b = os.path.join(ROOTS[root][0], sub)
        for f in ls(b):
            r = os.path.join(sub, f); fl = f.lower()
            if fl.endswith(VID) and ("final" in fl or sub != rel): t.add(t.dai_vid, root, r)
            elif fl.endswith(IMG) and "@160" not in fl and sub != rel: t.add(t.anh_nho, root, r)
            elif fl.endswith((".md", ".txt")) and fl not in ("nguon-anh.txt", "loai.txt", "phong-cach.md", "quy-trinh.md"): t.add(t.dai_txt, root, r)
        ph = os.path.join(b, "phat-hanh")
        for f in ls(ph):
            r = os.path.join(sub, "phat-hanh", f); fl = f.lower()
            if fl.endswith(VID): t.add(t.dai_vid, root, r)
            elif fl.endswith(IMG) and "@160" not in fl: t.add(t.anh_nho, root, r)
            elif fl.endswith((".md", ".txt")): t.add(t.dai_txt, root, r)
    hl = os.path.join(rel, "3-doan-noi-bat"); hb = os.path.join(ROOTS[root][0], hl)
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
            elif fl.endswith(IMG) and "@160" not in fl: t.add(t.anh_nho, "xong", r)
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
            if os.path.isdir(p) and not v.startswith("_") and re.fullmatch(r"[a-z0-9-]+", v) and (isf(os.path.join(p, "video-hoan-chinh.mp4")) or os.path.isdir(os.path.join(p, "phat-hanh"))):
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
    out = [t for t in taps.values() if t.dai_vid or t.anh_nho or t.dai_txt or any(c["vid"] or c["txt"] for c in t.clips.values())]
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

def nhan_vid(n):
    n = n.lower()
    if "xem" in n or "dien-thoai" in n: return "Bản nhẹ điện thoại"
    if "khong-teaser" in n: return "Bản không teaser"
    return "Bản dài"

def chinh(n): return nhan_vid(n) == "Bản dài"
def la_chon(x): return os.path.basename(x[1]).lower().startswith("thumbnail")
def q(rel): return urllib.parse.quote(rel)

NHAN_TXT = {"phat-hanh.md": "Bài phát hành", "dang-bai.md": "Bài đăng clip", "chuong.txt": "Chương YouTube",
            "ke-hoach-dang.md": "Kế hoạch đăng", "ke-hoach-canh.md": "Kế hoạch cảnh", "ke-hoach-cat.md": "Kế hoạch cắt",
            "ke-hoach-ghep.md": "Kế hoạch ghép", "so-lieu.md": "Số liệu"}

def read(root, rel):
    try: return open(os.path.join(ROOTS[root][0], rel), encoding="utf-8").read()
    except Exception: return ""

def trong(txt):
    """Mẫu số liệu chưa điền?"""
    return "<tên video>" in txt or not re.search(r"\|[^|\n]*\|\s*[^|\s][^|\n]*\|", txt.split("## Sau 7 ngày")[-1].split("\n", 3)[-1])

def sort_txt(lst):
    order = list(NHAN_TXT)
    return sorted(lst, key=lambda x: order.index(os.path.basename(x[1])) if os.path.basename(x[1]) in order else 99)

FOLDER = '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5h4l2 2.5h9A1.5 1.5 0 0 1 21 9v9.5a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18.5z"/></svg><span>Finder</span>'
def fp(x): return f"{x[0]}/{q(x[1])}"

def media_vid(root, rel, nhan, doc=False):
    return (f'<figure class="m{" doc" if doc else ""}"><video controls playsinline preload=none poster="/poster/{root}/{q(rel)}" src="{url(root, rel)}"></video>'
            f'<figcaption>{esc(nhan)}</figcaption><button class=fd onclick="finder(\'{root}/{q(rel)}\',event)" title="Mở trong Finder">{FOLDER}</button></figure>')

def media_img(root, rel, nhan):
    return (f'<figure class=m><img loading=lazy src="{url(root, rel)}" onclick="anh(this.src)" alt="">'
            f'<figcaption>{esc(nhan)}</figcaption><button class=fd onclick="finder(\'{root}/{q(rel)}\',event)" title="Mở trong Finder">{FOLDER}</button></figure>')

def nut(nhan, onclick, tat=False):
    return f'<button class=f{" tat" if tat else ""} onclick="{esc(onclick)}"{" disabled" if tat else ""}>{esc(nhan)}</button>'

def status_html(t):
    out = ""
    for r in t.danh_muc:
        cells = "".join(f"<div><span>{esc(k)}</span>{inline(esc(v))}</div>" for k, v in r.items() if v and k != "Tài nguyên")
        out += f'<div class=res>{inline(esc(r.get("Tài nguyên", "")))}</div><div class=kv>{cells}</div>'
    return out

def section(t):
    k = t.key
    thumbs = sorted(t.anh_nho, key=lambda x: not la_chon(x))
    bia = [x for x in thumbs if la_chon(x)][:1] or thumbs          # đã chọn → chỉ hiện ảnh chọn; chưa chọn → hiện mọi phương án
    dai = [x for x in t.dai_vid if chinh(x[1])] or t.dai_vid[:1]
    strip = "".join(media_vid(*x, "Bản dài") for x in dai)
    for c in sorted(t.clips):
        v = t.clips[c]["vid"]
        strip += media_vid(*v[-1], f"Clip {c}", doc=True) if v else f'<figure class="m doc cho"><div>Clip {c}<br><small>đang dựng</small></div><figcaption>Clip {c}</figcaption></figure>'
    strip += "".join(media_img(*x, "Bìa đã chọn" if la_chon(x) else f"Bìa {i + 1}" if len(bia) > 1 else "Bìa") for i, x in enumerate(bia))
    # Tài liệu: ẩn sau một nút
    files, da = [], set()
    for x in sort_txt(t.dai_txt + t.hl_txt):
        f = os.path.basename(x[1]); txt = read(*x)
        if not txt.strip() or f in da: continue   # cùng tên ở hai nguồn (dự án + thanh-pham) → giữ bản đọc trước
        da.add(f)
        nhan = NHAN_TXT.get(f, f)
        if f == "so-lieu.md" and trong(txt): files.append(nut(f"{nhan}: chưa có", "", True)); continue
        files.append(nut(nhan, f"xem('/doc/{x[0]}/{q(x[1])}','{esc(ten(t))} · {nhan}','{fp(x)}')"))
    for c in sorted(t.clips):
        for x in t.clips[c]["txt"]: files.append(nut(f"Lời clip {c}", f"xem('/doc/{x[0]}/{q(x[1])}','{esc(ten(t))} · Lời clip {c}','{fp(x)}')"))
    for x in t.dai_vid:
        if x not in dai: files.append(nut(nhan_vid(x[1]), f"phat('{url(*x)}','{fp(x)}')"))
    for i, x in enumerate(thumbs):
        if x not in bia: files.append(nut(f"Bìa phương án {i}", f"anh('{url(*x)}','{fp(x)}')"))
    if t.danh_muc: files.insert(0, nut("Lọc & trạng thái", f"xemTpl('st-{k}','{esc(ten(t))} · Lọc & trạng thái')"))
    tt = t.danh_muc[-1].get("Trạng thái", "") if t.danh_muc else ""
    goc = (dai + [v for c in t.clips.values() for v in c["vid"]] + t.anh_nho + t.dai_txt + t.hl_txt)[:1]
    thu_muc = (f'<button class="more fdir" onclick="finder(\'{goc[0][0]}/{q(goc[0][1].split("/")[0])}\',event)" title="Mở thư mục tập trong Finder">{FOLDER}</button>' if goc else "")
    chip = f'<span class=chip title="{esc(re.sub(r"[`*]", "", tt))}">{esc(re.sub(r"[`*]", "", tt))}</span>' if tt else ""
    so = len([f for f in files if "disabled" not in f])
    return (f'<section class=tap id="tap-{esc(k)}" data-thu="{1 if nhom(k) else 0}" data-q="{esc((ten(t) + " " + k + " " + tt).lower())}">'
            f'<div class=hd><h2>{esc(ten(t))}</h2>{chip}'
            f'{f"<button class=more onclick=mo(this)>Tài liệu · {so}</button>" if files else ""}{thu_muc}</div>'
            f'<div class=strip>{strip or "<div class=trong>Chưa có video</div>"}</div>'
            f'<div class=files hidden>{"".join(files)}</div>'
            f'{f"<template id=st-{esc(k)}>{status_html(t)}</template>" if t.danh_muc else ""}</section>')

def page_home(taps):
    n = sum(1 for t in taps if not nhom(t.key)); m = len(taps) - n
    return (f'<header><h1>Kết quả video</h1><a class=nav href=/bai-dang>Bài đăng →</a><a class=nav href=/mac>Video trên Mac →</a><span class=dem>{n} video</span>'
            f'<input id=q type=search placeholder="Tìm…" oninput="loc()">'
            f'{f"<label class=thu><input type=checkbox id=thu onchange=loc()> Bản thử ({m})</label>" if m else ""}</header>'
            + "".join(section(t) for t in taps)
            + '<dialog id=dlg><div class=dh><b id=dt></b><button id=dfd onclick="finder(fpHien,event)">Mở trong Finder</button><button id=cp onclick="chep()">Chép</button><button onclick="dlg.close()" aria-label="Đóng">✕</button></div><div id=db></div></dialog>')

CSS = """
:root{--bg:#121216;--card:#1c1c22;--card2:#26262e;--tx:#ececf1;--dim:#8d8d99;--ac:#ff7a2f;--bd:#2c2c36;--h:230px}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 -apple-system,system-ui,sans-serif}
main{max-width:1400px;margin:0 auto;padding:0 20px 80px}
header{position:sticky;top:0;z-index:5;background:rgba(18,18,22,.92);backdrop-filter:blur(10px);display:flex;align-items:center;gap:14px;flex-wrap:wrap;padding:14px 0;margin-bottom:6px;border-bottom:1px solid var(--bd)}
h1{margin:0;font-size:20px;letter-spacing:.01em} .nav{color:var(--ac);text-decoration:none;font-size:14px;border:1px solid var(--bd);border-radius:999px;padding:4px 12px} .nav:hover{border-color:var(--ac)} .dem{color:var(--dim);font-size:13px}
#q{margin-left:auto;width:220px;padding:7px 12px;border-radius:8px;border:1px solid var(--bd);background:var(--card);color:var(--tx);font-size:14px}
.thu{color:var(--dim);font-size:13px;display:flex;gap:6px;align-items:center;cursor:pointer}
.tap{padding:22px 0 8px;border-bottom:1px solid var(--bd)} .tap[hidden]{display:none}
.hd{display:flex;align-items:center;gap:10px;margin-bottom:12px;min-width:0}
h2{margin:0;font-size:17px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:none;max-width:60%}
.chip{color:var(--dim);font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;flex:1}
.more{flex:none;margin-left:auto;background:var(--card2);color:var(--tx);border:1px solid var(--bd);border-radius:999px;padding:5px 14px;font-size:13px;cursor:pointer}
.more:hover,.more.on{border-color:var(--ac);color:var(--ac)}
.strip{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x proximity;padding-bottom:8px;scrollbar-width:thin}
.m{margin:0;flex:none;scroll-snap-align:start;position:relative}
.m video,.m img{display:block;height:var(--h);width:auto;max-width:min(86vw,520px);aspect-ratio:16/9;object-fit:cover;border-radius:10px;background:#000;cursor:pointer}
.m.doc video{aspect-ratio:9/16} .m img{object-fit:contain;background:#000}
.m figcaption{position:absolute;left:8px;top:8px;background:rgba(0,0,0,.6);color:#fff;font-size:11.5px;font-weight:600;padding:2px 8px;border-radius:6px;pointer-events:none}
.fd{position:absolute;right:8px;top:8px;display:flex;gap:4px;align-items:center;background:rgba(0,0,0,.6);color:#fff;border:0;border-radius:6px;padding:3px 8px;font-size:11.5px;font-weight:600;cursor:pointer}
.fd:hover,.fdir:hover{background:var(--ac);color:#fff} .fd.ok,.fdir.ok{background:#2e9e5b;color:#fff}
.fdir{display:flex;align-items:center;gap:4px;padding:5px 10px} .m.doc .fd span{display:none}
.m video:not([data-play]) + figcaption{opacity:1} .m video[data-play] + figcaption{opacity:0}
.cho div{height:var(--h);aspect-ratio:9/16;border:1px dashed var(--bd);border-radius:10px;display:flex;align-items:center;justify-content:center;text-align:center;color:var(--dim);font-size:14px}
.trong{color:var(--dim);font-size:13px;padding:10px 0}
.files[hidden]{display:none} .files{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 10px}
.f{background:var(--card);color:var(--tx);border:1px solid var(--bd);border-radius:8px;padding:6px 12px;font-size:13px;cursor:pointer}
.f:hover{border-color:var(--ac)} .f.tat{color:var(--dim);cursor:default;border-style:dashed}
dialog{width:min(860px,94vw);max-height:88vh;padding:0;border:1px solid var(--bd);border-radius:14px;background:var(--card);color:var(--tx)}
dialog::backdrop{background:rgba(0,0,0,.7)}
.dh{position:sticky;top:0;display:flex;gap:10px;align-items:center;padding:12px 16px;background:var(--card);border-bottom:1px solid var(--bd)}
.dh b{flex:1;font-size:14px} .dh button{background:var(--card2);color:var(--tx);border:1px solid var(--bd);border-radius:8px;padding:4px 12px;cursor:pointer;font-size:13px}
#db{padding:6px 20px 20px;overflow:auto} #db img,#db video{max-width:100%;max-height:78vh;display:block;margin:10px auto;border-radius:8px}
#db h3,#db h4,#db h5{color:var(--ac);margin:18px 0 6px} #db p{margin:6px 0} #db .li{margin:2px 0 2px 8px} code{color:var(--ac)}
pre{white-space:pre-wrap;font:13px/1.6 ui-monospace,monospace} .tw{overflow-x:auto} table{border-collapse:collapse;margin:8px 0;font-size:13px}
td,th{border:1px solid var(--bd);padding:4px 8px;text-align:left;vertical-align:top}
.res{font-weight:600;margin:14px 0 8px} .kv{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px 16px;font-size:14px}
.kv span{display:block;color:var(--dim);font-size:12px}
@media(max-width:700px){:root{--h:190px} main{padding:0 16px 60px} #q{width:100%;margin-left:0;order:3} h2{max-width:100%;white-space:normal} .hd{flex-wrap:wrap} .chip{flex-basis:100%;order:3}}
"""
JS = r"""
const dlg=document.getElementById('dlg'),dt=document.getElementById('dt'),db=document.getElementById('db'),cpb=document.getElementById('cp');
function mo(b){const f=b.closest('.tap').querySelector('.files');f.hidden=!f.hidden;b.classList.toggle('on',!f.hidden)}
let fpHien='';const dfd=document.getElementById('dfd');
function hien(t,html,chep,fp){dt.textContent=t;db.innerHTML=html;cpb.hidden=!chep;fpHien=fp||'';dfd.hidden=!fp;dlg.showModal();db.scrollTop=0}
async function xem(u,t,fp){hien(t,'<p style="color:var(--dim)">Đang mở…</p>',true,fp);db.innerHTML=await (await fetch(u)).text()}
function finder(p,e){e&&(e.preventDefault(),e.stopPropagation());const b=e&&e.currentTarget;fetch('/finder/'+p,{method:'POST'}).then(r=>{if(b){const o=b.innerHTML;b.classList.add('ok');setTimeout(()=>b.classList.remove('ok'),1200)}})}
function xemTpl(id,t){hien(t,document.getElementById(id).innerHTML,true)}
function anh(u,fp){hien('Ảnh bìa','<img src="'+u+'">',false,fp)}
function phat(u,fp){hien('Video','<video controls autoplay playsinline src="'+u+'"></video>',false,fp)}
function chep(){navigator.clipboard.writeText(db.innerText).then(()=>{cpb.textContent='Đã chép';setTimeout(()=>cpb.textContent='Chép',1500)})}
dlg.addEventListener('close',()=>{db.querySelectorAll('video').forEach(v=>v.pause())});
dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()});
document.addEventListener('play',e=>{document.querySelectorAll('video').forEach(v=>{if(v!==e.target)v.pause()});e.target.dataset.play=1},true);
// khung đúng tỉ lệ thật của video (ngang/dọc) theo ảnh đại diện
document.querySelectorAll('.m video').forEach(v=>{const i=new Image();i.onload=()=>{v.style.aspectRatio=i.naturalWidth+'/'+i.naturalHeight};i.src=v.poster});
document.querySelectorAll('.m img').forEach(i=>{const f=()=>{i.style.aspectRatio=i.naturalWidth+'/'+i.naturalHeight};i.complete?f():i.onload=f});
function loc(){const s=document.getElementById('q').value.toLowerCase().trim(),c=document.getElementById('thu'),thu=c&&c.checked;
 document.querySelectorAll('.tap').forEach(t=>{t.hidden=(t.dataset.thu==='1'&&!thu)||(s&&!t.dataset.q.includes(s))})}
loc();
if(location.hash){const e=document.querySelector(location.hash);e&&e.scrollIntoView()}
"""

def doc_html(root, rel):
    txt = read(root, rel)
    return f"<pre>{esc(txt)}</pre>" if rel.endswith(".txt") else md(txt)

def page(sel):
    taps = tap_all()
    return (f'<!doctype html><html lang=vi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
            f"<title>Kết quả video</title><style>{CSS}</style><main>{page_home(taps)}</main><script>{JS}</script></html>")

# ---------- trang video trên Mac (David 20/11/2026: "sắp xếp để tôi tự kiểm tra nhanh hơn") — chỉ đọc, gọi kiem-video-mac.py ----------
def page_mac():
    import importlib.util
    sp = importlib.util.spec_from_file_location("kiem_video_mac", os.path.join(os.path.dirname(os.path.realpath(__file__)), "kiem-video-mac.py"))
    km = importlib.util.module_from_spec(sp); sp.loader.exec_module(km)
    k = km.kiem()
    head = ('<header><h1>Video trên Mac</h1><a class=nav href=/>← Kết quả video</a>'
            '<span class=dem>chỉ đọc · xoá bằng luu-drive.sh</span></header>')
    if not k["drive"]: body = "<p>⚠️ Google Drive chưa mở, không kiểm được. Mở app Google Drive rồi tải lại trang.</p>"
    elif not k["rows"]: body = "<p>~/Movies không còn tập video nào. Mac đang nhẹ.</p>"
    else:
        tr = "".join(f"<tr><td>{esc(r['tap'])}</td><td>{km.gb(r['size'])}</td><td>{r['render_ok']}/{r['render']}</td>"
                     f"<td>{r['goc_ok']}/{r['goc']}</td><td>{esc(r['ket_luan'])}"
                     + "".join(f"<div class=dem>thiếu: {esc(x)}</div>" for x in (r['thieu_render'] + r['thieu_goc'])[:6]) + "</td></tr>" for r in k["rows"])
        tong = sum(r["xoa_duoc"] for r in k["rows"])
        body = (f"<p>Xoá được ngay: <b>{km.gb(tong)}</b> (nhắn Claude \"dọn Mac\" — chạy luu-drive.sh: chép lên Drive, kiểm, rồi mới xoá).</p>"
                "<div style='overflow-x:auto'><table style='border-collapse:collapse;width:100%'><tr style='text-align:left;color:var(--dim)'>"
                "<th>Tập</th><th>Dung lượng</th><th>Render trên Drive</th><th>Gốc trên Drive</th><th>Kết luận</th></tr>"
                f"{tr}</table></div>")
    return (f'<!doctype html><html lang=vi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
            f"<title>Video trên Mac</title><style>{CSS} td,th{{padding:10px 12px;border-bottom:1px solid var(--bd);vertical-align:top}}</style>"
            f"<main>{head}{body}</main></html>")

# ---------- trang bài đăng (David 17/11/2026: "tạo riêng 1 trang … với đầy đủ mọi thứ trong 1 bài đăng để tôi lên copy nội dung và tự tải ảnh") ----------
# Đọc ~/Documents/1-nghe-nghiep/bai-dang/YYYY-MM-DD/bai.md (đầu file: "# tiêu đề", các dòng ghi chú, "Tệp: <đường dẫn video>" nếu có; sau "---" là chữ đăng)
# + anh.png. Nút Đã đăng ghi file .da-dang trong thư mục ngày. Hệ thống lịch: du-an/lich-dang-bai.md.
MA_BAI = r"(\d{4}-\d{2}-\d{2}|video-san/[a-z0-9-]+)"   # bài theo ngày, hoặc video sẵn (không thuộc lịch)
THU = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ nhật"]

def bai_doc(ngay):
    d = os.path.join(ROOTS["bai"][0], ngay); txt = read("bai", f"{ngay}/bai.md")
    dau, _, than = txt.partition("\n---\n")
    dong = dau.strip().splitlines(); tieu = dong[0].lstrip("# ").strip() if dong else ngay
    ghi = [l for l in dong[1:] if l.strip() and not l.startswith(("Tệp:", "Lọc:"))]
    loc = next((l[4:].strip() for l in dong if l.startswith("Lọc:")), "")   # dòng lọc trùng do lịch thứ 6 ghi
    da = os.path.join(d, ".da-dang"); da_txt = open(da, encoding="utf-8").read().strip() if isf(da) else ""
    tep = next((os.path.expanduser(l[4:].strip()) for l in dong if l.startswith("Tệp:")), "")
    return {"ngay": ngay, "tieu": tieu, "ghi": ghi, "than": than.strip(), "anh": isf(os.path.join(d, "anh.png")),
            "video": tep if isf(tep) else "", "video_thieu": bool(tep) and not isf(tep), "da": isf(da), "tu_dang": "tự đăng" in da_txt, "loc": loc}

def bai_the(b):
    import datetime
    n = b["ngay"]; k = n.replace("/", "-")
    h2 = f'{THU[datetime.date.fromisoformat(n).weekday()]} {datetime.date.fromisoformat(n):%d/%m}' if n[:1].isdigit() else esc(b["tieu"].split(" · ")[0])
    tt = (f'<span class="tt da">{"David tự đăng" if b["tu_dang"] else "Đã đăng"}</span>' if b["da"] else ('<span class=tt>Chờ đăng · 20:00</span>' if n[:1].isdigit() else '<span class=tt>Đăng thêm khi muốn</span>'))
    tt += f'<span class=loc title="{esc(b["loc"])}">Lọc: {esc(b["loc"][:70])}</span>' if b["loc"] else '<span class="loc chua">Chưa lọc trùng</span>'
    media = ""
    if b["video"]:
        media = (f'<div class=bm><video controls preload=metadata playsinline src="/bv/{n}"></video>'
                 f'<a class=f href="/bv/{n}" download="video-{k}.mp4">Tải video</a></div>')
    elif b["anh"]:
        media = (f'<div class=bm><img src="/f/bai/{n}/anh.png" alt="Ảnh bài {n}" onclick="anh(this.src)">'
                 f'<a class=f href="/f/bai/{n}/anh.png" download="anh-{k}.png">Tải ảnh</a></div>')
    else:
        media = f'<div class="bm cho"><div>{"Không thấy tệp video" if b["video_thieu"] else "Chưa có ảnh"}</div></div>'
    ghi = "".join(f"<div>{esc(g)}</div>" for g in b["ghi"])
    return (f'<section class="bai{" xong" if b["da"] else ""}" id="b-{k}"><div class=bh><h2>{h2}</h2>{tt}'
            f'<button class=more onclick="daDang(\'{n}\',this)">{"Bỏ đánh dấu" if b["da"] else "Đã đăng"}</button></div>'
            f'<div class=bt>{esc(b["tieu"])}</div><div class=bb>{media}<div class=bc>'
            f'<pre class=noi id="n-{k}">{esc(b["than"])}</pre><button class=chepb onclick="chepBai(\'{k}\',this)">Chép bài</button>'
            f'{f"<details><summary>Ghi chú soạn</summary>{ghi}</details>" if ghi else ""}</div></div></section>')

def page_bai():
    goc = ROOTS["bai"][0]
    ngay = [d for d in ls(goc) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) and isf(os.path.join(goc, d, "bai.md"))]
    bai = [bai_doc(d) for d in ngay]; cho = [b for b in bai if not b["da"]]; xong = [b for b in bai if b["da"]]   # đã đăng: ẩn, chỉ đếm (David 17/11)
    vs = [bai_doc("video-san/" + d) for d in ls(os.path.join(goc, "video-san")) if isf(os.path.join(goc, "video-san", d, "bai.md"))]
    vs = [b for b in vs if not b["da"]]
    kho = [f for f in ls(os.path.join(goc, "kho-bai-nen")) if f.endswith(".md")]
    than = (f'<header><h1>Bài đăng Facebook cá nhân</h1><a class=nav href=/>← Kết quả video</a>'
            f'<span class=dem>{len(cho)} bài chờ đăng · đã đăng {len(xong)} (ẩn) · kho bài nền {len(kho)}</span></header>'
            '<p class=huong>Mỗi bài: bấm <b>Chép bài</b> → dán vào Facebook · <b>Tải ảnh</b> (hay video) → đính kèm · đăng xong bấm <b>Đã đăng</b>.</p>'
            + ("".join(bai_the(b) for b in cho) or "<div class=trong>Chưa có bài chờ đăng.</div>")
            + (f'<h3 class=nhom>Video sẵn ({len(vs)}) · không thuộc lịch 4 bài/tuần, đăng thêm khi muốn</h3>' + "".join(bai_the(b) for b in vs) if vs else "")
            + '<dialog id=dlg><div class=dh><b id=dt></b><button id=dfd hidden></button><button id=cp hidden></button><button onclick="dlg.close()" aria-label="Đóng">✕</button></div><div id=db></div></dialog>')
    return (f'<!doctype html><html lang=vi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'
            f"<title>Bài đăng</title><style>{CSS}{CSS_BAI}</style><main>{than}</main><script>{JS_BAI}</script></html>")

CSS_BAI = """
.huong{color:var(--dim);font-size:13.5px;margin:10px 0 0}
.bai{padding:22px 0;border-bottom:1px solid var(--bd)} .bai.xong{opacity:.55}
.bh{display:flex;align-items:center;gap:12px;flex-wrap:wrap} .bh h2{max-width:none}
.tt{font-size:12.5px;color:var(--ac);border:1px solid var(--ac);border-radius:999px;padding:2px 10px} .tt.da{color:#2e9e5b;border-color:#2e9e5b}
.loc{font-size:12px;color:#7fc8a9;border:1px solid #2f5f4c;border-radius:999px;padding:2px 10px;max-width:52ch;overflow:hidden;text-overflow:ellipsis;white-space:nowrap} .loc.chua{color:var(--dim);border-color:var(--bd)}
.bt{color:var(--dim);font-size:13px;margin:6px 0 14px}
.bb{display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap}
.bm{flex:none;display:flex;flex-direction:column;gap:8px;align-items:flex-start}
.bm img,.bm video{width:300px;max-width:86vw;border-radius:10px;background:#000;display:block;cursor:zoom-in}
.bm.cho div{width:300px;height:200px} .bm .f{text-decoration:none}
.bc{flex:1;min-width:260px} .noi{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:14px 16px;margin:0 0 10px;font:15px/1.6 -apple-system,system-ui,sans-serif;max-height:460px;overflow:auto}
.chepb{background:var(--ac);color:#fff;border:0;border-radius:8px;padding:8px 18px;font-size:14px;font-weight:600;cursor:pointer} .chepb.ok{background:#2e9e5b}
details{margin-top:10px;color:var(--dim);font-size:12.5px} summary{cursor:pointer}
.nhom{color:var(--dim);margin:30px 0 0;font-size:15px}
"""
JS_BAI = r"""
const dlg=document.getElementById('dlg'),dt=document.getElementById('dt'),db=document.getElementById('db');
function anh(u){dt.textContent='Ảnh';db.innerHTML='<img src="'+u+'">';dlg.showModal()}
dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()});
function chepBai(n,b){const t=document.getElementById('n-'+n).innerText;
 const ok=()=>{b.textContent='Đã chép';b.classList.add('ok');setTimeout(()=>{b.textContent='Chép bài';b.classList.remove('ok')},1500)};
 if(navigator.clipboard)navigator.clipboard.writeText(t).then(ok);else{const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove();ok()}}
function daDang(n,b){fetch('/da-dang/'+n,{method:'POST'}).then(r=>{if(r.ok)location.reload()})}
"""

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
        if u.path.startswith("/?") or (u.path == "/" and "tap=" in u.query):   # link cũ ?tap=x → neo #tap-x
            t = urllib.parse.parse_qs(u.query).get("tap", [""])[0]
            self.send_response(302); self.send_header("Location", f"/#tap-{urllib.parse.quote(t)}"); self.end_headers(); return
        if u.path.rstrip("/") == "/mac":
            try: b = page_mac().encode()
            except Exception as e: b = f"<pre>Lỗi kiểm video trên Mac: {esc(e)}</pre>".encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
            return self.wfile.write(b)
        if u.path.rstrip("/") == "/bai-dang":
            try: b = page_bai().encode()
            except Exception as e: b = f"<pre>Lỗi đọc bài đăng: {esc(e)}</pre>".encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
            return self.wfile.write(b)
        if u.path.startswith("/bv/"):   # /bv/<ngày> hoặc /bv/video-san/<tên>   # video của bài: đường dẫn lấy từ dòng "Tệp:" trong bai.md, không nhận đường dẫn từ ngoài
            n = urllib.parse.unquote(u.path[4:])
            if not re.fullmatch(MA_BAI, n): return self.send_error(404)
            v = bai_doc(n)["video"]
            return self.send_file(v) if v else self.send_error(404)
        if u.path.startswith(("/f/", "/poster/", "/doc/")):
            kind, rid, rel = u.path[1:].split("/", 2) if u.path.count("/") > 2 else ("", "", "")
            if rid not in ROOTS: return self.send_error(404)
            base = os.path.realpath(ROOTS[rid][0]); p = os.path.realpath(os.path.join(base, urllib.parse.unquote(rel)))
            if not p.startswith(base + os.sep) or not os.path.isfile(p): return self.send_error(404)
            if kind == "doc":
                b = doc_html(rid, os.path.relpath(p, base)).encode()
                self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
                return self.wfile.write(b)
            return self.send_file(poster(p) if kind == "poster" else p)
        try: b = page(urllib.parse.parse_qs(u.query).get("tap", [""])[0]).encode()
        except Exception as e: b = f"<pre>Lỗi đọc kết quả: {esc(e)}</pre>".encode()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
        self.wfile.write(b)
    def do_POST(self):   # nút "Finder": hiện file trong Finder (máy chủ chỉ nghe 127.0.0.1)
        u = urllib.parse.urlparse(self.path)
        if u.path.startswith("/da-dang/"):   # bật / tắt dấu đã đăng của một bài
            n = urllib.parse.unquote(u.path[9:]); d = os.path.join(ROOTS["bai"][0], n)
            if not re.fullmatch(MA_BAI, n) or not os.path.isdir(d): return self.send_error(404)
            m = os.path.join(d, ".da-dang")
            if isf(m): os.remove(m)
            else: open(m, "w").write(time.strftime("%Y-%m-%d %H:%M\n"))
            self.send_response(204); self.end_headers(); return
        if not u.path.startswith("/finder/"): return self.send_error(404)
        rid, _, rel = u.path[8:].partition("/")
        if rid not in ROOTS: return self.send_error(404)
        base = os.path.realpath(ROOTS[rid][0]); p = os.path.realpath(os.path.join(base, urllib.parse.unquote(rel)))
        if not p.startswith(base + os.sep) or not os.path.exists(p): return self.send_error(404)
        import subprocess; subprocess.run(["open", "-R", p])
        self.send_response(204); self.end_headers()
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
