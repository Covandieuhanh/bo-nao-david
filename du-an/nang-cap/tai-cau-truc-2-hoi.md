---
description: "Tái bản 2 (10/11), phần bộ hỏi skill thu-thap-yeu-cau."
---

# Tái bản 2 — bộ hoi (`ky-nang/thu-thap-yeu-cau/SKILL.md`)

Máy đo lúc mở: dau_ngay 1/8 · ghi_de 0/4 · trung 0/3 · sua 3/15 · dong 82/300 (chưa tái bản lần nào).
Nguồn đã đọc: SKILL.md hiện tại + 3 bản git (`7abb767`, `8013537`, `785283a`), ghi nhớ `quy-tac-tu-hoi-khi-mo-ho`,
`quy-tac-goi-y-de-david-chon`, `quy-tac-noi-dung-cua-david`, `quy-tac-khong-tu-chay-viec-cua-david`; `chuan-muc-lam-viec.md`,
`AGENTS.md`, `co-so-tri-thuc/david.md`, `co-so-tri-thuc/chi-dan-toan-cuc.md` (= `~/.claude/CLAUDE.md`), các chỗ trỏ trong `ky-nang/san-xuat-video/`.

## Bảng luật đang sống

Cột: luật · nhà nên ở · nguồn hiện tại · ngày chốt gần nhất · trạng thái. "hoi:n" = dòng n của SKILL.md trước tái bản.

