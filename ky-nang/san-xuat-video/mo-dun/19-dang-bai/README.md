---
description: "Khối 19 đăng bài / hẹn giờ lên YouTube, trang Facebook, TikTok qua trình duyệt."
---

# Khối 19-dang-bai: Đăng / hẹn giờ lên YouTube, trang Facebook, TikTok qua trình duyệt

**Dùng trong:** skill `phan-phoi-da-kenh` bước 7 · **Đầu vào:** bản cuối + bài đăng trên trang xem kết quả, David đã nói "đăng" · `ho-so-thuong-hieu/kenh.json` · `ho-so-thuong-hieu/giong-thuong-hieu-david.md`
**Đầu ra:** bài đã hẹn giờ (hoặc đăng) + ảnh chụp xác nhận · dòng "chờ đăng / đã đăng" trong sổ danh mục
**Trạng thái:** các bước dưới lấy từ giao diện thật lúc đọc trang, chưa được kiểm bằng một lần bấm đăng thật. Ở lần đăng thật đầu tiên trên mỗi
nền tảng, Claude làm chậm, chụp từng bước và sửa README này theo giao diện thật.

## Luật an toàn (không ngoại lệ)
- **Chỉ đăng khi David nói "đăng"**, đúng bản trên trang xem kết quả (video, chữ, kênh, giờ). Nếu đổi bất cứ điều gì sau khi duyệt thì Claude hỏi lại.
  Chữ "đăng" nói trước khi có bản cuối (ví dụ "xong thì đăng") chưa được tính: Claude bàn giao bản cuối kèm gói đăng, không hỏi; chờ David nói "đăng" (`quy-trinh.md` mục 1, Đ2).
- **Không bao giờ nhập mật khẩu**, không đổi cài đặt tài khoản (tên, ảnh, bio, quyền) khi David chưa duyệt riêng việc đó.
- **Ưu tiên hẹn giờ** (thứ Ba / thứ Sáu 20:00 giờ Việt Nam) bằng chức năng có sẵn của nền tảng để David huỷ được trước giờ bài lên; thiết bị không cần bật lúc bài lên.
- **Facebook cá nhân:** Claude soạn câu, **David tự bấm chia sẻ** (tự động hoá tài khoản cá nhân dễ bị khoá).
- Trước lần bấm cuối ("Lên lịch" / "Đăng" / "Chia sẻ"): chụp màn hình phần xem trước, đối chiếu với bản đã duyệt; sau đó chụp màn hình xác nhận.
- Khi gặp mã xác minh, CAPTCHA, yêu cầu đăng nhập lại, cảnh báo bảo mật, Claude **dừng, gọi David** (không tự vượt qua).

## Thứ tự hẹn giờ một đợt (video dài + clip)
1. YouTube video dài trước, lấy link, điền vào các bài còn lại. 2. Bài trang Facebook, Reels, Shorts. 3. TikTok.
- **TikTok chỉ hẹn được trong 10 ngày:** với clip xa hơn, Claude đặt việc tự chạy (scheduled task) khi ngày đăng đã nằm trong giới hạn đó; việc này cần thiết bị bật và ứng dụng Claude mở.
- **Bình luận ghim không hẹn được trước:** Claude đặt việc tự chạy ngay sau giờ bài lên, đăng đúng chữ đã duyệt.
- **Link trong mô tả TikTok không bấm được:** ghi tên kênh, không dán link. Shorts gắn "Video liên quan" về video dài.
- Gói đăng: chữ từng bài nằm chung một file; David nói "đăng" một lần cho cả đợt (Đ2). Mẫu: [mau-ke-hoach-dang.md](mau-ke-hoach-dang.md) (đợt Đi trainer).

