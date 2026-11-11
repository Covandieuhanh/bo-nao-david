---
name: hoi-chuyen-gia
description: Luật hỏi của David — sản phẩm làm từ tài nguyên (video, bài đăng) thì KHÔNG hỏi, làm theo mặc định skill + đề xuất của Claude rồi báo lựa chọn; thiết kế lớn và sửa bộ não / skill / tài liệu thì Claude dừng lại, hỏi theo vòng từ góc nhìn chuyên gia thực chiến (nêu tên ngắn), mỗi câu 2–3 gợi ý có đề xuất đứng đầu; sự thật tự tra, quyết định David chốt; diễn giải lại ý hiểu và CHỜ David "ok" mới làm. Tự nhận diện lúc cần hỏi (6 tín hiệu), cả lúc bắt đầu lẫn giữa chừng. Dùng ở đầu mọi yêu cầu tạo/sửa, khi David nói "hỏi kỹ", "hỏi chuyên gia", "grill me", "/hoi-chuyen-gia", kể cả khi không nhắc. Không dùng cho câu hỏi nhanh, tra cứu, việc 1–2 bước.
---

# Hỏi chuyên gia trước khi làm

Đọc trước: `skills/thoi-quen-lam-viec.md`. File này là nhà của **cách hỏi và khi nào hỏi**; thoi-quen mục 2 giữ những gì không hỏi.

**Mục tiêu:** hỏi đúng câu trước khi làm để ra đúng ý ngay lần đầu, cho **người lần đầu dẫn người** (khách của David) và **người xem video** của David.

## Khi nào áp dụng

- **Áp (hỏi theo vòng, diễn giải, chờ "ok"):** thiết kế lớn (kế hoạch, chiến lược, skill hay quy trình mới) và sửa bộ não, skill,
  tài liệu, code.
- **Không hỏi — làm thẳng tới kết quả:** sản phẩm làm từ tài nguyên David đưa (video, highlight, podcast, bài đăng, bài viết). Điểm skill
  đã định thì theo skill; điểm chưa định Claude tự chọn; báo "đã chọn X vì Y" ở báo cáo cuối để David sửa ở bản cuối
  (`thoi-quen-lam-viec.md` mục 2). Giữa chừng chỉ dừng khi gặp tín hiệu nặng (dưới).
- **Không áp:** câu hỏi nhanh, tra cứu, giải thích, việc 1–2 bước → trả lời thẳng.
- **"Làm đi", "theo skill", câu không được trả lời** = chốt theo mặc định của skill, phần chưa định theo đề xuất của Claude. Đề xuất
  đứng đầu luôn là mặc định của skill khi skill đã định.
- **Không có David để trả lời** (việc tự động, lịch chạy): làm theo giả định hợp lý nhất, ghi rõ giả định ở đầu báo cáo.

## Sáu tín hiệu phải tự dừng hỏi

Lúc bắt đầu và cả giữa chừng, không đợi David yêu cầu. Với sản phẩm từ tài nguyên chỉ các tín hiệu **nặng** (1 khi làm đổi hẳn kết quả, 2, 3 khi đăng / xoá / khó đảo ngược, 5) mới dừng; tín hiệu 4 và 6 thì tự chọn theo mặc định + đề xuất và ghi vào báo cáo:
1. **Hiểu được nhiều cách**: câu mơ hồ, nhất là chữ đọc chính tả lệch làm đổi nghĩa — không tự đoán rồi làm.
2. **Mâu thuẫn** với luật, bộ nhớ, skill hoặc quyết định David đã chốt.
3. **Tốn thời gian / tiền / khó đảo ngược**: render > 10 phút, xoá, đăng, gửi tin, dịch vụ trả phí, sửa hàng loạt.
4. **Thiếu một quyết định làm đổi kết quả**: người xem, nền tảng, mục tiêu, phạm vi.
5. **Đang làm thì phát hiện vấn đề** làm đổi kế hoạch (thiếu file, nguồn kém, cách cũ không chạy).
6. **Sắp tự đặt một giả định** David chưa xác nhận.

Giữa chừng: dừng đúng bước bị ảnh hưởng, hỏi một vòng ngắn; phần không bị ảnh hưởng vẫn làm tiếp.
Không hỏi thừa: có mặc định rõ, hoặc sửa được ở bản cuối → tự làm, ghi một dòng "đã chọn X vì Y".

## Độ sâu

Claude tự xếp loại việc, David không cần nói "grill me":

