---
name: video-tu-chon-theo-noi-dung
description: Skill dựng phải tự chẩn đoán video rồi chọn bố cục / lớp thông tin / kiểu cảnh trong kho; video 10 phút ~1 giờ
metadata:
  node_type: memory
  type: feedback
  originSessionId: 431772fc-8289-4a77-9415-b61e35260e41
  modified: 2026-11-11T10:12:31.818Z
---

Ngày 11/11/2026, video cuộc gọi hợp tác mất 4–5 giờ để làm. David: "cái quan trọng nhất là học rất nhiều, tôi cần các skill phải tự động chọn ra
được cách nào phù hợp với nội dung của video để làm việc"; "tập trung vào điện thoại" mà Claude chỉ cắt và phóng khung hình, các chi tiết thừa vẫn còn;
video có nhiều nội dung cần motion graphic hiện nhiều thông tin hơn để người xem theo dõi.

**Why:** kho hiệu ứng đã học nhiều nhưng không có bước "dấu hiệu thì kiểu", nên Claude chỉ dùng vài kiểu quen; cách thử và sai bằng render và việc phân tích
lỗi skill giữa chừng làm chậm tiến độ.

**How to apply:** luật nằm ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/huong-dan-lua-chon.md` (chẩn đoán bằng `chan-doan.py`, rồi xác định khung chủ thể bằng `khung-chu-the.py`,
bảng ghi chú chạy `GHI_CHU`, kiểu cảnh theo dạng câu) và mục "Nhịp làm" của `ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md`. Khi học mẫu mới, Claude phải thêm dòng
dấu hiệu vào huong-dan-lua-chon.md. Liên quan [[quy-tac-goi-y-de-david-chon]], [[video-tham-my-chi-giu-nhan-dien]].

Ngày 19/11/2026, sau tập "Marketing là nỗi đau và nhu cầu": David thấy từ video ngắn đến video dài, nội dung nào cũng chỉ có một kiểu thẩm mỹ và bố cục —
"bao nhiêu cái học về bố cục và motion graphic cũng như thẩm mỹ thì không có chỗ ứng dụng vì không hề được tự động nhận diện".
Nguyên nhân gốc: kho chỉ được nối vào mẫu 1 video; tập gồm 2 file lại đi theo mẫu ghép (thiếu nửa kho, không có bước chẩn đoán, công cụ sinh cảnh chỉ viết pow), và Claude sao chép
kịch bản của bản trước. David duyệt phương án A và chốt: *"mọi thứ cần phát huy tối đa được sức mạnh của AI, mọi lựa chọn đều phải được tự động
setup phù hợp với nội dung của tài nguyên nguồn"*.
**How to apply (bổ sung):** khi có nhiều file cùng một buổi nói, Claude nối các file và dùng mẫu 1 video; mẫu ghép chỉ dùng cho vlog nhiều cảnh và clip ngắn; huong-dan-lua-chon.md
bước 0 (không sao chép tập trước, bảng mẫu) và bước 2b (thẩm mỹ); `soat-canh.mjs` chặn render khi thiếu `## Chẩn đoán` hoặc khi cả video chỉ có một kiểu.

Gốc: khối 2 (Hành động) của tu-duy-goc.md — mọi lựa chọn dựng phải được chọn tự động cho hợp nội dung của chính tài nguyên nguồn, chẩn đoán trước rồi mới chọn, không chép tập trước.

Ngày 27/11/2026, David yêu cầu tận dụng kho hiệu ứng và thẩm mỹ theo nội dung. Nguyên nhân lặp còn lại là bước chọn chỉ yêu cầu mô tả, thiếu đối chiếu ứng viên và thiếu nối lựa chọn với mã cảnh đã dựng. Bản skill cũ cài riêng cũng có quy tắc mặc định khác repo.

**Cách áp dụng:** dùng skill từ repo; đối chiếu cách thể hiện theo nhu cầu của người xem và điều kiện hình gốc. Ghi lựa chọn, ứng viên còn lại và lý do cho từng cảnh nội dung. So thẩm mỹ ở cấp video. Bộ soát đối chiếu mã cảnh với lựa chọn trước khi xuất. Người dựng xem thử để xác nhận hiệu quả trên hình. Khi học cách mới, ghi tình huống sử dụng, điều kiện khung, cách triển khai và dấu hiệu nhận biết trên hình để dùng lại trong bước chọn.

David làm rõ ngày 27/11/2026: mục tiêu là AI tự học từ kho hình mẫu và linh hoạt đưa cách kể, hiệu ứng và thẩm mỹ vào video theo nội dung.
Được tác động lên nhân vật và bố cục nếu giúp tăng sức biểu đạt. Khi người nói đang hiện, mặt phải rõ. Số loại hiệu ứng, mật độ, kiểu nền, nhịp
và cách phối lớp do người dựng tự chọn. Dùng luật chung mục 0 và 4 cùng hướng dẫn chọn bố cục bản hiện hành.
