---
description: "Hướng dẫn cài đặt bộ não lên máy mới / nơi khác từ GitHub: Mac chính, Mac khác và Windows chỉ dựng video (khoá phiên bản, máy tự kiểm), lối tắt, bot, lịch, cái gì không lên GitHub."
---

# Dùng bộ não ở nơi khác

**Nguyên tắc:** GitHub chỉ giữ **bộ não**: hồ sơ, luật, bộ nhớ, skill, việc đang dở, và file mẫu (nằm trong skill, ví dụ `ky-nang/san-xuat-video/mau-chuan/`). Thành quả và thư mục sản phẩm (dự án video, bài đăng, tài liệu đã làm xong) ở lại máy nào giữ máy đó, cộng Drive. Máy mới chỉ cần não; thư mục làm việc tự tạo theo máy.

**Hai repo** (David chốt 20/11/2026):
- `bo-nao-david` (công khai): phần dùng chung, mọi máy kéo về.
- `bo-nao-david-mac` (riêng tư): phần chỉ Mac chính, gồm bot Telegram, lịch tự chạy, trang xem kết quả, app Mở Tài Liệu, lưu trữ cũ. Danh sách ở `tu-dong-hoa/phan-rieng-mac.txt`. Repo này nằm cùng thư mục với repo công khai, chỉ Mac chính có.

Các dòng dưới đây nhắc tới bot, lịch, trang xem là việc của Mac chính.

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

## 2. Claude Code trên máy Mac mới

```bash
brew install gh && gh auth login
```

```bash
gh repo clone Covandieuhanh/bo-nao-david ~/Documents/bo-nao-david
```

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/cai-dat-bo-nao.sh ~/Documents/bo-nao-david
```

`cai-dat-bo-nao.sh` thay `~/.claude/david.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và sổ danh mục bằng **lối tắt trỏ vào repo** (bản cũ sao lưu vào `~/.claude/backups/`), rồi cài hook đồng bộ 2 chiều: đầu phiên kéo từ GitHub về, cuối phiên đẩy lên. Từ đó máy và GitHub luôn là một bộ não. Khi cài **Mac chính** (không có `--chi-video`), script tự kéo luôn repo riêng tư `bo-nao-david-mac` vào cùng thư mục, nên `gh auth login` phải đăng nhập đúng tài khoản David. Sau đó cài bot, lịch, trang xem theo mục 5.

Bộ nhớ của Claude Code gắn theo thư mục dự án. Tham số cuối là thư mục bạn sẽ mở Claude Code (mặc định là chính repo). Muốn dùng ở thư mục khác thì chạy lại với thư mục đó.

**Mac chỉ dựng video** (không phải Mac chính): thêm `--chi-video` vào lệnh cài ở trên. Máy đó vẫn đồng bộ 2 chiều nhưng không cài bot Telegram, không cài lịch tự chạy. Rồi cài công cụ dựng đúng phiên bản và để máy tự kiểm:

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/may-khac/cai-cong-cu-video.sh
```

```bash
zsh ~/Documents/bo-nao-david/tu-dong-hoa/may-khac/kiem-may.sh
```

Đồng bộ tay bất cứ lúc nào:

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/dong-bo.sh
```

## 3. Máy Windows (chỉ dựng video)

Windows chạy skill qua **WSL2**, tức một Ubuntu chạy bên trong Windows. Nhờ vậy dùng nguyên script của Mac, chỉ giữ một bộ skill. Máy nào cũng đẩy được lên GitHub vì đăng nhập đúng tài khoản David. Bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ ở Mac chính. Chi tiết cái gì giống hệt, cái gì gần giống: [tu-dong-hoa/may-khac/README.md](tu-dong-hoa/may-khac/README.md).

**Một lần trên Windows** (David tự làm):

