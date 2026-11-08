#!/usr/bin/env python3
"""TẠO DỰ ÁN an toàn: tao_du_an.py <W>
Gọi new_project.sh của skill với video trên Mac (bước Lấy video). Dự án đã có ĐỦ (project.js + video_goc mở được) → bỏ qua.
Dự án dở dang của lần chạy hỏng trước (vd tệp 0 byte, lỗi 08/11/2026) → chuyển thư mục 2-ban-dai dở vào Thùng rác rồi tạo lại,
thay vì bỏ qua như trước (bỏ qua làm bước Chép lời hỏng theo)."""
import glob, json, os, shutil, subprocess, sys, time
from pathlib import Path

W = Path(sys.argv[1]); tt = json.loads((W / "trang-thai.json").read_text(encoding="utf-8"))
P = Path(tt["P"]); video = tt.get("video_may") or tt["video"]
S = Path(__file__).resolve().parents[2] / "video-style-edit/scripts"
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))


def du(P):
    v = glob.glob(str(P / "davinci/media/video_goc.*")) + glob.glob(str(P / "davinci/media/video_goc_raw.*"))
    if not (P / "motion/src/project.js").exists() or not v:
        return False
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v[0]], capture_output=True, text=True, env=ENV)
    return r.stdout.strip() not in ("", "N/A")


if P.exists():
    if du(P):
        print(f"Dự án đã có đủ: {P} — bỏ qua"); sys.exit(0)
    rac = Path.home() / ".Trash" / f"{P.parent.name}-2-ban-dai-do-dang-{time.strftime('%H%M%S')}"
    shutil.move(str(P), str(rac)); print(f"Dự án dở dang của lần chạy trước → Thùng rác: {rac.name}")
r = subprocess.run(["zsh", str(S / "new_project.sh"), video, "", tt["ten"]], env=ENV)
if r.returncode != 0 or not du(P):
    raise SystemExit("Tạo dự án chưa xong — xem dòng lỗi phía trên.")