| # | Luật | Nhà | Nguồn hiện tại | Ngày | Trạng thái |
|---|---|---|---|---|---|
| 1 | Áp cho mọi yêu cầu tạo/sửa sản phẩm (file, skill, tài liệu, video, kịch bản, bài đăng, kế hoạch, code) | hoi | hoi:3,14 · AGENTS:22 · david.md:31 · chi-dan-toan-cuc:4 | 08/11 | sống (nơi khác là dòng trỏ) |
| 2 | Không áp: câu hỏi nhanh, tra cứu, giải thích, việc 1–2 bước → trả lời thẳng | hoi | hoi:3,15 · AGENTS:22 · david.md:31 · chi-dan-toan-cuc:4 | 08/11 | sống (trỏ) |
| 3 | David nói đủ / "làm đi": bỏ câu đã có lời đáp, vẫn diễn giải, chờ "ok"; "làm đi" không chốt lựa chọn bên trong | hoi | hoi:16 · thoi-quen:29 · ghi nhớ luat-goi-y | 08/11 | trùng (thoi-quen chép) → Chéo bộ 1 |
| 4 | Ngoại lệ được tự chọn: cắt highlight, làm lại video cũ — vẫn báo rõ đã chọn gì | thoi-quen mục 2 (hoặc video `quy-tac-chung`) | hoi:17 (trỏ) · thoi-quen:31 · ghi nhớ luat-goi-y | 07/11 | sống, hoi chỉ trỏ |
| 5 | Không có David để trả lời (việc tự động): giả định hợp lý nhất, ghi giả định đầu báo cáo | hoi | hoi:18 | 08/11 | sống |
| 6 | Sáu tín hiệu tự dừng hỏi, lúc đầu và giữa chừng, không đợi David yêu cầu | hoi | hoi:20–28 · ghi nhớ luat-tu-hoi · thoi-quen:30 (trỏ) · dung-video-theo-phong-cach:17, dung-podcast:19 (trỏ) | 05/11 | sống; bỏ dấu ngày + ví dụ có ngày ở tín hiệu 1 (chuyện về sổ, ghi nhớ đã giữ) |
| 7 | Giữa chừng: dừng đúng bước bị ảnh hưởng, một vòng ngắn; phần không bị ảnh hưởng làm tiếp | hoi | hoi:30 · thoi-quen:30 | 05/11 | trùng → Chéo bộ 1 |
| 8 | Không hỏi thừa: chuyện nhỏ có mặc định rõ, không đổi thứ người xem thấy/nghe, đảo ngược dễ → tự làm, ghi "đã chọn X vì Y" | hoi | hoi:31 · ghi nhớ luat-goi-y ("việc kỹ thuật…") | 08/11 | sống |
| 9 | Phần quy trình mặc định đã định thì không hỏi, không đề xuất bỏ/giảm | thoi-quen mục 2 | thoi-quen:32–34 | 10/11 | sống; hoi thêm một dòng trỏ (chưa có) |
| 10 | Độ sâu: sản phẩm một vòng gộp tối đa 5 câu rồi chạy một mạch · thiết kế lớn nhiều vòng · "grill me"/"hỏi kỹ" nhiều vòng kể cả việc nhỏ; Claude tự chọn độ sâu | hoi | hoi:33–39 · quy-tac-chung video:103 (trỏ) | 08/11 | sống; gộp luật cũ "video diễn giải một lần đầu rồi chạy trọn" và "tự chọn độ sâu" (bản 7abb767) |
| 11 | Số câu: tối đa 5 câu/vòng | hoi | hoi:38,49 · chi-dan-toan-cuc:4 ghi "3–5 câu" | 08/11 | lệch → Chéo bộ 2 |
| 12 | Cây quyết định: mỗi vòng chỉ hỏi câu đủ điều kiện; câu phụ thuộc để vòng sau; xong khi mọi nhánh đã đi qua | hoi | hoi:41 | 05/11 | sống |
| 13 | Sự thật Claude tự tra (file, bộ nhớ, skill, web, công cụ) song song; quyết định hỏi David; không hỏi điều đã có/tra được | hoi | hoi:43,49 · thoi-quen:23,28 · david.md:37 | 08/11 | trùng trong chính hoi (43 & 49) → gộp; thoi-quen chép → Chéo bộ 1 |
| 14 | Vòng 1 mở bằng một dòng `Góc nhìn tổng hợp từ:` — chuyên gia có thật, thực chiến đúng lĩnh vực, tối đa 10 tên, không chắc thì ít hơn, không bịa; vòng sau không lặp | hoi | hoi:48 · chi-dan-toan-cuc:4 | 05/11 | sống |
| 15 | Mỗi câu: đánh số, tiêu đề ngắn, một ý; 2–3 gợi ý, đề xuất đứng đầu; "đồng ý" = nhận đề xuất; ưu tiên điều đổi kết quả; câu nhiều phương án có thể dùng AskUserQuestion | hoi | hoi:49 · thoi-quen:27 · ghi nhớ luat-goi-y | 08/11 | trùng → Chéo bộ 1 |
| 16 | David trả lời bằng giọng nói: hiểu theo ý, chấp nhận chữ lệch (chỉ hỏi lại khi hiểu được nhiều cách — tín hiệu 1) | hoi | hoi:50 | 05/11 | sống; viết rõ quan hệ với tín hiệu 1 (không thêm luật) |
| 17 | Diễn giải lại 3–6 dòng: làm gì, cho ai, ra gì, ở đâu, theo luật nào, gì **không** làm; kèm Mục tiêu + 2–4 dòng Xong khi | hoi (Mục tiêu/Xong khi: thoi-quen mục 5) | hoi:51 | 08/11 | sống |
| 18 | Chờ "ok" ("ok", "đồng ý", "đúng", "làm đi"); chưa có thì không tạo/sửa file; David sửa ý → diễn giải lại phần đổi, chờ lần nữa | hoi | hoi:52 · AGENTS:22 · david.md:31 · chi-dan-toan-cuc:4 | 08/11 | sống (nơi khác trỏ) |
| 19 | Làm xong báo cáo theo thoi-quen mục 4 | thoi-quen mục 4 | hoi:53 (trỏ) | 08/11 | sống, trỏ |
| 20 | Nội dung là của David: không đề xuất khuôn lời cho David nói | AGENTS luật 4 | hoi:55 · AGENTS:24 · ghi nhớ quy-tac-noi-dung-cua-david | 05/11 | trùng → hoi giữ một dòng trỏ |
| 21 | Mục tiêu skill: ra đúng ý lần đầu cho người lần đầu dẫn người (khách David) và người xem video | hoi | hoi:10 | 08/11 | sống (thay "khách thuê làm nội dung" bản 7abb767) |
| 22 | Mẫu một vòng (khuôn trình bày câu hỏi) | hoi | hoi:57–70 | 08/11 | sống |
| 23 | Tiếng Việt, ngắn gọn; không hỏi lại điều đã biết | AGENTS luật 1 · david.md 3.7 | bản 7abb767 "Luật đã chốt" | 05/11 | đã có nhà ở nao; hoi không chép |
| 24 | Xong khi 7 dòng | hoi | hoi:72–80 | 08/11 | giữ nguyên ý |

Tổng: 24 dòng thành 19 luật có nhà trong hoi, 5 luật chỉ trỏ (4, 9, 19, 20, 23). Gộp: 10 (gộp 2 luật cũ), 13 (hai câu trong hoi). Bỏ: không bỏ luật nào; chỉ bỏ dấu ngày "(chốt 05/11/2026)" và ví dụ có ngày ở tín hiệu 1 (đã có ở Nhật ký + ghi nhớ).

## Chéo bộ

