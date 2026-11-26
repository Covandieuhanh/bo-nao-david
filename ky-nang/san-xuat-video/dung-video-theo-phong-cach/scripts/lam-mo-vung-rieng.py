#!/usr/bin/env python3
"""Làm mờ vùng riêng tư trên màn hình máy tính / điện thoại trong video quay CẦM TAY (khối 05).

Bám mặt phẳng màn hình bằng đặc trưng SIFT + phép biến đổi phối cảnh (homography) từ vài khung mẫu, nên vùng mờ đi theo màn hình
khi máy rung, phóng gần, ra xa. Chỉ làm mờ đúng vùng khai báo; tiếng giữ nguyên.

Dùng (Python của ~/.cache/dung-video-theo-phong-cach/mat-venv, có OpenCV):
  python -I lam-mo-vung-rieng.py <video-vào> <video-ra> <vung.json>
vung.json:
  {"khoang": [12.5, 56.5],                       # chỉ xử lý trong khoảng giây này của video vào
   "mau": [{"t": 17.2, "vung": [{"ten": "danh-sach", "diem": [[165,640],[525,640],[535,1079],[110,1079]]}]}, …]}
  t = giây của khung mẫu (trong video vào); diem = 4 góc (điểm ảnh) của vùng cần che trên khung mẫu đó.
  Cùng "ten" ở nhiều khung mẫu = cùng một vùng: mỗi khung hình lấy khung mẫu khớp tốt nhất. Màn hình cuộn thì thêm khung mẫu mới.
Ra thêm <video-ra>.log.json (mỗi khung bám được vùng nào). Làm xong PHẢI xem ảnh rải mỗi giây và phóng to chỗ khó.
"""
import json, subprocess, sys
import cv2, numpy as np

vao, ra, cauhinh = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3], encoding='utf-8'))
W, H, FR = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
    'stream=width,height,r_frame_rate', '-of', 'csv=p=0', vao], text=True).split()[0].split(',')[:3]
W, H = int(W), int(H); fps = int(FR.split('/')[0]) / int(FR.split('/')[1])

def khung(t):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', vao, '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                       capture_output=True, check=True).stdout
    return np.frombuffer(p, np.uint8).reshape(H, W, 3)

sift = cv2.SIFT_create(6000)
def dac_trung(anh):
    g = cv2.resize(cv2.cvtColor(anh, cv2.COLOR_BGR2GRAY), (W // 2, H // 2))
    k, d = sift.detectAndCompute(g, None)
    return (np.float32([x.pt for x in k]) * 2 if k else np.zeros((0, 2), np.float32)), d

MAU = [(dac_trung(khung(m['t'])), m['vung']) for m in cauhinh['mau']]
TEN = {v['ten'] for m in cauhinh['mau'] for v in m['vung']}
bf = cv2.BFMatcher()
def bien_doi(a, b):
    (pa, da), (pb, db) = a, b
    if da is None or db is None or len(db) < 8: return None, 0
    m = [x[0] for x in bf.knnMatch(da, db, k=2) if len(x) == 2 and x[0].distance < 0.75 * x[1].distance]
    if len(m) < 12: return None, 0
    Hm, mask = cv2.findHomography(np.float32([pa[x.queryIdx] for x in m]), np.float32([pb[x.trainIdx] for x in m]), cv2.RANSAC, 4)
    return Hm, (0 if Hm is None else int(mask.sum()))

a, b = cauhinh['khoang']
doc = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', vao, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
ghi = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', FR, '-i', '-', '-i', vao,
    '-map', '0:v', '-map', '1:a?', '-vf', 'scale=out_color_matrix=bt709:out_range=tv', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
    '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'copy', ra], stdin=subprocess.PIPE)
n, log, cuoi, ho = 0, [], {}, {k: [] for k in TEN}
while True:
    buf = doc.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy(); t = n / fps
    if a <= t <= b:
        hien = dac_trung(f); tot = {}
        for mau, vung in MAU:
            Hm, khop = bien_doi(mau, hien)
            if Hm is None or khop < 15: continue
            for ten in {v['ten'] for v in vung}:
                ds = [cv2.perspectiveTransform(np.float32(v['diem']).reshape(-1, 1, 2), Hm).reshape(-1, 2) for v in vung if v['ten'] == ten]
                hop_le = all(cv2.isContourConvex(x.astype(np.float32)) and 0 < cv2.contourArea(x.astype(np.float32)) < 0.9 * W * H for x in ds)
                if hop_le and khop > tot.get(ten, (0, None))[0]: tot[ten] = (khop, ds)
        for ten in TEN:
            if ten in tot: cuoi[ten] = (n, tot[ten][1])
        for ten in TEN:   # ghi lại khoảng KHÔNG che được của từng vùng
            if ten not in cuoi or n - cuoi[ten][0] > 20:
                if ho[ten] and t - ho[ten][-1][1] < 0.1: ho[ten][-1][1] = t
                else: ho[ten].append([t, t])
        mask = np.zeros((H, W), np.uint8)
        for m, ds in cuoi.values():
            if n - m <= 20:   # mất bám ngắn (máy lia nhanh) → giữ vị trí cuối tối đa 20 khung
                for x in ds: cv2.fillPoly(mask, [np.clip(x, -4000, 6000).astype(np.int32)], 255)
        if mask.any():
            mask = cv2.dilate(mask, np.ones((9, 9), np.uint8))
            mo = cv2.GaussianBlur(cv2.resize(cv2.resize(f, (W // 12, H // 12), interpolation=cv2.INTER_AREA), (W, H)), (0, 0), 6)
            f[mask > 0] = mo[mask > 0]
        log.append((round(t, 2), {k: v[0] for k, v in tot.items()}))
    ghi.stdin.write(f.tobytes()); n += 1
ghi.stdin.close()
if ghi.wait() or doc.wait(): sys.exit('⛔ ffmpeg lỗi — không dùng video ra')
json.dump(log, open(ra + '.log.json', 'w'))
print('khung', n, '· trong khoảng', len(log), '· khung không bám được vùng nào:', sum(1 for _, x in log if not x))
for ten, ds in sorted(ho.items()):
    for x, y in ds: print(f'⚠ vùng "{ten}" KHÔNG được che {x:.2f}–{y:.2f} s → xem khung đoạn này (vùng có thể đã ra khỏi hình)')
