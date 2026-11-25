---
description: "Biểu mẫu 03 gói dựng bộ não: khuôn bài kiểm (câu hỏi trong bộ não, đáp án để ngoài), câu kiểm tốt trông thế nào, cách chấm theo tỉ lệ."
---

# Biểu mẫu 03 · Mẫu bài kiểm

Bài kiểm là cách duy nhất biết chắc bộ não dạy AI đúng hay không. **Câu hỏi và đáp án tách hai file:**
- `bo-nao/bai-kiem.md`: chỉ câu hỏi, tải lên cùng bộ não (tầng 3), có dòng trong bảng file ở `doc-truoc.md`.
- `ngoai-bo-nao/dap-an.md`: đáp án, **không bao giờ tải lên AI**. Vì nằm ngoài bộ não nên không cần dòng trong bảng file.

## `bai-kiem.md`

```markdown
Mô tả: Bài kiểm người đọc mới: câu hỏi tình huống để thử AI mới có hiểu đúng bộ não không. Không có đáp án ở đây.

## Câu 1
Tình huống: <chuyện thật đã xảy ra, kể ngắn>
Câu hỏi: <AI nên làm gì?>
A. <…>  B. <…>  C. <…>  D. <…>

## Câu 2
…
```

## `dap-an.md`

```markdown
Mô tả: Đáp án bài kiểm. Giữ ngoài bộ não, không tải lên khi chạy bài kiểm người đọc mới.

| Câu | Đáp án | Vì sao | Nằm ở file | Từ lỗi ngày |
|---|---|---|---|---|
| 1 | B | <…> | luat-lam-viec.md luật 4 | <ngày> |
```

## Câu kiểm tốt
- **Lấy từ lỗi thật** (lần mình phải sửa AI), không tự nghĩ ra câu dễ.
- **Là tình huống**, không phải câu đố trí nhớ. Tốt: "Khách nhắn hỏi giá lúc 23 giờ, AI soạn trả lời thế nào?". Kém: "Luật số 4 là gì?".
- **Các lựa chọn sai đều nghe hợp lý**: mỗi lựa chọn sai là một cách AI từng làm sai hoặc dễ làm sai.
- **Đáp án chỉ ra đúng file** trong bộ não. Không chỉ ra được file nào thì bộ não đang thiếu: thêm vào bộ não trước.
- Buổi 3 có ít nhất 5 câu; tới nghiệm thu có ít nhất 10 câu. Sau đó mỗi lỗi mới thêm một câu. Bài kiểm chỉ lớn lên, không bỏ câu.

## Chấm
**Chuẩn đạt: đúng ít nhất 90% số câu** (10 câu thì đúng ít nhất 9; 20 câu thì đúng ít nhất 18). Câu đúng nhưng AI ghi "phải tự suy" vẫn tính đúng, nhưng phải viết rõ lại file.

| Kết quả từng câu | Làm gì |
|---|---|
| Đúng, AI chỉ ra đúng file | giữ nguyên |
| Đúng nhưng AI ghi "phải tự suy" | file chưa nói rõ: viết rõ hơn |
| Sai | tìm file làm AI hiểu sai, sửa file đó; không sửa câu kiểm |

Ghi điểm vào bảng "Nâng cấp" của `bai-hoc.md`. Đạt tối đa ngay lần đầu thì câu còn dễ: thêm câu khó hơn từ lỗi mới.
