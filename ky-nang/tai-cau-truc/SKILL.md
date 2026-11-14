---
name: tai-cau-truc
description: Tái bản bộ skill — khi luật đã chồng nhiều lớp (học mẫu lớp 1, lớp 2, lớp 3, sửa góp ý…), gom toàn bộ luật đang sống của CẢ BỘ NÃO (mọi bộ skill + ghi nhớ, một đợt) rồi VIẾT LẠI thành một bản sạch: mỗi luật một nhà, không ngày, không "thay luật cũ", không câu tự mâu thuẫn; lịch sử chuyển về sổ quyết định. Có máy đo chồng chéo (do-chong-cheo.py) để biết khi nào nên tái bản. Dùng khi David nói "tái bản", "viết lại skill", "viết lại toàn bộ luật", "gom luật", "luật bị chồng chéo", "/tai-cau-truc", hoặc khi máy đo báo "NÊN TÁI BẢN" và David đồng ý.
---

# Tái bản bộ skill

**Đọc trước:** `../chuan-muc-lam-viec.md` (mục 4 có luật "sửa thẳng, không chồng câu" — tái bản là bước dọn định kỳ của luật đó).

**Mục tiêu:** dù đã học, sửa bao nhiêu lớp, lúc làm việc AI chỉ đọc **một bản luật hiện hành**, đọc một lần là làm đúng, không phải tự
đoán câu nào còn hiệu lực. Kết quả làm ra phải **bằng hoặc tốt hơn** trước khi tái bản.

## Ba loại file (định nghĩa từng bộ ở `bo.json`)
| Loại | Chứa | Lúc làm việc |
|---|---|---|
| **Bản luật** | chỉ luật đang dùng, viết như mới: không ngày, không "thay luật cũ / bổ sung 09/11", không lời kể lịch sử | đọc |
| **Sổ quyết định** | ngày · lời David nguyên văn · lý do · luật nào bị thay | không đọc (chỉ khi cân nhắc đổi luật, gỡ lỗi) |
| **Kho** | thực đơn để chọn (bố cục, nguồn học, hình mẫu) — không phải luật | chỉ khi cần chọn |

Bộ: `video` (ky-nang/san-xuat-video) · `hoi` (thu-thap-yeu-cau) · `nao` (AGENTS, CLAUDE, chi-dan-toan-cuc, david.md, chuan-muc-lam-viec). Ghi nhớ `co-so-tri-thuc/bo-nho/`
là sổ, không đo ở đây, nhưng **dọn cùng đợt** bằng skill `consolidate-memory`.

## Tái bản là tái bản toàn bộ
Mỗi lần tái bản là **một đợt cho cả bộ não**: cả ba bộ + dọn ghi nhớ, cùng một mốc `tai-ban-<n>`. Vì học tài nguyên mới thường kéo
theo bỏ hoặc đổi luật ở nhiều bộ cùng lúc; tái bản lẻ một bộ thì luật ở bộ khác vẫn giữ lớp cũ.

## Khi nào tái bản
- Máy đo: **một bộ bất kỳ vượt ngưỡng** → báo "NÊN TÁI BẢN TOÀN BỘ" một dòng → Claude nhắc David **một dòng**, David quyết.
  Chạy máy đo cuối mỗi việc có sửa bản luật (thoi-quen mục 4):
  ```bash
  python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py [--chi-tiet]
  ```
- Hoặc David gọi "tái bản".

## Quy trình (mỗi đợt)
1. **Mốc** *(bước nhẹ)*: `bash tu-dong-hoa/dong-bo.sh --push`, rồi `git tag tai-ban-<n>-truoc`. Chạy máy đo, lưu kết quả vào
   `du-an/tai-ban-<n>.md` (file theo dõi chung của đợt). Mỗi phiên con ghi file riêng `du-an/tai-ban-<n>-<bộ>.md`
   (video · hoi · nao · ghi-nho) để không ghi đè nhau.
2. **Chia phiên:** phiên điều phối mở một phiên con cho mỗi bộ (video · hoi · nao) và một phiên dọn ghi nhớ, chạy cùng lúc.
   Mỗi phiên chỉ sửa file của bộ mình, không commit, không chạy `dong-bo.sh` — phiên điều phối đẩy một lần khi đóng mốc.
   Bộ vừa sạch (máy đo gần 0) vẫn làm bước 3 để tìm luật lệch với bộ khác, viết lại chỗ lệch.
3. **Bảng luật đang sống** (file của bộ): đọc toàn bộ bản luật + sổ quyết định + ghi nhớ liên quan, mỗi luật một dòng:
   `luật · nhà nên ở · nguồn hiện tại (file:dòng, có thể nhiều) · ngày chốt gần nhất · trạng thái (sống / trùng / ngược / cũ)`.
   Luật ngược nhau: theo `chuan-muc-lam-viec.md` mục 0 (lời David vừa nói > ngày chốt gần nhất > cũ); chỗ vẫn không rõ → gom lại
   **hỏi David một lần** (thu-thap-yeu-cau), có đề xuất. Không tự bỏ luật nào David đã chốt mà không có luật mới hơn thay.
   Luật đụng bộ khác → ghi vào mục "Chéo bộ" của file bộ mình; phiên điều phối gom, chốt nhà duy nhất.
