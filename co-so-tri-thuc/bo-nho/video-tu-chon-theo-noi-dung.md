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

**Why:** kho hiệu ứng học nhiều nhưng không có bước "dấu hiệu → kiểu", nên Claude chỉ dùng vài kiểu quen; thử-sai bằng render và mổ xẻ
lỗi skill giữa chừng làm chậm.

**How to apply:** luật ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/tu-chon.md` (chẩn đoán `chan-doan.py` → khung chủ thể `khung-chu-the.py`,
bảng ghi chú chạy `GHI_CHU`, kiểu cảnh theo dạng câu) và mục "Nhịp làm" của `dung-video-theo-phong-cach/SKILL.md`. Học mẫu mới phải thêm dòng
dấu hiệu vào tu-chon.md. Liên quan [[quy-tac-goi-y-de-david-chon]], [[video-tham-my-chi-giu-nhan-dien]].
