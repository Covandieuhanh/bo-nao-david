---
name: phan-tich-video-mau
description: Học cách trình bày từ một video mẫu David gửi (link YouTube/TikTok hoặc file) để BỔ SUNG vào bộ skill dựng video — chỉ học bố cục, thứ tự hiện, cách nối cảnh, nhịp, hiệu ứng âm thanh; học cả nền, kết cấu, kiểu hình, chữ nhấn làm tài nguyên sáng tạo; chỉ giữ chữ ký nhận diện (người xem nhận ra video của David) và thành phần đang có. Skill lập phiếu học, tự đưa vào skill (đụng màu chủ đạo, chữ ký nhận diện thì chờ David duyệt), rồi kiểm tra để không làm hỏng phần cũ (mặt, phụ đề, dấu góc, thanh thời gian, cả khung ngang và dọc). Dùng khi David gửi video và nói "học cái này", "học video này", "học mẫu này", "học cách họ làm", "học bố cục", "học hiệu ứng", "/phan-tich-video-mau" — kể cả khi chỉ gửi link kèm chữ "học".
---

# Học video mẫu

**Đọc trước:** `../../chuan-muc-lam-viec.md` · `../thiet-ke-bo-cuc/README.md` (mục 4 — toàn bộ luật và quy trình). Làm theo đúng thứ tự ở đó.
Skill này chỉ là **điểm vào**; không ghi luật riêng ở đây để chỉ có một nguồn duy nhất phải sửa.

## Ba điều không được quên
1. **Học là bổ sung** (bộ nhớ `quy-tac-hoc-la-bo-sung`): không xoá hay sửa nghĩa thành phần cũ. Thẩm mỹ chỉ giữ **chữ ký nhận diện**
   (`../thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0); ngoài phần đó, điều gì học được cũng có thể thêm vào.
2. **Phiếu học trước, sửa skill sau.** Điền `../thiet-ke-bo-cuc/phieu-hoc-mau.md` thành `../thiet-ke-bo-cuc/nguon-tham-khao/<ten-nguon>-<ngay>.md`,
   gửi David. Không có cổng hỏi: điểm cần chọn thì Claude tự chọn theo tiêu chí của skill, ghi "đã chọn X vì Y" trong phiếu, rồi làm tiếp; đụng màu chủ đạo, chữ ký nhận diện thì chờ "duyệt" (Đ3).
3. **Kiểm tra không làm hỏng phần cũ** trước khi dùng vào video thật: chụp đủ lớp ở cả khung ngang lẫn dọc, phần cũ phải giữ nguyên.

## Đọc kèm (ở đúng bước cần)
- `../thiet-ke-bo-cuc/bo-cuc.md`, `../thiet-ke-bo-cuc/am-thanh.md`: kho đã có, để biết điều mới có trùng với phần đã có không.
- `../quy-tac-chung.md`, `../dung-video-theo-phong-cach/references/loi-thuong-gap.md`: các quy tắc chặn đã có phải giữ.
- `../thiet-ke-bo-cuc/nguon-tham-khao/`: các nguồn đã học, mỗi nguồn một file.
- [references/nhat-ky-thay-doi.md](references/nhat-ky-thay-doi.md): sổ quyết định theo ngày kèm lý do (không đọc lúc làm việc).

## Xong khi
1. Phiếu học nằm trong `nguon-tham-khao/` và đã báo David.
2. Claude chỉ thêm vào kho; chữ ký nhận diện (màu nhấn cam, hai font chính, thành phần cố định) không đổi.
3. `bo-cuc.md` / `am-thanh.md` có dòng mới, ghi rõ "đã có code" hay "chưa có code".
4. Ảnh kiểm khung ngang và dọc đã được xem; phần cũ giữ nguyên so với ảnh trước khi thêm.
5. File mẫu đã tải (nếu có) đã xoá khỏi thư mục tạm.
6. Claude đã đẩy lên GitHub (`bash tu-dong-hoa/dong-bo.sh --push`) và báo David: thêm gì, đã kiểm gì, chưa kiểm gì.
