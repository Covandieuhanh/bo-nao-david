---
description: "Biểu mẫu 02 gói dựng bộ não: sáu câu lệnh dán vào AI — phỏng vấn viết hồ sơ, lưu cuối buổi bằng sáu câu hỏi, lỗi thành câu kiểm, nhìn lại tuần, dọn khi nâng cấp, kiểm bằng người đọc mới."
---

# Biểu mẫu 02 · Sáu câu lệnh mẫu

Dán nguyên phần trong khung vào AI (trong Projects "Bộ não" ở mức cơ bản, hoặc trong thư mục bộ não ở mức nâng cao). Chỗ `<…>` là chỗ điền. Câu lệnh nào cũng bắt AI **đề xuất trước, chờ duyệt rồi mới viết bản cuối**: bộ não là của mình, AI không tự quyết.

Ở mức cơ bản, khi AI đưa bản cuối của một file: bảo AI "tạo file để tôi tải về" rồi thay file trong Projects (biểu mẫu 00, thao tác 4). Ở mức nâng cao, AI tự sửa file.

| Câu lệnh | Dùng khi | Bước |
|---|---|---|
| 1 · Phỏng vấn | dựng hồ sơ và luật lần đầu | 2 |
| 2 · Lưu cuối buổi | cuối mỗi buổi làm việc | 4 |
| 3 · Lỗi thành câu kiểm | mỗi lần phải sửa AI | 5 |
| 4 · Nhìn lại tuần | mỗi tuần | 6 |
| 5 · Dọn khi nâng cấp | giữa đo trước và đo sau | 7 |
| 6 · Người đọc mới | đo trước và đo sau mỗi đợt nâng cấp; nghiệm thu | 7, 9 |

---

## Câu lệnh 1 · Phỏng vấn để viết hồ sơ và luật

```text
Bạn là người phỏng vấn giúp tôi dựng bộ não bằng file, để mọi AI sau này đọc là hiểu tôi.
Trong Projects có mẫu các file (biểu mẫu 01). Hãy hỏi tôi theo từng vòng, mỗi vòng tối đa 5 câu,
chờ tôi trả lời rồi mới hỏi vòng sau:
vòng 1 tôi là ai và làm gì; vòng 2 mục tiêu và thước đo thành công; vòng 3 thế mạnh, điểm cần bù, nhịp làm việc;
vòng 4 tôi muốn AI làm việc với tôi thế nào, 5 điều tôi hay phải nhắc AI nhất, điều AI không bao giờ được làm.
Câu nào tôi trả lời mơ hồ thì hỏi lại một lần, có gợi ý sẵn 2–3 lựa chọn.
Không hỏi mật khẩu, số giấy tờ, thông tin tài chính.
Hỏi xong thì viết ho-so.md, luat-lam-viec.md, trang-thai.md (việc tôi đang làm, việc tiếp theo, việc chờ tôi quyết)
và điền tên tôi vào doc-truoc.md, theo đúng mẫu, viết đủ từ, không viết tắt,
rồi hỏi tôi chỗ nào sai để sửa. Khi tôi nói "được", tạo bốn file để tôi tải về.
```

## Câu lệnh 2 · Lưu cuối buổi bằng sáu câu hỏi

```text
Buổi làm việc này đã xong. Hãy đọc truc-hoc.md, rồi với từng điều mới xuất hiện trong buổi
(quyết định của tôi, cách làm mới, lời tôi đã sửa bạn, bài học, số liệu), trả lời sáu câu hỏi khi lưu:
là gì · phục vụ mục tiêu nào trong ho-so.md · đã có chỗ chưa · vì sao đúng · nối vào đâu · kiểm thế nào.
Sau đó đưa tôi một bảng đề xuất: điều mới | ghi vào file nào | sửa câu nào hay thêm câu nào | tầng mấy.
Có chỗ rồi thì sửa thẳng câu cũ, không chồng câu mới. Chưa có chỗ thì ghi ở tầng 3.
Luôn có: một dòng mới trong du-an-<tên dự án>.md (chưa có file thì tạo theo mẫu), cập nhật trang-thai.md,
và thêm dòng vào bảng file ở doc-truoc.md cho mọi file mới.
Chờ tôi duyệt, rồi tạo các file đã sửa để tôi tải về (mỗi file đủ toàn bộ nội dung, không chỉ phần sửa).
```

## Câu lệnh 3 · Lỗi thành câu kiểm

