---
description: "Gói 2 dựng bộ não bằng file cho AI, phần 1 quy trình: lý do cần có, bốn tầng, cấu trúc thư mục phẳng, 10 bước từ số 0 tới bộ não tự nâng cấp, sáu câu hỏi khi lưu, luật an toàn, yêu cầu thiết bị."
---

# 1. Quy trình: dựng và duy trì bộ não bằng file cho AI

Người mới bắt đầu đọc [bo-bieu-mau/00-tu-moi-va-thao-tac-co-ban.md](bo-bieu-mau/00-tu-moi-va-thao-tac-co-ban.md) trước: bảng từ mới và các thao tác thủ công (tạo file, tạo Projects, thay file).

## Lý do cần có
Mỗi lần mở cuộc trò chuyện mới, AI **bắt đầu từ số 0** về người dùng: AI chỉ biết những gì đọc được lúc đó. Chức năng "trí nhớ" có sẵn của ứng dụng AI thì ngắn, khó xem, khó sửa, không chuyển sang AI khác được. Bộ não bằng file giải quyết cả ba vấn đề: người dùng đọc được, sửa được, chuyển sang AI nào cũng dùng được.

**Thước đo không bao giờ đổi:** một AI mới hoàn toàn, đọc ít nhất, vẫn làm đúng như người dùng muốn, và lần sau đúng hơn lần trước.

## Mục tiêu
Học viên có một thư mục bộ não của chính mình; mỗi lần làm xong một dự án thì bộ não tốt hơn một chút, theo một cách cố định, không phải nghĩ lại cách lưu mỗi lần.

## Kế hoạch: bốn tầng
Bộ não chia thành bốn tầng. Tầng càng cao thì càng ít thay đổi, và càng cần nhiều dẫn chứng mới được thay đổi.

| Tầng | Chứa | Ví dụ | Đổi khi |
|---|---|---|---|
| 0 · Trục | người dùng là ai, luật làm việc, cách học | `ho-so.md`, `luat-lam-viec.md` | gần như không đổi; người dùng tự chốt sau vài ngày suy nghĩ |
| 1 · Nguyên lý | lý do làm như vậy; áp dụng được cho nhiều việc | "khách hỏi giá thì trả lời kèm lý do, vì khách sợ bị hớ" | có ít nhất 3 trường hợp cùng một bài học |
| 2 · Quy trình | các bước của một loại việc | các bước nhận một đơn hàng | một cách làm đã lặp lại ít nhất 2 lần |
| 3 · Dữ liệu | sổ dự án, bài học, nguồn học, trạng thái, bài kiểm | sổ đợt bán Trung thu | thêm hằng ngày; chỉ thêm, không sửa nghĩa nội dung cũ |

Trong tầng 1 và 2, mỗi ý chỉ nằm ở **một nguồn duy nhất**; nơi khác chỉ trỏ tới. Tầng 3 được phép có nhiều bản, vì là dữ liệu.

Lý do chia như vậy: đây chính là cách một mô hình AI được tạo ra. Rất nhiều ví dụ thực tế (tầng 3) được nén thành quy luật chung (tầng 1), nằm dưới vài nguyên tắc gốc (tầng 0), và mỗi phiên bản mới chỉ được phát hành khi làm bài kiểm tốt hơn phiên bản cũ.

**Cấu trúc thư mục: một thư mục phẳng, không có thư mục con.** Chức năng Projects của các ứng dụng AI không giữ thư mục con, nên tầng được nhận diện bằng **chữ đầu tên file**. Tên file không dấu, chữ thường, gạch nối.

```
bo-nao/                          tải toàn bộ lên AI
├── doc-truoc.md                 tầng 0 · file cửa vào: AI đọc đầu tiên, có bảng mọi file
├── ho-so.md                     tầng 0 · tôi là ai, mục tiêu, cách muốn được làm việc
├── luat-lam-viec.md             tầng 0 · luật AI phải theo
├── truc-hoc.md                  tầng 0 · cách nhận, lưu, nâng cấp mọi thông tin
├── nguyen-ly-<ten>.md           tầng 1 · mỗi file một nguyên lý
├── quy-trinh-<ten-viec>.md      tầng 2 · mỗi file một loại việc
├── trang-thai.md                tầng 3 · việc đang dở, việc tiếp theo, việc chờ mình quyết
├── bai-hoc.md                   tầng 3 · sổ bài học, nhìn lại tuần, các đợt nâng cấp
├── y-tuong.md                   tầng 3 · ý tưởng chưa gắn với mục tiêu nào (chưa làm)
├── du-an-<ten>.md               tầng 3 · mỗi dự án một file sổ
├── nguon-hoc-<ten>.md           tầng 3 · tóm tắt một sách, khoá học, video đã học
└── bai-kiem.md                  tầng 3 · câu kiểm (chỉ câu hỏi)

ngoai-bo-nao/                    KHÔNG tải lên AI
├── dap-an.md                    đáp án bài kiểm
├── luu-tru/                     file lâu không dùng hoặc đã lỗi thời (cất, không xoá)
└── bo-nao-ban-<ngày>/           bản sao trước mỗi đợt nâng cấp
```

