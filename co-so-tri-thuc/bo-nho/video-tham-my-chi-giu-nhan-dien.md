---
name: video-tham-my-chi-giu-nhan-dien
description: "Về thẩm mỹ, Claude chỉ giữ chữ ký nhận diện, ngoài phần đó được sáng tạo tự do; hiểu hơn cầu kì: kho hiệu ứng để lựa chọn, mỗi video dùng ít kiểu, bỏ hiệu ứng chữ sau người / bóng người (10/11; gộp 15/11)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 39383a2e-bf70-432e-8fcc-63c950a840d4
  modified: 2026-11-10T11:34:16.992Z
---

David 10/11/2026: "Về thẩm mỹ thì tôi chỉ cần duy nhất 1 thứ là người xem có thể nhận diện được dù xem video nào cũng là của cùng 1 người làm là được, còn việc sáng tạo để phù hợp nội dung thì thoải mái" và "càng nhiều tài nguyên để tùy ý sáng tạo càng tốt".

**Why:** trước đó, luật học mẫu cấm đổi màu, font, nét vẽ, nền, nên khi học Ali Abdaal / Joseph Video Editing, Claude phải bỏ nhiều thành phần hay (chữ nghiêng nhấn, nền hạt, nền người mờ). David nới luật: chỉ cần người xem nhận ra được video là của David.

**How to apply:**
- Chữ ký nhận diện (giữ cố định) được ghi ở một nguồn duy nhất: `ky-nang/san-xuat-video/thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0: bộ nhận diện chung (dấu góc, phụ đề, thanh, màn chốt, thẻ cuối) với màu cam, hai font chính, nhạc kênh.
- **Hiệu ứng học từ hình mẫu giữ trọn thẩm mỹ của mẫu** (David 28/11/2026): màu, font, tỉ lệ chữ, bo góc, bóng, khoảng trống, vị trí so với người; không phối lại sang đen cam. Cam chỉ thay chỗ nhấn mẫu đã có. **Why:** trong bản xem kho hiệu ứng, cảnh giữ nguyên mẫu nền sáng hiển thị chuẩn, còn cảnh phối lại đen cam thì lỗi thẩm mỹ và che mặt.
- Ngoài chữ ký nhận diện: nền, kết cấu, kiểu hình, chiều sâu, bố cục, chuyển động được chọn theo nội dung từng video.
- Học video mẫu: Claude rút đủ cả phần thẩm mỹ làm tài nguyên, không chỉ rút bố cục. Claude vẫn giữ mọi quy tắc chặn cũ ([[quy-tac-hoc-la-bo-sung]]) và chữ nguyên văn ([[video-chu-nguyen-van]]).
- Tự do nhưng **hiểu hơn cầu kì**: Claude chọn ít kiểu phù hợp nội dung (xem mục gộp bên dưới).
- Liên quan [[quy-tac-noi-dung-cua-david]], [[video-bo-cuc-tu-can-bang]] (phần "giữ thẩm mỹ" cũ của hai ghi nhớ này đã được viết lại theo luật 10/11), [[video-nhan-dien-chung]], [[video-do-hoa-ke-chuyen]].

## Gộp từ `video-tham-my-chi-giu-nhan-dien` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

Mỗi video chỉ dùng vài kiểu hiệu ứng phù hợp nội dung nhất, do Claude tự cân đối. Thước đo là người xem hiểu nhanh hơn, không phải video trông cầu kì. Khi hình bị rối hoặc lỗi, Claude bớt hiệu ứng đi, không thêm vào.

**Why:** ngày 10/11/2026 David xem ảnh thử các thành phần mới học từ Ali Abdaal / Joseph và nhận xét: "hiệu ứng chữ sau người là không cần đâu, nhiều hiệu ứng quá là bị rối, nhìn ảnh toàn lỗi" và "học nhiều là để ứng dụng cho phù hợp với tuỳ mỗi loại nội dung chứ không cần phải nhét hết tất cả vào cùng 1 video… quan trọng nhất là truyền tải cho người xem hiểu chứ không phải là cầu kì".

**How to apply:**
- Luật nằm ở `ky-nang/san-xuat-video/quy-tac-chung.md` §0 "Hiểu hơn cầu kì"; bước rà soát ở khối 17 ("video có rối không").
- **Chữ sau người và bóng người (tách người khỏi nền): David không dùng.** Mã nguồn đã được gỡ; các lần học mẫu sau không thêm lại.
- Khi học mẫu, Claude vẫn lấy nhiều (`video-tham-my-chi-giu-nhan-dien`), nhưng khi dựng thì chọn ít. Luật không lặp kiểu ([[video-do-hoa-ke-chuyen]], khối 07) chỉ để tránh nhàm chán, không phải để thêm kiểu.
- Đưa ảnh thử cho David: Claude chỉ gửi khi ảnh đã hết lỗi, không gửi ảnh còn lỗi hình.

Gốc: khối 4 (R&D) của tu-duy-goc.md — bản chất của thẩm mỹ kênh là người xem nhận ra cùng một người làm, nên chỉ giữ cứng chữ ký nhận diện và tự do phần còn lại.
