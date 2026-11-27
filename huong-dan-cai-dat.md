---
description: "Hướng dẫn cài đặt bộ não lên thiết bị mới / nơi khác từ GitHub: Mac chính, Mac khác và Windows chỉ dựng video (khoá phiên bản, thiết bị tự kiểm tra), lối tắt, bot, lịch, những gì không đưa lên GitHub."
---

# Dùng bộ não ở nơi khác

**Nguyên tắc:** GitHub chỉ giữ **bộ não**: hồ sơ, luật, bộ nhớ, skill, việc làm chưa xong, và file mẫu (nằm trong skill, ví dụ `ky-nang/san-xuat-video/mau-chuan/`). Thành quả và thư mục sản phẩm (dự án video, bài đăng, tài liệu đã làm xong) ở lại thiết bị đang lưu chúng, cùng bản trên Drive. Thiết bị mới chỉ cần bộ não; thư mục làm việc được tạo tự động theo từng thiết bị.

**Hai repo** (David chốt 20/11/2026):
- `bo-nao-david` (công khai): phần dùng chung, mọi thiết bị pull về.
- `bo-nao-david-mac` (riêng tư): phần chỉ Mac chính, gồm bot Telegram, lịch tự chạy, trang xem kết quả, app Mở Tài Liệu, lưu trữ cũ. Danh sách ở `tu-dong-hoa/phan-rieng-mac.txt`. Repo này nằm cùng thư mục với repo công khai, chỉ Mac chính có.

Các dòng dưới đây nhắc tới bot, lịch, trang xem là việc của Mac chính.

## 1. Tài khoản Claude khác, cùng máy này

Trên Mac chính, skill, hồ sơ, luật và bộ nhớ trong `~/.claude` là lối tắt trỏ vào repo này; lịch sử chat thô nằm trong `~/.claude/projects`, dự án dựng nằm trong `~/Movies`. Khi đổi tài khoản trên cùng thiết bị, các phần này vẫn còn, không cần cài gì. Lịch tự chạy, nhắc giờ, bot, hook đều là file và script trên máy (`tu-dong-hoa/lich/`, `tu-dong-hoa/so-tay/`), không gắn với tài khoản nào.

**Các bước sau khi đăng nhập tài khoản mới:**

1. Trong ứng dụng Claude, mở đúng thư mục `~/Documents/bo-nao-david` để Claude Code nhận bộ nhớ (bộ nhớ gắn theo đường dẫn thư mục).
2. Dán câu này vào phiên đầu tiên:

> Đọc ~/Documents/bo-nao-david/AGENTS.md rồi đọc tiếp theo đúng thứ tự trong đó. Xong thì tóm tắt 3 dòng: tôi là ai, bạn sẽ làm việc với tôi thế nào, việc đang dở là gì. Sau đó hỏi tôi các câu còn mở trong bao-cao-trang-thai.md.

3. Thiết bị tự làm khi phát hiện app đổi tài khoản: mở Terminal chạy `claude auth login` (David chọn đúng tài khoản mới, bấm cho phép; bot, giao việc, lịch thu thập/đóng gói dùng đăng nhập này) (lịch tự chạy dùng chính đăng nhập này, không phải cài lại). Kiểm tra: `bash tu-dong-hoa/kiem-tra-tai-khoan.sh`.
4. Bật lại trong ứng dụng: tiện ích Claude in Chrome đăng nhập đúng tài khoản mới (tổng hợp tin đọc Zalo, Messenger, Telegram qua đây), kết nối Claude Docs nếu cần viết tài liệu. Đăng nhập YouTube, Facebook, TikTok nằm ở hồ sơ Chrome trên máy, không gắn với tài khoản Claude.

**Những gì không chuyển sang tài khoản mới, và đã sao lưu ở đâu (07/11/2026):**

| Hạng mục | Bản sao |
|---|---|
| Trang và tài liệu trên claude.ai | Toàn bộ ở Drive `sao-luu-claude-2026-11-07/tai-lieu-claude-ai` (không còn trong repo). Bản PDF đọc được nhưng không còn sửa trực tiếp như trên claude.ai |
| Lịch sử trò chuyện | Danh sách phiên trong ứng dụng không theo sang. Bản thô vẫn ở `~/.claude/projects` trên máy, không đưa lên mạng. Những gì cần cho việc tiếp theo đã ghi vào `bao-cao-trang-thai.md` và `co-so-tri-thuc/bo-nho/` |

