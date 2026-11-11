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

**Điều khiển từ xa:** bot là lễ tân (Haiku, nhanh). Ghi nhớ thì tự ghi; ra việc cho Claude thì chạy `giao-viec.sh`: mở phiên `claude -p` (Opus, chế độ auto, thư mục bộ não) trong screen `viec-N`, ghi `viec-giao.md`, log ở `.trang-thai/viec/N.log`. Phiên đó xong hoặc cần quyết thì `bao-cao.sh "#N …"`; David trả lời → bot `--tiep N` mở lại đúng phiên (`--resume`). Phiên việc bỏ `TELEGRAM_STATE_DIR` để không giành bot.

**Cài trên máy mới:** cài Bun (`curl -fsSL https://bun.sh/install | bash`), `claude plugin install telegram@claude-plugins-official --scope user`, David tự ghi `TELEGRAM_BOT_TOKEN=...` vào `~/.claude/channels/so-nho/.env` (chmod 600), cấp **Toàn quyền truy cập ổ đĩa** cho `/usr/bin/screen`, rồi `bash scripts/so-nho/cai-dat.sh`. Nhắn bot lấy mã ghép cặp, thêm vào `allowFrom` trong `access.json`, đặt `dmPolicy` = `allowlist`.

**Vì sao làm vậy (bài học 11/11/2026):**
- Token để ở `channels/so-nho/` (đặt `TELEGRAM_STATE_DIR`), không ở `channels/telegram/`: plugin cho phiên mở sau tắt bot của phiên trước, nên mọi phiên Claude khác không được thấy token.
- launchd chạy qua `screen` vì macOS chặn tiến trình nền đọc Documents; chỉ cấp quyền cho `screen`.
- Mod cấp người dùng (collision-guard, so-viec, goal-meter, savvy-progress) làm kẹt lệnh trong phiên bot, nên tắt riêng ở `settings.json`.
- Kết nối Telegram đôi khi hỏng lúc mở phiên mà không báo (`/mcp` ghi failed, không có tiến trình `bun server.ts`): canh-bot.sh thấy vậy sau 2 phút thì mở lại phiên.
- `MCP_TIMEOUT=120000`: lần đầu Bun cài thư viện lâu hơn 30 giây.
- `ProcessType` = `Interactive` trong plist: không có thì launchd hạ ưu tiên tiến trình nền, mỗi lần đọc/sửa file chậm 6–18 giây, một tin mất ~2 phút. `ENABLE_TOOL_SEARCH=false` nạp sẵn công cụ, bớt một vòng. `ackReaction` 👀 báo đã nhận tin ngay.
- Chế độ `dontAsk`: không có ai bấm duyệt, việc ngoài quyền tự bị từ chối thay vì treo. Model Haiku cho nhanh nhất (đo 11/11: một lượt đọc 3 file + sửa 1 file mất 6 giây), tắt kết nối claude.ai và bộ nhớ tự động trong phiên bot. Bot không dùng Bash (lệnh shell treo hơn 1 phút trong phiên nền), lấy giờ từ `ts` của tin; nhắc đúng giờ do canh-bot.sh đọc `nhac-viec.md`, không dùng CronCreate (mất khi phiên mở lại).

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
