#!/bin/zsh
# Tờ kiểm tra: kiem-khung-hinh.sh <dự án> <video> <giây> <giây> ...
# Cắt khung ở các mốc, phủ khung an toàn lên, ghép thành <dự án>/check/sheet.jpg để Claude xem.
set -e
export PATH=/opt/homebrew/bin:$PATH
P=${1:?}; V=${2:?}; shift 2
G="$P/davinci/media/khung_an_toan.png"
D="$P/check/sheet_tmp"; rm -rf "${D:?}"; mkdir -p "$D"
i=0
for t in "$@"; do
  if [ -f "$G" ]; then ffmpeg -v error -y -ss $t -i "$V" -i "$G" -filter_complex "[0:v:0][1:v]overlay,scale=240:-2" -frames:v 1 "$D/f$(printf %03d $i).jpg"
  else ffmpeg -v error -y -ss $t -i "$V" -map 0:v:0 -vf scale=240:-2 -frames:v 1 "$D/f$(printf %03d $i).jpg"; fi
  i=$((i+1))
done
COLS=$(( i < 8 ? i : 8 )); ROWS=$(( (i + COLS - 1) / COLS ))
ffmpeg -v error -y -pattern_type glob -i "$D/f*.jpg" -vf "tile=${COLS}x${ROWS}:padding=4:color=white" "$P/check/sheet.jpg"
echo "$P/check/sheet.jpg ($i khung)"
