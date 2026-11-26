---
description: "Biểu mẫu 00 gói dựng bộ não: bảng từ mới cho người mới bắt đầu và các thao tác thủ công ở mức cơ bản (tạo Projects, tạo file .md, thay file, trò chuyện tạm thời, sao lưu Google Drive)."
---

# Biểu mẫu 00 · Từ mới và thao tác thủ công ở mức cơ bản

Học viên đọc biểu mẫu này trước bài 1. Mọi thao tác dưới đây thực hiện trên **máy tính** (Mac hoặc Windows) có trình duyệt. Điện thoại dùng để trò chuyện với AI được, nhưng việc tạo và sửa file thì thực hiện trên máy tính.

## Từ mới
| Từ | Nghĩa trong gói |
|---|---|
| **AI** | trí tuệ nhân tạo: ChatGPT, Claude, Gemini |
| **Bộ não** | một thư mục chứa các file chữ mô tả người dùng là ai, muốn làm việc thế nào, đã học được gì; AI đọc để hiểu người dùng |
| **File `.md`** | file chỉ có chữ, không in đậm, không màu (gọi là Markdown). Mở được bằng mọi ứng dụng soạn chữ, AI nào cũng đọc được. Dấu `#` đầu dòng là tiêu đề; dòng có dấu `|` là bảng |
| **Mẫu** | file mẫu có sẵn chỗ trống `<…>`; chép ra rồi điền vào chỗ trống |
| **Chức năng Projects** | chức năng của ứng dụng AI (ChatGPT, Claude; trên Gemini gọi là Gems) để tải file lên một lần, mọi cuộc trò chuyện trong đó đều đọc được. Trong gói luôn gọi là "Projects" để tránh nhầm với "dự án" là công việc thực tế người dùng làm |
| **Dự án** | công việc thực tế người dùng làm cùng AI (một kế hoạch, một đợt bán hàng, một khoá học). Mỗi dự án có một file sổ |
| **Trỏ tới** | file này có ghi tên file kia, để AI biết và mở. File không được file nào trỏ tới gọi là **mồ côi**: AI sẽ không biết file đó tồn tại |
| **Nạp bộ não** | tải các file bộ não vào chức năng Projects (hoặc mở thư mục bộ não ở mức nâng cao) |
| **Sáu câu hỏi khi lưu** | sáu câu người dùng tự hỏi cho mỗi điều mới trước khi lưu (1-quy-trinh.md) |
| **Câu lệnh 1–6** | sáu đoạn chữ soạn sẵn để dán vào AI (biểu mẫu 02) |
| **Câu kiểm** | một câu hỏi tình huống trong bài kiểm (biểu mẫu 03) |
| **Người đọc mới** | một AI mới hoàn toàn, chưa biết gì về người dùng, chỉ đọc bộ não |
| **Trường hợp cùng gốc** | nhiều trường hợp khác nhau nhưng cùng một nguyên nhân hoặc cùng một bài học |
| **Đo trước, đo sau** | chạy bài kiểm trước và sau khi sửa bộ não, so sánh điểm để biết phiên bản mới có tốt hơn không |
| **OTP** | mã dùng một lần gửi qua tin nhắn để đăng nhập; không bao giờ đưa vào bộ não |
| **Google Drive** | ổ lưu trữ trực tuyến của Google |
| **Tên file không dấu, chữ thường** | tên file viết tiếng Việt không dấu, không viết hoa, nối bằng gạch ngang, ví dụ `luat-lam-viec.md` |
| **UTF-8** | cách máy tính lưu chữ có dấu tiếng Việt cho đúng; khi lưu file trên Windows chọn "UTF-8" ở ô Mã hoá (Encoding) |
| **File .zip** | một file nén chứa cả thư mục; bấm đúp vào thì máy tự giải nén thành thư mục |
| **Dấu `*` trong tên file** | nghĩa là "mọi file bắt đầu như vậy": `du-an-*.md` là mọi file sổ dự án |
| **Trục, thước đo không đổi** | trục là phần gốc của bộ não, gần như không thay đổi; thước đo không đổi là câu dùng để chấm mọi thứ: "AI mới tinh đọc bộ não vẫn làm đúng như mình muốn" |
| **Trainer** | người hướng dẫn kèm cặp học viên trong gói |
| **Link** | đường dẫn bấm vào để mở hoặc tải một file |
| **Instructions** | ô "Hướng dẫn" của Projects: câu dán vào đây sẽ được AI tuân theo trong mọi cuộc trò chuyện của Projects |

## Thao tác 1 · Tạo thư mục bộ não
- **Khuyên dùng Google Drive** để bộ não không bị mất khi hỏng máy: tải ứng dụng "Google Drive cho máy tính" (Google Drive for desktop) ở trang google.com/drive/download, cài đặt, đăng nhập tài khoản Google. Máy sẽ có thêm một ổ tên Google Drive; tạo hai thư mục dưới đây trong ổ đó ("Drive của tôi" hay "My Drive").
- Nếu không dùng Google Drive thì tạo trong thư mục Tài liệu (Documents), và tự sao lưu theo thao tác 6.
- Cách tạo thư mục: **Mac** mở Finder, vào đúng vị trí, bấm chuột phải vào chỗ trống, chọn "Thư mục mới" (New Folder), gõ tên. **Windows** mở File Explorer, vào đúng vị trí, bấm chuột phải, chọn "Mới" rồi "Thư mục" (New, Folder), gõ tên.
- Tạo hai thư mục: `bo-nao` (tải lên AI) và `ngoai-bo-nao` (chứa đáp án bài kiểm, bản cũ, file đã lưu trữ; không bao giờ tải lên AI).

