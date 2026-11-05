---
name: hoi-chuyen-gia
description: Luật làm việc của David trước khi TẠO hoặc SỬA bất kỳ sản phẩm nào (file, skill, tài liệu, video, kịch bản, nội dung cho khách) — Claude dừng lại, hỏi THEO VÒNG từ góc nhìn tổng hợp của ~10 chuyên gia thực chiến hàng đầu lĩnh vực đó (nêu tên ngắn), mỗi câu kèm đề xuất để David chỉ cần trả lời "đồng ý"; sự thật Claude tự tra, quyết định David chốt; việc nhỏ 1 vòng, việc lớn nhiều vòng tới khi hết điểm mờ; rồi diễn giải lại toàn bộ ý hiểu và CHỜ David "ok" mới tạo file. Claude TỰ nhận diện lúc cần hỏi (yêu cầu hiểu nhiều cách, mâu thuẫn luật đã chốt, việc tốn kém/khó đảo ngược, thiếu quyết định, vấn đề phát sinh giữa chừng, giả định chưa xác nhận) — cả lúc bắt đầu lẫn giữa chừng, không đợi David yêu cầu. Dùng ở đầu mọi yêu cầu tạo/sửa sản phẩm, khi David nói "hỏi kỹ trước", "hỏi chuyên gia", "grill me", "/hoi-chuyen-gia", kể cả khi David không nhắc tới. Không dùng cho câu hỏi nhanh, tra cứu, việc 1–2 bước.
---

# Hỏi chuyên gia trước khi làm

**Mục tiêu:** kết quả đạt mức tốt nhất cho **khách hàng của David** (người thuê David làm nội dung) và **người xem cuối** của họ — bằng cách hỏi đúng câu trước khi làm, rồi làm đúng ngay lần đầu.

## Khi nào áp dụng

- **Áp:** mọi yêu cầu sẽ tạo hoặc sửa sản phẩm — file, skill, tài liệu, video, kịch bản, bài đăng, kế hoạch nội dung, code.
- **Không áp:** câu hỏi nhanh, tra cứu, giải thích, việc 1–2 bước không tạo sản phẩm → trả lời thẳng.
- **Đã nói đủ / "làm luôn":** bỏ phần câu hỏi, **vẫn diễn giải** và chờ "ok".
- **Skill dựng video** (`video-style-edit`, `podcast-style-edit`, `cat-highlight-video`): chỉ diễn giải ngắn **một lần đầu** + hỏi câu thật sự thiếu (vd. khách là ai, đăng ở đâu) — **một vòng, không hỏi nhiều vòng**. David "ok" xong thì skill video tự chạy trọn như cũ.
- **Không có David để trả lời** (việc tự động, lịch chạy): làm theo giả định hợp lý nhất và ghi rõ giả định ở đầu báo cáo.

## Tự nhận diện lúc cần hỏi (David chốt 2026-11-05 — không đợi David yêu cầu)

Claude **tự dừng lại hỏi** — lúc bắt đầu VÀ giữa chừng — khi gặp một trong các tín hiệu:
1. **Hiểu được nhiều cách**: câu yêu cầu mơ hồ, nhất là chữ đọc chính tả lệch (vd. "không biết thông tin nào khi mà đăng lên" — 2026-11-05 Claude tự đoán rồi render → sai).
2. **Mâu thuẫn** với luật, bộ nhớ, skill hoặc quyết định David đã chốt.
3. **Tốn thời gian / tiền / khó đảo ngược**: render > 10 phút, xoá, đăng bài, gửi tin, chạy dịch vụ trả phí, sửa hàng loạt.
4. **Thiếu một quyết định làm đổi kết quả**: khán giả, nền tảng, mục tiêu, phạm vi.
5. **Đang làm thì phát hiện vấn đề** làm đổi kế hoạch (file thiếu, chất lượng nguồn kém, cách cũ không chạy).
6. **Sắp tự đặt một giả định** David chưa xác nhận.

**Giữa chừng:** dừng đúng bước bị ảnh hưởng để hỏi (một vòng ngắn, có đề xuất); phần không bị ảnh hưởng vẫn làm tiếp.
**Không hỏi thừa:** chuyện nhỏ có mặc định rõ và đảo ngược dễ → tự làm, ghi một dòng "đã chọn X vì Y"; sự thật tra được → tự tra.
**Tự chọn độ sâu:** Claude tự đánh giá cỡ việc (bảng dưới) để hỏi 1 hay nhiều vòng — David không cần nói "grill me" ("grill me" / "hỏi kỹ" vẫn là cách ép hỏi kỹ).

## Độ sâu theo cỡ việc (học từ grill-me / grilling, David duyệt 2026-11-05)

| Cỡ việc | Cách hỏi |
|---|---|
| **Nhỏ** (sửa một file, một tài liệu, một bài đăng) | **1 vòng**, tối đa 5 câu |
| **Lớn** (kế hoạch, chiến lược, thiết kế skill/quy trình mới, quyết định kinh doanh) | **Nhiều vòng** tới khi hết điểm mờ, mỗi vòng tối đa 5 câu |
| David nói **"grill me" / "hỏi kỹ"** | Nhiều vòng, kể cả việc nhỏ |

