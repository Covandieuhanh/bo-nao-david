---
description: "Khối 01 chép lời bằng Whisper và hiểu video."
---

# Khối 01-phien-am: Chép lời (Whisper) + hiểu video

**Dùng trong:** cả 4
**Đầu vào:** file video/tiếng
**Đầu ra:** kiem-tra/goc/{ban-chep-loi.srt, moc-tung-tu.srt, bang-khung-hinh.jpg, khung-XX.jpg}
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** 02 (làm sạch đổi mốc → chép lại trên bản sạch), 03, 13

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/kiem-moi-truong.sh`
- `dung-video-theo-phong-cach/scripts/phan-tich-video.sh`
- `dung-podcast/scripts/phien-am.sh`

## Cách làm

### Kiểm tra môi trường

```bash
zsh $SKILL/scripts/kiem-moi-truong.sh
```
Thiếu gì thì xử lý theo lệnh nó in ra. Homebrew cần mật khẩu máy → đưa lệnh cho người dùng tự chạy (không bao giờ
tự nhập mật khẩu dù được cho). Mô hình Whisper 1,5 GB: hỏi trước khi tải lần đầu.

### Hiểu video (bản sạch, đã đổi khung nếu có)
```bash
zsh $SKILL/scripts/phan-tich-video.sh "$P/tu-lieu/video-goc.mp4" "$P/kiem-tra/goc"
```
Đọc `ban-chep-loi.srt` (Whisper hay nghe nhầm tên riêng, thuật ngữ — tự sửa khi dùng làm chữ trên màn hình). Whisper bịa câu ở đoạn
không lời → bỏ (quy-tac-chung mục 1).
**Nơi ồn (quán cà phê, ngoài trời), chép lại một đoạn để kiểm** (19/11/2026): chép theo khúc ≤ 20 s, `-mc 0` (không ngữ cảnh), **bản gốc
trước, không lọc**; dính câu ảo "Hãy subscribe cho kênh…" mới thử bản lọc dải tiếng (lọc trước làm ảo giác nhiều hơn). Bản dài chép một
lượt có thể lặp một câu hàng chục lần ("Mình nó bị vướng quá nhiều" × 40) → không dùng làm mốc. Mốc từng từ (`-ml 1`) lệch 0,5–2 s:
dùng để tìm câu, không dùng làm điểm cắt (khối 02 `diem-ngat.py`) hay mốc phụ đề (khối 03 `soat-khop-tieng.py`).
**Tên riêng / thuật ngữ người nói giới thiệu hay "bật mí" là nội dung chính → PHẢI hiện đúng tên đó** đúng lúc nói;
không chắc chính tả thì dùng cách Whisper nghe được (khớp mọi lần xuất hiện) và nêu trong báo cáo để người dùng sửa —
không đổi thành cụm chung chung hay câu tự nghĩ ra ("Haruku" thành "ĐI BỘ MỖI NGÀY" → minh hoạ sai ý).
Xem `bang-khung-hinh.jpg` và vài `khung-XX.jpg` để biết:
mặt người nói nằm ở đâu, khoảng trống nào còn dùng được, nền sáng hay tối (ảnh hưởng độ dễ đọc của chữ).
Vị trí lớp phủ không cố định: khối 05 tự đặt từng cảnh tránh mặt (`vi-tri-khuon-mat.sh`), không cần chỉnh `SAFE.overlayTop`.

