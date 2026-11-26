#!/bin/bash
# CÀI CÔNG CỤ DỰNG VIDEO ĐÚNG PHIÊN BẢN KHOÁ (phien-ban.env) — mọi máy: Mac, Windows (qua WSL2 Ubuntu), Linux.
#   bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh
# Chạy lại nhiều lần không sao: cái gì đúng bản rồi thì bỏ qua. Cần mạng; Linux cần mật khẩu máy (sudo apt) — David tự gõ.
# Cài: ffmpeg, whisper.cpp + mô hình Whisper (1,5 GB), Node qua nvm, uv, Pillow, môi trường podcast (numpy), pyannote
# (tách người nói), dò mặt (máy không phải Mac: YuNet + MediaPipe thay Vision). Xong thì chạy kiem-tra-thiet-bi.sh để so với Mac chính.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
source "$HERE/phien-ban.env"
CACHE="$HOME/.cache/dung-video-theo-phong-cach"
LB="$HOME/.local/bin"
mkdir -p "$CACHE" "$LB" "$HOME/whisper-models"
OS=$(uname); LOI=0
buoc() { printf '\n== %s\n' "$*"; }
ok() { echo "  ✓ $*"; }
loi() { echo "  ✗ $*"; LOI=1; }
sha_ok() { [ -s "$1" ] && [ "$( (shasum -a 256 "$1" 2>/dev/null || sha256sum "$1") | awk '{print $1}')" = "$2" ]; }
tai() {   # tai <url> <file> <sha>
  sha_ok "$2" "$3" && { ok "$(basename "$2") đã có"; return 0; }
  curl -fL --retry 3 -o "$2.tam" "$1" && mv "$2.tam" "$2"
  sha_ok "$2" "$3" && ok "đã tải $(basename "$2")" || loi "tải $(basename "$2") sai mã kiểm"
}
# PATH cho mọi kiểu shell (script dựng chạy bằng zsh không tương tác → chỉ đọc ~/.zshenv)
them_path() {
  local dong='export PATH="$HOME/.local/bin:$PATH"'
  for f in "$HOME/.zshenv" "$HOME/.bashrc" "$HOME/.profile"; do
    grep -qsF "$dong" "$f" || echo "$dong   # công cụ dựng video (cai-cong-cu-video.sh)" >> "$f"
  done
  export PATH="$LB:$PATH"
}
them_path

if [ "$OS" = Linux ]; then
  grep -qi microsoft /proc/version 2>/dev/null && echo "Máy: Windows qua WSL2" || echo "Máy: Linux"
  buoc "Gói hệ thống (apt — cần mật khẩu máy)"
  sudo apt-get update -qq
  GOI="zsh rsync curl git gh build-essential cmake pkg-config xz-utils unzip python3 python3-pip python3-venv fonts-dejavu-core
       libgl1 libglib2.0-0 libnss3 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libgbm1 libasound2 libxrandr2 libxkbcommon0
       libxfixes3 libxcomposite1 libxdamage1 libpango-1.0-0 libcairo2 libcups2"
  for g in $GOI; do   # Ubuntu 24.04 đổi tên vài gói thành ...t64
    dpkg -s "$g" >/dev/null 2>&1 || dpkg -s "${g}t64" >/dev/null 2>&1 || \
      sudo apt-get install -y -qq "$g" >/dev/null 2>&1 || sudo apt-get install -y -qq "${g}t64" >/dev/null 2>&1 || loi "không cài được $g"
  done
  ok "gói hệ thống"

  buoc "ffmpeg $FFMPEG"
  if ffmpeg -version 2>/dev/null | head -1 | grep -q "version n\?$FFMPEG"; then ok "$(ffmpeg -version | head -1 | cut -c1-40)"
  else
    T=$(mktemp -d); curl -fsSL -o "$T/ff.tar.xz" "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n$FFMPEG-latest-$( [ "$(uname -m)" = aarch64 ] && echo linuxarm64 || echo linux64 )-gpl-$FFMPEG.tar.xz" \
      && rm -rf "$HOME/.local/opt/ffmpeg" && mkdir -p "$HOME/.local/opt/ffmpeg" && tar -xJf "$T/ff.tar.xz" -C "$HOME/.local/opt/ffmpeg" --strip-components=1 \
      && ln -sf "$HOME/.local/opt/ffmpeg/bin/ffmpeg" "$LB/ffmpeg" && ln -sf "$HOME/.local/opt/ffmpeg/bin/ffprobe" "$LB/ffprobe" \
      && ok "$("$LB/ffmpeg" -version | head -1 | cut -c1-40)" || loi "ffmpeg"
    rm -rf "$T"
  fi

  buoc "whisper.cpp $WHISPER_CPP"
  if whisper-cli --version 2>&1 | grep -q "$WHISPER_CPP"; then ok "whisper-cli $WHISPER_CPP"
  else
    T=$(mktemp -d)
    CUDA=""; command -v nvcc >/dev/null && CUDA="-DGGML_CUDA=1"   # có card NVIDIA + CUDA trong WSL thì chép lời nhanh hơn nhiều
    curl -fsSL "https://github.com/ggml-org/whisper.cpp/archive/refs/tags/v$WHISPER_CPP.tar.gz" | tar -xz -C "$T" \
      && cmake -S "$T/whisper.cpp-$WHISPER_CPP" -B "$T/b" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF $CUDA >/dev/null \
      && cmake --build "$T/b" -j"$(nproc)" --target whisper-cli >/dev/null \
      && cp "$T/b/bin/whisper-cli" "$LB/whisper-cli" && ok "whisper-cli $WHISPER_CPP${CUDA:+ (CUDA)}" || loi "dựng whisper.cpp"
    rm -rf "$T"
  fi
  command -v uv >/dev/null || { buoc "uv"; curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null && ok "uv" || loi "uv"; }
