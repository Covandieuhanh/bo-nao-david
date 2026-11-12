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

**Công tắc bot chính** (12/11/2026 tối David chốt quay về bot Sổ nhớ; `bot-chinh` = `so-nho`, Hermes tắt, bật lại: chuyển plist từ `~/.hermes/tat-tam/` về `~/Library/LaunchAgents/`, `hermes gateway start`, `hermes cron resume e13813810422`, ghi `hermes`. Trước đó sáng 12/11 gom về Hermes): `~/Documents/2-ca-nhan/so-nho/.trang-thai/bot-chinh` ghi `hermes` thì `bao-cao.sh` (nên cả duyệt từ xa, cổng duyệt, nhắc giờ, cảnh báo) gửi qua bot Hermes (token và chat lấy ở `~/.hermes/.env`, chỉ `sendMessage` nên không giành kết nối của Hermes); `duyet-tu-xa.py` không gõ `[CHO-DUYET]` vào phiên bot; `canh-bot.sh` tắt và không giữ phiên bot cũ, bỏ tóm tắt sáng và nhắc có thẻ máy (lịch Hermes lo), vẫn nhắc giờ, sao lưu, đóng phiên việc. Xoá file = về bot cũ. Thử không bật công tắc: `BOT_CHINH=hermes bash bao-cao.sh --chi-gui "…"`. Hermes làm sổ nhớ theo `luat-bot.md` qua bảng đổi trong [hermes/giao-cho-hermes.md](../../hermes/giao-cho-hermes.md) mục 7.

**Tiết kiệm token Hermes** (12/11, David chốt; ngày đầu Hermes tốn ~4 lần bot cũ mỗi tin: 1,77 triệu so với 0,43 triệu token, ngữ cảnh ~220K/lượt gọi). Sửa `~/.hermes/config.yaml` (bản cũ `config.yaml.bak-2026-11-12`), giữ Opus: `compression.threshold_tokens: 40000`, `tail_mode: lean`, `protect_last_n: 6`, `proactive_prune_tokens: 20000` (`min_result_chars: 2000`); `session_reset` both, nghỉ 30 phút hoặc 4h sáng thì mở phiên mới; `tool_output.max_bytes: 12000`, `max_lines: 400`. `~/.hermes/SOUL.md` thêm mục "Tiết kiệm token": tìm trước, đọc đúng đoạn, lọc kết quả lệnh, việc nặng giao Claude Code. Đo lại: `sessions` trong `~/.hermes/state.db` (input/cache_read/cache_write/output, estimated_cost_usd).

**Điều khiển từ xa:** bot là trạm điều khiển (Opus từ 11/11, vì Haiku giao nhầm đường; thiếu quyền thì luôn tự giao việc, không bảo David bật quyền). Ghi nhớ, câu hỏi nhanh thì tự làm; việc đụng tới file thì chạy `giao-viec.sh`: mở phiên Claude Code thật (Opus, chế độ auto, thư mục bộ não) ở chế độ **Remote Control** (`--remote-control="Telegram #N · …"`) trong screen `viec-N`, nên phiên hiện như khung chat bình thường trong app Claude trên điện thoại và claude.ai/code, David xem và gõ tiếp được. Ghi `viec-giao.md`. Phiên báo `bao-cao.sh "#N ✅/❓ …"` (tự ghi trạng thái vào `viec-giao.md`); David nhắn qua bot → `--tiep N` gõ thẳng vào phiên (không bấm Esc vì Esc ngắt việc; phiên bận thì Claude xếp hàng tin), phiên đã đóng thì mở lại bằng `--resume`. Phiên nghỉ quá 12 giờ thì canh-bot đóng cho nhẹ máy. Phiên việc bỏ mọi biến `CLAUDE*` và `TELEGRAM_STATE_DIR`. Thử 11/11: giao, gõ tiếp, mở lại phiên đã đóng đều đạt. (Đường `claude://code/new` của app chỉ mở khung trống chờ bấm gửi, không tự chạy được.)

**Cài trên máy mới:** cài Bun (`curl -fsSL https://bun.sh/install | bash`), `claude plugin install telegram@claude-plugins-official --scope user`, David tự ghi `TELEGRAM_BOT_TOKEN=...` vào `~/.claude/channels/so-nho/.env` (chmod 600), cấp **Toàn quyền truy cập ổ đĩa** cho `/usr/bin/screen`, rồi `bash scripts/so-nho/cai-dat.sh`. Nhắn bot lấy mã ghép cặp, thêm vào `allowFrom` trong `access.json`, đặt `dmPolicy` = `allowlist`.

