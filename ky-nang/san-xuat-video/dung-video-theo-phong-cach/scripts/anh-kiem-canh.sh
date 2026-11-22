#!/bin/bash
# ẢNH KIỂM TỪNG CẢNH: anh-kiem-canh.sh <dự án> [ảnh ra]
# Chụp mỗi cảnh trong canh.js ở (end − 0,8 s) — lúc mọi chữ đã hiện — ghép lên đúng khung video gốc, xếp lưới 3 cột (640 px mỗi ô).
# Dùng để soát bằng mắt trước khi render: không che ai, chữ đọc được, không đè phụ đề. Mặc định ra <dự án>/kiem-tra/luoi-canh.jpg
P=$(cd "$1" && pwd); OUT=${2:-$P/kiem-tra/luoi-canh.jpg}
cd "$P/chuyen-dong" || exit 1
ARGS=$(node --input-type=module -e "const m=await import('./src/canh.js');console.log(m.SCENES.map(s=>s.id+'@'+(s.end-0.8).toFixed(2)).join(' '))" 2>/dev/null)
[ -z "$ARGS" ] && { echo "canh.js chưa có cảnh"; exit 1; }
rm -f "$P"/kiem-tra/chuyen-dong/*.png
node xem-truoc.mjs $ARGS > /dev/null 2>&1
T=$(mktemp -d); i=0
for a in $ARGS; do t=${a#*@}
  ffmpeg -v error -y -ss "$t" -i "$P/tu-lieu/video-goc.mp4" -i "$P/kiem-tra/chuyen-dong/$a.png" \
    -filter_complex "[0][1]overlay,scale=640:-2" -frames:v 1 "$T/a_$(printf %03d $i).jpg"; i=$((i+1)); done
while [ $((i % 3)) -ne 0 ]; do cp "$T/a_000.jpg" "$T/a_$(printf %03d $i).jpg"; i=$((i+1)); done
ffmpeg -v error -y -pattern_type glob -i "$T/a_*.jpg" -filter_complex "tile=3x$((i/3))" -frames:v 1 "$OUT" && echo "$OUT ($i ô)"
rm -rf "$T"