**App xem, in, sửa tài liệu (Mở Tài Liệu):** `brew install --cask libreoffice` (bộ dàn trang cho Bản in và lưu Word) rồi `bash tu-dong-hoa/trinh-xem-tai-lieu/dung.sh` (xem `tu-dong-hoa/trinh-xem-tai-lieu/README.md`).

**Phòng khi thiết bị này hỏng:** repo này giữ bộ não và skill; Drive `thanh-pham` giữ thành phẩm; Drive `sao-luu-claude-2026-11-07/du-an-video` giữ âm thanh gốc và kịch bản từng dự án (bỏ `node_modules` và file render, dựng lại được). Giải nén vào `~/Movies`, chạy `npm install` trong `chuyen-dong/`, rồi render lại. File `.env` của App notion, `~/Documents/mk.csv`, hồ sơ đăng nhập Chrome và lịch sử chat chỉ có trên máy này, cố ý không đưa lên mạng.

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

`cai-dat-bo-nao.sh` thay `~/.claude/david.md`, `CLAUDE.md`, các skill, thư mục bộ nhớ và sổ danh mục bằng **lối tắt trỏ vào repo** (bản cũ sao lưu vào `~/.claude/backups/`), rồi cài hook đồng bộ 2 chiều: đầu phiên pull từ GitHub về, cuối phiên push lên. Từ đó thiết bị và GitHub luôn là một bộ não. Khi cài **Mac chính** (không có `--chi-video`), script tự tải luôn repo riêng tư `bo-nao-david-mac` vào cùng thư mục, nên `gh auth login` phải đăng nhập đúng tài khoản David. Sau đó cài bot, lịch, trang xem theo mục 5.

Bộ nhớ của Claude Code gắn theo thư mục dự án. Tham số cuối là thư mục bạn sẽ mở Claude Code (mặc định là chính repo). Muốn dùng ở thư mục khác thì chạy lại với thư mục đó.

**Mac chỉ dựng video** (không phải Mac chính): thêm `--chi-video` vào lệnh cài ở trên. Thiết bị đó vẫn đồng bộ 2 chiều nhưng không cài bot Telegram, không cài lịch tự chạy. Sau đó người dùng cài công cụ dựng đúng phiên bản và để thiết bị tự kiểm tra:

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh
```

```bash
zsh ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh
```

Đồng bộ thủ công bất cứ lúc nào:

```bash
bash ~/Documents/bo-nao-david/tu-dong-hoa/dong-bo.sh
```

## 3. Máy Windows (chỉ dựng video)

Windows chạy skill qua **WSL2**, tức một Ubuntu chạy bên trong Windows. Nhờ vậy Windows dùng nguyên script của Mac, chỉ giữ một bộ skill. Thiết bị nào cũng push được lên GitHub vì đăng nhập đúng tài khoản David. Bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ ở Mac chính. Chi tiết phần nào giống hệt, phần nào gần giống: [tu-dong-hoa/thiet-bi-khac/README.md](tu-dong-hoa/thiet-bi-khac/README.md).

**Một lần trên Windows** (David tự làm):

1. Mở PowerShell bằng quyền quản trị (nhấp chuột phải rồi chọn Run as administrator), chạy `wsl --install -d Ubuntu-24.04`, khởi động lại máy. Mở "Ubuntu" từ menu Start, đặt tên và mật khẩu cho Ubuntu.
2. Cài **Google Drive cho máy tính** (bản Windows), đăng nhập tài khoản của David, để chế độ tệp trên mây; không thêm thư mục nào của máy vào đồng bộ và **không gắn ổ Drive vào Ubuntu** (`du-an/kho-drive.md` mục "Máy Windows").
   Để chạy `kiem-tra-thiet-bi.sh`: tải thư mục `tu-lieu-goc/_bo-thu-may` bằng link David gửi (`gdown --folder <link>`) rồi chạy `BO_THU=<thư mục đó> zsh .../kiem-tra-thiet-bi.sh`; chưa chạy đạt thì **chưa tính là cài xong**.
   **Không dựng bằng bản repo clone phía Windows** (Git cho Windows chuyển liên kết thư viện hình thành file văn bản): chỉ dùng bản trong Ubuntu `~/Documents/bo-nao-david`.

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
bash ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh
```

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

```bash
zsh ~/Documents/bo-nao-david/tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh
```

