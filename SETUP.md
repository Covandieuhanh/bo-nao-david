# Dùng bộ não ở nơi khác

## 1. Tài khoản Claude khác, cùng máy này

Skill và bộ nhớ nằm trong `~/.claude` nên đổi tài khoản vẫn còn. Không cần cài gì.

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

Bộ nhớ của Claude Code gắn theo thư mục dự án. Tham số cuối là thư mục bạn sẽ mở Claude Code. Muốn dùng ở thư mục khác thì chạy lại với thư mục đó.

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
| Video gốc và thành phẩm | Ở Drive và `~/Movies`, không nằm trong repo |
| Code App notion | Ở `~/Documents/App notion` trên Mac hiện tại, không nằm trong repo |

## 5. Sau khi cài, kiểm tra nhanh

Mở Claude Code và nói: "Tôi là ai, và bạn phải làm gì trước khi tạo một file mới?" Câu trả lời đúng phải nói được David là nhà đào tạo cho người lần đầu dẫn người, và phải hỏi rồi chờ "ok".
