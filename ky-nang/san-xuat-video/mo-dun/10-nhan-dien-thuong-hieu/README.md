---
description: "Khối 10 bộ nhận diện David trên video: dấu góc, thanh thời gian, màu, font."
---

# Khối 10-nhan-dien-thuong-hieu: Bộ nhận diện David + phong cách; rút phong cách từ video mẫu

**Dùng trong:** cả 4
**Đầu vào:** thuong-hieu.json, chu-de.js / thuong-hieu.js, video mẫu (nếu có)
**Đầu ra:** token phong cách trong dự án
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** mọi khối hình (06, 07, 08, 12, 14) → 17

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/assets/khuon-remotion/src/{thuong-hieu.json,chu-de.js,phong-chu.js}`
- `dung-video-theo-phong-cach/assets/khuon-dung-ghep/src/thuong-hieu.js`
- `dung-video-theo-phong-cach/references/phan-tich-phong-cach.md`

## Luật
- Bộ nhận diện (chữ ký + thành phần cố định): `thu-vien-tai-nguyen/nhan-dien-chung.md`. Không có mẫu → phong cách mặc định của template.
- **Rút phong cách từ mẫu không đụng chữ ký:** màu nhấn cam, hai font chính, thành phần cố định giữ nguyên. Ngoài chữ ký (nền, màu phụ,
  hình dạng thẻ, kiểu hình, chuyển động, loại cảnh, mật độ) được lấy theo mẫu.

## Cách làm — rút phong cách từ video mẫu
```bash
zsh $SKILL/scripts/phan-tich-video.sh "$P/tai-lieu-tham-khao/mau.<ext>" "$P/tai-lieu-tham-khao"
```
Xem kỹ contact sheet + các khung lớn của mẫu (nếu chỉ có ảnh chụp thì xem ảnh). Làm theo `references/phan-tich-phong-cach.md` để viết
`$P/phong-cach.md`: nền, màu phụ (mã hex), hình dạng thẻ, kiểu chuyển động, các loại cảnh xuất hiện, mật độ. Rồi áp vào code: `chu-de.js`
(màu ngoài màu nhấn), và chỉnh/viết thêm component khi mẫu có kiểu cảnh mà template chưa có. Font chữ nhấn phụ có tiếng Việt:
`phong-chu.js` (cài `@fontsource/<font>`). Mẫu ngang 16:9 mà video gốc dọc: giữ tinh thần (nền, nhịp), bố cục theo khung dọc.
