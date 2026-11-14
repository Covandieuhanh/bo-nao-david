#!/bin/zsh
# Gốc ngang → xuất dọc, bước 1: phan-tich-doi-khung.sh <dự án>
# Dò mặt (Vision của macOS) 4 khung/giây trên bản sạch video_goc.mp4, gom thành từng người (A, B… từ trái sang),
# đoán người đang nói theo từng câu (miệng cử động nhiều nhất) → check/reframe/plan.json + plan.md,
# tracks.jpg (khung có ô màu từng người), shots.jpg (khung dọc dự kiến của từng shot).
set -e
export PATH=/opt/homebrew/bin:$PATH
SKILL=${0:A:h:h}
P=${1:?thiếu thư mục dự án}
O="$P/check/reframe"; rm -rf "${O:?}/f"; mkdir -p "$O/f"
V=( "$P"/davinci/media/video_goc_ngang.*(N) "$P"/davinci/media/video_goc.mp4(N) ); V=$V[1]
# Bộ dò mặt: biên dịch một lần (~2 phút lần đầu), dùng lại cho mọi dự án
BIN=~/.cache/dung-video-theo-phong-cach/faces
if [ ! -x $BIN ] || [ "$SKILL/scripts/nhan-dien-khuon-mat.swift" -nt $BIN ]; then
  mkdir -p ${BIN:h}; swiftc -O "$SKILL/scripts/nhan-dien-khuon-mat.swift" -o $BIN
fi
ffmpeg -v error -y -i "$V" -vf "fps=4,scale=640:-2" -q:v 4 "$O/f/f_%05d.jpg"
$BIN "$O/f" "$O/faces.json"
# Lời nói theo câu (mốc của bản sạch) để gán người nói
[ -f "$P/check/goc/transcript.srt" ] && [ "$P/check/goc/transcript.srt" -nt "$V" ] || zsh "$SKILL/scripts/phan-tich-video.sh" "$V" "$P/check/goc"
python3 -I "$SKILL/scripts/ke-hoach-doi-khung.py" "$P" suggest
