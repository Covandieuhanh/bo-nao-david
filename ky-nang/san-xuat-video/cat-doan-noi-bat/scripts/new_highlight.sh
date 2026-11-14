#!/bin/zsh
# Tạo dự án cắt highlight: new_highlight.sh <video dài | thư mục dự án gốc> <tên ngắn> [phụ đề .srt/.vtt]
# → ~/Movies/tap-<tên>/3-doan-noi-bat/ : nguon.<ext> + check/goc/ (transcript.srt, words.srt, contact.jpg, frame_0X.jpg) + loai.txt
#   - Tham số 1 là THƯ MỤC dự án gốc (dung-podcast / dung-video-theo-phong-cach, có motion/src/captions.js):
#     lấy davinci/media/video_goc.mp4 (bản không bìa — mốc khớp phụ đề), chép check/goc/{transcript,words}.srt và
#     captions.js đã sửa chính tả (check/goc/captions-goc.js), scenes.js (check/goc/scenes-goc.js) — không chép lời lại.
#     loai.txt = podcast | tu-quay theo project.js của dự án gốc.
#   - Tham số 1 là FILE video: chép lời bằng whisper.cpp (analyze_video.sh của skill gốc); loai.txt = chua-ro (Claude xem
#     contact.jpg để quyết). Phụ đề YouTube (tham số 3) → check/goc/youtube.srt để đối chiếu chính tả.
# Ghi thêm check/goc/loud05.txt (độ lớn tiếng mỗi 0,05 s) cho loud_check.py. Dòng cuối = đường dẫn dự án.
# Video 30–60 phút: chép lời ~6–12 phút → chạy nền.
set -e
export PATH=/opt/homebrew/bin:$PATH
BASE=${0:A:h:h:h}/dung-video-theo-phong-cach   # cùng bộ san-xuat-video
SRC=${1:?thiếu video dài hoặc dự án gốc}; NAME=${2:?thiếu tên ngắn}; SUB=${3:-}
P=~/Movies/tap-$NAME/3-doan-noi-bat   # cùng thư mục tập với bản dài; clip sau đó đặt tên hl-$NAME-<id>
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "$P"/{check/goc,cat}
if [ -d "$SRC" ]; then
  G=${SRC:A}
  [ -f "$G/motion/src/captions.js" ] && [ -f "$G/davinci/media/video_goc.mp4" ] || { echo "Không phải dự án dựng (thiếu motion/src/captions.js hoặc davinci/media/video_goc.mp4)"; exit 1; }
  cp "$G/davinci/media/video_goc.mp4" "$P/nguon.mp4"
  cp "$G/check/goc/transcript.srt" "$G/check/goc/words.srt" "$P/check/goc/" 2>/dev/null || true
  cp "$G/motion/src/captions.js" "$P/check/goc/captions-goc.js"
  cp "$G/motion/src/scenes.js" "$P/check/goc/scenes-goc.js"
  grep -q "podcast: true" "$G/motion/src/project.js" && echo podcast > "$P/loai.txt" || echo tu-quay > "$P/loai.txt"
  echo "$G" > "$P/check/goc/du-an-goc.txt"
  # lời chép sẵn của dự án gốc có thể bị Whisper "ảo" → kiểm, ảo thì chép lại
  { [ -f "$P/check/goc/words.srt" ] && python3 -I $BASE/scripts/loi_ao.py kiem "$P/check/goc/transcript.srt" >/dev/null; } \
    || zsh $BASE/scripts/analyze_video.sh "$P/nguon.mp4" "$P/check/goc"
else
  cp "$SRC" "$P/nguon.${SRC:e:l}"
  echo chua-ro > "$P/loai.txt"
  zsh $BASE/scripts/analyze_video.sh "$P/nguon.${SRC:e:l}" "$P/check/goc"
fi
if [ -n "$SUB" ]; then
  case "${SUB:e:l}" in
    vtt) ffmpeg -v error -y -i "$SUB" "$P/check/goc/youtube.srt" ;;
    *) cp "$SUB" "$P/check/goc/youtube.srt" ;;
  esac
fi
V=( "$P"/nguon.* ); V=$V[1]
[ -f "$P/check/goc/contact.jpg" ] || { D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
  ffmpeg -v error -y -i "$V" -map 0:v:0 -vf "fps=24/$D,scale=270:-2,tile=6x4:padding=4:color=white" -frames:v 1 "$P/check/goc/contact.jpg"; }
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 "$P/check/goc/a16.wav"
ffmpeg -v error -i "$P/check/goc/a16.wav" -af "asetnsamples=800,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null - \
  | grep RMS | awk -F= '{printf "%.2f %s\n", (NR-1)*0.05, ($2 == "-inf" ? -99 : int($2))}' > "$P/check/goc/loud05.txt"
rm -f "$P/check/goc/a16.wav"
read W H <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 "$V" | tr '\n' ' ')
echo "Khung nguồn: ${W}x${H} · loại: $(cat "$P/loai.txt")"
echo "$P"
