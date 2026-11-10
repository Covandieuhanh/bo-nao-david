# Bộ nhận diện chung — mọi loại video

David chốt 08/11/2026: **mọi loại video có cùng tiêu chuẩn** (vị trí, thành phần cố định, ngôn ngữ thiết kế). Chỉ **motion graphics** là
tự do chọn theo loại video và theo từng cảnh. Một nguồn code: `nhan-dien.js` (`khung(W, H)`), `DauGoc.jsx`, `ThanhThoiGian.jsx`,
`EndCardBody.jsx`, `tokens.js`, `brand.json`, `subStyle.js`. Khuôn 1 video, podcast, ghép vlog, highlight đều đọc ở đây.

## 1. Thành phần cố định (có ở mọi video)

| Thành phần | Khung dọc 1080×1920 | Khung ngang 1920×1080 | Code |
|---|---|---|---|
| Vùng an toàn | x 70–900, y 210–1420 (chừa nút, chữ của Reels/TikTok) | lề 5 % mỗi bên, trên 5 %, dưới 15 % | `khung().safe` |
| Dấu góc ● DAVID │ chủ đề | góc trên trái, top 228 | góc trên trái, top 54 (sát mép vùng an toàn) | `DauGoc.jsx`, `khung().brand` |
| Thanh thời gian (đã chạy · thanh · còn m:ss) | y 1386, cao 30 — **chỉ video dọc dài**; dọc ngắn không có (10/11) | y 884, cao 30 | `ThanhThoiGian.jsx`, `khung().tl` |
| Phụ đề | luôn chạy, đáy ngay trên thanh thời gian (y 1374) | như dọc (y 870) | `subStyle.js`, `khung().capBottom` |
| Màn chốt (`cta`) | câu nguyên văn ≤ 55 ký tự, tick + "ting"; dọc ngắn: ô câu đặt trên khung hình, không thu nhỏ video (10/11) | như dọc, ô video 50 % bề ngang, ẩn dấu góc | `cta.js`, `Action.jsx` / `Show.jsx` |
| Thẻ cuối | **bỏ ở video dọc ngắn** (10/11/2026); video dọc dài: nhận diện / dẫn bản đầy đủ | — | `EndCardBody.jsx` |
| Màn kết YouTube (video dài) | — | 15–20 s, khung chừa 2 video + nút đăng ký | `YtEnd.jsx` |

Luật kèm theo:
- **Không logo nền tảng, không nút phát đỏ** ở bất kỳ thẻ nào (06/11/2026).
- Mọi lớp phủ góc trên nằm **dưới** `brand.bottom`; mọi lớp phủ đáy nằm **trên** phụ đề và thanh thời gian.
- **Video dọc ngắn** (Reels/TikTok/Shorts — dọc ≤ 90 s, mọi highlight, podcast dọc trích ngắn; David chốt 10/11/2026): **không thanh thời gian, không thẻ cuối**; màn chốt hiện câu nguyên văn ngay trên khung hình (không thu nhỏ video), video kết ở chữ cuối để tự lặp. Lý do: nền tảng đã có thanh riêng, "còn 0:20" và màn "hết rồi" khiến người xem lướt đi, thẻ cuối làm đứt vòng lặp. Dẫn về bản đầy đủ / mời bình luận để ở caption + bình luận ghim. Máy tự nhận (`nganDoc()` trong `nhan-dien.js`, `NGAN_DOC` trong `thanh.js`); ép tay `project.thanh` / `project.theCuoi` (1 video, podcast) · `THANH` / `THE_CUOI` (edl.js).
- Ép tay thanh thời gian: `project.thanh = false` (khuôn 1 video, podcast) · `export const THANH = false` (edl.js khuôn ghép).
- Highlight có thanh của cả tập gốc (`HL.bar`) thì thanh đó thay thanh thường, cùng vị trí.
- Màu, font, nét vẽ, tiếng ký hiệu, nhạc kênh: `tokens.js`, `Icons.jsx`, `brand.json` — không đổi khi học video mẫu.

## 2. Phần tự do (motion graphics)

Bố cục và hiệu ứng trong lòng video (thẻ, chữ to, minh hoạ, sơ đồ, người vào ô, màn chương, điểm nhấn trên người…) chọn theo nội dung,
theo danh mục `../trinh-bay/bo-cuc.md`. Tự do về **cái gì, lúc nào**; không tự do về **vị trí các thành phần cố định** ở mục 1.

## 3. Sửa bộ nhận diện

1. Sửa đúng một chỗ trong thư mục này (không viết số vị trí riêng trong khuôn dựng).
2. Chụp kiểm cả khung ngang lẫn dọc, mỗi loại một dự án đã duyệt: podcast ngang (`tap-di-trainer/2-ban-dai`), clip podcast dọc
   (`tap-di-trainer/3-highlight/clip-A`), video người nói ngang (`tap-su-tap-trung/2-ban-dai`, `tap-di-bo-hang-ngay/2-ban-dai`),
   clip người nói dọc (`tap-*/3-highlight/clip-A` của 4 video cũ).
3. Đẩy GitHub.

## 4. Còn thiếu (ghi để không quên)

- **Vlog ghép clip khung ngang:** khuôn ghép đã lấy vùng an toàn, dấu góc, thanh thời gian theo `khung()`, nhưng nhiều thành phần
  bên trong (thẻ địa điểm, thẻ tên, màn chốt, thẻ cuối) vẫn đặt số theo khung dọc. Chưa có dự án vlog ngang để kiểm → làm vlog ngang
  đầu tiên thì chụp kiểm kỹ và sửa các thành phần đó theo `khung()`.
- Màn `pow` toàn khung của khuôn ghép: lề trái lệch (~18 px), dải tối khác màu ở đỉnh — chưa sửa (xem `cat-highlight-video/references/changelog.md`).
