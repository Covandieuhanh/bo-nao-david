---
name: dang-da-kenh
description: Quy trình trọn gói của David — từ MỘT tài nguyên (video quay, ghi âm, bài nói bộc phát; thường không kèm yêu cầu) Claude tự lọc theo hồ sơ David, quyết định có đáng làm và làm thành gì, hỏi David một lần ở phiếu lọc, dựng bằng skill dựng sẵn, soạn bài theo giọng David cho từng kênh, hẹn giờ đăng YouTube, trang Facebook, TikTok qua trình duyệt đã đăng nhập, rồi gom bình luận và đọc số liệu. Hai cổng duyệt: phiếu lọc trước khi dựng, bản cuối + bài đăng trước khi đăng. Dùng khi David gửi video/ghi âm mới, bỏ file vào Drive Video-goc, nói "có video mới", "đăng giúp", "đăng lên các kênh", "làm bài đăng", "lọc nội dung này", "/dang-da-kenh" — kể cả khi chỉ gửi file mà không nói gì.
---

# Đăng đa kênh — một lần nói → đủ bài cho mọi kênh

**Đọc trước:** `../../thoi-quen-lam-viec.md` · `../luat-chung.md`. File khác chỉ đọc ở đúng bước cần (cột cuối bảng quy trình).

**Vai trò:** nội dung là của David (nói tự do, có cảm xúc, không khuôn). Claude lo nhận diện, lọc, thẩm mỹ, nhịp,
phân phối, đăng và đo. Mọi bài có mục tiêu: kéo tương tác đúng nền tảng → chuyển hoá → người xem nhắn "gỡ".

## Mục tiêu
Một tài nguyên vào → (nếu đáng) video + bài đăng đúng kênh, đúng giờ, đúng định vị trainer; (nếu không đáng) không tốn thời gian dựng.

## Quy trình (8 bước, 2 cổng duyệt)
| # | Bước | Ai | Đọc / dùng |
|---|---|---|---|
| 0 | **Nhận tài nguyên** *(bước nhẹ)*: Drive `Video-goc` (`~/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/Video-goc/`) hoặc file gửi vào chat. Chép lời, đo độ dài, khung, chất lượng | Claude | khối 01 |
| 1 | **Lọc + nhận diện**: **đối chiếu kho 100 video** (ý khớp · ⚠️ lệch kho · ý kế tiếp nên quay), chấm 5 tiêu chí, lằn ranh, 7 kết luận, nhánh, trùng sổ; đề xuất sản phẩm → kênh → giờ, kiểu dẫn dắt theo tỉ lệ, loại dựng | Claude | khối 00 (mục 1b) · `dang-lam/kho-100-video.md` · `~/.claude/David.md` · `../ho-so/kenh.json` (lịch, tỉ lệ dẫn dắt) · `../nhan-dien.md` · sổ `~/Movies/_so-danh-muc/danh-muc.md` |
| 2 | **CỔNG 1 — phiếu lọc + mọi điểm cần chọn, một vòng** (`hoi-chuyen-gia`): kết luận, loại dựng, kênh và giờ, và mỗi điểm 2–3 gợi ý đề xuất đứng đầu: tiêu đề, chữ bìa. Câu chốt không hỏi (nguyên văn câu cuối của David, khối 08). Kết luận ⛔ / 👤 / 🗂 → dừng dựng, chỉ cập nhật sổ (👤: soạn câu chia sẻ Facebook cá nhân) | David duyệt | khối 00 |
| 3 | **Dựng** theo loại: `video-style-edit` (1 video / ghép vlog), `podcast-style-edit`. Chỉ render sau cổng 1; độ dài theo nội dung | Claude | skill dựng |
| 4 | **Soạn bài từng kênh** (chạy song song bước 3, xem dưới): YouTube (tiêu đề, mô tả, chương, thumbnail nếu ngang) · Reels / bài trang · TikTok caption · câu chia sẻ Facebook cá nhân · bình luận ghim "Vấn đề / Kết quả" · bài Mời: "nhắn mình một chữ 'gỡ'" + link nhắn tin trang · **kế hoạch clip ngắn** | Claude | khối 15 · `../ho-so/giong-van-david.md` · `cat-highlight-video` |
| 5 | **CỔNG 2 — bản cuối + chữ từng bài**: bản xem được trên điện thoại (nén < 30 MB nếu cần; bản gốc ở Drive `Video-xong/tap-<ten>/ban-dai|highlight/`, cách xếp ở ghi nhớ `video-chuyen-qua-drive`) + bảng bài đăng (kênh · giờ · chữ) + clip đã chọn. David duyệt từng bài | David duyệt | khối 17 |
| 6 | **Hẹn giờ đăng** đúng các bài đã duyệt qua trình duyệt (YouTube Studio · Business Suite · TikTok Studio), chụp xác nhận; Facebook cá nhân David tự bấm | Claude | khối 19 |
| 7 | **Sau 24 giờ** *(bước nhẹ)*: kiểm bài đã lên; gom bình luận / tin nhắn → "người xem đang hỏi gì", số "gỡ" (chỉ đọc, không tự trả lời) | Claude | khối 20 |
| 8 | **Sau 7 ngày** *(bước nhẹ)*: số liệu từng kênh → `so-lieu.md` + sổ danh mục → 1–3 đề xuất cho lần sau | Claude | khối 20, 16 |

