# Bộ skill dựng video của David

Thư mục này chứa **toàn bộ bộ skill dựng video** — 3 skill, mẫu dựng, nhạc nền, hiệu ứng tiếng, script. Sao lưu hoặc chép sang
máy khác chỉ cần chép cả thư mục `san-xuat-video/`. Ở `~/.claude/skills/<tên>` chỉ là lối tắt trỏ về đây để Claude nhận lệnh `/<tên>`
(chép sang máy khác thì tạo lại lối tắt: `ln -s ~/.claude/skills/san-xuat-video/<tên> ~/.claude/skills/<tên>` cho từng skill).

| Skill | Dùng khi | Ra gì |
|---|---|---|
| `dung-video-theo-phong-cach/` — **1 video** | Gửi 1 video nói trước camera, nói "làm video này" | Giữ nguyên hình, phủ hiệu ứng + phụ đề |
| `dung-video-theo-phong-cach/` — **ghép nhiều video** | Gửi từ 2 clip trở lên, nói "ghép thành 1 video" | Tự sắp mạch, trích dẫn clip minh hoạ; **duyệt kế hoạch trước khi render** |
| `dung-podcast/` — **podcast** | Gửi file tiếng/video và nói "podcast" | Toàn bộ khung là đồ hoạ chuyển động, thanh thời gian |
| `cat-doan-noi-bat/` — **cắt highlight** | Gửi 1 video dài (YouTube, podcast đã dựng, hoặc thư mục dự án của nó), nói "cắt highlight" hoặc `/cat-doan-noi-bat` | Các clip **dọc 9:16** tự chọn ý, mỗi clip một ý trọn, **cùng loại với video gốc**; thẻ tít nguyên văn, phụ đề cụm 5–8 chữ, cắt cứng; kèm lịch đăng, mô tả + bình luận ghim |
| `phan-tich-video-mau/` — **học mẫu** | Gửi video mẫu, nói "học cái này" | Phiếu học để duyệt, rồi thêm vào kho trình bày |
| `phan-phoi-da-kenh/` — **trọn gói** | Gửi tài nguyên mới (thường không kèm yêu cầu) | Lọc → dựng → bài đăng → hẹn giờ → số liệu |

Mọi thứ của một tập nằm chung `~/Movies/tap-<tên>/` (xem `dung-video-theo-phong-cach/scripts/noi-luu.sh`): gốc ở `1-goc/`, bản dài ở
`2-ban-day-du/video-hoan-chinh.mp4`, highlight: chọn câu ở `3-doan-noi-bat/`, bản cuối mỗi clip ở `3-doan-noi-bat/clip-A/`, `clip-B/`…; vlog ở
`~/Movies/vlog/<tên>/`. Bản dài và highlight của cùng tập phải dùng **cùng một `<tên>`**. Tiêu đề + thumbnail ở `phat-hanh/` của dự
án. Muốn thêm thì nói kèm: "xuất ngang/dọc", "không dùng ảnh", "thêm ảnh", "giữ ngập ngừng". Không làm bản cho CapCut/DaVinci; David
chốt bản cuối thì dọn file tạm rồi đưa tập lên Drive, xoá trên Mac (`don-tap.py` → `luu-drive.sh`, khối 17).

## Kiến trúc — sửa đúng một chỗ, không viết lại khung

```
san-xuat-video/
├── nguyen-tac.md      7 điểm chung của 80 video thành công (hiếm đổi)
├── nhan-dien-thuong-hieu.md       đầu vào → chọn loại video (1 chỗ duy nhất)
├── quy-tac-chung.md      luật nền: kim chỉ nam, nội dung, nhịp, phụ đề, hình, lời kêu gọi, phát hành
├── ho-so-thuong-hieu/             HÌNH MẪU → THAM SỐ cho từng loại (.json đọc bằng máy + .md giải thích + nhật ký)  ← đổi nhiều nhất
├── mo-dun/              các khối 00–20: mỗi khối = README (luật, đầu vào/ra, sửa thì chạy lại gì) + code của nó
├── thu-vien-tai-nguyen/     MỘT bộ thành phần hình cho cả 4 loại + bộ nhận diện chung (nhan-dien-chung.md)
├── thiet-ke-bo-cuc/         khung gốc để học video mẫu + kho bố cục, âm thanh, nguồn học
├── mau-chuan/         dự án mẫu + `kiem-mau.py` — chạy sau mỗi lần sửa để chắc không vỡ chỗ khác
├── dung-video-theo-phong-cach/  công thức Làm video + Ghép vlog (references/nhieu-doan-video.md) — thứ tự khối + tiêu chí đạt
├── dung-podcast/  công thức Podcast
├── cat-doan-noi-bat/ công thức Highlight
├── phan-tich-video-mau/     cửa vào học video mẫu
└── phan-phoi-da-kenh/      quy trình trọn gói từ tài nguyên tới đăng
```

| Anh muốn | Sửa ở đâu |
|---|---|
| Học thêm hình mẫu → đổi một con số / một lựa chọn | `ho-so-thuong-hieu/<loai>.json` (+ 1 dòng nhật ký trong `.md`) |
| Đổi / thêm cách làm (kiểu phụ đề, kiểu cảnh minh hoạ, màn kết…) | đúng 1 khối (`mo-dun/NN-…`) — phần hình nằm ở `thu-vien-tai-nguyen/`, cả 4 loại tự dùng |
| Đổi luật dùng chung | `quy-tac-chung.md` (một luật một nhà, sửa thẳng câu cũ) |
| Thêm loại video mới | 1 công thức (skill) + 1 hồ sơ, nhặt lại khối có sẵn |
| Sau mọi lần sửa | `python3 -I mau-chuan/kiem-mau.py` → ✓ giữ nguyên / ⚠ xem lại |

Luật áp dụng mọi video: **[`quy-tac-chung.md`](quy-tac-chung.md)**. Bộ nhận diện: [`thu-vien-tai-nguyen/nhan-dien-chung.md`](thu-vien-tai-nguyen/nhan-dien-chung.md).

## Bên trong mỗi skill

- `SKILL.md`: quy trình từng bước + luật riêng của skill.
- `references/nhat-ky-thay-doi.md`: sổ quyết định của David theo ngày, kèm lý do (không đọc lúc làm việc).
- `references/loi-thuong-gap.md`: các lỗi đã gặp và cách tránh.
- `references/thiet-ke-canh.md`, `nhieu-doan-video.md`, `thiet-ke-podcast.md`: các loại cảnh, cách ghép, cách thiết kế podcast.
- `references/hoc-tu-*`: báo cáo học hình mẫu (kho, không phải luật).
- Highlight: `cat-doan-noi-bat/scripts/` (`tao-doan-noi-bat.sh`, `kiem-am-luong.py`, `cat-doan-noi-bat.py`, `danh-sach-cat-doan-noi-bat.py`, `ap-dung-doan-noi-bat.py`) —
  chọn, soát, cắt câu, viết kịch bản dựng; dựng qua 2 skill kia. `cat-doan-noi-bat/assets/nhac/` — kho nhạc kênh (README trong đó).
- `scripts/`: công cụ (làm sạch, dò mặt, nâng khung, phụ đề, render, `anh-thu-nho.sh`…).
- `assets/`: mẫu Remotion cho video đơn, video ghép (cũng là khung của highlight người nói) và podcast, cộng tiếng "ting", "vút tua".

Công cụ phụ (mô hình Whisper, bộ dò mặt, môi trường Python) nằm ở `~/.cache/dung-video-theo-phong-cach` và `~/whisper-models` — đừng xoá.
