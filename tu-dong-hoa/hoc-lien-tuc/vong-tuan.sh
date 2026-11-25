#!/bin/bash
# VÒNG TUẦN (skill hoc-lien-tuc Việc 1) chạy tay ở bất kỳ máy nào: gom mọi tín hiệu rồi in ra để AI làm buổi nhìn lại tuần.
# Dùng: bash tu-dong-hoa/hoc-lien-tuc/vong-tuan.sh   rồi mở skill hoc-lien-tuc Việc 1, ghi kết quả vào du-an/hoc-lien-tuc/<YYYY-MM-DD>.md
REPO="$(cd "$(dirname "$0")/../.." && pwd)"; cd "$REPO" || exit 1
echo "== Vòng tuần gần nhất: $(ls du-an/hoc-lien-tuc/ 2>/dev/null | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}' | sort | tail -1 | cut -c1-10)"
echo "== Skill dùng và lời David sửa (30 ngày, máy này)"; python3 -I tu-dong-hoa/hoc-lien-tuc/dem-ky-nang.py 30
[ -f tu-dong-hoa/hoc-lien-tuc/thang-cap.py ] && { echo "== Đề xuất thăng cấp"; python3 -I tu-dong-hoa/hoc-lien-tuc/thang-cap.py; }
[ -f tu-dong-hoa/hoc-lien-tuc/phu-cau-kiem.py ] && { echo "== Bộ kiểm phủ luật"; python3 -I tu-dong-hoa/hoc-lien-tuc/phu-cau-kiem.py; }
[ -f tu-dong-hoa/hoc-lien-tuc/de-xuat-cat-giam.py ] && { echo "== Đề xuất cắt giảm"; python3 -I tu-dong-hoa/hoc-lien-tuc/de-xuat-cat-giam.py; }
echo "== Chồng chéo bản luật"; python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py | tail -2
echo "Tiếp theo: mở skill hoc-lien-tuc Việc 1 với kết quả trên; ghi du-an/hoc-lien-tuc/$(date +%F).md; đề xuất sửa trong 4 phần cho David."
