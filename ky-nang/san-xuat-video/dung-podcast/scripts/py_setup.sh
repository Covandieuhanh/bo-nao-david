#!/bin/zsh
# Cài numpy vào venv dùng chung (một lần) cho speakers.py / envelope.py → in đường dẫn python
set -e
VENV=~/.cache/dung-video-theo-phong-cach/podcast-venv
$VENV/bin/python -c "import numpy" 2>/dev/null || { python3 -m venv $VENV; $VENV/bin/pip install -q numpy >/dev/null 2>&1; }
echo $VENV/bin/python
