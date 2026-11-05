#!/bin/zsh
# Lời nói podcast: transcribe.sh <dự án> → check/goc/transcript.srt (theo câu) + words.srt (từng từ) + audio16k.wav (cho speakers.py)
# Hai lần chạy Whisper khác nhau → dùng để đối chiếu khi sửa phụ đề (câu bịa kiểu "Hãy subscribe…").
set -e
export PATH=/opt/homebrew/bin:$PATH
P=${1:?thiếu dự án}; O="$P/check/goc"; mkdir -p "$O"
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
ffmpeg -v error -y -i "$P/davinci/media/audio.wav" -ac 1 -ar 16000 "$O/audio16k.wav"
whisper-cli -m $MODEL -l ${2:-vi} -f "$O/audio16k.wav" -osrt -of "$O/transcript" -np >/dev/null 2>&1
whisper-cli -m $MODEL -l ${2:-vi} -f "$O/audio16k.wav" -ml 1 -sow -osrt -of "$O/words" -np >/dev/null 2>&1
echo "transcript: $(grep -c -- '-->' "$O/transcript.srt") đoạn · words: $(grep -c -- '-->' "$O/words.srt") từ"
