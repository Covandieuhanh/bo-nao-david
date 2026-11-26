---
name: thu-thap-yeu-cau
description: Cách Claude hỏi David khi trình 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi) trước việc chưa có quy trình (việc đã có quy trình thì tự động hoàn toàn, không hỏi) — hỏi theo vòng từ góc nhìn chuyên gia thực chiến, mỗi điểm cần chốt có 2–3 gợi ý với đề xuất đứng đầu; sự thật thì Claude tự tra, quyết định thì David chốt; Claude chờ David "duyệt" rồi mới tạo hay sửa file; duyệt rồi làm trọn không ngắt quãng. Claude tự nhận diện 6 tín hiệu phải dừng lại để hỏi, cả lúc bắt đầu lẫn giữa chừng. Dùng khi trình 4 phần cho một việc, khi David nói "hỏi kỹ", "hỏi chuyên gia", "grill me", "/thu-thap-yeu-cau". Không dùng cho câu hỏi nhanh, tra cứu.
---

# Hỏi chuyên gia trước khi làm

Tài liệu đọc trước: [chuan-muc-lam-viec.md](../chuan-muc-lam-viec.md). Luật **đã có quy trình thì tự động hoàn toàn; chưa có quy trình thì trình 4 phần, chờ "duyệt", duyệt rồi làm trọn**, phần miễn và cách chọn từng điểm (mặc định của skill, "làm đi") nằm ở `chuan-muc-lam-viec.md` mục 2. File này là nguồn của **cách hỏi** trong 4 phần: điểm nào cần chốt, hỏi thế nào, sâu tới đâu, khi nào phải dừng hỏi.

**Mục tiêu:** Claude hỏi đúng câu trước khi làm để ra kết quả đúng ý ngay lần đầu, phục vụ khách và người xem của David ở cả ba hướng nghề (`co-so-tri-thuc/david.md` 4.1).

Skill này không dùng cho câu hỏi nhanh, tra cứu, giải thích (Claude trả lời thẳng) và lịch tự chạy đã duyệt (Claude làm theo lời giao, ghi giả định ở đầu báo cáo).

## Sáu tín hiệu phải tự dừng lại để hỏi

Khi được giao thực hiện việc đã có quy trình: tự chạy theo luật 2 của AGENTS.md; chỉ dừng ở các trường hợp của `chuan-muc-lam-viec.md` mục 2 ("Chỉ dừng hỏi khi"), tín hiệu còn lại tự chọn và ghi báo cáo. Việc chưa có quy trình, lúc trình 4 phần: Claude gom mọi tín hiệu vào các điểm cần chốt. Sau khi David duyệt, giữa chừng chỉ các tín hiệu **nặng** (tín hiệu 1 khi việc làm đổi hẳn kết quả, tín hiệu 2, tín hiệu 3 khi đăng, xoá hay khó đảo ngược, tín hiệu 5) mới khiến Claude dừng; với tín hiệu 4 và 6, Claude tự chọn theo mặc định và đề xuất rồi ghi vào báo cáo:
1. **Hiểu được nhiều cách**: câu mơ hồ, nhất là chữ đọc chính tả bị lệch làm đổi nghĩa; Claude không tự đoán rồi làm.
2. **Mâu thuẫn** với luật, bộ nhớ, skill hoặc quyết định David đã chốt.
3. **Tốn thời gian, tốn tiền hoặc khó đảo ngược**: render quá 10 phút (Claude chỉ nêu trong 4 phần; giữa chừng thì chạy nền, không dừng), xoá, đăng, gửi tin nhắn, dịch vụ trả phí, sửa hàng loạt.
4. **Thiếu một quyết định làm đổi kết quả**: người xem, nền tảng, mục tiêu, phạm vi.
5. **Đang làm thì phát hiện vấn đề** làm đổi kế hoạch (thiếu file, nguồn chất lượng kém, cách làm cũ không chạy được).
6. **Sắp tự đặt một giả định** David chưa xác nhận.

Giữa chừng: Claude dừng đúng bước bị ảnh hưởng, hỏi một vòng ngắn; phần không bị ảnh hưởng vẫn làm tiếp.
Không hỏi thừa: điểm nào có mặc định rõ, hoặc sửa được ở bản cuối, thì Claude tự làm và ghi một dòng "đã chọn X vì Y".

## Độ sâu

Claude tự xếp loại việc, David không cần nói "grill me":

