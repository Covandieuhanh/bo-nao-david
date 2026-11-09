#!/usr/bin/env python3
"""TẠO DỰ ÁN HIGHLIGHT: hl_tao.py <W>
Nguồn (VIDEO) là thư mục dự án bản dài (tốt nhất: lời đã sửa chính tả, bản sạch) hoặc một video dài → new_highlight.sh <nguồn> <tập>.
Dự án đủ (nguon.* + check/goc/words.srt) → bỏ qua; dở dang (lần chạy hỏng trước) → chuyển vào Thùng rác rồi tạo lại.
Loại nguồn chưa rõ (video thô) → theo tuỳ chọn của việc (mặc định người nói)."""
import glob, json, shutil, subprocess, sys, time
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import HL, ENV
W = Path(sys.argv[1]); tt = json.loads((W / "trang-thai.json").read_text(encoding="utf-8"))
H = Path(tt["P"]); nguon = tt.get("video_may") or tt["video"]; tap = H.parent.name[4:]
du = lambda: glob.glob(str(H / "nguon.*")) and (H / "check/goc/words.srt").exists()
if H.exists():
    if du():
        print(f"Dự án highlight đã có đủ: {H} — bỏ qua"); sys.exit(0)
    rac = Path.home() / ".Trash" / f"tap-{tap}-3-highlight-do-dang-{time.strftime('%H%M%S')}"
    shutil.move(str(H), str(rac)); print(f"Dự án highlight dở dang → Thùng rác: {rac.name}")
if Path(nguon).is_dir() and not (Path(nguon) / "davinci/media/video_goc.mp4").exists():
    raise SystemExit(f"Dự án bản dài {nguon} đã dọn file làm việc (không còn video_goc.mp4). Chọn video gốc trong 1-goc của tập thay vì thư mục dự án.")
r = subprocess.run(["zsh", str(HL / "new_highlight.sh"), nguon, tap], env=ENV)
if r.returncode != 0 or not du():
    raise SystemExit("Tạo dự án highlight chưa xong — xem dòng lỗi phía trên.")
l = (H / "loai.txt").read_text().strip()
if l == "chua-ro":
    (H / "loai.txt").write_text(tt.get("tuy_chon", {}).get("loai_nguon", "tu-quay") + "\n")
print("Loại nguồn:", (H / "loai.txt").read_text().strip())
