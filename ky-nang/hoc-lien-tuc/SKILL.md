---
name: hoc-lien-tuc
description: Tự học và cải tiến liên tục bộ skill của David (học từ cách Hermes tự học, nhưng giữ một nguồn duy nhất, có số liệu, tốn ít token). Bốn việc — (1) NHÌN LẠI TUẦN từ tín hiệu hệ thống tự động ghi cuối mỗi phiên (lời David sửa, skill đã dùng, lỗi) để sửa skill đúng chỗ, cập nhật giọng văn, dọn ghi nhớ và skill thừa; (2) HỌC TỪ HÌNH MẪU cùng thể loại đang có kết quả tốt nhất, đo bằng số liệu, rồi nâng cấp skill và luật kênh; (3) HỌC THÀNH SKILL từ một nguồn hay quy trình vừa làm; (4) NÂNG CẤP định kỳ cả bộ não như R&D: đo trước, chưng cất luật lẻ thành nguyên lý, cắt giảm phần không mang lại kết quả, dọn trùng / rối (tai-cau-truc), đo sau, chỉ ra bản mới khi bằng hoặc tốt hơn. Phân tích và sửa đều tự chạy theo quy trình này, báo David sau; chỉ chờ David chốt khi đưa lên tầng 1, đổi nghĩa tầng 0, hay sửa thông tin về David. Dùng khi hệ thống tự động gửi [TU-HOC], khi David nói "nhìn lại tuần", "tự học", "cải tiến skill", "học thành skill", "học từ kênh X", "học cái này thành quy trình", "nâng cấp", "nâng cấp bộ não", "tái bản", "/hoc-lien-tuc", hoặc khi công cụ đo chồng chéo báo "NÊN NÂNG CẤP".
---

# Tự học, cải tiến skill

Đọc trước: `co-so-tri-thuc/truc-tri-thuc.md` (trục: bốn tầng, luật thăng cấp, ba vòng học, bốn thước đo — skill này là vòng "mỗi tuần" và "Nâng cấp") · `ky-nang/chuan-muc-lam-viec.md`. Luật nền: `AGENTS.md` luật 2 (đã có quy trình thì tự động hoàn toàn; skill này là quy trình nên tự chạy trọn, cần đổi thì sửa chính skill).

**Mục tiêu:** mỗi tuần bộ skill làm ra kết quả tốt hơn tuần trước (đo bằng số liệu kênh và số lần David phải sửa), tốn ít token nhất.
Học càng nhiều thì bộ não càng lớn, và lớn là đúng hướng; việc của skill này là giữ cho bộ não **càng lớn càng dễ hiểu, càng làm đúng**.

Ba vòng học (mỗi việc · mỗi tuần · Nâng cấp) và luật thăng cấp giữa các tầng được nêu ở trục mục 4–5. Skill này làm vòng tuần (Việc 1–3) và Nâng cấp (Việc 4).

## Tự sửa theo quy trình, báo sau

Phần phân tích (đếm skill, đọc tín hiệu, so số liệu) và **phần sửa** đều tự chạy, không hỏi. Claude sửa liền một mạch theo "Cách sửa" dưới,
ghi nhật ký thay đổi, push, rồi báo David một dòng cho mỗi thay đổi kèm lý do có số liệu (`chuan-muc-lam-viec.md` mục 2). Chỉ chờ David chốt: đưa lên tầng 1, đổi nghĩa tầng 0, thông tin về David (mục dưới).
- **Phạm vi Claude tự sửa:** mọi `SKILL.md`, khối, script, `references/`; giọng văn (`ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md`);
  luật kênh (`ky-nang/san-xuat-video/ho-so-thuong-hieu/kenh.json`: lịch đăng, dẫn dắt, từ khoá bình luận, cách đo); hiệu ứng, motion graphics.
- **Trình David chờ "duyệt" trước khi sửa (Đ3, thông tin về David):** `co-so-tri-thuc/david.md`, `co-so-tri-thuc/ho-so-ca-nhan.md`, ghi nhớ David đã chốt; **màu chủ đạo** và **chữ ký
  nhận diện**; mọi thao tác trên mạng xã hội của David.
