---
name: dang-da-kenh
description: Quy trình trọn gói của David — từ MỘT tài nguyên (video quay, ghi âm, bài nói bộc phát; thường không kèm yêu cầu) Claude tự lọc theo hồ sơ David, quyết định có đáng làm và làm thành gì, rồi làm một mạch không cổng duyệt: dựng bản dài + clip ngắn, soạn bài theo giọng David cho từng kênh, giao lên Drive và trang xem kết quả (localhost:8765); góp ý thì render lại toàn bộ; khi David nói "đăng" thì hẹn giờ YouTube, trang Facebook, TikTok qua trình duyệt đã đăng nhập, rồi gom bình luận và đọc số liệu. Dùng khi David gửi video/ghi âm mới, bỏ file vào Drive Video-goc, nói "có video mới", "đăng giúp", "đăng lên các kênh", "làm bài đăng", "lọc nội dung này", "/dang-da-kenh" — kể cả khi chỉ gửi file mà không nói gì.
---

# Đăng đa kênh — một lần nói → đủ bài cho mọi kênh

**Đọc trước:** `../../thoi-quen-lam-viec.md` · `../luat-chung.md`. File khác chỉ đọc ở đúng bước cần (cột cuối bảng quy trình).

**Vai trò:** nội dung là của David (nói tự do, có cảm xúc, không khuôn). Claude lo nhận diện, lọc, thẩm mỹ, nhịp,
phân phối, đăng và đo. Mọi bài có mục tiêu: kéo tương tác đúng nền tảng → chuyển hoá → người xem nhắn "gỡ".