## Thao tác 2 · Tạo Projects
- **ChatGPT:** ở thanh bên trái, bấm "Projects" (hoặc "New project"), đặt tên "Bộ não". Tại ô "Instructions" dán một câu: `Trước khi trả lời, luôn đọc file doc-truoc.md và làm theo.`
- **Claude:** ở thanh bên trái, bấm "Projects", "Create project", đặt tên "Bộ não". Tại ô "Project instructions" dán cùng câu trên.
- Giao diện có thể đổi tên nút theo thời gian; tìm chữ "Project" là thấy.

## Thao tác 3 · Tạo một file `.md`
**Cách dễ nhất (đề xuất):** yêu cầu AI tạo file để người dùng tải về:
```text
Tạo file tên doc-truoc.md với nội dung dưới đây, cho tôi link tải về:
<dán nội dung>
```
ChatGPT và Claude đều tạo được file để tải. Tải về rồi chép vào thư mục `bo-nao`.

**Tự tạo thủ công:**
- **Mac:** mở TextEdit, menu Định dạng (Format) chọn "Tạo văn bản thường" (Make Plain Text), dán nội dung, lưu với tên `doc-truoc.md`; nếu máy hỏi đuôi file thì chọn "Dùng .md".
- **Windows:** mở Notepad, dán nội dung, Lưu với tên `doc-truoc.md`, ô "Lưu dưới dạng" chọn "Tất cả các tệp" (All files), mã hoá UTF-8.

Khi chép mẫu từ biểu mẫu: **chỉ chép phần bên trong**, không chép dòng có ba dấu ``` ở đầu và cuối mẫu.

## Thao tác 4 · Thay một file trong Projects
AI ở mức cơ bản không tự sửa được file trong Projects. Mỗi lần sửa:
1. Yêu cầu AI đưa **toàn bộ nội dung mới** của file (hoặc tạo file để tải, như thao tác 3).
2. File tải về nằm trong thư mục Tải về (Downloads), và có thể bị đổi tên thành `ten-file (1).md`. Chuyển file vào `bo-nao`, đổi lại đúng tên (bỏ phần ` (1)`), đồng ý thay file cũ khi máy hỏi.
3. Trong Projects: **xoá file cũ cùng tên trước**, rồi tải file mới lên. Nếu không xoá thì sẽ có hai bản, AI không biết bản nào đúng.

Mẹo giảm khối lượng việc: cuối buổi gộp mọi file cần sửa vào một lần (câu lệnh 2 đã làm như vậy).

## Thao tác 5 · AI "mới tinh" để kiểm
Chức năng trí nhớ của ứng dụng khiến AI không còn "mới" (đã biết về người dùng). Khi chạy bài kiểm người đọc mới, chọn một trong ba cách:
- **Tốt nhất:** dùng một AI khác (đang dùng ChatGPT thì kiểm bằng Claude bản miễn phí, hoặc ngược lại).
- ChatGPT: bật "Trò chuyện tạm thời" (Temporary Chat) rồi tải bộ não vào cuộc trò chuyện đó.
- Hoặc tắt trí nhớ trong Cài đặt, mục Cá nhân hoá (Personalization), phần Trí nhớ (Memory), rồi bật lại sau khi kiểm.

Khi kiểm, tải các file trong `bo-nao`, **không tải thư mục `ngoai-bo-nao`**. AI bản miễn phí có thể không nhận hết nhiều file một lúc: khi đó dùng cách thứ hai (trò chuyện tạm thời trên tài khoản đang dùng), hoặc yêu cầu AI đang dùng gộp mọi file trong `bo-nao` thành một file `bo-nao-gop.md` để tải về rồi tải file đó lên AI dùng để kiểm.

## Thao tác 6 · Sao lưu
- Nếu thư mục `bo-nao` nằm trong Google Drive for desktop thì đã được tự sao lưu.
- Trước mỗi đợt nâng cấp: trên máy tính, chép cả thư mục `bo-nao` vào `ngoai-bo-nao` và đặt tên `bo-nao-ban-<ngày>`. Trên Drive bản trình duyệt không chép được cả thư mục: tải thư mục về (Drive tự nén thành file .zip), lưu file .zip đó trong `ngoai-bo-nao`.

## Thao tác 7 · Quay lại bản trước
Dùng khi điểm đo sau thấp hơn điểm đo trước:
1. Trong Projects: xoá **hết** các file của bộ não (giữ lại `01-mau-file-goc.md`).
2. Lấy bản sao `bo-nao-ban-<ngày>` trong `ngoai-bo-nao` (nếu là file .zip thì bấm đúp để giải nén thành thư mục).
3. Chép các file trong bản sao đè vào thư mục `bo-nao`, rồi tải tất cả lên lại Projects.

## Thao tác 8 · Lưu trữ một file
Chuyển file từ `bo-nao` sang `ngoai-bo-nao/luu-tru/`, **xoá file đó khỏi Projects**, bỏ dòng của file đó khỏi bảng file ở `doc-truoc.md`.

## Giới hạn số file
Projects của mỗi ứng dụng có giới hạn số file (xem trong ứng dụng, thường từ vài chục file trở lên). Khi gần đạt giới hạn thì: gộp các sổ dự án đã xong thành một file `du-an-da-xong.md`, hoặc chuyển lên mức nâng cao.
