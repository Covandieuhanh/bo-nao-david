---
description: "Dự án chuẩn hoá bộ skill theo thói quen làm việc chung (08/11): các bước, mốc commit, việc còn lại."
---

# Chuẩn hoá bộ skill theo thói quen làm việc chung

Bắt đầu: 08/11/2026. Mốc trước khi sửa: commit `1810b8c`.

## Mục tiêu
Mọi skill tự làm việc theo một bộ thói quen chung: đúng quy trình, tiết kiệm token, cho kết quả đúng ý ngay lần đầu. Mỗi luật chỉ nằm ở một nguồn duy nhất.

## Đã chốt (vòng 1, 08/11/2026)
1. Phạm vi: 5 skill video, `thu-thap-yeu-cau`, các khối dùng chung và `david.md`, `AGENTS.md`, `MEMORY.md`. Bỏ qua `playwright-cli`.
2. Có một file thói quen chung, mọi skill đọc file này trước; trong skill chỉ thêm "cổng kiểm" ngắn ở bước dễ sai.
3. Claude rà soát trước (trùng lặp, mâu thuẫn, lỗi thời), David quyết định từng chỗ rồi mới sửa.
4. Mỗi skill có danh sách "Xong khi" 5–8 dòng do David duyệt; skill chạy một việc thật đạt đủ tiêu chí mà không phải sửa lại.
5. Mỗi bước được làm trong một phiên ngắn và được theo dõi ở file này.

## Đã chốt (vòng 2, 08/11/2026): nội dung file thói quen chung
1. Bốn nhóm: **đầu việc** (chỉ đọc đúng phần cần, không đọc cả repo) · **hỏi** (gộp câu hỏi một lần, có đề xuất) · **trong lúc làm** (chụp khung hình có giới hạn, chỉ dùng agent phụ khi David cho phép, chạy lệnh theo lô) · **cuối việc** (cập nhật bộ não và file theo dõi, đề nghị phiên mới cho việc tiếp theo).
2. Khi có xung đột thì **chất lượng được ưu tiên** ("kết quả hơn tốc độ"); chỉ tiết kiệm ở chỗ không ảnh hưởng kết quả (ví dụ: khi kiểm video, chỉ chụp đúng các mốc dễ lỗi, không chụp từng cảnh).
3. Skill ghi rõ bước nào là bước nhẹ; tới bước đó, Claude nhắc một dòng để David tự đổi mô hình, Claude không tự đổi.
4. Góp ý của David được ghi ở **đúng một chỗ**: skill hoặc khối bị ảnh hưởng, kèm một dòng nhật ký; chỉ luật dùng chung cho nhiều skill mới được đưa vào bộ nhớ, không tạo ghi nhớ trùng lặp.
5. File được đặt ở `ky-nang/chuan-muc-lam-viec.md` (cấp gốc); `ky-nang/san-xuat-video/quy-tac-chung.md` chỉ giữ luật riêng cho video.

## Thực thi
- [x] Bước 0: lưu mốc lên GitHub
- [x] Vòng 2: chốt nội dung file thói quen chung
- [x] Bước 1: lập bảng rà soát luật (trùng / ngược / cũ) rồi David duyệt
  - [x] Bảng đã xong: `du-an/danh-gia-luat.md` (15 ngược · 12 trùng · 8 cũ · 3 câu hỏi), 08/11/2026
  - [x] David duyệt 08/11: chỗ mâu thuẫn thì lấy bên mới nhất; chữ trên video chỉ dùng lời David nói chính xác; lịch phát hành chỉ ghi khi David đưa; tên trang để sau
- [x] Bước 2: viết file thói quen chung rồi David duyệt
  - [x] Bản nháp: `ky-nang/chuan-muc-lam-viec.md` (08/11)
  - [x] David duyệt 08/11
