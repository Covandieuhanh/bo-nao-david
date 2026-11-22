---
name: phan-phoi-da-kenh
description: Quy trình trọn gói của David — từ MỘT tài nguyên (video quay, ghi âm, bài nói bộc phát; thường không kèm yêu cầu) Claude tự lọc theo hồ sơ David, quyết định có đáng làm và làm thành gì, trình 4 phần chờ David duyệt, rồi làm một mạch không cổng duyệt: dựng bản dài + clip ngắn, soạn bài theo giọng David cho từng kênh, giao lên Drive và trang xem kết quả (localhost:8765); góp ý thì render lại toàn bộ; khi David nói "đăng" thì hẹn giờ YouTube, trang Facebook, TikTok qua trình duyệt đã đăng nhập, rồi gom bình luận và đọc số liệu. Dùng khi David gửi video/ghi âm mới, bỏ file vào Drive tu-lieu-goc, nói "có video mới", "đăng giúp", "đăng lên các kênh", "làm bài đăng", "lọc nội dung này", "/phan-phoi-da-kenh" — kể cả khi chỉ gửi file mà không nói gì.
---

# Đăng đa kênh — một lần nói thì đủ bài cho mọi kênh

**Đọc trước:** `../../chuan-muc-lam-viec.md` · `../quy-tac-chung.md`. File khác chỉ đọc ở đúng bước cần (cột cuối bảng quy trình).

**Vai trò:** nội dung là của David (nói tự do, có cảm xúc, không khuôn). Claude lo nhận diện, lọc, thẩm mỹ, nhịp,
phân phối, đăng và đo. Mọi bài có mục tiêu: kéo tương tác đúng nền tảng → chuyển hoá → người xem nhắn "gỡ".

## Mục tiêu
Một tài nguyên vào thì Claude làm một mạch tới **kết quả xem được**: bản dài + clip ngắn + thumbnail + bài đăng, nằm sẵn trên trang
xem kết quả (`python3 tu-dong-hoa/xem-ket-qua.py` → localhost:8765; trang tự gom `~/Movies/tap-*`, Drive `sao-luu-mac/video`,
Drive `thanh-pham` và sổ danh mục — giữ đúng tên `2-ban-day-du/phat-hanh/`, `3-doan-noi-bat/clip-X/`, `cat/X.md`, `dang-bai.md` là hiện đủ). Không cổng duyệt nào trước khi xong: David
không ưng thì góp ý rồi render lại toàn bộ. Chỉ việc **đăng lên mạng xã hội** chờ David nói "đăng" (AGENTS luật 4).

**Bước 0 — duyệt 4 phần** (`chuan-muc-lam-viec.md` mục 2): nhận tài nguyên + lọc (bước 0–1 dưới) xong thì, trước khi dựng, trình 4 phần gọn lấy từ phiếu lọc (làm thành gì, khung, số clip, kênh; điểm skill đã định ghi luôn) và chờ David "duyệt". Duyệt rồi mới chạy một mạch như dưới.

