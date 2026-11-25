#!/bin/zsh
# Phân tích một video: phan-tich-video.sh <video> <thư mục ra> [ngôn ngữ, mặc định vi]
# Ra: ban-chep-loi.srt (lời nói có mốc thời gian), moc-tung-tu.srt (mốc từng từ), bang-khung-hinh.jpg (24 khung trải đều), khung-XX.jpg (8 khung lớn)
set -e
export PATH=/opt/homebrew/bin:$PATH
V=${1:?thiếu video}; O=${2:?thiếu thư mục ra}; LANG_=${3:-vi}
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
mkdir -p "$O"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ffmpeg -v error -y -i "$V" -vn -ac 1 -ar 16000 "$O/am-thanh-16k.wav"
whisper-cli -m $MODEL -l $LANG_ -f "$O/am-thanh-16k.wav" -mc 0 -osrt -of "$O/ban-chep-loi" -np >/dev/null 2>&1
whisper-cli -m $MODEL -l $LANG_ -f "$O/am-thanh-16k.wav" -mc 0 -ml 1 -sow -osrt -of "$O/moc-tung-tu" -np >/dev/null 2>&1   # mốc từng từ (phụ đề)
# Whisper lặp vô hạn ("Hãy subscribe cho kênh…" lặp cả bài): chép lại riêng đoạn ảo; còn ảo thì dừng, không chạy tiếp với lời sai
python3 -I ${0:A:h}/loi-ao-giac.py sua "$O/am-thanh-16k.wav" "$O" $LANG_ || { rm -f "$O/am-thanh-16k.wav"; echo "⛔ Bản lời vẫn ảo sau khi chép lại — xem $O/ban-chep-loi.srt"; exit 1; }
STEP=$(python3 -c "print(max(0.5, $DUR / 24))")
ffmpeg -v error -y -i "$V" -map 0:v:0 -vf "fps=1/$STEP,scale=270:-2,tile=6x4:padding=4:color=white" -frames:v 1 "$O/bang-khung-hinh.jpg"
for i in 1 2 3 4 5 6 7 8; do
  t=$(python3 -c "print($DUR * ($i - 0.5) / 8)")
  ffmpeg -v error -y -ss $t -i "$V" -map 0:v:0 -frames:v 1 -vf "scale='min(1080,iw)':-2" "$O/khung-0$i.jpg"
done
rm -f "$O/am-thanh-16k.wav"
echo "Thời lượng ${DUR}s · transcript: $(grep -c -- '-->' "$O/ban-chep-loi.srt") đoạn · $O"
