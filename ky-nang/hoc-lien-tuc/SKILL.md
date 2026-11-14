---
name: hoc-lien-tuc
description: Tự học và cải tiến liên tục bộ skill của David (học từ cách Hermes tự học, nhưng một nhà, có số liệu, ít token). Ba việc — (1) NHÌN LẠI TUẦN từ tín hiệu máy ghi cuối mỗi phiên (lời David sửa, skill dùng, lỗi) để sửa skill đúng chỗ, cập nhật giọng văn, dọn ghi nhớ và skill thừa; (2) HỌC TỪ HÌNH MẪU cùng thể loại đang có kết quả tốt nhất, đo bằng số liệu, rồi nâng cấp skill và luật kênh; (3) HỌC THÀNH SKILL từ một nguồn hay quy trình vừa làm. Skill, giọng văn, luật kênh được sửa tự do rồi báo một dòng; chỉ hỏi khi đụng thông tin về David. Dùng khi máy gửi [TU-HOC], khi David nói "nhìn lại tuần", "tự học", "cải tiến skill", "học thành skill", "học từ kênh X", "học cái này thành quy trình", "/hoc-lien-tuc".
---

# Tự học, cải tiến skill

Đọc trước: `ky-nang/chuan-muc-lam-viec.md`. Luật nền: `AGENTS.md` luật 2 (skill tự cải tiến, chỉ hỏi khi đụng thông tin David).

**Mục tiêu:** mỗi tuần bộ skill làm ra kết quả tốt hơn tuần trước (đo bằng số liệu kênh và số lần David phải sửa), tốn ít token nhất.

## Được sửa tự do / phải hỏi

- **Tự do, không hỏi:** mọi `SKILL.md`, khối, script, `references/`; giọng văn (`ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md`);
  luật kênh (`ky-nang/san-xuat-video/ho-so-thuong-hieu/kenh.json`: lịch đăng, dẫn dắt, từ khoá bình luận, cách đo); hiệu ứng, motion graphics.
- **Hỏi trước (diễn giải, chờ "ok"):** `co-so-tri-thuc/David.md`, `co-so-tri-thuc/ho-so-ca-nhan.md`, ghi nhớ David đã chốt; **màu chủ đạo** và **chữ ký
  nhận diện**; mọi thao tác trên mạng xã hội của David.
- **Không bao giờ phá:** chữ trên video là nguyên văn lời David (phụ đề, mô tả, motion graphics); quyền riêng tư (mật khẩu, OTP, token).

## Cách sửa một skill (mọi việc dưới đây dùng chung)
1. Tìm **đúng một nhà** của luật (mỗi luật một chỗ, `chuan-muc-lam-viec.md`); sửa thẳng câu cũ, không chồng lớp ("lời mới nhất thắng").
2. Ghi changelog của skill đó (`references/nhat-ky-thay-doi.md`, chưa có thì tạo): ngày · sửa gì · **vì sao** (tín hiệu nào / hình mẫu + số liệu nào).
3. Đẩy GitHub (`bash tu-dong-hoa/sync.sh --push`). Báo David **một dòng mỗi thay đổi**: `Đã sửa <skill>: <điều đổi> (vì <bằng chứng>).`
4. Chạy máy đo chồng chéo của `tai-cau-truc` khi sửa từ 5 chỗ trở lên trong tuần; báo "NÊN TÁI BẢN" thì nói David.

## Việc 1 — Nhìn lại tuần (máy gửi `[TU-HOC]` tối chủ nhật, hoặc David gọi)
Máy đã ghi sẵn tín hiệu cuối mỗi phiên (hook `tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py` → `~/.claude/hoc-lien-tuc/tin-hieu.jsonl`), không tốn token.
1. `python3 -I tu-dong-hoa/hoc-lien-tuc/dem-skill.py 7` → skill dùng nhiều, skill bị sửa nhiều, skill không dùng.
2. Đọc các dòng 7 ngày qua trong `tin-hieu.jsonl` (chỉ trường `david_sua`, `skill`, `loi_cong_cu`). Gom **điều lặp ≥ 2 lần**: cùng một
   lỗi, cùng một câu David phải nhắc, cùng một việc David làm tay. Cần thêm ngữ cảnh thì `python3 -I tu-dong-hoa/tim-phien.py "<từ khoá>"`,
   không mở cả phiên.
