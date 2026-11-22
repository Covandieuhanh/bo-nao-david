---
name: thu-thap-yeu-cau
description: Cách hỏi của David khi trình 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi) trước mọi việc — hỏi theo vòng từ góc nhìn chuyên gia thực chiến, mỗi điểm cần chốt 2–3 gợi ý có đề xuất đứng đầu; sự thật tự tra, quyết định David chốt; chờ David "duyệt" rồi mới tạo/sửa file; duyệt rồi làm trọn một mạch. Tự nhận diện 6 tín hiệu phải dừng hỏi, cả lúc bắt đầu lẫn giữa chừng. Dùng khi trình 4 phần cho một việc, khi David nói "hỏi kỹ", "hỏi chuyên gia", "grill me", "/thu-thap-yeu-cau". Không dùng cho câu hỏi nhanh, tra cứu.
---

# Hỏi chuyên gia trước khi làm

Đọc trước: [chuan-muc-lam-viec.md](../chuan-muc-lam-viec.md). Luật **trình 4 phần trước mọi việc, chờ "duyệt", duyệt rồi làm trọn**, phần miễn và cách chọn từng điểm (mặc định skill, "làm đi") ở `chuan-muc-lam-viec.md` mục 2. File này là nhà của **cách hỏi** trong 4 phần: điểm nào cần chốt, hỏi thế nào, sâu tới đâu, khi nào phải dừng hỏi.

**Mục tiêu:** hỏi đúng câu trước khi làm để ra đúng ý ngay lần đầu, cho khách và người xem của David ở cả ba hướng nghề (`co-so-tri-thuc/david.md` 4.1).

Không dùng cho câu hỏi nhanh, tra cứu, giải thích (trả lời thẳng) và lịch tự chạy đã duyệt (làm theo lời giao, ghi giả định ở đầu báo cáo).

## Sáu tín hiệu phải tự dừng hỏi

Lúc trình 4 phần: mọi tín hiệu gom vào điểm cần chốt. Sau khi duyệt, giữa chừng chỉ các tín hiệu **nặng** (1 khi làm đổi hẳn kết quả, 2, 3 khi đăng / xoá / khó đảo ngược, 5) mới dừng; tín hiệu 4 và 6 thì tự chọn theo mặc định + đề xuất và ghi vào báo cáo:
1. **Hiểu được nhiều cách**: câu mơ hồ, nhất là chữ đọc chính tả lệch làm đổi nghĩa — không tự đoán rồi làm.
2. **Mâu thuẫn** với luật, bộ nhớ, skill hoặc quyết định David đã chốt.
3. **Tốn thời gian / tiền / khó đảo ngược**: render > 10 phút (chỉ nêu trong 4 phần, giữa chừng chạy nền không dừng), xoá, đăng, gửi tin, dịch vụ trả phí, sửa hàng loạt.
4. **Thiếu một quyết định làm đổi kết quả**: người xem, nền tảng, mục tiêu, phạm vi.
5. **Đang làm thì phát hiện vấn đề** làm đổi kế hoạch (thiếu file, nguồn kém, cách cũ không chạy).
6. **Sắp tự đặt một giả định** David chưa xác nhận.

Giữa chừng: dừng đúng bước bị ảnh hưởng, hỏi một vòng ngắn; phần không bị ảnh hưởng vẫn làm tiếp.
Không hỏi thừa: có mặc định rõ, hoặc sửa được ở bản cuối thì tự làm, ghi một dòng "đã chọn X vì Y".

## Độ sâu

Claude tự xếp loại việc, David không cần nói "grill me":

| Loại việc | Cách hỏi |
|---|---|
| **Sản phẩm từ tài nguyên** (video, highlight, podcast, bài đăng) | **4 phần gọn** (định làm thành gì, khung, số clip, kênh): điểm skill đã định ghi luôn, chỉ hỏi điểm skill chưa định; duyệt xong chạy một mạch tới kết quả |
| **Sửa một file / tài liệu / skill** | **4 phần + một vòng gộp** mọi điểm cần chọn; "duyệt" xong chạy một mạch |
| **Thiết kế lớn** (kế hoạch, chiến lược, skill hoặc quy trình mới) | **Nhiều vòng** tới khi hết điểm mờ |
| David nói **"grill me" / "hỏi kỹ"** | Nhiều vòng, kể cả việc nhỏ |

