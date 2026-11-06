# Bộ skill dựng video của David

Thư mục này chứa **toàn bộ bộ skill dựng video** — 3 skill, mẫu dựng, nhạc nền, hiệu ứng tiếng, script. Sao lưu hoặc chép sang
máy khác chỉ cần chép cả thư mục `dung-video/`. Ở `~/.claude/skills/<tên>` chỉ là lối tắt trỏ về đây để Claude nhận lệnh `/<tên>`
(chép sang máy khác thì tạo lại lối tắt: `ln -s ~/.claude/skills/dung-video/<tên> ~/.claude/skills/<tên>` cho từng skill).

| Skill | Dùng khi | Ra gì |
|---|---|---|
| `video-style-edit/` — **1 video** | Gửi 1 video nói trước camera, nói "làm video này" | Giữ nguyên hình, phủ hiệu ứng + phụ đề |
| `video-style-edit/` — **ghép nhiều video** | Gửi từ 2 clip trở lên, nói "ghép thành 1 video" | Tự sắp mạch, trích dẫn clip minh hoạ; **duyệt kế hoạch trước khi render** |
| `podcast-style-edit/` — **podcast** | Gửi file tiếng/video và nói "podcast" | Toàn bộ khung là đồ hoạ chuyển động, có bìa 1 giây, thanh thời gian |
| `cat-highlight-video/` — **cắt highlight** | Gửi 1 video dài (YouTube, podcast đã dựng, hoặc thư mục dự án của nó), nói "cắt highlight" hoặc `/cat-highlight-video` | **các clip tự chọn ý, mỗi clip một ý trọn** **dọc 9:16** 30–60 giây, mỗi clip một khoảnh khắc mạnh, **cùng loại với video gốc**; thẻ tít mở đầu, phụ đề 1–3 chữ to mỗi nhịp, cắt cứng, lời trong clip nguyên văn; kèm lịch đăng, mô tả bài đăng + bình luận ghim |

Video ra ở `~/Movies/edit-<tên>/video-final.mp4` (hoặc `~/Movies/podcast-<tên>/`; highlight: chọn câu ở `~/Movies/highlight-<tên>/`, bản cuối mỗi clip ở `~/Movies/edit-hl-<tên>-A/`, `-B/`… hoặc `~/Movies/podcast-hl-<tên>-A/`…). Tiêu đề + thumbnail ở `phat-hanh/` của dự án. Muốn thêm thì nói kèm:
"xuất ngang/dọc", "làm thêm timeline CapCut", "không dùng ảnh", "thêm ảnh".

## Kiến trúc (2026-11-04) — sửa đúng một chỗ, không viết lại khung

```
dung-video/
├── nguyen-tac.md      7 điểm chung của 80 video thành công (hiếm đổi)
├── nhan-dien.md       đầu vào → chọn loại video (1 chỗ duy nhất)
├── luat-chung.md      luật nền: không bịa, lằn ranh, phụ đề, hình, nhận diện, phát hành
├── ho-so/             HÌNH MẪU → THAM SỐ cho từng loại (.json đọc bằng máy + .md giải thích + nhật ký)  ← đổi nhiều nhất
├── khoi/              18 khối: mỗi khối = README (luật, đầu vào/ra, sửa thì chạy lại gì) + code của nó
├── thu-vien-hinh/     MỘT bộ thành phần hình cho cả 4 loại (phụ đề, nhận diện, minh hoạ, màn chốt, thẻ cuối, màn kết…)
├── mau-chuan/         4 dự án mẫu + `kiem-mau.py` — chạy sau mỗi lần sửa để chắc không vỡ chỗ khác
├── video-style-edit/  công thức Làm video + Ghép vlog (references/multi-clip.md) — thứ tự khối + tiêu chí đạt
├── podcast-style-edit/  công thức Podcast
└── cat-highlight-video/ công thức Highlight
```

| Anh muốn | Sửa ở đâu |
|---|---|
| Học thêm hình mẫu → đổi một con số / một lựa chọn | `ho-so/<loai>.json` (+ 1 dòng nhật ký trong `.md`) |
| Đổi / thêm cách làm (kiểu phụ đề, kiểu cảnh minh hoạ, màn kết…) | đúng 1 khối (`khoi/NN-…`) — phần hình nằm ở `thu-vien-hinh/`, cả 4 loại tự dùng |
| Thêm loại video mới | 1 công thức (skill) + 1 hồ sơ, nhặt lại khối có sẵn |
| Sau mọi lần sửa | `python3 -I mau-chuan/kiem-mau.py` → ✓ giữ nguyên / ⚠ xem lại |

## Luật đã chốt (áp dụng mọi video)

**Một nguồn: [`luat-chung.md`](luat-chung.md)** — Claude đọc file này trước mọi skill. Tóm tắt:

