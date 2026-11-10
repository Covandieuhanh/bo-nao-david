---
name: tai-ban
description: Tái bản bộ skill — khi luật đã chồng nhiều lớp (học mẫu lớp 1, lớp 2, lớp 3, sửa góp ý…), gom toàn bộ luật đang sống của một bộ rồi VIẾT LẠI thành một bản sạch: mỗi luật một nhà, không ngày, không "thay luật cũ", không câu tự mâu thuẫn; lịch sử chuyển về sổ quyết định. Có máy đo chồng chéo (do_chong_cheo.py) để biết khi nào nên tái bản. Dùng khi David nói "tái bản", "viết lại skill", "viết lại toàn bộ luật", "gom luật", "luật bị chồng chéo", "/tai-ban", hoặc khi máy đo báo "NÊN TÁI BẢN" và David đồng ý.
---

# Tái bản bộ skill

**Đọc trước:** `../thoi-quen-lam-viec.md` (mục 4 có luật "sửa thẳng, không chồng câu" — tái bản là bước dọn định kỳ của luật đó).

**Mục tiêu:** dù đã học, sửa bao nhiêu lớp, lúc làm việc AI chỉ đọc **một bản luật hiện hành**, đọc một lần là làm đúng, không phải tự
đoán câu nào còn hiệu lực. Kết quả làm ra phải **bằng hoặc tốt hơn** trước khi tái bản.

## Ba loại file (định nghĩa từng bộ ở `bo.json`)
| Loại | Chứa | Lúc làm việc |
|---|---|---|
| **Bản luật** | chỉ luật đang dùng, viết như mới: không ngày, không "thay luật cũ / bổ sung 09/11", không lời kể lịch sử | đọc |
| **Sổ quyết định** | ngày · lời David nguyên văn · lý do · luật nào bị thay | không đọc (chỉ khi cân nhắc đổi luật, gỡ lỗi) |
| **Kho** | thực đơn để chọn (bố cục, nguồn học, hình mẫu) — không phải luật | chỉ khi cần chọn |

Bộ: `video` (skills/dung-video) · `hoi` (hoi-chuyen-gia) · `nao` (AGENTS, CLAUDE, David.md, thoi-quen-lam-viec). Ghi nhớ `nao/bo-nho/`
là sổ, dọn bằng skill `consolidate-memory`, không tái bản ở đây.

## Khi nào tái bản
- Máy đo vượt ngưỡng → Claude nhắc David **một dòng**, David quyết. Chạy máy đo cuối mỗi việc có sửa bản luật (thoi-quen mục 4):
  ```bash
  python3 -I skills/tai-ban/do_chong_cheo.py [video|hoi|nao] [--chi-tiet]
  ```
- Hoặc David gọi "tái bản".
- **Mỗi lần một bộ, mỗi bộ một phiên riêng** (bộ video lớn: có thể chia phiên theo nhóm file, nhưng xong cả bộ mới đóng mốc).

## Quy trình (mỗi bộ)
1. **Mốc** *(bước nhẹ)*: `bash scripts/sync.sh --push`, rồi `git tag tai-ban-<bộ>-<n>-truoc`. Chạy máy đo, lưu kết quả vào
   `dang-lam/tai-ban-<bộ>-<n>.md` (file theo dõi của đợt này).
2. **Bảng luật đang sống** (trong file theo dõi): đọc toàn bộ bản luật + sổ quyết định + ghi nhớ liên quan, mỗi luật một dòng:
   `luật · nhà nên ở · nguồn hiện tại (file:dòng, có thể nhiều) · ngày chốt gần nhất · trạng thái (sống / trùng / ngược / cũ)`.
   Luật ngược nhau: theo `thoi-quen-lam-viec.md` mục 0 (lời David vừa nói > ngày chốt gần nhất > cũ); chỗ vẫn không rõ → gom lại
   **hỏi David một lần** (hoi-chuyen-gia), có đề xuất. Không tự bỏ luật nào David đã chốt mà không có luật mới hơn thay.