- **Không bao giờ vi phạm:** chữ trên video là nguyên văn lời David (phụ đề, mô tả, motion graphics); quyền riêng tư (mật khẩu, OTP, token).

## Cách sửa một skill (mọi việc dưới đây dùng chung)
1. Tìm **đúng một nguồn duy nhất** của luật (mỗi luật một chỗ, `chuan-muc-lam-viec.md`); sửa trực tiếp vào câu cũ, không chồng thêm lớp mới ("lời mới nhất thắng").
2. Ghi nhật ký thay đổi của skill đó (`references/nhat-ky-thay-doi.md`, chưa có thì tạo): ngày · sửa gì · **vì sao** (tín hiệu nào, hoặc hình mẫu và số liệu nào).
3. Push lên GitHub (`bash tu-dong-hoa/dong-bo.sh --push`). Báo David **một dòng cho mỗi thay đổi**: `Đã sửa <skill>: <điều đổi> (vì <bằng chứng>).`
4. Chạy công cụ đo chồng chéo (`python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py`) khi sửa từ 5 chỗ trở lên trong tuần; công cụ báo "NÊN NÂNG CẤP" thì nhắc David một dòng (Việc 4).

## Việc 1 — Nhìn lại tuần (hệ thống tự động gửi `[TU-HOC]` 07:00 sáng thứ 6 — ngày tổng kết tuần, hoặc khi David yêu cầu)
Hệ thống tự động đã ghi sẵn tín hiệu cuối mỗi phiên (hook `tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py` ghi vào `~/.claude/hoc-lien-tuc/tin-hieu.jsonl`), không tốn token.
1. Chạy `python3 -I tu-dong-hoa/hoc-lien-tuc/dem-ky-nang.py 7` để có danh sách skill dùng nhiều, skill bị sửa nhiều, skill không dùng.
2. Đọc các dòng 7 ngày qua trong `tin-hieu.jsonl` (chỉ trường `david_sua`, `skill`, `loi_cong_cu`). Gom **điều lặp ít nhất 2 lần**: cùng một
   lỗi, cùng một câu David phải nhắc, cùng một việc David làm thủ công. Cần thêm ngữ cảnh thì chạy `python3 -I tu-dong-hoa/tim-phien.py "<từ khoá>"`,
   không mở cả phiên.
3. Mỗi điều lặp thành một chỗ sửa (Claude tự sửa theo "Cách sửa") **và một câu kiểm** vào bộ kiểm của bộ đó (trục mục 4), để bản sau không lặp lại. Việc làm thủ công lặp ít nhất 3 lần thì viết thành script hoặc bước trong skill (Việc 3).
4. **Giọng văn:** đọc lời David trong tuần (tin nhắn, lời nói trong video đã duyệt). Thấy cách nói mới, từ hay dùng, từ David sửa
   lại thì cập nhật `giong-thuong-hieu-david.md` (ví dụ nguyên văn ngắn kèm ngày).
5. **Dọn:** skill 30 ngày không dùng thì đề xuất gộp hoặc chuyển vào `luu-tru/` (không xoá). Ghi nhớ trùng hoặc quá dài trong `co-so-tri-thuc/bo-nho/` thì
   gộp lại phần chữ (giữ nguyên ý David đã chốt), cập nhật `MEMORY.md`.
6. Ghi phiếu tuần `du-an/hoc-lien-tuc/<YYYY-MM-DD>.md` (không chép nguyên nội dung trò chuyện thô): điều lặp · đã sửa gì · số liệu kênh tuần · việc tuần sau.
   Sửa xong thì ghi "đã sửa gì" vào phiếu, báo `📈 Tự học tuần: …`; điều cần David chốt (tầng 1, tầng 0, Đ3) ghi riêng một mục.