- `cai-dat-bo-nao.sh` thấy máy không phải Mac thì tự cài kiểu "chỉ dựng video".
- `cai-cong-cu-video.sh` cài đúng phiên bản Mac đang dùng: ffmpeg, whisper.cpp kèm mô hình 1,5 GB, Node, pyannote, công cụ phát hiện khuôn mặt. Script hỏi mật khẩu Ubuntu một lần. Trên Windows script tự đặt `PYTHONUTF8=1` để Python phía Windows không lỗi chữ Việt. Script cũng in các bước để David tự lấy token Hugging Face cho phần tách người nói podcast (một lần).
- `kiem-tra-thiet-bi.sh` dựng thử 20 giây bằng đúng script của skill rồi so với bản chuẩn của Mac. Bộ dữ liệu thử nằm trên Drive `tu-lieu-goc/_bo-thu-may/` (tải bằng link, đặt `BO_THU`). Kết quả phải là **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**.

**Dùng hằng ngày:** mở Ubuntu, `cd ~/Documents/bo-nao-david && claude`, rồi làm như trên Mac: gửi video, gọi skill.
- Video gốc: David gửi link, Claude tải về bằng `gdown`.
- Dự án dựng nằm ở `~/Movies` của Ubuntu. Mở bằng Windows Explorer: gõ `explorer.exe ~/Movies` trong Ubuntu, hoặc vào `\\wsl$\Ubuntu-24.04\home\<tên>\Movies`.
- Thành phẩm lên Drive bằng `cho-dang.sh gui` / `luu-drive.sh` (tự chép từ phía Windows). Khác Mac: không hỏi được từng tệp đã lên mây chưa và không tự xoá bản trên máy.
- Máy có card NVIDIA cài CUDA trong WSL thì Whisper chạy nhanh hơn nhiều (script tự dùng). Không có thì chạy bằng CPU: chậm hơn Mac nhưng ra cùng kết quả.

## 4. AI khác hoặc Claude bản web

- Có kết nối GitHub: cấp quyền cho repo `Covandieuhanh/bo-nao-david`, rồi dán câu mở đầu trong `README.md`.
- Không có kết nối GitHub: tải ZIP của repo, hoặc tải riêng `AGENTS.md`, `co-so-tri-thuc/david.md`, `bao-cao-trang-thai.md`, `ky-nang/thu-thap-yeu-cau/SKILL.md`.
- AI bản web không chạy được lệnh trên máy: làm được phần lọc, kế hoạch, viết bài; không dựng được video.

### Kiểm tra khả năng thực thi

Dùng cùng mục này trên mọi AI và thiết bị khi David giao một việc cần đầu ra. Trao đổi để làm rõ thông tin tiếp tục theo tư duy gốc.

1. **Nguồn và phiên bản.** Đọc `AGENTS.md`, Mục tiêu, nguồn trạng thái và quy trình lá phù hợp. Dùng bản repo đang có hiệu lực và cùng bản đầu vào khi so sánh hai lần chạy. Ghi mã commit khi xác định được. Nếu chỉ đọc một bản tệp được cung cấp, ghi nguồn và phiên bản chưa xác định nếu cần.
2. **Khả năng thực thi.** Kiểm đúng công cụ, tài nguyên, quyền và cách ghi nhật ký cần cho việc đang làm. Khi quy trình có phép kiểm thiết bị, chạy phép kiểm đó. Với lời giao cần tạo tệp hoặc dựng video, xác nhận môi trường thực sự có thể mở nguồn, chạy công cụ và ghi đầu ra. Kiểm tra nhật ký theo mục dưới nếu ứng dụng có hỗ trợ.
3. **Cách thay thế.** Nếu thiếu một cấu hình, công cụ hoặc quyền, dùng phương án tương đương đã kiểm được khi có. Tiếp tục các phần đã đủ điều kiện và nêu chính xác phần bị chặn, lý do và phần cần thiết để hoàn tất.
4. **Nghiệm thu.** Dùng cùng các tiêu chí bắt buộc trong “Xong khi” trên mọi lần chạy. Phiên chỉ báo một tiêu chí đạt khi có đầu ra và bằng chứng tương ứng. Sau khi chuẩn chung đạt, ghi nhận giá trị sáng tạo tăng thêm của từng AI.

Ví dụ: cùng một video gốc, yêu cầu và phiên bản quy trình, Mac và Windows có thể dùng bộ mã hóa khác nhau nhưng phải qua cùng phép kiểm đầu ra. Một phiên chỉ có quyền đọc tài liệu có thể hoàn thành bản kế hoạch dựng. Bản video cần bằng chứng đã thực thi và kiểm trên môi trường có công cụ.

### Bật nhật ký công việc

[Nhật ký công việc](tu-dong-hoa/nhat-ky/README.md) hướng dẫn bật trên Claude Code, Codex và nhập bản ghi từ nguồn khác. Kho mặc định ở ngoài Git trên thiết bị. Chọn thư mục đồng bộ riêng nếu cần đọc lịch sử chung từ nhiều máy.

