---
description: "Gói 2 dựng bộ não bằng file cho AI, phần 3 giáo trình 8 bài: mục tiêu, nội dung, thực hành, bài tập, xong khi."
---

# 3. Giáo trình: 8 bài dựng bộ não bằng file cho AI

Mỗi bài: **Mục tiêu · Nội dung · Thực hành · Bài tập · Xong khi**. Học viên làm trên chính đời và việc của mình. Biểu mẫu dùng trong bài: [bo-bieu-mau/](bo-bieu-mau/README.md).

| Bài | Tên | Buổi | Bước trong quy trình | Biểu mẫu |
|---|---|---|---|---|
| 1 | AI quên gì, bộ não file giữ gì | 1 | 0 | 00 |
| 2 | Bốn file gốc và cuộc phỏng vấn | 1 | 1, 2 | 00, 01, 02 (câu lệnh 1) |
| 3 | Trục bốn tầng | 2 | 3 | 01 |
| 4 | Làm dự án, lưu bằng sáu câu hỏi | 2 | 4 | 01, 02 (câu lệnh 2) |
| 5 | Lỗi thành câu kiểm | 3 | 5 | 02 (câu lệnh 3), 03 |
| 6 | Nhìn lại tuần: từ dữ liệu lên quy trình, lên nguyên lý | 3 | 6 | 01, 02 (câu lệnh 4) |
| 7 | Nâng cấp: sao lưu, đo trước, dọn, đo sau | 4 | 7 | 00, 02 (câu lệnh 5, 6), 04 |
| 8 | Đổi AI, đổi máy, người đọc mới | 4 | 8, 9 | 00, 02 (câu lệnh 6), 03 |

---

## Bài 1 · AI quên gì, bộ não file giữ gì
- **Mục tiêu:** hiểu vì sao cần bộ não bằng file; chuẩn bị xong chỗ làm.
- **Nội dung:** mỗi cuộc trò chuyện mới AI bắt đầu từ số 0; "trí nhớ" có sẵn trong ứng dụng ngắn, khó sửa, không mang đi được; file thì đọc được, sửa được, AI nào cũng dùng được. Thước không đổi: AI mới tinh đọc ít nhất vẫn làm đúng. Hai mức cơ bản và nâng cao. Bảng từ mới (biểu mẫu 00). Luật an toàn: không lưu mật khẩu, mã OTP, giấy tờ, dữ liệu riêng của khách.
- **Thực hành:** trainer demo: hỏi một AI mới "tôi là ai, tôi muốn làm việc thế nào" khi chưa và khi đã nạp bộ não mẫu. Học viên làm thao tác 1 và 2 của biểu mẫu 00: tạo thư mục `bo-nao`, `ngoai-bo-nao`, tạo Projects "Bộ não".
- **Bài tập:** ghi ra **5 điều** phải nhắc lại AI nhiều lần nhất.
- **Xong khi:** có hai thư mục, có Projects, có danh sách 5 điều hay phải nhắc.

## Bài 2 · Bốn file gốc và cuộc phỏng vấn
- **Mục tiêu:** có bốn file gốc đúng về chính mình.
- **Nội dung:** vai trò từng file gốc: cửa vào (AI đọc gì trước, bảng mọi file), hồ sơ (tôi là ai), luật làm việc (AI phải theo gì), trạng thái (việc đang dở). Dòng mô tả đầu file. Để AI phỏng vấn thay vì tự viết: AI hỏi từng vòng, mình trả lời thật, AI viết, mình sửa.
- **Thực hành:** tạo bốn file từ mẫu (biểu mẫu 00 thao tác 3, biểu mẫu 01); tải bốn file và biểu mẫu 01 (tên `01-mau-file-goc.md`, để luôn trong Projects) lên Projects; chạy câu lệnh 1 (AI viết hồ sơ, luật, trạng thái và điền tên vào file cửa vào); đưa 5 điều hay phải nhắc vào luật 4 tới 8; thay file đã sửa (biểu mẫu 00 thao tác 4).
- **Bài tập:** mở cuộc trò chuyện mới trong Projects, hỏi "tóm 3 dòng về tôi"; sửa file ở chỗ AI tóm sai.
- **Xong khi:** AI tóm đúng 3 dòng mà không cần giải thích thêm.

