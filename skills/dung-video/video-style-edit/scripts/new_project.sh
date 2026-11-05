#!/bin/zsh
# Tạo thư mục dự án chuẩn: new_project.sh <video gốc> [video mẫu] [tên ngắn]
# In ra đường dẫn dự án ở dòng cuối.
set -e
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
SKILL=${0:A:h:h}
SRC=${1:?thiếu video gốc}; REF=${2:-}; NAME=${3:-$(date +%Y%m%d-%H%M)}
P=~/Movies/edit-$NAME
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "$P"/{ref,check,images,davinci/media}
EXT=${SRC:e}
cp "$SRC" "$P/davinci/media/video_goc.$EXT"
[ -n "$REF" ] && cp "$REF" "$P/ref/mau.${REF:e}"
cp -RL "$SKILL/assets/remotion-template" "$P/motion"   # -L: chép BẢN THẬT thư viện hình (src/lib)
python3 -I "$SKILL/../khoi/hoso.py" lam-video "$P/motion/src/hoso.json" >/dev/null   # hồ sơ tham số cho khung dựng
mkdir -p "$P/motion/public/photos"
# Thông số video gốc (dùng kích thước hiển thị, tính cả xoay)
read W H FR ROT <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:stream_side_data=rotation -of default=nw=1:nk=1 "$SRC" | tr '\n' ' ')
case "${ROT:-0}" in 90|-90|270|-270) T=$W; W=$H; H=$T;; esac
FN=${FR%/*}; FD=${FR#*/}
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SRC")
cat > "$P/motion/src/project.js" <<JS
// Thông số video gốc — tự điền bởi new_project.sh
export default {fpsNum: $FN, fpsDen: $FD, width: $W, height: $H, duration: $DUR, source: 'video_goc.$EXT'};
JS
( cd "$P/motion" && npm install --no-fund --no-audit >/dev/null 2>&1 && npm approve-scripts esbuild >/dev/null 2>&1 || true )
echo "Video gốc: ${W}x${H}, ${FN}/${FD} fps, ${DUR}s"
echo "$P"
