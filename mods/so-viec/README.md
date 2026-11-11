# Sổ việc (mod của Claude Code)

Bảng cạnh khung chat, chỉ 3 phần, chữ viết đầy đủ, tự chạy ở mọi khung Claude Code trên máy:

- **🎬 Video đang làm** (mọi khung đang làm video, cả khung mở trước khi cài mod): thời gian và phần trăm hạn mức tuần đã tốn, mỗi thứ một thanh so với trung bình một video.
- **Hạn mức tuần này:** từng tài khoản Claude đã đăng nhập trên máy một dòng có thanh (đã dùng bao nhiêu phần trăm, ngày làm mới), và gộp mọi tài khoản còn đủ khoảng bao nhiêu video.
- **Trung bình một video:** mất bao nhiêu phút, tốn bao nhiêu phần trăm hạn mức tuần, **gộp mọi tài khoản**.

**Video** gộp mọi skill video: `video-style-edit`, `podcast-style-edit`, `cat-highlight-video`, `dang-da-kenh`, `hoc-video-mau`. **Một video = mọi việc video trong cùng một khung chat** (dựng, cắt highlight, đăng bài), chỉ tính khi **skill video được gọi** (model nhỏ không gán nhãn video) và làm từ 3 phút trở lên. Bảng hiện **mọi khung đang làm video** trên máy, ghi tên khung. Thời gian là lúc Claude chạy.

**Nhiều tài khoản:** mod gắn với máy nên đổi tài khoản vẫn chạy. Mỗi tài khoản có sổ hạn mức riêng (`~/.claude/so-viec/tai-khoan/<mã>.json`, ghi khi tài khoản đó đang đăng nhập): phần trăm đã dùng, ngày làm mới, và **1% hạn mức tuần ≈ bao nhiêu token** (tổng token tài khoản đó dùng từ đầu tuần chia phần trăm đã dùng). Mỗi lượt ghi kèm 8 ký tự đầu mã tài khoản; tên hiện trên bảng là phần trước @ của email. Mỗi video đổi ra phần trăm theo đúng tài khoản đã làm nó, rồi lấy trung bình. Tài khoản chưa đo được thì dùng mức trung bình của các tài khoản khác. Đây là ước tính.

`/bao-cao` in bản chữ vào khung chat, `/so-viec` mở lại bảng.

Mod vẫn ghi ngầm mọi việc (loại việc theo skill, việc khác do model nhỏ gán nhãn), chỉ không hiện.

**Dữ liệu** (trên máy, không lên GitHub): `~/.claude/so-viec/phien/<phiên>.json` mỗi phiên tự ghi sổ của mình;
`~/.claude/so-viec/nhap/<phiên>.json` phiên cũ nhập ngược bằng `python3 -I mods/so-viec/scripts/nhap-lich-su.py`
(chạy lại bao nhiêu lần cũng được; phiên cũ: bước im quá 5 phút trong một lượt coi là chờ David, không tính).

**Đang chạy cũng hiện:** phiên mở trước khi cài mod vẫn hiện trên bảng ("chưa có mod"): mod đọc đuôi lịch sử phiên đó đang ghi (thời gian lượt, token, skill gần nhất).
**Token trực tiếp:** cộng sau mỗi lần gọi model, nên lượt dài (render) thanh token cũng chạy.

**Cài:** `bash scripts/install.sh` (hoặc `claude plugin marketplace add <repo>` rồi `claude plugin install so-viec@david-claude --scope user`), mở phiên mới. Xem [mods/README.md](../README.md).
Kiểm tra: `claude plugin validate mods/so-viec`, `claude plugin test mods/so-viec`.
