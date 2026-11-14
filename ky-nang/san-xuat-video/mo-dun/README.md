---
description: "Kho khối dựng video: mỗi khối một việc, viết một lần, 4 công thức nhặt dùng; danh sách khối."
---

# Kho khối — mỗi khối một việc, viết MỘT lần, 4 công thức nhặt dùng

Sửa một cách làm → sửa đúng một khối (README + code của nó). Đổi con số → sửa `../ho-so-thuong-hieu/`, không sửa khối.

| Khối | Việc | Dùng trong |
|---|---|---|
| [00-sang-loc-noi-dung](00-sang-loc-noi-dung/README.md) | **Bộ lọc nội dung + phân phối kênh** (làm TRƯỚC): chấm theo hồ sơ David, 7 kết luận, phiếu lọc (không chờ duyệt), sổ danh mục | mọi tài nguyên |
| [01-phien-am](01-phien-am/README.md) | Chép lời (Whisper) + hiểu video | cả 4 |
| [02-lam-sach](02-lam-sach/README.md) | Làm sạch: cắt thừa đầu/cuối, câu nói lại, khoảng lặng + tiếng đệm, sửa chiều hình | làm video, highlight (cắt lặng trong câu) |
| [03-phu-de](03-phu-de/README.md) | Phụ đề: dài = hộp tối đầy câu; ngắn = cụm 5–8 chữ cỡ bằng chữ thẻ, mỗi lúc một chỗ chữ | cả 4 |
| [04-khung-hinh](04-khung-hinh/README.md) | Khung hình: đổi khung (ngang↔dọc), nâng khung khi người nằm thấp | làm video, ghép vlog, highlight người nói (podcast: khung xuất riêng) |
| [05-tranh-che-chu-the](05-tranh-che-chu-the/README.md) | Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ → tự toàn màn hình, dài theo nội dung | làm video, ghép vlog, highlight người nói |
| [06-phan-mo-dau](06-phan-mo-dau/README.md) | Mở đầu 0–3 s: câu chạm, thẻ tít nguyên văn (highlight), đoạn ghép mở vlog, teaser podcast dài | cả 4 |
| [07-canh-minh-hoa](07-canh-minh-hoa/README.md) | Bố cục tự cân, motion graphic kể chuyện, điểm nhấn trên người, minh hoạ, sơ đồ, chuyển động; ảnh thật chỉ khi cần | cả 4 |
| [08-phan-ket](08-phan-ket/README.md) | Kết: màn chốt (cta) · thẻ cuối (nhận diện / dẫn bản đầy đủ) · màn kết YouTube 15–20 s · lịch phát | cả 4 |
| [09-am-thanh](09-am-thanh/README.md) | Âm thanh: nhạc kênh cố định, tiếng ký hiệu, ting, vút; cân giọng −20 LUFS, bản cuối −14 LUFS | cả 4 |
| [10-nhan-dien-thuong-hieu](10-nhan-dien-thuong-hieu/README.md) | Bộ nhận diện David + phong cách (màu, font, dấu kênh, khuôn tiêu đề); rút phong cách từ video mẫu | cả 4 |
| [11-dung-ghep](11-dung-ghep/README.md) | Ghép cảnh từ nhiều clip: hiểu clip, giữ/bỏ, bản đồ liên kết, khung vlog, danh-sach-cat.js | ghép vlog, highlight người nói |
| [12-san-khau-podcast](12-san-khau-podcast/README.md) | Sân khấu podcast: tên tập, ý đang bàn (TOPICS + PHẦN n), sóng âm theo người nói, nền lắng | podcast, highlight từ podcast |
| [13-chon-doan-noi-bat](13-chon-doan-noi-bat/README.md) | Chọn khoảnh khắc highlight: bản đồ cả video, tự chọn ý theo 4 câu, chọn câu, bố trí lời kêu gọi, cắt + kiểm lời | highlight |
| [14-anh-thu-nho](14-anh-thu-nho/README.md) | Thumbnail YouTube 1280×720 (chỉ video ngang đăng YouTube): quay hình = mặt + ≤ 3 tầng chữ; podcast = bìa không mặt | làm video, ghép vlog, podcast |
| [15-xuat-ban](15-xuat-ban/README.md) | Phát hành: 3 tiêu đề, mô tả, mốc khung bìa, chương YouTube, teaser, bình luận ghim | cả 4 |
| [16-phan-tich-so-lieu](16-phan-tich-so-lieu/README.md) | Số liệu sau đăng (báo lỗi, không quyết định): ảnh chụp số liệu 7 ngày → so-lieu.md | cả 4 |
| [17-kiem-soat-chat-luong](17-kiem-soat-chat-luong/README.md) | Dựng + kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, soát khung / âm lượng / tiếng rè | cả 4 |
| [19-dang-bai](19-dang-bai/README.md) | Đăng / hẹn giờ YouTube, trang Facebook, TikTok qua trình duyệt (khi David nói "đăng"); Facebook cá nhân David tự chia sẻ | phan-phoi-da-kenh |
| [20-hop-thu-so-lieu](20-hop-thu-so-lieu/README.md) | Gom bình luận + tin nhắn (đếm "gỡ"), số liệu 24 giờ / 7 ngày — chỉ đọc | phan-phoi-da-kenh |

Đọc kèm: `../nguyen-tac.md` (7 điểm chung), `../quy-tac-chung.md` (luật nền), `../ho-so-thuong-hieu/` (tham số), `ho_so.py` (đọc tham số).

Thành phần hình dùng chung: `../thu-vien-tai-nguyen/` (một bản). Kiểm sau khi sửa: `python3 -I ../mau-chuan/kiem-mau.py`.
