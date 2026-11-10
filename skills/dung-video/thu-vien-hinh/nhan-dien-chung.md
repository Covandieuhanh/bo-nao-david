# Bộ nhận diện chung — mọi loại video

**Mọi loại video có cùng tiêu chuẩn** (vị trí, thành phần cố định, ngôn ngữ thiết kế). Chỉ **motion graphics** là tự do chọn theo loại
video và theo từng cảnh. Một nguồn code: `nhan-dien.js` (`khung(W, H)`), `DauGoc.jsx`, `ThanhThoiGian.jsx`, `EndCardBody.jsx`,
`tokens.js`, `brand.json`, `subStyle.js`, `cta.js`, `Icons.jsx`. Khuôn 1 video, podcast, ghép vlog, highlight đều đọc ở đây.

## 0. Chữ ký nhận diện — thứ duy nhất thẩm mỹ phải giữ

> "Về thẩm mỹ thì tôi chỉ cần duy nhất 1 thứ là người xem có thể nhận diện được dù xem video nào cũng là của cùng 1 người làm." — David

Giữ ở MỌI video, mọi cảnh có chữ:
1. Các thành phần cố định ở mục 1 (dấu góc ● DAVID, phụ đề, thanh thời gian, màn chốt, thẻ cuối) — đúng vị trí, đúng kiểu.
2. **Màu nhấn cam** `C.accent` là màu nhấn duy nhất (khoảng 10 % khung). Màu nền và màu phụ đổi theo nội dung được.
3. **Hai font chính** `HEAD` (Barlow Condensed) cho chữ to, `BODY` (Be Vietnam Pro) cho chữ thường. Font phụ `NHAN` (chữ có chân,
   nghiêng) chỉ cho **một từ nhấn** trong cụm (`*từ*` trong ChuHien), không thay font chính.

Ngoài ba điều trên là **tự do sáng tạo theo nội dung**: nền tối / sáng / giấy / người mờ, kết cấu, ánh sáng, kiểu hình (biểu tượng nét
tròn, phấn vẽ tay, ảnh), bố cục, chuyển động. Thử: che dấu góc đi, người xem quen kênh vẫn đoán được là video của David nhờ cam + chữ
+ phụ đề → đạt. Màu nhấn, hai font chính, nhạc kênh (`tokens.js`, `brand.json`) không đổi khi học video mẫu.

## 1. Thành phần cố định (có ở mọi video)

| Thành phần | Khung dọc 1080×1920 | Khung ngang 1920×1080 | Code |
|---|---|---|---|
| Vùng an toàn | x 70–900, y 210–1420 (chừa nút, chữ của Reels/TikTok) | lề 5 % mỗi bên, trên 5 %, dưới 15 % | `khung().safe` |
| Dấu góc ● DAVID │ chủ đề | góc trên trái, top 228 | góc trên trái, top 54 (sát mép vùng an toàn) | `DauGoc.jsx`, `khung().brand` |
| Thanh thời gian (đã chạy · thanh · còn m:ss) | y 1386, cao 30 — chỉ video dọc dài | y 884, cao 30 | `ThanhThoiGian.jsx`, `khung().tl` |
| Phụ đề | luôn chạy, đáy ngay trên thanh thời gian (y 1374) | như dọc (y 870) | `subStyle.js`, `khung().capBottom` |
| Màn chốt (`cta`) | câu nguyên văn ≤ 55 ký tự, tick + "ting" | như dọc, ô video 50 % bề ngang, ẩn dấu góc | `cta.js`, `Action.jsx` / `Show.jsx` |
| Thẻ cuối | chỉ video dọc dài: nhận diện / dẫn bản đầy đủ | nhận diện (chủ đề + DAVID) | `EndCardBody.jsx` |
| Màn kết YouTube (video dài) | — | 15–20 s, khung chừa 2 video + nút đăng ký | `YtEnd.jsx` |

Chủ đề ở dấu góc: `project.topic` (1 video), `show.name` (vlog), tên chương trình (podcast), tên tập gốc (highlight).
Khuôn tiêu đề: dòng nhỏ cam → gạch cam → chữ cô đặc in hoa trắng, dòng nhấn cam.

Luật kèm theo:
- **Không logo nền tảng, không nút phát đỏ** ở bất kỳ thẻ nào.
- Mọi lớp phủ góc trên nằm **dưới** `brand.bottom` (`BRAND_BOT`); mọi lớp phủ đáy nằm **trên** phụ đề và thanh thời gian. Không viết
  số vị trí của khung dọc vào khung ngang.
- **Video dọc ngắn** (Reels/TikTok/Shorts — dọc ≤ 90 s, mọi highlight, podcast dọc trích ngắn): **không thanh thời gian, không thẻ
  cuối**; màn chốt hiện câu nguyên văn ngay trên khung hình (không thu nhỏ video), video kết ở chữ cuối để tự lặp. Lý do: nền tảng đã
  có thanh riêng, "còn 0:20" và màn "hết rồi" khiến người xem lướt đi, thẻ cuối làm đứt vòng lặp. Dẫn về bản đầy đủ / mời bình luận
  để ở caption + bình luận ghim. Máy tự nhận (`nganDoc()` trong `nhan-dien.js`, `NGAN_DOC` trong `thanh.js`).
- Ép tay: thanh thời gian `project.thanh` / thẻ cuối `project.theCuoi` (khuôn 1 video, podcast) · `export const THANH` /
  `THE_CUOI` (edl.js khuôn ghép).
- Highlight có thanh của cả tập gốc (`HL.bar`) thì thanh đó thay thanh thường, cùng vị trí.

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