3. **Viết lại từ bảng, không vá:** mỗi file bản luật viết lại thành trạng thái hiện hành.
   - Mỗi luật **một nhà**; nơi khác một dòng trỏ. Luật dùng chung nhiều skill → `thoi-quen-lam-viec.md` / `luat-chung.md`, không chép.
   - Không ngày, không "(David chốt …)", không "thay luật cũ", không "chuyển nguyên văn từ SKILL.md cũ". Lý do một luật tồn tại
     viết ngắn **trong luật** nếu giúp AI làm đúng ("vì người xem không đọc hai chỗ cùng lúc"); lịch sử thì vào sổ.
   - Giữ đúng nghĩa từng luật trong bảng; viết gọn hơn, không thêm luật mới. Code đi kèm (tên khoá, lệnh) giữ khớp.
   - Bảng "Xong khi" của mỗi skill giữ nguyên ý.
4. **Đóng sổ cũ:** mỗi sổ quyết định của bộ thêm một dòng đầu `## Tái bản <n> — <ngày>: bản luật viết lại từ bảng dang-lam/tai-ban-<bộ>-<n>.md`.
   Sổ quá dài (> 400 dòng) → chuyển phần cũ vào `luu-tru/` cạnh sổ.
5. **Kiểm** (bắt buộc, đủ cả 4):
   - **Đủ luật:** đi từng dòng bảng — luật "sống" nào cũng có nhà trong bản mới (ghi `file` vào cột nhà). Thiếu = chưa xong.
   - **Máy đo:** chạy lại; dấu ngày và câu ghi đè gần 0, câu trùng 0.
   - **Hình y nguyên** (bộ video): `python3 -I skills/dung-video/mau-chuan/kiem-mau.py` + soát cảnh một dự án cũ. Tái bản chỉ viết lại
     chữ, không đổi code; ảnh khác = có gì sai.
   - **Việc thật:** chạy skill vừa tái bản trên một đoạn ngắn trọn một ý (`luat-thu-bang-doan-ngan`), David chấm. Phải bằng hoặc tốt hơn.
6. **Đóng mốc:** `git tag tai-ban-<bộ>-<n>`, thêm một dòng vào `lich-su.md`, chỉnh ngưỡng trong `bo.json` nếu thấy lệch (ví dụ ngưỡng
   quá thấp làm nhắc liên tục), đẩy GitHub, báo David: đã gom bao nhiêu luật, bỏ / gộp gì, đã kiểm gì, chưa kiểm gì.

## Không làm
- Không đổi luật, không thêm luật mới trong lúc tái bản — chỉ viết lại. Thấy luật nên đổi → ghi vào file theo dõi, hỏi David sau.
- Không đụng kho (bố cục, nguồn học) ngoài việc sửa đường trỏ.
- Không gộp nhiều bộ trong một phiên.

## Xong khi
1. Bảng luật đang sống có đủ, mỗi dòng có nhà trong bản mới.
2. Máy đo bộ đó: "Chưa cần tái bản"; dấu ngày, câu ghi đè gần 0; câu trùng 0.
3. Mẫu chuẩn y nguyên (bộ video) và một việc thật David chấm đạt.
4. Có tag `tai-ban-<bộ>-<n>`, dòng trong `lich-su.md`, đã đẩy GitHub.

## Nhật ký
- 10/11/2026 · tạo skill. David: "mỗi lần học hay bổ sung hay sửa thì không bị chồng chéo… cứ một thời gian… viết lại toàn bộ… học được lớp 1, lớp 2, lớp 3 thì lại phải tổng kết lại toàn bộ để viết lại thành một skill hoàn chỉnh bao gồm cả 3 lớp". Chốt 5 điểm: sửa thẳng mỗi lần + lý do vào sổ · máy đo nhắc, David quyết · từng bộ một · kiểm mẫu chuẩn + việc thật · skill riêng.
