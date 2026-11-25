---
description: "Tái bản 3 (14/11), phiên con bộ nao: bảng luật hiện hành, chéo bộ, hỏi David."
---

# Tái bản 3 — bộ nao

Phiên điều phối: [tai-ban-3.md](tai-ban-3.md). Đợt trước: [tai-cau-truc-2-nao.md](tai-cau-truc-2-nao.md) (55 luật, giữ nguyên nghĩa; bảng này chỉ ghi luật thêm/đổi từ đó và luật công cụ đo bắt).

Nhà: **A** = `AGENTS.md` · **C** = `CLAUDE.md` · **G** = `co-so-tri-thuc/chi-dan-toan-cuc.md` (= `~/.claude/CLAUDE.md`, nạp mọi phiên kể cả ngoài repo) · **T** = `ky-nang/chuan-muc-lam-viec.md` · **D** = `co-so-tri-thuc/david.md` (để nguyên, không sửa).

Công cụ đo lúc mở: `dau_ngay 5/15 · ghi_de 2/6 · trung 0/4 · sua 30/25 · dong 242/600`.
Công cụ đo sau viết lại: `dau_ngay 3/15 · ghi_de 0/6 · trung 0/4 · sua 30/25 · dong 244/600`. 3 dấu ngày còn lại đều ở D (D không sửa): 2 là dữ kiện (ngày cập nhật, "từ 13/11/2026 ba hướng"), 1 là dấu ngày luật ở D 3.1 nên Hỏi David 1. `sua 30` là số commit git, chỉ hạ khi có tag `tai-ban-3`.