| Loại việc | Cách hỏi |
|---|---|
| **Sản phẩm từ tài nguyên** (video, highlight, podcast, bài đăng) | **Đã có quy trình (lá B1): không hỏi**, tự làm trọn theo mặc định của skill; điểm skill chưa định thì tự chọn theo tiêu chí của skill, ghi "đã chọn X vì Y" trong báo cáo |
| **Sửa một file, tài liệu hoặc skill** | góp ý của David hay vòng tự học: tự sửa theo quy trình, báo sau; việc mới chưa có quy trình: **4 phần kèm một vòng gộp** mọi điểm cần chọn, có "duyệt" thì chạy liên tục |
| **Thiết kế lớn** (kế hoạch, chiến lược, skill hoặc quy trình mới) | **Nhiều vòng** tới khi hết điểm chưa rõ |
| David nói **"grill me" / "hỏi kỹ"** | Nhiều vòng, kể cả việc nhỏ |

Mỗi vòng **tối đa 5 câu**. **Cây quyết định:** mỗi vòng Claude chỉ hỏi câu đã đủ điều kiện (không phụ thuộc câu còn bỏ ngỏ); câu phụ thuộc thì để vòng sau. Xong khi mọi nhánh đã được đi qua.

**Sự thật thì Claude tự tra** (file, bộ nhớ, skill, web, công cụ), chạy song song; **quyết định thì hỏi David**. Claude không hỏi điều đã có hoặc tra được.

## Quy trình

1. Claude xác định lĩnh vực và loại việc (theo bảng trên).
2. **Vòng 1 mở bằng một dòng:** `Góc nhìn tổng hợp từ: <tên>, <tên>, …` gồm các chuyên gia **có thật**, thực chiến đúng lĩnh vực, tối đa 10 tên. Không chắc thì Claude nêu ít hơn, không bịa đặt. Vòng sau không lặp lại dòng này.
3. **Các câu hỏi**, mỗi câu: đánh số, tiêu đề ngắn, một ý; **2–3 gợi ý, đề xuất đứng đầu**, "đồng ý" nghĩa là nhận đề xuất. Claude ưu tiên điều làm đổi kết quả. Câu nhiều phương án có thể dùng AskUserQuestion.
4. David trả lời (thường bằng giọng nói): Claude hiểu theo ý, chấp nhận chữ bị lệch; chỉ hỏi lại khi hiểu được nhiều cách (tín hiệu 1). Thiết kế lớn thì mở vòng tiếp theo.
4b. **Thiết kế lớn (nhiều vòng): Claude ghi ngay vào file** `du-an/phong-van/<ngày>-<chủ-đề>.md` sau mỗi câu trả lời: câu hỏi · đề xuất · **đã chốt**.
   Phiên dài hay phiên bị ngắt vẫn không mất gì; cuối buổi Claude thêm phần tóm tắt các quyết định và việc còn bỏ ngỏ.
5. **Trình 4 phần** khi hết điểm chưa rõ: Mục tiêu (một dòng kèm 2–4 dòng **Xong khi**, `chuan-muc-lam-viec.md` mục 5) · Kế hoạch (diễn giải 3–6 dòng: làm gì, cho ai, ra gì, ở đâu, theo luật nào, cái gì **không** làm; "chọn X vì Y") · Quy trình · Thực thi.
6. **Chờ "duyệt"** ("duyệt", "ok", "đồng ý", "đúng", "làm đi" đều tính). Chưa có lời duyệt thì Claude không tạo, không sửa file nào. David sửa phần nào thì Claude trình lại phần đó và chờ lần nữa.
7. Làm xong: Claude báo cáo theo `chuan-muc-lam-viec.md` mục 4.

Nội dung là của David (`chuan-muc-lam-viec.md` mục 0, ghi nhớ [quy-tac-noi-dung-cua-david](../../co-so-tri-thuc/bo-nho/quy-tac-noi-dung-cua-david.md)): Claude không đề xuất mẫu lời cho David nói.

