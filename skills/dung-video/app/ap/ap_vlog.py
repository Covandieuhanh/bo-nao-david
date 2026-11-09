#!/usr/bin/env python3
"""ÁP KẾ HOẠCH GHÉP VLOG: ap_vlog.py <dự án> <ke-hoach-ghep.json> [--kiem]
Claude viết plan (khuôn của vlog_edl.py — mốc là giây trong từng clip, vì vlog có nhiều cảnh không lời) + kế hoạch ghép cho David.
Soát: clip có thật, mốc trong thời lượng clip, chữ hiệu ứng nguyên văn lời CLIP đó (chữ đã sửa trong `fix` được tính), tuyến nhạc có
trong hồ sơ. Rồi ghi plan.json + ke-hoach-ghep.md, chạy vlog_edl.py (edl.js + soát hình check/segs) và link_sheet.py nếu có liên kết."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import loi
from vlog_chung import ds_clip
from hl_chung import S, ENV, DV
sys.path.insert(0, str(DV / "khoi")); import hoso
P, kp = Path(sys.argv[1]), sys.argv[2]; kiem = "--kiem" in sys.argv
kh = json.loads(Path(kp).read_text(encoding="utf-8")); plan = kh["plan"]; loi_ds = []
CL = set(ds_clip(P)); fix = frozenset(t for v in (plan.get("fix") or {}).values() for t in loi.chuan(v))
T = {c: (loi.tu(P / f"check/{c}/words.srt") if (P / f"check/{c}/words.srt").exists() else []) for c in CL}
dur = {c: float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(P / f"motion/public/clips/{c}.mp4")],
                               capture_output=True, text=True, env=ENV).stdout.strip() or 0) for c in CL}
tuyen = hoso.get(hoso.load("ghep-vlog"), "nhac.tuyen") or {}
if plan.get("tuyen") not in tuyen: loi_ds.append(f"plan.tuyen '{plan.get('tuyen')}' không có trong hồ sơ: {list(tuyen)}")
for x in plan.get("clips", []):
    c = x.get("c")
    if x.get("montage"): continue
    if c not in CL: loi_ds.append(f"clip '{c}' không có (chỉ: {sorted(CL)})"); continue
    if not x.get("skip") and not (0 <= x.get("from", 0) < x.get("to", dur[c]) <= dur[c] + 0.5):
        loi_ds.append(f"{c}: from/to {x.get('from')}–{x.get('to')} ngoài thời lượng clip {dur[c]:.1f} s")
for fx in plan.get("fx", []):
    c = fx.get("c")
    if c not in CL: loi_ds.append(f"fx {fx.get('type')}: clip '{c}' không có"); continue
    chu = [fx.get(k) for k in ("text", "quote", "label") if isinstance(fx.get(k), str)]
    chu += [i[0] if isinstance(i, list) else i.get("label", "") for i in fx.get("items", []) if isinstance(i, (list, dict))] if fx.get("type") == "chips" else []
    for t in chu:
        if T[c] and loi.co_trong_loi(t, T[c], fx.get("at", 0) - 5, fx.get("at", 0) + fx.get("len", 4) + 5, them=fix) < 0.6 \
                and loi.co_trong_loi(t, T[c], 0, 1e9, 0, them=fix) < 0.85:
            loi_ds.append(f"fx {fx.get('type')} ({c} @ {fx.get('at')}): chữ «{t}» không nguyên văn lời clip đó")
print(f"{len(plan.get('clips', []))} mục clip · {len(plan.get('fx', []))} hiệu ứng · {len(loi_ds)} lỗi")
for x in loi_ds: print("✗", x)
if loi_ds: sys.exit(1)
if kiem: sys.exit(0)
if sum(x.get("to", 0) - x.get("from", 0) for x in plan.get("clips", []) if not x.get("skip") and x.get("c") in dur) > 180:
    plan.setdefault("ytEnd", hoso.get(hoso.load("ghep-vlog"), "youtube.man_ket_s", 20))   # khối 08: video > 3 phút → màn kết YouTube
(P / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
(P / "ke-hoach-ghep.md").write_text(kh.get("ke_hoach_md", ""), encoding="utf-8")
subprocess.run(["python3", "-I", str(S / "vlog_edl.py"), str(P)], env=ENV, check=True)
if "liên kết" in kh.get("ke_hoach_md", "").lower():
    subprocess.run(["python3", "-I", str(S / "link_sheet.py"), str(P)], env=ENV)
