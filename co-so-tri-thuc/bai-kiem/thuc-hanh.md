---
description: "Các ca thực hành để kiểm chất lượng đầu ra giữa các thiết bị, mô hình trí tuệ nhân tạo và phiên mới: dựng video, tiếp quản công việc và trình kế hoạch."
---

# Thực hành trên cùng chuẩn chất lượng

Người tổ chức sao chép lời giao và tài liệu đầu vào cho mỗi phiên mới. Dặn phiên thử tra quy trình từ repo và để người chấm giữ tài liệu này, phiếu chấm và bản chuẩn đến khi nộp. Chạy trong thư mục thử riêng, với đầu vào chỉ đọc. Lưu sản phẩm thử và phiếu chấm ở nơi làm việc của David.

1. Ghi phiên bản GitHub, định danh đầu vào, lời giao, ngày, thiết bị, ứng dụng, gói hoặc mô hình thực tế, công cụ và quyền cần cho việc. Cho các phiên cùng đầu vào, quyền phù hợp và phiên bản quy trình.
2. Lấy một lần chạy làm mốc. Giữ AI cố định và đổi thiết bị. Sau đó giữ thiết bị cố định và đổi AI. Muốn kiểm theo thời gian thì chạy lại trong phiên mới với cùng cấu hình. Chỉ kết luận cho những cấu hình đã chạy.
3. Với mỗi tiêu chí bắt buộc, ghi Đạt, Chưa đạt hoặc Chưa kiểm, kèm bằng chứng. Một lần chạy đạt chuẩn khi tất cả tiêu chí bắt buộc đạt. Hai lần chạy tương đương về chuẩn khi cả hai đạt độc lập. Chấm giá trị tăng thêm sau bước này và nêu cụ thể lợi ích thấy được trong đầu ra.
4. Ghi số lần David phải nhắc lại thông tin đã có, số vòng sửa lỗi và đầu ra có đạt ngay lần đầu không. Nếu lệch, ghi chứng cứ và nguyên nhân có khả năng nhất (truy xuất, quy trình, công cụ hoặc thực thi), rồi chạy lại ca đó sau khi sửa đúng nguồn.

## Ca 1. Dựng video từ tài nguyên được duyệt dùng thử

**Đầu vào:** chọn một đoạn ngắn David tự quay có ít nhất một câu mang điều kiện hoặc phủ định và một chi tiết trên màn hình cần giữ rõ. Dùng cùng tệp nguồn cho mọi lần. Người chấm ghi trước mốc câu và vùng hình cần giữ, lấy một bản David đã duyệt cùng loại làm mốc về nhận diện và chất lượng. Có thể dùng bộ thử thiết bị sẵn có nếu đoạn nguồn đáp ứng hai điều kiện trên.

**Lời giao:** “Dựng đoạn này theo quy trình dựng video tự quay. Giao bản xem được, phụ đề và ghi chú kiểm tra trong thư mục thử. Chỉ bàn giao trong thư mục này.”

| Tiêu chí bắt buộc | Bằng chứng để chấm |
|---|---|
| Chọn đúng quy trình và có đầu ra dùng được trong thư mục thử | Bản dựng phát được, có phụ đề và ghi chú kiểm tra |
| Giữ trọn ý và lời gốc | Nghe đối chiếu câu đã đánh dấu và các điểm nối, đọc phụ đề tại các mốc đó |
| Đồ họa giữ rõ người và chi tiết đang truyền tải thông tin | Xem trước, trong và sau mỗi lần đồ họa xuất hiện ở vùng đã đánh dấu |
| Âm thanh, phụ đề và nhận diện đạt chuẩn | Đối chiếu các tiêu chí âm thanh, phụ đề và nhận diện trong mục “Xong khi” của [skill dựng video](../../ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) với bản cuối và mốc kiểm tra |

**Giá trị tăng thêm:** ghi một mốc mà cách minh họa hoặc nhịp xuất hiện giúp hiểu ý nhanh hơn, cùng lý do người chấm quan sát được. Dùng [bộ kiểm kỹ thuật thiết bị](../../tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh) để khoanh vùng nếu có lệch về công cụ dựng.

## Ca 2. Tiếp quản việc đang dở trong phiên mới

**Đầu vào:** chuẩn bị ba tệp thử theo nội dung sau. Đặt trong thư mục thử của mỗi phiên cùng một bản bộ não.

