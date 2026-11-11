# Sổ việc (mod của Claude Code)

Tự đo từng việc Claude làm, không hỏi David gì:

- **Loại việc:** lấy từ skill được gọi (`video-style-edit`, `cat-highlight-video`...). Việc không gọi skill thì model nhỏ tự gán nhãn (`sua-bo-nao`, `viet-bai`, `nghien-cuu`, `lap-ke-hoach`, `lam-mod`, `hoi-dap`, `khac`). Trả lời ngắn ("ok", "làm đi") tính vào việc đang làm.
- **Thời gian:** chỉ lúc Claude thật sự chạy, không tính lúc chờ duyệt. Im lặng quá 60 phút thì việc cũ coi như xong.
- **Token:** cộng mọi token của các lượt trong việc, kể cả trợ lý con.
- **Dự kiến:** trung bình các lần trước cùng loại, cần ít nhất 3 lần.
- **Hôm nay X/4h:** thời gian các lượt cộng khoảng nghỉ ≤15 phút giữa hai lượt; đủ 4 tiếng thì báo.

Hiện ra ở: bảng "Sổ việc" cạnh khung chat (`/so-viec` để mở lại), dòng trạng thái, lệnh `/bao-cao` (bảng trung bình theo loại việc).

Số liệu lưu trên máy (kho của mod), **không** lên GitHub. Code ở đây là bản gốc.

**Cài trên máy** (Mac chính đã cài): thêm vào `~/.claude/settings.json`:
`"env": { "CLAUDE_CODE_PLUGIN_DIRS": "/Users/moon/Documents/David.Claude/mods/so-viec" }`, rồi mở phiên mới.
Kiểm tra: `claude plugin validate mods/so-viec`, `claude plugin test mods/so-viec`.
