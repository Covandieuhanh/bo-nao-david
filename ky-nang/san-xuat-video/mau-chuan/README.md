---
description: "Bộ mẫu chuẩn video: dựng lại 5 dự án mẫu bằng kiem-mau.py để kiểm tra sau mỗi lần sửa skill."
---

# Bộ mẫu chuẩn (kiểm tra sau mỗi lần sửa)

Lệnh `python3 -I kiem-mau.py` dựng lại 5 dự án mẫu (`mau.json`: 3 clip podcast đồ hoạ dọc `podcast-doc-clip-1/2/3` và 2 video dài `podcast-dai-trainer`, `podcast-dai-muc-tieu`, David chốt làm bản chuẩn 2026-11-06) bằng
khung dựng, thư viện hình và hồ sơ HIỆN TẠI, chụp khung hình cố định ra `<tên>/moi.jpg`, rồi so với `<tên>/chuan.jpg`.
- `✓ giữ nguyên` nghĩa là lần sửa không làm hỏng chỗ khác. `⚠ hình đổi` thì người làm mở 2 ảnh để so: nếu đúng ý thay đổi thì chạy `python3 -I kiem-mau.py <tên> --chot`.
- Công cụ chỉ đọc dự án gốc (dữ liệu lời, kịch bản, mốc) và làm trong thư mục tạm. Muốn thêm mẫu thì thêm một mục vào `mau.json`.
- **Chỉ chạy ở Mac chính**: cần các dự án gốc trong `~/Movies` của Mac (`mau.json`). Thiết bị khác (Windows qua WSL, Mac phụ) kiểm tra bằng
  `tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh`; nếu sửa skill trên thiết bị khác thì báo David chạy `kiem-mau.py` ở Mac chính trước khi dùng tiếp.


Mẫu ảnh bìa podcast không có mặt người, David duyệt 2026-11-06: `anh-thu-nho-podcast/chuan.jpg`. `kiem-mau.py` chưa kiểm tra ảnh bìa; khi sửa mẫu ảnh bìa, người làm dựng lại bằng lệnh ở khối 14 và so với file này.

Từ 2026-11-06 không còn mẫu đang chạy cho loại làm video có người nói, ghép vlog và highlight có người nói: dự án gốc đã dọn theo yêu cầu của David. Ảnh `chuan.jpg` cũ của các loại đó vẫn giữ để tham khảo. Khi có video mới loại đó được duyệt, người làm thêm lại vào `mau.json`.