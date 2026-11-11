# Bot Sổ nhớ (Telegram)

David nhắn Telegram những gì nhớ, biết, cần làm. Phiên Claude Code trên Mac (gói của tài khoản đang đăng nhập) phân loại và ghi vào file mãi mãi, trả lời một dòng, 7h sáng gửi tóm tắt. Không dùng API key, không chạy trên cloud.

| Thứ | Ở đâu |
|---|---|
| Luật bot (chép thành `CLAUDE.md` của thư mục dữ liệu) | [luat-bot.md](luat-bot.md) |
| Quyền + tắt mod cho phiên bot | [settings.json](settings.json) |
| Canh bot (giữ thức, tự mở lại, làm mới 4h, tóm tắt 7h, sao lưu 3h) | [canh-bot.sh](canh-bot.sh) |
| Báo cáo lên Telegram (mọi phiên Claude, cuối việc) | [bao-cao.sh](bao-cao.sh) |
| Giao việc cho phiên Claude nền / làm tiếp / dừng | [giao-viec.sh](giao-viec.sh) (`"<yêu cầu>"`, `--tiep N "<trả lời>"`, `--dung N`) |
| Liệt kê việc đang có trên Mac | [viec-dang-chay.sh](viec-dang-chay.sh): tiến trình Claude đang sống → biến `CLAUDE_CODE_HOST_SESSION_ID` → dữ liệu phiên của app (`~/Library/Application Support/Claude/claude-code-sessions/*/*/local_*.json`: tên, `postTurnSummary`) + tiến trình con (ffmpeg, render, python) + đoạn Claude viết cuối trong transcript. Không dùng mod Sổ việc để biết "đang chạy": lệnh dài (render) không có lượt nói nên mod ghi là nghỉ |
| Cài đặt (tạo thư mục, đăng ký launchd `com.david.so-nho`) | [cai-dat.sh](cai-dat.sh) |
| Dữ liệu (không lên GitHub) | `~/Documents/2-ca-nhan/so-nho/`, sao lưu Drive `Sao-luu-mac/So-nho/` |
| Token + danh sách người được nhắn (không lên GitHub) | `~/.claude/channels/so-nho/` |

**Điều khiển từ xa:** bot là trạm điều khiển (Haiku, nhanh). Ghi nhớ, câu hỏi nhanh thì tự làm; việc đụng tới file thì chạy `giao-viec.sh`: mở phiên Claude Code thật (Opus, chế độ auto, thư mục bộ não) ở chế độ **Remote Control** (`--remote-control="Telegram #N · …"`) trong screen `viec-N`, nên phiên hiện như khung chat bình thường trong app Claude trên điện thoại và claude.ai/code, David xem và gõ tiếp được. Ghi `viec-giao.md`. Phiên báo `bao-cao.sh "#N ✅/❓ …"` (tự ghi trạng thái vào `viec-giao.md`); David nhắn qua bot → `--tiep N` gõ thẳng vào phiên (không bấm Esc vì Esc ngắt việc; phiên bận thì Claude xếp hàng tin), phiên đã đóng thì mở lại bằng `--resume`. Phiên nghỉ quá 12 giờ thì canh-bot đóng cho nhẹ máy. Phiên việc bỏ mọi biến `CLAUDE*` và `TELEGRAM_STATE_DIR`. Thử 11/11: giao, gõ tiếp, mở lại phiên đã đóng đều đạt. (Đường `claude://code/new` của app chỉ mở khung trống chờ bấm gửi, không tự chạy được.)