Khi đầu ra là bảng giao việc, tra [cách lập bảng giao việc](../quy-trinh-van-hanh-chung.md#2a-lập-bảng-giao-việc). Đọc nguồn đang có trước vòng hỏi và xác nhận cách đo mục tiêu trước khi chia việc.

## Mẫu một vòng

```
Góc nhìn tổng hợp từ: A, B, C, D, E…        ← chỉ vòng 1

❓ Q1 · <tiêu đề>: <câu hỏi>
➡️ <đề xuất> · hoặc <gợi ý 2> · hoặc <gợi ý 3>

❓ Q2 · …

(Thiết kế lớn: "Còn vòng sau về <nhánh còn mở>.")
4 phần: Mục tiêu · Kế hoạch · Quy trình · Thực thi   ← khi hết điểm mờ
Bạn trả lời "đồng ý" / "duyệt" hoặc sửa câu nào nhé.
```

## Xong khi

1. Vòng 1 mở bằng một dòng tên chuyên gia có thật; vòng sau không lặp lại dòng này.
2. Mỗi vòng tối đa 5 câu, câu nào cũng có 2–3 gợi ý, đề xuất đứng đầu.
3. Không câu nào hỏi điều đã có trong file, bộ nhớ, đã được skill định, hoặc tra được.
4. 4 phần có diễn giải 3–6 dòng, nói rõ cả điều **không** làm, kèm Mục tiêu và Xong khi.
5. Không file nào bị tạo hay sửa trước khi David "duyệt" 4 phần. Sau duyệt: Claude không hỏi gì ngoài tín hiệu nặng, báo cáo cuối có đủ "đã chọn X vì Y".
6. Giữa chừng gặp tín hiệu thì Claude dừng đúng bước, không tự đoán.
7. Sau "duyệt" Claude làm liên tục không ngắt quãng, không phải làm lại vì hiểu sai.
8. Thiết kế lớn: mọi câu đã chốt nằm trong file phỏng vấn, có phần tóm tắt cuối buổi.

## Nhật ký
## Tái bản 3 — 14/11/2026: bản luật viết lại từ bảng `du-an/nang-cap/tai-ban-3-hoi.md` (24 dòng; không bỏ luật nào). Luật "trình 4 phần trước mọi việc, chờ duyệt" (việc #22) cùng phần miễn, cách chọn từng điểm, "làm đi" nghĩa là theo mặc định, hoc-lien-tuc: nguồn duy nhất là `chuan-muc-lam-viec.md` mục 2, skill chỉ còn một dòng trỏ về. Bỏ hàng trùng "sản phẩm từ tài nguyên" (đã có ở bảng Độ sâu). Diễn giải 3–6 dòng ghép vào bước trình 4 phần; "chờ ok" thành "chờ duyệt". Sửa tên cũ "thoi-quen" thành `chuan-muc-lam-viec.md`. "Nội dung của David" trỏ về chuẩn mực làm việc mục 0 và ghi nhớ (AGENTS luật 4 nay là luật về mạng xã hội).
- 2026-11-14 · Claude học từ bài "16 bài học sau 1000 giờ dùng Claude" (Nhật Anh AI, mẹo 5): skill grill-me bản tiếng Việt ghi từng câu trả lời vào file ngay, nên thêm bước 4b và Xong khi 8.
- 2026-11-11 · David: "Hạn chế hỏi những thứ theo tiêu chí nhất có thể… mục tiêu cuối cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong." Nguyên nhân: ở video cuộc gọi hợp tác, Claude đưa khung hình vào câu hỏi dù skill đã định khung theo gốc, đề xuất đứng đầu (dọc) trái với mặc định, David không trả lời câu đó thì Claude lấy đề xuất của mình và làm sai. Sửa: sản phẩm từ tài nguyên thì không hỏi; đề xuất đứng đầu là mặc định của skill; câu không được trả lời hoặc David nói "làm đi" thì theo mặc định; chỉ tín hiệu nặng mới dừng. Thay luật cũ "làm đi ≠ chốt lựa chọn".
## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng `du-an/nang-cap/tai-cau-truc-2-hoi.md` (24 dòng; không bỏ luật nào). Bỏ dấu "(chốt 05/11/2026)" và ví dụ có ngày ở tín hiệu 1 (sự việc ngày 05/11: Claude tự đoán câu "không biết thông tin nào khi mà đăng lên" rồi render là sai; giữ ở ghi nhớ `quy-tac-tu-hoi-khi-mo-ho`). Gộp hai câu "tự tra / không hỏi điều tra được" làm một; "tối đa 5 câu" chỉ nói một lần; thêm lại "Claude tự xếp loại việc" (luật của bản đầu bị mất ở lần chuẩn hoá); ghi rõ chữ lệch chỉ hỏi lại khi hiểu được nhiều cách; ngoại lệ tự chọn và phần cố định không hỏi trỏ về thoi-quen mục 2; "nội dung của David" trỏ AGENTS luật 4.
- 2026-11-05 · Claude học grill-me / grilling (mattpocock/skills): hỏi theo vòng theo cây quyết định, đề xuất có thể "đồng ý" được, sự thật thì tự tra, nhiều vòng cho việc lớn.
- 2026-11-05 · Claude tự nhận diện lúc cần hỏi (6 tín hiệu), hỏi cả giữa chừng — David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".
- 2026-11-08 · chuẩn hoá (`du-an/chuan-hoa-ky-nang.md` bước 3): mỗi câu 2–3 gợi ý với đề xuất đứng đầu; khách gồm hai nhóm: người lần đầu dẫn người, và người xem; bỏ "kinh doanh"; sản phẩm thì một vòng gộp, thiết kế lớn thì nhiều vòng; "làm đi" không phải là chốt lựa chọn; trỏ `chuan-muc-lam-viec.md`; rút gọn mô tả, bỏ mục lặp; thêm "Xong khi".
