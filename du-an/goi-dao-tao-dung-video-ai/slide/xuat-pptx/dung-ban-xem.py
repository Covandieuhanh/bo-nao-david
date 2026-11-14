# dung-ban-xem.py <thư mục slide-ban-xem>
# Dựng lại bai-1…8.html (bản xem trên máy, nguồn để chụp ra pptx) từ mã gốc trong repo:
# giao-dien-slide.css + bai-N/deck.json (thứ tự) + bai-N/trang-trinh-chieu/*.html. Ảnh /_blob/… đổi sang anh/… theo anh-blob.json.
# Lần đầu (chưa có anh-blob.json) thì dò ánh xạ từ bản xem cũ.
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
OUT = os.path.expanduser(sys.argv[1]); MAPF = os.path.join(HERE, "anh-blob.json")
SEC = re.compile(r'<section id="([^"]+)".*?</section>', re.S)
SRC = re.compile(r'src="([^"]+)"')

def repo_slides(n):
    deck = json.load(open(f"{ROOT}/bai-{n}/deck.json"))
    return deck, [(sid, open(f"{ROOT}/bai-{n}/trang-trinh-chieu/{sid}.html").read()) for sid in deck["order"]]

if os.path.exists(MAPF):
    amap = json.load(open(MAPF))
else:
    amap = {}
    for n in range(1, 9):
        old = open(f"{OUT}/bai-{n}.html").read()
        olds = {m.group(1): m.group(0) for m in SEC.finditer(old)}
        for sid, h in repo_slides(n)[1]:
            if sid in olds:
                for a, b in zip(SRC.findall(h), SRC.findall(olds[sid])):
                    if a.startswith("/_blob/"): amap[a] = b
    json.dump(amap, open(MAPF, "w"), indent=1, sort_keys=True)

css = open(f"{ROOT}/giao-dien-slide.css").read()
HEAD = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{t}</title>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap">\n'
        "<style>body{{margin:0;background:#2b2f36;font-family:'Be Vietnam Pro',Arial,sans-serif}} p,h1,h2,h3{{margin:0}} x-shape,x-icon{{display:block}}\n")
TAIL = ("\nsection{width:1920px;height:1080px;position:relative;overflow:hidden} .wrap{zoom:.5;margin:40px auto;width:1920px}\n"
        ".ghichu{font-size:28px;color:#C9D3DC;padding:20px 8px;line-height:1.5}\n"
        "x-shape[kind=ellipse]{border-radius:50%} x-shape[kind=arrow-right]{clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%)} x-shape[kind=arrow-down]{clip-path:polygon(30% 0,70% 0,70% 60%,100% 60%,50% 100%,0 60%,30% 60%)}\n"
        "x-icon{background:currentColor;border-radius:8px;opacity:.85}</style></head><body>")
for n in range(1, 9):
    deck, slides = repo_slides(n); parts = []
    for sid, h in slides:
        m = re.search(r"<aside>(.*?)</aside>", h, re.S); note = m.group(1).strip() if m else ""
        h = re.sub(r"<aside>.*?</aside>\s*", "", h, flags=re.S)
        h = SRC.sub(lambda m: f'src="{amap.get(m.group(1), m.group(1))}"', h)
        parts.append(f'<div class="wrap">{h.strip()}\n<p class="ghichu"><b>Ghi chú trainer:</b> {note}</p></div>')
    open(f"{OUT}/bai-{n}.html", "w").write(HEAD.format(t=deck["title"]) + css + TAIL + "".join(parts) + "</body></html>")
    print(n, len(slides))
