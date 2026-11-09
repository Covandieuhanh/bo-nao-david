#!/usr/bin/env python3
"""ÁP KẾ HOẠCH ĐỔI KHUNG NGANG → DỌC sau khi Claude duyệt: ap_reframe.py <dự án> <reframe.json> [--kiem]
Claude đã xem tracks.jpg / shots.jpg / plan.md + lời (khối 04): sửa shot "?" theo người nói, đặt cx khi khung cắt nửa mặt, "wide" cho
slide/cảnh rộng, follow cho người đi lại. Script thay `shots` trong check/reframe/plan.json, vẽ lại shots.jpg (sheet) rồi apply."""
import json, os, subprocess, sys
from pathlib import Path
P, kp = Path(sys.argv[1]), sys.argv[2]; kiem = "--kiem" in sys.argv
S = Path(__file__).resolve().parents[2] / "video-style-edit/scripts"
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
f = P / "check/reframe/plan.json"; plan = json.loads(f.read_text(encoding="utf-8")); kh = json.loads(Path(kp).read_text(encoding="utf-8"))
shots = kh.get("shots") or []; loi = []; ai = set(plan.get("tracks", {})) | {"wide"}
for i, s in enumerate(shots):
    if s.get("target") not in ai: loi.append(f"shot {i + 1}: target '{s.get('target')}' không có (chỉ: {sorted(ai)})")
    if not s.get("end", 0) > s.get("start", 0): loi.append(f"shot {i + 1}: end phải lớn hơn start")
    if s.get("cx") is not None and not 0 <= s["cx"] <= 1: loi.append(f"shot {i + 1}: cx phải trong 0–1")
    if i and abs(s["start"] - shots[i - 1]["end"]) > 0.3: loi.append(f"shot {i + 1}: phải nối liền shot trước (hở/chồng {s['start'] - shots[i - 1]['end']:.2f} s)")
for x in loi: print("✗", x)
if not shots: print("✗ thiếu shots"); sys.exit(1)
if loi: sys.exit(1)
if kiem: sys.exit(0)
plan["shots"] = [{"start": s["start"], "end": s["end"], "target": s["target"], "sure": True, "text": s.get("text", ""),
                  **({"cx": s["cx"]} if s.get("cx") is not None else {}), **({"follow": True} if s.get("follow") else {})} for s in shots]
f.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
subprocess.run(["python3", "-I", str(S / "reframe_plan.py"), str(P), "sheet"], env=ENV, check=True)
subprocess.run(["python3", "-I", str(S / "reframe_plan.py"), str(P), "apply"], env=ENV, check=True)
print(f"Đã áp {len(shots)} shot → video dọc 1080×1920 (bản ngang giữ là video_goc_ngang.mp4)")
