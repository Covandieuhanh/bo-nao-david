---
name: hoc-lien-tuc
description: Tự học và cải tiến liên tục bộ skill của David (học từ cách Hermes tự học, nhưng một nguồn duy nhất, có số liệu, ít token). Bốn việc — (1) NHÌN LẠI TUẦN từ tín hiệu máy ghi cuối mỗi phiên (lời David sửa, skill dùng, lỗi) để sửa skill đúng chỗ, cập nhật giọng văn, dọn ghi nhớ và skill thừa; (2) HỌC TỪ HÌNH MẪU cùng thể loại đang có kết quả tốt nhất, đo bằng số liệu, rồi nâng cấp skill và luật kênh; (3) HỌC THÀNH SKILL từ một nguồn hay quy trình vừa làm; (4) NÂNG CẤP định kỳ cả bộ não như R&D: đo trước, chưng cất luật lẻ thành nguyên lý, cắt giảm cái không giúp, dọn trùng / rối (tai-cau-truc), đo sau, chỉ ra bản mới khi bằng hoặc tốt hơn. Phân tích tự chạy; phần sửa skill, giọng văn, luật kênh trình 4 phần cho David duyệt rồi mới sửa. Dùng khi máy gửi [TU-HOC], khi David nói "nhìn lại tuần", "tự học", "cải tiến skill", "học thành skill", "học từ kênh X", "học cái này thành quy trình", "nâng cấp", "nâng cấp bộ não", "tái bản", "/hoc-lien-tuc", hoặc khi công cụ đo chồng chéo báo "NÊN NÂNG CẤP".
---

# Tự học, cải tiến skill

Đọc trước: `co-so-tri-thuc/truc-tri-thuc.md` (trục: bốn tầng, luật thăng cấp, ba vòng học, bốn thước — skill này là vòng "mỗi tuần" và "Nâng cấp") · `ky-nang/chuan-muc-lam-viec.md`. Luật nền: `AGENTS.md` luật 2 (việc gì cũng duyệt 4 phần trước; tự học tự phân tích, phần sửa trình 4 phần).

**Mục tiêu:** mỗi tuần bộ skill làm ra kết quả tốt hơn tuần trước (đo bằng số liệu kênh và số lần David phải sửa), tốn ít token nhất.
Học càng nhiều thì bộ não càng lớn, và lớn là đúng; việc của skill này là giữ cho nó **càng lớn càng dễ hiểu, càng làm đúng**.

Ba vòng học (mỗi việc · mỗi tuần · Nâng cấp) và luật thăng cấp giữa các tầng: trục mục 4–5. Skill này làm vòng tuần (Việc 1–3) và Nâng cấp (Việc 4).

## Duyệt 4 phần rồi mới sửa

Phần phân tích (đếm skill, đọc tín hiệu, so số liệu) tự chạy, không hỏi. **Phần sửa** gom thành **một bộ 4 phần** (Mục tiêu · Kế hoạch: từng chỗ sửa + lý do có số liệu ·
Quy trình · Thực thi), gửi David `bao-cao.sh "#N ❓ Chờ anh duyệt 4 phần tự học tuần: …"` rồi dừng; duyệt rồi sửa một mạch, ghi sổ thay đổi (`chuan-muc-lam-viec.md` mục 2, David 14/11/2026).
- **Phạm vi được đề xuất sửa:** mọi `SKILL.md`, khối, script, `references/`; giọng văn (`ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md`);
  luật kênh (`ky-nang/san-xuat-video/ho-so-thuong-hieu/kenh.json`: lịch đăng, dẫn dắt, từ khoá bình luận, cách đo); hiệu ứng, motion graphics.
- **Diễn giải kỹ trong 4 phần (đụng thông tin về David):** `co-so-tri-thuc/david.md`, `co-so-tri-thuc/ho-so-ca-nhan.md`, ghi nhớ David đã chốt; **màu chủ đạo** và **chữ ký
  nhận diện**; mọi thao tác trên mạng xã hội của David.
