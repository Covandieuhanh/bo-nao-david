# Ảnh khung an toàn (vùng đỏ = bị giao diện nền tảng che): vung-an-toan.py <dự án>
# Ra tu-lieu/khung-an-toan.png — dùng để kiểm tra khung hình (check_frames, chụp thử).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _chung import load, safe_zone, font_he_thong
from PIL import Image, ImageDraw, ImageFont

P = os.path.expanduser(sys.argv[1])
o = load(P)["out"]; W, H = o["width"], o["height"]
Z = safe_zone(W, H); L, R, T, B = Z["left"], Z["right"], Z["top"], Z["bottom"]
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
red = (255, 40, 40, 90)
d.rectangle((0, 0, W - 1, T), fill=red); d.rectangle((0, B, W - 1, H - 1), fill=red)
d.rectangle((0, T, L, B), fill=(255, 40, 40, 40)); d.rectangle((R, T, W - 1, B), fill=red)
for x in range(L, R, 30):
    for y in (T, B): d.line((x, y, min(x + 15, R), y), fill=(255, 255, 255, 220), width=3)
for y in range(T, B, 30):
    for x in (L, R): d.line((x, y, x, min(y + 15, B)), fill=(255, 255, 255, 220), width=3)
f = ImageFont.truetype(font_he_thong(), round(W * 0.032))
d.text((W // 2, (B + H) // 2), "Tiêu đề, mô tả, nút của nền tảng", font=f, fill=(255, 255, 255, 230), anchor="mm")
if H > W: d.text(((R + W) // 2, H * 0.43), "Nút\nthích\nbình\nluận", font=f, fill=(255, 255, 255, 230), anchor="mm", align="center")
out = os.path.join(P, "tu-lieu/khung-an-toan.png"); img.save(out); print(out)
