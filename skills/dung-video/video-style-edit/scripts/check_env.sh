#!/bin/zsh
# Kiểm tra công cụ cần cho quy trình. In ra cái còn thiếu và lệnh cài.
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
ok=1
chk() { if eval "$2" >/dev/null 2>&1; then echo "✅ $1"; else echo "❌ $1 — cài: $3"; ok=0; fi; }
chk "Homebrew" "command -v brew" '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  (cần mật khẩu máy — người dùng tự chạy)'
chk "ffmpeg" "command -v ffmpeg" "brew install ffmpeg"
chk "whisper.cpp" "command -v whisper-cli" "brew install whisper-cpp"
chk "Mô hình Whisper (1,5 GB)" "test -s $MODEL" "mkdir -p ~/whisper-models && curl -fL -o $MODEL https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin  (hỏi người dùng trước khi tải)"
chk "Node.js" "command -v node" "cài nvm rồi: nvm install --lts"
chk "Pillow (Python)" "python3 -c 'import PIL'" "python3 -m pip install --user pillow"
df -h ~ | awk 'NR==2 {print "💾 Ổ đĩa còn trống: " $4 " (mỗi dự án cần ~3 GB)"}'
[ $ok = 1 ] && echo "Sẵn sàng." || exit 1
