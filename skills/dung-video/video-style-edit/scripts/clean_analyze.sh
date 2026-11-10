#!/bin/zsh
# Phân tích để làm sạch video gốc (chế độ 1 video): clean_analyze.sh <dự án> [tu-nhien]
# Ra check/clean/: words.srt (mốc từng từ), transcript.srt, loud.txt (độ lớn mỗi 0,5 s),
#   orient.jpg (4 khung để nhận ra lộn ngược/nằm ngang/lật gương), head.jpg + tail.jpg (15 s đầu/cuối, mỗi 0,5 s),
#   rồi clean_suggest.py → cuts.json (đề xuất cắt) + cuts.md (bảng để đọc).
set -e
export PATH=/opt/homebrew/bin:$PATH
SKILL=${0:A:h:h}
P=${1:?thiếu thư mục dự án}
O="$P/check/clean"; mkdir -p "$O"
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
# Luôn phân tích bản thô (lần chạy lại sau khi đã áp cắt vẫn đọc đúng file)
V=( "$P"/davinci/media/video_goc_raw.*(N) "$P"/davinci/media/video_goc.*(N) ); V=$V[1]
[ -z "$V" ] && { echo "Không thấy video_goc trong davinci/media"; exit 1; }
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 "$O/a.wav"
whisper-cli -m $MODEL -l vi -f "$O/a.wav" -osrt -of "$O/transcript" -np >/dev/null 2>&1
whisper-cli -m $MODEL -l vi -f "$O/a.wav" -ml 1 -sow -osrt -of "$O/words" -np >/dev/null 2>&1
# Whisper "ảo" (cả bài lặp một câu kiểu "Hãy subscribe cho kênh…", hoặc rỗng) — gặp ở video cũ nhiều tiếng trầm (2026-11-08):
# chép lại với tiếng đã lọc (cắt trầm + cân âm động). Chỉ đổi file tiếng cho Whisper, không đổi tiếng video.
if python3 -I -c "import re,sys;L=[l.strip() for l in open(sys.argv[1],encoding='utf-8') if l.strip() and '-->' not in l and not l.strip().isdigit()];sys.exit(0 if (not L or max(L.count(x) for x in set(L))/len(L)>0.3) else 1)" "$O/transcript.srt"; then
  echo "Whisper chép ảo → chép lại với tiếng đã lọc"
  ffmpeg -v error -y -i "$V" -vn -af "highpass=f=120,dynaudnorm" -ac 1 -ar 16000 "$O/a_loc.wav"
  whisper-cli -m $MODEL -l vi -f "$O/a_loc.wav" -osrt -of "$O/transcript" -np >/dev/null 2>&1
  whisper-cli -m $MODEL -l vi -f "$O/a_loc.wav" -ml 1 -sow -osrt -of "$O/words" -np >/dev/null 2>&1
  rm -f "$O/a_loc.wav"
fi
# Còn đoạn ảo lẻ (vd 30 s đầu) → chép lại riêng đoạn đó
python3 -I "$SKILL/scripts/loi_ao.py" sua "$O/a.wav" "$O" vi || { rm -f "$O/a.wav"; echo "⛔ Bản lời vẫn ảo — xem $O/transcript.srt"; exit 1; }
ffmpeg -v error -i "$O/a.wav" -af "asetnsamples=8000,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null - \
  | grep RMS | awk -F= '{printf "%.1fs %d dB\n", (NR-1)*0.5, $2}' > "$O/loud.txt"
# Khoảng lặng: ngưỡng = nền ồn (phân vị 10 của loud.txt) + 12 dB, nhưng không quá điểm giữa nền ồn và lời nói
# (phân vị 90) — bản ghi ngoài trời/nhỏ tiếng có lời nói chỉ cao hơn nền ~8–10 dB; lặng ≥ 1 s
THR=$(awk '{print $2}' "$O/loud.txt" | sort -n | awk '{a[NR]=$1} END{lo=a[int(NR*0.1)+1]; hi=a[int(NR*0.9)+1];
  t=lo+12; m=(lo+hi)/2; if(t>m)t=m; if(t>-30)t=-30; print t}')
ffmpeg -v info -i "$O/a.wav" -af "silencedetect=n=${THR}dB:d=1" -f null - 2>&1 \
  | grep -o 'silence_\(start\|end\): [0-9.]*' | awk '{printf "%s%s", $2, (NR%2?" ":"\n")}' > "$O/silence.txt"
echo "$THR" > "$O/threshold.txt"
# Độ lớn mỗi 0,05 s — clean_suggest.py dò khoảng lặng ngắn (≥ 0,45 s) để cắt nhịp kiểu kênh lớn
ffmpeg -v error -i "$O/a.wav" -af "asetnsamples=800,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null - \
  | grep RMS | awk -F= '{printf "%.2f %s\n", (NR-1)*0.05, ($2 == "-inf" ? -99 : int($2))}' > "$O/loud05.txt"
rm -f "$O/a.wav"
# Chiều hình: 4 khung nguyên khung (ffmpeg đã áp metadata xoay) — nhìn mặt đất, chữ trên áo/biển để biết cần xoay/lật
ffmpeg -v error -y -i "$V" -vf "fps=4/$DUR,scale=360:-2,tile=4x1:padding=6:color=white" -frames:v 1 "$O/orient.jpg"
ffmpeg -v error -y -t 15 -i "$V" -vf "fps=2,scale=150:-2,tile=10x3:padding=2" -frames:v 1 "$O/head.jpg"
ffmpeg -v error -y -sseof -15 -i "$V" -vf "fps=2,scale=150:-2,tile=10x3:padding=2" -frames:v 1 "$O/tail.jpg"
python3 -I "$SKILL/scripts/clean_suggest.py" "$P" "$DUR" ${2:-}   # tham số 2 `tu-nhien` = không cắt lặng/tiếng đệm
