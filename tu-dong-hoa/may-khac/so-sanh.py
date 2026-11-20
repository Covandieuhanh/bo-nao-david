"""So kết quả dựng thử của máy này với bản chuẩn Mac chính (kiem-may.sh gọi). Không cần thư viện ngoài.
  python3 -I so-sanh.py loi <chuan.srt> <moi.srt>          → tỉ lệ chữ trùng (ĐẠT ≥ 0,90)
  python3 -I so-sanh.py mat <chuan.json> <moi.json>        → tỉ lệ mặt khớp + độ trùng khung trung vị (ĐẠT ≥ 0,80 và ≥ 0,70)
  python3 -I so-sanh.py hinh <chuan.png> <moi.png>         → SSIM qua ffmpeg (ĐẠT ≥ 0,98)
In một dòng: ĐẠT|LỆCH <tên> <số đo>; mã thoát 0 = đạt, 1 = lệch."""
import difflib, json, re, statistics, subprocess, sys

kieu, a, b = sys.argv[1:4]


def chu(p):
    t = open(p, encoding="utf-8").read()
    t = "\n".join(l for l in t.splitlines() if l.strip() and "-->" not in l and not l.strip().isdigit())
    return re.findall(r"\w+", t.lower())


def bao(dat, ten, so):
    print(("ĐẠT " if dat else "LỆCH") + f" {ten}: {so}")
    sys.exit(0 if dat else 1)


if kieu == "loi":
    x, y = chu(a), chu(b)
    r = difflib.SequenceMatcher(None, x, y, autojunk=False).ratio()
    bao(r >= 0.90, "chép lời", f"trùng {r:.1%} ({len(x)} / {len(y)} chữ)")
elif kieu == "mat":
    A, B = json.load(open(a)), json.load(open(b))
    khop, iou = 0, []
    for fa, fb in zip(A, B):
        for p in fa:
            for q in fb:
                if abs(p["x"] + p["w"] / 2 - q["x"] - q["w"] / 2) < p["w"] and abs(p["y"] + p["h"] / 2 - q["y"] - q["h"] / 2) < p["h"]:
                    x0, y0 = max(p["x"], q["x"]), max(p["y"], q["y"])
                    x1, y1 = min(p["x"] + p["w"], q["x"] + q["w"]), min(p["y"] + p["h"], q["y"] + q["h"])
                    i = max(0, x1 - x0) * max(0, y1 - y0)
                    iou.append(i / (p["w"] * p["h"] + q["w"] * q["h"] - i)); khop += 1
                    break
    n = sum(map(len, A))
    tl = khop / n if n else 1.0
    md = statistics.median(iou) if iou else (1.0 if n == 0 else 0.0)
    bao(tl >= 0.80 and md >= 0.70, "dò mặt", f"khớp {khop}/{n} mặt ({tl:.0%}), độ trùng khung {md:.2f}; máy này thấy {sum(map(len, B))} mặt")
elif kieu == "hinh":
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", a, "-i", b, "-lavfi", "[0:v]format=rgba[x];[1:v]format=rgba[y];[x][y]ssim", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.search(r"All:([0-9.]+)", r.stderr)
    s = float(m.group(1)) if m else 0.0
    bao(s >= 0.98, "khung " + a.rsplit("/", 1)[-1], f"SSIM {s:.4f}")
