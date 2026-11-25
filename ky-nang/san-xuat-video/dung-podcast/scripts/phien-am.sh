#!/bin/zsh
# Lời nói podcast: phien-am.sh <dự án> → kiem-tra/goc/ban-chep-loi.srt (theo câu) + moc-tung-tu.srt (từng từ) + am-thanh-16k.wav (cho nguoi-noi.py)
# Hai lần chạy Whisper khác nhau → dùng để đối chiếu khi sửa phụ đề (câu bịa đặt kiểu "Hãy subscribe…").
set -e
export PATH=/opt/homebrew/bin:$PATH
P=${1:?thiếu dự án}; O="$P/kiem-tra/goc"; mkdir -p "$O"
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
ffmpeg -v error -y -i "$P/tu-lieu/am-thanh.wav" -ac 1 -ar 16000 "$O/am-thanh-16k.wav"
whisper-cli -m $MODEL -l ${2:-vi} -f "$O/am-thanh-16k.wav" -osrt -of "$O/ban-chep-loi" -np >/dev/null 2>&1
whisper-cli -m $MODEL -l ${2:-vi} -f "$O/am-thanh-16k.wav" -ml 1 -sow -osrt -of "$O/moc-tung-tu" -np >/dev/null 2>&1
echo "transcript: $(grep -c -- '-->' "$O/ban-chep-loi.srt") đoạn · words: $(grep -c -- '-->' "$O/moc-tung-tu.srt") từ"
