# Khối 14-thumbnail: Thumbnail YouTube 1280×720 (chỉ video ngang đăng YouTube): mặt + ≤ 3 tầng chữ, số khổng lồ, nhãn series

**Dùng trong:** làm video, ghép vlog, podcast
**Đầu vào:** khung của CHÍNH video này / ảnh David gửi riêng cho video này
**Đầu ra:** phat-hanh/thumb-N.jpg (+ @160)
**Tham số hồ sơ:** chung: thumbnail.*
**Sửa khối này → chạy lại:** —

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/thumbnail.sh`
- `video-style-edit/assets/thumb-template/`

## Luật
- Chỉ khi video xuất **ngang** VÀ đăng YouTube (hỏi lúc đầu). Video dọc: chỉ ghi mốc khung bìa đề xuất.
- Mặt có cảm xúc rõ + 2–3 tầng chữ (≤ `thumbnail.max_chu`), dòng cam = từ khoá to nhất; `THUMB_NUM` số khổng lồ; `THUMB_BADGE` nhãn series/số tập; `THUMB_L3` dòng 3.
- Tiêu đề và thumbnail bổ sung, không lặp chữ. Soát bản @160 (cỡ điện thoại). Nguồn ảnh: **chỉ khung của chính video này** (hoặc ảnh David gửi riêng cho video này) — không lấy từ video/dự án khác (luat-chung 7, 2026-11-05). Podcast không mặt: khung cảnh minh hoạ của chính `video-final.mp4` (`<giây>` hoặc ảnh cắt từ nó).
- Lệnh: `zsh video-style-edit/scripts/thumbnail.sh "$P" <giây | cN@giây | ảnh> "<DÒNG 1>" "<DÒNG 2>" <số> [left|right] [vị trí] [phóng]`.

**Podcast (không mặt) — cách làm nền** (2026-11-05): thêm tạm 1–2 cảnh `illus` KHÔNG nhãn (cùng biểu tượng của cảnh đắt nhất) vào scenes.js → `node preview.mjs <id>@<giây>` → bỏ cảnh tạm khỏi scenes.js → dời hình sang trái ~430 px (dải phải lấp màu mép) → `thumbnail.sh … right`. Không dùng khung video-final (dính phụ đề, nhãn của cảnh trùng chữ thumbnail).
