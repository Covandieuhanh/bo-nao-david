# Sổ việc (mod của Claude Code)

Bảng cạnh khung chat, chỉ 3 phần, tự chạy ở mọi phiên Claude Code trên máy:

- **🎬 Video đang làm** (mọi khung đang làm video, cả phiên mở trước khi cài mod): thời gian và % tuần so với trung bình một video, có thanh.
- **Tuần này:** % giới hạn 7 ngày của tài khoản đã dùng (như trang usage), còn đủ khoảng bao nhiêu video.
- **TB 1 video:** trung bình một video mất bao nhiêu phút và tốn bao nhiêu % token tuần.

**Video** gộp mọi skill video: `video-style-edit`, `podcast-style-edit`, `cat-highlight-video`, `dang-da-kenh`, `hoc-video-mau`. **Một video = mọi việc video trong cùng một phiên** (dựng, cắt highlight, đăng). Thời gian là lúc Claude chạy.
**% tuần** là ước tính: tổng token mọi phiên từ đầu cửa sổ 7 ngày chia % đã dùng ra "1% ≈ bao nhiêu token", rồi đổi token mỗi video ra %.
Dòng trạng thái: `Video 24p/40p · 3%/8% tuần · tuần 62%`. `/bao-cao` in bản chữ, `/so-viec` mở lại bảng.

Mod vẫn ghi ngầm mọi việc (loại việc theo skill, việc khác do model nhỏ gán nhãn), chỉ không hiện.

**Dữ liệu** (trên máy, không lên GitHub): `~/.claude/so-viec/phien/<phiên>.json` mỗi phiên tự ghi sổ của mình;
`~/.claude/so-viec/nhap/<phiên>.json` phiên cũ nhập ngược bằng `python3 -I mods/so-viec/scripts/nhap-lich-su.py`
(chạy lại bao nhiêu lần cũng được; phiên cũ: bước im quá 5 phút trong một lượt coi là chờ David, không tính).

**Đang chạy cũng hiện:** phiên mở trước khi cài mod vẫn hiện trên bảng ("chưa có mod"): mod đọc đuôi lịch sử phiên đó đang ghi (thời gian lượt, token, skill gần nhất).
**Token trực tiếp:** cộng sau mỗi lần gọi model, nên lượt dài (render) thanh token cũng chạy.

**Cài:** `bash scripts/install.sh` (hoặc `claude plugin marketplace add <repo>` rồi `claude plugin install so-viec@david-claude --scope user`), mở phiên mới. Xem [mods/README.md](../README.md).
Kiểm tra: `claude plugin validate mods/so-viec`, `claude plugin test mods/so-viec`.
