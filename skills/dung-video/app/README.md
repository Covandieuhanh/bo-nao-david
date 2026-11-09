# App dựng video (chạy trên máy này)

Mục tiêu ưu tiên David xác nhận 09/11/2026: **chất lượng render phải đạt chuẩn skill về thẩm mỹ, nội dung và kỹ thuật**.
Tiết kiệm token chỉ là mục tiêu phụ sau khi giữ được chất lượng. Chưa có đối chiếu thành phẩm đầy đủ thì không tuyên bố ngang skill.

## Chọn Claude hoặc Codex
- Việc mới: chọn AI trên giao diện. Việc cũ đang dừng: đổi “AI cho các bước tiếp theo”; không tự chạy lại bước đã xong.
- Mọi bước có `loai: claude` (tên cũ để tương thích) đều qua adapter chung: Claude CLI hoặc Codex CLI.
- Codex: cài CLI, `codex login`, kiểm tra `codex login status`. Dùng đăng nhập sẵn của chính máy, không bắt buộc API key.
- `APP_AI=codex` đặt mặc định cho việc mới; `APP_CODEX_MODEL=<tên>` hoặc `tuy_chon.ai_model` ghim model khi cần đối chiếu có thể lặp lại.
  Không ghim thì CLI chọn mặc định; log ghi rõ không ghim, không coi là so sánh model cố định.
- Codex nhận ảnh trực tiếp qua `--image`, trả JSON qua `--output-schema`; chạy read-only và không lưu phiên.
  JSON bên trong qua kiểm khuôn cục bộ và cùng bộ kiểm nghiệp vụ như Claude.
- Cache gồm AI, model yêu cầu, mức suy nghĩ, luật, đầu vào và nội dung ảnh. Đổi AI không dùng nhầm kết quả AI cũ.
- Không tự đổi nhà cung cấp hoặc hạ model khi hết hạn mức. Người dùng chọn rõ ràng trên app.
- Lời, hình và kế hoạch được gửi đến nhà cung cấp AI đã chọn, dùng tài khoản của David; không phải AI chạy hoàn toàn offline.
- Tài liệu chính thức: https://learn.chatgpt.com/docs/non-interactive-mode

## Kiểm chất lượng
- Video người nói: chụp thử từng cảnh → AI duyệt → sửa và AI xem lại ảnh mới trước render.
- Sau render: AI duyệt → sửa → tạo ảnh kiểm mới → AI duyệt lại. Tối đa 2 lần sửa mỗi đợt; vẫn chưa đạt thì dừng, không chuyển phát hành.
- Lỗi cần sửa nguồn hoặc code mà JSON không xử lý được: trả `can_xu_ly_ngoai_ke_hoach`, app dừng và báo; chưa có agent tự sửa code trong app.
- Tờ kiểm bản cuối chia trang 32 mốc, giữ mọi cảnh, không cắt bỏ mốc cuối video.
- Kiểm kỹ thuật thất bại phải dừng. Các phép kiểm hiện tại chưa thay thế nghe/xem toàn video hoặc David chấm thẩm mỹ.
- Kiểm thử: `python3 -I app/tests/test_app.py` (chạy từ thư mục skill).

## Mở app
App chạy nền tự động (LaunchAgent của macOS): mở máy là có, tắt hay lỗi thì macOS tự bật lại. **Chỉ cần mở http://localhost:8765.**
Cài một lần trên mỗi máy (đã cài trên Mac chính 08/11/2026):
```bash
zsh ~/Documents/David.Claude/scripts/app-video.sh cai
```
Khác: `app-video.sh xem` (đang chạy không) · `khoi-lai` (sau khi sửa code app; việc đang dựng không bị ngắt) · `go` (gỡ hẳn). Log: `~/Movies/_app/may-chu.log`.
**Truy cập:** chỉ trên Mac này qua localhost; máy chủ bind loopback. Không mở qua Tailscale hoặc mạng ngoài.

