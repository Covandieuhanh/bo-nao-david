---
description: "Biểu mẫu 01 cho học viên: hướng dẫn thiết lập hệ thống (cài công cụ dựng video AI trên máy)."
---

# Biểu mẫu 01 · Hướng dẫn thiết lập hệ thống (System Setup Guide) (Bài 1)

> Lệnh và tên gói đổi theo thời gian: **trainer kiểm lại trang chính thức của từng công cụ trước mỗi khoá**.

## Cần những gì, để làm gì
| Công cụ | Việc | Giá |
|---|---|---|
| **Trợ lý AI chạy lệnh**: chọn 1 (Claude Code · Codex CLI · Gemini CLI…) | đọc quy trình vận hành chuẩn (SOP), chạy các công cụ dưới, làm trọn 8 bước | theo gói AI học viên đang trả |
| **ffmpeg** | cắt, ghép, đổi khung, gắn phụ đề, chuẩn âm lượng | miễn phí |
| **Whisper** | chép lời có mốc thời gian (chạy trên máy) | miễn phí |
| **Node.js** | chạy trợ lý AI và Remotion | miễn phí |
| **Python** | các bước tự động nhỏ | miễn phí |
| **Remotion** (khi cần đồ hoạ đẹp) | dựng chữ, hình minh hoạ bằng code | miễn phí cho cá nhân, công ty tối đa 3 người; lớn hơn cần giấy phép |

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
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/cai-dat-bo-nao.sh)"
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
Cài bản whisper.cpp thì lệnh kiểm là:
```bash
whisper-cli --help
```
Cả hai in ra chữ, không báo lỗi thì đạt. Rồi chép biểu mẫu 02 vào thư mục `lam-video` (Bài 2).

## Lỗi hay gặp
- **"command not found"**: đóng mở lại Terminal / PowerShell; vẫn lỗi thì nhờ trợ lý AI sửa đường dẫn.
- **Whisper chậm**: dùng mô hình nhỏ hơn (`--model small`) khi thử, `medium` khi làm thật.
- **Không tìm thấy file vừa làm, không biết đường dẫn**: kéo thả file hay thư mục vào cửa sổ Terminal / PowerShell là hiện đường dẫn; hoặc nói với trợ lý AI "mở thư mục 3-xuat của tap-…" (Mac: `open`, Windows: `explorer`). Đặt tên thư mục theo nghĩa rõ, không dấu, gạch nối để AI và người cùng tìm ra.
- **Hết ổ đĩa**: trước khi xuất bản dài, nhờ AI kiểm ổ trống (ít nhất gấp 3 dung lượng bản xuất); AI xoá file tạm ngay khi xong mỗi bước; mỗi tập xong chỉ giữ bản gốc + bản cuối.
- **AI hết lượt khi đang làm dở**: tài khoản AI thường có hai hạn mức, một theo phiên vài giờ và một theo tuần (giờ mở lại xem trong phần mức dùng của app). Trước khi giao việc dài, dặn AI ghi tiến độ vào `2-lam/ke-hoach.md` sau mỗi bước; hết lượt thì chờ mở lại rồi nói "đọc ke-hoach.md, làm tiếp", không phải làm lại từ đầu.
