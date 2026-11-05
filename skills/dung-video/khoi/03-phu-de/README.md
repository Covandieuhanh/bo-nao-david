# Khối 03-phu-de: Phụ đề: dài = hộp tối đầy câu; ngắn = 1–3 chữ to mỗi nhịp, màu theo nghĩa

**Dùng trong:** cả 4
**Đầu vào:** check/goc/words.srt + transcript.srt
**Đầu ra:** motion/src/captions.js (1 video, podcast) · SUBS trong edl.js (ghép)
**Tham số hồ sơ:** chung: phu_de.*
**Sửa khối này → chạy lại:** 17 (render lại lớp phu-de)

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/captions.py`
- `video-style-edit/assets/remotion-template/src/subStyle.js (một nguồn)`
- `video-style-edit/assets/remotion-template/src/components/Captions.jsx`

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

**3d. Phụ đề đầy đủ** — luôn có (người dùng chốt): toàn bộ lời nói, đúng từng chữ, chạy suốt video.
```bash
python3 -I $SKILL/scripts/captions.py "$P"          # check/goc/words.srt + transcript.srt → motion/src/captions.js (nháp)
```
Đọc lại TỪNG dòng trong `captions.js`, sửa tay:
- **Chính tả** lỗi Whisper (tên riêng, từ nghe nhầm như "tư giãn" → "thư giãn"). Giữ nguyên lời: không rút gọn, không
  diễn đạt lại, giữ cả "thì", "là", "cái".
- **Câu bị mất / câu bịa**: script bỏ câu kiểu "Hãy subscribe cho kênh…"; nếu chỗ đó người nói có nói thật (vd. "Xin chào"
  cuối video) thì đối chiếu `check/clean/transcript.srt` (lần chạy khác) + `loud.txt` và thêm tay.
- **Chỗ ngắt dòng**: không tách đôi từ ghép ("chia | sẻ", "giải | trình"); ngắt trước từ nối (thì, là, nhưng, mà…).
Kiểu phụ đề tự chọn theo độ dài (luat-chung 3): video dọc ≤ 90 s → 1–3 chữ to mỗi nhịp ngang ngực; còn lại hộp tối đầy câu.
Cả hai nằm trong dải 140 px ở **đáy vùng an toàn**. Lớp phủ (thẻ, chữ to, hook, tên) tự **thu nhỏ còn 78%** — người dùng
muốn thấy hình nhiều hơn — và **không bao giờ che mặt/người nói** (xem bước 5, `face_place.sh`): mặc định ngay trên dải
phụ đề, mặt nằm thấp thì dời lên đỉnh vùng an toàn hoặc chỗ trống khác. Component vẫn thiết kế trên dải gốc như cũ. Cảnh toàn màn hình phải chừa trống ~140 px cuối vùng an toàn. Render tự động (`phu-de` → `phu_de.mov`,
đè trên cùng ở bản cuối).

