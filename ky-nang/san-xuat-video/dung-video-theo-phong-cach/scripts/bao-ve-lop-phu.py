#!/usr/bin/env python3
"""TỰ CHUYỂN TOÀN MÀN HÌNH cho chế độ GHÉP (vlog, highlight người nói) — David chốt 2026-11-04: lớp chữ/hiệu ứng (pow, chips,
location, nameCard, replay, pinTitle, title trên đoạn ghép) mà che MẶT + ĐẦU + VAI + NGỰC người trong khung → thành cảnh toàn màn
hình (nền tối + nội dung phóng ra giữa), dài tối đa 4 s để người vẫn hiện nhiều. bao-ve-lop-phu.py <dự án ghép>
Đọc chuyen-dong/src/danh-sach-cat.js (SEGS, OVERLAYS) + nang-lop.js + kiem-tra/khuon-mat/<clip>.json (nang-lop.py dò 2 khung/giây) → chuyen-dong/src/bao-ve.js +
kiem-tra/khuon-mat/guard.md. Chạy SAU nang-lop.py và sau MỖI lần sửa danh-sach-cat.js (danh-sach-cat-doan-noi-bat.py / danh-sach-cat-vlog.py ghi lại danh-sach-cat.js). Lớp có `keep: true`
trong OVERLAYS thì bỏ qua (giữ lớp phủ)."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mo-dun")); import ho_so as hoso   # tham số: san-xuat-video/ho-so
P = os.path.expanduser(sys.argv[1]); M = os.path.join(P, "chuyen-dong")
js = "Promise.all([import('./src/danh-sach-cat.js'), import('./src/nang-lop.js').catch(()=>({default:{}}))]).then(([m,l])=>console.log(JSON.stringify({s:m.SEGS,o:m.OVERLAYS,l:l.default||{}})))"
d = json.loads(subprocess.run(["node", "--input-type=module", "-e", js], cwd=M, capture_output=True, text=True, check=True).stdout)
W, H, LOW_Y = 1080, 1920, 1254
MAX = hoso.get(hoso.load('ghep-vlog'), 'toan_man_max_s') or float('inf')   # không trần cứng (2026-11-07)   # hồ sơ
faces = {}
def fc(clip):
    if clip not in faces:
        f = os.path.join(P, "kiem-tra/khuon-mat", clip + ".json")
        faces[clip] = json.load(open(f)) if os.path.exists(f) else None
    return faces[clip]
def band(o):
    t = o["type"]; txt = o.get("text", "") or ""
    if t == "pow":
        h = (2 if len(txt) > 14 else 1) * (124 if len(txt) > 12 else 150) * 1.15
        return (o["y"], o["y"] + h) if o.get("y") is not None else (LOW_Y - h, LOW_Y)
    if t == "chips":
        h = len(o.get("items", [])) * 92 + 40
        return (o["top"], o["top"] + h) if o.get("top") is not None else (LOW_Y - h, LOW_Y)
    if t in ("location", "nameCard", "replay"): return (LOW_Y - 230, LOW_Y)
    if t == "pinTitle": return (284, 284 + (2 if len(txt) > 30 else 1) * 70 + 24)
    if t == "title" and o.get("over"): return (LOW_Y - 140, LOW_Y)
    return None
def faces_at(t):
    seg = next((s for s in d["s"] if s["start"] <= t < s["start"] + s["dur"]), None)
    if not seg or seg.get("cite") or seg.get("freeze"): return []
    fr = fc(seg["clip"])
    if not fr: return []
    src = seg["from"] + (t - seg["start"]) * seg.get("rate", 1)
    i = int(round(src * 2))
    if i < 0 or i >= len(fr): return []
    lf = d["l"].get(seg["id"], {}) if isinstance(d["l"], dict) else {}
    ly, ls = lf.get("y", 0), lf.get("s", 1)
    out = []
    for f in fr[i] or []:
        y0 = ((f["y"] - 0.4 * f["h"]) * H) * ls - ly; y1 = ((f["y"] + 2.0 * f["h"]) * H) * ls - ly   # đầu → ngực
        x0 = (f["x"] - 0.9 * f["w"]) * W; x1 = (f["x"] + 1.9 * f["w"]) * W
        if f["w"] > 0.08: out.append((x0, y0, x1, y1))
    return out
res, rows = {}, []
for i, o in enumerate(d["o"]):
    b = band(o)
    if not b or o.get("keep"): continue
    ts = [o["start"] + k * 0.5 for k in range(max(1, int((o["end"] - o["start"]) / 0.5)))]
    hit = sum(1 for t in ts if any(min(b[1], z[3]) > max(b[0], z[1]) and min(900, z[2]) > max(70, z[0]) for z in faces_at(t)))
    if hit >= max(1, 0.3 * len(ts)) and o["type"] == "pinTitle":   # tít ghim chạy suốt clip: không thành toàn màn hình → ẩn
        res[str(i)] = {"off": True}
        rows.append(f"| {i} | pinTitle | {o['start']:.1f}–{o['end']:.1f} | {hit}/{len(ts)} | → ẩn (tít ghim sẽ che đầu người nói) |")
        continue
    if hit >= max(1, 0.3 * len(ts)):
        en = round(min(o["end"], o["start"] + MAX), 2)
        res[str(i)] = {"full": True, "end": en, "dy": round(H * 0.44 - (b[0] + b[1]) / 2)}
        rows.append(f"| {i} | {o['type']} | {o['start']:.1f}–{o['end']:.1f} | {hit}/{len(ts)} | → toàn màn hình {o['start']:.1f}–{en:.1f} |")
open(os.path.join(M, "src/bao-ve.js"), "w").write("// Lớp phủ tự chuyển toàn màn hình (che mặt / thân trên) — bao-ve-lop-phu.py sinh; khoá = số thứ tự trong OVERLAYS\nexport default " + json.dumps(res, indent=1) + ";\n")
os.makedirs(os.path.join(P, "kiem-tra/khuon-mat"), exist_ok=True)
open(os.path.join(P, "kiem-tra/khuon-mat/guard.md"), "w").write("| # | Lớp | Giây | Khung che người | Kết quả |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
print("\n".join(rows) or "Không lớp nào che người — giữ nguyên"); print(f"{len(res)} lớp → toàn màn hình")