## Bảng luật hiện hành
| # | Luật | Nguồn nên ở | Nguồn hiện tại | Ngày chốt gần nhất | Trạng thái |
|---|---|---|---|---|---|
| 1 | Thứ tự đọc 7 bước; tra CCL khi làm nội dung lãnh đạo | A | A:5–19 | 08/11 | sống |
| 2 | Tìm trong bộ não: grep chỉ mục → bản đồ → toàn repo; luật mạng lưới ở `quy-uoc-lien-ket.md` | A | A:17 | 14/11 | sống, giữ nguyên |
| 3 | Trả lời tiếng Việt, ý chính, ngắn, từ bản chất gốc | A luật 1 | A:23, G:3, D:3 | 12/11 | sống; G, D nhắc lại có chủ đích (nạp mọi phiên) |
| 4 | Việc gì cũng duyệt 4 phần, duyệt rồi tự làm trọn; miễn câu hỏi nhanh, tra cứu, bot ghi sổ, lịch đã duyệt | A luật 2 (tóm tắt) · T mục 2 (cách làm) | A:24, G:4, T:28–35, D:3.1 | 14/11 | sống; T bỏ "(David 14/11/2026, việc #22.)"; D 3.1 còn ngày → Hỏi David 1 |
| 5 | Thông tin trực tiếp về David (hồ sơ, màu, chữ ký nhận diện, mạng xã hội) đi qua 4 phần; sau duyệt sửa thứ này vẫn diễn giải + chờ "ok" | A luật 2 · T mục 2 | A:24, T:42–44 | 14/11 | sống |
| 6 | Skill, giọng văn, luật kênh tự học theo hình mẫu có số liệu, phần sửa trình 4 phần | A luật 2 | A:24, T:44 | 14/11 | trùng → T trỏ A luật 2 |
| 7 | Video đúng nguyên văn lời David | A luật 3 | A:25 | 12/11 | sống |
| 8 | Mạng xã hội, quyền riêng tư không tự động; không chạm mật khẩu, OTP, token, cookie, giấy tờ | A luật 4 | A:26, T:42, T:59 | 12/11 | sống; T:59 trỏ sai "luật 5" → sửa thành luật 4 |
| 9 | Lời mới nhất thắng; sửa luật thì viết lại chính câu đó mọi nơi | A luật 5 | A:27, G:4 | 12/11 | sống; bỏ chữ "thay mọi luật cũ" / "thắng luật cũ" (câu ghi đè), giữ nghĩa |
| 10 | GitHub là bản sao lưu đầy đủ, đẩy ngay, "cập nhật não", danh sách không đưa lên | A luật 6 | A:28–29, T:86 | 12/11 | sống, T trỏ |
| 11 | Khi nguồn mâu thuẫn: lời David mới nhất > bản luật > ghi nhớ; chất lượng thắng tiết kiệm; mơ hồ → sản phẩm duyệt mới nhất | T mục 0 | T:11–15, A:31 | 08/11 | sống |
| 12 | AI sáng tạo trong khung; luật nội dung không phải mẫu | T mục 0 | T:17–19 | 09/11 | sống |
| 13 | Bảng chọn skill; chỉ gửi tài nguyên → `phan-phoi-da-kenh` | A | A:33–52 | 14/11 | sống |
| 14 | Không phải Claude Code: ánh xạ đường dẫn, nói rõ phần không làm được, chỉ tin repo + lời David | A | A:54–59 | — | sống |
| 15 | Tên file từ thuật ngữ kinh doanh tiếng Anh chuẩn, dịch sang không dấu; ghi nhớ một máy `thiet-bi-` | A | A:64 | 14/11 | sống |
| 16 | C nạp `@AGENTS.md`; thiếu `~/.claude/david.md` → đề nghị `cai-dat-bo-nao.sh` | C | C:1–3 | — | sống |
| 17 | G: 3 luật nền + đọc T trước mọi skill + `@david.md` | G | G:1–7 | 14/11 | sống, giữ ngắn |
| 18 | Đầu việc đọc đúng phần cần | T mục 1 | T:21–26 | 08/11 | sống |
| 19 | Cách chọn từng điểm trong 4 phần (skill định → làm đúng; chưa định → tự chọn "chọn X vì Y"; "làm đi" = mặc định); sau duyệt chỉ dừng ở các trường hợp nêu | T mục 2 | T:36–45 | 11/11, 14/11 | sống |
| 20 | Việc tự chạy (lịch, việc Telegram) mở thành phiên hiện trong app (Remote Control), không chạy ngầm | T mục 2 (một dòng trỏ) | ghi nhớ `quy-tac-duyet-ke-hoach-4-phan` (ghi "luật ở T mục 2" nhưng T chưa có), `tu-dong-hoa/lich/lich-chay.md`, `tu-dong-hoa/so-tay/README.md` | 14/11 | sống, **thiếu nguồn ở T** → thêm một dòng trỏ |
| 21 | Lệnh theo lô, nền > 2 phút; agent phụ khi được phép, `nghien-cuu` cho việc đọc; bước nhẹ nhắc | T mục 3 | T:48–51 | 08/11 | sống |
| 22 | Việc của David là của David; việc thử tên `thu-…` | T mục 3 | T:52–55 | 08/11 | sống |
| 23 | Công cụ David đã cài → đề xuất tích hợp, giữ cách cũ dự phòng | T mục 3 | T:56–57 | 07/11 | sống |
| 24 | Không dùng mod giao diện, chỉ giữ Telegram, mod mới hỏi trước | T mục 3 | T:58, ghi nhớ `quy-tac-mod-tu-chay` | 13/11 | sống; bỏ "David gỡ hết 13/11/2026", thêm phần "chỉ giữ Telegram / hỏi trước" từ ghi nhớ |
| 25 | Tự soát trước khi báo xong; báo cáo ngắn | T mục 4 | T:62–65 | 08/11 | sống |
| 26 | Báo Telegram khi xong trọn việc hoặc vướng | T mục 4 | T:66–68 | 11/11 | sống |
| 27 | Nhắc lần hai thành luật ngay | T mục 4 | T:69–70 | — | sống |
| 28 | Góp ý ghi đúng một chỗ; ghi nhớ chỉ luật dùng chung | T mục 4 | T:71–72 | — | sống |
| 29 | Sửa thẳng, không chồng câu; ba loại file ở `tai-cau-truc` | T mục 4 | T:73–76 | 10/11 | sống |
| 30 | Đo chồng chéo sau mỗi lần sửa bản luật | T mục 4 | T:77–78, T bảng mục 5 | 10/11 | sống |
| 31 | Giữ mạng lưới liên kết; kiến thức đáng giữ vào `kien-thuc/` | T mục 4 | T:80–83 | 14/11 | sống, giữ nguyên |
| 32 | Giữ dung lượng Mac thấp (Drive) | T mục 4 | T:84–85 | 11/11 | sống |
| 33 | Mục tiêu + Xong khi; nhắc một dòng; bảng "Khi → Claude làm" (có đóng phiên khi xong) | T mục 5 | T:88–109 | 14/11 | sống |
| 34 | Thói quen của David để nhắc | T mục 5 | T:111–113 | 08/11 | sống |
| 35 | Hồ sơ, luật cá nhân, mục 3.2–3.5, bảng mục 4–9 | D | D:1–56 | 14/11 | sống, không sửa |

