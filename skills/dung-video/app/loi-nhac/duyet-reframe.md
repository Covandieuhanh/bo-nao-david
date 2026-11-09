Bạn duyệt kế hoạch ĐỔI KHUNG ngang → dọc 9:16 cho video của David Trần (khối 04). Máy đã dò mặt, gom người A, B… (từ trái sang) và
đoán người nói từng câu. Mở bằng công cụ Read: tracks.jpg (ô màu = ai là ai) và shots.jpg (khung vàng = phần giữ lại). Đọc plan.md
(shot, người, ✓ chắc / ? chưa chắc) và lời nói. Trả `shots` = danh sách shot ĐÃ SỬA, nối liền nhau từ đầu tới cuối, mỗi shot
{start, end, target ("A"/"B"… hoặc "wide"), cx? (0–1, chỉ khi khung cắt nửa mặt), follow? (người đi lại), text?}:
- shot "?" → đọc câu nói để biết AI đang nói, đặt đúng target; nhảy cắt khi lời chuyển người (không chia đôi khung).
- người bị khung cắt nửa mặt → đặt cx; slide / cảnh rộng / vật cần thấy cả khung → "wide"; người đi lại → follow: true.
- Giữ nguyên thời lượng và mọi lời. Shot đã đúng thì giữ nguyên.

{{file:khoi/04-khung-hinh/README.md}}
