#!/bin/zsh
# Tạo dự án podcast: tao-podcast.sh <file tiếng hoặc video> <tên-ngắn> [doc|ngang] [cat-thua]  → in đường dẫn dự án ở dòng cuối
# Lấy TIẾNG (bỏ hình), GIỮ NGUYÊN toàn bộ (David chốt 2026-11-05: video dài không cắt gì); `cat-thua` = cắt lặng đầu/cuối, chỉ cho clip
# highlight. Chép template Remotion của dung-video-theo-phong-cach (có Stage),
# 30 fps. Khung theo nguồn: video ngang → NGANG 1920×1080 (thiết kế toàn khung, không chia cột); video dọc / chỉ tiếng → dọc
# 1080×1920. Tham số 3 (doc|ngang) = người dùng yêu cầu khung khác.
set -e
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
BASE=${0:A:h:h:h}/dung-video-theo-phong-cach   # cùng bộ san-xuat-video
SRC=${1:?thiếu file nguồn}; NAME=${2:-$(date +%Y%m%d-%H%M)}
source "$BASE/scripts/noi-luu.sh"; P=$(noi_luu "$NAME")   # tap-<tên>/2-ban-day-du · hl-<tên>-<id> → tap-<tên>/3-doan-noi-bat/clip-<id>
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "${P:h}"; luu_goc "$SRC" "$NAME"
mkdir -p "$P"/{ref,check/goc,images,davinci/media}
M="$P/davinci/media"
cp "$SRC" "$M/nguon.${SRC:e:l}"
# Chiều khung của nguồn (video có xoay thì tính theo khung hiển thị); chỉ có tiếng → dọc
read W H ROT <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height:stream_side_data=rotation -of default=nw=1:nk=1 "$SRC" 2>/dev/null | tr '\n' ' ')
case "${ROT:-0}" in 90|-90|270|-270) T=$W; W=$H; H=$T;; esac
LAND=0; [ -n "$W" ] && [ -n "$H" ] && [ "$W" -gt "$H" ] && LAND=1
case "${3:-}" in ngang) LAND=1;; doc) LAND=0;; esac
FW=1080; FH=1920; [ $LAND = 1 ] && { FW=1920; FH=1080; }
# Khoảng lặng thừa đầu/cuối (ngưỡng = nền ồn + 12 dB, giống bước làm sạch của skill gốc) — giữa bài giữ nguyên
ffmpeg -v error -y -i "$SRC" -vn -ac 2 -ar 48000 -c:a pcm_s16le "$M/_full.wav"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M/_full.wav")
NOISE=$(ffmpeg -i "$M/_full.wav" -af "astats=metadata=1:reset=48000,ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null - 2>&1 \
  | grep -o "RMS_level=-\?[0-9.]*" | cut -d= -f2 | grep -v inf | sort -n | awk '{a[NR]=$1} END {print a[int(NR*0.1)+1]}')
TH=$(python3 -c "print(round(max(-60, min(-25, ${NOISE:--50} + 12))))")
ffmpeg -i "$M/_full.wav" -af "silencedetect=n=${TH}dB:d=0.6" -f null - 2> "$P/check/silence.txt" || true
read A B <<< $(python3 - "$P/check/silence.txt" "$DUR" <<'PY'
import re, sys
t = open(sys.argv[1]).read(); dur = float(sys.argv[2])
s = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", t)]; e = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", t)]
a = max(0.0, e[0] - 0.4) if s and s[0] <= 0.05 and e else 0.0
b = min(dur, s[-1] + 0.4) if s and (len(e) < len(s) or e[-1] >= dur - 0.05) else dur
print(round(a, 3), round(b, 3))
PY
)
if [ "${4:-}" = cat-thua ]; then
  ffmpeg -v error -y -ss $A -to $B -i "$M/_full.wav" -af "afade=t=in:d=0.03,areverse,afade=t=in:d=0.08,areverse" -c:a pcm_s16le "$M/audio.wav"
  rm -f "$M/_full.wav"
else
  A=0; B=$DUR; mv "$M/_full.wav" "$M/audio.wav"
fi
ffmpeg -v error -y -i "$M/audio.wav" -c:a aac -b:a 256k "$M/audio.m4a"
D2=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M/audio.wav")
echo "Cắt thừa: đầu ${A}s, cuối từ ${B}s / ${DUR}s (ngưỡng ${TH} dB)" > "$P/check/trim.txt"
cp -RL "$BASE/assets/remotion-template" "$P/motion"   # -L: bản thật thư viện hình
python3 -I "$BASE/../mo-dun/ho_so.py" podcast "$P/motion/src/hoso.json" >/dev/null
mkdir -p "$P/motion/public/photos"
cat > "$P/motion/src/du-an.js" <<JS
// Dự án PODCAST — tự điền bởi dung-podcast/scripts/tao-podcast.sh. source = sân khấu nền + tiếng (nen-podcast.py)
export default {fpsNum: 30, fpsDen: 1, width: $FW, height: $FH, duration: $D2, source: 'video_goc.mp4', podcast: true};
JS
( cd "$P/motion" && npm install --no-fund --no-audit >/dev/null 2>&1 && npm approve-scripts esbuild >/dev/null 2>&1 || true )
echo "$(cat "$P/check/trim.txt") · nguồn ${W:-chỉ tiếng}${H:+×$H} → xuất $([ $LAND = 1 ] && echo 'ngang 1920×1080' || echo 'dọc 1080×1920')"
echo "$P"
