---
description: "Thư viện hình dùng chung cho cả 4 loại video: file, việc, khối dùng."
---

# Thư viện hình dùng chung (một bản duy nhất cho cả 4 loại video)

| File | Việc | Khối |
|---|---|---|
| `bien-thiet-ke.js` | màu, font, hàm ease của kênh | 10 |
| `thuong-hieu.json` | tên kênh, tiếng ký hiệu, mức nhạc, độ dài thẻ cuối | 10 · 09 |
| `kieu-phu-de.js` | phụ đề dài (SUB) và ngắn cụm 5–8 chữ cỡ 58 (ShortLine, chunks), tô màu theo nghĩa | 03 |
| `keu-goi-hanh-dong.js` | câu màn chốt dự phòng, biểu tượng, mốc tick | 08 |
| `bieu-tuong.jsx` | biểu tượng nét vẽ dần (Icon, Pictogram) | 07 |
| `man-ket-youtube.jsx` | màn kết YouTube 15–20 s | 08 |
| `minh-hoa.jsx` | cảnh minh hoạ toàn màn hình | 07 |
| `so-do.jsx` | sơ đồ nói thay lời: tang, vong, moc, cot, luoi, tu-thanh, xay-tang, doi-trang-thai, chuyen-giao, anh | 07 |
| `than-man-ket.jsx` | nội dung bên trong thẻ cuối (gạch nhận diện, BẢN ĐẦY ĐỦ TRÊN KÊNH…, tên, người nói, lịch phát; không logo nền tảng) | 08 |
| `nhan-dien-thuong-hieu.js` | **bộ nhận diện chung**: vùng an toàn ngang/dọc, vị trí dấu góc, thanh thời gian, đáy phụ đề (`khung(W, H)`) — xem `nhan-dien-chung.md` | 10 |
| `dau-goc.jsx` | dấu góc ● DAVID │ chủ đề | 10 |
| `thanh-thoi-gian.jsx` | thanh thời gian ở đáy: đã chạy · thanh · còn m:ss | 10 |
| `chuyen-dong.js` | easing theo vai, vào/ra mờ nhoè, chữ hiện từng từ (3 kiểu), lò xo theo ζ, thời gian đọc | 07 |
| `chu-hien.jsx` | một dòng chữ hiện từng từ theo kiểu của `chuyen-dong.js`, không dịch chỗ | 07 |
| `mach.js` | **mạch hình**: một hình kể chuyện vẽ tiếp qua nhiều cảnh tự vẽ (`buoc`, `tu_buoc`, `moc_buoc`) và nét vẽ dần `net()` | 07 |

Cách nối: `mau-remotion/src/thu-vien` và `mau-dung-ghep/src/thu-vien` là **lối tắt** trỏ về thư mục này; lúc tạo dự án, `tao-du-an.sh` /
`tao-podcast.sh` / `tao-dung-ghep.sh` chép **bản thật** (`cp -RL`) vào `chuyen-dong/src/thu-vien/` — dự án cũ giữ nguyên bản lúc tạo, dự án mới
luôn có bản mới nhất. Sửa ở đây thì mọi dự án tạo sau đều đổi. Thành phần mới dùng chung thì đặt ở đây, chỉ import `react`, `remotion`, `./bien-thiet-ke`.
