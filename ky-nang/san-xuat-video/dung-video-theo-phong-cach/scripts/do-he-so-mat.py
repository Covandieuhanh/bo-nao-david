"""CHỈ CHẠY TRÊN MAC: đo hệ số quy đổi để cách dò mặt của máy khác (nhan-dien-khuon-mat.py) ra khung giống Vision của Mac.
  ~/.cache/dung-video-theo-phong-cach/mat-venv/bin/python do-he-so-mat.py <video> [video …]
Lấy 1 khung / 15 giây (360 px như lúc dựng), dò bằng cả hai cách, ghép từng cặp mặt, lấy trung vị độ lệch tâm, tỉ lệ rộng/cao,
tỉ lệ độ mở miệng → ghi he-so-mat.json cạnh file này (đẩy GitHub là mọi máy dùng). Giữ nguyên ngưỡng đang có."""
import json, os, shutil, statistics as st, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HS = os.path.join(HERE, "he-so-mat.json")
VISION = os.path.expanduser("~/.cache/dung-video-theo-phong-cach/faces")
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
if sys.platform != "darwin":
    sys.exit("Chỉ đo được trên Mac (cần Vision).")
if not os.path.exists(VISION) or os.path.getmtime(os.path.join(HERE, "nhan-dien-khuon-mat.swift")) > os.path.getmtime(VISION):
    subprocess.run(["swiftc", "-O", os.path.join(HERE, "nhan-dien-khuon-mat.swift"), "-o", VISION], check=True, env=ENV)
old = json.load(open(HS, encoding="utf-8")) if os.path.exists(HS) else {}
T = tempfile.mkdtemp(prefix="he-so-mat-")
d = os.path.join(T, "f"); os.makedirs(d)
for i, v in enumerate(sys.argv[1:]):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", v, "-vf", "fps=1/15,scale=360:-2", "-q:v", "5", os.path.join(d, f"f_{i}_%05d.jpg")], check=True, env=ENV)
subprocess.run([VISION, d, os.path.join(T, "v.json")], check=True, env=ENV, capture_output=True)
# chạy cách máy khác với hệ số trung tính
tho = {"cx": 0, "cy": 0, "sw": 1, "sh": 1, "m": 1, "nguong": old.get("nguong", 0.9)}
json.dump(tho, open(HS, "w"))
try:
    subprocess.run([sys.executable, os.path.join(HERE, "nhan-dien-khuon-mat.py"), d, os.path.join(T, "y.json")], check=True, capture_output=True)
finally:
    json.dump(old or tho, open(HS, "w"))
V = json.load(open(os.path.join(T, "v.json"))); Y = json.load(open(os.path.join(T, "y.json")))
pairs, thieu = [], 0
for v, y in zip(V, Y):
    dung = set()
    for a in v:
        ca = (a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
        j = next((j for j, b in enumerate(y) if j not in dung and abs(ca[0] - b["x"] - b["w"] / 2) < a["w"] and abs(ca[1] - b["y"] - b["h"] / 2) < a["h"]), None)
        if j is None: thieu += 1
        else: dung.add(j); pairs.append((a, y[j]))
them = sum(map(len, Y)) - len(pairs)
if len(pairs) < 20:
    shutil.rmtree(T); sys.exit(f"Quá ít mặt ghép được ({len(pairs)}) — chọn video có người nói rõ mặt.")
med = st.median
mm = [(a["m"], b["m"]) for a, b in pairs if b["m"] > 0.005 and a["m"] > 0.005]
hs = {"cx": round(med([(a["x"] + a["w"] / 2 - b["x"] - b["w"] / 2) / b["w"] for a, b in pairs]), 4),
      "cy": round(med([(a["y"] + a["h"] / 2 - b["y"] - b["h"] / 2) / b["h"] for a, b in pairs]), 4),
      "sw": round(med([a["w"] / b["w"] for a, b in pairs]), 4), "sh": round(med([a["h"] / b["h"] for a, b in pairs]), 4),
      "m": round(med([a / b for a, b in mm]), 4) if mm else 1.0, "nguong": tho["nguong"],
      "do_tren": f"{len(V)} khung, {len(pairs)} cặp mặt; Vision có mà máy khác thiếu {thieu}, máy khác thêm {them}"}
json.dump(hs, open(HS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
shutil.rmtree(T)
print(json.dumps(hs, ensure_ascii=False))