## Quy trình: 10 bước
| # | Bước | Làm gì | Đạt khi |
|---|---|---|---|
| 0 | **Chuẩn bị** | chọn AI đang dùng; tạo thư mục `bo-nao` và `ngoai-bo-nao`; tạo Projects (biểu mẫu 00, thao tác 1 và 2) | có hai thư mục và một Projects tên "Bộ não" |
| 1 | **Tạo bốn file gốc** | bốn file gốc là `doc-truoc.md`, `ho-so.md`, `luat-lam-viec.md`, `trang-thai.md`; tạo từ mẫu (biểu mẫu 01, cách tạo file ở biểu mẫu 00 thao tác 3); tải cả bốn file **và file biểu mẫu 01** lên Projects | Projects có bốn file gốc; hỏi AI "trong Projects có những file nào" thì AI liệt kê đúng |
| 2 | **Cho AI phỏng vấn người dùng** | dán câu lệnh 1; trả lời trung thực; AI viết lại hồ sơ và luật; người dùng sửa chỗ sai rồi thay file trong Projects (biểu mẫu 00, thao tác 4) | mở cuộc trò chuyện mới trong Projects, hỏi "tóm 3 dòng về tôi": AI tóm đúng tôi là ai, làm việc với tôi thế nào, việc đang làm chưa xong |
| 3 | **Dựng trục bốn tầng** | tạo `truc-hoc.md`, `bai-hoc.md`, `y-tuong.md` từ mẫu; thêm ba dòng này vào bảng file ở `doc-truoc.md` | mỗi file thuộc đúng một tầng; bảng file ở `doc-truoc.md` có đủ mọi file trong `bo-nao` (trừ chính file đó và file mẫu) |
| 4 | **Làm dự án thực tế, cuối buổi lưu** | buổi đầu của một dự án: tạo `du-an-<ten>.md` từ mẫu. Làm việc thực tế với AI; lần nào phải sửa AI thì ghi ngay một dòng "Đã sửa AI: …" vào sổ (dùng ở bước 5); cuối buổi dán câu lệnh 2; duyệt đề xuất; thay các file đã sửa | mỗi buổi để lại ít nhất một dòng ở sổ dự án; bảng file ở `doc-truoc.md` có file mới |
| 5 | **Lỗi thành câu kiểm** | lần nào phải sửa AI (nhắc lại, chỉnh lời, đổi cách làm) thì dán câu lệnh 3: AI sửa đúng file gây lỗi, thêm một câu vào `bai-kiem.md` và đáp án vào `ngoai-bo-nao/dap-an.md` (biểu mẫu 03) | file gây lỗi đã được sửa; bài kiểm và đáp án đều có câu mới |
| 6 | **Nhìn lại tuần** | mỗi tuần một lần, dán câu lệnh 4: AI đọc sổ của tuần qua, tìm điều lặp lại; lặp ít nhất 2 lần thì thành quy trình, có ít nhất 3 trường hợp cùng bài học thì thành nguyên lý | một dòng nhìn lại tuần trong `bai-hoc.md`; có quy trình, nguyên lý mới, hoặc ghi rõ "tuần này chưa có điều lặp" |
| 7 | **Nâng cấp định kỳ** | khoảng mỗi tháng, hoặc khi thấy luật chồng chéo, AI làm sai việc đã từng làm đúng. Ba chặng: sao lưu bản cũ và **đo trước** (câu lệnh 6) · **dọn** bốn việc: gộp ý trùng, xử lý mâu thuẫn, lưu trữ nội dung lâu không dùng, viết rõ chỗ AI hiểu sai (câu lệnh 5) · **đo sau** (câu lệnh 6) | điểm đo sau bằng hoặc cao hơn điểm đo trước; thấp hơn thì quay lại bản đã sao lưu (biểu mẫu 00, thao tác 7) |
| 8 | **Sao lưu, đổi AI, đổi thiết bị** | thư mục `bo-nao` nằm trong Google Drive (khuyên dùng ở mức cơ bản; không có thì sao lưu thủ công theo biểu mẫu 00 thao tác 6) hoặc GitHub (mức nâng cao). Projects tự có trên mọi thiết bị đăng nhập cùng tài khoản; bản trên Drive dùng khi đổi sang AI khác hoặc mất tài khoản | tải bộ não vào một AI khác, AI đó tóm đúng 3 dòng về người dùng |
| 9 | **Kiểm bằng người đọc mới** | dùng AI mới hoàn toàn (biểu mẫu 00, thao tác 5), tải các file trong `bo-nao`, dán câu lệnh 6; người dùng chấm bằng `dap-an.md` | đúng ít nhất 90% số câu (bài kiểm nghiệm thu có ít nhất 10 câu); câu sai thì sửa file khiến AI hiểu sai, không sửa bài kiểm |

