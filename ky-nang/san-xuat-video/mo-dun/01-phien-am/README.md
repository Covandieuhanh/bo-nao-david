# Khối 01-phien-am: Chép lời (Whisper) + hiểu video

**Dùng trong:** cả 4
**Đầu vào:** file video/tiếng
**Đầu ra:** check/goc/{transcript.srt, words.srt, contact.jpg, frame_XX.jpg}
**Tham số hồ sơ:** —
**Sửa khối này → chạy lại:** 02 (làm sạch đổi mốc → chép lại trên bản sạch), 03, 13

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/check_env.sh`
- `dung-video-theo-phong-cach/scripts/analyze_video.sh`
- `dung-podcast/scripts/transcribe.sh`

## Cách làm

### Kiểm tra môi trường

```bash
zsh $SKILL/scripts/check_env.sh
```
Thiếu gì thì xử lý theo lệnh nó in ra. Homebrew cần mật khẩu máy → đưa lệnh cho người dùng tự chạy (không bao giờ
tự nhập mật khẩu dù được cho). Mô hình Whisper 1,5 GB: hỏi trước khi tải lần đầu.

### Hiểu video (bản sạch, đã đổi khung nếu có)
```bash
zsh $SKILL/scripts/analyze_video.sh "$P/davinci/media/video_goc.mp4" "$P/check/goc"
```
Đọc `transcript.srt` (Whisper hay nghe nhầm tên riêng, thuật ngữ — tự sửa khi dùng làm chữ trên màn hình). Whisper bịa câu ở đoạn
không lời → bỏ (quy-tac-chung mục 1).
**Tên riêng / thuật ngữ người nói giới thiệu hay "bật mí" là nội dung chính → PHẢI hiện đúng tên đó** đúng lúc nói;
không chắc chính tả thì dùng cách Whisper nghe được (khớp mọi lần xuất hiện) và nêu trong báo cáo để người dùng sửa —
không đổi thành cụm chung chung hay câu tự nghĩ ra ("Haruku" thành "ĐI BỘ MỖI NGÀY" → minh hoạ sai ý).
Xem `contact.jpg` và vài `frame_XX.jpg` để biết:
mặt người nói nằm ở đâu, khoảng trống nào còn dùng được, nền sáng hay tối (ảnh hưởng độ dễ đọc của chữ).
Vị trí lớp phủ không cố định: khối 05 tự đặt từng cảnh tránh mặt (`face_place.sh`), không cần chỉnh `SAFE.overlayTop`.