**Duyệt từ xa** ([duyet-tu-xa.py](duyet-tu-xa.py), hook `PermissionRequest` cho mọi phiên, cài bằng `scripts/cai-hook.py`): David vắng (Mac không có thao tác ≥2 phút, hoặc nhắn bot "tôi đi vắng") thì yêu cầu duyệt và câu hỏi lên Telegram **bằng tiếng Việt dễ hiểu**: xin phép thì Haiku (`claude -p`, bỏ biến môi trường `CLAUDE*` để không bị coi là phiên lồng) viết 3 dòng Việc muốn làm · Để làm gì · Rủi ro từ lời Claude vừa nói trong phiên; câu hỏi thì hiện đủ câu, lựa chọn và mô tả. David trả lời tự nhiên ("đồng ý", "không vì…", "2"), mã chỉ cần khi nhiều yêu cầu cùng lúc. Hook gõ `[CHO-DUYET]` vào phiên bot để bot biết; bot ghi `.trang-thai/duyet/MÃ.tra`, hook trả quyết định cho phiên. 30 phút không trả lời → hộp thoại về màn hình Mac. Thử 11/11 bằng phiên CLI: duyệt Bash, trả lời câu hỏi, duyệt Write đạt; "đồng ý" tới lúc lệnh chạy 8 giây.

**Canh 24/7** (`canh-bot.sh`, mỗi phút; thử 11/11: tắt máy chủ Telegram → Claude tự bật lại tức thì; tắt phiên → mở lại sau 50 giây):

| Hỏng | Tự sửa |
|---|---|
| Phiên bot chết, thừa phiên | Mở lại đúng một phiên |
| Máy chủ Telegram chết / Claude bỏ qua bước bật lúc mở phiên / bị giành (409) | Không thấy `bun server.ts` sau 40 giây → gõ `/mcp reconnect plugin:telegram:telegram` (tối đa 3 lần), không được thì mở lại phiên |
| Còn máy chủ nhưng không giữ kết nối Telegram (sau khi Mac thức dậy, đổi Wi-Fi) | Có mạng mà mất kết nối >3 phút → mở lại; không có mạng >30 phút → báo David |
| Phiên treo (đang làm >10 phút) / hộp thoại chặn | Bấm Esc; >15 phút → mở lại |
| Hết hạn mức gói, chưa đăng nhập / hết hạn đăng nhập | Báo David (3 giờ / 6 giờ một lần) |
| Mở lại >4 lần trong 30 phút | Báo David cần xem |
| Đổi tài khoản Claude, ngữ cảnh đầy | Mở lại khi đổi; làm mới 4h sáng |

- Tin David gửi lúc bot hỏng **không mất**: Telegram giữ tới 24 giờ, bot nối lại thì nhận.
- Nhắc đúng giờ và cảnh báo gửi thẳng qua Telegram (`bao-cao.sh --chi-gui`), không cần Claude chạy. Tóm tắt sáng chỉ đánh dấu khi gửi được, thử lại tới 12h.
- Nhắc chỉ gửi mục tới giờ trong 60 phút qua, mỗi giờ hẹn một lần (bot sửa chữ dòng cũ không gửi lại), bỏ dòng `· (đã …)`. Giờ theo múi của Mac, canh-bot ghi `.trang-thai/mui-gio.md` (CLAUDE.md của bot nhập file này); đổi múi thì mở lại bot.
- Gọi phiên bot bằng mã đủ (`12345.so-nho`): tên `so-nho` là đầu của `so-nho-canh` nên `screen -S so-nho` bị nhầm.
- Nhận máy chủ Telegram bằng `pgrep -fx ".*/bun server\.ts"` (khớp trọn): `pgrep -f` khớp cả lệnh khác có chữ đó và báo nhầm.
- PATH có `/usr/sbin` (lsof, taskpolicy). Không chạy `claude mcp list` với `TELEGRAM_STATE_DIR` của bot: nó giành kết nối.
- Không tự sửa được: Mac gập máy hoặc rút điện (ngủ), Mac khởi động lại mà chưa đăng nhập macOS.
- Sức khoẻ: `bash scripts/so-nho/viec-dang-chay.sh` (mục "Sức khoẻ bot"), hoặc hỏi bot "bot có ổn không".

Xem phiên bot: `screen -r so-nho` (thoát: Ctrl-A rồi D). Nhật ký canh: `~/Documents/2-ca-nhan/so-nho/.trang-thai/canh-bot.log`.
