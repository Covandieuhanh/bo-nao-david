#!/bin/bash
# Chuyển tin nhắn thoại (Telegram .oga/.ogg, hay file tiếng bất kỳ) thành chữ tiếng Việt, chạy hoàn toàn trên Mac (không tốn token).
# Dùng: bash nghe-thoai.sh <đường dẫn file>   → in ra lời nói.
# Cần: ffmpeg, whisper-cli (brew install ffmpeg whisper-cpp) và mô hình ~/whisper-models/ggml-large-v3-turbo.bin
#   (tải: curl -L -o ~/whisper-models/ggml-large-v3-turbo.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin).
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
VAO="$1"; MH="${WHISPER_MODEL:-$HOME/whisper-models/ggml-large-v3-turbo.bin}"
[ -f "$VAO" ] || { echo "LOI: không thấy file $VAO"; exit 1; }
[ -f "$MH" ] || { echo "LOI: chưa có mô hình whisper ($MH)"; exit 1; }
TAM=$(mktemp -d); trap 'rm -rf "$TAM"' EXIT
ffmpeg -nostdin -loglevel error -i "$VAO" -ar 16000 -ac 1 "$TAM/a.wav" || { echo "LOI: không đọc được file tiếng"; exit 1; }
whisper-cli -m "$MH" -l vi -nt -np -t 8 -f "$TAM/a.wav" 2>/dev/null | sed 's/^ *//' | tr '\n' ' ' | sed 's/  */ /g; s/ *$//'
echo
