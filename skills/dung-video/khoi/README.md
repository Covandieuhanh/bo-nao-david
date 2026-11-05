# Kho khối — mỗi khối một việc, viết MỘT lần, 4 công thức nhặt dùng

Sửa một cách làm → sửa đúng một khối (README + code của nó). Đổi con số → sửa `../ho-so/`, không sửa khối.

| Khối | Việc | Dùng trong |
|---|---|---|
| [00-loc-noi-dung](00-loc-noi-dung/README.md) | **Bộ lọc nội dung + phân phối kênh** (làm TRƯỚC): chấm theo hồ sơ David, 7 kết luận, phiếu lọc = cổng duyệt 1, sổ danh mục | mọi tài nguyên |
| [01-chep-loi](01-chep-loi/README.md) | Chép lời (Whisper) + hiểu video | cả 4 |
| [02-lam-sach](02-lam-sach/README.md) | Làm sạch: cắt thừa đầu/cuối, câu nói lại, khoảng lặng + tiếng đệm, sửa chiều hình | làm video, highlight (cắt lặng trong câu) |
| [03-phu-de](03-phu-de/README.md) | Phụ đề: dài = hộp tối đầy câu; ngắn = 1–3 chữ to mỗi nhịp, màu theo nghĩa | cả 4 |
| [04-khung-hinh](04-khung-hinh/README.md) | Khung hình: đổi khung (ngang↔dọc), nâng khung khi người nằm thấp | làm video, ghép vlog, highlight người nói (podcast: khung xuất riêng) |
| [05-tranh-che-nguoi](05-tranh-che-nguoi/README.md) | Tránh che người: lớp phủ không chạm mặt + đầu + vai + ngực; không có chỗ → tự toàn màn hình ≤ 4 s | làm video, ghép vlog, highlight người nói |
| [06-mo-dau](06-mo-dau/README.md) | Mở đầu 0–3 s: thẻ tít / hook, đoạn ghép mở vlog, teaser podcast dài | cả 4 |
| [07-canh-minh-hoa](07-canh-minh-hoa/README.md) | Cảnh minh hoạ toàn màn hình (2 trạng thái): biểu tượng vẽ, số chạy, sơ đồ + nhãn ≤ 3 chữ; ảnh thật chỉ khi cần | cả 4 |
| [08-ket-thuc](08-ket-thuc/README.md) | Kết: màn chốt (cta) · thẻ cuối (nhận diện / dẫn bản đầy đủ) · màn kết YouTube 15–20 s · lịch phát | cả 4 |
| [09-am-thanh](09-am-thanh/README.md) | Âm thanh: nhạc kênh cố định, tiếng ký hiệu, ting, vút; cân giọng −20 LUFS, bản cuối −14 LUFS | cả 4 |
| [10-nhan-dien](10-nhan-dien/README.md) | Bộ nhận diện David + phong cách (màu, font, dấu kênh, khuôn tiêu đề); rút phong cách từ video mẫu | cả 4 |
| [11-ghep-canh](11-ghep-canh/README.md) | Ghép cảnh từ nhiều clip: hiểu clip, giữ/bỏ, bản đồ liên kết, khung vlog, edl.js | ghép vlog, highlight người nói |
| [12-san-khau-podcast](12-san-khau-podcast/README.md) | Sân khấu podcast: tên tập, ý đang bàn (TOPICS + PHẦN n), sóng âm theo người nói, nền lắng | podcast, highlight từ podcast |
| [13-chon-khoanh-khac](13-chon-khoanh-khac/README.md) | Chọn khoảnh khắc highlight: bản đồ cả video, 3–5 clip, chọn câu, bố trí lời kêu gọi, cắt + kiểm lời | highlight |
| [14-thumbnail](14-thumbnail/README.md) | Thumbnail YouTube 1280×720 (chỉ video ngang đăng YouTube): mặt + ≤ 3 tầng chữ, số khổng lồ, nhãn series | làm video, ghép vlog, podcast |
| [15-phat-hanh](15-phat-hanh/README.md) | Phát hành: 3 tiêu đề, mô tả, mốc khung bìa, chương YouTube, teaser, bình luận ghim | cả 4 |
| [16-so-lieu](16-so-lieu/README.md) | Số liệu sau đăng (báo lỗi, không quyết định): ảnh chụp số liệu 7 ngày → so-lieu.md | cả 4 |
| [17-dung-kiem-tra](17-dung-kiem-tra/README.md) | Dựng + kiểm tra: chụp thử từng cảnh, render, ghép bản cuối, soát khung / âm lượng / tiếng rè | cả 4 |
| [18-xuat-app-dung](18-xuat-app-dung/README.md) | Xuất timeline DaVinci / dự án CapCut (chỉ khi David yêu cầu) | làm video, podcast |
| [19-dang-bai](19-dang-bai/README.md) | Đăng / hẹn giờ YouTube, trang Facebook, TikTok qua trình duyệt (sau cổng 2); Facebook cá nhân David tự chia sẻ | dang-da-kenh |
| [20-hop-thu-so-lieu](20-hop-thu-so-lieu/README.md) | Gom bình luận + tin nhắn (đếm "gỡ"), số liệu 24 giờ / 7 ngày — chỉ đọc | dang-da-kenh |

Đọc kèm: `../nguyen-tac.md` (7 điểm chung), `../luat-chung.md` (luật nền), `../ho-so/` (tham số), `hoso.py` (đọc tham số).

Thành phần hình dùng chung: `../thu-vien-hinh/` (một bản). Kiểm sau khi sửa: `python3 -I ../mau-chuan/kiem-mau.py`.
