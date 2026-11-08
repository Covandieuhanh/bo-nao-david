# Chuẩn hoá bộ skill theo thói quen làm việc chung

Bắt đầu: 08/11/2026. Mốc trước khi sửa: commit `1810b8c`.

## Mục tiêu
Mọi skill tự làm việc theo một bộ thói quen chung: đúng quy trình, tiết kiệm token, ra đúng ý ngay lần đầu. Mỗi luật chỉ nằm một chỗ.

## Đã chốt (vòng 1, 08/11/2026)
1. Phạm vi: 5 skill video + `hoi-chuyen-gia` + các khối dùng chung + `David.md`, `AGENTS.md`, `MEMORY.md`. Bỏ qua `playwright-cli`.
2. Một file thói quen chung, mọi skill đọc trước; trong skill chỉ thêm "cổng kiểm" ngắn ở bước dễ sai.
3. Rà soát trước (trùng, ngược, cũ), David quyết từng chỗ rồi mới sửa.
4. Mỗi skill có danh sách "Xong khi" 5–8 dòng do David duyệt; chạy một việc thật đạt đủ mà không phải sửa lại.
5. Mỗi bước một phiên ngắn, theo dõi ở file này.

## Đã chốt (vòng 2, 08/11/2026): nội dung file thói quen chung
1. Bốn nhóm: **đầu việc** (đọc đúng phần cần, không đọc cả repo) · **hỏi** (gộp một lần, có đề xuất) · **trong lúc làm** (chụp khung có giới hạn, agent phụ chỉ khi David cho, chạy lệnh theo lô) · **cuối việc** (cập nhật não + file theo dõi, đề nghị phiên mới cho việc tiếp).
2. Xung đột thì **chất lượng thắng** ("kết quả hơn tốc độ"); tiết kiệm chỉ ở chỗ không ảnh hưởng kết quả (vd. kiểm video chụp đúng mốc dễ lỗi, không chụp từng cảnh).
3. Skill ghi rõ bước nào nhẹ; tới đó Claude nhắc một dòng để David tự đổi mô hình, không tự đổi.
4. Góp ý của David ghi **đúng một chỗ**: skill/khối bị ảnh hưởng + một dòng nhật ký; chỉ luật dùng chung nhiều skill mới vào bộ nhớ, không tạo ghi nhớ trùng.
5. File đặt ở `skills/thoi-quen-lam-viec.md` (cấp gốc); `skills/dung-video/luat-chung.md` chỉ giữ luật riêng video.

## Thực thi
- [x] Bước 0: lưu mốc lên GitHub
- [x] Vòng 2: chốt nội dung file thói quen chung
- [x] Bước 1: bảng rà soát luật (trùng / ngược / cũ) → David duyệt
  - [x] Bảng đã xong: `dang-lam/ra-soat-luat.md` (15 ngược · 12 trùng · 8 cũ · 3 câu hỏi), 08/11/2026
  - [x] David duyệt 08/11: ngược thì lấy bên mới nhất; chữ trên video chỉ lời David nói chính xác; lịch phát khi David đưa; tên trang để sau
- [x] Bước 2: viết file thói quen chung → David duyệt
  - [x] Bản nháp: `skills/thoi-quen-lam-viec.md` (08/11)
  - [x] David duyệt 08/11
- [ ] Bước 3: gọt từng skill + "Xong khi" (mỗi skill một phiên)
  - [x] hoi-chuyen-gia (08/11: 2–3 gợi ý, bỏ "kinh doanh", một vòng gộp / thiết kế nhiều vòng, "Xong khi" 7 dòng David duyệt)
  - [x] dang-da-kenh (08/11: đọc trước 2 file, cổng 1 gộp mọi lựa chọn, clip tự chọn theo bốn câu, bước nhẹ 0·7·8, "Xong khi" 7 dòng)
  - [ ] video-style-edit
  - [ ] podcast-style-edit
  - [ ] cat-highlight-video
  - [ ] hoc-video-mau
  - [ ] 3 file não
- [ ] Bước 4: chạy thử một việc thật, David chấm, sửa đúng một chỗ
