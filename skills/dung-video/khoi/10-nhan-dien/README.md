# Khối 10-nhan-dien: Bộ nhận diện David + phong cách (màu, font, dấu kênh, khuôn tiêu đề); rút phong cách từ video mẫu

**Dùng trong:** cả 4
**Đầu vào:** brand.json, theme.js / brand.js, video mẫu (nếu có)
**Đầu ra:** token phong cách trong dự án
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** mọi khối hình (06, 07, 08, 12, 14) → 17

**File thật (code, một bản duy nhất):**
- `video-style-edit/assets/remotion-template/src/{brand.json,theme.js,fonts.js}`
- `video-style-edit/assets/montage-template/src/brand.js`
- `video-style-edit/references/style-analysis.md`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

### 4. Rút phong cách từ video mẫu

```bash
zsh $SKILL/scripts/analyze_video.sh "$P/ref/mau.<ext>" "$P/ref"
```
Xem kỹ contact sheet + các khung lớn của mẫu (nếu chỉ có ảnh chụp thì xem ảnh). Làm theo
`references/style-analysis.md` để viết `$P/style.md`: bảng màu (mã hex), kiểu chữ → font Google có tiếng Việt,
hình dạng thẻ, kiểu chuyển động, các loại cảnh xuất hiện, mật độ (bao nhiêu giây một hiệu ứng, tỉ lệ toàn màn hình).
Rồi áp vào code: `theme.js` (màu, font), `fonts.js` (import font; cài gói `@fontsource/<font>` nếu đổi font),
và chỉnh/viết thêm component khi mẫu có kiểu cảnh mà template chưa có. Mẫu ngang 16:9 mà video gốc dọc:
giữ tinh thần (màu, chữ, nhịp), bố cục thì theo khung dọc.

