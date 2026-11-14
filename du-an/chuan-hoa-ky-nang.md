# Chuẩn hoá bộ skill theo thói quen làm việc chung

Bắt đầu: 08/11/2026. Mốc trước khi sửa: commit `1810b8c`.

## Mục tiêu
Mọi skill tự làm việc theo một bộ thói quen chung: đúng quy trình, tiết kiệm token, ra đúng ý ngay lần đầu. Mỗi luật chỉ nằm một chỗ.

## Đã chốt (vòng 1, 08/11/2026)
1. Phạm vi: 5 skill video + `thu-thap-yeu-cau` + các khối dùng chung + `David.md`, `AGENTS.md`, `MEMORY.md`. Bỏ qua `playwright-cli`.
2. Một file thói quen chung, mọi skill đọc trước; trong skill chỉ thêm "cổng kiểm" ngắn ở bước dễ sai.
3. Rà soát trước (trùng, ngược, cũ), David quyết từng chỗ rồi mới sửa.
4. Mỗi skill có danh sách "Xong khi" 5–8 dòng do David duyệt; chạy một việc thật đạt đủ mà không phải sửa lại.
5. Mỗi bước một phiên ngắn, theo dõi ở file này.

## Đã chốt (vòng 2, 08/11/2026): nội dung file thói quen chung
1. Bốn nhóm: **đầu việc** (đọc đúng phần cần, không đọc cả repo) · **hỏi** (gộp một lần, có đề xuất) · **trong lúc làm** (chụp khung có giới hạn, agent phụ chỉ khi David cho, chạy lệnh theo lô) · **cuối việc** (cập nhật não + file theo dõi, đề nghị phiên mới cho việc tiếp).
2. Xung đột thì **chất lượng thắng** ("kết quả hơn tốc độ"); tiết kiệm chỉ ở chỗ không ảnh hưởng kết quả (vd. kiểm video chụp đúng mốc dễ lỗi, không chụp từng cảnh).
3. Skill ghi rõ bước nào nhẹ; tới đó Claude nhắc một dòng để David tự đổi mô hình, không tự đổi.
4. Góp ý của David ghi **đúng một chỗ**: skill/khối bị ảnh hưởng + một dòng nhật ký; chỉ luật dùng chung nhiều skill mới vào bộ nhớ, không tạo ghi nhớ trùng.
5. File đặt ở `ky-nang/chuan-muc-lam-viec.md` (cấp gốc); `ky-nang/san-xuat-video/quy-tac-chung.md` chỉ giữ luật riêng video.

## Thực thi
- [x] Bước 0: lưu mốc lên GitHub
- [x] Vòng 2: chốt nội dung file thói quen chung
- [x] Bước 1: bảng rà soát luật (trùng / ngược / cũ) → David duyệt
  - [x] Bảng đã xong: `du-an/danh-gia-luat.md` (15 ngược · 12 trùng · 8 cũ · 3 câu hỏi), 08/11/2026
  - [x] David duyệt 08/11: ngược thì lấy bên mới nhất; chữ trên video chỉ lời David nói chính xác; lịch phát khi David đưa; tên trang để sau
- [x] Bước 2: viết file thói quen chung → David duyệt
  - [x] Bản nháp: `ky-nang/chuan-muc-lam-viec.md` (08/11)
  - [x] David duyệt 08/11
- [x] Bước 3: gọt từng skill + "Xong khi" (mỗi skill một phiên)
  - [x] thu-thap-yeu-cau (08/11: 2–3 gợi ý, bỏ "kinh doanh", một vòng gộp / thiết kế nhiều vòng, "Xong khi" 7 dòng David duyệt)
  - [x] phan-phoi-da-kenh (08/11: đọc trước 2 file, cổng 1 gộp mọi lựa chọn, clip tự chọn theo bốn câu, bước nhẹ 0·7·8, "Xong khi" 7 dòng)
  - [x] dung-video-theo-phong-cach (08/11: hỏi một lần đầu, bỏ con số cố định/thẻ tít/2 trạng thái, màn chốt nguyên văn, bước nhẹ 1·2·5, "Xong khi" 7 dòng; sửa 1 dòng scene-design + multi-clip)
  - [x] dung-podcast (08/11: hỏi một lần + giữ cổng chụp thử, bỏ thẻ tên tập/số nhịp/2 trạng thái, màn chốt nguyên văn, phụ đề dọc cỡ 58, "Xong khi" 7 dòng)
  - [x] cat-doan-noi-bat (08/11: mọi chữ nguyên văn, màn chốt một luật, thẻ cuối không nút phát/không câu Claude viết, bỏ số nhịp, "Xong khi" 7 dòng)
  - [x] phan-tich-video-mau (08/11: đọc trước thói quen chung, phiếu học là cổng hỏi duy nhất, tải 720p chỉ để học rồi xoá, bước nhẹ 1–3 ở thiet-ke-bo-cuc, "Xong khi" 6 dòng)
  - [x] 3 file não (08/11: David.md 3.1/3.8/5 trỏ nhà chính; AGENTS thêm thoi-quen vào bảng đọc, rút mục giữ não; chi-dan-toan-cuc trỏ thoi-quen; 2 ghi nhớ vào luu-tru, 3 ghi nhớ rút ngắn, 9 ghi nhớ sửa theo N8/N9/C2/C4/C7/T3/T8; MEMORY khớp 33 file)
- [x] Phiên A (08/11): gọt khối 05, 06, 07, 08, 13, 15, 17, 19, `mo-dun/README`, `quy-tac-chung` mục 0 (N9); bỏ chữ "2 trạng thái là mặc định" ở scene-design, thu-vien-tai-nguyen, Illus, vlog_edl, highlight.md; code: thẻ cuối luôn "Bản đầy đủ trên kênh …" (bỏ "XEM BẢN ĐẦY ĐỦ" và `tease`), phụ đề podcast dọc cụm 5–8 chữ mọi độ dài
  - [x] David đồng ý 08/11: câu mời bình luận / câu hỏi tự soi / "gỡ" theo luật kênh nằm ở mô tả + bình luận ghim, không lên video (khối 08, quy-tac-chung)
- [x] Dọn file tạm (08/11): `dung-video-theo-phong-cach/scripts/don_tap.py`, gắn vào khối 17, thoi-quen mục 4, 3 skill; bỏ khối 18 cùng mọi phần xuất CapCut/DaVinci (David không dùng)
  - [x] David duyệt 08/11 → đã dọn 8 tập (~62 GB; 16 bản cuối còn đủ); tap-zoom-trainer chưa có bản cuối nên giữ nguyên
- [ ] Bước 4: chạy thử một việc thật, David chấm, sửa đúng một chỗ (chưa render thử thẻ cuối và phụ đề podcast dọc sau phiên A)

## Code còn lệch với skill
Đã sửa ở phiên A (08/11).

## Xong khi (mục não, David duyệt 08/11)
1. Mỗi luật chỉ một nhà; chỗ khác một dòng trỏ.
2. Không ghi nhớ nào ngược luật đã chốt hoặc trỏ đường dẫn không tồn tại.
3. `MEMORY.md` khớp từng file (33/33, đã kiểm 08/11).
4. AI mới đọc `AGENTS.md` đi tới được `chuan-muc-lam-viec.md`.
5. Đã đẩy GitHub; file trong `~/.claude` vẫn là lối tắt vào repo.