3. Mỗi điều lặp → sửa skill (mục trên). Việc tay lặp ≥ 3 lần → viết thành script hoặc bước trong skill (Việc 3).
4. **Giọng văn:** đọc lời David trong tuần (tin nhắn, lời nói trong video đã duyệt). Thấy cách nói mới, từ hay dùng, từ David sửa
   lại → cập nhật `giong-thuong-hieu-david.md` (ví dụ nguyên văn ngắn + ngày).
5. **Dọn:** skill 30 ngày không dùng → đề xuất gộp hoặc cất vào `luu-tru/` (không xoá). Ghi nhớ trùng / quá dài trong `co-so-tri-thuc/bo-nho/` →
   gộp chữ (giữ nguyên ý David chốt), cập nhật `MEMORY.md`.
6. Ghi phiếu tuần `du-an/hoc-lien-tuc/<YYYY-MM-DD>.md` (không chép lời chat thô): điều lặp · đã sửa gì · số liệu kênh tuần · việc tuần sau.
   Gửi David bản ngắn qua `bash tu-dong-hoa/so-tay/bao-cao.sh "📈 Tự học tuần: …"`.

## Việc 2 — Học từ hình mẫu có số liệu
1. **Số liệu của David trước:** đọc số liệu kênh (bước đo của `phan-phoi-da-kenh`, `kenh.json` mục đo). Video nào tốt / kém nhất tuần, khác nhau ở đâu.
2. **Hình mẫu:** chọn 2–3 kênh cùng thể loại, cùng ngôn ngữ hoặc cùng tệp người xem, đang có số liệu tốt nhất **có thể kiểm**
   (lượt xem trên số người theo dõi, lượt xem trung bình 10 video gần nhất, tương tác). Ghi nguồn + số liệu + ngày đo.
3. Học **cái làm ra số liệu** (mở đầu 3 giây, nhịp, độ dài, tít, bìa, lịch đăng, câu kêu gọi), không chép nội dung. Video mẫu cụ thể
   thì dùng `phan-tich-video-mau`.
4. Đưa vào skill / `kenh.json` theo "Cách sửa"; ghi giả thuyết đo lại: "đổi X, kỳ vọng Y tăng; đo lại sau N video". Tuần sau đo:
   không cải thiện thì quay lại bản cũ (git) và ghi bài học.

## Việc 3 — Học thành skill (giống `/learn` của Hermes)
Nguồn: tài liệu, link, thư mục, hoặc "quy trình vừa làm trong phiên này".
1. Có skill gần đúng việc này → **bổ sung vào skill đó** (ưu tiên). Chỉ tạo skill mới khi việc lặp ≥ 3 lần hoặc David yêu cầu.
2. Tạo mới: theo `skill-creator`; thư mục `ky-nang/<ten-khong-dau>/SKILL.md`; mô tả nói rõ khi nào dùng (câu David hay nói);
   thêm một dòng vào bảng chọn skill trong `AGENTS.md`; chạy `bash tu-dong-hoa/install.sh` nếu skill cần liên kết vào `~/.claude/skills`.
3. Thử một lần trên việc thật hoặc đoạn ngắn (`quy-tac-thu-bang-doan-ngan`), rồi báo David một dòng.

## Tiết kiệm token
- Script làm phần đếm, tìm; Claude chỉ đọc kết quả gọn. Không đọc cả nhật ký phiên.
- Một lượt nhìn lại mỗi tuần; Việc 2 chỉ khi có số liệu mới (≥ 3 video từ lần học trước) hoặc David gọi.
- Việc nặng chạy trong phiên Claude Code riêng (bot giao qua `giao-viec.sh`), không chạy trong bot Telegram.
