# Khối 06-mo-dau: Mở đầu 0–3 s: thẻ tít / hook, đoạn ghép mở vlog, teaser podcast dài

**Dùng trong:** cả 4
**Đầu vào:** lời + bản đồ ý
**Đầu ra:** cảnh hook (scenes.js) · pow 0–2,5 s (edl.js) · plan.json intro · teaser.py
**Tham số hồ sơ:** lam-video: the_tit_mo_s, ghep-vlog: mo_dau.*, chung: youtube.teaser_*
**Sửa khối này → chạy lại:** 05, 17

**File thật (code, một bản duy nhất):**
- `video-style-edit/assets/remotion-template/src/components/Overlays.jsx (Hook)`
- `video-style-edit/scripts/teaser.py`
- `video-style-edit/scripts/vlog_edl.py (intro)`

## Luật
- **David chốt 2026-11-07: KHÔNG làm thẻ tít mở đầu mặc định** — tít tự rút ý có thể chưa đúng điều David muốn truyền tải. Chỉ làm khi David
  yêu cầu, và chữ phải là nguyên văn lời David. (Lỗi kèm: `hook` 2 dòng ở khung ngang bị cắt dòng 2 — sửa Hook trước khi dùng lại cho khung ngang.)
- 0–3 s nói ngay video về cái gì / đang đặt cược gì (nguyen-tac 1). Thẻ tít là **ngoại lệ duy nhất** của 2 trạng thái — được đè lên
  người 0–2,5 s (khối 05 vẫn chuyển toàn màn hình nếu che mặt/thân trên).
- Làm video: cảnh `hook` 0 → ~3 s, ý chính cả video, trích lời (scene-design.md "Mở đầu 3 giây").
- Highlight: thẻ tít ≤ 8 chữ viết như tít báo đúng ý (`"tit"` trong phuong-an.json → `hl_edl.py` tự đặt pow 0–2,5 s); khung 0,3 s = ảnh bìa.
- Vlog: đoạn ghép cảnh đắt nhất (2 phách/cảnh) hoặc câu nêu nhiệm vụ / tiền cược lên đầu — multi-clip.md 2d (kiểu 1/2/3).
- Video > 10 phút đăng YouTube: teaser 15–25 s câu đắt nhất sau render (`teaser.py`, khối 15 chạy lại chương).
