#!/bin/bash
# cat-canh.sh <thư mục 1-goc> <danh-sach-canh.txt> <thư mục ra public/canh>
# Cắt từng đoạn: tự xoay đúng chiều, chỉ lấy luồng hình đầu (file DJI có nhiều luồng), 1920×1080, 30 khung/giây,
# màu điện ảnh chung cho mọi đoạn (học từ intro diễn giả 23/11: tối, ấm, ít màu, viền tối nhẹ) để các cảnh liền một khối.
set -euo pipefail
GOC="$1"; DS="$2"; RA="$3"; mkdir -p "$RA"
MAU="fps=30,eq=contrast=1.12:saturation=0.86:brightness=-0.02:gamma=0.96,colorbalance=rs=-0.02:bs=0.04:rh=0.05:gh=0.01:bh=-0.05,vignette=angle=PI/5"
grep -v '^#' "$DS" | while read -r id mau_file ss len co; do
  [ -z "${id:-}" ] && continue
  f=$(compgen -G "$GOC/$mau_file" | head -1) || { echo "✗ không thấy $mau_file"; exit 1; }
  case "${co:-}" in
    bo-logo) vf="crop=1728:972:192:60,scale=1920:1080,$MAU" ;;
    phai)    vf="crop=1280:720:640:200,scale=1920:1080:flags=lanczos,$MAU" ;;
    *)       vf="scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,$MAU" ;;
  esac
  ffmpeg -v error -y -ss "$ss" -i "$f" -t "$len" -map 0:v:0 -an -vf "$vf" -c:v libx264 -preset fast -crf 16 -pix_fmt yuv420p "$RA/$id.mp4" </dev/null
  echo "✓ $id"
done