- `trang-thai.md`: “Việc V-01. Bản 1 đã qua kiểm tra kỹ thuật. Bước tiếp theo theo ghi chú ngày 24/11 là chuẩn bị gói đăng. Xem `so-video.md` để biết trạng thái từng bản.”
- `so-video.md`: “Việc V-01, ngày 26/11. David đã duyệt bố cục bản 2. Bản 1 đã được thay thế. Bản 2 còn kiểm phụ đề ở 00:12 và chưa chốt toàn bộ. Lời gốc đã đối chiếu: ‘Chỉ mở rộng khi đội hiện tại đã làm ổn định.’”
- `phu-de-ban-2.srt` có một mục ở 00:12 với nội dung “Mở rộng khi đội hiện tại đã làm ổn định.”

**Lời giao:** “Làm tiếp việc video đang dở theo hồ sơ trong thư mục thử. Cập nhật lại việc đã làm để phiên sau tiếp tục được.”

| Tiêu chí bắt buộc | Bằng chứng để chấm |
|---|---|
| Xác định đúng bản và bước tiếp theo | Báo cáo dẫn sổ video ngày 26/11, chọn bản 2 và bước kiểm phụ đề ở 00:12 |
| Thực hiện bước đang mở | Tệp phụ đề bản 2 khôi phục chữ “Chỉ”, giữ nguyên thời gian |
| Phân biệt các mức duyệt | Sổ video ghi đã sửa phụ đề, bố cục đã duyệt và toàn bộ bản 2 còn chờ chốt |
| Có thể bàn giao qua phiên mới | Báo cáo nêu thay đổi, căn cứ và bước còn lại; thực hiện được mà David không phải cung cấp lại dữ liệu |

**Giá trị tăng thêm:** ghi nếu AI giải thích được tác động của từ “Chỉ” đối với ý của David hoặc để lại ghi chú bàn giao giúp người sau kiểm nhanh.

## Ca 3. Giao bản kế hoạch trong phiên mới

**Lời giao:** “Lên kế hoạch chuẩn hóa toàn bộ tên tệp và mô tả trong bộ não theo hệ thuật ngữ hiện hành.”

| Tiêu chí bắt buộc | Bằng chứng để chấm |
|---|---|
| Trình đúng cấu trúc | Bốn đề mục theo thứ tự Mục tiêu, Kế hoạch, Quy trình, Thực thi |
| Đặt được tiêu chí nghiệm thu | Mục tiêu nêu phạm vi rà soát và cách xác nhận tên, mô tả, tham chiếu đều đúng |
| Phân biệt kế hoạch và việc đã làm | Thực thi nêu hành động tiếp theo và cách kiểm tra. Cây Git chưa có thay đổi do việc đổi tên |
| Áp dụng đúng phạm vi | Một lời giao tương tự cho việc đã có quy trình vẫn nhận bản kế hoạch đủ bốn phần khi yêu cầu rõ đầu ra là kế hoạch |

## Ca 4. Trao đổi rồi chuyển sang việc có đầu ra

**Lời giao thứ nhất:** “Trao đổi thôi. Tôi đang phân vân vì sao người xem chưa hiểu phần mở đầu.”

**Lời giao thứ hai:** “Bây giờ hãy lập bản kế hoạch cải thiện đoạn mở đầu.”

| Tiêu chí bắt buộc | Bằng chứng để chấm |
|---|---|
| Tiếp nhận đúng ngữ cảnh | Lời đầu được xử lý như đối thoại để làm rõ, có bóc tách thông tin phù hợp và chưa thay đổi đầu ra. |
| Chuyển đúng chế độ | Lời thứ hai nhận bản kế hoạch với Mục tiêu, Kế hoạch, Quy trình, Thực thi theo thứ tự. |
| Đặt mục tiêu rõ | Kế hoạch nêu người xem cần hiểu gì và dùng bằng chứng nào để xác nhận. |

## Ca 5. Việc lớn có việc nhỏ

**Lời giao:** “Trong phần Thực thi của việc chuẩn hóa bộ não có việc lập danh mục đường dẫn. Hãy làm riêng việc lập danh mục tên tệp Markdown trong một thư mục thử đã được cung cấp.”

| Tiêu chí bắt buộc | Bằng chứng để chấm |
|---|---|
| Phân cấp mục tiêu | Nêu cách danh mục phục vụ việc lớn và tiêu chí riêng của danh mục trước khi bóc tách. |
| Thực hiện đúng phạm vi | Danh mục khớp tệp Markdown trong thư mục thử, gồm đường dẫn và mô tả tại mỗi tệp khi có. |
| Bàn giao kiểm được | Ghi số tệp, cách đối chiếu và phần còn thiếu mô tả nếu có. |

## Phiếu ghi kết quả

| Ca | Phiên bản, đầu vào | Thiết bị, AI, ngày | Chuẩn bắt buộc và bằng chứng | Giá trị tăng thêm | Lần nhắc / vòng sửa / đạt lần đầu |
|---|---|---|---|---|---|
| | | | | | |