Mỗi vòng **tối đa 5 câu**. **Cây quyết định:** mỗi vòng chỉ hỏi câu đã đủ điều kiện (không phụ thuộc câu còn mở); câu phụ thuộc thì vòng sau. Xong khi mọi nhánh đã đi qua.

**Sự thật Claude tự tra** (file, bộ nhớ, skill, web, công cụ), chạy song song; **quyết định hỏi David**. Không hỏi điều đã có hoặc tra được.

## Quy trình

1. Xác định lĩnh vực và loại việc (bảng trên).
2. **Vòng 1 mở bằng một dòng:** `Góc nhìn tổng hợp từ: <tên>, <tên>, …` — chuyên gia **có thật**, thực chiến đúng lĩnh vực, tối đa 10 tên. Không chắc thì nêu ít hơn, không bịa. Vòng sau không lặp.
3. **Các câu hỏi**, mỗi câu: đánh số, tiêu đề ngắn, một ý; **2–3 gợi ý, đề xuất đứng đầu**, "đồng ý" = nhận đề xuất. Ưu tiên điều đổi kết quả. Câu nhiều phương án có thể dùng AskUserQuestion.
4. David trả lời (thường bằng giọng nói): hiểu theo ý, chấp nhận chữ lệch; chỉ hỏi lại khi hiểu được nhiều cách (tín hiệu 1). Thiết kế lớn thì vòng tiếp.
4b. **Thiết kế lớn (nhiều vòng): ghi ngay vào file** `du-an/phong-van/<ngày>-<chủ-đề>.md` sau mỗi câu trả lời: câu hỏi · đề xuất · **đã chốt**.
   Phiên dài hay bị ngắt vẫn không mất gì; cuối buổi thêm phần tóm tắt các quyết định và việc còn bỏ ngỏ.
5. **Trình 4 phần** khi hết điểm mờ: Mục tiêu (một dòng + 2–4 dòng **Xong khi**, `chuan-muc-lam-viec.md` mục 5) · Kế hoạch (diễn giải 3–6 dòng: làm gì, cho ai, ra gì, ở đâu, theo luật nào, cái gì **không** làm; "chọn X vì Y") · Quy trình · Thực thi.
6. **Chờ "duyệt"** ("duyệt", "ok", "đồng ý", "đúng", "làm đi" đều tính). Chưa có thì không tạo, không sửa file nào. David sửa phần nào thì trình lại phần đó, chờ lần nữa.
7. Làm xong: báo cáo theo `chuan-muc-lam-viec.md` mục 4.

Nội dung là của David (`chuan-muc-lam-viec.md` mục 0, ghi nhớ [quy-tac-noi-dung-cua-david](../../co-so-tri-thuc/bo-nho/quy-tac-noi-dung-cua-david.md)): không đề xuất khuôn lời cho David nói.

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

1. Vòng 1 mở bằng một dòng tên chuyên gia có thật; vòng sau không lặp.
2. Mỗi vòng tối đa 5 câu, câu nào cũng có 2–3 gợi ý, đề xuất đứng đầu.
3. Không câu nào hỏi điều đã có trong file, bộ nhớ, đã được skill định, hoặc tra được.
4. 4 phần có diễn giải 3–6 dòng, nói rõ cả điều **không** làm, kèm Mục tiêu và Xong khi.
5. Không file nào bị tạo/sửa trước khi David "duyệt" 4 phần. Sau duyệt: không hỏi gì ngoài tín hiệu nặng, báo cáo cuối có đủ "đã chọn X vì Y".
6. Giữa chừng gặp tín hiệu thì dừng đúng bước, không tự đoán.
7. Sau "duyệt" làm một mạch, không phải làm lại vì hiểu sai.
8. Thiết kế lớn: mọi câu đã chốt nằm trong file phỏng vấn, có phần tóm tắt cuối buổi.

