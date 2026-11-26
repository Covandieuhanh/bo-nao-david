---
name: quy-tac-goi-y-de-david-chon
description: "Nhận tài nguyên, trả kết quả: đã có quy trình nên Claude tự làm liên tục theo mặc định skill, ghi \"đã chọn X vì Y\" trong báo cáo, không hỏi (2026-11-11, 14/11; sửa 26/11)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 241f9930-2980-493a-b016-898308dc0f47
  modified: 2026-11-14
---

Từ 26/11/2026 sản phẩm từ tài nguyên đã có quy trình nên Claude không trình 4 phần, tự làm trọn ([[quy-tac-duyet-ke-hoach-4-phan]]). Trước đó (14/11): với sản phẩm làm từ tài nguyên David đưa (video, highlight, podcast, bài đăng), trước khi làm, Claude trình 4 phần gọn theo mặc định skill kèm đề xuất
"chọn X vì Y", rồi chờ David "duyệt" ([[quy-tac-duyet-ke-hoach-4-phan]]). Điểm skill đã định thì Claude làm đúng skill, không đưa vào câu hỏi; điểm chưa
định thì Claude tự chọn; câu David không trả lời, "làm đi", "theo skill" đều có nghĩa là theo mặc định skill và đề xuất của Claude. Sau khi duyệt, Claude làm liên tục,
**không hỏi giữa chừng**; Claude báo "đã chọn X vì Y" ở báo cáo cuối để David sửa ở bản cuối. Claude chỉ dừng khi đăng, gửi, xoá hoặc gặp tín hiệu nặng.

**How to apply:** đề xuất không bao giờ trái với mặc định skill; yêu cầu nào đáp ứng được trong mặc định thì giữ mặc định (ví dụ: "tập trung vào điện
thoại" không có nghĩa là đổi khung). Liên quan [[quy-tac-tu-hoi-khi-mo-ho]], [[video-clip-ngan-dung-doc-lap]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 2 và skill `thu-thap-yeu-cau`. Ghi nhớ này giữ ngày, lời David, lý do.

## Sổ
- 06/11/2026: luật "làm đi không chốt lựa chọn, câu chưa trả lời vẫn phải hỏi".
- 11/11/2026, video cuộc gọi hợp tác: Claude đưa khung hình vào câu hỏi dù skill đã định khung là khung gốc (ngang), đề xuất đầu tiên là dọc; David
  không trả lời câu đó nên Claude lấy đề xuất của mình, làm sai skill. David: "Hạn chế hỏi những thứ theo tiêu chí nhất có thể… mục tiêu cuối
  cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong, toàn bộ quá trình làm việc nhiều lần là để chỉnh các phần ở giữa trong
  khi làm thực tế trên nhiều video thôi.", nên Claude bỏ luật 06/11; sản phẩm từ tài nguyên được làm liên tục, không hỏi.
- 14/11/2026 (việc #22): mọi việc phải trình 4 phần trước khi làm (lời David nguyên văn ở [[quy-tac-duyet-ke-hoach-4-phan]]), nên phần "không hỏi"
  chỉ còn áp dụng cho giai đoạn làm sau khi duyệt.

Gốc: khối 2 (Hành động) của tu-duy-goc.md — chốt mọi lựa chọn ở bước kế hoạch rồi thực thi một mạch thì tài nguyên vào là ra kết quả, không đứt giữa chừng.
