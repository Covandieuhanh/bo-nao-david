#!/bin/zsh
# Chụp thử podcast (trước khi render): anh-tinh-podcast.sh <dự án> <id>@<giây> ... → kiem-tra/anh-tinh.jpg
# Mỗi mốc: sân khấu nền (nen@giây) + cảnh (id@giây, bỏ qua nếu id = nen) + phụ đề (phu-de@giây) + khung an toàn.
set -e
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
BASE=${0:A:h:h:h}/dung-video-theo-phong-cach   # cùng bộ san-xuat-video
P=${1:?}; shift
C="$P/kiem-tra/chuyen-dong"; G="$P/tu-lieu/khung-an-toan.png"
[ -f "$G" ] || python3 "$BASE/scripts/vung-an-toan.py" "$P" >/dev/null
ARGS=()
for a in "$@"; do
  t=${a##*@}; id=${a%@*}
  ARGS+=("nen@$t" "phu-de@$t"); [ "$id" != nen ] && ARGS+=("$a")
done
( cd "$P/chuyen-dong" && node xem-truoc.mjs "${ARGS[@]}" >/dev/null )
D="$P/kiem-tra/anh-tinh-tam"; rm -rf "${D:?}"; mkdir -p "$D"; i=0
SW=270; MAXC=7; grep -q "width: 1920" "$P/chuyen-dong/src/du-an.js" && { SW=640; MAXC=3; }   # khung ngang: ảnh to hơn
for a in "$@"; do
  t=${a##*@}; id=${a%@*}
  IN=(-i "$C/nen@$t.png"); FL="[0:v]null[b0]"; k=1; prev=b0
  for f in "$C/$id@$t.png" "$C/phu-de@$t.png" "$G"; do
    [ "$id" = nen ] && [ "$f" = "$C/nen@$t.png" ] && continue
    [ -f "$f" ] || continue
    IN+=(-i "$f"); FL="$FL;[$prev][$k:v]overlay[b$k]"; prev=b$k; k=$((k+1))
  done
  ffmpeg -v error -y "${IN[@]}" -filter_complex "$FL;[$prev]scale=$SW:-2" -frames:v 1 "$D/c$(printf %03d $i).jpg"
  i=$((i+1))
done
COLS=$(( i < MAXC ? i : MAXC )); ROWS=$(( (i + COLS - 1) / COLS ))
ffmpeg -v error -y -pattern_type glob -i "$D/c*.jpg" -vf "tile=${COLS}x${ROWS}:padding=6:color=white" "$P/kiem-tra/anh-tinh.jpg"
echo "$P/kiem-tra/anh-tinh.jpg ($i khung)"