## Mục tiêu
Một tài nguyên vào → Claude làm một mạch tới **kết quả xem được**: bản dài + clip ngắn + thumbnail + bài đăng, nằm sẵn trên trang
xem kết quả (`python3 scripts/xem-ket-qua.py` → localhost:8765; trang tự gom `~/Movies/tap-*`, Drive `Sao-luu-mac/Movies`,
Drive `Video-xong` và sổ danh mục — giữ đúng tên `2-ban-dai/phat-hanh/`, `3-highlight/clip-X/`, `cat/X.md`, `dang-bai.md` là hiện đủ). Không cổng duyệt nào trước khi xong (David 13/11/2026: "không cần duyệt
cổng 1, cổng 2 nữa, cứ thế làm thôi; không ưng thì góp ý rồi render lại toàn bộ"). Chỉ việc **đăng lên mạng xã hội** chờ David nói "đăng" (AGENTS luật 4).

## Quy trình (một mạch, không dừng chờ)
| # | Bước | Đọc / dùng |
|---|---|---|
| 0 | **Nhận tài nguyên**: Drive `Video-goc` hoặc file gửi vào chat → `~/Movies/tap-<ten>/1-goc/`. Chép lời, đo độ dài, khung, chất lượng | khối 01 |
| 1 | **Lọc** (ghi phiếu vào dự án, không chờ): đối chiếu kho 100 video, 5 tiêu chí, lằn ranh, kết luận, kênh, giờ, loại dựng. ⛔ / 👤 / 🗂 → không dựng, chỉ ghi sổ, báo một dòng; lằn ranh → không lấy đoạn đó làm chữ đồ hoạ, tiêu đề, mô tả | khối 00 · `dang-lam/kho-100-video.md` · `../ho-so/kenh.json` · sổ `~/Movies/_so-danh-muc/danh-muc.md` |
| 2 | **Dựng bản dài** theo loại (`video-style-edit` / `podcast-style-edit`). Trong lúc render chạy nền: soạn bài đăng (bước 3) và chọn ý clip ngắn | skill dựng |
| 3 | **Bài đăng** từng kênh vào `phat-hanh/phat-hanh.md`: YouTube (3 tiêu đề, mô tả, chương, thumbnail nếu ngang) · Reels / bài trang · TikTok caption · câu chia sẻ Facebook cá nhân · bình luận ghim · bài Mời "gỡ" theo tỉ lệ | khối 15 · `../ho-so/giong-van-david.md` |
| 4 | **Clip ngắn**: chọn ý trọn đắt nhất theo bốn câu (luôn có, hoặc ghi lý do không có) và **dựng luôn** sau khi bản dài render xong (render nối tiếp, không song song) | `cat-highlight-video` |
| 5 | **Kiểm + giao**: khung hình, âm lượng (khối 17, 09); chép bản dài, clip, thumbnail, `phat-hanh.md` vào Drive `Video-xong/tap-<ten>/ban-dai|highlight/` (trang xem kết quả đọc từ đây); gửi bản xem < 30 MB; ghi sổ; báo Telegram một lần | khối 17 · ghi nhớ `video-chuyen-qua-drive` |
| 6 | **Góp ý của David** → sửa skill / kịch bản đúng chỗ rồi **render lại toàn bộ luôn**, giao lại như bước 5 (không chờ chữ "render") | `../luat-chung.md` mục 8 |
| 7 | **Đăng** (chỉ khi David nói "đăng"): hẹn giờ đúng bản trên trang xem kết quả qua trình duyệt, chụp xác nhận; Facebook cá nhân David tự bấm | khối 19 |
| 8 | **Sau 24 giờ / 7 ngày** *(bước nhẹ)*: hộp thư, số "gỡ", số liệu → `so-lieu.md` + sổ → 1–3 đề xuất | khối 20, 16 |

Bước đánh dấu *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn theo `thoi-quen-lam-viec.md` mục 3.

## Luật riêng của skill
- Chung (tiết kiệm, lệnh nền, báo cáo): `thoi-quen-lam-viec.md`. Video (nhạc, chữ nguyên văn, video dài không cắt, ảnh chỉ Việt Nam): `luat-chung.md`; hình của chính video: khối 14.
- Luật an toàn khi đăng (mật khẩu, cài đặt tài khoản, chỉ đăng đúng bản David bảo đăng): khối 19.
- **Sổ danh mục là nơi duy nhất ghi trạng thái** (lọc → dựng → xong → đã đăng + link).
- Báo cuối gọn: ở đâu (trang xem kết quả + Drive), đã chọn X vì Y, tên riêng cần xác nhận, cảnh báo (lệch nhánh, thiếu bài Mời, kho < 4 video, lịch trống).

## Xong khi
1. Bản dài + clip ngắn + thumbnail (khi ngang) + `phat-hanh.md` đều có trên Drive `Video-xong/tap-<ten>/` và hiện trên trang xem kết quả.
2. Không dừng hỏi giữa chừng; mọi lựa chọn ghi "đã chọn X vì Y" trong báo cáo cuối.
3. Bài đủ kênh theo kết luận, đúng giọng David, kiểu dẫn dắt khớp tỉ lệ.
4. Góp ý → đã render lại toàn bộ và giao lại, không chờ nhắc.
5. Không gì được đăng khi David chưa nói "đăng"; mỗi lần hẹn giờ có ảnh chụp xác nhận.
6. Sổ danh mục và cột Trạng thái trong kho 100 video đúng ở từng bước.

## Nhật ký
- 2026-11-13 · David: "không cần duyệt cổng 1, cổng 2 nữa, cứ thế làm thôi, nếu tôi không ưng thì sẽ góp ý rồi render lại toàn bộ video" → bỏ cả hai cổng: làm một mạch tới bản dài + clip ngắn + bài đăng trên trang xem kết quả; góp ý thì render lại toàn bộ luôn; chỉ việc đăng chờ David nói "đăng".
- 2026-11-13 · Thiếu đề xuất clip ngắn khi gửi bản cuối → "Xong khi" 5: báo cổng 2 luôn có mục clip ngắn đề xuất.
- 2026-11-11 · David: "mục tiêu cuối cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong". Bỏ cổng 1: phiếu lọc chỉ để báo, Claude tự chọn theo mặc định + đề xuất rồi dựng luôn; giữ cổng duyệt trước khi đăng (AGENTS luật 5).
- 2026-11-10 · David chốt: mọi tài nguyên đối chiếu kho 100 video ở phiếu lọc (khớp ý / ⚠️ lệch kho / ý kế tiếp nên quay), dựng / đăng xong đổi trạng thái ý trong kho — để kênh dần đi đúng kế hoạch nội dung.
- 2026-11-05 · vai trò Claude; làm song song khi render.
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): Đọc trước chỉ 2 file, file khác theo bước; cổng 1 gộp mọi điểm cần chọn (tiêu đề, chữ bìa, câu chốt, kênh, giờ), cổng 2 chỉ duyệt bản cuối + chữ bài; clip ngắn Claude tự chọn ý theo bốn câu; đánh dấu bước nhẹ 0, 7, 8; lịch và tỉ lệ trỏ `kenh.json`; luật chung trỏ về nhà; thêm "Xong khi".
