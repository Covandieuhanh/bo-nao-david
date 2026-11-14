#!/usr/bin/env python3
"""Đặt lớp phủ (hook, tên, chữ to, thẻ) tránh mặt người nói: vi-tri-khuon-mat.py <dự án>
Đọc kiem-tra/khuon-mat/khuon-mat.json (vi-tri-khuon-mat.sh) + chuyen-dong/src/canh.js → chuyen-dong/src/vi-tri.js + kiem-tra/khuon-mat/placement.md.
Mỗi cảnh không toàn màn hình: lấy vùng mặt người nói trong suốt cảnh (đầu + cổ = vùng CẤM che; thân = vùng nên tránh),
thử mọi vị trí dọc của dải lớp phủ trong vùng an toàn (trên dải phụ đề), cỡ 78% → 68% → 60% → 55%; chọn vị trí không chạm vùng cấm,
ít che thân nhất, gần chỗ mặc định (đáy) nhất.
TỰ CHUYỂN TOÀN MÀN HÌNH (David chốt 2026-11-04): không vị trí/cỡ nào tránh được MẶT + ĐẦU + VAI + NGỰC (thân trên) → cảnh thành
toàn màn hình (`full: true` trong vi-tri.js, Place vẽ nền + phóng nội dung ra giữa), dài tối đa FULL_MAX s (`end`) để mặt
tỷ lệ người / đồ hoạ tự cân theo nội dung (07/11/2026). Đặt tay `place: {full: false}` trong cảnh để giữ lớp phủ.
Cảnh có `place` trong canh.js (đặt tay) thì giữ nguyên, script không ghi đè."""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mo-dun")); import ho_so as hoso   # tham số: san-xuat-video/ho-so

P = os.path.expanduser(sys.argv[1])
SRC = os.path.join(P, "chuyen-dong/src")
read = lambda f: open(os.path.join(SRC, f)).read()

proj = read("du-an.js")
W = int(re.search(r"width: (\d+)", proj).group(1)); H = int(re.search(r"height: (\d+)", proj).group(1))
FPS = int(re.search(r"fpsNum: (\d+)", proj).group(1)) / int(re.search(r"fpsDen: (\d+)", proj).group(1))
if W > H:
    sys.exit("Khung ngang: lớp phủ đã đặt theo vùng an toàn ngang — script này cho khung dọc")
out = re.search(r"^export default \{layout: '(\w+)'", read("dau-ra.js"), re.M) if os.path.exists(os.path.join(SRC, "dau-ra.js")) else None
if out and out.group(1) == "pillar":
    sys.exit("Khung ngang pillar: lớp phủ nằm ở cột trái, không đè lên video — không cần đặt tránh mặt")

theme = read("chu-de.js")
ov_top = int(re.search(r"overlayTop: (\d+)\}", theme).group(1))
S_LEFT, S_RIGHT, S_TOP, S_BOTTOM = 70, 180, 210, H - 500          # = SAFE trong chu-de.js (khung dọc)
lay = read("bo-cuc.js")
OV_SCALE = float(re.search(r"OV_SCALE = ([\d.]+)", lay).group(1))
FULL = set(re.findall(r"'(\w+)'", re.search(r"export const FULL = .*", lay).group(0)))   # cả nhánh điều kiện ('card' = thẻ toàn cảnh)
if re.search(r"podcast: true", proj): FULL.discard('card'); FULL.discard('cta')
HL = os.path.exists(os.path.join(P, "chuyen-dong/src/doan-noi-bat.js")) and not re.search(r"export default null", read("doan-noi-bat.js")) \
     and not re.search(r'"bar": false', read("doan-noi-bat.js"))   # thanh tập gốc tắt (mặc định 2026-11-04) → không đẩy phụ đề
CAP_H = (140 + (40 if HL and not re.search(r"podcast: true", proj) else 0)) if re.search(r"start:", read("phu-de.js")) else 0   # = bo-cuc.js
BAND_H, SAFE_W = S_BOTTOM - ov_top, W - S_LEFT - S_RIGHT
OV_BOTTOM = S_BOTTOM - CAP_H

frames = json.load(open(os.path.join(P, "kiem-tra/khuon-mat/khuon-mat.json")))
STEP = 0.5                                                             # vi-tri-khuon-mat.sh dò 2 khung/giây
FULL_MAX = hoso.get(hoso.load('lam-video'), 'toan_man_max_s') or float('inf')   # không trần cứng (2026-11-07)    # cảnh tự chuyển toàn màn hình dài tối đa (giây) — hồ sơ

def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, max(0, int(round(q * (len(v) - 1)))))]