- [x] Bước 3: tinh gọn từng skill và viết "Xong khi" (mỗi skill một phiên)
  - [x] thu-thap-yeu-cau (08/11: 2–3 gợi ý, bỏ "kinh doanh", một vòng gộp / thiết kế nhiều vòng, "Xong khi" 7 dòng David duyệt)
  - [x] phan-phoi-da-kenh (08/11: đọc trước 2 file, cổng 1 gộp mọi lựa chọn, clip tự chọn theo bốn câu, bước nhẹ 0·7·8, "Xong khi" 7 dòng)
  - [x] dung-video-theo-phong-cach (08/11: hỏi một lần đầu, bỏ con số cố định/thẻ tiêu đề/2 trạng thái, màn chốt nguyên văn, bước nhẹ 1·2·5, "Xong khi" 7 dòng; sửa 1 dòng scene-design và multi-clip)
  - [x] dung-podcast (08/11: hỏi một lần và giữ cổng chụp thử, bỏ thẻ tên tập/số nhịp/2 trạng thái, màn chốt nguyên văn, phụ đề dọc cỡ 58, "Xong khi" 7 dòng)
  - [x] cat-doan-noi-bat (08/11: mọi chữ nguyên văn, màn chốt một luật, thẻ cuối không nút phát/không câu Claude viết, bỏ số nhịp, "Xong khi" 7 dòng)
  - [x] phan-tich-video-mau (08/11: đọc trước thói quen chung, phiếu học là cổng hỏi duy nhất, tải 720p chỉ để học rồi xoá, bước nhẹ 1–3 ở thiet-ke-bo-cuc, "Xong khi" 6 dòng)
  - [x] 3 file bộ não (08/11: david.md 3.1/3.8/5 trỏ nguồn chính; AGENTS thêm thoi-quen vào bảng đọc, rút gọn mục giữ bộ não; chi-dan-toan-cuc trỏ thoi-quen; 2 ghi nhớ chuyển vào luu-tru, 3 ghi nhớ được rút ngắn, 9 ghi nhớ được sửa theo N8/N9/C2/C4/C7/T3/T8; MEMORY khớp 33 file)
- [x] Phiên A (08/11): tinh gọn khối 05, 06, 07, 08, 13, 15, 17, 19, `mo-dun/README`, `quy-tac-chung` mục 0 (N9); bỏ chữ "2 trạng thái là mặc định" ở scene-design, thu-vien-tai-nguyen, Illus, vlog_edl, doan-noi-bat.md; mã nguồn: thẻ cuối luôn là "Bản đầy đủ trên kênh …" (bỏ "XEM BẢN ĐẦY ĐỦ" và `tease`), phụ đề podcast dọc là cụm 5–8 chữ ở mọi độ dài
  - [x] David đồng ý 08/11: câu mời bình luận / câu hỏi tự xét / "gỡ" theo luật kênh nằm ở mô tả và bình luận ghim, không đưa lên video (khối 08, quy-tac-chung)
- [x] Dọn file tạm (08/11): `dung-video-theo-phong-cach/scripts/don-tap.py`, tích hợp vào khối 17, thoi-quen mục 4, 3 skill; bỏ khối 18 cùng mọi phần xuất sang CapCut/DaVinci (David không dùng)
  - [x] Sau khi David duyệt 08/11, 8 tập đã được dọn (khoảng 62 GB; 16 bản cuối vẫn còn đủ); tap-zoom-trainer chưa có bản cuối nên được giữ nguyên
- [ ] Bước 4: chạy thử một việc thật, David chấm, sửa đúng một chỗ (chưa render thử thẻ cuối và phụ đề podcast dọc sau phiên A)

## Code còn lệch với skill
Đã sửa ở phiên A (08/11).

## Xong khi (mục não, David duyệt 08/11)
1. Mỗi luật chỉ có một nguồn duy nhất; chỗ khác chỉ có một dòng trỏ về nguồn đó.
2. Không có ghi nhớ nào mâu thuẫn với luật đã chốt hoặc trỏ tới đường dẫn không tồn tại.
3. `MEMORY.md` khớp từng file (33/33, đã kiểm 08/11).
4. Một AI mới đọc `AGENTS.md` sẽ đi tới được `chuan-muc-lam-viec.md`.
5. Đã push lên GitHub; file trong `~/.claude` vẫn là lối tắt vào repo.
