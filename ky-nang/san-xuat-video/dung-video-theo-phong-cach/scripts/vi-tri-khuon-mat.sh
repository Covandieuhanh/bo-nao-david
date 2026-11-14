#!/bin/zsh
# Đặt lớp phủ tránh mặt người nói: vi-tri-khuon-mat.sh <dự án>
# Dò mặt (Vision của macOS) 2 khung/giây trên bản sạch video_goc.mp4 → check/faces/faces.json (chỉ dò lại khi video đổi),
# rồi vi-tri-khuon-mat.py đọc canh.js → motion/src/vi-tri.js (vị trí + cỡ từng cảnh) + check/faces/placement.md.
# Chạy lại vi-tri-khuon-mat.py mỗi khi sửa mốc cảnh trong canh.js (không cần dò lại mặt).
set -e
export PATH=/opt/homebrew/bin:$PATH
SKILL=${0:A:h:h}
P=${1:?thiếu thư mục dự án}
O="$P/check/faces"; mkdir -p "$O"
V="$P/davinci/media/video_goc.mp4"
BIN=~/.cache/dung-video-theo-phong-cach/faces
if [ ! -x $BIN ] || [ "$SKILL/scripts/nhan-dien-khuon-mat.swift" -nt $BIN ]; then
  mkdir -p ${BIN:h}; swiftc -O "$SKILL/scripts/nhan-dien-khuon-mat.swift" -o $BIN
fi
if [ ! -f "$O/faces.json" ] || [ "$V" -nt "$O/faces.json" ]; then
  rm -rf "${O:?}/f"; mkdir -p "$O/f"
  ffmpeg -v error -y -i "$V" -vf "fps=2,scale=360:-2" -q:v 5 "$O/f/f_%05d.jpg"
  $BIN "$O/f" "$O/faces.json"
  rm -rf "${O:?}/f"
fi
python3 -I "$SKILL/scripts/vi-tri-nhan.py" "$P"     # điểm nhấn trên người → motion/src/mat.js (cả khung ngang)
python3 -I "$SKILL/scripts/vi-tri-khuon-mat.py" "$P"
