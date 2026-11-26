#!/bin/bash
# KẾT NỐI MÁY NÀY VỚI GOOGLE DRIVE ĐỂ TẢI LÊN BẰNG LỆNH — DAVID TỰ CHẠY, một lần (duyệt 26/11/2026).
# Không tạo ổ đĩa, không đồng bộ nền. Quyền drive.file: rclone chỉ thấy và sửa tệp, thư mục do chính nó tạo.
# Khoá truy cập nằm ở ~/.config/rclone/rclone.conf trên máy này: không đưa lên GitHub, Claude không mở, không in.
# Thu hồi: myaccount.google.com → Bảo mật → ứng dụng có quyền truy cập → xoá; rồi: rclone config delete drive-david
RC=drive-david
GOC=thanh-pham-may-windows
command -v rclone >/dev/null || { echo "✗ Chưa có rclone: tải ở https://rclone.org/downloads/"; exit 1; }
if rclone listremotes | grep -qx "$RC:"; then
  echo "Đã có kết nối $RC. Đang kiểm..."
else
  echo "Mã ứng dụng Google RIÊNG (nên có: mã dùng chung của rclone sắp ngừng trong năm 2026)."
  echo "Cách tạo: tu-dong-hoa/thiet-bi-khac/ket-noi-drive.md. Chưa có thì để trống rồi bấm Enter."
  read -r -p "Client ID: " ID
  THEM=()
  if [ -n "$ID" ]; then
    read -r -s -p "Client secret (gõ hoặc dán, chữ không hiện): " BIMAT; echo
    THEM=(client_id "$ID" client_secret "$BIMAT")
  fi
  echo
  echo "Sắp hiện một đường link bắt đầu bằng http://127.0.0.1:53682/ : mở link đó trong trình duyệt trên máy này,"
  echo "đăng nhập Google và bấm Cho phép. Xong thì cửa sổ này tự chạy tiếp."
  # --no-output: không in cấu hình (có khoá truy cập) ra màn hình
  rclone config create "$RC" drive scope drive.file "${THEM[@]}" --no-output || { echo "✗ Chưa kết nối được"; rclone config delete "$RC"; exit 1; }
  chmod 600 "$(rclone config file | tail -1)"
fi
rclone mkdir "$RC:$GOC" && rclone lsf "$RC:" --dirs-only | grep -qx "$GOC/" \
  && echo "✓ ĐÃ KẾT NỐI. Trên Drive có thư mục $GOC. Báo Claude \"đã kết nối\"." \
  || { echo "✗ Có cấu hình nhưng chưa dùng được. Xoá rồi làm lại: rclone config delete $RC"; exit 1; }
