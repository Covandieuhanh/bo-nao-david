---
name: quy-tac-hoc-la-bo-sung
description: Học video mẫu mới là BỔ SUNG vào skill, không thay thế những gì David đã sửa; học NGUYÊN LÝ để cải tiến phần đang có, không sao chép từng hiệu ứng rời (20/11); thông số của khung dọc không dùng cho khung ngang (2026-11-08)
metadata:
  type: feedback
---

Điều học từ mẫu mới (bố cục, trình bày, âm thanh) chỉ được **thêm** vào skill. Claude không xoá, không thay những thứ David đã chốt hoặc đã sửa nhiều lần (dấu góc, không đè chữ, thanh thời gian, phụ đề…).

**Why:** 08/11/2026 David xem 4 video cũ được làm lại, thấy dấu góc đè hình, điểm nhấn chồng lên dấu góc, thiếu thanh thời gian, dấu góc thấp. David nói "học là bổ sung chứ không phải thay thế đi các thứ trong skill đã xây dựng". Khi tra lại, nguyên nhân gốc của lỗi là mẫu viết cho khung dọc được áp sang khung ngang có người nói lần đầu (chi tiết ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/loi-thuong-gap.md`).

"Bổ sung" gồm cả thẩm mỹ (nền, kết cấu, kiểu hình, chữ nhấn); chỉ giữ chữ ký nhận diện: [[video-tham-my-chi-giu-nhan-dien]] (10/11/2026).

**Học nguyên lý, không sao chép từng hiệu ứng rời (20/11/2026).** David: *"học để tự động áp dụng chứ không phải hoàn toàn là áp dụng một cách máy móc y
chang… học để cải tiến trên chính những gì mình đang có… trong 1 video cũng không cần quá nhiều motion graphics… ngày càng thể hiện được
rõ sự mô tả các nội dung đang được nói đến… nhưng vẫn phải đảm bảo sự tinh gọn và đơn giản chứ không cầu kỳ, loè loẹt gây phân tán sự chú ý"*.
Lý do: phiếu học đầu tiên của video Cường Mê AI liệt kê 9 hiệu ứng mới; David muốn biết vì sao video đó dễ hiểu rồi nâng cấp chính các thành phần đang có.
Luật hiện hành: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4a (ý nào cần hình, năm nguyên lý).

**How to apply:**
- Phiếu học trả lời trước câu "vì sao mẫu này dễ hiểu" (nguyên lý), rồi xác định mỗi nguyên lý nâng cấp thành phần nào đang có. Hiệu ứng rời chỉ để trang trí thì ghi vào "Không lấy".
- Trước khi thêm điều gì từ bài học: đọc luật và gotchas liên quan, giữ nguyên các quy tắc chặn đã có, thêm quy tắc chặn mới cho thành phần mới (ví dụ thành phần mới phải tránh dấu góc, phụ đề, thanh thời gian).
- Khi khung mới (ngang/dọc) chạy lần đầu: chụp đủ lớp (cảnh, phụ đề, dấu góc, thanh thời gian) trước khi render, không chỉ chụp lớp cảnh.
- Khi David gửi video mẫu để học: dùng skill `phan-tich-video-mau` (điểm vào), rồi theo quy trình 10 bước ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` mục 4: phiếu học David duyệt trước, kiểm tra không làm hỏng phần cũ sau (David chọn phương án A, 08/11/2026).
- Khi David góp ý mà bảo không render lại: Claude chỉ sửa skill, chụp thử ảnh để kiểm. Liên quan [[video-gop-y-render-lai]], [[video-bo-cuc-tu-can-bang]].

Gốc: khối 3 (Học và thay đổi) của tu-duy-goc.md — học mới là nối vào cái đã đúng, học nguyên lý để cải tiến; thay thế cái David đã sửa là làm mất bài học cũ.