Bước đánh dấu *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn theo `thoi-quen-lam-viec.md` mục 3.

## Làm song song khi render
Qua cổng 1 Claude đã có lời chép và các lựa chọn đã chốt, nên **bước 3 và bước 4 chạy cùng lúc**: render chạy nền thì soạn ngay,
không chờ David nhắc. Video dài để nguyên nên mốc theo lời không đổi.
Chờ bản cuối mới làm: ảnh thumbnail, kiểm khung hình và âm lượng.
**Clip ngắn:** Claude tự chọn ý theo bốn câu của `cat-highlight-video`, báo rõ đã chọn gì ở cổng 2 để David sửa;
chỉ dựng khi David đồng ý ở cổng 2, đăng sau video dài.

## Luật riêng của skill
- Chung (hỏi, không đăng khi chưa duyệt, tiết kiệm): `thoi-quen-lam-viec.md`. Video (nhạc, chữ nguyên văn, video dài không cắt, không tự render lại): `luat-chung.md`; hình của chính video: khối 14.
- Luật an toàn khi đăng (mật khẩu, cài đặt tài khoản, chỉ đăng bài đã duyệt): khối 19.
- **Sổ danh mục là nơi duy nhất ghi trạng thái** (lọc → dựng → chờ đăng → đã đăng + link).
- **Cảnh báo** khi lệch nhánh, thiếu bài Mời theo tỉ lệ, kho < 4 video quay sẵn, lịch trống.
- Phiếu lọc gọn một màn hình.

## Xong khi
1. Phiếu lọc gọn một màn hình, gửi trước khi dựng; kết luận ⛔ / 👤 / 🗂 thì không dựng.
2. Cổng 1 gộp mọi điểm cần chọn trong một vòng.
3. Không render trước cổng 1; bài đăng soạn trong lúc render chạy nền.
4. Bài đủ kênh theo kết luận, đúng giọng David, kiểu dẫn dắt khớp tỉ lệ.
5. Không gì được đăng trước cổng 2; mỗi lần hẹn giờ có ảnh chụp xác nhận.
6. Sổ danh mục và cột Trạng thái trong kho 100 video đúng ở từng bước.
7. Sau 24 giờ và 7 ngày có báo cáo hộp thư / số liệu + 1–3 đề xuất.

## Nhật ký
- 2026-11-10 · David chốt: mọi tài nguyên đối chiếu kho 100 video ở phiếu lọc (khớp ý / ⚠️ lệch kho / ý kế tiếp nên quay), dựng / đăng xong đổi trạng thái ý trong kho — để kênh dần đi đúng kế hoạch nội dung.
- 2026-11-05 · vai trò Claude; làm song song khi render.
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): Đọc trước chỉ 2 file, file khác theo bước; cổng 1 gộp mọi điểm cần chọn (tiêu đề, chữ bìa, câu chốt, kênh, giờ), cổng 2 chỉ duyệt bản cuối + chữ bài; clip ngắn Claude tự chọn ý theo bốn câu; đánh dấu bước nhẹ 0, 7, 8; lịch và tỉ lệ trỏ `kenh.json`; luật chung trỏ về nhà; thêm "Xong khi".