## Quy trình (sau khi duyệt 4 phần: một mạch, không dừng chờ)
| # | Bước | Đọc / dùng |
|---|---|---|
| 0 | **Nhận tài nguyên** (link Drive / YouTube, file trong chat, Drive `tu-lieu-goc`: `references/nhan-tai-nguyen.md`) → `~/Movies/tap-<ten>/1-goc/`. Chép lời, đo độ dài, khung, chất lượng | khối 01 |
| 1 | **Lọc + phân hướng** (ghi phiếu vào dự án; phiếu là nguồn của 4 phần, không có cổng duyệt riêng): chia đoạn theo ý, gán đủ ba hướng, mỗi hướng có ý trọn ra một bản riêng (khối 00 mục 0b) → ghi `phan-huong.md` của tập + mục nhật ký từng hướng `du-an/nhat-ky-noi-dung/` (luôn ghi, kể cả tập không dựng); đối chiếu kho 100 video, 5 tiêu chí, lằn ranh, kết luận, kênh, giờ, loại dựng. Bước 2–4 làm cho từng bản theo hướng. ⛔ / 👤 / 🗂 → không dựng, chỉ ghi sổ, báo một dòng; lằn ranh → không lấy đoạn đó làm chữ đồ hoạ, tiêu đề, mô tả | khối 00 · `du-an/ke-hoach-noi-dung-100-video.md` · `../ho-so-thuong-hieu/kenh.json` · sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md` |
| 2 | **Dựng bản dài** theo loại (`dung-video-theo-phong-cach` / `dung-podcast`); nhiều file cùng một buổi nói → nối file, dựng khuôn 1 video; mỗi bản theo hướng chẩn đoán riêng (`../thiet-ke-bo-cuc/tu-chon.md`, không chép kịch bản bản khác). Trong lúc render chạy nền: soạn bài đăng (bước 3) và chọn ý clip ngắn | skill dựng |
| 3 | **Bài đăng** từng kênh vào `phat-hanh/phat-hanh.md`: YouTube (3 tiêu đề, mô tả, chương, thumbnail nếu ngang) · Reels / bài trang · TikTok caption · câu chia sẻ Facebook cá nhân · bình luận ghim · bài Mời "gỡ" theo tỉ lệ | khối 15 · `../ho-so-thuong-hieu/giong-thuong-hieu-david.md` |
| 4 | **Clip ngắn**: chọn ý trọn đắt nhất theo bốn câu (luôn có, hoặc ghi lý do không có) và **dựng luôn** sau khi bản dài render xong (render nối tiếp, không song song) | `cat-doan-noi-bat` |
| 5 | **Kiểm + giao**: khung hình, âm lượng (khối 17, 09); chép bản cuối (bản dài, clip, thumbnail, `phat-hanh.md`, `dang-bai.md`) vào `~/Movies/cho-dang/tap-<ten>/ban-dai|highlight/` rồi `cho-dang.sh gui tap-<ten>` (lên Drive `thanh-pham/` y hệt, trang xem kết quả đọc từ đây); dự án dựng chuyển lên Drive bằng `luu-drive.sh` — **Mac chỉ giữ bản cuối chưa đăng**; gửi bản xem < 30 MB; ghi sổ; báo Telegram một lần | khối 17 · ghi nhớ `video-chuyen-qua-drive` · `../dung-video-theo-phong-cach/scripts/cho-dang.sh` |
| 6 | **Góp ý của David** → sửa skill / kịch bản đúng chỗ rồi **render lại toàn bộ luôn**, giao lại như bước 5 (không chờ chữ "render") | `../quy-tac-chung.md` mục 8 |
| 7 | **Đăng** (chỉ khi David nói "đăng"): hẹn giờ đúng bản trong `~/Movies/cho-dang/tap-<ten>/` qua trình duyệt, chụp xác nhận; Facebook cá nhân David tự bấm. Đăng xong mọi kênh của tập (hoặc David nói "đã đăng <tập>") → `cho-dang.sh xong tap-<ten>` (kiểm Drive rồi mới xoá bản Mac) | khối 19 |
| 8 | **Sau 24 giờ / 7 ngày** *(bước nhẹ)*: hộp thư, số "gỡ", số liệu → `so-lieu.md` + sổ → 1–3 đề xuất | khối 20, 16 |

Bước *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn (`../../chuan-muc-lam-viec.md` mục 3).

## Luật riêng của skill
- Chung (tiết kiệm, lệnh nền, báo cáo): `chuan-muc-lam-viec.md`. Video (nhạc, chữ nguyên văn, video dài không cắt, ảnh chỉ Việt Nam): `quy-tac-chung.md`; hình của chính video: khối 14.
- Luật an toàn khi đăng (mật khẩu, cài đặt tài khoản, chỉ đăng đúng bản David bảo đăng): khối 19.
- **Sổ danh mục là nơi duy nhất ghi trạng thái** (lọc → dựng → xong → đã đăng + link).
- **Máy chỉ dựng video** (`~/.claude/vai-may` ghi `chi-video`: Windows qua WSL2, Mac khác): bước 0–6 làm y như Mac chính. Giao bằng Drive (`cho-dang.sh gui`), không có trang xem kết quả. Bước 7 (đăng) chỉ làm ở Mac chính: báo David mở Mac chính và nói "đăng". Video gốc trên Drive đọc ở `/mnt/<ổ>/My Drive/...`.
- Báo cuối gọn: ở đâu (trang xem kết quả + Drive), đã chọn X vì Y, tên riêng cần xác nhận, cảnh báo (lệch nhánh, thiếu bài Mời, kho < 4 video, lịch trống).

## Xong khi
1. Bản dài + clip ngắn + thumbnail (khi ngang) + `phat-hanh.md` đều có trên Drive `thanh-pham/tap-<ten>/` và ở `~/Movies/cho-dang/tap-<ten>/`, hiện trên trang xem kết quả và trang Chờ đăng (`localhost:8765/mac`, cột ✅).
2. Không dừng hỏi giữa chừng; mọi lựa chọn ghi "đã chọn X vì Y" trong báo cáo cuối.
3. Bài đủ kênh theo kết luận, đúng giọng David, kiểu dẫn dắt khớp tỉ lệ.
4. Góp ý thì đã render lại toàn bộ và giao lại, không chờ nhắc.
5. Không gì được đăng khi David chưa nói "đăng"; mỗi lần hẹn giờ có ảnh chụp xác nhận.
6. Sổ danh mục và cột Trạng thái trong kho 100 video đúng ở từng bước.

## Tài liệu kèm
- [references/nhat-ky-thay-doi.md](references/nhat-ky-thay-doi.md) — sổ quyết định theo ngày + lý do (không đọc lúc làm việc).
