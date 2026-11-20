---
description: "Hướng dẫn cài đặt bộ não lên máy mới / nơi khác từ GitHub: lệnh cài, lối tắt, bot, lịch, cái gì không lên GitHub."
---

# Dùng bộ não ở nơi khác

**Nguyên tắc:** GitHub chỉ giữ **bộ não**: hồ sơ, luật, bộ nhớ, skill, việc đang dở, và file mẫu (nằm trong skill, ví dụ `ky-nang/san-xuat-video/mau-chuan/`). Thành quả và thư mục sản phẩm (dự án video, bài đăng, tài liệu đã làm xong) ở lại máy nào giữ máy đó, cộng Drive. Máy mới chỉ cần não; thư mục làm việc tự tạo theo máy.

## 1. Tài khoản Claude khác, cùng máy này

Trên Mac chính, skill, hồ sơ, luật và bộ nhớ trong `~/.claude` là lối tắt trỏ vào repo này; lịch sử chat thô nằm trong `~/.claude/projects`, dự án dựng nằm trong `~/Movies`. Đổi tài khoản trên cùng máy vẫn còn, không cần cài gì. Lịch tự chạy, nhắc giờ, bot, hook đều là file và script trên máy (`tu-dong-hoa/lich/`, `tu-dong-hoa/so-tay/`), không gắn với tài khoản nào.

**Các bước sau khi đăng nhập tài khoản mới:**

1. Trong ứng dụng Claude, mở đúng thư mục `~/Documents/bo-nao-david` để Claude Code nhận bộ nhớ (bộ nhớ gắn theo đường dẫn thư mục).
2. Dán câu này vào phiên đầu tiên:

> Đọc ~/Documents/bo-nao-david/AGENTS.md rồi đọc tiếp theo đúng thứ tự trong đó. Xong thì tóm tắt 3 dòng: tôi là ai, bạn sẽ làm việc với tôi thế nào, việc đang dở là gì. Sau đó hỏi tôi các câu còn mở trong bao-cao-trang-thai.md.

3. Máy tự làm khi thấy app đổi tài khoản: mở Terminal chạy `claude auth login` (anh chọn đúng tài khoản mới, bấm cho phép; bot, giao việc, lịch gom/đóng gói dùng đăng nhập này) (lịch tự chạy dùng chính đăng nhập này, không phải cài lại). Kiểm tra: `bash tu-dong-hoa/kiem-tra-tai-khoan.sh`.
4. Bật lại trong ứng dụng: tiện ích Claude in Chrome đăng nhập đúng tài khoản mới (tổng hợp tin đọc Zalo, Messenger, Telegram qua đây), kết nối Claude Docs nếu cần viết tài liệu. Đăng nhập YouTube, Facebook, TikTok nằm ở hồ sơ Chrome trên máy, không gắn với tài khoản Claude.

**Không đi theo sang tài khoản mới, và đã sao lưu ở đâu (07/11/2026):**

| Thứ | Bản sao |
|---|---|
| Trang và tài liệu trên claude.ai | Toàn bộ ở Drive `sao-luu-claude-2026-11-07/tai-lieu-claude-ai` (không còn trong repo). Bản PDF đọc được nhưng không còn sửa trực tiếp như trên claude.ai |
| Lịch sử trò chuyện | Danh sách phiên trong ứng dụng không theo sang. Bản thô vẫn ở `~/.claude/projects` trên máy, không đưa lên mạng. Những gì cần cho việc tiếp theo đã ghi vào `bao-cao-trang-thai.md` và `co-so-tri-thuc/bo-nho/` |

**App xem, in, sửa tài liệu (Mở Tài Liệu):** `brew install --cask libreoffice` (bộ dàn trang cho Bản in và lưu Word) rồi `bash tu-dong-hoa/trinh-xem-tai-lieu/dung.sh` (xem `tu-dong-hoa/trinh-xem-tai-lieu/README.md`).

**Phòng khi máy này hỏng:** repo này giữ não và skill; Drive `thanh-pham` giữ thành phẩm; Drive `sao-luu-claude-2026-11-07/du-an-video` giữ âm thanh gốc và kịch bản từng dự án (bỏ `node_modules` và file render, dựng lại được). Giải nén vào `~/Movies`, chạy `npm install` trong `chuyen-dong/`, rồi render lại. File `.env` của App notion, `~/Documents/mk.csv`, hồ sơ đăng nhập Chrome và lịch sử chat chỉ có trên máy này, cố ý không đưa lên mạng.

## 2. Claude Code trên máy mới (Mac)

```bash
brew install gh && gh auth login
```

```bash
gh repo clone Covandieuhanh/bo-nao-david ~/Documents/bo-nao-david
```

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/cai-dat-bo-nao.sh ~/Documents/bo-nao-david
```

`cai-dat-bo-nao.sh` thay `~/.claude/david.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và sổ danh mục bằng **lối tắt trỏ vào repo** (bản cũ sao lưu vào `~/.claude/backups/`), rồi cài hook đồng bộ 2 chiều: đầu phiên kéo từ GitHub về, cuối phiên đẩy lên. Từ đó máy và GitHub luôn là một bộ não.

