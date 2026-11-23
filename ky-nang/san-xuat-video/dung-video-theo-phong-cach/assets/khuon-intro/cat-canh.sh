#!/bin/bash
# cat-canh.sh <thư mục 1-goc> <danh-sach-canh.txt> <thư mục ra public/canh>
# Cắt từng đoạn: tự xoay đúng chiều, chỉ lấy luồng hình đầu (file DJI có nhiều luồng), 1920×1080, 30 khung/giây, chỉnh màu nhẹ cho đều.
set -euo pipefail
GOC="$1"; DS="$2"; RA="$3"; mkdir -p "$RA"
MAU="fps=30,eq=contrast=1.06:saturation=1.12:brightness=0.01"
grep -v '^#' "$DS" | while read -r id mau_file ss len co; do
  [ -z "${id:-}" ] && continue
  f=$(compgen -G "$GOC/$mau_file" | head -1) || { echo "✗ không thấy $mau_file"; exit 1; }
  if [ "${co:-}" = "bo-logo" ]; then vf="crop=1728:972:192:60,scale=1920:1080,$MAU"
  else vf="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,$MAU"; fi
  ffmpeg -v error -y -ss "$ss" -i "$f" -t "$len" -map 0:v:0 -an -vf "$vf" -c:v libx264 -preset fast -crf 17 -pix_fmt yuv420p "$RA/$id.mp4" </dev/null
  echo "✓ $id"
done