## 5. Những thứ repo không mang theo được

| Hạng mục cần có | Cách lấy lại |
|---|---|
| Công cụ dựng video, đúng phiên bản Mac | `bash tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh` (ffmpeg, whisper.cpp, Node, Pillow, pyannote, phát hiện khuôn mặt; bản khoá phiên bản ở `tu-dong-hoa/thiet-bi-khac/phien-ban.env`). Kiểm tra nhanh: `kiem-moi-truong.sh` của skill; so kết quả với Mac: `kiem-tra-thiet-bi.sh` |
| Mô hình Whisper (1,5 GB) | `cai-cong-cu-video.sh` tải về `~/whisper-models` và kiểm tra mã checksum |
| `~/.cache/dung-video-theo-phong-cach` (phát hiện khuôn mặt, môi trường Python) | `cai-cong-cu-video.sh` tạo lại; trên Mac, Vision tự dựng lại khi dùng lần đầu |
| Mô hình tách người nói pyannote (khoảng 31 MB) | Cần tài khoản Hugging Face. `cai-cong-cu-video.sh` in các bước David tự làm một lần (đồng ý điều khoản, dán token đọc); chưa có thì skill đoán người nói trong podcast nhiều người theo giọng |
| Bot Telegram Sổ nhớ (chạy 24/7) | Cài plugin Telegram (cai-dat-bo-nao.sh đã cài), dán token bot vào `~/.claude/channels/so-tay/.env` (David giữ token, không lên GitHub), rồi `bash tu-dong-hoa/so-tay/cai-dat.sh`: sao chép luật và quyền của bot, cài launchd `com.david.so-tay`. Chức năng nghe tin nhắn thoại dùng chung mô hình Whisper ở dòng trên |
| Bot Telegram Điều hành (chạy 24/7, sau bot Sổ nhớ) | Tạo bot ở @BotFather (David giữ token), rồi `bash tu-dong-hoa/dieu-hanh/cai-dat.sh "<token>"`: lưu token vào `~/.claude/channels/dieu-hanh/.env`, cài launchd `com.david.dieu-hanh`, sao chép luật mới cho Sổ nhớ. Không cần Claude chạy. Xem `tu-dong-hoa/dieu-hanh/README.md` |
| Bộ não công ty Veltrix (riêng, private) | `git clone https://github.com/Covandieuhanh/veltrix.git ~/Documents/bo-nao-veltrix`. Phiên lịch tự thêm thư mục này (`chay-lich.sh --add-dir`) để ghi nhật ký điều hành; push bằng `bash ~/Documents/bo-nao-veltrix/dong-bo.sh` |
| Trang xem kết quả video + trang bài đăng + trang kiểm video trên Mac (`localhost:8765`, `/bai-dang`, `/mac`, tự khởi động khi bật máy) | `bash tu-dong-hoa/cai-trang-xem.sh`: cài launchd `com.david.xem-ket-qua` chạy `tu-dong-hoa/xem-ket-qua.py`; bài, ảnh đọc từ `~/Documents/1-nghe-nghiep/bai-dang/` (không lên GitHub) |
| Lịch tự chạy (tổng hợp tin 7:00, thu thập 23:00, đóng gói thứ 6 06:30) | Theo repo: `tu-dong-hoa/lich/lich-chay.md`. Đến giờ, tiến trình giám sát của bot mở một phiên hiện trong app Claude (Remote Control, có Claude in Chrome); cài bot thì có lịch này. Không dùng Scheduled tasks của app (app chỉ đọc lịch lúc khởi động, gắn theo tài khoản). Lần đầu trên máy: chạy `claude --chrome` trong Terminal, bấm Enter ở màn giới thiệu Claude in Chrome rồi `/exit`. Zalo, Messenger, Telegram Web đăng nhập trong Chrome. Kho thu thập `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/` chỉ ở thiết bị, sao lưu lên Drive cùng sổ nhớ |
| Tín hiệu tự học (`~/.claude/hoc-lien-tuc/`) | Có nội dung trò chuyện nên giữ lại trên thiết bị; thiết bị mới tự ghi lại từ đầu (hook do cai-dat-bo-nao.sh cài) |
| `playwright-cli` | Cài qua npm toàn cục, kiểm tra bằng `playwright-cli --help` |
| Đăng nhập YouTube, Facebook, TikTok | David tự đăng nhập lại. Hồ sơ Chrome đăng bài ở `~/.cache/david-mxh-chrome` |
| Google Drive (`tu-lieu-goc`, `thanh-pham`) | Cài Google Drive cho máy tính, đăng nhập tài khoản của David; máy Windows xem thêm `du-an/kho-drive.md` mục "Máy Windows" |
| Trình duyệt và kết nối của Claude | Bật lại trong ứng dụng Claude |
| Video gốc, thành phẩm, kịch bản, bài đăng từng dự án | Ở Drive và `~/Movies` của máy làm, không nằm trong repo. Repo chỉ ghi trạng thái ở `bao-cao-trang-thai.md` và `du-an/danh-muc-noi-dung.md` |