1. **`ky-nang/chuan-muc-lam-viec.md` mục 2 (dòng 26–31) chép lại gần hết cách hỏi** của hoi: hỏi một lần đầu, gộp, đề xuất đứng đầu, không
   hỏi điều đã có, "ok" thì chạy một mạch, "làm đi" ≠ chốt lựa chọn, giữa chừng 6 tín hiệu. Thêm dòng 23 "sự thật tra được thì tự tra".
   **Đề xuất nhà duy nhất:** `thu-thap-yeu-cau` cho *cách hỏi và khi nào hỏi*. thoi-quen mục 2 rút còn: một dòng trỏ hoi + luật 4 (ngoại lệ
   tự chọn) + luật 9 (phần cứng không hỏi) — hai luật này nói *cái gì không hỏi*, dùng chung, để ở thoi-quen. Mục 1 dòng 23 thì trỏ hoi.
2. **`co-so-tri-thuc/chi-dan-toan-cuc.md:4` (= `~/.claude/CLAUDE.md`) ghi "hỏi 3–5 câu"**, lệch với hoi "tối đa 5 câu/vòng, bỏ câu đã có lời đáp"
   (việc đã đủ có thể 0–2 câu). Đề xuất viết thành dòng trỏ không số: "làm theo skill `thu-thap-yeu-cau`: hỏi trước, diễn giải, chờ David
   'ok'". Kèm: `bo.json` bộ nao chưa đo file này (chỉ có `CLAUDE.md` của repo) nên đề xuất thêm `co-so-tri-thuc/chi-dan-toan-cuc.md` vào `ban_luat` nao.
3. **Ghi nhớ `quy-tac-goi-y-de-david-chon`** ghi "Nhà chính: `chuan-muc-lam-viec.md` mục 2" cho "làm đi ≠ chốt lựa chọn". Nếu chốt Chéo bộ 1
   → đổi thành "Nhà chính: `thu-thap-yeu-cau` mục Khi nào áp dụng; ngoại lệ tự chọn ở thoi-quen mục 2". (Phiên ghi-nho.)
4. **Ghi nhớ `quy-tac-tu-hoi-khi-mo-ho`** trỏ `thu-thap-yeu-cau` mục "Sáu tín hiệu" — bản mới giữ đúng tên mục này, không cần sửa.
5. `AGENTS.md:22` và `co-so-tri-thuc/david.md:31` cùng nhắc "hỏi trước, chờ ok" — cả hai là dòng trỏ về hoi, đúng; trùng giữa AGENTS và david.md
   là việc của bộ nao.
6. Các skill video (`quy-tac-chung.md:103`, `dung-video-theo-phong-cach:16–17`, `dung-podcast:17–19`, `phan-phoi-da-kenh:21`, `phan-tich-video-mau:15`,
   `nhan-dien-thuong-hieu.md:14`, khối 00, khối 14) trỏ hoi đúng nghĩa ("một lần đầu", "6 tín hiệu", "2–3 gợi ý đề xuất đứng đầu"). Phần
   "2–3 gợi ý đề xuất đứng đầu" bị chép lại ở vài nơi — chấp nhận được vì là câu ngắn mô tả cổng; nếu muốn sạch hẳn thì chỉ ghi "(`thu-thap-yeu-cau`)".

## Hỏi David

Không có chỗ ngược cần David chốt. Mọi lệch đều tự xử được theo `chuan-muc-lam-viec.md` mục 0 hoặc là chuyện chọn nhà (phiên điều phối chốt):
- "3–5 câu" (CLAUDE toàn cục) vs "tối đa 5" (hoi): theo nhà chính hoi, đề xuất ở Chéo bộ 2.
- "Không có David thì tự giả định" (luật 5) không ngược "David chọn, không tự chốt" (luật 3): luật 5 chỉ cho việc tự động không ai trả lời.

## Kết quả
- SKILL.md viết lại: xem `ky-nang/thu-thap-yeu-cau/SKILL.md`; Nhật ký có dòng đầu `## Tái bản 2 — 10/11/2026`.
- Máy đo sau: dau_ngay 0/8 · ghi_de 0/4 · trung 0/3 · sua 3/15 (về 0 khi có tag `tai-ban-2`) · dong 84/300 (bản luật 74 dòng trước Nhật ký).
- Kiểm đủ luật: 19 luật có nhà trong hoi đều tìm thấy trong bản mới; 5 luật trỏ đều có dòng trỏ. Tên mục "Sáu tín hiệu" giữ nguyên (ghi nhớ trỏ vào).
- Chưa làm: không commit, không sync, không tag (phiên điều phối làm).
