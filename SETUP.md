# Dùng bộ não ở nơi khác

**Nguyên tắc:** GitHub chỉ giữ **bộ não**: hồ sơ, luật, bộ nhớ, skill, việc đang dở, và file mẫu (nằm trong skill, ví dụ `skills/dung-video/mau-chuan/`). Thành quả và thư mục sản phẩm (dự án video, bài đăng, tài liệu đã làm xong) ở lại máy nào giữ máy đó, cộng Drive. Máy mới chỉ cần não; thư mục làm việc tự tạo theo máy.

## 1. Tài khoản Claude khác, cùng máy này

Trên Mac chính, skill, hồ sơ, luật và bộ nhớ trong `~/.claude` là lối tắt trỏ vào repo này; lịch sử chat thô nằm trong `~/.claude/projects`, dự án dựng nằm trong `~/Movies`. Đổi tài khoản trên cùng máy vẫn còn, không cần cài gì.

**Các bước sau khi đăng nhập tài khoản mới:**

1. Trong ứng dụng Claude, mở đúng thư mục `~/Documents/David.Claude` để Claude Code nhận bộ nhớ (bộ nhớ gắn theo đường dẫn thư mục).
2. Dán câu này vào phiên đầu tiên:

> Đọc ~/Documents/David.Claude/AGENTS.md rồi đọc tiếp theo đúng thứ tự trong đó. Xong thì tóm tắt 3 dòng: tôi là ai, bạn sẽ làm việc với tôi thế nào, việc đang dở là gì. Sau đó hỏi tôi các câu còn mở trong TRANG-THAI-HIEN-TAI.md.

3. Bật lại trong ứng dụng: trình duyệt Claude in Chrome nếu dùng, kết nối Claude Docs nếu cần viết tài liệu. Đăng nhập YouTube, Facebook, TikTok nằm ở hồ sơ Chrome trên máy, không gắn với tài khoản Claude.

**Không đi theo sang tài khoản mới, và đã sao lưu ở đâu (07/11/2026):**

| Thứ | Bản sao |
|---|---|
| Trang và tài liệu trên claude.ai | Toàn bộ ở Drive `Sao-luu-Claude-2026-11-07/tai-lieu-claude-ai` (không còn trong repo). Bản PDF đọc được nhưng không còn sửa trực tiếp như trên claude.ai |
| Lịch sử trò chuyện | Danh sách phiên trong ứng dụng không theo sang. Bản thô vẫn ở `~/.claude/projects` trên máy, không đưa lên mạng. Những gì cần cho việc tiếp theo đã ghi vào `TRANG-THAI-HIEN-TAI.md` và `nao/bo-nho/` |

**Phòng khi máy này hỏng:** repo này giữ não và skill; Drive `Video-xong` giữ thành phẩm; Drive `Sao-luu-Claude-2026-11-07/du-an-video` giữ âm thanh gốc và kịch bản từng dự án (bỏ `node_modules` và file render, dựng lại được). Giải nén vào `~/Movies`, chạy `npm install` trong `motion/`, rồi render lại. File `.env` của App notion, `~/Documents/mk.csv`, hồ sơ đăng nhập Chrome và lịch sử chat chỉ có trên máy này, cố ý không đưa lên mạng.

## 2. Claude Code trên máy mới (Mac)

```bash
brew install gh && gh auth login
```

```bash
gh repo clone Covandieuhanh/David.Claude ~/Documents/David.Claude
```

```bash
bash ~/Documents/David.Claude/scripts/install.sh ~/Documents/David.Claude
```

`install.sh` thay `~/.claude/David.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và sổ danh mục bằng **lối tắt trỏ vào repo** (bản cũ sao lưu vào `~/.claude/backups/`), rồi cài hook đồng bộ 2 chiều: đầu phiên kéo từ GitHub về, cuối phiên đẩy lên. Từ đó máy và GitHub luôn là một bộ não.

Bộ nhớ của Claude Code gắn theo thư mục dự án. Tham số cuối là thư mục bạn sẽ mở Claude Code (mặc định là chính repo). Muốn dùng ở thư mục khác thì chạy lại với thư mục đó.

Đồng bộ tay bất cứ lúc nào:

```bash
bash ~/Documents/David.Claude/scripts/sync.sh
```

## 3. AI khác hoặc Claude bản web

- Có kết nối GitHub: cấp quyền cho repo `Covandieuhanh/David.Claude`, rồi dán câu mở đầu trong `README.md`.
- Không có kết nối GitHub: tải ZIP của repo, hoặc tải riêng `AGENTS.md`, `nao/David.md`, `TRANG-THAI-HIEN-TAI.md`, `skills/hoi-chuyen-gia/SKILL.md`.
- AI bản web không chạy được lệnh trên máy: làm được phần lọc, kế hoạch, viết bài; không dựng được video.

## 4. Những thứ repo không mang theo được

| Thứ cần có | Cách lấy lại |
|---|---|
| Công cụ dựng video | Chạy `zsh ~/.claude/skills/dung-video/video-style-edit/scripts/check_env.sh`, nó in lệnh cài từng thứ còn thiếu (ffmpeg, whisper.cpp, Node, Pillow) |
| Mô hình Whisper (1,5 GB) | Lệnh tải do `check_env.sh` in ra, lưu ở `~/whisper-models` |
| `~/.cache/video-style-edit` (font, dò mặt, môi trường Python, 92 MB) | Các script dựng dùng thư mục này. Chép từ máy cũ cho chắc, hoặc để script báo thiếu rồi cài lại |
| `playwright-cli` | Cài qua npm toàn cục, kiểm tra bằng `playwright-cli --help` |
| Đăng nhập YouTube, Facebook, TikTok | David tự đăng nhập lại. Hồ sơ Chrome đăng bài ở `~/.cache/david-mxh-chrome` |
| Google Drive (`Video-goc`, `Video-xong`) | Cài Google Drive cho máy tính, đăng nhập tài khoản của David |
| Trình duyệt và kết nối của Claude | Bật lại trong ứng dụng Claude |
| Video gốc, thành phẩm, kịch bản, bài đăng từng dự án | Ở Drive và `~/Movies` của máy làm, không nằm trong repo. Repo chỉ ghi trạng thái ở `TRANG-THAI-HIEN-TAI.md` và `dang-lam/danh-muc.md` |

## 5. Sau khi cài, kiểm tra nhanh

Mở Claude Code và nói: "Tôi là ai, và bạn phải làm gì trước khi tạo một file mới?" Câu trả lời đúng phải nói được David là nhà đào tạo cho người lần đầu dẫn người, và phải hỏi rồi chờ "ok".
