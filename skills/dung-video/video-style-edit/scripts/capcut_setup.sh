#!/bin/zsh
# Cài pycapcut (tạo dự án CapCut) vào venv dùng chung, một lần: capcut_setup.sh → in đường dẫn python của venv
set -e
VENV=~/.cache/video-style-edit/capcut-venv
if ! $VENV/bin/python -c "import pycapcut" 2>/dev/null; then
  python3 -m venv $VENV
  $VENV/bin/pip install -q "pycapcut==0.0.4" >/dev/null   # 0.1.0 đổi API track — giữ 0.0.4
fi
echo $VENV/bin/python
