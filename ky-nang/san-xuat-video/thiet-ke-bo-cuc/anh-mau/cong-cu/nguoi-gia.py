# Người giả + ảnh mẫu cho chup-anh-mau.sh (không dùng mặt thật).
import sys
from PIL import Image, ImageDraw
def khung(W, H, cx, out):
    im = Image.new('RGB', (W, H)); d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H; d.line([(0, y), (W, y)], fill=(int(70 + 40 * t), int(78 + 30 * t), int(92 + 20 * t)))
    d.rectangle([0, int(H * 0.72), W, H], fill=(96, 74, 58))                      # bàn
    s = min(W, H)
    hx, hy, r = int(W * cx), int(H * 0.36), int(s * 0.11)
    d.ellipse([hx - int(r * 2.1), hy + int(r * 1.0), hx + int(r * 2.1), hy + int(r * 5.2)], fill=(214, 168, 92))   # vai, áo
    d.ellipse([hx - r, hy - int(r * 1.2), hx + r, hy + int(r * 1.2)], fill=(236, 200, 170))                        # mặt
    d.pieslice([hx - int(r * 1.05), hy - int(r * 1.35), hx + int(r * 1.05), hy + int(r * 0.6)], 180, 360, fill=(40, 34, 30))   # tóc
    im.save(out, quality=92)
khung(1080, 1920, 0.5, sys.argv[1] + '/nguoi-doc.jpg'); khung(1920, 1080, 0.66, sys.argv[1] + '/nguoi-ngang.jpg')
for i, (a, b) in enumerate([((42, 111, 151), (255, 183, 3)), ((33, 158, 188), (2, 48, 71))]):
    im = Image.new('RGB', (1280, 960), a); d = ImageDraw.Draw(im)
    d.rounded_rectangle([160, 160, 1120, 800], 60, fill=b); d.ellipse([480, 300, 800, 620], fill=a)
    im.save(f'{sys.argv[1]}/anh{i + 1}.jpg', quality=90)