1. Mở PowerShell bằng quyền quản trị (chuột phải thì Run as administrator), chạy `wsl --install -d Ubuntu-24.04`, khởi động lại máy. Mở "Ubuntu" từ menu Start, đặt tên và mật khẩu cho Ubuntu.
2. Cài **Google Drive cho máy tính** (bản Windows), đăng nhập tài khoản của David. Drive hiện thành một ổ đĩa (thường là G:), Ubuntu đọc ở `/mnt/g/My Drive`.
   Ubuntu chỉ gắn ổ mới khi khởi động: cài Drive xong thì chạy `wsl --shutdown` trong PowerShell rồi mở lại Ubuntu, kiểm bằng `ls "/mnt/g/My Drive"`.
   Chưa có Drive thì vẫn dựng được, nhưng chưa giao được kết quả và chưa chạy được `kiem-may.sh`, nên **chưa tính là cài xong**.
   Muốn chạy `kiem-may.sh` khi chưa có Drive: tải thư mục `tu-lieu-goc/_bo-thu-may` về (ví dụ `gdown --folder <link>`) rồi chạy `BO_THU=<thư mục đó> zsh .../kiem-may.sh`.
   **Không dựng bằng bản repo clone phía Windows** (Git cho Windows biến liên kết thư viện hình thành file chữ): chỉ dùng bản trong Ubuntu `~/Documents/bo-nao-david`.

**Trong cửa sổ Ubuntu**, chạy lần lượt:

```bash
sudo apt update && sudo apt install -y git gh
```

```bash
gh auth login && gh auth setup-git
```

```bash
git config --global user.name "David Trần" && git config --global user.email "<email GitHub của David>"
```

