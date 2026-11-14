#!/bin/bash
# kiem-tra.sh <pptx> <outdir>: Quick Look preview -> PNG per slide -> contact sheets
set -e
cd "$(dirname "$0")"
P="$1"; O="$2"
mkdir -p "$O"
timeout 60 qlmanage -p -o "$O" "$P" >/dev/null 2>&1 || true
Q=$(ls -d "$O"/*.qlpreview | head -1)
for f in "$Q"/Attachment*.pdf; do sips -s format png "$f" --out "${f%.pdf}.png" >/dev/null 2>&1; done
sed -i '' 's/\(Attachment[0-9]*\)\.pdf/\1.png/g' "$Q/Preview.html"
node trang-quicklook.mjs "$PWD/$Q/Preview.html" "$PWD/$O/sl"
venv/bin/python bang-tinh.py "$O"
