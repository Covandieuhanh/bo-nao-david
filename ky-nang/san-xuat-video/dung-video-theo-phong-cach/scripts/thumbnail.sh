#!/bin/zsh
# ẢNH THUMBNAIL YOUTUBE (bước phát hành, David chốt 2026-11-04): thumbnail.sh <dự án> <nguồn> "<DÒNG 1>" "<DÒNG 2>" [số] [left|right] [vị trí] [phóng]
#   <nguồn>: giây trong davinci/media/video_goc.mp4 (1 video) · cN@giây (dự án ghép: motion/public/clips/cN.mp4) · đường dẫn ảnh .jpg/.png
#   CHỈ hình của CHÍNH dự án này (hoặc ảnh David gửi riêng cho video này) — không dùng ảnh từ dự án khác (quy-tac-chung 7, 2026-11-05)
#   DÒNG 1 trắng, DÒNG 2 cam (từ khoá, to nhất) — KHÔNG lặp tiêu đề video (thumbnail + tiêu đề bổ sung cho nhau)
#   Kiểu Việt (2026-11-04): thêm biến môi trường THUMB_L3="DÒNG 3" · THUMB_NUM="5" (số khổng lồ) · THUMB_BADGE="TÊN SERIES · TẬP 12"
#   Tổng ≤ ~8 chữ; video dài nói trước camera / podcast thường 3 tầng; vlog 2–3 chữ hoặc con số / giá.
#   left|right: phía đặt chữ (mặt người nằm phía còn lại) · vị trí: object-position của ảnh, vd. "70% 30%" · phóng: 1.0–1.4
#   ẢNH BÌA PODCAST KHÔNG MẶT (David duyệt 2026-11-06, khối 14): <nguồn> = - · THUMB_HINH=danh-sach|<tên trong ICONS> · THUMB_TAG=PODCAST
#     THUMB_HINH=danh-sach THUMB_TAG=PODCAST zsh thumbnail.sh "$P" - "MÌNH GIỎI" "CÁI GÌ?" 1
# → <dự án>/phat-hanh/thumb-<số>.jpg (1280×720, < 2 MB) + thumb-<số>@160.jpg (cỡ xem trên điện thoại — soát đọc được không)
set -e
export PATH=/opt/homebrew/bin:$PATH
SKILL=${0:A:h:h}
P=${1:?thiếu dự án}; SRC=${2:?thiếu nguồn}; L1=${3:-}; L2=${4:-}; N=${5:-1}; SIDE=${6:-left}; POS=${7:-50% 35%}; Z=${8:-1.1}
M="$P/motion"; T="$M/thumb"; O="$P/phat-hanh"
[ -d "$M/node_modules" ] || { echo "Không thấy $M/node_modules — dự án chưa cài gói"; exit 1; }
mkdir -p "$T/public" "$O"
cp "$SKILL/assets/thumb-template/"*.jsx "$SKILL/assets/thumb-template/render-thumb.mjs" "$SKILL/../thu-vien-tai-nguyen/brand.json" "$SKILL/../thu-vien-tai-nguyen/Icons.jsx" "$SKILL/../thu-vien-tai-nguyen/tokens.js" "$T/"
BG="$T/public/bg-$N.jpg"
if [ "$SRC" = "-" ]; then
  [ -n "${THUMB_HINH:-}" ] || { echo "Nguồn - cần THUMB_HINH"; exit 1; }
elif [ -f "$SRC" ]; then
  ffmpeg -v error -y -i "$SRC" -q:v 2 "$BG"
else
  if [[ "$SRC" == *@* ]]; then V="$M/public/clips/${SRC%@*}.mp4"; S=${SRC#*@}; else V="$P/davinci/media/video_goc.mp4"; S=$SRC; fi
  ffmpeg -v error -y -ss "$S" -i "$V" -frames:v 1 -q:v 2 "$BG"
fi
if [ "$SRC" = "-" ]; then BW=1280; BH=720; else
read BW BH <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 "$BG" | tr '\n' ' ')
fi
PANEL=$([ "$BH" -gt "$BW" ] && echo 1 || echo 0)   # nguồn dọc → ảnh thành khung một bên
PROPS=$(python3 -c 'import json,sys; print(json.dumps(dict(bg=sys.argv[1], l1=sys.argv[2], l2=sys.argv[3], side=sys.argv[4], pos=sys.argv[5], zoom=float(sys.argv[6]), panel=sys.argv[7] == "1", l3=sys.argv[8], num=sys.argv[9], badge=sys.argv[10], hinh=sys.argv[11], tag=sys.argv[12]), ensure_ascii=False))' \
  "bg-$N.jpg" "$L1" "$L2" "$SIDE" "$POS" "$Z" "$PANEL" "${THUMB_L3:-}" "${THUMB_NUM:-}" "${THUMB_BADGE:-}" "${THUMB_HINH:-}" "${THUMB_TAG:-}")
cd "$M" && node thumb/render-thumb.mjs "$PROPS" "$O/thumb-$N.png" >/dev/null
ffmpeg -v error -y -i "$O/thumb-$N.png" -q:v 3 "$O/thumb-$N.jpg" && rm "$O/thumb-$N.png"
ffmpeg -v error -y -i "$O/thumb-$N.jpg" -vf scale=160:-2 "$O/thumb-$N@160.jpg"
echo "$O/thumb-$N.jpg"