def zones(a, b):
    """Vùng cấm (đầu + cổ) và vùng nên tránh (thân) trong [a, b] giây, toạ độ px khung xuất."""
    boxes, n = [], 0
    for i in range(int(a / STEP), min(len(frames), int(b / STEP) + 1)):
        n += 1
        fs = frames[i]
        if not fs: continue
        big = max(f["w"] for f in fs)
        boxes += [f for f in fs if f["w"] >= 0.5 * big]
    if not n or len(boxes) < 0.2 * n: return None, None
    hard = (pct([(f["x"] - 0.25 * f["w"]) * W for f in boxes], .05), pct([(f["y"] - 0.4 * f["h"]) * H for f in boxes], .05),
            pct([(f["x"] + 1.25 * f["w"]) * W for f in boxes], .95), pct([(f["y"] + 1.06 * f["h"]) * H for f in boxes], .93))
    # Đáy khung mặt của Vision ≈ cằm → chừa 0,06 mặt; phân vị 93% (selfie vừa đi vừa quay: đầu nhún lên xuống liên tục)
    soft = (pct([(f["x"] - 0.9 * f["w"]) * W for f in boxes], .05), hard[3],
            pct([(f["x"] + 1.9 * f["w"]) * W for f in boxes], .95), min(H, pct([(f["y"] + 4 * f["h"]) * H for f in boxes], .95)))
    # THÂN TRÊN (vai + ngực): bề ngang vai ≈ 2,8 mặt, xuống tới cằm + 1 mặt — cùng đầu/cổ là vùng CẤM che (David chốt 2026-11-04)
    upper = (soft[0], hard[1], soft[2], min(H, pct([(f["y"] + 2.0 * f["h"]) * H for f in boxes], .93)))
    return upper, soft

def overlap(r, z):
    if not z: return 0
    return max(0, min(r[2], z[2]) - max(r[0], z[0])) * max(0, min(r[3], z[3]) - max(r[1], z[1]))

def choose(hard, soft):
    """Ưu tiên 2 điểm neo cố định (đáy = ngay trên phụ đề, đỉnh = mép trên vùng an toàn) để các cảnh đứng cùng chỗ;
    cả hai chạm vùng cấm → dò khoảng giữa; vẫn không được → thu nhỏ (78% → 68% → 60%)."""
    for s in (OV_SCALE, 0.68, 0.6, 0.55):
        h = BAND_H * s
        rect = lambda t: (S_LEFT, t, S_LEFT + SAFE_W * s, t + h)
        default = round(OV_BOTTOM - h)
        anchors = [t for t in (default, S_TOP) if not overlap(rect(t), hard)]
        if anchors:   # đáy thắng khi che thân ngang nhau
            return min(anchors, key=lambda t: (round(overlap(rect(t), soft) / (SAFE_W * s * h), 2), t != default)), s, ""
        free = [t for t in range(S_TOP, default + 1, 10) if not overlap(rect(t), hard)]
        if free:
            return min(free, key=lambda t: (overlap(rect(t), soft), -t)), s, ""
    return None, None, "→ TOÀN MÀN HÌNH (lớp phủ sẽ che mặt / thân trên)"

scenes = read("canh.js")
body = scenes[scenes.index("export const SCENES"):]
res, rows = {}, []
for m in re.finditer(r"\{id: '([^']+)', type: '(\w+)', start: ([\d.]+), end: ([\d.]+)(.*?)(?=\n  \{id: |\n\];)", body, re.S):
    sid, typ, a, b, rest = m.group(1), m.group(2), float(m.group(3)), float(m.group(4)), m.group(5)
    if typ in FULL or typ in ('nhan', 'bocuc', 've'): continue   # 'nhan' tự tránh mặt (nhan.jsx + mat.js)
    hard, soft = zones(a, b)
    manual = re.search(r"\bplace: \{", rest) is not None
    if hard is None:
        t, s, note = round(OV_BOTTOM - BAND_H * OV_SCALE), OV_SCALE, "không thấy mặt → mặc định"
    else:
        t, s, note = choose(hard, soft)
    if manual: note = "đặt tay trong canh.js (giữ)"
    if t is None:
        en = round(min(b, a + FULL_MAX), 2)
        res[sid] = {"full": True, "end": en}
        rows.append(f"| {sid} | {a:.1f}–{b:.1f} | {round(hard[1])}–{round(hard[3])} | toàn màn hình {a:.1f}–{en:.1f} | — | {note} |")
        continue
    res[sid] = {"top": t, "scale": s}
    where = "đáy" if t >= OV_BOTTOM - BAND_H * s - 5 else ("đỉnh" if t <= S_TOP + 5 else f"y {t}")
    face = f"{round(hard[1])}–{round(hard[3])}" if hard else "—"
    rows.append(f"| {sid} | {a:.1f}–{b:.1f} | {face} | {where} ({t}–{round(t + BAND_H * s)}) | {round(s * 100)}% | {note} |")

open(os.path.join(SRC, "vi-tri.js"), "w").write(
    "// Vị trí lớp phủ từng cảnh (tránh mặt người nói) — tự sinh bởi scripts/vi-tri-khuon-mat.py; đặt tay: thêm `place: {top, scale}` vào cảnh\n"
    "export default " + json.dumps(res, ensure_ascii=False, indent=1) + ";\n")
tot = float(re.search(r"duration: ([\d.]+)", proj).group(1))
fulls = sum(v["end"] - float(re.search(rf"id: '{k}', type: '\w+', start: ([\d.]+)", body).group(1)) for k, v in res.items() if v.get("full"))
rows.append(f"\nTự chuyển toàn màn hình: {sum(1 for v in res.values() if v.get('full'))} cảnh, {fulls:.1f} s"
            + (f" — cộng cảnh toàn màn hình sẵn có, tự cân tỷ lệ mặt / đồ hoạ theo nội dung ({tot:.0f} s)" if tot else ""))
md = os.path.join(P, "kiem-tra/khuon-mat/placement.md")
open(md, "w").write("| Cảnh | Giây | Mặt (y px, cấm che) | Lớp phủ | Cỡ | Ghi chú |\n|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
print("\n".join(rows)); print(os.path.join(SRC, "vi-tri.js"))
