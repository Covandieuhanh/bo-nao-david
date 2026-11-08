# App dựng video (chạy trên máy này)

Mục tiêu: **tiết kiệm token tối đa** mà vẫn ra kết quả như skill. Phần cố định do máy chạy; Claude chỉ được gọi ở bước cần phán đoán,
mỗi lần chỉ nhận đúng thứ cần và trả về một JSON ngắn (trích câu, không dò mốc, không viết code).

## Mở app
```bash
python3 -I ~/Documents/David.Claude/skills/dung-video/app/giao_dien.py
```
Mở http://localhost:8765 → **+ Việc mới** → kéo thả (hoặc chọn) video, tên tập tự đặt → app tự chạy, dừng ở 2 cổng chờ David duyệt.
Nút: **⏹ Dừng** (tắt cả render) · **▶ Chạy tiếp** (làm lại bước dở) · **làm lại từ đây** · **🗑 Xoá dự án** (chuyển `~/Movies/_app/<tên>` + `~/Movies/tap-<tên>` vào Thùng rác).
Việc chạy trong nhóm tiến trình riêng: tắt/khởi động lại giao diện không làm ngắt việc đang chạy.
Dòng lệnh thay giao diện: `python3 -I chay.py moi lam-video <video> <tên>` · `chay.py duyet <tên> [góp ý]` · `chay.py lai <tên> <bước>`.

## Lần đầu: đăng nhập Claude cho app (David tự làm, một lần)
App gọi Claude Code chạy ngầm (`claude -p`), tính vào gói Claude của David, không tốn tiền API. Lệnh này cần đăng nhập riêng:
```bash
"$(ls -t ~/Library/Application\ Support/Claude/claude-code/*/*/claude.app/Contents/MacOS/claude | head -1)"
```
Gõ `/login`, đăng nhập bằng tài khoản Claude của David trên trình duyệt, xong gõ `/exit`.

## Cấu trúc (app không chứa luật)
| Thư mục | Là gì |
|---|---|
| `cong-thuc/<loại>.json` | thứ tự bước cho một loại video |
| `buoc/<id>.json` | phiếu một bước: `co-dinh` (lệnh) · `claude` (lời nhắc + khuôn + lệnh kiểm) · `duyet` (cổng) |
| `loi-nhac/*.md` | lời nhắc cho Claude — **chèn thẳng README khối** (`{{file:…}}`), hồ sơ tham số (`{{ho_so:…}}`), danh sách biểu tượng (`{{bieu_tuong}}`) |
| `khuon/*.json` | khuôn JSON Claude phải trả |
| `ap/` | script biến kế hoạch của Claude thành file dự án (tìm mốc từ câu trích, soát nguyên văn) |
| `kiem/kiem_*.py` | luật kiểm bản cuối, app tự chạy mọi file trong thư mục |
| `chay.py` · `goi_claude.py` · `giao_dien.*` | máy chạy bước, gọi Claude, giao diện |

Trạng thái từng việc, log, kế hoạch Claude, số token: `~/Movies/_app/<tên>/` (ở lại máy, không lên GitHub).

## Thêm tiêu chí cố định — KHÔNG sửa app
| Muốn | Làm |
|---|---|
| Đổi một con số | sửa `ho-so/*.json` |
| Thêm luật kiểm | thả `kiem/kiem_<tên>.py` (nhận `<dự án>`, in 1 dòng, thoát 0 = đạt) |
| Thêm bước | thêm `buoc/<id>.json` + tên bước vào `cong-thuc/<loại>.json` |
| Thêm biểu tượng / tuyến nhạc | thêm vào thư viện hình / hồ sơ — Claude tự thấy |
| Đổi luật dựng (bố cục, kết thúc, lọc, phát hành) | sửa README khối — lời nhắc chèn thẳng file đó |
| Đổi bước nào cần Claude hay không | đổi `loai` trong phiếu bước |

## Giới hạn hiện tại (làm bằng Claude Code như cũ)
- Mới có công thức **làm video 1 người nói** (`lam-video`). Highlight, podcast, ghép vlog: thêm công thức sau.
- Không tự xử lý chữ/viền in cứng trong hình của video cũ (cần nhìn hình).
- Góp ý ở cổng 2 làm lại từ bước kịch bản cảnh và render lại cả video.
