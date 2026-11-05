---
name: dang-da-kenh
description: Quy trình trọn gói của David — từ MỘT tài nguyên David đưa (video quay, file ghi âm, bài nói bộc phát; không kèm yêu cầu) Claude tự lọc theo hồ sơ định hướng (~/.claude/David.md), quyết định có đáng làm không và làm thành gì, hỏi lại David, dựng video bằng các skill dựng sẵn, soạn bài theo giọng David cho từng kênh, rồi hẹn giờ đăng lên YouTube, trang Facebook, TikTok (Facebook cá nhân David tự bấm chia sẻ) qua trình duyệt đã đăng nhập; sau đó gom bình luận/tin nhắn và đọc số liệu. Hai cổng duyệt: phiếu lọc trước khi dựng, bản cuối + bài đăng trước khi đăng. Dùng khi David gửi video/ghi âm mới, bỏ file vào Drive Video-goc, nói "có video mới", "đăng giúp", "đăng lên các kênh", "làm bài đăng", "lọc nội dung này", "/dang-da-kenh" — kể cả khi David chỉ gửi file mà không nói gì.
---

# Đăng đa kênh — một lần nói → đủ bài cho mọi kênh

**Vai trò (David chốt 05/11/2026):** nội dung là của David (nói tự do, có cảm xúc, không khuôn). Claude lo phần nhận diện, lọc, thẩm mỹ,
nhịp, phân phối, đăng và đo. Mọi bài phải có mục tiêu: kéo tương tác trên đúng nền tảng → chuyển hoá → người xem nhắn "gỡ".

**Đọc trước:** `~/.claude/David.md` (hồ sơ) · `../khoi/00-loc-noi-dung` (bộ lọc) · `../ho-so/kenh.json` (kênh, lịch, dẫn dắt) ·
`../ho-so/giong-van-david.md` (giọng văn) · `../luat-chung.md` · sổ `~/Movies/_so-danh-muc/danh-muc.md`.

## Mục tiêu
Một tài nguyên vào → (nếu đáng) video + bài đăng đúng kênh, đúng giờ, đúng định vị trainer; (nếu không đáng) không tốn thời gian dựng.

## Làm song song khi render (David chốt 05/11/2026)
Qua cổng 1 là Claude đã đọc hết lời, nên **bước 3 (dựng) và bước 4 (soạn bài) chạy cùng lúc**: lệnh render chạy nền thì bắt tay soạn ngay, không chờ render xong,
không chờ David nhắc. Soạn gồm: tiêu đề, mô tả, bài viết từng kênh, bình luận ghim, chữ thumbnail, lịch đăng, **kế hoạch trích clip ngắn** (mốc từ–đến trên bản gốc,
kiểu clip, chú thích). Mọi thứ xoay quanh lời đã chép, và video dài để nguyên nên mốc không đổi.
Chờ bản cuối mới làm: ảnh thumbnail, kiểm tra khung hình và âm lượng. Clip chỉ là kế hoạch: dựng khi David đồng ý ở cổng 2, đăng sau video dài. Claude chỉ đọc lời, chưa nghe giọng, nên mốc clip là đề xuất để David chốt.

