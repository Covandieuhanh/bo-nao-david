#!/bin/bash
# Tự thử lệnh mở phiên lịch: mở một phiên qua chính chay-lich.sh (cùng cờ, cùng thư mục thêm) với lời giao vô hại,
# chờ tối đa 3 phút. Trả lời được THU-MO-PHIEN-OK → thoát 0. Kẹt hộp hỏi / không trả lời → in màn hình, thoát 1.
# Máy canh bot tự chạy mỗi khi chay-lich.sh bị sửa; chạy tay: bash tu-dong-hoa/lich/thu-mo-phien.sh
GOC="$(cd "$(dirname "$0")" && pwd)"; TT="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai"; MH="$TT/thu-mo-phien.txt"
bash "$GOC/chay-lich.sh" thu-mo-phien >/dev/null || { echo "chay-lich.sh lỗi"; exit 1; }
KQ=1
for i in $(seq 1 36); do
  sleep 5; S=$(screen -ls 2>/dev/null | awk '$1 ~ /\.lich-thu-mo-phien$/ {print $1; exit}')
  [ -z "$S" ] && { echo "phiên thử tự tắt trước khi trả lời"; break; }
  rm -f "$MH"; screen -S "$S" -p 0 -X hardcopy "$MH" 2>/dev/null; sleep 0.5
  if tr -d '\000' < "$MH" 2>/dev/null | grep -v "Chỉ trả lời" | grep -q "THU-MO-PHIEN-OK"; then KQ=0; break; fi
  tr -d '\000' < "$MH" 2>/dev/null | grep -qE "Enter to confirm|Esc to cancel|Do you trust|\(y/n\)" && [ $i -ge 4 ] && break
done
[ $KQ = 0 ] && echo "đạt: phiên lịch mở và trả lời bình thường" || { echo "hỏng, màn hình phiên thử:"; tr -d '\000' < "$MH" 2>/dev/null | grep -v '^[[:space:]]*$' | head -20; }
for s in $(screen -ls 2>/dev/null | awk '$1 ~ /\.lich-thu-mo-phien$/ {print $1}'); do screen -S "$s" -X quit; done
rm -f "$MH"; exit $KQ
