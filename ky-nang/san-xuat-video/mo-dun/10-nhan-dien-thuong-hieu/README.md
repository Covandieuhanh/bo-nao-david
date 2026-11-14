# Khối 10-nhan-dien-thuong-hieu: Bộ nhận diện David + phong cách; rút phong cách từ video mẫu

**Dùng trong:** cả 4
**Đầu vào:** brand.json, theme.js / brand.js, video mẫu (nếu có)
**Đầu ra:** token phong cách trong dự án
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** mọi khối hình (06, 07, 08, 12, 14) → 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/remotion-template/src/{brand.json,theme.js,fonts.js}`
- `dung-video-theo-phong-cach/assets/montage-template/src/brand.js`
- `dung-video-theo-phong-cach/references/style-analysis.md`

## Luật
- Bộ nhận diện (chữ ký + thành phần cố định): `thu-vien-tai-nguyen/nhan-dien-chung.md`. Không có mẫu → phong cách mặc định của template.
- **Rút phong cách từ mẫu không đụng chữ ký:** màu nhấn cam, hai font chính, thành phần cố định giữ nguyên. Ngoài chữ ký (nền, màu phụ,
  hình dạng thẻ, kiểu hình, chuyển động, loại cảnh, mật độ) được lấy theo mẫu.

## Cách làm — rút phong cách từ video mẫu
```bash
zsh $SKILL/scripts/analyze_video.sh "$P/ref/mau.<ext>" "$P/ref"
```
Xem kỹ contact sheet + các khung lớn của mẫu (nếu chỉ có ảnh chụp thì xem ảnh). Làm theo `references/style-analysis.md` để viết
`$P/style.md`: nền, màu phụ (mã hex), hình dạng thẻ, kiểu chuyển động, các loại cảnh xuất hiện, mật độ. Rồi áp vào code: `theme.js`
(màu ngoài màu nhấn), và chỉnh/viết thêm component khi mẫu có kiểu cảnh mà template chưa có. Font chữ nhấn phụ có tiếng Việt:
`fonts.js` (cài `@fontsource/<font>`). Mẫu ngang 16:9 mà video gốc dọc: giữ tinh thần (nền, nhịp), bố cục theo khung dọc.