35 dòng (gộp nhóm theo nguồn; chi tiết từng luật cũ ở bảng đợt 2). Không bỏ luật nào, không đổi nghĩa. 1 luật thiếu nguồn đã có nguồn duy nhất (dòng 20) · 1 trùng chuyển thành trỏ (dòng 6) · 1 đường trỏ sai đã sửa (dòng 8). Số mục T giữ 0–5 (skill khác trỏ "mục 0/2/3/4/5").

## Sổ (gỡ khỏi bản luật)
- T mục 2: "(David 14/11/2026, việc #22.)" thì lời David nguyên văn đã có ở ghi nhớ `quy-tac-duyet-ke-hoach-4-phan`.
- T mục 3: "David gỡ hết 13/11/2026" nay đã có ở ghi nhớ `quy-tac-mod-tu-chay`.
- A luật 5: "lời David nói sau cùng thay mọi luật cũ" nên viết "là luật hiện hành"; G: "Lời David mới nhất thắng luật cũ" thành "Lời David nói sau cùng là luật hiện hành". Cùng nghĩa, bỏ chữ ghi đè. Ngày chốt 12/11 ở ghi nhớ `quy-tac-ky-nang-tu-cai-tien`.

## Chéo bộ
1. **Ghi nhớ (phiên ghi-nho):** `quy-tac-duyet-ke-hoach-4-phan` ghi "Luật ở `chuan-muc-lam-viec.md` mục 2" — nay đúng (đã thêm dòng "Việc tự chạy phải nhìn thấy được"). Không cần sửa ghi nhớ.
2. **Ghi nhớ:** `quy-tac-goi-y-de-david-chon` thân còn câu "Sản phẩm…: **không hỏi**", rồi đoạn 14/11 thêm "vẫn trình 4 phần". Đọc thân dễ hiểu sai; đề nghị phiên ghi-nho viết thân thành trạng thái hiện hành (trình 4 phần gọn theo mặc định skill, duyệt rồi không hỏi giữa chừng). Tương tự `quy-tac-ky-nang-tu-cai-tien` (dòng "Chỉ hỏi trước: hồ sơ David…" đã bị đoạn 14/11 thay) và `quy-tac-phien-telegram-tu-chay`.
3. **tu-dong-hoa (không thuộc bộ nào):** nguồn chi tiết của luật dòng 20 là `tu-dong-hoa/lich/lich-chay.md` + `tu-dong-hoa/so-tay/README.md`; README so-tay còn nhiều dấu ngày, câu "14/11 đổi từ toàn quyền Bypass…" — ngoài công cụ đo, phiên điều phối cân nhắc đưa vào bộ nao hoặc để nguyên.

## Hỏi David
1. **`co-so-tri-thuc/david.md` mục 3.1** trùng `AGENTS.md` luật 2 và còn dấu ngày luật "(14/11/2026)" — là dấu ngày duy nhất còn lại của bộ nao không phải dữ kiện. Đề xuất viết lại (đề xuất đứng đầu):
   - **(a, đề xuất)** `1. **Việc gì cũng trình đủ 4 phần, David duyệt rồi mới làm:** Mục tiêu · Kế hoạch · Quy trình (từng bước) · Thực thi (checklist chia càng nhỏ càng tốt để có mốc làm ngay). Chưa duyệt thì chưa tạo/sửa file nào; duyệt rồi tự làm trọn tới khi chắc dùng được, không dừng giữa chừng.` (chỉ bỏ ngày; giữ vì david.md nạp ở mọi phiên ngoài repo).
   - (b) Thay bằng một dòng trỏ: `1. **4 phần trước mọi việc:** \`AGENTS.md\` luật 2, cách làm \`ky-nang/chuan-muc-lam-viec.md\` mục 2.` (gọn hơn nhưng phiên ngoài repo không đọc được AGENTS).