## Việc 2 — Học từ hình mẫu có số liệu
1. **Số liệu của David trước:** đọc số liệu kênh (bước đo của `phan-phoi-da-kenh`, `kenh.json` mục đo). Xác định video nào tốt nhất và kém nhất tuần, chúng khác nhau ở đâu.
2. **Hình mẫu:** tra bản đồ `co-so-tri-thuc/hinh-mau/` trước; chọn ít nhất 5 kênh (việc lớn thì 10 kênh) cùng thể loại, cùng ngôn ngữ hoặc
   cùng nhóm người xem mục tiêu, đang có số liệu tốt nhất **có thể kiểm chứng** (lượt xem trên số người theo dõi, lượt xem trung bình 10 video gần nhất,
   tương tác). Ghi nguồn, số liệu và ngày đo vào bảng mục nhỏ của bản đồ và một mục nhật ký (quy trình lá A8).
3. Học **yếu tố tạo ra số liệu** (mở đầu 3 giây, nhịp, độ dài, tiêu đề, bìa, lịch đăng, câu kêu gọi hành động), không chép nội dung. Video mẫu cụ thể
   thì dùng `phan-tich-video-mau`.
4. Đưa vào skill hoặc `kenh.json` theo "Cách sửa"; ghi giả thuyết đo lại: "đổi X, kỳ vọng Y tăng; đo lại sau N video". Tuần sau đo lại:
   không cải thiện thì quay lại bản trước (git) và ghi bài học rút ra.

## Việc 3 — Học thành skill (giống `/learn` của Hermes)
Nguồn: tài liệu, link, thư mục, hoặc "quy trình vừa làm trong phiên này".
1. Có skill gần đúng việc này thì **bổ sung vào skill đó** (ưu tiên). Chỉ tạo skill mới khi việc lặp ít nhất 3 lần hoặc David yêu cầu.
2. Tạo mới: theo `skill-creator`; thư mục `ky-nang/<ten-khong-dau>/SKILL.md`; mô tả nói rõ khi nào dùng (câu David hay nói);
   thêm một dòng vào bảng chọn skill trong `AGENTS.md`; chạy `bash tu-dong-hoa/cai-dat-bo-nao.sh` nếu skill cần liên kết vào `~/.claude/skills`.
3. Thử một lần trên việc thật hoặc đoạn ngắn (`quy-tac-thu-bang-doan-ngan`), rồi báo David một dòng.

## Việc 4 — Nâng cấp (định kỳ, cả bộ não một đợt)
**Khi:** công cụ đo báo "NÊN NÂNG CẤP" (trùng / rối vượt ngưỡng), hoặc từ lần nâng cấp trước đã có **ít nhất 10 video có số liệu 7 ngày**, hoặc David
nói "nâng cấp" hoặc "tái bản". Nhắc David một dòng; David quyết định. Mỗi đợt có một mốc chung `nang-cap-<n>` và một file theo dõi `du-an/nang-cap-<n>.md`.