## Quy trình (8 bước, 2 cổng duyệt)
| # | Bước | Ai | Khối / skill |
|---|---|---|---|
| 0 | **Nhận tài nguyên**: Drive `Video-goc` (`~/Library/CloudStorage/GoogleDrive-…/Drive của tôi/Video-goc/`) hoặc file gửi vào chat. David KHÔNG cần kèm yêu cầu. Chép lời, đo độ dài, khung, chất lượng | Claude | 01 |
| 1 | **Lọc + nhận diện**: chấm 5 tiêu chí theo hồ sơ, lằn ranh, 7 kết luận, nhánh, trùng/lấp kho, đề xuất sản phẩm → kênh → giờ (thứ Ba / thứ Sáu 20:00 VN), kiểu dẫn dắt theo tỉ lệ 4·4·2, loại dựng (`../nhan-dien.md`) | Claude | 00 |
| 2 | **CỔNG 1 — phiếu lọc** gửi David + câu hỏi chỉ David quyết được (mỗi câu có đề xuất "đồng ý" được — `hoi-chuyen-gia`, một vòng). Kết luận ⛔ / 👤 / 🗂 → dừng dựng, chỉ cập nhật sổ (👤: soạn câu chia sẻ Facebook cá nhân) | David duyệt | 00 |
| 3 | **Dựng**: skill dựng theo loại — `video-style-edit` (1 video / ghép vlog), `podcast-style-edit`, `cat-highlight-video` (highlight Reels/TikTok). Chỉ render sau cổng 1; độ dài theo nội dung | Claude | skill dựng |
| 4 | **Soạn bài từng kênh** theo giọng David: YouTube (tiêu đề, mô tả, chương, thumbnail nếu ngang) · Reels / bài viết trang · TikTok caption · câu chia sẻ Facebook cá nhân · bình luận ghim "Vấn đề / Kết quả" · bài Mời: "nhắn mình một chữ 'gỡ'" + link nhắn tin trang | Claude | 15, giong-van |
| 5 | **CỔNG 2 — bản cuối + bài đăng**: gửi bản xem được trên điện thoại (nén < 30 MB nếu cần; bản gốc ở Drive `Video-xong`) + bảng bài đăng (kênh · giờ · chữ). David duyệt từng bài | David duyệt | 17 |
| 6 | **Hẹn giờ đăng** đúng các bài đã duyệt qua trình duyệt (YouTube Studio · Business Suite · TikTok Studio); Facebook cá nhân David tự bấm | Claude | 19 |
| 7 | **Sau 24 giờ**: kiểm bài đã lên; gom bình luận / tin nhắn → "người xem đang hỏi gì", số "gỡ" (chỉ đọc, không tự trả lời) | Claude | 20 |
| 8 | **Sau 7 ngày**: số liệu từng kênh → `so-lieu.md` + sổ danh mục → 1–3 đề xuất cho lần sau | Claude | 20, 16 |

## Thực thi (checklist mỗi tài nguyên)
- [ ] Chép lời xong · phiếu lọc gửi David (cổng 1) · ghi dòng "lọc" vào sổ
- [ ] David duyệt phiếu → dựng (không render trước cổng 1; không tự render lại sau góp ý nhỏ)
- [ ] Ngay khi render chạy nền: bài đăng soạn đủ kênh theo kết luận + kế hoạch trích clip · kiểu dẫn dắt khớp tỉ lệ 4·4·2 trong sổ
- [ ] Cổng 2: David duyệt bản cuối + từng bài
- [ ] Hẹn giờ xong ở từng nền tảng (ảnh chụp xác nhận) · sổ "chờ đăng"
- [ ] 24 giờ: "đã đăng" + link · gom hộp thư
- [ ] 7 ngày: số liệu + đề xuất

## Luật
- **Tự hỏi khi cần** (skill `hoi-chuyen-gia`, 6 tín hiệu) — cả giữa chừng; chuyện nhỏ có mặc định rõ thì tự làm và ghi một dòng.
- **Không đăng bất cứ gì chưa qua cổng 2.** Không nhập mật khẩu, không đổi cài đặt tài khoản (tên, bio, ảnh) khi David chưa duyệt riêng.
- **Chỉ hình của chính tài nguyên** (thumbnail, ảnh bìa) · không ghi số tập / ngày lên video · nhạc theo tuyến nội dung.
- **Tiết kiệm thời gian David** (điều David kiêng nhất): phiếu lọc gọn một màn hình; câu hỏi gộp một lần; không render khi chưa cần.
- Sổ danh mục là nơi duy nhất ghi trạng thái; cảnh báo lệch nhánh, thiếu bài Mời, kho < 4 video, lịch trống.
