---
description: "Biểu mẫu 01 gói dựng bộ não: mẫu bốn file gốc (cửa vào, hồ sơ, luật làm việc, trạng thái), trục học, sổ bài học, ý tưởng, sổ dự án, nguyên lý, quy trình; chép ra rồi điền."
---

# Biểu mẫu 01 · Mẫu các file

Học viên tải file biểu mẫu này lên Projects ở bước 1 với tên `01-mau-file-goc.md` và **giữ ở đó lâu dài**: AI dùng nó để tạo file mới. Nó là mẫu, không phải thông tin về học viên, nên không ghi vào bảng file.

Học viên chép từng mẫu thành một file trong thư mục `bo-nao`, đúng tên file ghi ở tiêu đề (cách tạo file: biểu mẫu 00, thao tác 3). **Chỉ chép phần bên trong**, không chép dòng ba dấu ``` ở đầu và cuối mỗi mẫu. Chỗ `<…>` là chỗ điền. Dòng đầu mỗi file luôn là câu mô tả file đó chứa gì: AI đọc câu này để biết có cần mở file hay không.

| Mẫu | Tạo ở bước |
|---|---|
| bốn file gốc: `doc-truoc.md`, `ho-so.md`, `luat-lam-viec.md`, `trang-thai.md` | 1 |
| `truc-hoc.md`, `bai-hoc.md`, `y-tuong.md` | 3 |
| `du-an-<ten>.md` | 4 (buổi đầu mỗi dự án) |
| `quy-trinh-<ten-viec>.md` | 3 (bài tập, cho việc đã làm ít nhất 2 lần) và 6 |
| `nguyen-ly-<ten>.md` | 6 (khi nhìn lại tuần thấy ít nhất 3 chuyện cùng bài học) |
| `bai-kiem.md`, `dap-an.md` | 5 (mẫu ở biểu mẫu 03) |

---

## `doc-truoc.md` (file cửa vào)

Ở bước 1, bảng file chỉ có bốn file gốc. Học viên tạo file mới nào thì thêm một dòng vào bảng.

```markdown
Mô tả: File cửa vào bộ não của <tên>. AI đọc file này đầu tiên rồi đọc tiếp theo thứ tự bên dưới.

# Bắt đầu từ đây

Bạn đang làm việc với <tên>. Các file ở đây là bộ não của <tên>: <tên> là ai, muốn được làm việc thế nào, đang làm gì, đã học được gì.
Đọc xong, hãy làm việc như một trợ lý đã đồng hành từ trước, không hỏi lại điều đã có ở đây.

## Đọc theo thứ tự
1. ho-so.md
2. luat-lam-viec.md
3. trang-thai.md
4. Các file khác: tra bảng dưới, mở file đúng việc đang làm.

## Bảng file (tạo file mới thì thêm một dòng)
Bảng ghi mọi file trong bộ não, trừ chính file này và file 01-mau-file-goc.md (file đó chỉ là mẫu để tạo file mới, không phải thông tin về <tên>).
Tên file bắt đầu bằng "quy-trinh-" là tầng 2, "nguyen-ly-" là tầng 1, "du-an-" và "nguon-hoc-" là tầng 3.

| File | Tầng | Chứa |
|---|---|---|
| ho-so.md | 0 | tôi là ai, mục tiêu |
| luat-lam-viec.md | 0 | luật bạn phải theo |
| trang-thai.md | 3 | việc đang dở |
```

---

## `ho-so.md` (tôi là ai)

```markdown
Mô tả: Hồ sơ của <tên>: là ai, làm gì, mục tiêu, thế mạnh, cách muốn được làm việc.

# Hồ sơ

## Tôi là ai
- Tên, nghề, đang sống và làm việc ở: <…>
- Làm những việc gì (mỗi việc một dòng): <…>
- Khách hàng hay người tôi phục vụ là ai: <…>

## Mục tiêu
- Mục tiêu năm nay: <…>
- Thước đo thành công của tôi: <…>

## Thế mạnh và điểm cần bù
- Mạnh nhất ở: <…>
- Không mạnh ở (AI nên đỡ phần này): <…>

## Nhịp làm việc
- Làm tốt nhất vào lúc: <…>
- Cách tôi ra quyết định: <…>
```

---

## `luat-lam-viec.md` (luật AI phải theo)

Luật 4 tới 8 là **5 điều học viên hay phải nhắc AI nhất** (học viên ghi ra ở bài tập bài 1).

```markdown
Mô tả: Luật AI phải theo khi làm việc với <tên>. Lời <tên> nói sau cùng là luật hiện hành.

# Luật làm việc

1. Ngôn ngữ và cách trả lời: <ví dụ: tiếng Việt, ý chính trước, ngắn gọn, viết đủ từ không viết tắt>
2. Trước khi làm việc lớn: <ví dụ: nói mục tiêu và các bước, chờ tôi duyệt rồi mới làm>
3. Không bao giờ: <ví dụ: hỏi mật khẩu, bịa đặt số liệu, tự quyết thay tôi việc tốn tiền>
4. <điều hay phải nhắc 1>
5. <điều hay phải nhắc 2>
6. <điều hay phải nhắc 3>
7. <điều hay phải nhắc 4>
8. <điều hay phải nhắc 5>
9. Lời mới nhất thắng: khi tôi đổi luật, sửa thẳng câu cũ ở đây, không thêm câu mới chồng lên.
```

---

## `trang-thai.md` (việc đang làm chưa xong)

```markdown
Mô tả: Trạng thái hiện tại: việc đang dở, việc tiếp theo, việc chờ <tên> quyết. Cập nhật cuối mỗi buổi.

