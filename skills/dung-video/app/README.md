# App dựng video (chạy trên máy này)

Mục tiêu: **tiết kiệm token tối đa** mà vẫn ra kết quả như skill. Phần cố định do máy chạy; Claude chỉ được gọi ở bước cần phán đoán,
mỗi lần chỉ nhận đúng thứ cần và trả về một JSON ngắn (trích câu, không dò mốc, không viết code).

## Mở app
App chạy nền tự động (LaunchAgent của macOS): mở máy là có, tắt hay lỗi thì macOS tự bật lại. **Chỉ cần mở http://localhost:8765.**
Cài một lần trên mỗi máy (đã cài trên Mac chính 08/11/2026):
```bash
zsh ~/Documents/David.Claude/scripts/app-video.sh cai
```
Khác: `app-video.sh xem` (đang chạy không) · `khoi-lai` (sau khi sửa code app; việc đang dựng không bị ngắt) · `go` (gỡ hẳn). Log: `~/Movies/_app/may-chu.log`.
**Từ iPhone / máy khác (Tailscale):** cài Tailscale, đăng nhập cùng tài khoản với Mac → mở `http://macbook-david:8765`
(tên đầy đủ `http://macbook-david.tail58c7e2.ts.net:8765`). App chỉ nhận chính Mac + thiết bị trong Tailscale của David; máy cùng wifi
hay ngoài Internet bị chặn. `app-video.sh cai` cũng giữ Mac không ngủ khi cắm sạc (`caffeinate -s`), để iPhone luôn vào được.

Trong app: **+ Việc mới** → kéo thả / chọn tệp từ máy đang cầm (tải lên Mac), hoặc **📁 Chọn tệp trên Mac** (duyệt Drive Video-goc, Tải về,
Màn hình nền, Phim… có ảnh nhỏ; chỉ trong thư mục nhà, bỏ thư mục ẩn và ~/Library trừ Google Drive) → tên tập tự đặt, chọn tuỳ chọn (khung xuất, ảnh minh hoạ, thẻ tít, lịch phát,
yêu cầu riêng) → app tự chạy, dừng ở 2 cổng chờ David duyệt. Cổng 2: xem video, tờ kiểm tra hình, chọn thumbnail, kết quả kiểm, bài đăng.
Nút: **⏹ Dừng** (tắt cả render) · **▶ Chạy tiếp** (làm lại bước dở) · **làm lại từ đây** · **🗑 Xoá dự án** (chuyển `~/Movies/_app/<tên>` + `~/Movies/tap-<tên>` vào Thùng rác).
**Sửa skill khi đang có dự án:** bước CHƯA chạy tự dùng skill mới (lời nhắc, hồ sơ, script đọc lúc chạy). Bước đã chạy: bấm
**làm lại từ đây** — chạy lại bước đó và các bước sau; bước Claude nào đầu vào không đổi thì **dùng lại kết quả cũ, 0 token**
(`~/Movies/_app/<tên>/nho-claude/`; `APP_KHONG_NHO=1` để tắt). Phần hình (khung dựng, thư viện hình) được CHÉP vào dự án lúc tạo →
bấm **🔄 Cập nhật khung dựng** để lấy bản mới (giữ kịch bản, phụ đề, thông số; bản cũ cất ở `check/khung-truoc-<giờ>/`; đã render thì tự render lại).
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
| `loi-nhac/*.md` | lời nhắc cho Claude — **chèn thẳng luật gốc**: cả file (`{{file:…}}`), một mục (`{{muc:file|tiêu đề}}`), hồ sơ tham số (`{{ho_so:…}}`), biểu tượng (`{{bieu_tuong}}`), kiểu cảnh của template (`{{kieu_canh}}`) |
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

## Công thức `lam-video` (28 bước = đủ skill video-style-edit chế độ 1 video)
| Nhóm | Bước | Ai |
|---|---|---|
| Chuẩn bị | kiểm công cụ · tạo dự án · chép lời thô + đề xuất cắt | máy |
| Lọc | lọc nội dung + chọn chỗ cắt + **xem ảnh**: chiều hình, chữ/viền in cứng; đề xuất câu chốt, ý chính, chữ thumbnail | Claude |
| | ghi phiếu lọc · ghi sổ danh mục | máy |
| **Cổng 1** | David duyệt phiếu lọc (thay "hỏi một lần" của skill) | David |
| Làm sạch | cắt + sửa chiều hình · cắt chữ/viền in cứng · đổi khung (ngang↔dọc, nếu chọn) · nâng khung · chép lời bản sạch + phụ đề | máy |
| Kịch bản | kịch bản cảnh: mọi kiểu cảnh của template, trích câu | Claude |
| | tìm mốc, ghi scenes.js / project.js (chủ đề, nhạc, **màn kết YouTube**, lịch), sửa phụ đề, ke-hoach-canh.md | máy |
| Ảnh (khi cần) | tìm ảnh Openverse → **Claude xem & chọn** → tải ảnh, nguồn ảnh (không có ảnh tốt thì giữ biểu tượng) | máy · Claude |
| Dựng | tránh che mặt · soát cảnh · render (**chỉ phần bị đổi**) · tờ kiểm tra hình · luật kiểm | máy |
| Phát hành | tiêu đề, mô tả, bình luận ghim, khung bìa, chữ thumbnail, teaser | Claude |
| | thumbnail 2 mẫu (ngang) · teaser · chương · phat-hanh.md · so-lieu.md | máy |
| **Cổng 2** | David xem video + tờ kiểm tra, chọn thumbnail, duyệt hoặc góp ý | David |
| Xong | ghi sổ danh mục (chờ đăng) · dọn file tạm (vào Thùng rác) | máy |

Luật kiểm (`kiem/`): âm lượng −14 LUFS · âm so bản gốc + tiếng rè · thời lượng · chữ nguyên văn.

## Ngoài app (làm bằng Claude Code như cũ)
- Highlight, podcast, ghép vlog: chưa có công thức.
- Học cách trình bày từ video mẫu: skill `hoc-video-mau` (sửa bộ skill, app tự theo vì dùng chung luật và thư viện hình).
- Đưa video lên Drive, đăng bài lên kênh: skill `dang-da-kenh` (cần trình duyệt, David duyệt từng bài).
- Đổi khung ngang → dọc dùng kế hoạch tự động của `reframe_plan.py`, chưa có bước Claude xem lại `tracks.jpg`.
