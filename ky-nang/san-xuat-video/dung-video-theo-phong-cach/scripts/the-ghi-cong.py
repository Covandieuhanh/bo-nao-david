# Ghi nguồn ảnh (bắt buộc với ảnh CC BY / BY-SA), chỉ ảnh thực sự dùng trong canh.js: the-ghi-cong.py <dự án> [--card]
#   mặc định: <dự án>/nguon-anh.txt để dán vào MÔ TẢ bài đăng — video KHÔNG có màn hình nguồn ảnh ở cuối (người dùng chốt)
#   --card:   thêm màn hình 5 s davinci/media/nguon_anh.png ở cuối video (chỉ khi người dùng yêu cầu; cần Pillow → không -I)
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _chung import load, safe_zone

P = os.path.expanduser(sys.argv[1])
d_ = load(P); W, H = d_["out"]["width"], d_["out"]["height"]   # khung xuất
used = set(re.findall(r'"photo":\s*"([^"]+)\.jpg"', json.dumps(d_["scenes"])))
rows = [l.split("\t", 1)[1] for l in open(os.path.join(P, "images/credits.tsv")).read().splitlines()
        if l.strip() and l.split("\t")[0] in used]
out = os.path.join(P, "davinci/media/nguon_anh.png")
txt = os.path.join(P, "nguon-anh.txt")
for f in (out, txt):
    if os.path.exists(f): os.remove(f)
if not rows:
    print("Không dùng ảnh nào → không cần ghi nguồn"); sys.exit()
open(txt, "w", encoding="utf-8").write("Nguồn ảnh minh hoạ:\n" + "\n".join("- " + r for r in rows) + "\n")
if "--card" not in sys.argv:
    print(txt, len(rows), "ảnh (dán vào mô tả bài đăng)"); sys.exit()
from PIL import Image, ImageDraw, ImageFont
Z = safe_zone(W, H)
F = "/System/Library/Fonts/Supplemental/"
title_f = ImageFont.truetype(F + "Arial Bold.ttf", round(W * 0.05))
size = round(W * 0.023)
img = Image.new("RGB", (W, H), (13, 13, 16))
d = ImageDraw.Draw(img)

def site(url):
    return "Wikimedia Commons" if "wikimedia" in url else "StockSnap" if "stocksnap" in url else \
        "rawpixel" if "rawpixel" in url else re.sub(r"https?://(www\.)?([^/]+).*", r"\2", url)

def lines_for(f):
    out = []
    for r in rows:
        title, author, lic, url = [p.strip() for p in r.split(" — ")]
        title = re.sub(r"\.(jpe?g|png|webp)$", "", title.strip('"').replace("File:", ""), flags=re.I)
        if len(title) > 42: title = title[:40].rstrip() + "…"
        words, cur, block = f"{title} — {author} — {lic} ({site(url)})".split(), "", []
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) <= Z["right"] - Z["left"]: cur = t
            else: block.append(cur); cur = w
        block.append(cur); out.append(block)
    return out

while True:   # thu nhỏ chữ tới khi vừa vùng an toàn
    f = ImageFont.truetype(F + "Arial Unicode.ttf", size)
    blocks = lines_for(f)
    need = sum(len(b) for b in blocks) * size * 1.32 + len(blocks) * size * 0.55
    if Z["top"] + title_f.size * 2 + need < Z["bottom"] - size * 2 or size <= 14: break
    size -= 1
d.text((Z["left"], Z["top"] + title_f.size // 2 + 10), "Nguồn ảnh minh hoạ", font=title_f, fill="white", anchor="lm")
y = Z["top"] + title_f.size * 2
for b in blocks:
    for ln in b:
        d.text((Z["left"], y), ln, font=f, fill=(225, 225, 225)); y += round(size * 1.32)
    y += round(size * 0.55)
d.text((Z["left"], Z["bottom"] - size), "Ảnh có giấy phép Creative Commons / phạm vi công cộng", font=f, fill=(150, 150, 150), anchor="lm")
img.save(out); print(out, len(rows), "ảnh, cỡ chữ", size)