elif [ "$OS" = Darwin ]; then
  echo "Máy: Mac"
  export PATH=/opt/homebrew/bin:$PATH
  command -v brew >/dev/null || { echo "⛔ Chưa có Homebrew. David tự chạy (cần mật khẩu máy):"; echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'; exit 1; }
  buoc "brew: ffmpeg, whisper.cpp, uv, gh, rsync"
  for g in ffmpeg whisper-cpp uv gh rsync; do brew list "$g" >/dev/null 2>&1 || brew install -q "$g" >/dev/null || loi "brew $g"; done
  ffmpeg -version | head -1 | grep -q "version $FFMPEG" && ok "ffmpeg $FFMPEG" || echo "  ⚠ ffmpeg khác bản khoá ($FFMPEG): $(ffmpeg -version | head -1 | cut -c1-30) — Homebrew chỉ có bản mới nhất; kiem-tra-thiet-bi.sh sẽ báo nếu video lệch"
  whisper-cli --version 2>&1 | grep -q "$WHISPER_CPP" && ok "whisper-cli $WHISPER_CPP" || echo "  ⚠ whisper.cpp khác bản khoá ($WHISPER_CPP)"
else
  echo "⛔ Hệ điều hành chưa hỗ trợ: $OS. Windows: cài WSL2 Ubuntu rồi chạy script này trong Ubuntu (huong-dan-cai-dat.md mục 3)."; exit 1
fi

buoc "Mô hình Whisper (1,5 GB)"
tai "$WHISPER_MODEL_URL" "$HOME/whisper-models/ggml-large-v3-turbo.bin" "$WHISPER_MODEL_SHA"

buoc "Node $NODE (nvm)"
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] || curl -fsSL "https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM/install.sh" | bash >/dev/null 2>&1
. "$NVM_DIR/nvm.sh"
nvm ls "$NODE" >/dev/null 2>&1 || nvm install "$NODE" >/dev/null 2>&1
nvm alias default "$NODE" >/dev/null && [ "$(nvm version "$NODE")" = "v$NODE" ] && ok "node v$NODE" || loi "node $NODE"

buoc "Pillow $PILLOW (python3 hệ thống)"
if python3 -c "import PIL,sys;sys.exit(PIL.__version__!='$PILLOW')" 2>/dev/null; then ok "Pillow $PILLOW"
else python3 -m pip install -q --user --break-system-packages "Pillow==$PILLOW" 2>/dev/null || python3 -m pip install -q --user "Pillow==$PILLOW"
  python3 -c "import PIL;print('  ✓ Pillow',PIL.__version__)" || loi "Pillow"; fi

buoc "Tải link: gdown $GDOWN, yt-dlp $YT_DLP (uv tool)"
for t in "gdown==$GDOWN" "yt-dlp==$YT_DLP"; do
  uv tool install -q "$t" >/dev/null 2>&1 || uv tool install -q --force "$t" >/dev/null 2>&1 || loi "uv tool $t"
done
command -v gdown >/dev/null && command -v yt-dlp >/dev/null && ok "gdown, yt-dlp" || loi "gdown / yt-dlp chưa có trong PATH (~/.local/bin)"

buoc "Môi trường Python (uv, Python $PYTHON)"
mk_venv() {   # mk_venv <thư mục> <gói ...>  — tạo nếu chưa có, cài đúng bản
  local V=$1; shift
  [ -x "$V/bin/python" ] || uv venv -q --python "$PYTHON" "$V" || { loi "venv $V"; return 1; }
  uv pip install -q --python "$V/bin/python" "$@" && ok "$(basename "$V"): $*" || loi "cài vào $V: $*"
}
mk_venv "$CACHE/podcast-venv" "numpy==$NUMPY"
if [ "$OS" = Linux ]; then
  uv venv -q --python "$PYTHON" "$HOME/.venvs/pyannote" 2>/dev/null || [ -x "$HOME/.venvs/pyannote/bin/python" ]
  uv pip install -q --python "$HOME/.venvs/pyannote/bin/python" "torch==$TORCH" "torchaudio==$TORCHAUDIO" --index-url https://download.pytorch.org/whl/cpu \
    || loi "torch (bản CPU)"