4. **Viết lại từ bảng, không vá:** mỗi file bản luật viết lại thành trạng thái hiện hành.
   - Mỗi luật **một nhà**; nơi khác một dòng trỏ. Luật dùng chung nhiều skill → `chuan-muc-lam-viec.md` / `quy-tac-chung.md`, không chép.
   - Không ngày, không "(David chốt …)", không "thay luật cũ", không "chuyển nguyên văn từ SKILL.md cũ". Lý do một luật tồn tại
     viết ngắn **trong luật** nếu giúp AI làm đúng ("vì người xem không đọc hai chỗ cùng lúc"); lịch sử thì vào sổ.
   - Giữ đúng nghĩa từng luật trong bảng; viết gọn hơn, không thêm luật mới. Code đi kèm (tên khoá, lệnh) giữ khớp.
   - Bảng "Xong khi" của mỗi skill giữ nguyên ý.
   - Ghi nhớ: gộp trùng, bỏ cái đã lỗi thời, cập nhật `MEMORY.md`; ghi nhớ không chứa luật mà bản luật không có.
5. **Đóng sổ cũ:** mỗi sổ quyết định thêm một dòng đầu `## Tái bản <n> — <ngày>: bản luật viết lại từ bảng du-an/tai-ban-<n>.md`.
   Sổ quá dài (> 400 dòng) → chuyển phần cũ vào `luu-tru/` cạnh sổ.
6. **Kiểm chung** (bắt buộc, đủ cả 4, khi mọi phiên con xong):
   - **Đủ luật:** đi từng dòng bảng mọi bộ — luật "sống" nào cũng có nhà trong bản mới. Thiếu = chưa xong.
   - **Máy đo:** chạy lại; mọi bộ "Chưa cần"; dấu ngày và câu ghi đè gần 0, câu trùng 0.
   - **Hình y nguyên** (bộ video): `python3 -I ky-nang/san-xuat-video/mau-chuan/kiem-mau.py` + soát cảnh một dự án cũ. Tái bản chỉ viết lại
     chữ, không đổi code; ảnh khác = có gì sai.
   - **Việc thật:** chạy một việc đi qua nhiều bộ (ví dụ một đoạn ngắn trọn một ý từ phiếu lọc tới bản dựng, `quy-tac-thu-bang-doan-ngan`),
     David chấm. Phải bằng hoặc tốt hơn.
7. **Đóng mốc:** `git tag tai-ban-<n>`, thêm một dòng vào `lich-su.md`, chỉnh ngưỡng trong `bo.json` nếu thấy lệch (ví dụ ngưỡng
   quá thấp làm nhắc liên tục), đẩy GitHub, báo David: đã gom bao nhiêu luật, bỏ / gộp gì, đã kiểm gì, chưa kiểm gì.

## Không làm
- Không đổi luật, không thêm luật mới trong lúc tái bản — chỉ viết lại. Thấy luật nên đổi → ghi vào file theo dõi, hỏi David sau.
- Không đụng kho (bố cục, nguồn học) ngoài việc sửa đường trỏ.
- Không tái bản lẻ một bộ; không đóng mốc khi còn bộ chưa xong.

## Xong khi
1. Bảng luật đang sống của mọi bộ có đủ, mỗi dòng có nhà trong bản mới; ghi nhớ đã dọn.
2. Máy đo mọi bộ: "Chưa cần tái bản"; dấu ngày, câu ghi đè gần 0; câu trùng 0.
3. Mẫu chuẩn y nguyên và một việc thật David chấm đạt.
4. Có tag `tai-ban-<n>`, dòng trong `lich-su.md`, đã đẩy GitHub.

## Nhật ký
- 10/11/2026 · tạo skill. David: "mỗi lần học hay bổ sung hay sửa thì không bị chồng chéo… cứ một thời gian… viết lại toàn bộ… học được lớp 1, lớp 2, lớp 3 thì lại phải tổng kết lại toàn bộ để viết lại thành một skill hoàn chỉnh bao gồm cả 3 lớp". Chốt 5 điểm: sửa thẳng mỗi lần + lý do vào sổ · máy đo nhắc, David quyết · từng bộ một · kiểm mẫu chuẩn + việc thật · skill riêng.
- 10/11/2026 · đổi sang tái bản toàn bộ. David: "khi tái bản thì cứ tái bản hết toàn bộ mọi thứ để tối ưu nhất". Chốt: cả ba bộ + dọn ghi nhớ · một bộ vượt ngưỡng là tái bản cả đợt · một mốc chung `tai-ban-<n>`, mỗi bộ một phiên con chạy cùng lúc · đợt 2 chạy ngay. Thay luật "từng bộ một".