# Trạng thái

| Việc | Đang ở đâu | Bước tiếp theo |
|---|---|---|
| <…> | <…> | <…> |

## Chờ tôi quyết
- <…>
```

---

## `truc-hoc.md` (trục học, tầng 0)

```markdown
Mô tả: Trục học của bộ não: cách nhận, lưu, nâng cấp mọi thông tin. Gần như không đổi; học thêm gì cũng đi qua đây.

# Trục học

Thước không đổi: một AI mới tinh, đọc ít nhất, vẫn làm đúng như tôi muốn, và lần sau đúng hơn lần trước.

## Bốn tầng (tầng càng cao càng ít đổi)
| Tầng | Chứa | Tên file | Đổi khi |
|---|---|---|---|
| 0 Trục | cửa vào, hồ sơ, luật, trục học | doc-truoc, ho-so, luat-lam-viec, truc-hoc | tôi chốt sau vài ngày |
| 1 Nguyên lý | vì sao làm vậy | nguyen-ly-<ten> | có ít nhất 3 chuyện cùng bài học |
| 2 Quy trình | các bước một loại việc | quy-trinh-<ten-viec> | cách làm lặp ít nhất 2 lần |
| 3 Dữ liệu | sổ, bài học, nguồn học, trạng thái, bài kiểm | du-an-, nguon-hoc-, bai-hoc, y-tuong, trang-thai, bai-kiem | thêm hằng ngày, chỉ thêm |
Trong tầng 1 và 2 mỗi ý chỉ một chỗ; nơi khác chỉ ghi tên file đó.
Đáp án bài kiểm, bản cũ và file đã cất nằm ngoài bộ não, không bao giờ tải lên.

## Sáu câu hỏi khi lưu
1. Là gì? (sự thật · quyết định · cách làm · ví dụ, số liệu)
2. Phục vụ mục tiêu nào trong ho-so.md? Không gắn được thì chỉ ghi vào y-tuong.md.
3. Đã có chỗ chưa? Có thì sửa thẳng câu cũ. Chưa thì ghi ở tầng 3 trước.
4. Vì sao đúng? Ghi ngắn lý do.
5. Nối vào đâu? Thêm dòng vào bảng file ở doc-truoc.md.
6. Kiểm thế nào? Câu kiểm nào sẽ cho biết nó giúp?

## Ba vòng học
| Vòng | Khi | Làm |
|---|---|---|
| Mỗi buổi | cuối buổi làm việc | lưu bằng sáu câu hỏi (câu lệnh 2); lỗi thành câu kiểm (câu lệnh 3) |
| Mỗi tuần | <thứ, giờ> | nhìn lại sổ (câu lệnh 4) |
| Nâng cấp | khoảng mỗi tháng | sao lưu, đo trước, dọn (câu lệnh 5), đo sau; kém hơn thì quay lại bản cũ |
```

---

## `bai-hoc.md` (sổ bài học)

```markdown
Mô tả: Sổ bài học: mỗi điều học được một dòng; dòng nhìn lại tuần; dòng các đợt nâng cấp.

## Bài học
| Ngày | Chuyện gì | Học được gì | Đã lưu vào |
|---|---|---|---|
| <ngày> | <…> | <…> | <file> |

## Nhìn lại tuần
| Tuần | Điều lặp | Đã đưa lên (quy trình, nguyên lý) | Câu kiểm mới |
|---|---|---|---|
| <ngày đầu tuần> | <…> hoặc "chưa có điều lặp" | <file> | <số câu> |

## Nâng cấp
| Ngày | Đo trước | Đo sau | Đã gom, gỡ, cất, viết rõ | Giữ bản mới? |
|---|---|---|---|---|
| <ngày> | <đúng>/<tổng> | <đúng>/<tổng> | <…> | có / quay lại bản cũ |
```

---

## `y-tuong.md` (ý tưởng chưa làm)

```markdown
Mô tả: Ý tưởng, dự định chưa gắn với mục tiêu nào trong ho-so.md. AI không coi đây là việc đang làm.

| Ngày | Ý tưởng | Khi nào xem lại |
|---|---|---|
| <ngày> | <…> | <…> |
```

---

## `du-an-<ten>.md` (sổ một dự án)

```markdown
Mô tả: Sổ dự án <tên dự án>: mục tiêu, mỗi buổi một dòng, đã làm gì, học được gì, đã lưu vào đâu.

Mục tiêu dự án: <…>

| Ngày | Đã làm | Học được | Đã lưu vào |
|---|---|---|---|
| <ngày> | <…> | <…> | <file> |
```

## `nguyen-ly-<ten>.md` (một nguyên lý)

```markdown
Mô tả: Nguyên lý <tên>: <một câu>.

# <Tên nguyên lý>
**Vì sao:** <một đến ba câu>
**Áp dụng khi:** <…>
**Chuyện thật:** 1. <…> 2. <…> 3. <…>
```

## `quy-trinh-<ten-viec>.md` (một quy trình)

```markdown
Mô tả: Quy trình <việc>: các bước, mỗi bước có chuẩn đạt.

| # | Bước | Đạt khi |
|---|---|---|
| 1 | <…> | <…> |
```
