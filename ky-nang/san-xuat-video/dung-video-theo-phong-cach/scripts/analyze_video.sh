#!/bin/zsh
# Phân tích một video: analyze_video.sh <video> <thư mục ra> [ngôn ngữ, mặc định vi]
# Ra: transcript.srt (lời nói có mốc thời gian), words.srt (mốc từng từ), contact.jpg (24 khung trải đều), frame_XX.jpg (8 khung lớn)
set -e
export PATH=/opt/homebrew/bin:$PATH
V=${1:?thiếu video}; O=${2:?thiếu thư mục ra}; LANG_=${3:-vi}
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
mkdir -p "$O"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 "$O/audio16k.wav"
whisper-cli -m $MODEL -l $LANG_ -f "$O/audio16k.wav" -mc 0 -osrt -of "$O/transcript" -np >/dev/null 2>&1
whisper-cli -m $MODEL -l $LANG_ -f "$O/audio16k.wav" -mc 0 -ml 1 -sow -osrt -of "$O/words" -np >/dev/null 2>&1   # mốc từng từ (phụ đề)
# Whisper kẹt vòng ("Hãy subscribe cho kênh…" lặp cả bài): chép lại riêng đoạn ảo; còn ảo thì dừng, không chạy tiếp với lời sai
python3 -I ${0:A:h}/loi_ao.py sua "$O/audio16k.wav" "$O" $LANG_ || { rm -f "$O/audio16k.wav"; echo "⛔ Bản lời vẫn ảo sau khi chép lại — xem $O/transcript.srt"; exit 1; }
STEP=$(python3 -c "print(max(0.5, $DUR / 24))")
ffmpeg -v error -y -i "$V" -map 0:v:0 -vf "fps=1/$STEP,scale=270:-2,tile=6x4:padding=4:color=white" -frames:v 1 "$O/contact.jpg"
for i in 1 2 3 4 5 6 7 8; do
  t=$(python3 -c "print($DUR * ($i - 0.5) / 8)")
  ffmpeg -v error -y -ss $t -i "$V" -map 0:v:0 -frames:v 1 -vf "scale='min(1080,iw)':-2" "$O/frame_0$i.jpg"
done
rm -f "$O/audio16k.wav"
echo "Thời lượng ${DUR}s · transcript: $(grep -c -- '-->' "$O/transcript.srt") đoạn · $O"
