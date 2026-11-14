#!/bin/zsh
# Ghép các khung chụp từ xem-truoc.mjs (kiem-tra/chuyen-dong/<id>@<giây>.png) lên đúng khung video gốc + khung an toàn
# → kiem-tra/anh-tinh.jpg để Claude xem một lượt. Dùng: ghep-anh-tinh.sh <dự án>
set -e
export PATH=/opt/homebrew/bin:$PATH
P=${1:?}; C="$P/kiem-tra/chuyen-dong"; G="$P/tu-lieu/khung-an-toan.png"
SRC=$(ls "$P"/tu-lieu/video-goc.* | head -1)
SW=270; MAXC=7
[ -f "$P/tu-lieu/nen-ngang.mp4" ] && { SRC="$P/tu-lieu/nen-ngang.mp4"; SW=640; MAXC=3; }   # pillar: nền ngang đã ghép (nen-cot.py)
D="$P/kiem-tra/anh-tinh-tam"; rm -rf "${D:?}"; mkdir -p "$D"
i=0
for f in $(ls "$C"/*@*.png | grep -v '/phu-de@' | sort -t@ -k2 -n); do
  t=${f##*@}; t=${t%.png}
  # Có ảnh phụ đề cùng mốc (node xem-truoc.mjs phu-de@<giây>) → đè lên cảnh trước khi ghép
  if [ -f "$C/phu-de@$t.png" ]; then ffmpeg -v error -y -i "$f" -i "$C/phu-de@$t.png" -filter_complex overlay -update 1 "$D/_m.png"; f="$D/_m.png"; fi
  if [ -f "$G" ]; then ffmpeg -v error -y -ss $t -i "$SRC" -i "$f" -i "$G" -filter_complex "[0:v:0][1:v]overlay[a];[a][2:v]overlay,scale=$SW:-2" -frames:v 1 "$D/c$(printf %03d $i).jpg"
  else ffmpeg -v error -y -ss $t -i "$SRC" -i "$f" -filter_complex "[0:v:0][1:v]overlay,scale=$SW:-2" -frames:v 1 "$D/c$(printf %03d $i).jpg"; fi
  i=$((i+1))
done
COLS=$(( i < MAXC ? i : MAXC )); ROWS=$(( (i + COLS - 1) / COLS ))
ffmpeg -v error -y -pattern_type glob -i "$D/c*.jpg" -vf "tile=${COLS}x${ROWS}:padding=6:color=white" "$P/kiem-tra/anh-tinh.jpg"
echo "$P/kiem-tra/anh-tinh.jpg ($i khung)"