- **Không bao giờ phá:** chữ trên video là nguyên văn lời David (phụ đề, mô tả, motion graphics); quyền riêng tư (mật khẩu, OTP, token).

## Cách sửa một skill (mọi việc dưới đây dùng chung)
1. Tìm **đúng một nguồn duy nhất** của luật (mỗi luật một chỗ, `chuan-muc-lam-viec.md`); sửa thẳng câu cũ, không chồng lớp ("lời mới nhất thắng").
2. Ghi changelog của skill đó (`references/nhat-ky-thay-doi.md`, chưa có thì tạo): ngày · sửa gì · **vì sao** (tín hiệu nào / hình mẫu + số liệu nào).
3. Đẩy GitHub (`bash tu-dong-hoa/dong-bo.sh --push`). Báo David **một dòng mỗi thay đổi**: `Đã sửa <skill>: <điều đổi> (vì <bằng chứng>).`
4. Chạy công cụ đo chồng chéo (`python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py`) khi sửa từ 5 chỗ trở lên trong tuần; báo "NÊN NÂNG CẤP" thì nhắc David một dòng (Việc 4).

## Việc 1 — Nhìn lại tuần (máy gửi `[TU-HOC]` 07:00 sáng thứ 6 — ngày tổng kết tuần, hoặc David gọi)
Máy đã ghi sẵn tín hiệu cuối mỗi phiên (hook `tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py` → `~/.claude/hoc-lien-tuc/tin-hieu.jsonl`), không tốn token.
1. `python3 -I tu-dong-hoa/hoc-lien-tuc/dem-ky-nang.py 7` cho ra skill dùng nhiều, skill bị sửa nhiều, skill không dùng.
2. Đọc các dòng 7 ngày qua trong `tin-hieu.jsonl` (chỉ trường `david_sua`, `skill`, `loi_cong_cu`). Gom **điều lặp ít nhất 2 lần**: cùng một
   lỗi, cùng một câu David phải nhắc, cùng một việc David làm thủ công. Cần thêm ngữ cảnh thì `python3 -I tu-dong-hoa/tim-phien.py "<từ khoá>"`,
   không mở cả phiên.
3. Mỗi điều lặp thành một chỗ sửa trong bộ 4 phần (mục trên) **và một câu kiểm** vào bộ kiểm của bộ đó (trục mục 4), để bản sau không lặp lại. Việc tay lặp ít nhất 3 lần thì viết thành script hoặc bước trong skill (Việc 3).
4. **Giọng văn:** đọc lời David trong tuần (tin nhắn, lời nói trong video đã duyệt). Thấy cách nói mới, từ hay dùng, từ David sửa
   lại thì cập nhật `giong-thuong-hieu-david.md` (ví dụ nguyên văn ngắn + ngày).
5. **Dọn:** skill 30 ngày không dùng thì đề xuất gộp hoặc cất vào `luu-tru/` (không xoá). Ghi nhớ trùng / quá dài trong `co-so-tri-thuc/bo-nho/` thì
   gộp chữ (giữ nguyên ý David chốt), cập nhật `MEMORY.md`.
6. Ghi phiếu tuần `du-an/hoc-lien-tuc/<YYYY-MM-DD>.md` (không chép lời chat thô): điều lặp · đề xuất sửa (4 phần) · số liệu kênh tuần · việc tuần sau.
   Gửi David 4 phần chờ duyệt; duyệt rồi sửa, ghi "đã sửa gì" vào phiếu, báo `📈 Tự học tuần: …`.

