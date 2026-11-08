---
name: hoi-chuyen-gia
description: Luật của David trước khi TẠO hoặc SỬA bất kỳ sản phẩm nào (file, skill, tài liệu, video, kịch bản, bài đăng, code) — Claude dừng lại, hỏi theo vòng từ góc nhìn chuyên gia thực chiến (nêu tên ngắn), mỗi câu 2–3 gợi ý có đề xuất đứng đầu; sự thật tự tra, quyết định David chốt; diễn giải lại ý hiểu và CHỜ David "ok" mới làm. Tự nhận diện lúc cần hỏi (6 tín hiệu), cả lúc bắt đầu lẫn giữa chừng. Dùng ở đầu mọi yêu cầu tạo/sửa sản phẩm, khi David nói "hỏi kỹ", "hỏi chuyên gia", "grill me", "/hoi-chuyen-gia", kể cả khi không nhắc. Không dùng cho câu hỏi nhanh, tra cứu, việc 1–2 bước.
---

# Hỏi chuyên gia trước khi làm

Đọc trước: `skills/thoi-quen-lam-viec.md` (thói quen chung; mục 2 là khi nào hỏi, file này là cách hỏi).

**Mục tiêu:** hỏi đúng câu trước khi làm để ra đúng ý ngay lần đầu, cho **người lần đầu dẫn người** (khách của David) và **người xem video** của David.

## Khi nào áp dụng

- **Áp:** mọi yêu cầu tạo hoặc sửa sản phẩm: file, skill, tài liệu, video, kịch bản, bài đăng, kế hoạch, code.
- **Không áp:** câu hỏi nhanh, tra cứu, giải thích, việc 1–2 bước không tạo sản phẩm → trả lời thẳng.
- **David nói đủ / "làm đi":** bỏ những câu đã có lời đáp, **vẫn diễn giải** và chờ "ok". "Làm đi" chỉ cho phép làm việc được giao, **không chốt các lựa chọn** bên trong nó (chữ, hình, câu chốt…); lựa chọn nào chưa được trả lời vẫn phải hỏi.
- **Ngoại lệ được tự chọn** (cắt highlight, làm lại video cũ): xem `thoi-quen-lam-viec.md` mục 2.
- **Không có David để trả lời** (việc tự động, lịch chạy): làm theo giả định hợp lý nhất, ghi rõ giả định ở đầu báo cáo.

## Sáu tín hiệu phải tự dừng hỏi (chốt 05/11/2026)

Lúc bắt đầu và cả giữa chừng, không đợi David yêu cầu:
1. **Hiểu được nhiều cách**: câu mơ hồ, nhất là chữ đọc chính tả lệch (05/11 Claude tự đoán "không biết thông tin nào khi mà đăng lên" rồi render → sai).
2. **Mâu thuẫn** với luật, bộ nhớ, skill hoặc quyết định David đã chốt.
3. **Tốn thời gian / tiền / khó đảo ngược**: render > 10 phút, xoá, đăng, gửi tin, dịch vụ trả phí, sửa hàng loạt.
4. **Thiếu một quyết định làm đổi kết quả**: người xem, nền tảng, mục tiêu, phạm vi.
5. **Đang làm thì phát hiện vấn đề** làm đổi kế hoạch (thiếu file, nguồn kém, cách cũ không chạy).
6. **Sắp tự đặt một giả định** David chưa xác nhận.

Giữa chừng: dừng đúng bước bị ảnh hưởng, hỏi một vòng ngắn; phần không bị ảnh hưởng vẫn làm tiếp.
Không hỏi thừa: chuyện nhỏ có mặc định rõ, không đổi thứ người xem thấy/nghe, đảo ngược dễ → tự làm, ghi một dòng "đã chọn X vì Y".

## Độ sâu

| Loại việc | Cách hỏi |
|---|---|
| **Làm ra sản phẩm** (video, bài, sửa một file/tài liệu) | **Một vòng gộp** mọi điểm cần chọn, tối đa 5 câu; "ok" xong chạy một mạch |
| **Thiết kế lớn** (kế hoạch, chiến lược, skill hoặc quy trình mới) | **Nhiều vòng** tới khi hết điểm mờ, mỗi vòng tối đa 5 câu |
| David nói **"grill me" / "hỏi kỹ"** | Nhiều vòng, kể cả việc nhỏ |

