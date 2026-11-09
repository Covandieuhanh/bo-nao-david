#!/usr/bin/env python3
"""TẠO DỰ ÁN GHÉP VLOG: vlog_tao.py <W> — new_montage.sh vlog-<tên> <clip1> <clip2>… (thứ tự David chọn) → ~/Movies/vlog/<tên>.
Clip trên Drive đã được bước Lấy video tải về Mac (video_may). Đủ (motion/public/clips/c1.mp4 + check/c1) → bỏ qua; dở → Thùng rác, tạo lại."""
import json, shutil, subprocess, sys, time
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import S, ENV
W = Path(sys.argv[1]); tt = json.loads((W / "trang-thai.json").read_text(encoding="utf-8"))
P = Path(tt["P"]); clips = tt.get("videos_may") or tt.get("tuy_chon", {}).get("videos") or [tt.get("video_may") or tt["video"]]
du = lambda: (P / "motion/public/clips/c1.mp4").exists() and (P / "check/c1").is_dir()
if P.exists():
    if du(): print(f"Dự án ghép đã có đủ: {P} — bỏ qua"); sys.exit(0)
    shutil.move(str(P), str(Path.home() / ".Trash" / f"vlog-{P.name}-do-dang-{time.strftime('%H%M%S')}"))
r = subprocess.run(["zsh", str(S / "new_montage.sh"), f"vlog-{tt['ten']}", *clips], env=ENV)
if r.returncode != 0 or not du(): raise SystemExit("Tạo dự án ghép chưa xong — xem dòng lỗi phía trên.")
