---
description: "Quy trình lá A8: nghiên cứu hình mẫu thành công cho một mục nhỏ trước khi làm (ít nhất 5 mẫu, việc lớn 10), bóc tách yếu tố tạo nên thành công, ghi bản đồ hình mẫu và nhật ký, đối chiếu và góp ý khi giao."
---

# Nghiên cứu hình mẫu (cây quy trình lá A8)

**Khi nào dùng:** quy trình gốc bước 2 tra [bản đồ hình mẫu](README.md) mà mục nhỏ của việc chưa có hoặc chưa đủ hình mẫu; David nói
"nghiên cứu hình mẫu", "xem người ta làm thế nào", "học từ kênh lớn"; hoặc trước một sản phẩm mới (video kiểu mới, bài đăng kiểu mới,
gói, chương trình, trang). Học một video cụ thể David gửi thì dùng skill `phan-tich-video-mau`; học để sửa skill theo số liệu kênh thì dùng
`hoc-lien-tuc` Việc 2 (cả hai ghi kết quả vào cùng bản đồ này).

**Đầu vào:** việc cần làm và mục nhỏ tương ứng trong cây (mục 2 của README); chưa có mục nhỏ thì thêm.

## Các bước
1. **Xác định mục nhỏ và câu hỏi:** việc này cần học điều gì cụ thể (độ dài, cấu trúc, nhịp, cách mở, cách bán…). Một câu hỏi một lần.
2. **Tìm nhiều mẫu:** ít nhất 5, việc lớn ít nhất 10; trộn quốc tế và Việt Nam cùng lĩnh vực hoặc cùng nhóm khách hàng mục tiêu của David. Ưu tiên mẫu
   có bằng chứng kiểm chứng được:
   - Kênh video: `yt-dlp --flat-playlist -I 1:10 --print "%(id)s|%(duration)s|%(view_count)s|%(title)s" "<kênh>/videos"`, so trung vị
     lượt xem với số người theo dõi; tìm theo chủ đề: `yt-dlp --flat-playlist --print … "ytsearch10:<từ khoá>"`.
   - Sản phẩm, gói, chương trình: trang chính thức, giá công bố, số học viên, đánh giá công khai.
   - Web search cho số liệu chung; ưu tiên số đo trực tiếp hơn bài hướng dẫn.
3. **Xem đúng phần cần, tốn ít tài nguyên:** với video, người làm chỉ tải đoạn cần (`--download-sections "*0-100"`, 480p), xem bằng lưới mỗi giây một khung hình
   (`ffmpeg -i <file> -vf "fps=1,scale=192:-2,tile=10x10" -frames:v 1 <ra>.jpg`); đếm cắt cảnh khi cần nhịp
   (`select='gt(scene,0.3)'`). Học xong thì người làm xoá file tải về.
4. **Bóc tách:** với mỗi mẫu, người làm ghi yếu tố tạo nên thành công (không phải hiệu ứng rời chỉ để trang trí); rồi tìm điểm chung của nhiều mẫu thành nguyên lý; điểm
   riêng phù hợp với David thành điều cải tiến. Mẫu nào kém hoặc rối thì ghi vào "không lấy" kèm lý do.
5. **Ghi lại:** mỗi mẫu một dòng ở bảng mục nhỏ (file mục lớn), đổi trạng thái mục nhỏ trong README; một mục [nhat-ky.md](nhat-ky.md)
   (ngày, câu hỏi, số mẫu, kết luận, áp dụng vào đâu). Phiếu học dài để ở file nghiên cứu của skill liên quan, bản đồ đặt liên kết.
6. **Áp dụng:** người làm đưa kết luận vào 4 phần của việc (điểm cần chốt có đề xuất theo hình mẫu). Đưa vào skill / luật thì qua 4 phần như mọi
   lần sửa skill.
7. **Đối chiếu khi giao:** 2–3 dòng "so với hình mẫu" trong tin báo cáo cuối: giống ở đâu, khác ở đâu, nên chỉnh gì tiếp.

## Điểm duyệt
Không có cho phần nghiên cứu và ghi bản đồ (phần chuẩn bị, trước Đ1 của việc chính). Đưa kết luận vào skill, luật: Đ1 của việc chính.

## Xong khi
- Mục nhỏ có ít nhất 5 hình mẫu (việc lớn 10), mỗi dòng đủ bốn cột, có ngày đo; trạng thái mục nhỏ trong README đã cập nhật.
- Nhật ký có mục mới; file tải về đã xoá.
- Kết luận đã vào 4 phần hoặc vào kết quả; tin bàn giao có 2–3 dòng đối chiếu.

## Kiểm gì
- Bằng chứng là số kiểm chứng được (có ngày, có cách đo), không phải cảm nhận.
- Không sao chép nội dung, nhận diện, logo của người khác; chữ trên video vẫn là lời David.

## Lỗi thường gặp
- Một số kênh đổi tên đường dẫn (`@ten`): tìm lại bằng `ytsearch` theo tên kênh.
- Trang chặn công cụ tải tự động (bước xác minh chống bot, yêu cầu đăng nhập): người làm không vượt qua; dùng nguồn khác hoặc nhờ David.