## Việc 2 — Học từ hình mẫu có số liệu
1. **Số liệu của David trước:** đọc số liệu kênh (bước đo của `phan-phoi-da-kenh`, `kenh.json` mục đo). Video nào tốt / kém nhất tuần, khác nhau ở đâu.
2. **Hình mẫu:** tra bản đồ `co-so-tri-thuc/hinh-mau/` trước; chọn ít nhất 5 kênh (việc lớn 10) cùng thể loại, cùng ngôn ngữ hoặc
   cùng tệp người xem, đang có số liệu tốt nhất **có thể kiểm** (lượt xem trên số người theo dõi, lượt xem trung bình 10 video gần nhất,
   tương tác). Ghi nguồn + số liệu + ngày đo vào bảng mục nhỏ của bản đồ và một mục nhật ký (quy trình lá A8).
3. Học **cái làm ra số liệu** (mở đầu 3 giây, nhịp, độ dài, tít, bìa, lịch đăng, câu kêu gọi), không chép nội dung. Video mẫu cụ thể
   thì dùng `phan-tich-video-mau`.
4. Đưa vào skill / `kenh.json` theo "Cách sửa"; ghi giả thuyết đo lại: "đổi X, kỳ vọng Y tăng; đo lại sau N video". Tuần sau đo:
   không cải thiện thì quay lại bản cũ (git) và ghi bài học.

## Việc 3 — Học thành skill (giống `/learn` của Hermes)
Nguồn: tài liệu, link, thư mục, hoặc "quy trình vừa làm trong phiên này".
1. Có skill gần đúng việc này thì **bổ sung vào skill đó** (ưu tiên). Chỉ tạo skill mới khi việc lặp ít nhất 3 lần hoặc David yêu cầu.
2. Tạo mới: theo `skill-creator`; thư mục `ky-nang/<ten-khong-dau>/SKILL.md`; mô tả nói rõ khi nào dùng (câu David hay nói);
   thêm một dòng vào bảng chọn skill trong `AGENTS.md`; chạy `bash tu-dong-hoa/cai-dat-bo-nao.sh` nếu skill cần liên kết vào `~/.claude/skills`.
3. Thử một lần trên việc thật hoặc đoạn ngắn (`quy-tac-thu-bang-doan-ngan`), rồi báo David một dòng.

## Việc 4 — Nâng cấp (định kỳ, cả bộ não một đợt)
**Khi:** công cụ đo báo "NÊN NÂNG CẤP" (trùng / rối vượt ngưỡng), hoặc từ lần nâng cấp trước đã có **ít nhất 10 video có số liệu 7 ngày**, hoặc David
nói "nâng cấp" / "tái bản". Nhắc David một dòng; David quyết. Mỗi đợt một mốc chung `nang-cap-<n>`, một file theo dõi `du-an/nang-cap-<n>.md`.

**Thước đo** (cùng một bảng, đo trước và sau; bản mới chỉ ra khi **bằng hoặc tốt hơn ở mọi dòng**):
| # | Thước đo | Cách đo | Đạt |
|---|---|---|---|
| 1 | **Người xem thật** (thước đo chính) | trung vị 10 video gần nhất từ `so-lieu.md` các dự án (khối 16): số nhắn "gỡ" / bình luận "Vấn đề"·"Kết quả", % còn lại ở giây 3, tỉ lệ xem hết | không giảm; đổi luật nào thì ghi giả thuyết "kỳ vọng Y tăng, đo lại sau N video" |
| 2 | **Suy luận** | AI làm thật `ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/` (không mở đáp án), chấm `cham.py` | ít nhất 8/10 và không thấp hơn lần trước |
| 3 | **Hình** | `python3 -I ky-nang/san-xuat-video/mau-chuan/kiem-mau.py` (dự án mẫu phải có trên máy; ở Drive thì kéo về trước) | y nguyên, trừ chỗ đổi có chủ đích |
| 4 | **Số lần David phải sửa** | `tin-hieu.jsonl` (trường `david_sua`) theo video / việc | giảm hoặc không tăng |
| 5 | **Trùng / rối** | công cụ đo chồng chéo | mọi bộ "Chưa cần" |
Thước đo nào chưa có dữ liệu (chưa đủ video có số liệu, dự án mẫu chưa kéo về) thì ghi "chưa đo" và lý do, không đoán.

