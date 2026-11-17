---
name: lich-dang-tuan
description: Soạn 4 bài Facebook cá nhân cho tuần tới (CN, T3, T5, T6), làm ảnh bằng ChatGPT khi không có ảnh của David, bù kho bài nền đủ 8, gửi David duyệt qua Telegram, đặt nhắc 19:45.
chrome: bat-buoc
kiem: ~/Documents/1-nghe-nghiep/bai-dang/tuan-{ngay}.md
---

Làm việc trong thư mục /Users/moon/Documents/bo-nao-david. Đọc ky-nang/chuan-muc-lam-viec.md, du-an/lich-dang-bai.md (hệ thống + sổ lịch), du-an/hinh-anh-facebook-ca-nhan.md (định vị, 4 trụ, 5 kiểu bài nền, luật ảnh), ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md và kenh.json mục lich.facebook_ca_nhan, rồi làm đúng từng bước. Đây là lịch David đã duyệt: không trình 4 phần, không hỏi lại.

1. Bốn ô cần có bài: Chủ nhật, thứ Ba, thứ Năm, thứ Sáu sắp tới (tính từ ngày của lịch). Ô đã có thư mục ~/Documents/1-nghe-nghiep/bai-dang/YYYY-MM-DD/bai.md thì giữ nguyên.
2. Ô video (T3, T6): chọn video David đã duyệt trong du-an/danh-muc-noi-dung.md chưa lên Facebook cá nhân; chữ đăng lấy nguyên văn lời David trong video hoặc từ phat-hanh.md của video (không đặt lời vào miệng David). Không có video thì dùng bài nền.
3. Ô bài viết (T5 công nghệ trụ 1 hoặc 4, CN con người trụ 2 hoặc đời thường trụ 3, xen theo tuần): soạn mới từ lời David tuần qua (python3 -I tu-dong-hoa/thu-thap-du-lieu/gom.py nếu đêm qua chưa chạy; đọc ~/Documents/2-ca-nhan/so-tay/kho-du-lieu/ và sổ nhớ). Chỉ dùng việc thật, không bịa ca, không bịa số; chuyện người khác ẩn danh; không nêu đơn vị phía sau, không nhắc vai điều hành; không tài chính, không chuyện sang Đức. Không đủ nguyên liệu thì lấy bài nền đúng trụ.
4. Bài nền lấy ra: chuyển file từ kho-bai-nen/ sang thư mục ngày đăng (bai.md). Soạn bù cho kho đủ 8 bài, đủ 5 kiểu, đánh số tiếp theo; cập nhật bảng "Kho bài nền" trong du-an/lich-dang-bai.md.
5. Ảnh: bài nào không có video hay ảnh của David thì tạo ảnh bằng ChatGPT trên Chrome (chatgpt.com, tab mới) theo luật ảnh mục 5 của hồ sơ (ảnh chân thực như ảnh thật + lớp motion graphics, dùng đúng câu lệnh mẫu), dòng "Ảnh:" đầu file bài chỉ là ý nội dung. Lấy ảnh: bấm ảnh để mở khung xem, bấm nút tải (mũi tên xuống, góc trên phải); 30 giây chưa thấy file mới trong ~/Downloads thì chụp đúng vùng ảnh trong khung xem bằng computer zoom có save_to_disk (ra ~700×870, đủ cho Facebook). Chuyển vào thư mục ngày đăng tên anh.png, xem lại ảnh: có chữ hay số, sai bối cảnh Việt Nam, đồ hoạ không nói đúng ý bài, trông giả hay kém chuyên nghiệp thì tạo lại tối đa 2 lần. Chrome chưa đăng nhập ChatGPT hay tạo hỏng thì ghi "cần ảnh", không đăng nhập thay David.
6. Ghi sổ lịch (bảng "Sổ lịch" trong du-an/lich-dang-bai.md, chỉ tên bài, không chép cả bài) với trạng thái "đã gửi duyệt". Viết bản tóm ~/Documents/1-nghe-nghiep/bai-dang/tuan-{ngay}.md (4 ô, đường dẫn bài, ảnh, ghi chú).
7. Gửi David qua Telegram: mỗi bài một tin bằng bash tu-dong-hoa/so-tay/bao-cao.sh --chi-gui --anh <anh.png hoặc bỏ nếu không có> "📅 <thứ, ngày> 20:00 · <trụ>\n\n<chữ đăng>"; tin cuối: "Anh trả lời 'duyệt tuần' hoặc 'sửa bài <ngày>: …'". Không đăng lên mạng xã hội, không gửi cho ai khác.
8. Thêm vào ~/Documents/2-ca-nhan/so-tay/nhac-viec.md mỗi ô một dòng "- YYYY-MM-DD 19:45 · Đến giờ đăng Facebook cá nhân lúc 20:00: bài <thứ, ngày> (chữ + ảnh trong tin 📅 gửi sáng thứ 6). Video thì lấy ở <đường dẫn>. Đăng xong nhắn 'đã đăng'". Không thêm trùng dòng đã có.
9. Cuối việc: báo bằng bash tu-dong-hoa/so-tay/bao-cao.sh "✅ Xong: lịch đăng tuần … · Còn lại: …" rồi đẩy GitHub bằng bash tu-dong-hoa/dong-bo.sh --push (bài và ảnh nằm ngoài repo, không đưa lên). Trả lời tiếng Việt, ngắn.
