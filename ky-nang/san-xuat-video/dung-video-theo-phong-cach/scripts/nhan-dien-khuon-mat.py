"""Dò mặt cho máy không phải Mac (Windows qua WSL2, Linux): cùng cách gọi, cùng định dạng ra với nhan-dien-khuon-mat.swift (Vision).
  python nhan-dien-khuon-mat.py <thư mục khung .jpg> <file json ra>
Mỗi khung: [{x, y, w, h (0–1, gốc trên-trái), m (độ mở miệng / chiều cao mặt)}].
Hai bước: (1) YuNet (OpenCV) tìm khung mặt, bắt được cả mặt nhỏ trong khung 360 px; (2) MediaPipe Face Landmarker đọc viền môi
trên phần mặt đã phóng to → độ mở miệng. Mô hình ở ~/.cache/dung-video-theo-phong-cach/ (cai-cong-cu-video.sh tải).
Khung mặt quy đổi theo thước của Vision bằng he-so-mat.json (đo trên Mac bằng cùng bộ khung: do-he-so-mat.py cạnh file này)
để bố cục tránh mặt ra giống máy Mac. Gọi qua do-mat.sh (tự chọn Vision trên Mac, file này ở máy khác)."""
import json, os, sys

import cv2
try:
    import mediapipe as mp          # đo độ mở miệng; máy Windows / Linux chip ARM chưa có bản MediaPipe → chỉ dò khung mặt (m = 0)
except ImportError:
    mp = None

CACHE = os.path.expanduser("~/.cache/dung-video-theo-phong-cach")
YUNET = os.path.join(CACHE, "face_detection_yunet_2023mar.onnx")
LANDMARK = os.path.join(CACHE, "face_landmarker.task")
HE_SO = {"cx": 0.0, "cy": 0.0, "sw": 1.0, "sh": 1.0, "m": 1.0, "nguong": 0.9}
_hs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "he-so-mat.json")
if os.path.exists(_hs):
    HE_SO.update({k: v for k, v in json.load(open(_hs, encoding="utf-8")).items() if k in HE_SO})
MOI_TRONG = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95]   # viền môi trong
PHONG = 2          # phóng khung lên 2 lần trước khi dò (mặt 20 px → 40 px)
# nguong 0.9: đo trên 255 khung, khớp Vision ~90% (Vision bỏ sót mặt nghiêng, YuNet vẫn bắt; ngưỡng thấp hơn thì thêm mặt giả)


def mo_mieng(lm, img, x, y, w, h):
    """Độ mở miệng / chiều cao mặt, đọc trên phần mặt phóng to 256 px (khung vuông, chừa lề 40%)."""
    H, W = img.shape[:2]
    c = max(w, h) * 1.8
    x0, y0 = int(max(0, x + w / 2 - c / 2)), int(max(0, y + h / 2 - c / 2))
    x1, y1 = int(min(W, x + w / 2 + c / 2)), int(min(H, y + h / 2 + c / 2))
    if x1 - x0 < 4 or y1 - y0 < 4:
        return 0.0
    crop = cv2.resize(img[y0:y1, x0:x1], (256, 256), interpolation=cv2.INTER_CUBIC)
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)))
    if not r.face_landmarks:
        return 0.0
    pts = r.face_landmarks[0]
    ly = [pts[i].y for i in MOI_TRONG]
    fy = [p.y for p in pts]
    return (max(ly) - min(ly)) / max(1e-6, max(fy) - min(fy))


def main(d, out):
    files = sorted(f for f in os.listdir(d) if f.endswith(".jpg"))
    det = None
    res = []
    if mp is None:
        print("⚠ thiếu MediaPipe: chỉ dò khung mặt, không đo độ mở miệng (đoán người nói kém hơn)", file=sys.stderr)
    lm = mp.tasks.vision.FaceLandmarker.create_from_options(mp.tasks.vision.FaceLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=LANDMARK), num_faces=1)) if mp else None
    try:
        for f in files:
            img = cv2.imread(os.path.join(d, f))
            H, W = img.shape[:2]
            big = cv2.resize(img, (W * PHONG, H * PHONG), interpolation=cv2.INTER_CUBIC)
            if det is None:
                det = cv2.FaceDetectorYN.create(YUNET, "", (W * PHONG, H * PHONG), HE_SO["nguong"], 0.3, 50)
            det.setInputSize((W * PHONG, H * PHONG))
            _, found = det.detect(big)
            faces = []
            for row in (found if found is not None else []):
                x, y, w, h = [float(v) / PHONG for v in row[:4]]
                cx, cy = x + w / 2 + HE_SO["cx"] * w, y + h / 2 + HE_SO["cy"] * h
                ww, hh = w * HE_SO["sw"], h * HE_SO["sh"]
                m = mo_mieng(lm, img, x, y, w, h) * HE_SO["m"] if lm else 0.0
                faces.append({"x": (cx - ww / 2) / W, "y": (cy - hh / 2) / H, "w": ww / W, "h": hh / H, "m": m})
            res.append(faces)
    finally:
        if lm: lm.close()
    json.dump(res, open(out, "w"))
    print(f"{len(files)} khung")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