Trong app: **+ Việc mới** → kéo thả / chọn tệp từ máy đang cầm (tải lên Mac), hoặc **📁 Chọn tệp trên Mac** (duyệt Drive Video-goc, Tải về,
Màn hình nền, Phim… có ảnh nhỏ; chỉ trong thư mục nhà, bỏ thư mục ẩn và ~/Library trừ Google Drive) → tên tập tự đặt, chọn tuỳ chọn (khung xuất, ảnh minh hoạ, thẻ tít, lịch phát,
yêu cầu riêng) → app tự chạy, dừng ở 2 cổng chờ David duyệt. Cổng 2: xem video, tờ kiểm tra hình, chọn thumbnail, kết quả kiểm, bài đăng.
Nút: **⏹ Dừng** (tắt cả render) · **▶ Chạy tiếp** (làm lại bước dở) · **làm lại từ đây** · **🗑 Xoá dự án** (chuyển `~/Movies/_app/<tên>` + `~/Movies/tap-<tên>` vào Thùng rác).
**Rà soát tự động (`ra_soat.py`):** mở một dự án, app tự so skill hiện tại với lúc từng bước chạy — bước Claude so lại cả luật đã
ghép, bước máy so script nó gọi + hồ sơ, phần hình so khung dựng. Có đổi → khung ⚠ "Skill đã đổi sau khi dự án này chạy", ⚠ cạnh
từng bước, nút **Làm lại từ** bước sớm nhất bị ảnh hưởng và nút **Cập nhật khung dựng**. Phiên Claude Code khác sửa skill cũng thấy
(cùng thư mục). Bước chạy trước bản app 08/11 23:30 chưa có giờ chạy nên không rà được.
**Video từ điện thoại qua Google Drive (`drive.py`):** tải video vào thư mục **Video-goc** trên Drive bằng điện thoại → ở Việc mới,
mục "Mới trong Drive Video-goc" hiện sẵn video mới nhất, bấm là chọn. Hoặc **dán link Drive** (tệp hay thư mục): app tìm đúng tệp
trên Mac qua mã Drive (`com.google.drivefs.item-id#S`) — không tải qua mạng, không cần mở chia sẻ công khai; chỉ thấy tệp của các
tài khoản Drive đã liên kết với Mac. Tệp vừa tải từ điện thoại cần vài phút để Drive trên Mac thấy.
Bước **Lấy video gốc về Mac** (`ap/lay_video.py`) tải tệp "chỉ trên mây" về `tap-<tên>/1-goc/` trước khi tạo dự án — app chạy nền phải tự xin
quyền kéo tệp về (`setiopolicy_np`), không thì macOS báo `Resource deadlock avoided` và để lại tệp 0 byte (lỗi 08/11/2026).
**Sửa skill khi đang có dự án:** bước CHƯA chạy tự dùng skill mới (lời nhắc, hồ sơ, script đọc lúc chạy). Bước đã chạy: bấm
**làm lại từ đây** — chạy lại bước đó và các bước sau; bước Claude nào đầu vào không đổi thì **dùng lại kết quả cũ, 0 token**
(`~/Movies/_app/<tên>/nho-claude/`; `APP_KHONG_NHO=1` để tắt). Phần hình (khung dựng, thư viện hình) được CHÉP vào dự án lúc tạo →
bấm **🔄 Cập nhật khung dựng** để lấy bản mới (giữ kịch bản, phụ đề, thông số; bản cũ cất ở `check/khung-truoc-<giờ>/`; đã render thì tự render lại).
**💬 Trao đổi (sổ góp ý `~/Movies/_app/<tên>/gop-y.json`):** mọi góp ý của David (ở cổng 1, cổng 2, hay sau khi video đã xong) được lưu
lại kèm câu trả lời của Claude ("đã sửa gì"). MỌI bước Claude từ bước được góp ý trở đi đều đọc sổ này → sửa tên/chính tả một lần là đúng
ở chữ trên màn hình, phụ đề (`sua_chu`) lẫn bài đăng; chữ đã sửa được coi là nguyên văn. Gõ góp ý mà bấm Duyệt → app hỏi lại, không để
mất góp ý. Video đã xong: ô góp ý + "Sửa video" / "Chỉ sửa bài đăng"; tập đã dọn file tạm thì dựng lại từ video gốc (giữ phiếu lọc).
**Nhiều việc cùng lúc:** tạo bao nhiêu việc cũng được. Bước nhẹ, bước Claude, cổng duyệt chạy song song; **bước nặng** (phiếu bước
`"nang": true`: chép lời, làm sạch, dò mặt, render, kiểm…) xếp hàng — mỗi lúc một việc (Mac M1 8 GB), việc sau hiện ⏳ và tự chạy khi tới lượt.
Bước ⏭/– "bỏ qua" = không cần cho video này (vd video ngang thì bỏ nâng khung), không phải đang chạy.
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

## Các loại video (công thức)
| Loại | Công thức | Claude làm | Cổng David |
|---|---|---|---|
| Làm video — 1 người nói (ngang/dọc, cả video cũ) | `lam-video` | lọc + cắt · kịch bản cảnh · phát hành | phiếu lọc · bản cuối |
| **Highlight** — clip dọc từ video dài (người nói) | `highlight` | tự chọn ý theo 4 câu · lớp phủ · kế hoạch đăng | các clip + kế hoạch đăng |
| **Podcast** — tiếng → toàn motion graphics | `podcast` | lọc · sân khấu + ý đang bàn + cảnh · phát hành (bìa không mặt) | phiếu lọc · bản cuối |
| **Ghép vlog** — nhiều clip → một video | `ghep-vlog` | xem từng clip + kế hoạch ghép · soát hình · phát hành | **kế hoạch ghép (trước render)** · bản cuối |
Highlight: chọn "Cắt highlight từ tập đã dựng bản dài" (dùng bản sạch + lời đã sửa) hoặc một video dài. Bản dài **không tự dọn** sau
cổng 2 (highlight cần bản sạch); highlight dọn cả tập ở cuối, hoặc bấm **🧹 Dọn tập**. Ghép vlog: chọn nhiều clip theo thứ tự ghép.
Nguồn podcast/highlight là podcast (đồ hoạ) → nhánh 7B của highlight chưa có trong app (làm bằng Claude Code).

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
- Highlight từ nguồn podcast (nhánh 7B): chưa có trong app.
- Học cách trình bày từ video mẫu: skill `hoc-video-mau` (sửa bộ skill, app tự theo vì dùng chung luật và thư viện hình).
- Đưa video lên Drive, đăng bài lên kênh: skill `dang-da-kenh` (cần trình duyệt, David duyệt từng bài).
- Đổi khung ngang → dọc dùng kế hoạch tự động của `reframe_plan.py`, chưa có bước Claude xem lại `tracks.jpg`.
