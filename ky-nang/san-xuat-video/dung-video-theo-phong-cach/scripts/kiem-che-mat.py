#!/usr/bin/env python3
"""Kiểm lớp hiệu ứng có che mặt người nào không (luật "không che mặt", nhu-cau-nguoi-xem.md mục 0).

  python3 -I kiem-che-mat.py <dự án 2-ban-day-du> chup      → in danh sách <id>@<giây> (đầu · giữa · cuối mỗi cảnh) để chạy
                                                               `node xem-truoc.mjs $(…)` trong chuyen-dong/
  python3 -I kiem-che-mat.py <dự án 2-ban-day-du> kiem [ngưỡng 0.12]
        → đọc ảnh chụp kiem-tra/chuyen-dong/<id>@<giây>.png (PNG trong suốt) và mặt dò được ở kiem-tra/khuon-mat/khuon-mat.json
          (2 khung mỗi giây, vi-tri-khuon-mat.sh), đo độ phủ trung bình của lớp hiệu ứng trên từng khung mặt (nới 15%).
          Cảnh phủ kín khung (người đã được đưa vào ô, màn chương, toàn màn hình) thì bỏ qua: mặt nằm trong ô video của chính cảnh đó.
          In mặt bị phủ quá ngưỡng; mã thoát 1 nếu có.
Chỉ đọc tệp, không sửa cảnh. Sửa bằng cách đổi phía (`bam`), vùng `o`, hoặc kiểu khác đặt được ở chỗ trống.
"""
import json, os, re, subprocess, sys

def doc_canh(P):
    js = open(os.path.join(P, 'chuyen-dong/src/canh.js'), encoding='utf-8').read()
    m = re.search(r'export const SCENES = (\[.*?\n\]);', js, flags=re.S)
    try:
        return json.loads(m.group(1))
    except ValueError:
        r = subprocess.run(['node', '-e', 'process.stdout.write(JSON.stringify(' + m.group(1) + '))'], capture_output=True, text=True)
        return json.loads(r.stdout)

def trung_binh(png, x, y, w, h, kenh):
    """Giá trị trung bình 0–1 của một kênh (alpha) trong vùng điểm ảnh."""
    vf = f"crop={max(2, w)}:{max(2, h)}:{x}:{y},{kenh},scale=1:1:flags=area,format=gray"
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', png, '-vf', vf, '-f', 'rawvideo', '-'], capture_output=True)
    return r.stdout[0] / 255 if r.stdout else 0.0

def kich_thuoc(png):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', png], capture_output=True, text=True)
    w, h = r.stdout.strip().split(',')[:2]
    return int(w), int(h)

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    P, viec = os.path.expanduser(sys.argv[1]), sys.argv[2]
    SC = doc_canh(P)
    if viec == 'chup':
        moc = []
        for c in SC:
            if c['type'] in ('cta',):
                continue
            a, b = c['start'], c['end']
            moc += [f"{c['id']}@{t:.2f}" for t in (a + min(0.8, (b - a) * 0.15), (a + b) / 2, b - min(0.6, (b - a) * 0.1))]
        print(' '.join(moc))
        return
    nguong = float(sys.argv[3]) if len(sys.argv) > 3 else 0.12
    MAT = json.load(open(os.path.join(P, 'kiem-tra/khuon-mat/khuon-mat.json')))
    K = os.path.join(P, 'kiem-tra/chuyen-dong')
    loi = 0
    for f in sorted(os.listdir(K), key=lambda x: (x.split('@')[0], float(x.split('@')[1][:-4]) if '@' in x else 0)):
        if '@' not in f or not f.endswith('.png'):
            continue
        id_, t = f[:-4].split('@')
        t = float(t)
        png = os.path.join(K, f)
        W, H = kich_thuoc(png)
        if trung_binh(png, 0, 0, W, H, 'alphaextract') > 0.9:
            continue   # phủ kín khung: người đã nằm trong ô video của cảnh
        i = min(len(MAT) - 1, max(0, round(t * 2)))
        for m in MAT[i] or []:
            x, y, w, h = m['x'], m['y'], m['w'], m['h']
            x0, y0 = max(0, x - w * 0.15), max(0, y - h * 0.15)
            x1, y1 = min(1, x + w * 1.15), min(1, y + h * 1.15)
            phu = trung_binh(png, int(x0 * W), int(y0 * H), int((x1 - x0) * W), int((y1 - y0) * H), 'alphaextract')
            if phu > nguong:
                loi += 1
                print(f'!  {id_:22} @{t:7.2f}  mặt ({x + w / 2:.2f}, {y + h / 2:.2f}) bị phủ {phu * 100:.0f}%')
    print(f'Mặt bị phủ quá {nguong * 100:.0f}%: {loi}')
    sys.exit(1 if loi else 0)

if __name__ == '__main__':
    main()
