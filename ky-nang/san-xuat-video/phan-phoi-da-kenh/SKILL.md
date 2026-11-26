---
name: phan-phoi-da-kenh
description: Quy trình trọn gói của David — từ MỘT tài nguyên (video quay, ghi âm, bài nói tự phát; thường không kèm yêu cầu), Claude tự lọc theo hồ sơ David, quyết định có đáng làm không và làm thành sản phẩm gì, rồi tự làm trọn không dừng giữa chừng (đã có quy trình nên tự động hoàn toàn): dựng bản dài và clip ngắn, soạn bài theo giọng David cho từng kênh, bàn giao lên Drive và trang xem kết quả (localhost:8765); khi có góp ý thì Claude render lại toàn bộ; Claude không đăng: gói đăng chuẩn bị đủ cho YouTube, trang Facebook, TikTok, David tự đăng; sau khi David đăng thì Claude đọc số liệu. Dùng khi David gửi video hoặc ghi âm mới, bỏ file vào Drive tu-lieu-goc, nói "có video mới", "đăng giúp", "đăng lên các kênh", "làm bài đăng", "lọc nội dung này", "/phan-phoi-da-kenh" — kể cả khi chỉ gửi file mà không nói gì.
---

# Đăng đa kênh — một lần nói thì đủ bài cho mọi kênh

**Đọc trước:** `../../chuan-muc-lam-viec.md` · `../quy-tac-chung.md`. File khác chỉ đọc ở đúng bước cần (cột cuối bảng quy trình).

**Vai trò:** nội dung là của David (nói tự do, có cảm xúc, không theo mẫu). Claude phụ trách nhận diện, lọc, thẩm mỹ, nhịp,
phân phối, đăng và đo lường. Mọi bài có mục tiêu: tạo tương tác đúng nền tảng, dẫn tới chuyển đổi, cuối cùng là người xem nhắn "gỡ".

## Mục tiêu
Khi nhận một tài nguyên, Claude làm liên tục tới **kết quả xem được**: bản dài, clip ngắn, thumbnail, bài đăng, nằm sẵn trên trang
xem kết quả (`python3 tu-dong-hoa/xem-ket-qua.py` mở localhost:8765; trang tự tổng hợp `~/Movies/tap-*`, Drive `sao-luu-mac/video`,
Drive `thanh-pham` và sổ danh mục; giữ đúng tên `2-ban-day-du/phat-hanh/`, `3-doan-noi-bat/clip-X/`, `cat/X.md`, `dang-bai.md` thì trang hiện đủ). Đây là quy trình đã có nên Claude không trình 4 phần, không dừng chờ ở bước nào trước khi xong: nếu David
chưa hài lòng thì David góp ý, rồi Claude render lại toàn bộ. Claude **không đăng** lên mạng xã hội (AGENTS luật 4): gói đăng Claude tự sắp xếp đủ theo sản phẩm, David tự đăng. **Dọn sau khi bàn giao** làm khi David nói "chốt" (`quy-trinh.md` mục 1), không hỏi lại.

**Không có bước duyệt 4 phần** (`chuan-muc-lam-viec.md` mục 2): nhận tài nguyên và lọc (bước 0–1 dưới) xong thì Claude dựng luôn theo phiếu lọc (làm thành gì, khung, số clip, kênh theo mặc định của skill), chạy liên tục như dưới; phiếu lọc ghi vào báo cáo.

