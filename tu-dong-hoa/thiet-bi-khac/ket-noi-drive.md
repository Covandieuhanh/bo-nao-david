---
description: "Hướng dẫn David kết nối máy Windows với Google Drive để tải lên bằng lệnh (rclone), gồm cách tạo mã ứng dụng Google riêng."
---

# Kết nối máy Windows để tải lên Drive (làm một lần, David tự làm)

Chạy trong PowerShell, rồi làm theo chữ trên màn hình:

```powershell
wsl -d Ubuntu-24.04 -- bash -lc "bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/ket-noi-drive.sh"
```

## Tạo mã ứng dụng Google riêng (nên làm)

Tài liệu rclone (đọc 26/11/2026, https://rclone.org/drive/ mục "Making your own client_id") ghi mã dùng chung sẽ ngừng hoạt động trong năm 2026, chưa công bố ngày.
Màn hình của Google hay đổi; khác chữ dưới đây thì theo tài liệu đó.

1. Mở https://console.cloud.google.com/ , tạo một dự án mới (đặt tên ví dụ `tai-len-drive`).
2. Tìm "Google Drive API" → **Enable**.
3. Mở "Google Auth Platform" → **Get started**: tên ứng dụng, email hỗ trợ, đối tượng **External**, email liên hệ → tạo.
4. Mục **Clients** → **Create client** → loại **Desktop app** → chép Client ID và Client secret (không gửi vào chat).
5. Mục **Audience** → **Publish app**. Để ở chế độ thử (Testing) thì quyền hết hạn sau một tuần. Nếu nút bị mờ, mục **Branding** đang đòi trang chủ và trang chính sách riêng tư; vướng ở đây thì báo Claude.
6. Chạy lệnh ở trên, dán Client ID và Client secret khi được hỏi. Google có thể cảnh báo ứng dụng chưa xác minh: đó là ứng dụng của chính bạn.

Đã lỡ kết nối bằng mã dùng chung, muốn đổi: `rclone config delete drive-david` rồi chạy lại.
