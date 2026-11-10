# Bộ skill dựng video của David

Thư mục này chứa **toàn bộ bộ skill dựng video** — 3 skill, mẫu dựng, nhạc nền, hiệu ứng tiếng, script. Sao lưu hoặc chép sang
máy khác chỉ cần chép cả thư mục `dung-video/`. Ở `~/.claude/skills/<tên>` chỉ là lối tắt trỏ về đây để Claude nhận lệnh `/<tên>`
(chép sang máy khác thì tạo lại lối tắt: `ln -s ~/.claude/skills/dung-video/<tên> ~/.claude/skills/<tên>` cho từng skill).

| Skill | Dùng khi | Ra gì |
|---|---|---|
| `video-style-edit/` — **1 video** | Gửi 1 video nói trước camera, nói "làm video này" | Giữ nguyên hình, phủ hiệu ứng + phụ đề |
| `video-style-edit/` — **ghép nhiều video** | Gửi từ 2 clip trở lên, nói "ghép thành 1 video" | Tự sắp mạch, trích dẫn clip minh hoạ; **duyệt kế hoạch trước khi render** |
| `podcast-style-edit/` — **podcast** | Gửi file tiếng/video và nói "podcast" | Toàn bộ khung là đồ hoạ chuyển động, thanh thời gian |
| `cat-highlight-video/` — **cắt highlight** | Gửi 1 video dài (YouTube, podcast đã dựng, hoặc thư mục dự án của nó), nói "cắt highlight" hoặc `/cat-highlight-video` | Các clip **dọc 9:16** tự chọn ý, mỗi clip một ý trọn, **cùng loại với video gốc**; thẻ tít nguyên văn, phụ đề cụm 5–8 chữ, cắt cứng; kèm lịch đăng, mô tả + bình luận ghim |
| `hoc-video-mau/` — **học mẫu** | Gửi video mẫu, nói "học cái này" | Phiếu học để duyệt, rồi thêm vào kho trình bày |
| `dang-da-kenh/` — **trọn gói** | Gửi tài nguyên mới (thường không kèm yêu cầu) | Lọc → dựng → bài đăng → hẹn giờ → số liệu |

Mọi thứ của một tập nằm chung `~/Movies/tap-<tên>/` (xem `video-style-edit/scripts/noi_luu.sh`): gốc ở `1-goc/`, bản dài ở
`2-ban-dai/video-final.mp4`, highlight: chọn câu ở `3-highlight/`, bản cuối mỗi clip ở `3-highlight/clip-A/`, `clip-B/`…; vlog ở
`~/Movies/vlog/<tên>/`. Bản dài và highlight của cùng tập phải dùng **cùng một `<tên>`**. Tiêu đề + thumbnail ở `phat-hanh/` của dự
án. Muốn thêm thì nói kèm: "xuất ngang/dọc", "không dùng ảnh", "thêm ảnh", "giữ ngập ngừng". Không làm bản cho CapCut/DaVinci; David
chốt bản cuối thì dọn file tạm (`don_tap.py`, khối 17).

## Kiến trúc — sửa đúng một chỗ, không viết lại khung

```
dung-video/
├── nguyen-tac.md      7 điểm chung của 80 video thành công (hiếm đổi)
├── nhan-dien.md       đầu vào → chọn loại video (1 chỗ duy nhất)
├── luat-chung.md      luật nền: kim chỉ nam, nội dung, nhịp, phụ đề, hình, lời kêu gọi, phát hành
├── ho-so/             HÌNH MẪU → THAM SỐ cho từng loại (.json đọc bằng máy + .md giải thích + nhật ký)  ← đổi nhiều nhất
├── khoi/              các khối 00–20: mỗi khối = README (luật, đầu vào/ra, sửa thì chạy lại gì) + code của nó
├── thu-vien-hinh/     MỘT bộ thành phần hình cho cả 4 loại + bộ nhận diện chung (nhan-dien-chung.md)
├── trinh-bay/         khung gốc để học video mẫu + kho bố cục, âm thanh, nguồn học
├── mau-chuan/         dự án mẫu + `kiem-mau.py` — chạy sau mỗi lần sửa để chắc không vỡ chỗ khác
├── video-style-edit/  công thức Làm video + Ghép vlog (references/multi-clip.md) — thứ tự khối + tiêu chí đạt
├── podcast-style-edit/  công thức Podcast
├── cat-highlight-video/ công thức Highlight
├── hoc-video-mau/     cửa vào học video mẫu
└── dang-da-kenh/      quy trình trọn gói từ tài nguyên tới đăng
```

| Anh muốn | Sửa ở đâu |
|---|---|
| Học thêm hình mẫu → đổi một con số / một lựa chọn | `ho-so/<loai>.json` (+ 1 dòng nhật ký trong `.md`) |
| Đổi / thêm cách làm (kiểu phụ đề, kiểu cảnh minh hoạ, màn kết…) | đúng 1 khối (`khoi/NN-…`) — phần hình nằm ở `thu-vien-hinh/`, cả 4 loại tự dùng |
| Đổi luật dùng chung | `luat-chung.md` (một luật một nhà, sửa thẳng câu cũ) |
| Thêm loại video mới | 1 công thức (skill) + 1 hồ sơ, nhặt lại khối có sẵn |
| Sau mọi lần sửa | `python3 -I mau-chuan/kiem-mau.py` → ✓ giữ nguyên / ⚠ xem lại |

Luật áp dụng mọi video: **[`luat-chung.md`](luat-chung.md)**. Bộ nhận diện: [`thu-vien-hinh/nhan-dien-chung.md`](thu-vien-hinh/nhan-dien-chung.md).

## Bên trong mỗi skill

- `SKILL.md`: quy trình từng bước + luật riêng của skill.
- `references/changelog.md`: sổ quyết định của David theo ngày, kèm lý do (không đọc lúc làm việc).
- `references/gotchas.md`: các lỗi đã gặp và cách tránh.
- `references/scene-design.md`, `multi-clip.md`, `podcast-design.md`: các loại cảnh, cách ghép, cách thiết kế podcast.
- `references/hoc-tu-*`: báo cáo học hình mẫu (kho, không phải luật).
- Highlight: `cat-highlight-video/scripts/` (`new_highlight.sh`, `loud_check.py`, `cut_highlight.py`, `hl_edl.py`, `hl_apply.py`) —
  chọn, soát, cắt câu, viết kịch bản dựng; dựng qua 2 skill kia. `cat-highlight-video/assets/music/` — kho nhạc kênh (README trong đó).
- `scripts/`: công cụ (làm sạch, dò mặt, nâng khung, phụ đề, render, `thumbnail.sh`…).
- `assets/`: mẫu Remotion cho video đơn, video ghép (cũng là khung của highlight người nói) và podcast, cộng tiếng "ting", "vút tua".

Công cụ phụ (mô hình Whisper, bộ dò mặt, môi trường Python) nằm ở `~/.cache/video-style-edit` và `~/whisper-models` — đừng xoá.
