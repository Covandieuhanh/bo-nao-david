# Bot Sổ nhớ (Telegram)

David nhắn Telegram những gì nhớ, biết, cần làm. Phiên Claude Code trên Mac (gói của tài khoản đang đăng nhập) phân loại và ghi vào file mãi mãi, trả lời một dòng, 7h sáng gửi tóm tắt. Không dùng API key, không chạy trên cloud.

| Thứ | Ở đâu |
|---|---|
| Luật bot (chép thành `CLAUDE.md` của thư mục dữ liệu) | [luat-bot.md](luat-bot.md) |
| Quyền + tắt mod cho phiên bot | [settings.json](settings.json) |
| Canh bot (giữ thức, tự mở lại, làm mới 4h, tóm tắt 7h, sao lưu 3h) | [canh-bot.sh](canh-bot.sh) |
| Báo cáo lên Telegram (mọi phiên Claude, cuối việc) | [bao-cao.sh](bao-cao.sh) |
| Giao việc cho phiên Claude nền / làm tiếp / dừng | [giao-viec.sh](giao-viec.sh) (`"<yêu cầu>"`, `--tiep N "<trả lời>"`, `--dung N`) |
| Liệt kê việc đang có trên Mac | [viec-dang-chay.sh](viec-dang-chay.sh) (đọc dữ liệu mod Sổ việc + phiên `viec-N`) |
| Cài đặt (tạo thư mục, đăng ký launchd `com.david.so-nho`) | [cai-dat.sh](cai-dat.sh) |
| Dữ liệu (không lên GitHub) | `~/Documents/2-ca-nhan/so-nho/`, sao lưu Drive `Sao-luu-mac/So-nho/` |
| Token + danh sách người được nhắn (không lên GitHub) | `~/.claude/channels/so-nho/` |

**Điều khiển từ xa:** bot là lễ tân (Haiku, nhanh). Ghi nhớ thì tự ghi; ra việc cho Claude thì chạy `giao-viec.sh`: mở phiên `claude -p` (Opus, chế độ auto, thư mục bộ não) trong screen `viec-N`, ghi `viec-giao.md`, log ở `.trang-thai/viec/N.log`. Phiên đó xong hoặc cần quyết thì `bao-cao.sh "#N …"`; David trả lời → bot `--tiep N` mở lại đúng phiên (`--resume`). Phiên việc bỏ `TELEGRAM_STATE_DIR` để không giành bot.

**Cài trên máy mới:** cài Bun (`curl -fsSL https://bun.sh/install | bash`), `claude plugin install telegram@claude-plugins-official --scope user`, David tự ghi `TELEGRAM_BOT_TOKEN=...` vào `~/.claude/channels/so-nho/.env` (chmod 600), cấp **Toàn quyền truy cập ổ đĩa** cho `/usr/bin/screen`, rồi `bash scripts/so-nho/cai-dat.sh`. Nhắn bot lấy mã ghép cặp, thêm vào `allowFrom` trong `access.json`, đặt `dmPolicy` = `allowlist`.

**Vì sao làm vậy (bài học 11/11/2026):**
- Token để ở `channels/so-nho/` (đặt `TELEGRAM_STATE_DIR`), không ở `channels/telegram/`: plugin cho phiên mở sau tắt bot của phiên trước, nên mọi phiên Claude khác không được thấy token.
- launchd chạy qua `screen` vì macOS chặn tiến trình nền đọc Documents; chỉ cấp quyền cho `screen`.
- Mod cấp người dùng (collision-guard, so-viec, goal-meter, savvy-progress) làm kẹt lệnh trong phiên bot, nên tắt riêng ở `settings.json`.
- `MCP_TIMEOUT=120000`: lần đầu Bun cài thư viện lâu hơn 30 giây.
- `ProcessType` = `Interactive` trong plist: không có thì launchd hạ ưu tiên tiến trình nền, mỗi lần đọc/sửa file chậm 6–18 giây, một tin mất ~2 phút. `ENABLE_TOOL_SEARCH=false` nạp sẵn công cụ, bớt một vòng. `ackReaction` 👀 báo đã nhận tin ngay.
- Chế độ `dontAsk`: không có ai bấm duyệt, việc ngoài quyền tự bị từ chối thay vì treo. Model Haiku cho nhanh nhất (đo 11/11: một lượt đọc 3 file + sửa 1 file mất 6 giây), tắt kết nối claude.ai và bộ nhớ tự động trong phiên bot. Bot không dùng Bash (lệnh shell treo hơn 1 phút trong phiên nền), lấy giờ từ `ts` của tin; nhắc đúng giờ do canh-bot.sh đọc `nhac-viec.md`, không dùng CronCreate (mất khi phiên mở lại).

Xem phiên bot: `screen -r so-nho` (thoát: Ctrl-A rồi D). Nhật ký canh: `~/Documents/2-ca-nhan/so-nho/.trang-thai/canh-bot.log`.