```bash
gh repo clone Covandieuhanh/bo-nao-david ~/Documents/bo-nao-david
```

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/cai-dat-bo-nao.sh ~/Documents/bo-nao-david
```

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/may-khac/cai-cong-cu-video.sh
```

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
zsh ~/Documents/bo-nao-david/tu-dong-hoa/may-khac/kiem-may.sh
```

- `cai-dat-bo-nao.sh` thấy máy không phải Mac thì tự cài kiểu "chỉ dựng video".
- `cai-cong-cu-video.sh` cài đúng phiên bản Mac đang dùng: ffmpeg, whisper.cpp kèm mô hình 1,5 GB, Node, pyannote, công cụ dò mặt. Script hỏi mật khẩu Ubuntu một lần. Script cũng in các bước để David tự lấy mã Hugging Face cho phần tách người nói podcast (một lần).
- `kiem-may.sh` dựng thử 20 giây bằng đúng script của skill rồi so với bản chuẩn của Mac. Bộ thử nằm trên Drive `tu-lieu-goc/_bo-thu-may/`. Kết quả phải là **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**.

**Dùng hằng ngày:** mở Ubuntu, `cd ~/Documents/bo-nao-david && claude`, rồi làm như trên Mac: gửi video, gọi skill.
- Video gốc trên Drive đọc thẳng ở `/mnt/g/My Drive/...`.
- Dự án dựng nằm ở `~/Movies` của Ubuntu. Mở bằng Windows Explorer: gõ `explorer.exe ~/Movies` trong Ubuntu, hoặc vào `\\wsl$\Ubuntu-24.04\home\<tên>\Movies`.
- Thành phẩm lên Drive bằng `cho-dang.sh gui` / `luu-drive.sh` như trên Mac. Khác Mac ở một điểm: máy chép lên và so khớp, nhưng không tự xoá bản trên máy. Khi biểu tượng Drive báo tải xong, David xoá tay.
- Máy có card NVIDIA cài CUDA trong WSL thì Whisper chạy nhanh hơn nhiều (script tự dùng). Không có thì chạy bằng CPU: chậm hơn Mac nhưng ra cùng kết quả.

## 4. AI khác hoặc Claude bản web

- Có kết nối GitHub: cấp quyền cho repo `Covandieuhanh/bo-nao-david`, rồi dán câu mở đầu trong `README.md`.
- Không có kết nối GitHub: tải ZIP của repo, hoặc tải riêng `AGENTS.md`, `co-so-tri-thuc/david.md`, `bao-cao-trang-thai.md`, `ky-nang/thu-thap-yeu-cau/SKILL.md`.
- AI bản web không chạy được lệnh trên máy: làm được phần lọc, kế hoạch, viết bài; không dựng được video.

## 5. Những thứ repo không mang theo được

| Thứ cần có | Cách lấy lại |
|---|---|
| Công cụ dựng video, đúng phiên bản Mac | `bash tu-dong-hoa/may-khac/cai-cong-cu-video.sh` (ffmpeg, whisper.cpp, Node, Pillow, pyannote, dò mặt; bản khoá ở `tu-dong-hoa/may-khac/phien-ban.env`). Kiểm nhanh: `kiem-moi-truong.sh` của skill; so kết quả với Mac: `kiem-may.sh` |
| Mô hình Whisper (1,5 GB) | `cai-cong-cu-video.sh` tải về `~/whisper-models` và kiểm mã |
| `~/.cache/dung-video-theo-phong-cach` (dò mặt, môi trường Python) | `cai-cong-cu-video.sh` tạo lại; trên Mac, Vision tự dựng lại khi dùng lần đầu |
| Mô hình tách người nói pyannote (khoảng 31 MB) | Cần tài khoản Hugging Face. `cai-cong-cu-video.sh` in các bước David tự làm một lần (đồng ý điều khoản, dán mã đọc); chưa có thì podcast nhiều người đoán người nói theo giọng |
| Bot Telegram Sổ nhớ (chạy 24/7) | Cài plugin Telegram (cai-dat-bo-nao.sh đã cài), dán token bot vào `~/.claude/channels/so-tay/.env` (David giữ token, không lên GitHub), rồi `bash tu-dong-hoa/so-tay/cai-dat.sh`: chép luật + quyền bot, cài launchd `com.david.so-tay`. Nghe tin thoại dùng chung mô hình Whisper ở dòng trên |
| Bot Telegram Điều hành (chạy 24/7, sau bot Sổ nhớ) | Tạo bot ở @BotFather (David giữ token), rồi `bash tu-dong-hoa/dieu-hanh/cai-dat.sh "<token>"`: lưu token vào `~/.claude/channels/dieu-hanh/.env`, cài launchd `com.david.dieu-hanh`, chép luật mới cho Sổ nhớ. Không cần Claude chạy. Xem `tu-dong-hoa/dieu-hanh/README.md` |
| Bộ não công ty Veltrix (riêng, private) | `git clone https://github.com/Covandieuhanh/veltrix.git ~/Documents/bo-nao-veltrix`. Phiên lịch tự thêm thư mục này (`chay-lich.sh --add-dir`) để ghi nhật ký điều hành; đẩy bằng `bash ~/Documents/bo-nao-veltrix/dong-bo.sh` |
| Trang xem kết quả video + trang bài đăng + trang kiểm video trên Mac (`localhost:8765`, `/bai-dang`, `/mac`, tự bật khi mở máy) | `bash tu-dong-hoa/cai-trang-xem.sh`: cài launchd `com.david.xem-ket-qua` chạy `tu-dong-hoa/xem-ket-qua.py`; bài, ảnh đọc từ `~/Documents/1-nghe-nghiep/bai-dang/` (không lên GitHub) |
| Lịch tự chạy (tổng hợp tin 7:00, gom 23:00, đóng gói thứ 6 06:30) | Theo repo: `tu-dong-hoa/lich/lich-chay.md`. Tới giờ máy canh bot mở một phiên hiện trong app Claude (Remote Control, có Claude in Chrome), cài bot là có. Không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, gắn theo tài khoản). Lần đầu trên máy: chạy `claude --chrome` trong Terminal, bấm Enter ở màn giới thiệu Claude in Chrome rồi `/exit`. Zalo, Messenger, Telegram Web đăng nhập trong Chrome. Kho gom `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/` chỉ ở máy, sao lưu Drive cùng sổ nhớ |
| Tín hiệu tự học (`~/.claude/hoc-lien-tuc/`) | Có lời chat nên ở lại máy; máy mới tự ghi lại từ đầu (hook do cai-dat-bo-nao.sh cài) |
| `playwright-cli` | Cài qua npm toàn cục, kiểm tra bằng `playwright-cli --help` |
| Đăng nhập YouTube, Facebook, TikTok | David tự đăng nhập lại. Hồ sơ Chrome đăng bài ở `~/.cache/david-mxh-chrome` |
| Google Drive (`tu-lieu-goc`, `thanh-pham`) | Cài Google Drive cho máy tính, đăng nhập tài khoản của David |
| Trình duyệt và kết nối của Claude | Bật lại trong ứng dụng Claude |
| Video gốc, thành phẩm, kịch bản, bài đăng từng dự án | Ở Drive và `~/Movies` của máy làm, không nằm trong repo. Repo chỉ ghi trạng thái ở `bao-cao-trang-thai.md` và `du-an/danh-muc-noi-dung.md` |

## 6. Sau khi cài, kiểm tra nhanh

Mở Claude Code và nói: "Tôi là ai, và bạn phải làm gì trước khi tạo một file mới?" Câu trả lời đúng phải nói được David là nhà đào tạo cho người lần đầu dẫn người, và phải hỏi rồi chờ "ok".
