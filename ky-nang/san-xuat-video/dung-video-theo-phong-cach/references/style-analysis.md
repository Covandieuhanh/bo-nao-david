# Đọc video mẫu thành token phong cách

Mục tiêu không phải sao chép từng khung hình của mẫu, mà rút ra **ngôn ngữ thiết kế** của nó để áp lên nội dung
của David. Một người xem hai video phải thấy "cùng một nhà sản xuất", dù nội dung khác hẳn.

**Chữ ký nhận diện không đổi** (`../../thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0): màu nhấn cam `C.accent`, hai font chính `HEAD` /
`BODY`, thành phần cố định. Từ mẫu chỉ lấy phần ngoài chữ ký: nền, màu phụ, hình dạng thẻ, kiểu hình, chuyển động, loại cảnh, mật độ,
font phụ cho một từ nhấn.

## Nhìn gì trong video mẫu

Xem `ref/contact.jpg` (24 khung trải đều) để nắm nhịp, rồi các `frame_XX.jpg` để đọc chi tiết.
Cần thì cắt thêm khung ở mốc cụ thể: `ffmpeg -ss <giây> -i ref/mau.* -frames:v 1 ref/x.jpg`.

| Hạng mục | Câu hỏi | Ghi vào |
|---|---|---|
| Màu | Nền thẻ/cảnh màu gì? Chữ trắng tinh hay ngà? Có gradient, phát sáng không? (màu nhấn giữ cam) | `C` trong chu-de.js (hex), trừ `accent` |
| Chữ | Đậm cỡ nào? In hoa? Có gạch chân/khung/nền sau chữ? Có font phụ cho từ nhấn không? | component Kinetic; font phụ `NHAN` (font chính giữ `HEAD`/`BODY`) |
| Thẻ | Bo góc nhiều/ít? Trong suốt, mờ kính, đặc? Có viền, bóng? Tiêu đề nhỏ màu nhấn (eyebrow) không? | CardShell |
| Chuyển động | Bật nảy (spring) hay trượt mượt? Nhanh (≤8 khung) hay chậm? Chữ hiện từng từ, từng dòng hay cả khối? Có đường kẻ tự vẽ, số đếm chạy không? | `pop`, `ease`, thời lượng vào/ra |
| Loại cảnh | Có cảnh toàn màn hình không? Biểu đồ, sơ đồ, dòng thời gian, danh sách tick, so sánh 2 cột, ảnh dồn dập? | chọn loại cảnh / viết component mới |
| Vị trí | Lớp phủ đặt cạnh mặt, dưới mặt hay giữa? (dù mẫu thế nào, KHÔNG che mặt người nói — `vi-tri-khuon-mat.sh` lo) | bố cục component; vị trí từng cảnh = vi-tri.js |
| Mật độ | Trung bình bao nhiêu giây có một hiệu ứng? Bao nhiêu % thời lượng là toàn màn hình? | nhịp trong canh.js |
| Âm thanh/nhịp cắt | Có nhạc nền, tiếng "whoosh"? Đặt ở đâu? | `thiet-ke-bo-cuc/am-thanh.md` (nhạc vẫn lấy kho kênh, khối 09) |

Transcript của mẫu (`ref/transcript.srt`) giúp thấy hiệu ứng được gắn vào loại câu nào (con số, khẳng định, liệt kê).

## Viết `style.md`

Ngắn, cụ thể, đủ để người khác dựng lại:
```
# Phong cách: <tên gợi nhớ>
Màu: nền #0D0D10 · thẻ rgba(24,24,28,.88) · nhấn #FF7A45 · chữ #F4F4F5 · phụ #A1A1AA
Chữ to: Barlow Condensed 800, in hoa, gạch chân màu nhấn tự vẽ
Chữ thường: Be Vietnam Pro 500–700
Thẻ: bo 36px, nền tối hơi trong, viền mảnh, eyebrow in hoa giãn chữ màu nhấn, dòng kết "→ ..." màu nhấn
Chuyển động: spring nảy nhẹ, chữ trồi lên từng từ, biểu đồ tự vẽ, số đếm chạy
Cảnh hay dùng: thẻ số liệu/biểu đồ, chữ to nhấn ý, (không/ít) toàn màn hình
Mật độ: ~1 hiệu ứng / 10–12 s, toàn màn hình ≈ 25% thời lượng
```

## Chọn font có tiếng Việt (font phụ cho từ nhấn)

Font phải có subset `vietnamese` trong `@fontsource` (kiểm tra: `ls node_modules/@fontsource/<font>/files | grep vietnamese`).
Ánh xạ kiểu chữ thường gặp:

| Kiểu thấy trong mẫu | Font gợi ý (fontsource) |
|---|---|
| Cô đặc đậm, kiểu tiêu đề thể thao/tin tức | barlow-condensed, oswald, saira-condensed |
| Grotesk hiện đại, rộng, kiểu Apple/startup | be-vietnam-pro, inter, manrope, plus-jakarta-sans |
| Tròn, thân thiện | nunito, quicksand, baloo-2 |
| Có chân, sang trọng/báo chí | playfair-display, lora, noto-serif |
| Viết tay, vui | dancing-script, pacifico (chỉ cho điểm nhấn ngắn) |
| Đơn cách, kiểu code/kỹ thuật | jetbrains-mono, roboto-mono |

Cài: `cd motion && npm install @fontsource/<font>` → import `vietnamese-<weight>.css` và `<weight>.css` trong `phong-chu.js`,
thêm dòng vào `FONT_CHECKS`; dùng cho từ nhấn, không đổi `HEAD`/`BODY`. Luôn thử chữ có dấu chồng (Ở, Ữ, Ặ, Ễ) và dấu dưới (ạ, ợ, ụ) khi chụp kiểm tra.

## Khi mẫu khác hẳn template

Template chỉ là điểm xuất phát. Nếu mẫu dùng thứ template không có (ví dụ phụ đề chạy theo từng chữ, khung ảnh polaroid,
nhãn dán emoji, hiệu ứng zoom vào mặt, chia đôi màn hình), viết component mới trong `thanh-phan/` (hoặc cảnh tự vẽ `ve`, khối 07), đăng ký trong
`goc.jsx` (TYPES).
Hiệu ứng tác động lên chính video gốc (zoom mặt, cắt nhịp, đổi màu) không làm bằng clip phủ được — làm trong
`xem-truoc-ban-dung.py` bằng filter ffmpeg (ví dụ `zoompan`/`crop` theo đoạn).