Bước 0–3 làm một lần. Bước 4–5 làm mỗi buổi. Bước 6 làm mỗi tuần. Bước 7 và 9 làm mỗi tháng. Bước 8 thiết lập một lần, sau đó Google Drive tự sao lưu; kiểm lại mỗi lần nâng cấp.

## Sáu câu hỏi khi lưu (cốt lõi của bước 4)
1. **Là gì?** sự thật · quyết định của người dùng · cách làm · ví dụ hoặc số liệu. Câu trả lời quyết định tầng và file.
2. **Phục vụ mục tiêu nào trong hồ sơ?** Không gắn được với mục tiêu thì không lưu, hoặc chỉ ghi vào `y-tuong.md`.
3. **Đã có vị trí chưa?** Nếu có thì sửa trực tiếp tại vị trí đó (viết lại câu cũ, không chồng thêm câu mới). Nếu chưa có thì ghi ở tầng 3 trước.
4. **Vì sao đúng?** Ghi ngắn gọn lý do. Lý do giúp AI làm đúng thì viết trong luật; ngày và lời gốc thì ghi vào sổ.
5. **Liên kết với đâu?** Thêm một dòng vào bảng file ở `doc-truoc.md`, hoặc file liên quan ghi tên file này. Không file nào trỏ tới thì AI không biết file đó tồn tại.
6. **Kiểm thế nào?** Câu kiểm nào, kết quả nào sẽ cho biết nội dung này có ích? Nếu chưa biết thì ghi một dự đoán, ví dụ "mong AI viết đúng giọng ngay lần đầu; xem lại sau 5 lần".

## Luật an toàn
- **Không bao giờ lưu** mật khẩu, mã OTP, số thẻ, số tài khoản, giấy tờ tuỳ thân vào bộ não. Bộ não được tải lên AI và có thể được đưa lên GitHub.
- Dữ liệu riêng của khách hàng (số điện thoại, địa chỉ) không ghi vào bộ não; sổ dự án chỉ ghi điều học được.
- Kho GitHub (mức nâng cao) luôn để chế độ riêng tư.
- Viết đủ từ, đủ nghĩa, không viết tắt: người khác hoặc AI khác đọc mà không có bối cảnh cũng phải hiểu.
- Lời người dùng nói sau cùng là luật hiện hành: khi đổi luật thì viết lại đúng câu đó, không để hai phiên bản cùng tồn tại.
- AI đề xuất, người dùng duyệt rồi mới ghi.

## Yêu cầu thiết bị
- **Mức cơ bản:** máy tính Mac hoặc Windows có trình duyệt; tài khoản AI có chức năng Projects (thường là bản trả phí); Google Drive (khuyên dùng; không có thì dùng thư mục trên máy và tự sao lưu). Thêm một AI khác bản miễn phí để kiểm bằng người đọc mới.
- **Mức nâng cao:** máy Mac hoặc Windows; trợ lý AI chạy trên máy, tức loại AI tự đọc và sửa file trong thư mục (Claude Code, Codex, Gemini CLI); tài khoản GitHub miễn phí (dịch vụ lưu thư mục có ghi lại mọi lần sửa). Ở mức này có thể dùng thư mục con, nhưng giữ nguyên tên file để chuyển qua lại giữa hai mức dễ dàng.