## Trình duyệt
- **Đọc / soạn / kiểm** (không cần tải file): trình duyệt riêng trong app (`mcp__Claude_Browser__*`) — David đã đăng nhập 3 nền tảng.
- **Tải video lên** cần lệnh chọn file thì **Playwright CLI + Chrome hồ sơ riêng** (trình duyệt trong app không chọn file được; YouTube chặn
  cách đưa file qua máy chủ cục bộ; Claude in Chrome giới hạn 10 MB/lần):
  ```bash
  playwright-cli -s=mxh open <url> --browser=chrome --headed --persistent --profile="$HOME/.cache/david-mxh-chrome"
  playwright-cli -s=mxh snapshot            # lấy ref của ô chọn file / nút
  playwright-cli -s=mxh upload "<đường dẫn video-hoan-chinh.mp4>"
  ```
  David đã đăng nhập cả 3 nền tảng trong hồ sơ này (`~/.cache/david-mxh-chrome`). Khi hết phiên đăng nhập, Claude nhờ David đăng nhập lại, không tự nhập.

## YouTube (Studio) — bản dài + Shorts
**Ảnh bìa tuỳ chỉnh cần kênh đã xác minh số điện thoại** (chưa xác minh thì Studio hiện hộp thoại "Xác minh"). David tự xác minh, Claude không làm thay.
1. `https://studio.youtube.com/channel/<id>/videos/upload?d=ud` → ô chọn file → `upload` video.
2. **Chi tiết:** Tiêu đề (tối đa 100 ký tự, theo phat-hanh.md) · Mô tả (tóm ý + "Vấn đề"/"Kết quả" + chương + link nhắn tin trang nếu bài Mời) ·
   Hình thu nhỏ (anh-thu-nho-1.jpg; chỉ video ngang) · "Không, nội dung này không dành cho trẻ em" · Thẻ / ngôn ngữ: Tiếng Việt.
3. **Thành phần video:** màn hình kết thúc (nếu có `ytEnd`: 2 video + nút đăng ký) · thẻ.
4. **Chế độ hiển thị → Lên lịch** → ngày + giờ (múi giờ Việt Nam, 20:00) → **Lên lịch** (cú bấm cuối).
5. Sau khi hẹn: ghim bình luận "Vấn đề / Kết quả" (Studio thì Bình luận) khi video đã lên, hoặc Claude nhắc David làm.
Shorts: video dọc tối đa 3 phút, theo cùng quy trình trên; tiêu đề ngắn + #Shorts không bắt buộc.

## Trang Facebook (Meta Business Suite) — Reels + bài viết
- **Reels:** `https://business.facebook.com/latest/reels_composer/?asset_id=<page_id>` → "Thêm video" → `upload` → **Mô tả** (caption
  theo giọng David + hashtag 2–3) → **Tiếp** (Chỉnh sửa: ảnh bìa = mốc khung bìa đề xuất) → **Tiếp** (Chia sẻ) → "Lên lịch" → ngày giờ → **Lên lịch**.
- **Bài viết chữ / ảnh:** Business Suite → Nội dung → Tạo bài viết → trang "<tên trang>" → nội dung → "Lên lịch".
- Bài **Mời**: kiểm tra trang có nút "Gửi tin nhắn" (Messenger) — link `kenh.fanpage.link_nhan_tin`.

## TikTok (TikTok Studio) — clip dọc
1. `https://www.tiktok.com/tiktokstudio/upload?from=upload` → "Chọn video" → `upload` (tối đa 30 GB / 60 phút).
2. **Mô tả** (caption + hashtag) · **Ảnh bìa** (chọn khung theo mốc đề xuất) · Ai có thể xem: Mọi người · cho phép bình luận.
3. **Thời điểm đăng → Lên lịch** (TikTok cho hẹn ít nhất 15 phút, tối đa 10 ngày) → ngày giờ → **Lên lịch** (cú bấm cuối).
4. Lưu ý: TikTok chặn tự động hoá khá nghiêm ngặt; nếu hiện kiểm tra bot hoặc hạn chế thì Claude dừng, nhờ David bấm.

## Facebook cá nhân
Claude không đăng tự động. Sau khi bài trên trang đã lên, Claude gửi David câu chia sẻ (1–2 câu, giọng văn gần gũi) kèm link bài trang để David bấm "Chia sẻ".
