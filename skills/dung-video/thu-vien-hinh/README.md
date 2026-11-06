# Thư viện hình dùng chung (một bản duy nhất cho cả 4 loại video)

| File | Việc | Khối |
|---|---|---|
| `tokens.js` | màu, font, hàm ease của kênh | 10 |
| `brand.json` | tên kênh, tiếng ký hiệu, mức nhạc, độ dài thẻ cuối | 10 · 09 |
| `subStyle.js` | phụ đề dài (SUB) + ngắn 1–3 chữ (ShortLine, chunks) + tô màu theo nghĩa | 03 |
| `cta.js` | câu màn chốt dự phòng + biểu tượng + mốc tick | 08 |
| `Icons.jsx` | biểu tượng nét vẽ dần (Icon, Pictogram) | 07 |
| `YtEnd.jsx` | màn kết YouTube 15–20 s | 08 |
| `Illus.jsx` | cảnh minh hoạ toàn màn hình (2 trạng thái) | 07 |
| `Diagram.jsx` | sơ đồ nói thay lời: tang, vong, moc, cot, luoi, tu-thanh, xay-tang, doi-trang-thai, chuyen-giao, anh | 07 |
| `EndCardBody.jsx` | ruột thẻ cuối (nút phát / gạch, XEM BẢN ĐẦY ĐỦ, tên, người nói, lịch phát) | 08 |

Cách nối: `remotion-template/src/lib` và `montage-template/src/lib` là **lối tắt** trỏ về thư mục này; lúc tạo dự án, `new_project.sh` /
`new_podcast.sh` / `new_montage.sh` chép **bản thật** (`cp -RL`) vào `motion/src/lib/` — dự án cũ giữ nguyên bản lúc tạo, dự án mới
luôn có bản mới nhất. Sửa ở đây → mọi dự án tạo sau đều đổi. Thành phần mới dùng chung → đặt ở đây, chỉ import `react`, `remotion`, `./tokens`.
