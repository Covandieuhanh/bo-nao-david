#!/bin/zsh
# Dò mặt trên mọi máy: do-mat.sh <thư mục khung .jpg> <file json ra>   (cùng định dạng ra ở mọi máy)
# Mac: Vision (nhan-dien-khuon-mat.swift, như từ trước tới nay). Máy khác (Windows qua WSL2, Linux): YuNet + MediaPipe
# (nhan-dien-khuon-mat.py, quy đổi theo thước Vision bằng he-so-mat.json; môi trường do cai-cong-cu-video.sh cài).
SC=${0:A:h}
if [[ $OSTYPE == darwin* ]]; then
  export PATH=/opt/homebrew/bin:$PATH
  BIN=~/.cache/dung-video-theo-phong-cach/faces
  if [ ! -x $BIN ] || [ "$SC/nhan-dien-khuon-mat.swift" -nt $BIN ]; then
    mkdir -p ${BIN:h}; swiftc -O "$SC/nhan-dien-khuon-mat.swift" -o $BIN || exit 1
  fi
  exec $BIN "$@"
fi
PY=~/.cache/dung-video-theo-phong-cach/mat-venv/bin/python
[ -x $PY ] || { echo "⛔ Thiếu môi trường dò mặt — chạy: bash ~/Documents/bo-nao-david/tu-dong-hoa/may-khac/cai-cong-cu-video.sh"; exit 1; }
exec $PY "$SC/nhan-dien-khuon-mat.py" "$@" 2> >(grep -vE "^(W0000|I0000|INFO:)|absl::InitializeLog|inference_feedback_manager" >&2)