## 6. Sau khi cài, kiểm tra nhanh

Mở Claude Code và nói: "Tôi là ai, và bạn phải làm gì trước khi tạo một file mới?" Câu trả lời đúng phải nói được David là nhà đào tạo cho người lần đầu dẫn người, và phải hỏi rồi chờ "ok".

## 7. Dựng video ở máy khác (Windows, Mac khác, AI khác)

Thiết bị chỉ cần có repo này là đủ để dựng video giống Mac chính. Không cần nhớ gì từ các phiên trước: mọi cách nghĩ đã nằm trong file.

1. **Cài đặt và tự kiểm tra thiết bị** (một lần): [huong-dan-cai-dat.md](huong-dan-cai-dat.md) mục 3, rồi `tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh` phải ra "giống Mac chính".
2. **Đọc theo thứ tự, trước khi viết kịch bản cảnh:**
   [nhu-cau-nguoi-xem.md](ky-nang/san-xuat-video/thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md) (cách nghĩ: loại nội dung → cái khó của người xem → nguyên lý) →
   [truong-hop-da-giai.md](ky-nang/san-xuat-video/thiet-ke-bo-cuc/truong-hop-da-giai.md) (19 trường hợp thực tế từ hình mẫu thành công) →
   [huong-dan-lua-chon.md](ky-nang/san-xuat-video/thiet-ke-bo-cuc/huong-dan-lua-chon.md) (các bước + kho cách thể hiện theo nguyên lý) →
   [bo-cuc.md](ky-nang/san-xuat-video/thiet-ke-bo-cuc/bo-cuc.md) (kiểu có sẵn, ảnh mẫu từng kiểu, cách viết `canh.js`) → skill dựng (cây quy trình lá B6).
3. **Yêu cầu của David** nằm trong thư mục dự án: `yeu-cau.md` (viết tự do) và `them-anh/` (ảnh `mau-*` là kiểu muốn học theo, ảnh khác là ảnh chèn).
   Cách xử lý: `huong-dan-lua-chon.md` bước 0b.
4. **Lập luận thành chữ** trong `ke-hoach-canh.md`: `Loại:` cho cả video, mỗi cảnh `Cần · Vì · Làm`. `soat-canh.mjs` chặn render khi thiếu;
   người làm không được bỏ qua cổng kiểm soát này, vì đây là cơ chế giữ video đúng nội dung khi không có người kiểm tra.
5. **Thiết bị mới: làm bài kiểm suy luận** [bai-kiem/](ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/README.md) (không mở đáp án), chấm bằng
   `python3 -I cham.py bai-lam.json`; đạt ít nhất 8/10 mới dựng video thật, chưa đạt thì gửi các đoạn ✗ cho David.

### Đồng bộ skill video đang cài cho Codex

Từ bản repo dùng chung, chạy `bash tu-dong-hoa/cai-dat-bo-nao.sh --codex-video`. Lệnh sao lưu hai thư mục skill cũ nếu có rồi liên kết skill dựng video, podcast và highlight với repo. Mở phiên mới để Codex nạp lại danh sách skill.

### Dựng lại một bản đối chiếu motion graphics

Mở Claude Code trong repo đã đồng bộ. Khi đã có gói dựng của một bản bàn giao, giải nén và đọc `README.md` trong gói. Chọn đúng tệp video nguồn theo hướng dẫn, dùng font kèm theo và chạy đúng lệnh xuất từ gói. Với bản có `render.py` và `doi-chieu.render.json`, dùng tùy chọn `--expect doi-chieu.render.json` để kiểm nguồn, mã dựng, phông và ảnh/tiếng đã giải mã. Sai nguồn hoặc tài nguyên thì xác định lại phiên bản trước khi dựng. Sai ảnh hoặc tiếng trên máy khác thì so phiên bản Pillow, FFmpeg và khung ở mốc kiểm. Skill và tài liệu triển khai cách chọn cảnh mới; gói dựng phục vụ xuất lại đúng bản đã kiểm.
