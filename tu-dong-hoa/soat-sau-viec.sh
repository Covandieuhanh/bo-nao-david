#!/bin/bash
# SOÁT SAU VIỆC (chuẩn mực làm việc mục 4): một lệnh chạy đủ mọi công cụ kiểm tra của bộ não trước khi báo David.
# Dùng: bash tu-dong-hoa/soat-sau-viec.sh        Mã trả về 1 khi có công cụ chặn báo lỗi.
# Việc sửa hàng loạt (đổi tên, thay từ, viết lại nhiều file) còn thêm một bước ngoài lệnh này: một AI khác soát diff trước khi báo.
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO" || exit 1
LOI=0
chay() { local ten="$1"; shift; echo "== $ten"; "$@" || { echo "   ⛔ $ten chưa đạt"; LOI=1; }; }
chay "Liên kết (0 gãy, 0 mồ côi)" python3 -I tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py
chay "Cây quy trình" python3 -I tu-dong-hoa/kiem-quy-trinh.py
chay "Cổng kiểm soát gốc" python3 -I tu-dong-hoa/cong-kiem-soat-goc.py
chay "Quét bí mật" python3 -I tu-dong-hoa/quet-bi-mat.py "$REPO"
echo "== Ngôn từ"; python3 -I tu-dong-hoa/kiem-ngon-tu.py | head -5
echo "== Chồng chéo bản luật"; python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py | tail -1
echo "== Bài kiểm (đáp án mẫu phải đủ điểm)"
python3 -I co-so-tri-thuc/bai-kiem/cham.py --mau > /tmp/_mau1.json && python3 -I co-so-tri-thuc/bai-kiem/cham.py /tmp/_mau1.json | tail -1
python3 -I ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/cham.py --mau > /tmp/_mau2.json && python3 -I ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/cham.py /tmp/_mau2.json | tail -1
echo "== Cú pháp mã của file vừa đổi"
for f in $( (git diff --name-only HEAD; git diff --cached --name-only) | sort -u ); do
  [ -f "$f" ] || continue
  case "$f" in
    *.py) python3 -m py_compile "$f" || { echo "   ⛔ $f"; LOI=1; };;
    *.sh) head -1 "$f" | grep -q zsh || bash -n "$f" || { echo "   ⛔ $f"; LOI=1; };;
    *.mjs) node --check "$f" 2>/dev/null || { echo "   ⛔ $f"; LOI=1; };;
    *.js|*.jsx) case "$f" in */assets/*|*/thu-vien-tai-nguyen/*|*/chuyen-dong/*) ;; *) node --check "$f" 2>/dev/null || { echo "   ⛔ $f"; LOI=1; };; esac;;
    *.json) python3 -c "import json,sys;json.load(open(sys.argv[1],encoding='utf-8'))" "$f" || { echo "   ⛔ $f"; LOI=1; };;
  esac
done
[ -f tu-dong-hoa/hoc-lien-tuc/thang-cap.py ] && { echo "== Đề xuất thăng cấp"; python3 -I tu-dong-hoa/hoc-lien-tuc/thang-cap.py | tail -6; }
[ -f tu-dong-hoa/hoc-lien-tuc/phu-cau-kiem.py ] && { echo "== Bộ kiểm phủ luật"; python3 -I tu-dong-hoa/hoc-lien-tuc/phu-cau-kiem.py | tail -3; }
if [ $LOI = 0 ]; then echo "✓ Soát sau việc: đạt. Việc sửa hàng loạt: còn bước AI khác soát diff."; else echo "⛔ Soát sau việc: có công cụ chưa đạt, sửa rồi chạy lại."; exit 1; fi
