#!/bin/zsh
# Đặt lớp phủ tránh mặt người nói: vi-tri-khuon-mat.sh <dự án>
# Dò mặt (do-mat.sh: Vision trên Mac) 2 khung/giây trên bản sạch video-goc.mp4 → kiem-tra/khuon-mat/khuon-mat.json (chỉ dò lại khi video đổi),
# rồi vi-tri-khuon-mat.py đọc canh.js → chuyen-dong/src/vi-tri.js (vị trí + cỡ từng cảnh) + kiem-tra/khuon-mat/placement.md.
# Chạy lại vi-tri-khuon-mat.py mỗi khi sửa mốc cảnh trong canh.js (không cần dò lại mặt).
set -e
export PATH=/opt/homebrew/bin:$PATH
SKILL=${0:A:h:h}
P=${1:?thiếu thư mục dự án}
O="$P/kiem-tra/khuon-mat"; mkdir -p "$O"
V="$P/tu-lieu/video-goc.mp4"
BIN="$SKILL/scripts/do-mat.sh"   # Vision trên Mac, YuNet + MediaPipe ở máy khác (cùng định dạng)
if [ ! -f "$O/khuon-mat.json" ] || [ "$V" -nt "$O/khuon-mat.json" ]; then
  rm -rf "${O:?}/f"; mkdir -p "$O/f"
  ffmpeg -v error -y -i "$V" -vf "fps=2,scale=360:-2" -q:v 5 "$O/f/f_%05d.jpg"
  zsh "$BIN" "$O/f" "$O/khuon-mat.json"
  rm -rf "${O:?}/f"
fi
python3 -I "$SKILL/scripts/vi-tri-nhan.py" "$P"     # điểm nhấn trên người → chuyen-dong/src/mat.js (cả khung ngang)
python3 -I "$SKILL/scripts/vi-tri-khuon-mat.py" "$P"