**Vì sao làm vậy (bài học 11/11/2026):**
- Token để ở `channels/so-nho/` (đặt `TELEGRAM_STATE_DIR`), không ở `channels/telegram/`: plugin cho phiên mở sau tắt bot của phiên trước, nên mọi phiên Claude khác không được thấy token.
- launchd chạy qua `screen` vì macOS chặn tiến trình nền đọc Documents; chỉ cấp quyền cho `screen`.
- Mod cấp người dùng (collision-guard, so-viec, goal-meter, savvy-progress) làm kẹt lệnh trong phiên bot, nên tắt riêng ở `settings.json`.
- Kết nối Telegram đôi khi hỏng lúc mở phiên mà không báo (`/mcp` ghi failed, không có tiến trình `bun server.ts`): canh-bot.sh thấy vậy sau 2 phút thì mở lại phiên.
- `MCP_TIMEOUT=120000`: lần đầu Bun cài thư viện lâu hơn 30 giây.
- `ProcessType` = `Interactive` trong plist: không có thì launchd hạ ưu tiên tiến trình nền, mỗi lần đọc/sửa file chậm 6–18 giây, một tin mất ~2 phút. `ENABLE_TOOL_SEARCH=false` nạp sẵn công cụ, bớt một vòng. `ackReaction` 👀 báo đã nhận tin ngay.
- Chế độ `dontAsk`: không có ai bấm duyệt, việc ngoài quyền tự bị từ chối thay vì treo. Model Opus (đổi từ Haiku 11/11 theo lời David: cần được việc hơn nhanh), tắt kết nối claude.ai và bộ nhớ tự động trong phiên bot. Bot không dùng Bash (lệnh shell treo hơn 1 phút trong phiên nền), lấy giờ từ `ts` của tin; nhắc đúng giờ và nhắc lặp ("- mỗi ngày / mỗi thứ 2, thứ 5 / mỗi ngày 15 HH:MM · …", tính bằng `nhac-lap.py`; dòng kết bằng `+ việc chưa xong` thì tin kèm danh sách việc `[ ]` của `viec-can-lam.md`; nội dung bắt đầu bằng thẻ máy như `[HOI-THOI-QUEN]` thì gõ vào phiên bot để bot đọc nhật ký hôm nay, chỉ hỏi thói quen chưa báo, khung 20:30 kèm lời khuyên cafe/thuốc lá; bot chưa sẵn sàng thì gửi thẳng chữ cố định) do canh-bot.sh đọc `nhac-viec.md`, không dùng CronCreate (mất khi phiên mở lại).

**Toàn quyền + cổng duyệt** (David chốt 11/11/2026, sửa 12/11: "đa phần tôi đều đồng ý các đề xuất, không cần hỏi, tôi chỉ quan tâm kết quả"): phiên việc giao qua Telegram chạy `--permission-mode bypassPermissions` (quyền như David ngồi máy) với `TELEGRAM_VIEC=1`. Hook `PreToolUse` [cong-duyet.py](cong-duyet.py) chỉ bật khi có biến đó, hai mức: **tự chạy + ghi sổ** `~/Documents/2-ca-nhan/so-nho/.trang-thai/tu-duyet.log` (xoá file, cài/gỡ phần mềm, sửa cấu hình máy hoặc Claude, sudo, thao tác GitHub thường), phiên kể lại trong tin báo cáo cuối; **vẫn hỏi** David qua Telegram (dùng chung `hoi_david` trong duyet-tu-xa.py) chỉ khi đăng/gửi ra ngoài, bấm/điền trên web (luật 4), tốn tiền, đẩy đè GitHub hoặc xoá repo (luật 6), xoá ổ đĩa: "đồng ý" thì chạy, "không" hoặc 30 phút thì chặn. Mẫu có dấu `!` trong lý do là mức hỏi. Thử 11/11: chặn `rm`, hỏi, "đồng ý" tới lúc xoá 10 giây. Lần đầu máy chạy bypass phải tự bấm "Yes, I accept" (`claude --permission-mode bypassPermissions` trong Terminal). Phiên mới trong app tự bật Remote Control (cài đặt app `connect_new_sessions_to_remote_control`).

**Hộp thư phiên** ([hop-thu-phien.py](hop-thu-phien.py), hook `PostToolUse` + `Stop` cho mọi phiên, cài bằng `scripts/cai-hook.py`): lời David qua Telegram cho một phiên **anh tự mở** (app Claude, terminal). Bot chạy `hop-thu-phien.py gui "<từ khoá phiên>" "<lời>"`: tìm phiên đang mở theo tên (tiến trình Claude → `CLAUDE_CODE_HOST_SESSION_ID` → dữ liệu phiên của app → `cliSessionId`), bỏ thư vào `.trang-thai/hop-phien/<mã phiên>/`. Hook của phiên đó: sau mỗi bước (PostToolUse) thêm lời vào ngữ cảnh; khi xong lượt (Stop) chặn dừng để làm tiếp theo lời. Phiên đang nghỉ hẳn thì chưa nhận: bot báo David mở phiên trên app/điện thoại. Báo David "📨 Phiên Claude đã nhận lời anh". Thử 11/11 trên phiên CLI: đạt. Lý do: không có đường chính thức để chương trình ngoài gõ vào phiên của app Claude.

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

**Học từ Hermes** (12/11): tin thoại → `nghe-thoai.sh` (ffmpeg + whisper-cli, mô hình `~/whisper-models/ggml-large-v3-turbo.bin`, ~5 giây, 0 token) · bot nghỉ 30 phút thì canh-bot gõ `/clear` (mục 7, nhớ dấu ở `.trang-thai/da-gon`) · `scripts/tim-phien.py` tìm lại cuộc trò chuyện cũ · `[TU-HOC]` tối chủ nhật 20:00 trong `nhac-viec.md` → bot giao phiên chạy skill `tu-hoc`.