**Năm bước:**
1. **Mốc + đo trước** *(bước nhẹ)*: `bash tu-dong-hoa/dong-bo.sh --push`, `git tag nang-cap-<n>-truoc`, ghi bảng thước đo "trước" vào file theo dõi.
2. **Chưng cất:** đọc phiếu tuần, sổ quyết định, ghi nhớ từ lần nâng cấp trước. Nhóm các luật lẻ **cùng một gốc** (cùng cái khó của
   người xem, cùng lý do) thành **một nguyên lý + 1–3 trường hợp mẫu** ở nguồn chung; luật lẻ trở thành ví dụ của nguyên lý (cách tầng
   `nguoi-xem-can-gi.md` + `giai-mau.md` đã làm). Giữ đúng nghĩa luật David đã chốt; không thêm luật mới.
3. **Cắt giảm:** luật, kiểu cảnh, skill không được dùng từ lần trước (`dem-ky-nang.py`, kiểu không xuất hiện trong `ke-hoach-canh.md` các dự án)
   hoặc số liệu cho thấy không giúp thì đề xuất gộp, bỏ hoặc cất `luu-tru/`. Không tự bỏ.
4. **Dọn:** skill `tai-cau-truc` (bảng luật hiện hành, mỗi luật một nguồn duy nhất, ngày về sổ, dọn ghi nhớ).
5. **Đo sau + ra bản:** chạy lại bảng thước đo. Đạt thì `git tag nang-cap-<n>`, một dòng ở `ky-nang/tai-cau-truc/lich-su.md`, chỉnh ngưỡng
   `bo.json` nếu lệch, đẩy GitHub, báo David: chưng cất gì, cắt giảm gì, thước đo trước và sau, chưa đo gì. Kém hơn ở một dòng thì sửa chỗ gây
   ra, hoặc quay về mốc `nang-cap-<n>-truoc`, ghi bài học vào file theo dõi.

Bước 2–3 là phần sửa: gom thành **một bộ 4 phần** (mục "Duyệt 4 phần") trước khi sửa. Thước đo 1 (người xem) thường chỉ đo lại được
sau vài video: ra bản khi 2–5 đạt, ghi giả thuyết cho thước 1 và đo ở lần nhìn lại tuần sau đủ video.

## Tiết kiệm token
- Script làm phần đếm, tìm; Claude chỉ đọc kết quả gọn. Không đọc cả nhật ký phiên.
- Một lượt nhìn lại mỗi tuần; Việc 2 chỉ khi có số liệu mới (ít nhất 3 video từ lần học trước) hoặc David gọi.
- Việc nặng chạy trong phiên Claude Code riêng (bot giao qua `giao-viec.sh`), không chạy trong bot Telegram.

## Xong khi
- **Việc 1 (nhìn lại tuần):** có bộ 4 phần gửi David (hoặc báo "tuần này không có gì cần sửa" kèm số tín hiệu đã đọc); sửa đã duyệt nằm ở
  đúng một nguồn duy nhất, có dòng changelog, đã đẩy GitHub, báo David một dòng mỗi thay đổi.
- **Việc 2 (học hình mẫu):** phiếu học có số liệu đo kèm ngày đo, mỗi cách học có dấu hiệu nhận ra và nguồn; phần đưa vào skill đã duyệt và có code / luật thật.
- **Việc 3 (học thành skill):** cách làm thành một lá trong cây quy trình `quy-trinh.md` (file quy trình đủ khung, script trong repo), chạy thử
  một lần ra đúng kết quả.
- **Việc 4 (nâng cấp):** thước đo sau tốt hơn hoặc bằng trước ở thước 2–5, `do-chong-cheo.py` dưới ngưỡng, có mốc `nang-cap-<n>`.