## Bài 3 · Trục bốn tầng
- **Mục tiêu:** bộ não có một cách sắp xếp cố định, học thêm bao nhiêu cũng không rối.
- **Nội dung:** bốn tầng (trục · nguyên lý · quy trình · dữ liệu); tầng càng cao càng ít đổi; tầng nhận ra bằng chữ đầu tên file vì Projects không giữ thư mục con; trong tầng 1 và 2 mỗi ý chỉ một chỗ; luật thăng cấp: lặp ít nhất 2 lần thì thành quy trình, ít nhất 3 chuyện cùng bài học thì thành nguyên lý.
- **Thực hành:** tạo `truc-hoc.md`, `bai-hoc.md`, `y-tuong.md` từ mẫu; thêm ba dòng vào bảng file ở `doc-truoc.md`; tải lên Projects.
- **Bài tập:** chọn một việc học viên **đã làm ít nhất 2 lần** (ví dụ chốt một đơn hàng), viết `quy-trinh-<ten-viec>.md` theo mẫu: ít nhất 3 bước, mỗi bước có "đạt khi".
- **Xong khi:** mỗi file thuộc một tầng; bảng file ở `doc-truoc.md` có đủ mọi file trong `bo-nao`.

## Bài 4 · Làm dự án, lưu bằng sáu câu hỏi
- **Mục tiêu:** mỗi buổi làm việc với AI để lại bài học đúng chỗ.
- **Nội dung:** sáu câu hỏi khi lưu (là gì · phục vụ mục tiêu nào · đã có chỗ chưa · vì sao đúng · nối vào đâu · kiểm thế nào). Sửa thẳng câu cũ thay vì chồng câu mới. Sổ dự án `du-an-<ten>.md`: mục tiêu, mỗi buổi một dòng.
- **Thực hành:** chọn một dự án thật; tạo `du-an-<ten>.md` từ mẫu; làm một việc thật với AI ngay trong buổi (soạn kế hoạch, bài viết, bảng giá…); cuối buổi chạy câu lệnh 2; duyệt từng đề xuất; thay các file đã sửa trong Projects. Từ buổi này, lần nào phải sửa AI thì ghi ngay một dòng "Đã sửa AI: …" vào sổ dự án.
- **Bài tập:** làm thêm 2 buổi việc thật ở nhà, lần nào cũng kết thúc bằng câu lệnh 2.
- **Xong khi:** sổ dự án có ít nhất 3 dòng; bảng file ở `doc-truoc.md` có mọi file mới.

## Bài 5 · Lỗi thành câu kiểm
- **Mục tiêu:** lỗi đã sửa một lần thì AI không lặp lại.
- **Nội dung:** "lỗi" là lần nào mình phải nhắc lại, chỉnh lời, hay đổi cách làm của AI. Mỗi lỗi sửa ba chỗ: đúng file gây lỗi; một câu hỏi trong `bai-kiem.md` (tình huống, 4 lựa chọn, không có đáp án); một dòng trong `ngoai-bo-nao/dap-an.md` (đáp án, vì sao, nằm ở file nào). Đáp án không bao giờ tải lên AI. Bài kiểm chỉ lớn lên.
- **Thực hành:** lấy các dòng "Đã sửa AI" trong sổ dự án, chạy câu lệnh 3 cho từng lần; tạo `bai-kiem.md` và `dap-an.md` theo biểu mẫu 03.
- **Bài tập:** ghi mỗi lần phải sửa AI trong tuần; cuối tuần biến tất cả thành câu kiểm, đủ 10 câu trước buổi 4.
- **Xong khi:** bài kiểm có ít nhất 5 câu, mỗi câu từ một lỗi thật, đáp án nằm ngoài bộ não.

