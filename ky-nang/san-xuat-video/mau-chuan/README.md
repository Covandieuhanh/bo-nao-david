# Bộ mẫu chuẩn (kiểm sau mỗi lần sửa)

`python3 -I kiem-mau.py` — dựng lại 5 dự án mẫu (`mau.json`: 3 clip podcast đồ hoạ dọc `podcast-doc-clip-1/2/3` và 2 video dài `podcast-dai-trainer`, `podcast-dai-muc-tieu`, David chốt làm bản chuẩn 2026-11-06) bằng
khung dựng + thư viện hình + hồ sơ HIỆN TẠI, chụp khung cố định → `<tên>/moi.jpg`, so `<tên>/chuan.jpg`.
- `✓ giữ nguyên` → sửa không làm vỡ chỗ khác. `⚠ hình đổi` → mở 2 tờ: đúng ý thay đổi thì `python3 -I kiem-mau.py <tên> --chot`.
- Chỉ đọc dự án gốc (dữ liệu lời, kịch bản, mốc); làm trong thư mục tạm. Thêm mẫu: thêm một mục vào `mau.json`.


Mẫu ảnh bìa podcast không mặt David duyệt 2026-11-06: `anh-thu-nho-podcast/chuan.jpg`. `kiem-mau.py` chưa kiểm ảnh bìa; sửa khuôn ảnh bìa thì dựng lại bằng lệnh ở khối 14 và so với file này.

Từ 2026-11-06 không còn mẫu đang chạy cho loại làm video có người nói, ghép vlog và highlight có người nói: dự án gốc đã dọn theo yêu cầu của David. Tờ `chuan.jpg` cũ của các loại đó vẫn giữ để tham khảo. Khi có video mới loại đó được duyệt, thêm lại vào `mau.json`.