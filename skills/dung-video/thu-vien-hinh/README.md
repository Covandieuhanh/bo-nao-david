# Thư viện hình dùng chung (một bản duy nhất cho cả 4 loại video)

| File | Việc | Khối |
|---|---|---|
| `tokens.js` | màu, font, hàm ease của kênh | 10 |
| `brand.json` | tên kênh, tiếng ký hiệu, mức nhạc, độ dài thẻ cuối | 10 · 09 |
| `subStyle.js` | phụ đề dài (SUB) + ngắn cụm 5–8 chữ cỡ 58 (ShortLine, chunks) + tô màu theo nghĩa | 03 |
| `cta.js` | câu màn chốt dự phòng + biểu tượng + mốc tick | 08 |
| `Icons.jsx` | biểu tượng nét vẽ dần (Icon, Pictogram) | 07 |
| `YtEnd.jsx` | màn kết YouTube 15–20 s | 08 |
| `Illus.jsx` | cảnh minh hoạ toàn màn hình (một kiểu của bố cục tự cân) | 07 |
| `Diagram.jsx` | sơ đồ nói thay lời: tang, vong, moc, cot, luoi, tu-thanh, xay-tang, doi-trang-thai, chuyen-giao, anh | 07 |
| `EndCardBody.jsx` | ruột thẻ cuối (gạch nhận diện, BẢN ĐẦY ĐỦ TRÊN KÊNH…, tên, người nói, lịch phát; không logo nền tảng) | 08 |
| `nhan-dien.js` | **bộ nhận diện chung**: vùng an toàn ngang/dọc, vị trí dấu góc, thanh thời gian, đáy phụ đề (`khung(W, H)`) — xem `nhan-dien-chung.md` | 10 |
| `DauGoc.jsx` | dấu góc ● DAVID │ chủ đề | 10 |
| `ThanhThoiGian.jsx` | thanh thời gian ở đáy: đã chạy · thanh · còn m:ss | 10 |
| `chuyen-dong.js` | easing theo vai, vào/ra mờ nhoè, chữ hiện từng từ (3 kiểu), lò xo theo ζ, thời gian đọc | 07 |
| `ChuHien.jsx` | một dòng chữ hiện từng từ theo kiểu của `chuyen-dong.js`, không dịch chỗ | 07 |
| `mach.js` | **mạch hình**: một hình kể chuyện vẽ tiếp qua nhiều cảnh tự vẽ (`buoc`, `tu_buoc`, `moc_buoc`) + nét vẽ dần `net()` | 07 |

Cách nối: `remotion-template/src/lib` và `montage-template/src/lib` là **lối tắt** trỏ về thư mục này; lúc tạo dự án, `new_project.sh` /
`new_podcast.sh` / `new_montage.sh` chép **bản thật** (`cp -RL`) vào `motion/src/lib/` — dự án cũ giữ nguyên bản lúc tạo, dự án mới
luôn có bản mới nhất. Sửa ở đây → mọi dự án tạo sau đều đổi. Thành phần mới dùng chung → đặt ở đây, chỉ import `react`, `remotion`, `./tokens`.