## Bài 6 · Nhìn lại tuần
- **Mục tiêu:** dữ liệu tự lên thành quy trình và nguyên lý, bộ não không chỉ dày thêm mà khôn thêm.
- **Nội dung:** tầng 3 được nhiều, vì là dữ liệu; tầng 1 và 2 phải gọn. Cách nhận ra điều lặp; cách viết một nguyên lý (một câu "vì sao" và 1–3 chuyện thật).
- **Thực hành:** chạy câu lệnh 4 trên sổ tuần vừa qua; duyệt đề xuất đưa lên quy trình hoặc nguyên lý; ghi dòng nhìn lại tuần vào `bai-hoc.md`.
- **Bài tập:** đặt một giờ cố định mỗi tuần để nhìn lại; ghi giờ đó vào `truc-hoc.md`.
- **Xong khi:** có một dòng nhìn lại tuần trong `bai-hoc.md`, kèm quy trình hoặc nguyên lý mới, hoặc ghi rõ "tuần này chưa có điều lặp".

## Bài 7 · Nâng cấp: sao lưu, đo trước, dọn, đo sau
- **Mục tiêu:** bộ não lớn lên mà vẫn gọn; mỗi bản mới tốt hơn bản cũ.
- **Nội dung:** khi nào nâng cấp (khoảng mỗi tháng, hoặc khi thấy luật chồng nhau, AI bắt đầu làm sai việc đã từng đúng). Ba chặng: sao lưu bản cũ và đo trước bằng câu lệnh 6 · dọn bốn việc bằng câu lệnh 5 (gom ý trùng, gỡ mâu thuẫn, cất cái lâu không dùng, viết rõ chỗ AI hiểu sai) · đo sau bằng câu lệnh 6. Đo sau kém hơn thì quay lại bản cũ (biểu mẫu 00, thao tác 7). Cất file thì xoá khỏi Projects (thao tác 8). Lời mới nhất thắng khi hai luật ngược nhau.
- **Thực hành:** sao lưu theo biểu mẫu 00 thao tác 6; đo trước; chạy câu lệnh 5; đo sau; kiểm theo biểu mẫu 04.
- **Bài tập:** ghi một dòng vào bảng "Nâng cấp" của `bai-hoc.md`: điểm trước, điểm sau, đã gom, gỡ, cất, viết rõ gì.
- **Xong khi:** điểm đo sau bằng hoặc cao hơn đo trước.

## Bài 8 · Đổi AI, đổi máy, người đọc mới
- **Mục tiêu:** bộ não không mất, dùng được với AI khác, và được chứng minh là dạy đúng.
- **Nội dung:** Projects tự có trên mọi máy đăng nhập cùng tài khoản; bản trong Google Drive là bản gốc, dùng khi đổi AI hay mất tài khoản. Mức nâng cao: GitHub kho riêng tư, mỗi lần sửa thì đưa lên, máy khác tải về. Người đọc mới: AI mới tinh hoặc AI khác hẳn, chỉ đọc bộ não, làm bài kiểm khi không thấy đáp án. Câu sai thì sửa file làm AI hiểu sai, không sửa bài kiểm.
- **Thực hành:** tải thư mục `bo-nao` vào một AI khác với AI hay dùng (biểu mẫu 00 thao tác 5); chạy câu lệnh 6; chấm theo biểu mẫu 03.
- **Bài tập:** làm dự án thật thứ 3 bằng trọn vòng học (làm, lưu, câu kiểm, kiểm), tự làm không cần trainer.
- **Xong khi:** người đọc mới đúng ít nhất 90% trên bài kiểm có ít nhất 10 câu; bộ não đã qua ít nhất 3 dự án thật.