## Nhật ký
## Tái bản 3 — 14/11/2026: bản luật viết lại từ bảng `du-an/nang-cap/tai-ban-3-hoi.md` (24 dòng; không bỏ luật nào). Luật "trình 4 phần trước mọi việc, chờ duyệt" (việc #22) và phần miễn, cách chọn từng điểm, "làm đi" = mặc định, hoc-lien-tuc: nhà duy nhất `chuan-muc-lam-viec.md` mục 2, skill còn một dòng trỏ. Bỏ hàng trùng "sản phẩm từ tài nguyên" (đã ở bảng Độ sâu). Diễn giải 3–6 dòng ghép vào bước trình 4 phần; "chờ ok" thành "chờ duyệt". Sửa tên cũ "thoi-quen" thành `chuan-muc-lam-viec.md`. "Nội dung của David" trỏ cm mục 0 + ghi nhớ (AGENTS luật 4 nay là mạng xã hội).
- 2026-11-14 · học từ bài "16 bài học sau 1000 giờ dùng Claude" (Nhật Anh AI, tip 5): skill grill-me bản Việt ghi từng câu trả lời vào file ngay thì thêm bước 4b và Xong khi 8.
- 2026-11-11 · David: "Hạn chế hỏi những thứ theo tiêu chí nhất có thể… mục tiêu cuối cùng của tôi luôn là đưa tài nguyên vào và chờ kết quả là xong." Nguyên nhân: video cuộc gọi hợp tác, Claude đưa khung hình vào câu hỏi dù skill đã định khung = gốc, đề xuất đầu (dọc) trái mặc định, David không trả lời câu đó thì Claude lấy đề xuất của mình, làm sai. Sửa: sản phẩm từ tài nguyên không hỏi; đề xuất đứng đầu = mặc định skill; câu không trả lời / "làm đi" = theo mặc định; chỉ tín hiệu nặng mới dừng. Thay luật cũ "làm đi ≠ chốt lựa chọn".
## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng `du-an/nang-cap/tai-cau-truc-2-hoi.md` (24 dòng; không bỏ luật nào). Bỏ dấu "(chốt 05/11/2026)" và ví dụ có ngày ở tín hiệu 1 (chuyện 05/11: Claude tự đoán câu "không biết thông tin nào khi mà đăng lên" rồi render là sai; giữ ở ghi nhớ `quy-tac-tu-hoi-khi-mo-ho`). Gộp hai câu "tự tra / không hỏi điều tra được" làm một; "tối đa 5 câu" nói một lần; thêm lại "Claude tự xếp loại việc" (luật bản đầu bị rơi ở lần chuẩn hoá); ghi rõ chữ lệch chỉ hỏi lại khi hiểu được nhiều cách; ngoại lệ tự chọn + phần cứng không hỏi trỏ về thoi-quen mục 2; "nội dung của David" trỏ AGENTS luật 4.
- 2026-11-05 · học grill-me / grilling (mattpocock/skills): hỏi theo vòng theo cây quyết định, đề xuất "đồng ý" được, sự thật tự tra, nhiều vòng cho việc lớn.
- 2026-11-05 · tự nhận diện lúc cần hỏi (6 tín hiệu), hỏi cả giữa chừng — David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".
- 2026-11-08 · chuẩn hoá (`du-an/chuan-hoa-ky-nang.md` bước 3): mỗi câu 2–3 gợi ý đề xuất đứng đầu; khách = người lần đầu dẫn người + người xem, bỏ "kinh doanh"; sản phẩm một vòng gộp, thiết kế lớn nhiều vòng; "làm đi" ≠ chốt lựa chọn; trỏ `chuan-muc-lam-viec.md`; rút mô tả, bỏ mục lặp; thêm "Xong khi".