- **Kim chỉ nam (2026-11-04):** người xem là trung tâm — kênh lớn đã chứng minh cách nào giữ người xem thì sao chép chuẩn đó.
- **Không bịa:** chữ trên video = lời người nói. Chỉ tiêu đề, thumbnail, thẻ tít highlight và câu màn chốt (video thường) được viết lời — đúng ý video.
- **Nhịp:** video nói trước camera + highlight cắt khoảng lặng ≥ 0,45 s và "ờ/ừm" (jump cut, phóng xen kẽ); vlog, podcast dài giữ tự nhiên.
  Muốn bản tự nhiên cho một video thì nói "giữ ngập ngừng".
- **Phụ đề:** video ngắn → 1–3 chữ to mỗi nhịp, ngang ngực; video dài → hộp tối đầy câu ở đáy.
- **2 trạng thái:** người + phụ đề, hoặc cảnh minh hoạ toàn màn hình (hình động + nhãn ≤ 3 chữ) + phụ đề — không chữ to đè người (trừ thẻ tít mở đầu).
- **Không che người nói**, không đè phụ đề, chữ tiếng Việt đủ dấu; minh hoạ mặc định là biểu tượng vẽ.
- **Phát hành (mọi video):** 3 tiêu đề + mốc khung bìa đề xuất. Ảnh thumbnail 1280×720 chỉ khi video **ngang** và **đăng YouTube** — Claude hỏi "có đăng YouTube không?" lúc đầu với mọi video xuất ngang.
- **Video dài đăng YouTube (> 3 phút):** màn kết 15–20 s chừa 2 video + nút đăng ký, chương YouTube, teaser 15–25 s câu đắt (> 10 phút).
- **Học từ 80 video Việt (2026-11-04):** báo cáo ở `*/references/hoc-tu-20-*-vn.md`, đề xuất + trạng thái ở `de-xuat-2026-11-04.md`.
- **Số liệu:** mỗi video có `so-lieu.md`; 7 ngày sau đăng gửi ảnh chụp số liệu để Claude rút ra một điều chỉnh có bằng chứng.

## Bộ nhận diện David (chốt 2026-11-04 — cả 4 loại: làm video · ghép vlog · podcast · highlight)
Xem bất kỳ video nào cũng phải nhận ra cùng một người làm. **Một nguồn:** `video-style-edit/assets/remotion-template/src/brand.json`
(tên kênh, tiếng ký hiệu, mức nhạc) + bảng màu/font (`theme.js` = `montage-template/src/brand.js`) + `subStyle.js` + `cta.js` + `Icons.jsx`.
- **Dấu góc trên** ● DAVID │ chủ đề — mọi video (BrandMark / Hud; podcast ở đầu sân khấu). Chủ đề: `project.topic` (1 video),
  `show.name` (vlog), tên chương trình (podcast), tên tập gốc (highlight).
- **Khuôn tiêu đề**: dòng nhỏ cam → gạch cam → chữ cô đặc in hoa trắng, dòng nhấn cam (Hook / Title).
- **Âm thanh**: tiếng ký hiệu `sting.wav` đúng lúc hiện tiêu đề mở đầu; nhạc kênh (`cat-highlight-video/assets/music`) dưới lời —
  vlog thấp hơn giọng 20 LU, 1 video / podcast rất nhỏ 22 LU (tự đo giọng); giọng cân −20 LUFS; bản cuối −14 LUFS.
- **Khuôn kết**: màn chốt kêu gọi (cta.js) → thẻ cuối: gạch cam + chủ đề + DAVID (highlight: tên tập gốc + nút phát).
- Biểu tượng nét vẽ dần dùng chung (Icons.jsx) cho cảnh minh hoạ ở mọi loại.

## Bên trong mỗi skill

- `luat-chung.md` (thư mục gốc): luật chung cả bộ · `so-lieu-mau.md`: mẫu ghi số liệu sau đăng.
- `SKILL.md`: quy trình từng bước + luật riêng của skill.
- `references/changelog.md`: sổ quyết định của bạn theo ngày, kèm lý do.
- `references/gotchas.md`: các lỗi đã gặp và cách tránh.
- `references/scene-design.md`, `multi-clip.md`, `podcast-design.md`: các loại cảnh, cách ghép, cách thiết kế podcast.
- Highlight: `cat-highlight-video/scripts/` (`new_highlight.sh`, `loud_check.py`, `cut_highlight.py`, `hl_edl.py`, `hl_apply.py`) — chọn, soát, cắt câu, viết kịch bản dựng; dựng qua 2 skill kia. `cat-highlight-video/assets/music/` — 4 bài nhạc nền của kênh (xem README trong đó).
- `scripts/`: công cụ (làm sạch, dò mặt, nâng khung, phụ đề, render, CapCut, `thumbnail.sh` ảnh thumbnail…).
- `assets/`: mẫu Remotion cho video đơn, video ghép (cũng là khung game show của highlight) và podcast, cộng tiếng "ting", "vút tua".

Công cụ phụ (mô hình Whisper, bộ dò mặt, môi trường Python) nằm ở `~/.cache/video-style-edit` và `~/whisper-models` — đừng xoá.