## Quy trình (làm liên tục, không dừng chờ)
| # | Bước | Đọc / dùng |
|---|---|---|
| 0 | **Nhận tài nguyên** (link Drive / YouTube, file trong chat, Drive `tu-lieu-goc`: `references/nhan-tai-nguyen.md`) → `~/Movies/tap-<ten>/1-goc/`. Chép lời **theo từng phân đoạn ngắn rồi hợp nhất** (`dung-video-theo-phong-cach/scripts/chep-theo-phan-doan.py`, chính xác hơn chép cả file nhất là nơi ồn); đo độ dài, khung, chất lượng | khối 01 |
| 1 | **Lọc + phân hướng** (ghi phiếu vào dự án; phiếu là nguồn của kế hoạch dựng, không có cổng duyệt): chia đoạn theo ý, gán đủ ba hướng, mỗi hướng có ý trọn ra một bản riêng (khối 00 mục 0b) → ghi `phan-huong.md` của tập + mục nhật ký từng hướng `du-an/nhat-ky-noi-dung/` (luôn ghi, kể cả tập không dựng); đối chiếu kho 100 video, 5 tiêu chí, lằn ranh, kết luận, kênh, giờ, loại dựng. Bước 2–4 làm cho từng bản theo hướng. ⛔ / 👤 / 🗂 → không dựng, chỉ ghi sổ, báo một dòng; lằn ranh → không lấy đoạn đó làm chữ đồ hoạ, tiêu đề, mô tả | khối 00 · `du-an/ke-hoach-noi-dung-100-video.md` · `../ho-so-thuong-hieu/kenh.json` · sổ `~/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md` |
| 2 | **Dựng bản dài** theo loại (`dung-video-theo-phong-cach` / `dung-podcast`); nhiều file cùng một buổi nói → nối file, dựng mẫu 1 video; mỗi bản theo hướng chẩn đoán riêng (`../thiet-ke-bo-cuc/huong-dan-lua-chon.md`, không chép kịch bản bản khác). Trong lúc render chạy nền: soạn bài đăng (bước 3) và chọn ý clip ngắn | skill dựng |
| 3 | **Bài đăng** từng kênh vào `phat-hanh/phat-hanh.md`: YouTube (3 tiêu đề, mô tả, chương, thumbnail nếu ngang) · Reels / bài trang · TikTok caption · câu chia sẻ Facebook cá nhân · bình luận ghim · bài Mời "gỡ" theo tỉ lệ | khối 15 · `../ho-so-thuong-hieu/giong-thuong-hieu-david.md` |
| 4 | **Clip ngắn**: chọn ý trọn then chốt nhất theo bốn câu hỏi (luôn có, hoặc ghi lý do không có) và **dựng luôn** sau khi bản dài render xong (render nối tiếp, không song song) | `cat-doan-noi-bat` |
| 5 | **Kiểm + giao**: khung hình, âm lượng (khối 17, 09); chép bản cuối (bản dài, clip, thumbnail, `phat-hanh.md`, `dang-bai.md`) vào `~/Movies/cho-dang/tap-<ten>/ban-dai|highlight/` rồi `cho-dang.sh gui tap-<ten>` (tự làm bản xem nhẹ, lên Drive `thanh-pham/` giống hệt, trang xem kết quả đọc từ đây); buổi tách nhiều hướng thì thêm `cho-dang.sh buoi <buổi>` (kết quả chung của buổi, `../dung-video-theo-phong-cach/references/tach-theo-huong.md` bước 5). **Làm ra gì thì lên Drive đủ hết**, so khớp rồi mới báo; gửi bản xem < 30 MB; khi David chốt bản cuối (Đ2) mới chuyển dự án dựng lên Drive bằng `luu-drive.sh` — **Mac chỉ giữ bản cuối chưa đăng**; ghi sổ; báo Telegram một lần | khối 17 · ghi nhớ `video-chuyen-qua-drive` · `../dung-video-theo-phong-cach/scripts/cho-dang.sh` |
| 6 | **Góp ý của David** (góp ý là lời duyệt cho chính thay đổi đó, `quy-trinh.md` mục 1) → sửa skill / kịch bản đúng chỗ rồi **render lại toàn bộ luôn**, giao lại như bước 5 (không chờ chữ "render") | `../quy-tac-chung.md` mục 8 |
| 7 | **David tự đăng** (Claude không đăng): gói đăng đủ ở `~/Movies/cho-dang/tap-<ten>/` và Drive `thanh-pham/` (bản cuối, `dang-bai.md`: tiêu đề, mô tả, bài từng kênh, bình luận ghim, ảnh bìa, lịch gợi ý). David báo "đã đăng <tập>" → ghi liên kết vào sổ danh mục, `cho-dang.sh xong tap-<ten>` (kiểm Drive rồi mới xoá bản Mac) | khối 15 |
| 8 | **Sau 24 giờ / 7 ngày** *(bước nhẹ)*: hộp thư, số "gỡ", số liệu → `so-lieu.md` + sổ → 1–3 đề xuất | khối 20, 16 |

