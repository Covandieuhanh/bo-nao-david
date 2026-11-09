#!/usr/bin/env python3
"""TẠO DỰ ÁN PODCAST an toàn: pod_tao.py <W> — new_podcast.sh <video/tiếng trên Mac> <tên> [doc|ngang theo tuỳ chọn khung].
Đủ (audio.wav + project.js) → bỏ qua; dở dang → Thùng rác rồi tạo lại (như tao_du_an.py)."""
import json, shutil, subprocess, sys, time
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import DV, ENV
W = Path(sys.argv[1]); tt = json.loads((W / "trang-thai.json").read_text(encoding="utf-8"))
P = Path(tt["P"]); video = tt.get("video_may") or tt["video"]
du = lambda: (P / "davinci/media/audio.wav").exists() and (P / "motion/src/project.js").exists()
if P.exists():
    if du(): print(f"Dự án podcast đã có đủ: {P} — bỏ qua"); sys.exit(0)
    rac = Path.home() / ".Trash" / f"{P.parent.name}-2-ban-dai-do-dang-{time.strftime('%H%M%S')}"
    shutil.move(str(P), str(rac)); print(f"Dự án dở dang → Thùng rác: {rac.name}")
k = {"ngang": "ngang", "doc": "doc"}.get(tt.get("tuy_chon", {}).get("khung"), "")
r = subprocess.run(["zsh", str(DV / "podcast-style-edit/scripts/new_podcast.sh"), video, tt["ten"]] + ([k] if k else []), env=ENV)
if r.returncode != 0 or not du(): raise SystemExit("Tạo dự án podcast chưa xong — xem dòng lỗi phía trên.")
