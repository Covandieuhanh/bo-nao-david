---
name: video-tu-chon-theo-noi-dung
description: Skill dựng phải tự chẩn đoán video rồi chọn bố cục / lớp thông tin / kiểu cảnh trong kho; video 10 phút ~1 giờ
metadata:
  node_type: memory
  type: feedback
  originSessionId: 431772fc-8289-4a77-9415-b61e35260e41
  modified: 2026-11-11T10:12:31.818Z
---

11/11/2026, video cuộc gọi hợp tác mất 4–5 giờ. David: "cái quan trọng nhất là học rất nhiều, tôi cần các skill phải tự động chọn ra
được cách nào phù hợp với nội dung của video để làm việc"; "tập trung vào điện thoại" mà Claude chỉ cắt-phóng khung, rác vẫn còn;
video nhiều nội dung cần motion graphic hiện nhiều thông tin hơn để người xem theo dõi.

**Why:** kho hiệu ứng học nhiều nhưng không có bước "dấu hiệu thì kiểu", nên Claude chỉ dùng vài kiểu quen; thử-sai bằng render và mổ xẻ
lỗi skill giữa chừng làm chậm.

**How to apply:** luật ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/huong-dan-lua-chon.md` (chẩn đoán `chan-doan.py` → khung chủ thể `khung-chu-the.py`,
bảng ghi chú chạy `GHI_CHU`, kiểu cảnh theo dạng câu) và mục "Nhịp làm" của `ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md`. Học mẫu mới phải thêm dòng
dấu hiệu vào huong-dan-lua-chon.md. Liên quan [[quy-tac-goi-y-de-david-chon]], [[video-tham-my-chi-giu-nhan-dien]].

19/11/2026, sau tập "Marketing là nỗi đau và nhu cầu": David thấy video ngắn đến dài, nội dung nào cũng một kiểu thẩm mỹ và bố cục —
"bao nhiêu cái học về bố cục và motion graphic cũng như thẩm mỹ thì không có chỗ ứng dụng vì không hề được tự động nhận diện".
Gốc: kho chỉ nối vào mẫu 1 video; tập 2 file đi mẫu ghép (thiếu nửa kho, không bước chẩn đoán, máy sinh chỉ viết pow), Claude chép
kịch bản bản trước. David duyệt đường A và chốt: *"mọi thứ cần phát huy tối đa được sức mạnh của AI, mọi lựa chọn đều phải được tự động
setup phù hợp với nội dung của tài nguyên nguồn"*.
**How to apply (bổ sung):** nhiều file cùng buổi nói thì nối file, mẫu 1 video; mẫu ghép chỉ cho vlog nhiều cảnh + clip ngắn; huong-dan-lua-chon.md
bước 0 (không chép tập trước, bảng mẫu) + bước 2b (thẩm mỹ); `soat-canh.mjs` chặn render khi thiếu `## Chẩn đoán` hoặc cả video một kiểu.