fi
mk_venv "$HOME/.venvs/pyannote" "torch==$TORCH" "torchaudio==$TORCHAUDIO" "pyannote.audio==$PYANNOTE_AUDIO" "huggingface_hub==0.25.2" "lightning==2.6.6" "numpy==$NUMPY"

buoc "Mô hình tách người nói (pyannote speaker-diarization-3.1)"
PM="$HOME/.cache/torch/pyannote/models--pyannote--speaker-diarization-3.1"
if [ -d "$PM" ]; then ok "đã có"
elif [ -s "$HOME/.cache/huggingface/token" ]; then
  HF_HUB_OFFLINE=0 "$HOME/.venvs/pyannote/bin/python" -c "from pyannote.audio import Pipeline; Pipeline.from_pretrained('pyannote/speaker-diarization-3.1', use_auth_token=True)" >/dev/null 2>&1 \
    && ok "đã tải" || loi "tải mô hình pyannote (đã đồng ý điều khoản 2 trang mô hình chưa?)"
else
  echo "  ⚠ Chưa có mô hình. Mô hình cần tài khoản Hugging Face (miễn phí). DAVID TỰ LÀM, một lần:"
  echo "     1. Đăng nhập huggingface.co, bấm đồng ý ở 2 trang: huggingface.co/pyannote/speaker-diarization-3.1 và huggingface.co/pyannote/segmentation-3.0"
  echo "     2. Tạo mã đọc (Read token) ở huggingface.co/settings/tokens, rồi chạy và dán mã vào:  ~/.venvs/pyannote/bin/huggingface-cli login"
  echo "     3. Chạy lại script này."
  echo "     Chưa làm thì podcast nhiều người vẫn dựng được (đoán người nói theo giọng), nhưng không giống hẳn Mac."
fi

if [ "$OS" != Darwin ]; then
  buoc "Dò mặt (thay Vision của Mac): YuNet + MediaPipe"
  [ -x "$CACHE/mat-venv/bin/python" ] || uv venv -q --python "$PYTHON" "$CACHE/mat-venv"
  if uv pip install -q --python "$CACHE/mat-venv/bin/python" "mediapipe==$MEDIAPIPE" "opencv-python-headless==$OPENCV" 2>/dev/null; then ok "mat-venv: mediapipe $MEDIAPIPE + opencv"
  else   # MediaPipe chưa có bản cho chip ARM trên Linux/Windows → vẫn dò khung mặt bằng YuNet, chỉ không đo độ mở miệng
    uv pip install -q --python "$CACHE/mat-venv/bin/python" "opencv-python-headless==$OPENCV" && \
      echo "  ⚠ mat-venv: chỉ có opencv (máy chip $(uname -m) chưa có MediaPipe) — dò được mặt, không đo độ mở miệng" || loi "opencv"
  fi
  tai "$YUNET_URL" "$CACHE/face_detection_yunet_2023mar.onnx" "$YUNET_SHA"
  tai "$LANDMARK_URL" "$CACHE/face_landmarker.task" "$LANDMARK_SHA"
  buoc "Font Arial (thẻ ghi nguồn ảnh, khung an toàn)"
  if [ -f /mnt/c/Windows/Fonts/arialbd.ttf ]; then ok "dùng font của Windows (C:\\Windows\\Fonts)"
  else echo "  ⚠ Không thấy Arial — cài: sudo apt install ttf-mscorefonts-installer (không có thì dùng DejaVu, chữ phần đó khác Mac)"; fi
  if grep -qi microsoft /proc/version 2>/dev/null && command -v powershell.exe >/dev/null; then
    buoc "Python phía Windows in chữ Việt bằng UTF-8 (biến người dùng PYTHONUTF8=1)"
    powershell.exe -NoProfile -Command "[Environment]::SetEnvironmentVariable('PYTHONUTF8','1','User')" >/dev/null 2>&1 && ok "PYTHONUTF8=1 (mở lại Claude để nhận)" || echo "  ⚠ Chưa đặt được PYTHONUTF8 — trong PowerShell: [Environment]::SetEnvironmentVariable('PYTHONUTF8','1','User')"
  fi
fi

echo
if [ $LOI = 0 ]; then echo "✅ Cài xong. Bước tiếp: zsh \"$HERE/kiem-tra-thiet-bi.sh\"  (dựng thử, so với Mac chính)"
else echo "⚠ Còn mục ✗ ở trên — sửa rồi chạy lại script này."; exit 1; fi
