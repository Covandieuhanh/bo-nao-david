# Sổ việc (mod của Claude Code)

Tự đo từng việc Claude làm ở **mọi phiên Claude Code trên máy**, không hỏi David gì. Chat claude.ai và app điện thoại không đo được (mod chỉ chạy trong Claude Code).

- **Loại việc:** lấy từ skill được gọi (`video-style-edit`, `cat-highlight-video`...). Việc không gọi skill thì model nhỏ tự gán nhãn (`sua-bo-nao`, `viet-bai`, `nghien-cuu`, `lap-ke-hoach`, `lam-mod`, `hoi-dap`, `khac`). Trả lời ngắn ("ok", "làm đi") tính vào việc đang làm.
- **Thời gian:** lúc Claude chạy. Im lặng quá 60 phút thì việc cũ coi như xong.
- **Token:** mọi token của các lượt trong việc, kể cả trợ lý con.
- **Dự kiến:** trung bình các lần trước cùng loại, cần ít nhất 3 lần.
- **Giờ hôm nay / tuần này:** gộp lượt của mọi phiên (hai khung chạy cùng lúc không tính đôi), nối khoảng nghỉ ≤15 phút; đủ 4 tiếng thì báo.

**Bảng "Sổ việc"** cạnh khung chat, khung nào cũng hiện cùng một tổng quan, có thanh tiến độ:
đang làm ở mọi khung (thời gian và token so với dự kiến) · hôm nay X/4h · tuần này · từ đầu · theo loại việc · 10 việc gần nhất.
`/so-viec` mở lại bảng, `/bao-cao` in bản đầy đủ vào khung chat, dòng trạng thái hiện việc của khung này.

**Dữ liệu** (trên máy, không lên GitHub): `~/.claude/so-viec/phien/<phiên>.json` mỗi phiên tự ghi sổ của mình;
`~/.claude/so-viec/nhap/<phiên>.json` phiên cũ nhập ngược bằng `python3 -I mods/so-viec/scripts/nhap-lich-su.py`
(chạy lại bao nhiêu lần cũng được; phiên cũ: bước im quá 5 phút trong một lượt coi là chờ David, không tính).

**Đang chạy cũng hiện:** phiên mở trước khi cài mod vẫn hiện trên bảng ("chưa có mod"): mod đọc đuôi lịch sử phiên đó đang ghi (thời gian lượt, token, skill gần nhất).
**Token trực tiếp:** cộng sau mỗi lần gọi model, nên lượt dài (render) thanh token cũng chạy.

**Cài:** `bash scripts/install.sh` (hoặc `claude plugin marketplace add <repo>` rồi `claude plugin install so-viec@david-claude --scope user`), mở phiên mới. Xem [mods/README.md](../README.md).
Kiểm tra: `claude plugin validate mods/so-viec`, `claude plugin test mods/so-viec`.
