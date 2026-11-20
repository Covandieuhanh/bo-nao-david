#!/bin/zsh
# Tạo thư mục dự án chuẩn: tao-du-an.sh <video gốc> [video mẫu] [tên ngắn]
# In ra đường dẫn dự án ở dòng cuối.
set -e
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
SKILL=${0:A:h:h}
SRC=${1:?thiếu video gốc}; REF=${2:-}; NAME=${3:-$(date +%Y%m%d-%H%M)}
source "$SKILL/scripts/noi-luu.sh"; P=$(noi_luu "$NAME")   # ~/Movies/tap-<tên>/2-ban-day-du (xem noi-luu.sh)
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "${P:h}"; luu_goc "$SRC" "$NAME"
mkdir -p "$P"/{tai-lieu-tham-khao,kiem-tra,hinh-anh,tu-lieu}
EXT=${SRC:e:l}   # đuôi chữ thường: Mac coi .MP4 = .mp4, Windows/WSL2 và Linux thì không (script sau đọc video-goc.mp4)
cp "$SRC" "$P/tu-lieu/video-goc.$EXT"
[ -n "$REF" ] && cp "$REF" "$P/tai-lieu-tham-khao/mau.${REF:e}"
cp -RL "$SKILL/assets/khuon-remotion" "$P/chuyen-dong"   # -L: chép BẢN THẬT thư viện hình (src/lib)
python3 -I "$SKILL/../mo-dun/ho_so.py" lam-video "$P/chuyen-dong/src/ho-so.json" >/dev/null   # hồ sơ tham số cho khung dựng
mkdir -p "$P/chuyen-dong/public/anh"
# Thông số video gốc (dùng kích thước hiển thị, tính cả xoay)
read W H FR ROT <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate:stream_side_data=rotation -of default=nw=1:nk=1 "$SRC" | tr '\n' ' ')
case "${ROT:-0}" in 90|-90|270|-270) T=$W; W=$H; H=$T;; esac
FN=${FR%/*}; FD=${FR#*/}
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SRC")
cat > "$P/chuyen-dong/src/du-an.js" <<JS
// Thông số video gốc — tự điền bởi tao-du-an.sh
export default {fpsNum: $FN, fpsDen: $FD, width: $W, height: $H, duration: $DUR, source: 'video-goc.$EXT'};
JS
( cd "$P/chuyen-dong" && npm install --no-fund --no-audit >/dev/null 2>&1 && npm approve-scripts esbuild >/dev/null 2>&1 || true )
echo "Video gốc: ${W}x${H}, ${FN}/${FD} fps, ${DUR}s"
echo "$P"