```text
Vừa rồi tôi phải sửa bạn: <tôi đã nói gì>.
1. Tìm file nào trong bộ não lẽ ra phải dạy bạn làm đúng (luật, quy trình, nguyên lý), hoặc nói rõ là chưa có file nào.
2. Đề xuất sửa đúng một chỗ ở file đó để lần sau bạn tự làm đúng (sửa thẳng câu cũ nếu có).
3. Viết một câu kiểm cho bai-kiem.md từ chính tình huống này: tình huống, câu hỏi, 4 lựa chọn A B C D,
   các lựa chọn sai đều nghe hợp lý; KHÔNG ghi đáp án trong bai-kiem.md.
4. Viết riêng một dòng đáp án để tôi tự chép vào dap-an.md (file này tôi giữ ngoài Projects):
   số câu | đáp án | vì sao | nằm ở file nào | ngày.
Chờ tôi duyệt rồi mới tạo file.
```

## Câu lệnh 4 · Nhìn lại tuần

```text
Đọc truc-hoc.md, bai-hoc.md và mọi file du-an-*.md, chỉ phần từ <ngày> tới hôm nay.
1. Liệt kê điều lặp lại: cách làm lặp ít nhất 2 lần, bài học có ít nhất 3 chuyện cùng gốc, lỗi lặp lại.
2. Đề xuất: cách làm nào thành quy-trinh-<ten-viec>.md, bài học nào thành nguyen-ly-<ten>.md (kèm 1–3 chuyện thật),
   lỗi nào cần thêm câu kiểm. Không có điều lặp thì nói thẳng "tuần này chưa có điều lặp".
3. Kiểm các file nguyen-ly- và quy-trinh-: có ý nào nằm ở hai chỗ không? Đề xuất gom về một chỗ.
4. Viết một dòng cho bảng "Nhìn lại tuần" trong bai-hoc.md.
Chờ tôi duyệt rồi mới tạo file.
```

## Câu lệnh 5 · Dọn khi nâng cấp

Trước câu lệnh này: đã sao lưu bản cũ (biểu mẫu 00, thao tác 6) và đã **đo trước** bằng câu lệnh 6.

```text
Ta dọn bộ não trong một đợt nâng cấp. Điểm đo trước: <đúng>/<tổng>; câu sai hoặc "phải tự suy": <số câu, nội dung>.
1. Gom: tìm ý trùng hoặc gần trùng ở các file nguyen-ly-, quy-trinh- và luat-lam-viec.md; đề xuất mỗi ý một chỗ, nơi khác chỉ ghi tên file đó.
2. Gỡ: tìm luật mâu thuẫn nhau; lời tôi nói sau cùng thắng; chỗ không rõ thì gom lại hỏi tôi một lần.
3. Cất: tìm file, luật lâu không dùng hoặc đã lỗi thời; đề xuất chuyển ra ngoai-bo-nao/luu-tru/ (không xoá hẳn): tôi sẽ xoá nó khỏi Projects và bỏ dòng của nó khỏi bảng file.
4. Viết rõ: với mỗi câu sai hoặc "phải tự suy", chỉ ra file làm AI hiểu sai và đề xuất câu viết lại cho rõ.
Không đặt thêm luật mới trong đợt này: chỉ gom, gỡ, cất, và viết rõ hơn luật đã có (được thêm câu giải thích cho luật đã có).
Đưa tôi bảng đề xuất cho cả bốn việc, chờ duyệt rồi mới tạo file.
```
Sửa xong thì **đo sau** bằng câu lệnh 6. Điểm đo sau thấp hơn đo trước thì quay về bản đã sao (biểu mẫu 00, thao tác 7). Ghi một dòng vào bảng "Nâng cấp" của `bai-hoc.md`.

## Câu lệnh 6 · Kiểm bằng người đọc mới

Dùng AI mới tinh (biểu mẫu 00, thao tác 5). Tải các file trong `bo-nao`, **không tải gì trong `ngoai-bo-nao`**. Dán:

```text
Bạn chưa biết gì về tôi. Hãy đọc doc-truoc.md rồi đọc tiếp theo thứ tự trong đó.
Sau đó làm bai-kiem.md: mỗi câu chọn một đáp án, ghi một dòng vì sao và file nào trong bộ não cho bạn biết điều đó.
Câu nào bộ não không nói rõ, hãy ghi "phải tự suy" thay vì đoán chắc.
Cuối cùng ghi 3 chỗ trong bộ não bạn thấy khó hiểu hoặc mâu thuẫn.
```
Mình tự chấm bằng `dap-an.md` (cách chấm: biểu mẫu 03). Câu sai hoặc "phải tự suy": sửa file trong bộ não cho rõ, **không sửa bài kiểm**.
