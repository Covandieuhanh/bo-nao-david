---
name: video-chu-nguyen-van
description: "Mọi chữ trên video là nguyên văn lời David và chỉ cho nội dung: không thẻ tít tự rút ý, màn chốt không tự viết, không số chạy, không nhãn kỹ thuật ×1,6 / slow-mo (07/11; gộp 15/11)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbdca2f7-d150-4f29-9b51-a450fb69af85
  modified: 2026-11-07T11:46:51.064Z
---

Motion graphics dùng loại nào cũng được, nhưng **không được sáng tạo sai lời chính xác của David**:
- Không làm thẻ tít mở đầu mặc định — tít tự rút ý có thể chưa đúng điều David muốn truyền tải.
- Chữ trên màn hình = cụm nguyên văn liền mạch trong lời; được tách thành nhiều mảnh, không được bỏ chữ làm đổi nghĩa (ví dụ: bỏ "muốn" trong "không muốn làm một mình").
- Màn chốt dùng câu David nói ở cuối video, không dùng câu Claude tự viết.
- Không dùng số chạy (từ 0 đến 60) vì khung giữa hiện số David không nói; liệt kê đúng các con số David nói.

**Why:** 07/11/2026 video "Đi bộ hằng ngày": thẻ tít bị cắt dòng ở khung ngang và David thấy tít có thể lệch ý; soát lại còn 4 chỗ chữ lệch lời.

**How to apply:** soát từng chữ đồ hoạ với phu-de.js cùng mốc trước khi render. Câu hỏi "Vấn đề / Kết quả" tự viết chỉ để ở bài đăng, bình luận ghim — không lên video. Liên quan [[quy-tac-noi-dung-cua-david]], [[video-do-hoa-ke-chuyen]].

## Gộp từ `video-chu-nguyen-van` (15/11/2026, tự học tuần: giảm ghi nhớ về 40)

Không hiện nhãn tốc độ hay ghi chú kỹ thuật trên video (×1,6, ×0,5, "tua nhanh", "slow-mo", "xem chậm"). Hiệu ứng tua nhanh/phát chậm vẫn dùng, chỉ không chú thích.

**Why:** người dùng thấy các ghi chú kỹ thuật thừa, chữ trên màn hình chỉ nên phục vụ nội dung.
**How to apply:** nhà của luật `ky-nang/san-xuat-video/quy-tac-chung.md` mục 4 (Hình); cách làm ở `ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/nhieu-doan-video.md`, template bỏ `speed`. Áp cho mọi video, cả khi tự viết component mới.
