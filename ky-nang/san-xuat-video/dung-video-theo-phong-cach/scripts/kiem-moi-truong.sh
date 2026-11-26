#!/bin/zsh
# Kiểm tra công cụ cần cho quy trình. In ra cái còn thiếu và lệnh cài. Mọi máy: Mac, Windows (WSL2), Linux.
# Cài đủ đúng phiên bản khoá một lần: bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh
# So kết quả dựng với Mac chính: zsh ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh
export PATH=$HOME/.local/bin:/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
CAI="bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh"
ok=1
chk() { if eval "$2" >/dev/null 2>&1; then echo "✅ $1"; else echo "❌ $1 — cài: $3"; ok=0; fi; }
if [[ $OSTYPE == darwin* ]]; then
  chk "Homebrew" "command -v brew" '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  (cần mật khẩu máy — người dùng tự chạy)'
  chk "Swift (dò mặt bằng Vision)" "command -v swiftc" "xcode-select --install  (người dùng tự chạy)"
else
  chk "Dò mặt (YuNet)" "~/.cache/dung-video-theo-phong-cach/mat-venv/bin/python -c 'import cv2'" "$CAI"
fi
chk "ffmpeg" "command -v ffmpeg" "$CAI"
chk "whisper.cpp" "command -v whisper-cli" "$CAI"
chk "Mô hình Whisper (1,5 GB)" "test -s $MODEL" "$CAI  (tải 1,5 GB — hỏi người dùng trước)"
chk "Node.js" "command -v node" "$CAI"
chk "Pillow (Python)" "python3 -c 'import PIL'" "$CAI"
chk "zsh, rsync" "command -v zsh && command -v rsync" "$CAI"
# Drive là nơi giao kết quả (cho-dang.sh, luu-drive.sh) và nơi bộ thử máy (kiem-tra-thiet-bi.sh): thiếu thì dựng được nhưng chưa giao được — cảnh báo, không chặn
if source "${0:A:h}/drive-chung.sh" 2>/dev/null && tim_drive; then echo "✅ Google Drive: $G"
elif [[ $OSTYPE == darwin* ]]; then echo "⚠ Chưa thấy Google Drive — dựng được nhưng chưa giao được kết quả: $DRIVE_HUONG_DAN"
elif co_rclone; then echo "✅ Drive: tải lên bằng rclone (kết nối $RC), không đồng bộ ổ"
else echo "⚠ Drive: $DRIVE_HUONG_DAN"; fi
df -h ~ | awk 'NR==2 {print "💾 Ổ đĩa còn trống: " $4 " (mỗi dự án cần ~3 GB)"}'
[ $ok = 1 ] && echo "Sẵn sàng." || exit 1
