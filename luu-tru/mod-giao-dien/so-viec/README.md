---
description: "Lưu trữ: mod Sổ việc (báo cáo việc lớn) đã gỡ."
---

# Sổ việc (mod của Claude Code)

Báo cáo tổng hợp theo **việc lớn**, chữ viết đầy đủ, tự chạy ở mọi khung Claude Code trên máy, gộp mọi tài khoản. Bảng cạnh khung chat có 4 phần:

- **Đang làm trên Claude:** mọi khung đang chạy (cả khung mở trước khi cài mod): tên khung, việc lớn, đã chạy bao lâu.
- **Hạn mức tuần:** từng tài khoản Claude đã đăng nhập trên máy, đã dùng bao nhiêu phần trăm, ngày làm mới.
- **Tuần này, mỗi việc lớn tốn bao nhiêu:** phần trăm hạn mức tuần và số giờ, có thanh. Riêng làm video có thêm trung bình một video.
- **Từ đầu tới giờ:** mỗi việc lớn chiếm bao nhiêu phần trong tổng token.

**Bốn việc lớn**, mọi việc nhỏ tự quy về một việc lớn (hàm `groupOf`), việc mới xuất hiện sau này cũng tự xếp:

| Việc lớn | Gồm |
|---|---|
| Làm video | Mọi skill trong bộ skill video (`ky-nang/san-xuat-video/`, kể cả skill video thêm sau này): dựng, podcast, cắt highlight, đăng bài, học video mẫu. Một video = mọi việc video trong một khung, từ 3 phút |
| Bot Telegram | Khung có tên liên quan Telegram, tin nhắn tới từ Telegram, skill `telegram:*`, lượt model nhỏ xếp vào bot Telegram |
| Xây bộ não (skill, luật, mod) | Sửa skill, luật, ghi nhớ, cấu hình Claude, làm mod; skill `tai-cau-truc`, `plugin-authoring`, `skill-creator`, `update-config`, `consolidate-memory` |
| Trò chuyện, hỏi đáp, viết, lên kế hoạch | Mọi việc còn lại |

Lượt không gọi skill: model nhỏ chỉ chọn giữa xây bộ não, bot Telegram, trò chuyện. Skill chỉ là luật chung (`thu-thap-yeu-cau`...) không đổi việc.

**Nhiều tài khoản:** mod gắn với máy nên đổi tài khoản vẫn chạy. Mỗi tài khoản có sổ hạn mức riêng (`~/.claude/so-viec/tai-khoan/<mã>.json`, ghi khi tài khoản đó đang đăng nhập): phần trăm đã dùng, ngày làm mới, và **1% hạn mức tuần ≈ bao nhiêu token** (tổng token tài khoản đó dùng từ đầu tuần chia phần trăm đã dùng). Mỗi lượt ghi kèm 8 ký tự đầu mã tài khoản; tên hiện trên bảng là phần trước @ của email. Mỗi việc đổi ra phần trăm theo đúng tài khoản đã làm nó. Tài khoản chưa đo được thì dùng mức trung bình của các tài khoản khác. Đây là ước tính.

**Hạn mức tuần cập nhật thế nào:** mỗi khung chỉ biết phần trăm sau lượt gần nhất của chính nó, nên mod giữ **số cao nhất** các khung đọc được trong cùng một tuần (khung đang nghỉ không kéo số tụt xuống), và cập nhật ngay khi Claude Code báo hạn mức tăng thêm một điểm. Con số đi theo khung vừa chạy gần nhất: lệch trang usage tối đa khoảng 1 điểm cho tới lượt kế tiếp.

`/bao-cao` in bản chữ vào khung chat, `/so-viec` mở lại bảng.

Mod vẫn ghi ngầm mọi việc (loại việc theo skill, việc khác do model nhỏ gán nhãn), chỉ không hiện.

**Dữ liệu** (trên máy, không lên GitHub): `~/.claude/so-viec/phien/<phiên>.json` mỗi phiên tự ghi sổ của mình;
`~/.claude/so-viec/nhap/<phiên>.json` phiên cũ nhập ngược bằng `python3 -I luu-tru/mod-giao-dien/so-viec/scripts/nhap-lich-su.py`
(chạy lại bao nhiêu lần cũng được; phiên cũ: bước im quá 5 phút trong một lượt coi là chờ David, không tính).

**Đang chạy cũng hiện:** phiên mở trước khi cài mod vẫn hiện trên bảng ("chưa có mod"): mod đọc đuôi lịch sử phiên đó đang ghi (thời gian lượt, token, skill gần nhất).
**Token trực tiếp:** cộng sau mỗi lần gọi model, nên lượt dài (render) thanh token cũng chạy.

**Cài:** `bash tu-dong-hoa/cai-dat-bo-nao.sh` (hoặc `claude plugin marketplace add <repo>` rồi `claude plugin install so-viec@david-claude --scope user`), mở phiên mới. Xem [luu-tru/mod-giao-dien/README.md](../README.md).
Kiểm tra: `claude plugin validate luu-tru/mod-giao-dien/so-viec`, `claude plugin test luu-tru/mod-giao-dien/so-viec`.