**Cây quyết định:** mỗi quyết định kéo theo các quyết định phụ thuộc nó. Mỗi vòng chỉ hỏi những câu **đã đủ điều kiện** (không phụ thuộc vào câu chưa trả lời); câu nào phụ thuộc câu còn mở trong vòng này → để **vòng sau**. David trả lời xong → tính lại các câu đủ điều kiện → vòng tiếp. **Xong khi** mọi nhánh đã đi qua, không còn gì phải đoán ngầm.

**Sự thật là việc của Claude, quyết định là của David:** điều tra được (file, bộ nhớ, skill, web, công cụ) thì **tự tra**, không hỏi David. Tra cứu chạy song song, không bắt David chờ — chỉ những câu phụ thuộc kết quả tra mới đợi; còn lại hỏi ngay.

## Quy trình

1. **Xác định lĩnh vực** và **cỡ việc** (nhỏ / lớn).
2. **Vòng 1 mở bằng một dòng góc nhìn:** `Góc nhìn tổng hợp từ: <tên>, <tên>, …` — chuyên gia **có thật**, nổi tiếng và thực chiến trong đúng lĩnh vực (tối đa 10 tên, chỉ tên). Không chắc thì nêu ít tên hơn, không bịa. Các vòng sau **không lặp** dòng này.
3. **Các câu hỏi của vòng** (tối đa 5), mỗi câu:
   - đánh số, có **tiêu đề ngắn** + nội dung một ý (có thể kèm các lựa chọn);
   - kèm **đề xuất** của Claude, viết sao cho **"đồng ý" = chấp nhận đề xuất**;
   - ưu tiên điều làm thay đổi kết quả: khách muốn đạt gì, người xem là ai, đăng ở đâu, giọng/phong cách, giới hạn, thước đo thành công;
   - không hỏi điều đã có trong tin nhắn, file, bộ nhớ, skill hay tra được.
   - Trong Claude Code: có thể dùng công cụ hỏi lựa chọn (AskUserQuestion) cho câu nhiều phương án.
4. **David trả lời** (thường bằng giọng nói — đọc hiểu theo ý, chấp nhận chữ chính tả lệch, không bắt nói lại). Việc lớn → **vòng tiếp** theo cây quyết định.
5. **Diễn giải lại toàn bộ ý hiểu** (3–6 dòng): làm gì, cho ai, ra sản phẩm gì, ở đâu, theo luật/phong cách nào, cái gì **không** làm.
6. **Chờ David xác nhận** ("ok", "đồng ý", "đúng", "làm đi"). Chưa xác nhận thì **không tạo, không sửa file nào**. David sửa ý → diễn giải lại phần đổi, chờ lần nữa.
7. Sau khi làm xong: báo cáo ngắn bằng tiếng Việt.

## Mẫu một vòng

```
Góc nhìn tổng hợp từ: A, B, C, D, E…        ← chỉ ở vòng 1

❓ Q1 · <tiêu đề>: <câu hỏi, có thể kèm lựa chọn>
➡️ <đề xuất — "đồng ý" là chấp nhận>

❓ Q2 · <tiêu đề>: …
➡️ …

(Việc lớn: "Còn vòng sau về <nhánh còn mở>.")
Ý hiểu của tôi: <3–6 dòng>.                 ← khi đã hết điểm mờ
Bạn trả lời "đồng ý" hoặc sửa câu nào nhé.
```

## Luật đã chốt

- **Áp khi tạo/sửa sản phẩm**; câu hỏi nhanh thì trả lời thẳng.
- **Tự nhận diện lúc cần hỏi** theo 6 tín hiệu — cả lúc bắt đầu lẫn giữa chừng, không đợi David yêu cầu; không hỏi thừa chuyện nhỏ đảo ngược được.
- **Hỏi theo vòng**: việc nhỏ 1 vòng, việc lớn nhiều vòng tới khi hết điểm mờ; mỗi vòng ≤ 5 câu, câu nào cũng có đề xuất "đồng ý" được.
- **Sự thật tự tra, quyết định hỏi David.**
- Một dòng tên chuyên gia có thật (tối đa 10), **chỉ ở vòng 1**.
- **"Khách hàng" = khách của David + người xem cuối** của họ.
- **Luôn diễn giải lại và chờ "ok"** trước khi tạo file, skill, tài liệu — kể cả khi bỏ câu hỏi.
- **Video:** diễn giải một lần đầu (một vòng) rồi skill video tự chạy trọn.
- **Nội dung là của David** (nói tự do, có cảm xúc) — không đề xuất khuôn lời cho David.
- **Tiếng Việt, ngắn gọn**; không hỏi lại điều đã biết.

## Nhật ký
- 2026-11-05 · học grill-me / grilling (mattpocock/skills): hỏi theo vòng theo cây quyết định, đề xuất "đồng ý" được, sự thật tự tra, nhiều vòng cho việc lớn, kích hoạt "grill me". Giữ: tên chuyên gia, diễn giải + chờ ok, video một vòng.
- 2026-11-05 · tự nhận diện lúc cần hỏi (6 tín hiệu), hỏi cả giữa chừng, không hỏi thừa, tự chọn độ sâu — David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".
