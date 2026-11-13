# Mẫu 07 · Cài đặt tuyến C: máy tính + AI tự làm (Bài 3)

> Lệnh và tên gói đổi theo thời gian: **trainer kiểm lại trang chính thức của từng công cụ trước mỗi khoá**. Tuyến A, B không cần file này.

## Cần những gì, để làm gì
| Công cụ | Việc | Giá |
|---|---|---|
| **Trợ lý AI chạy lệnh**: chọn 1 (Claude Code · Codex CLI · Gemini CLI…) | đọc hướng dẫn, chạy các công cụ dưới, làm trọn 9 bước | theo gói AI học viên đang trả |
| **ffmpeg** | cắt, ghép, đổi khung, gắn phụ đề, chuẩn âm lượng | miễn phí |
| **Whisper** | chép lời có mốc thời gian (chạy trên máy) | miễn phí |
| **Node.js** | chạy trợ lý AI và Remotion | miễn phí |
| **Python** | các bước tự động nhỏ | miễn phí |
| **Remotion** (khi cần đồ hoạ đẹp) | dựng chữ, hình minh hoạ bằng code | miễn phí cho cá nhân, công ty ≤ 3 người; lớn hơn cần giấy phép |

## Cách 1 (khuyên dùng): để AI tự cài
1. Cài Node.js từ trang chính thức nodejs.org (bản LTS).
2. Cài trợ lý AI theo trang chính thức của nó, đăng nhập bằng tài khoản của học viên (học viên tự gõ mật khẩu, không đưa cho ai).
3. Tạo thư mục `lam-video`, mở trợ lý AI trong thư mục đó, dán:
```
Kiểm tra máy tôi đã có ffmpeg, Python, Whisper chưa. Thiếu cái nào thì cài,
GIẢI THÍCH từng lệnh trước khi chạy và hỏi tôi đồng ý. Xong thì chạy thử:
chép lời một file mẫu 10 giây và báo kết quả.
```

## Cách 2: tự cài bằng lệnh
**Mac** (mở Terminal):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
```bash
brew install ffmpeg node python pipx
```
```bash
pipx install openai-whisper
```

**Windows** (mở PowerShell):
```powershell
winget install Gyan.FFmpeg
```
```powershell
winget install OpenJS.NodeJS.LTS
```
```powershell
winget install Python.Python.3.12
```
```powershell
pip install -U openai-whisper
```

**Trợ lý AI** (chọn 1, kiểm lại lệnh trên trang chính thức):
```bash
npm install -g @anthropic-ai/claude-code
```
```bash
npm install -g @openai/codex
```
```bash
npm install -g @google/gemini-cli
```

## Kiểm tra cài xong
```bash
ffmpeg -version
```
```bash
whisper --help
```
Cả hai in ra chữ, không báo lỗi → đạt. Rồi chép mẫu 08 vào thư mục `lam-video` và chạy thử Bài 3.

## Lỗi hay gặp
- **"command not found"**: đóng mở lại Terminal / PowerShell; vẫn lỗi thì nhờ trợ lý AI sửa đường dẫn.
- **Whisper chậm**: dùng mô hình nhỏ hơn (`--model small`) khi thử, `medium` khi làm thật.
- **Hết ổ đĩa**: mỗi tập xong chỉ giữ bản gốc + bản cuối.