Bộ nhớ của Claude Code gắn theo thư mục dự án. Tham số cuối là thư mục bạn sẽ mở Claude Code (mặc định là chính repo). Muốn dùng ở thư mục khác thì chạy lại với thư mục đó.

Đồng bộ tay bất cứ lúc nào:

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/dong-bo.sh
```

## 3. AI khác hoặc Claude bản web

- Có kết nối GitHub: cấp quyền cho repo `Covandieuhanh/bo-nao-david`, rồi dán câu mở đầu trong `README.md`.
- Không có kết nối GitHub: tải ZIP của repo, hoặc tải riêng `AGENTS.md`, `co-so-tri-thuc/david.md`, `bao-cao-trang-thai.md`, `ky-nang/thu-thap-yeu-cau/SKILL.md`.
- AI bản web không chạy được lệnh trên máy: làm được phần lọc, kế hoạch, viết bài; không dựng được video.

## 4. Những thứ repo không mang theo được

| Thứ cần có | Cách lấy lại |
|---|---|
| Công cụ dựng video | Chạy `zsh ~/.claude/skills/san-xuat-video/dung-video-theo-phong-cach/scripts/kiem-moi-truong.sh`, nó in lệnh cài từng thứ còn thiếu (ffmpeg, whisper.cpp, Node, Pillow) |
| Mô hình Whisper (1,5 GB) | Lệnh tải do `kiem-moi-truong.sh` in ra, lưu ở `~/whisper-models` |
| `~/.cache/dung-video-theo-phong-cach` (font, dò mặt, môi trường Python, 92 MB) | Các script dựng dùng thư mục này. Chép từ máy cũ cho chắc, hoặc để script báo thiếu rồi cài lại |
| Bot Telegram Sổ nhớ (chạy 24/7) | Cài plugin Telegram (cai-dat-bo-nao.sh đã cài), dán token bot vào `~/.claude/channels/so-tay/.env` (David giữ token, không lên GitHub), rồi `bash tu-dong-hoa/so-tay/cai-dat.sh`: chép luật + quyền bot, cài launchd `com.david.so-tay`. Nghe tin thoại dùng chung mô hình Whisper ở dòng trên |
| Bộ não công ty Veltrix (riêng, private) | `git clone https://github.com/Covandieuhanh/veltrix.git ~/Documents/bo-nao-veltrix`. Phiên lịch tự thêm thư mục này (`chay-lich.sh --add-dir`) để ghi nhật ký điều hành; đẩy bằng `bash ~/Documents/bo-nao-veltrix/dong-bo.sh` |
| Trang xem kết quả video + trang bài đăng + trang kiểm video trên Mac (`localhost:8765`, `/bai-dang`, `/mac`, tự bật khi mở máy) | `bash tu-dong-hoa/cai-trang-xem.sh`: cài launchd `com.david.xem-ket-qua` chạy `tu-dong-hoa/xem-ket-qua.py`; bài, ảnh đọc từ `~/Documents/1-nghe-nghiep/bai-dang/` (không lên GitHub) |
| Lịch tự chạy (tổng hợp tin 7:00, gom 23:00, đóng gói thứ 6 06:30) | Theo repo: `tu-dong-hoa/lich/lich-chay.md`. Tới giờ máy canh bot mở một phiên hiện trong app Claude (Remote Control, có Claude in Chrome), cài bot là có. Không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, gắn theo tài khoản). Lần đầu trên máy: chạy `claude --chrome` trong Terminal, bấm Enter ở màn giới thiệu Claude in Chrome rồi `/exit`. Zalo, Messenger, Telegram Web đăng nhập trong Chrome. Kho gom `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/` chỉ ở máy, sao lưu Drive cùng sổ nhớ |
| Tín hiệu tự học (`~/.claude/hoc-lien-tuc/`) | Có lời chat nên ở lại máy; máy mới tự ghi lại từ đầu (hook do cai-dat-bo-nao.sh cài) |
| `playwright-cli` | Cài qua npm toàn cục, kiểm tra bằng `playwright-cli --help` |
| Đăng nhập YouTube, Facebook, TikTok | David tự đăng nhập lại. Hồ sơ Chrome đăng bài ở `~/.cache/david-mxh-chrome` |
| Google Drive (`tu-lieu-goc`, `thanh-pham`) | Cài Google Drive cho máy tính, đăng nhập tài khoản của David |
| Trình duyệt và kết nối của Claude | Bật lại trong ứng dụng Claude |
| Video gốc, thành phẩm, kịch bản, bài đăng từng dự án | Ở Drive và `~/Movies` của máy làm, không nằm trong repo. Repo chỉ ghi trạng thái ở `bao-cao-trang-thai.md` và `du-an/danh-muc-noi-dung.md` |

## 5. Sau khi cài, kiểm tra nhanh

Mở Claude Code và nói: "Tôi là ai, và bạn phải làm gì trước khi tạo một file mới?" Câu trả lời đúng phải nói được David là nhà đào tạo cho người lần đầu dẫn người, và phải hỏi rồi chờ "ok".