**Thước đo** (cùng một bảng, đo trước và sau; bản mới chỉ được ra khi **bằng hoặc tốt hơn ở mọi dòng**):
| # | Thước đo | Cách đo | Đạt |
|---|---|---|---|
| 1 | **Người xem thật** (thước đo chính) | trung vị 10 video gần nhất từ `so-lieu.md` các dự án (khối 16): số tin nhắn "gỡ", bình luận "Vấn đề"·"Kết quả", % còn lại ở giây 3, tỉ lệ xem hết | không giảm; đổi luật nào thì ghi giả thuyết "kỳ vọng Y tăng, đo lại sau N video" |
| 2 | **Suy luận** | AI làm bài kiểm thật ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/` (không mở đáp án), chấm bằng `cham.py` | ít nhất 8/10 và không thấp hơn lần trước |
| 3 | **Hình** | `python3 -I ky-nang/san-xuat-video/mau-chuan/kiem-mau.py` (dự án mẫu phải có trên máy; nếu đang ở Drive thì tải về trước) | giữ y nguyên, trừ chỗ đổi có chủ đích |
| 4 | **Số lần David phải sửa** | `tin-hieu.jsonl` (trường `david_sua`) theo video / việc | giảm hoặc không tăng |
| 5 | **Trùng / rối** | công cụ đo chồng chéo | mọi bộ "Chưa cần" |
Thước đo nào chưa có dữ liệu (chưa đủ video có số liệu, dự án mẫu chưa tải về) thì ghi "chưa đo" và lý do, không đoán.

**Năm bước:**
1. **Mốc và đo trước** *(bước nhẹ)*: `bash tu-dong-hoa/dong-bo.sh --push`, `git tag nang-cap-<n>-truoc`, ghi bảng thước đo "trước" vào file theo dõi.
2. **Chưng cất:** đọc phiếu tuần, sổ quyết định, ghi nhớ từ lần nâng cấp trước. Nhóm các luật lẻ **cùng một gốc** (cùng một khó khăn của
   người xem, cùng lý do) thành **một nguyên lý kèm 1–3 trường hợp mẫu** ở nguồn chung; luật lẻ trở thành ví dụ của nguyên lý (theo cách tầng
   `nhu-cau-nguoi-xem.md` và `truong-hop-da-giai.md` đã làm). Giữ đúng nghĩa luật David đã chốt; không thêm luật mới.
3. **Cắt giảm:** luật, kiểu cảnh, skill không được dùng từ lần trước (`dem-ky-nang.py`, kiểu không xuất hiện trong `ke-hoach-canh.md` các dự án)
   hoặc số liệu cho thấy không mang lại kết quả thì đề xuất gộp, bỏ hoặc chuyển vào `luu-tru/`. Không tự ý bỏ.
4. **Dọn:** skill `tai-cau-truc` (bảng luật hiện hành, mỗi luật một nguồn duy nhất, chuyển các mốc ngày về sổ, dọn ghi nhớ).
5. **Đo sau và ra bản:** chạy lại bảng thước đo. Đạt thì `git tag nang-cap-<n>`, ghi một dòng ở `ky-nang/tai-cau-truc/lich-su.md`, chỉnh ngưỡng
   `bo.json` nếu lệch, push lên GitHub, báo David: chưng cất gì, cắt giảm gì, thước đo trước và sau, chưa đo gì. Kém hơn ở một dòng thì sửa chỗ gây
   ra, hoặc quay lại mốc `nang-cap-<n>-truoc`, ghi bài học rút ra vào file theo dõi.

Bước 2–3 là phần sửa: Claude tự làm theo quy trình này (mục "Tự sửa theo quy trình"), báo số đo trước và sau khi sửa; cắt giảm (bỏ, gộp luật) thì David chốt. Thước đo 1 (người xem) thường chỉ đo lại được
sau vài video: ra bản khi thước đo 2–5 đạt, ghi giả thuyết cho thước đo 1 và đo ở lần nhìn lại tuần sau khi đủ video.

## Tiết kiệm token
- Script làm phần đếm và tìm; Claude chỉ đọc kết quả rút gọn. Không đọc cả nhật ký phiên.
- Một lượt nhìn lại mỗi tuần; Việc 2 chỉ chạy khi có số liệu mới (ít nhất 3 video từ lần học trước) hoặc khi David yêu cầu.
- Việc tốn nhiều tài nguyên chạy trong phiên Claude Code riêng (bot giao qua `giao-viec.sh`), không chạy trong bot Telegram.

## Xong khi
- **Việc 1 (nhìn lại tuần):** đã sửa xong mọi điều lặp (hoặc báo "tuần này không có gì cần sửa" kèm số tín hiệu đã đọc); phần sửa nằm ở
  đúng một nguồn duy nhất, có dòng nhật ký thay đổi, đã push lên GitHub, đã báo David một dòng cho mỗi thay đổi.
- **Việc 2 (học hình mẫu):** phiếu học có số liệu đo kèm ngày đo, mỗi cách học có dấu hiệu nhận biết và nguồn; phần đưa vào skill có code hoặc luật thật, đã báo David.
- **Việc 3 (học thành skill):** cách làm trở thành một lá trong cây quy trình `quy-trinh.md` (file quy trình đủ khung, script trong repo), chạy thử
  một lần ra đúng kết quả.
- **Việc 4 (nâng cấp):** thước đo sau tốt hơn hoặc bằng trước ở thước đo 2–5, `do-chong-cheo.py` dưới ngưỡng, có mốc `nang-cap-<n>`.