**Cây quyết định:** mỗi vòng chỉ hỏi câu đã đủ điều kiện (không phụ thuộc câu còn mở); câu phụ thuộc → vòng sau. Xong khi mọi nhánh đã đi qua.

**Sự thật Claude tự tra** (file, bộ nhớ, skill, web, công cụ), chạy song song; **quyết định hỏi David**.

## Quy trình

1. Xác định lĩnh vực và loại việc (bảng trên).
2. **Vòng 1 mở bằng một dòng:** `Góc nhìn tổng hợp từ: <tên>, <tên>, …` — chuyên gia **có thật**, thực chiến đúng lĩnh vực, tối đa 10 tên. Không chắc thì nêu ít hơn, không bịa. Vòng sau không lặp.
3. **Tối đa 5 câu**, mỗi câu: đánh số, tiêu đề ngắn, một ý; **2–3 gợi ý, đề xuất đứng đầu**, "đồng ý" = nhận đề xuất. Ưu tiên điều đổi kết quả. Không hỏi điều đã có hoặc tra được. Câu nhiều phương án có thể dùng AskUserQuestion.
4. David trả lời (thường bằng giọng nói: hiểu theo ý, chấp nhận chữ lệch). Thiết kế lớn → vòng tiếp.
5. **Diễn giải lại** 3–6 dòng: làm gì, cho ai, ra gì, ở đâu, theo luật nào, cái gì **không** làm. Kèm một dòng **Mục tiêu** và 2–4 dòng **Xong khi** (`thoi-quen-lam-viec.md` mục 5).
6. **Chờ "ok"** ("ok", "đồng ý", "đúng", "làm đi"). Chưa có thì không tạo, không sửa file nào. David sửa ý → diễn giải lại phần đổi, chờ lần nữa.
7. Làm xong: báo cáo theo `thoi-quen-lam-viec.md` mục 4.

Nội dung là của David: không đề xuất khuôn lời cho David nói.

## Mẫu một vòng

```
Góc nhìn tổng hợp từ: A, B, C, D, E…        ← chỉ vòng 1

❓ Q1 · <tiêu đề>: <câu hỏi>
➡️ <đề xuất> · hoặc <gợi ý 2> · hoặc <gợi ý 3>

❓ Q2 · …

(Thiết kế lớn: "Còn vòng sau về <nhánh còn mở>.")
Ý hiểu: <3–6 dòng>.                          ← khi hết điểm mờ
Bạn trả lời "đồng ý" hoặc sửa câu nào nhé.
```

## Xong khi

1. Vòng 1 mở bằng một dòng tên chuyên gia có thật; vòng sau không lặp.
2. Mỗi vòng ≤ 5 câu, câu nào cũng có 2–3 gợi ý, đề xuất đứng đầu.
3. Không câu nào hỏi điều đã có trong file, bộ nhớ hoặc tra được.
4. Có diễn giải 3–6 dòng, nói rõ cả điều **không** làm, kèm Mục tiêu và Xong khi.
5. Không file nào bị tạo/sửa trước khi David "ok".
6. Giữa chừng gặp tín hiệu thì dừng đúng bước, không tự đoán.
7. Sau "ok" làm một mạch, không phải làm lại vì hiểu sai.

## Nhật ký
- 2026-11-05 · học grill-me / grilling (mattpocock/skills): hỏi theo vòng theo cây quyết định, đề xuất "đồng ý" được, sự thật tự tra, nhiều vòng cho việc lớn.
- 2026-11-05 · tự nhận diện lúc cần hỏi (6 tín hiệu), hỏi cả giữa chừng — David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): mỗi câu 2–3 gợi ý đề xuất đứng đầu; khách = người lần đầu dẫn người + người xem, bỏ "kinh doanh"; sản phẩm một vòng gộp, thiết kế lớn nhiều vòng; "làm đi" ≠ chốt lựa chọn; trỏ `thoi-quen-lam-viec.md`; rút mô tả, bỏ mục lặp; thêm "Xong khi".