2. **david.md mục 3 dòng "Sáu luật nền (…)"** nhắc lại tóm tắt sáu luật của A — đúng nghĩa hiện tại, không lệch. Đề xuất để nguyên (nạp mọi phiên). Chỉ cần nhớ: đổi một luật ở A luật 1–6 thì sửa luôn dòng này và G dòng 3–4.
3. Dữ kiện có ngày ở D ("Cập nhật lần cuối: 14/11/2026", "Từ 13/11/2026 làm ba hướng") là dữ kiện, giữ.

## Đã viết lại
- `ky-nang/chuan-muc-lam-viec.md`: mục 2 bỏ ngày, thêm dòng "Việc tự chạy phải nhìn thấy được" (trỏ tu-dong-hoa), dòng tự học thành trỏ A luật 2; mục 3 mod giao diện viết trạng thái hiện hành, sửa trỏ "luật 5" thành "luật 4".
- `AGENTS.md`: luật 5 bỏ chữ ghi đè, giữ nghĩa. Đoạn "Tìm thứ gì trong bộ não" giữ nguyên.
- `co-so-tri-thuc/chi-dan-toan-cuc.md`: dòng 4 bỏ chữ ghi đè; giữ `@david.md`.
- `CLAUDE.md`: sạch, không đổi (giữ `@AGENTS.md`).
- `co-so-tri-thuc/david.md`: không sửa (David chốt).
- **Đợt 2 (việc chéo bộ phiên điều phối giao):**
  - T mục 0: thêm luật "Nội dung là của David" (nguồn mới, nghĩa từ ghi nhớ `quy-tac-noi-dung-cua-david`; chi tiết video vẫn ở `quy-tac-chung.md` mục 0–1). `hermes/giao-cho-hermes.md` để nguyên.
  - T mục 2: "diễn giải + chờ ok" thành "trình lại, chờ duyệt"; câu tự học skill chuyển về T (gạch "Tự học"); "Mọi việc" thêm thông tin trực tiếp về David (trước nằm ở A luật 2).
  - T mục 4: thêm luật `david.md` chỉ ghi điều cố định đã chốt, ý tưởng đang cân nhắc vào `du-an/danh-sach-y-tuong.md` (từ ghi nhớ `quy-tac-david-md-chi-dieu-co-dinh`, nay có nguồn duy nhất: ghi nhớ đó sửa dòng "Nguồn của luật" trỏ T mục 4).
  - A luật 2: rút còn một câu tóm + trỏ T mục 2 (phần miễn, tự học, thông tin về David chỉ ở T).
  - **G (`chi-dan-toan-cuc.md`) chưa sửa đợt này:** file là `~/.claude/CLAUDE.md` nạp mọi phiên, phiên con không tự sửa cấu hình toàn cục theo lời phiên khác. Đề xuất để phiên điều phối / David áp: thay dòng 4 bằng `- Việc gì cũng trình đủ 4 phần (Mục tiêu · Kế hoạch · Quy trình · Thực thi), chờ David "duyệt" rồi mới làm; duyệt rồi tự làm trọn tới khi chắc dùng được. Lời David nói sau cùng là luật hiện hành. Cách làm, phần miễn: \`ky-nang/chuan-muc-lam-viec.md\` mục 2; sáu luật: \`AGENTS.md\`.` (bỏ danh sách miễn ở G, nên không cần bổ sung "bot ghi sổ").
- Đóng sổ: bộ nao không có file sổ riêng (sổ = git + ghi nhớ), nên dòng "Tái bản 3" ghi ở đây và ở mục Sổ trên; ghi nhớ do phiên ghi-nho xử lý.