| Loại việc | Cách hỏi |
|---|---|
| **Sản phẩm từ tài nguyên** (video, highlight, podcast, bài đăng) | **Không hỏi**: chạy một mạch tới kết quả, báo các lựa chọn đã làm |
| **Sửa một file / tài liệu / skill** | **Một vòng gộp** mọi điểm cần chọn; "ok" xong chạy một mạch |
| **Thiết kế lớn** (kế hoạch, chiến lược, skill hoặc quy trình mới) | **Nhiều vòng** tới khi hết điểm mờ |
| David nói **"grill me" / "hỏi kỹ"** | Nhiều vòng, kể cả việc nhỏ |

Mỗi vòng **tối đa 5 câu**. **Cây quyết định:** mỗi vòng chỉ hỏi câu đã đủ điều kiện (không phụ thuộc câu còn mở); câu phụ thuộc → vòng sau. Xong khi mọi nhánh đã đi qua.

**Sự thật Claude tự tra** (file, bộ nhớ, skill, web, công cụ), chạy song song; **quyết định hỏi David**. Không hỏi điều đã có hoặc tra được.

## Quy trình

1. Xác định lĩnh vực và loại việc (bảng trên).
2. **Vòng 1 mở bằng một dòng:** `Góc nhìn tổng hợp từ: <tên>, <tên>, …` — chuyên gia **có thật**, thực chiến đúng lĩnh vực, tối đa 10 tên. Không chắc thì nêu ít hơn, không bịa. Vòng sau không lặp.
3. **Các câu hỏi**, mỗi câu: đánh số, tiêu đề ngắn, một ý; **2–3 gợi ý, đề xuất đứng đầu**, "đồng ý" = nhận đề xuất. Ưu tiên điều đổi kết quả. Câu nhiều phương án có thể dùng AskUserQuestion.
4. David trả lời (thường bằng giọng nói): hiểu theo ý, chấp nhận chữ lệch; chỉ hỏi lại khi hiểu được nhiều cách (tín hiệu 1). Thiết kế lớn → vòng tiếp.
5. **Diễn giải lại** 3–6 dòng: làm gì, cho ai, ra gì, ở đâu, theo luật nào, cái gì **không** làm. Kèm một dòng **Mục tiêu** và 2–4 dòng **Xong khi** (`thoi-quen-lam-viec.md` mục 5).
6. **Chờ "ok"** ("ok", "đồng ý", "đúng", "làm đi"). Chưa có thì không tạo, không sửa file nào. David sửa ý → diễn giải lại phần đổi, chờ lần nữa.
7. Làm xong: báo cáo theo `thoi-quen-lam-viec.md` mục 4.

Nội dung là của David (`AGENTS.md` luật 4): không đề xuất khuôn lời cho David nói.

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
- 2026-11-11 · David: "Hạn chế hỏi những thứ theo tiêu chí nhất có thể… mục tiêu cuối cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong." Nguyên nhân: video cuộc gọi hợp tác, Claude đưa khung hình vào câu hỏi dù skill đã định khung = gốc, đề xuất đầu (dọc) trái mặc định, David không trả lời câu đó → Claude lấy đề xuất của mình, làm sai. Sửa: sản phẩm từ tài nguyên không hỏi; đề xuất đứng đầu = mặc định skill; câu không trả lời / "làm đi" = theo mặc định; chỉ tín hiệu nặng mới dừng. Thay luật cũ "làm đi ≠ chốt lựa chọn".
## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng `dang-lam/tai-ban-2-hoi.md` (24 dòng; không bỏ luật nào). Bỏ dấu "(chốt 05/11/2026)" và ví dụ có ngày ở tín hiệu 1 (chuyện 05/11: Claude tự đoán câu "không biết thông tin nào khi mà đăng lên" rồi render → sai; giữ ở ghi nhớ `luat-tu-hoi-khi-mo-ho`). Gộp hai câu "tự tra / không hỏi điều tra được" làm một; "tối đa 5 câu" nói một lần; thêm lại "Claude tự xếp loại việc" (luật bản đầu bị rơi ở lần chuẩn hoá); ghi rõ chữ lệch chỉ hỏi lại khi hiểu được nhiều cách; ngoại lệ tự chọn + phần cứng không hỏi trỏ về thoi-quen mục 2; "nội dung của David" trỏ AGENTS luật 4.
- 2026-11-05 · học grill-me / grilling (mattpocock/skills): hỏi theo vòng theo cây quyết định, đề xuất "đồng ý" được, sự thật tự tra, nhiều vòng cho việc lớn.
- 2026-11-05 · tự nhận diện lúc cần hỏi (6 tín hiệu), hỏi cả giữa chừng — David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): mỗi câu 2–3 gợi ý đề xuất đứng đầu; khách = người lần đầu dẫn người + người xem, bỏ "kinh doanh"; sản phẩm một vòng gộp, thiết kế lớn nhiều vòng; "làm đi" ≠ chốt lựa chọn; trỏ `thoi-quen-lam-viec.md`; rút mô tả, bỏ mục lặp; thêm "Xong khi".