Với bước có nhãn *(bước nhẹ)*, Claude nhắc đổi sang mô hình chi phí thấp hơn (`../../chuan-muc-lam-viec.md` mục 3).

## Luật riêng của skill
- Chung (tiết kiệm, lệnh nền, báo cáo): `chuan-muc-lam-viec.md`. Video (nhạc, chữ nguyên văn, video dài không cắt, ảnh chỉ Việt Nam): `quy-tac-chung.md`; hình của chính video: khối 14.
- Claude không đăng bài, không đụng mật khẩu, cài đặt tài khoản mạng xã hội (AGENTS luật 4); khối 19 tạm ngưng.
- **Sổ danh mục là nơi duy nhất ghi trạng thái** (lọc → dựng → xong → đã đăng + link).
- **Thiết bị chỉ dựng video** (`~/.claude/vai-may` ghi `chi-video`: Windows qua WSL2, Mac khác): bước 0–6 làm giống hệt Mac chính. Bàn giao bằng `cho-dang.sh gui tap-<ten>`; máy Windows này **không đồng bộ Drive** (`du-an/kho-drive.md` mục "Máy Windows": tải lên bằng lệnh vào `thanh-pham-may-windows/`, dự án bằng `luu-drive.sh`; chưa kết nối thì giữ ở ổ D và báo "chưa lên Drive"; chỗ nào dưới đây ghi `thanh-pham/` thì hiểu theo mục đó); không có trang xem kết quả và không có bot Telegram (`bao-cao.sh` chỉ ở repo riêng của Mac): bỏ bước báo Telegram, báo kết quả ngay trong chat. Bước 7: gói đăng ở `~/Movies/cho-dang/tap-<ten>/`, David tự đăng. Video gốc tải bằng link David gửi.
- **Xác định David trong khung trước khi gắn nhãn** (lời David: đã có rất nhiều ảnh và video mặt David thì không được để "chưa phân biệt được ai là David"): trước phân hướng, mở ảnh mẫu mặt David ở Drive `Tài nguyên làm video/mau-mat-david/` (và khung các tập cũ đã dựng) rồi so với khung của tập; ghi vào `phan-huong.md` "David là người … (vị trí, đặc điểm)". Người còn lại là người khác (đối tác / khách). Claude không suy luận từ nội dung lời nói khi đã so sánh được bằng hình.
- Báo cáo cuối ngắn gọn: ở đâu (trang xem kết quả + Drive), đã chọn X vì Y, tên riêng cần xác nhận, cảnh báo (lệch nhánh, thiếu bài Mời, kho < 4 video, lịch trống).

## Xong khi
1. Bản dài + bản xem nhẹ + clip ngắn + thumbnail (khi ngang) + `phat-hanh.md` (và `_buoi-<buổi>/` khi tách theo hướng) đều có trên Drive `thanh-pham/tap-<ten>/` và ở `~/Movies/cho-dang/tap-<ten>/`, hiện trên trang xem kết quả và trang Chờ đăng (`localhost:8765/mac`, cột ✅). Thiết bị chỉ dựng video: có ở `~/Movies/cho-dang/tap-<ten>/`, đã gửi bản xem nhẹ, đã lên Drive theo `du-an/kho-drive.md` mục "Máy Windows" (hoặc báo rõ vì sao chưa lên).
2. Không dừng hỏi giữa chừng (trừ Đ2, Đ3; quy trình sai thì sửa quy trình rồi làm tiếp); mọi lựa chọn ghi "đã chọn X vì Y" trong báo cáo cuối.
3. Bài đủ kênh theo kết luận, đúng giọng David, kiểu dẫn dắt khớp tỉ lệ.
4. Khi có góp ý, Claude đã render lại toàn bộ và bàn giao lại, không chờ nhắc.
5. Claude không đăng nội dung nào; gói đăng đủ để David tự đăng, có ở nơi giao và Drive.
6. Sổ danh mục và cột Trạng thái trong kho 100 video đúng ở từng bước.

## Tài liệu kèm
- [references/nhat-ky-thay-doi.md](references/nhat-ky-thay-doi.md) — sổ quyết định theo ngày + lý do (không đọc lúc làm việc).
