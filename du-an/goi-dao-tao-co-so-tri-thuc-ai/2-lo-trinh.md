---
description: "Gói 2 dựng bộ não bằng file cho AI, phần 2 lộ trình trainer: 4 buổi, mục tiêu học viên tự hoàn thành trọn vòng học mà không cần trainer và bộ não đã trải qua ít nhất 3 dự án thực tế."
---

# 2. Lộ trình trainer

## Mục tiêu (cam kết của gói)
Học viên **tự hoàn thành trọn một vòng học (làm dự án, lưu bằng sáu câu hỏi, biến lỗi thành câu kiểm, kiểm bằng người đọc mới) mà không cần trainer**, và **bộ não đã trải qua ít nhất 3 dự án thực tế**. Một AI mới hoàn toàn đọc bộ não và trả lời đúng ít nhất 90% bài kiểm có ít nhất 10 câu. Chưa đạt thì trainer tiếp tục kèm cặp.

## Kế hoạch: 4 buổi kèm riêng (một trainer, một học viên), online, mỗi buổi 90 phút, khoảng 4 tuần
| Buổi | Bài | Kết quả |
|---|---|---|
| 1 | 1, 2 | thư mục bộ não, bốn file gốc, hồ sơ viết qua phỏng vấn; AI mới tóm đúng 3 dòng về học viên |
| 2 | 3, 4 | trục bốn tầng; dự án thực tế đầu tiên được lưu bằng sáu câu hỏi |
| 3 | 5, 6 | bài kiểm đầu tiên (ít nhất 5 câu từ lỗi thực tế, đủ 10 câu trước buổi 4); một lần nhìn lại tuần |
| 4 | 7, 8 + nghiệm thu | đợt nâng cấp đầu tiên có đo trước và sau; sao lưu; người đọc mới đúng ít nhất 90% |
| Kèm tới khi đạt | nhắn tin | đủ 3 dự án thực tế, học viên tự hoàn thành một vòng học |

Giữa hai buổi: học viên dùng bộ não cho công việc thực tế của mình, gửi sổ dự án và câu kiểm mới; trainer phản hồi trong 24 giờ.

## Quy trình cho một học viên
1. **Kiểm đầu vào** (15 phút): học viên đang dùng AI nào, đã có chức năng Projects chưa, đã có máy tính chưa, dùng mấy thiết bị. Nếu chưa có AI phù hợp thì trainer hướng dẫn chọn trước buổi 1.
2. **Phiếu khảo sát đầu vào** (`4-phieu-khao-sat-va-nghiem-thu.md`).
3. **4 buổi** theo `3-giao-trinh.md`, mỗi buổi ghi: đã làm gì · kết quả · vấn đề · bài tập.
4. **Nghiệm thu**: học viên tự chạy bài kiểm người đọc mới trước mặt trainer, trainer chỉ quan sát.
5. **Sau gói**: lời chứng thực và số liệu trước, sau.

## Chuẩn mực khi kèm cặp (trainer tuân thủ)
- Học viên tự gõ, tự quyết định. Trainer không viết hồ sơ thay, không dán bộ não của mình cho học viên chép.
- Nội dung bộ não là thông tin riêng của học viên. Trainer chỉ xem cấu trúc (tầng, vị trí đặt, liên kết, câu kiểm), chỉ đọc nội dung khi học viên cho phép.
- Trainer không xem và không nhận mật khẩu, mã đăng nhập của học viên.

## Thực thi: trainer chuẩn bị trước khách hàng đầu tiên
- [x] Bộ biểu mẫu ([bo-bieu-mau/](bo-bieu-mau/README.md)): từ mới và thao tác thủ công, mẫu file, câu lệnh mẫu, mẫu bài kiểm, danh sách kiểm soát chất lượng.
- [x] Một AI chưa đọc gì đóng vai người mới làm thử từ bước 0 tới bước 9 (21/11): lần 1 chấm 4/10, vướng mắc ở thao tác thủ công; đã thêm biểu mẫu 00, thư mục phẳng, xử lý mâu thuẫn bài kiểm. Lần 2 chấm 7/10, không còn bước bị chặn; đã sửa tiếp: thao tác quay lại bản trước và lưu trữ file, câu lệnh 1 viết luôn trạng thái, file tải về bị đổi tên, Google Drive khuyên dùng, thêm từ mới. Bước 7 và 9 ở lần đầu nên có trainer ngồi cạnh.
- [ ] Thử trọn 10 bước ở mức cơ bản trên ChatGPT và trên Claude, mỗi nơi một tài khoản mới hoàn toàn.
- [ ] Thử mức nâng cao trên một máy mới hoàn toàn (Claude Code hoặc Codex, kèm GitHub).
- [ ] Kết quả mẫu để demo: bộ não của trainer (chỉ cho xem cấu trúc và một bài kiểm người đọc mới, không cho chép nội dung).
- [ ] Chốt giá, thời gian kèm cặp tiếp tối đa, bán riêng hay kèm gói 1.
- [ ] Học viên thử nghiệm đầu tiên (`../pheu-ban-hang-goi-cong-nghe.md`).
