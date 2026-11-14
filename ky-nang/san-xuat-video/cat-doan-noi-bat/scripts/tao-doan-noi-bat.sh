#!/bin/zsh
# Tạo dự án cắt highlight: tao-doan-noi-bat.sh <video dài | thư mục dự án gốc> <tên ngắn> [phụ đề .srt/.vtt]
# → ~/Movies/tap-<tên>/3-doan-noi-bat/ : nguon.<ext> + kiem-tra/goc/ (ban-chep-loi.srt, moc-tung-tu.srt, bang-khung-hinh.jpg, khung-0X.jpg) + loai.txt
#   - Tham số 1 là THƯ MỤC dự án gốc (dung-podcast / dung-video-theo-phong-cach, có chuyen-dong/src/phu-de.js):
#     lấy tu-lieu/video-goc.mp4 (bản không bìa — mốc khớp phụ đề; có video-goc-tho.* cùng độ dài thì hình từ bản thô, tiếng bản cân), chép kiem-tra/goc/{transcript,words}.srt và
#     phu-de.js đã sửa chính tả (kiem-tra/goc/captions-goc.js), canh.js (kiem-tra/goc/scenes-goc.js) — không chép lời lại.
#     loai.txt = podcast | tu-quay theo du-an.js của dự án gốc.
#   - Tham số 1 là FILE video: chép lời bằng whisper.cpp (phan-tich-video.sh của skill gốc); loai.txt = chua-ro (Claude xem
#     bang-khung-hinh.jpg để quyết). Phụ đề YouTube (tham số 3) → kiem-tra/goc/phu-de-youtube.srt để đối chiếu chính tả.
# Ghi thêm kiem-tra/goc/am-luong-05.txt (độ lớn tiếng mỗi 0,05 s) cho kiem-am-luong.py. Dòng cuối = đường dẫn dự án.
# Video 30–60 phút: chép lời ~6–12 phút → chạy nền.
set -e
export PATH=/opt/homebrew/bin:$PATH
BASE=${0:A:h:h:h}/dung-video-theo-phong-cach   # cùng bộ san-xuat-video
SRC=${1:?thiếu video dài hoặc dự án gốc}; NAME=${2:?thiếu tên ngắn}; SUB=${3:-}
P=~/Movies/tap-$NAME/3-doan-noi-bat   # cùng thư mục tập với bản dài; clip sau đó đặt tên hl-$NAME-<id>
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "$P"/{kiem-tra/goc,cat}
if [ -d "$SRC" ]; then
  G=${SRC:A}
  [ -f "$G/chuyen-dong/src/phu-de.js" ] && [ -f "$G/tu-lieu/video-goc.mp4" ] || { echo "Không phải dự án dựng (thiếu chuyen-dong/src/phu-de.js hoặc tu-lieu/video-goc.mp4)"; exit 1; }
  # Bản dài kiểu "khung chủ thể": video-goc.mp4 đã có khung bo góc trên nền tối → cắt dọc lệch mặt. Có hình quay gốc
  # (tu-lieu/video-goc-tho.*) cùng độ dài thì lấy HÌNH từ bản thô + TIẾNG đã cân của video-goc.mp4; lệch > 0,5 s (đã làm sạch/cắt) thì giữ video-goc.mp4.
  THO=( "$G"/tu-lieu/video-goc-tho.*(N) )
  dur() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1" }
  if (( $#THO )) && (( $(echo "d=$(dur "$THO[1]")-$(dur "$G/tu-lieu/video-goc.mp4"); if (d<0) d=-d; d <= 0.5" | bc) )); then
    ffmpeg -v error -y -i "$THO[1]" -i "$G/tu-lieu/video-goc.mp4" -map 0:v:0 -map 1:a:0 -c copy -shortest "$P/nguon.mp4"
    echo "Hình: ${THO[1]:t} (bản thô) · tiếng: video-goc.mp4"
  else
    (( $#THO )) && echo "⚠ ${THO[1]:t} lệch độ dài với video-goc.mp4 (đã cắt) → dùng video-goc.mp4"
    cp "$G/tu-lieu/video-goc.mp4" "$P/nguon.mp4"
  fi
  cp "$G/kiem-tra/goc/ban-chep-loi.srt" "$G/kiem-tra/goc/moc-tung-tu.srt" "$P/kiem-tra/goc/" 2>/dev/null || true
  cp "$G/chuyen-dong/src/phu-de.js" "$P/kiem-tra/goc/captions-goc.js"
  cp "$G/chuyen-dong/src/canh.js" "$P/kiem-tra/goc/scenes-goc.js"
  grep -q "podcast: true" "$G/chuyen-dong/src/du-an.js" && echo podcast > "$P/loai.txt" || echo tu-quay > "$P/loai.txt"
  echo "$G" > "$P/kiem-tra/goc/du-an-goc.txt"
  # lời chép sẵn của dự án gốc có thể bị Whisper "ảo" → kiểm, ảo thì chép lại
  { [ -f "$P/kiem-tra/goc/moc-tung-tu.srt" ] && python3 -I $BASE/scripts/loi-ao.py kiem "$P/kiem-tra/goc/ban-chep-loi.srt" >/dev/null; } \
    || zsh $BASE/scripts/phan-tich-video.sh "$P/nguon.mp4" "$P/kiem-tra/goc"
else
  cp "$SRC" "$P/nguon.${SRC:e:l}"
  echo chua-ro > "$P/loai.txt"
  zsh $BASE/scripts/phan-tich-video.sh "$P/nguon.${SRC:e:l}" "$P/kiem-tra/goc"
fi
if [ -n "$SUB" ]; then
  case "${SUB:e:l}" in
    vtt) ffmpeg -v error -y -i "$SUB" "$P/kiem-tra/goc/phu-de-youtube.srt" ;;
    *) cp "$SUB" "$P/kiem-tra/goc/phu-de-youtube.srt" ;;
  esac
fi
V=( "$P"/nguon.* ); V=$V[1]
[ -f "$P/kiem-tra/goc/bang-khung-hinh.jpg" ] || { D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
  ffmpeg -v error -y -i "$V" -map 0:v:0 -vf "fps=24/$D,scale=270:-2,tile=6x4:padding=4:color=white" -frames:v 1 "$P/kiem-tra/goc/bang-khung-hinh.jpg"; }
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 "$P/kiem-tra/goc/a16.wav"
ffmpeg -v error -i "$P/kiem-tra/goc/a16.wav" -af "asetnsamples=800,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null - \
  | grep RMS | awk -F= '{printf "%.2f %s\n", (NR-1)*0.05, ($2 == "-inf" ? -99 : int($2))}' > "$P/kiem-tra/goc/am-luong-05.txt"
rm -f "$P/kiem-tra/goc/a16.wav"
read W H <<< $(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1:nk=1 "$V" | tr '\n' ' ')
echo "Khung nguồn: ${W}x${H} · loại: $(cat "$P/loai.txt")"
echo "$P"
