---
name: video-style-edit
description: Tự động dựng video người dùng tự quay thành bản đăng được ngay lên Reels/TikTok/Shorts/YouTube, theo phong cách một video mẫu (hoặc một dự án cũ). Hai chế độ tự chọn theo đầu vào — (1) MỘT video nói trước camera (talking-head) → tự làm sạch trước (cắt thừa đầu/cuối, câu nói lại, khoảng lặng và tiếng đệm kiểu jump cut của kênh lớn; sửa video lộn ngược, nằm ngang, lật gương) rồi phủ motion graphics, thẻ thông tin, mở đầu 3 giây có tiêu đề nội dung chính, chữ to nhấn mạnh, cảnh hoạt hình toàn màn hình, minh hoạ bằng biểu tượng vẽ (ảnh giấy phép mở chỉ khi cần địa danh/sản phẩm thật), (gói timeline DaVinci chỉ làm khi người dùng yêu cầu); đổi khung khi cần — gốc dọc xuất ngang (video giữa, hai bên chữ theo phong cách) hoặc gốc ngang xuất dọc (tự cắt khung bám người đang nói); (2) NHIỀU video gốc (từ 2 clip trở lên, hoặc cảnh quay sự kiện/vlog) → chọn cảnh hay, cắt bỏ đoạn hỏng, ghép thành vlog kiểu game show/chương trình thực tế có teaser, tiêu đề, chia vòng, zoom dồn, đóng băng hình, phát lại chậm, phụ đề, hiệu ứng âm thanh và nhạc nền. Mọi chế độ kết bằng bước phát hành: 3 tiêu đề + mốc khung bìa + ảnh thumbnail khi video ngang đăng YouTube + mẫu số liệu sau đăng. Dùng skill này bất cứ khi nào người dùng đưa một hay nhiều video gốc (thường kèm video/ảnh mẫu phong cách) và muốn edit, dựng, ghép, nối video, làm vlog, thêm hiệu ứng, thêm chữ, thêm ảnh minh hoạ, làm "giống video này", "theo style này", "edit như mẫu", "ghép mấy video này", "làm như game show/chương trình", làm motion graphics/animation cho video, kể cả khi họ chỉ gửi vài file video mà không nói rõ — hoặc khi họ nói "edit video", "dựng video", "ghép video", "làm video như mẫu", "/video-style-edit".
---
# Dựng video theo phong cách mẫu

Người dùng đưa **video gốc** (họ tự quay, thường dọc 9:16, nói tiếng Việt) và **video mẫu** (phong cách họ muốn).
Mục tiêu: trả về một video **đăng được ngay**, giống tinh thần video mẫu, khớp từng câu nói — không cần mở CapCut/DaVinci.
**Mặc định KHÔNG làm gói timeline cho app dựng** (DaVinci/CapCut): không `build_timeline.py`, không `HUONG-DAN.md`,
không nhắc tới DaVinci trong báo cáo. Chỉ làm khi người dùng yêu cầu (xem "Timeline cho app dựng" ở cuối).
Thư mục `davinci/media/` vẫn là nơi chứa video nguồn và clip hiệu ứng trung gian — chỉ là tên thư mục.

Cách làm cốt lõi: không vẽ tay, mà **viết code hoạt hình** (Remotion/React) theo một bộ "token" phong cách rút ra từ
video mẫu, gắn từng cảnh vào mốc thời gian lấy từ transcript Whisper, render ra clip nền trong suốt rồi ghép lên video gốc.

Người dùng muốn **đưa 2 video là xong**. Vì vậy chạy hết quy trình một mạch, không dừng hỏi duyệt từng bước;
chỉ dừng khi bị chặn thật (thiếu công cụ cần mật khẩu, tải mô hình 1,5 GB lần đầu, không đọc được file).
Sau khi giao bản cuối, nhận góp ý và sửa đúng cảnh được nêu.

## Đọc trước (lần đầu trong phiên)
`../nguyen-tac.md` (7 điểm chung của hình mẫu) · `../luat-chung.md` (luật nền) · `../nhan-dien.md` (chọn loại) · hồ sơ `../ho-so/lam-video (hoặc ghep-vlog).md`
(hình mẫu chính + tham số — **con số lấy ở đây, không ghi cứng**) · `../khoi/README.md` (kho khối). Skill này là **CÔNG THỨC**: thứ tự
khối + quyết định riêng của loại + tiêu chí đạt. Cách làm từng bước nằm trong README của khối; sửa cách làm → sửa khối, không sửa công thức.

## Luật (kiểm lại trước khi giao)

**Đọc `../luat-chung.md` trước** — kim chỉ nam "người xem là trung tâm, sao chép chuẩn kênh lớn", nội dung không bịa, lằn ranh,
nhịp, phụ đề, hình, bộ nhận diện, lời kêu gọi, phát hành, vòng số liệu. Dưới đây chỉ là luật RIÊNG của skill này.

1. **Tối giản:** một màn = một ý, một hình, một câu; ~1 hiệu ứng / 15–20 s ở video dài (video ngắn ≤ 90 s: dày hơn, ~1 / 5–8 s);
   chữ to ≤ 3–4 lần / video; giữa hai cảnh chữ ≥ 5 s chỉ có người nói + phụ đề.
2. **Mở đầu `hook` 0 → ~3 s** — **TẠM BỎ mặc định (David 2026-11-07, khối 06): chỉ làm khi David yêu cầu, chữ nguyên văn.** Khi làm: ý chính cả video, trích lời. `project.js` ghi `topic: '<CHỦ ĐỀ>'` (≤ 3 chữ, trích lời) cho dấu góc + thẻ cuối.
3. **2 TRẠNG THÁI** (David chốt 2026-11-04, khối 07): người + phụ đề, hoặc cảnh **`illus`** toàn màn hình (hình động + nhãn ≤ 3 chữ)
   + phụ đề — mỗi ý cần hình là một cảnh `illus` 3–5 s. Không chữ to / thẻ / câu trích dài đè người (khung dựng tự đổi lớp cũ sang
   toàn màn hình, bỏ câu trích). Mặt người nói hiện ≥ 60%.
   **Trạng thái thứ 3 — điểm nhấn trên người** (`nhan`, David chốt 2026-11-07): zoom dồn / làm tối viền / chữ nhấn hay biểu tượng cạnh mặt
   ở câu đắt, 2–5 s, không che mặt. Mọi video đều có motion graphics trộn nhiều loại — "dựng nhẹ" vẫn có (~8–10 điểm nhấn / 4 phút, ~4 trên người). Khối 07.
4. **Màn hành động** (`action`, 3–5 s, biểu tượng + tick + `label` ≤ 4 chữ cụm việc nguyên văn) đúng lúc người nói giao việc (1–2 câu cụ thể nhất). **Màn chốt** (`cta`, ~4 s cuối mọi
   video): video lùi vào khung bo góc, câu chốt = **nguyên văn câu David nói cuối video** (David 2026-11-07; luat-chung 1). **Kênh thương hiệu David: theo luật kênh (khối 08 — Không / Gợi mở → `comment` với
   "Vấn đề" / "Kết quả", Mời → `moi` "nhắn mình một chữ 'gỡ'")**; video khác chọn MỘT `kind` — quan điểm/kiến thức → `comment`
   với câu hỏi dễ trả lời; mẹo nhiều bước → `save`; hành trình nhiều kỳ → `follow`; hữu ích cho người thân → `share`. Không bịa,
   không hứa "tập sau" khi người nói không hẹn. Ghi câu + lý do vào `ke-hoach-canh.md`.
   Ví dụ: "Bạn hay tắm nắng lúc mấy giờ? **Kể David nghe** nhé!" (comment) · "**Lưu lại** để mai thử đi bộ kiểu Haruku cùng David!" (save).
5. **Làm sạch:** video > 3 phút **không cắt gì** (luat-chung 2); video ≤ 3 phút: cắt thừa đầu/cuối, câu nói lại (giữ lần sau cùng), **khoảng lặng** ≥ 0,45 s + tiếng đệm; sửa video
   lộn ngược/nằm ngang/lật gương; giữ vẫy tay chào cuối.
6. **Lớp phủ thu 78%, không che mặt** (`face_place.sh`); nhân vật nằm thấp → nâng khung ≤ 400 px (`lift.py`).
7. Mặc định KHÔNG làm timeline DaVinci/CapCut (chỉ khi được yêu cầu — mục cuối file).
8. **Học từ 20 video nói trước camera Việt** (`references/hoc-tu-20-video-noi-truoc-camera-vn.md`, David duyệt 2026-11-04):
   - **Nhãn số danh sách** (`listItem` {n, of?, text}): người nói đếm ≥ 3 ý → mỗi ý một nhãn đúng lúc nói, 2,5–4 s, text nguyên văn
     cụm việc (thay `kinetic` cho các ý đếm).
   - **Thẻ tóm tắt để lưu**: video danh sách / hướng dẫn → `card` variant `steps` toàn cảnh 3–4 s ngay trước màn chốt liệt kê các ý
     (nguyên văn, bỏ bớt chữ), màn chốt `kind: 'save'`.
   - **Thẻ chương + chương YouTube** cho video dài có ý lớn: `CHAPTERS` trong scenes.js (mốc + tên trích lời) → `chapters.py`.
   - Video ngắn: thẻ tít 0–2 s là câu hỏi / lời hứa (hook) — chuẩn 5/10 video ngắn Việt.

## Chọn chế độ (làm đầu tiên)

| Đầu vào | Chế độ | Làm theo |
|---|---|---|
| **1 video gốc** có người nói trước camera | Phủ đồ hoạ lên video gốc (giữ nguyên hình) | Phần "Quy trình" bên dưới |
| **Từ 2 video gốc trở lên**, hoặc 1 clip quay sự kiện/vlog không phải nói trước camera | **Ghép nhiều clip** (game show, giải thích, vlog…): tự sắp mạch nội dung, clip minh hoạ được **trích dẫn đúng câu nói** liên quan; **duyệt kế hoạch trước khi render** | `references/multi-clip.md` (bỏ qua phần Quy trình dưới) |

Video mẫu (nếu có) là phong cách, không tính vào số video gốc. Người dùng gửi cả thư mục → dùng mọi video trong đó
làm video gốc theo thứ tự tên file (chế độ ghép); chỉ hỏi lại khi không rõ file nào là mẫu.
Muốn "giống video trước"/cùng phong cách với một dự án cũ → lấy token phong cách từ `~/Movies/tap-<tên>/2-ban-dai/motion/src`
của dự án đó (áp cho cả hai chế độ).

## Đầu vào

- **Video gốc**: đường dẫn file (chế độ ghép: nhiều file).
- **Video mẫu**: tốt nhất là file video (hoặc bản quay màn hình). Nếu người dùng chỉ đưa link YouTube/TikTok,
  không tải video từ nền tảng (vi phạm điều khoản); nhờ họ gửi file hoặc 4–8 ảnh chụp màn hình các cảnh tiêu biểu.
  Ảnh chụp màn hình cũng đủ để rút phong cách.
- Không có mẫu: dùng phong cách mặc định của template (thẻ tối, nhấn cam, chữ cô đặc in hoa) — đã được duyệt.
- Yêu cầu thêm của người dùng (thông điệp chính, tên, chỗ muốn nhấn) luôn ưu tiên hơn suy luận.
- **Không đưa ghi chú kỹ thuật lên video**: không nhãn tốc độ (×1,6, ×0,5, "tua nhanh", "slow-mo", "xem chậm"), không
  thông số kỹ thuật. Hiệu ứng tốc độ vẫn dùng, chỉ không chú thích; chữ trên màn hình chỉ dành cho nội dung.
- **Khung xuất**: mặc định cùng khung video gốc. Chỉ đổi khi người dùng nói ("xuất ngang cho YouTube",
  "xuất dọc cho TikTok"):

| Gốc → xuất | Cách làm | Ở đâu |
|---|---|---|
| dọc → dọc, ngang → ngang | Bình thường | — |
| **dọc → ngang** (pillar) | Giữ nguyên video dọc, không cắt/kéo giãn, đặt giữa khung 1920×1080. Hai bên là nền + chữ cùng phong cách: **trái** = chủ đề, người nói, từ khoá của ý đang nói; **phải** = danh sách ý tích dần theo lời. Thẻ/chữ to/tên chuyển ra ô ở cột trái (không đè lên mặt); cảnh toàn màn hình thay video ở cột giữa | Khối 04, 07, 17 |
| **ngang → dọc** (reframe) | Cắt khung 9:16 bám theo **người đang nói**, nhảy cắt sang người kia khi lời thoại chuyển (không chia đôi màn hình). **Giữ nguyên thời lượng và mọi lời nói** (vẫn làm sạch ở bước 3a). Cảnh không có người hoặc phải thấy cả khung (slide, chữ trên màn hình, cảnh rộng) → `wide`: cả khung ngang đặt giữa trên nền mờ | Khối 04 |

## Công thức — Làm video (1 video nói trước camera) · hồ sơ `lam-video`
| # | Bước | Khối | Lệnh chính |
|---|---|---|---|
| 1 | Môi trường | [01](../khoi/01-chep-loi/README.md) | `zsh $SKILL/scripts/check_env.sh` |
| 2 | Tạo dự án | — | `zsh $SKILL/scripts/new_project.sh "<video gốc>" "<video mẫu>" <tên>` (mục dưới) |
| 3 | Làm sạch (video > 3 phút không cắt gì, chỉ sửa chiều hình; ≤ 3 phút: cắt thừa, nói lại, khoảng lặng theo hồ sơ) | [02](../khoi/02-lam-sach/README.md) | `clean_analyze.sh` → sửa cuts.json → `clean_apply.py` |
| 4 | Đổi khung (nếu cần) + nâng khung | [04](../khoi/04-khung-hinh/README.md) | `reframe_*` / `set_output.py` · `lift.py "$P" apply` |
| 5 | Chép lời + hiểu video | [01](../khoi/01-chep-loi/README.md) | `analyze_video.sh` |
| 6 | Phụ đề | [03](../khoi/03-phu-de/README.md) | `captions.py` → sửa từng dòng |
| 7 | Phong cách (video mẫu / dự án cũ) · **tuyến nội dung → nhạc** (`project.tuyen`, bắt buộc, ghi sau clean_apply) | [10](../khoi/10-nhan-dien/README.md) · [09](../khoi/09-am-thanh/README.md) | style.md → theme.js |
| 8 | Kịch bản: thẻ tít mở · cảnh minh hoạ 2 trạng thái · màn chốt | [06](../khoi/06-mo-dau/README.md) · [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) | scenes.js + ke-hoach-canh.md |
| 9 | Tránh che người | [05](../khoi/05-tranh-che-nguoi/README.md) | `face_place.sh` |
| 10 | Chụp thử → render → kiểm bản cuối (+ âm thanh) | [17](../khoi/17-dung-kiem-tra/README.md) · [09](../khoi/09-am-thanh/README.md) | `preview.mjs` → `render.mjs` → `render_preview.py` → `check_frames.sh` |
| 11 | Phát hành: tiêu đề, khung bìa, màn kết/chương/teaser (YouTube > 3 phút), thumbnail (ngang), số liệu | [15](../khoi/15-phat-hanh/README.md) · [08](../khoi/08-ket-thuc/README.md) · [14](../khoi/14-thumbnail/README.md) · [16](../khoi/16-so-lieu/README.md) | `teaser.py` · `chapters.py` · `thumbnail.sh` |
| — | Timeline DaVinci / CapCut (chỉ khi được yêu cầu) | [18](../khoi/18-xuat-app-dung/README.md) | `build_timeline.py` / `build_capcut.py` |

**Ghép vlog** (≥ 2 clip): công thức ở `references/multi-clip.md` (khối 11) · hồ sơ `ghep-vlog`.

### 2. Tạo dự án

```bash
zsh $SKILL/scripts/new_project.sh "<video gốc>" "<video mẫu>" <tên-ngắn>
```
Tạo `~/Movies/tap-<tên>/2-ban-dai/` (gốc tự đặt vào `tap-<tên>/1-goc/`; tên `vlog-…` → `~/Movies/vlog/<tên>/`) với cấu trúc chuẩn (xem cuối file), chép video, chép template Remotion vào `motion/`,
điền thông số video vào `motion/src/project.js`, cài gói npm. Dòng cuối là đường dẫn dự án `$P`.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| cuts.json (làm sạch) | clean_apply.py → lift.py apply → analyze_video.sh → captions.py → dời mốc scenes.js → face_place.sh → render |
| scenes.js (mốc / loại cảnh) | face_place.sh → `node render.mjs <id>` → render_preview.py |
| captions.js | `node render.mjs phu-de` → render_preview.py |
| theme.js / brand | render lại tất cả |
| project.js (topic, ytEnd, schedule) — ghi lại SAU clean_apply (nó viết đè project.js) | `node render.mjs the-cuoi` → render_preview.py |
| video-final (teaser) | chapters.py |
| hồ sơ lam-video | chạy lại khối dùng khoá đó (xem bảng khoá trong ho-so/lam-video.md) |

## Tiêu chí đạt (soát trước khi giao)
- 0–3 s có thẻ tít / hook đúng ý chính · người + phụ đề / cảnh minh hoạ toàn màn hình / điểm nhấn trên người `nhan` (không che mặt); không chữ to tự do đè người · có trộn nhiều loại điểm nhấn
- Mặt người nói hiện ≥ `mat_hien_min` · phụ đề đúng chữ, không bị đè · tiếng Việt đủ dấu · không gì lọt vùng đỏ
- Màn chốt + thẻ cuối · (YouTube > 3 phút) màn kết, chương, teaser > 10 phút · thumbnail nếu ngang · phat-hanh.md + so-lieu.md
- Âm lượng ±0,5 dB, tiếng rè ±1 dB so nguồn; thời lượng đúng

## Sửa theo góp ý

Người dùng thường nói kiểu "cảnh 2:08 chữ to quá", "đổi hình thợ hồ", "bỏ cảnh AI". Sửa đúng chỗ trong
`scenes.js`/component/ảnh → đổi mốc thì chạy lại `python3 -I $SKILL/scripts/face_place.py "$P"` → `node render.mjs <id>` (chỉ cảnh đó) → `render_preview.py` → kiểm tra khung quanh mốc đó.
Đổi phong cách toàn bộ → sửa `theme.js` rồi render lại tất cả. Đã có timeline cho app dựng → chạy lại `build_timeline.py`.
"Giữ lại đoạn bị cắt"/"cắt thêm đoạn X" → đổi mốc người dùng nói (mốc bản cuối) sang mốc thô bằng `segments.json`,
sửa `cuts.json`, lưu bản `segments.json` cũ, chạy `clean_apply.py`, rồi dời mốc mọi cảnh (`start`, `end`, `at`…)
theo bảng mới (thô → sạch). Chỉ render lại cảnh có mối đổi nằm **bên trong** nó (cảnh chỉ bị dời nguyên khối thì
clip không đổi), rồi `render_preview.py` (+ `build_timeline.py` nếu đã làm timeline).

## Cấu trúc dự án

```
~/Movies/tap-<tên>/2-ban-dai/
├── davinci/                 # tên lịch sử; chỉ thành "gói DaVinci" khi người dùng yêu cầu timeline
│   ├── media/               # video_goc.mp4 (bản sạch), video_goc_raw.* (bản thô), <id>.mov (ProRes 4444 alpha), khung_an_toan.png
│   └── timeline.fcpxml · HUONG-DAN.md   # chỉ khi được yêu cầu
├── motion/                  # dự án Remotion (src/scenes.js, theme.js, fonts.js, components/, public/photos/)
├── images/                  # queries.json, candidates.json, thumbs/, sheets/, picks.json, credits.tsv
├── ref/                     # video mẫu + phân tích
├── check/                   # khung kiểm tra; reframe/ = plan.json, shots.jpg (ngang → dọc); clean/ = cuts.json, cuts.md, segments.json (làm sạch)
├── phat-hanh/              # phat-hanh.md (tiêu đề, mô tả) · thumb-1.jpg · thumb-2.jpg (+ @160 xem cỡ điện thoại)
├── style.md · ke-hoach-canh.md · nguon-anh.txt (nguồn ảnh để dán vào mô tả bài đăng) · so-lieu.md
└── video-final.mp4          # BẢN CUỐI
```

## Tài liệu kèm

- `../luat-chung.md` — luật chung cả bộ (đọc trước); `dung-video/khoi/16-so-lieu/mau-so-lieu.md` — mẫu số liệu sau đăng.
- `references/style-analysis.md` — cách đọc video mẫu thành token phong cách; bảng font Google có tiếng Việt.
- `references/scene-design.md` — các loại cảnh có sẵn, khi nào dùng loại nào, mật độ, vùng an toàn.
- `references/example-scenes.js` — kịch bản 17 cảnh thật đã duyệt.
- `references/changelog.md` — sổ quyết định của người dùng theo ngày + lý do (đọc khi cân nhắc đổi một luật).
- `references/gotchas.md` — các lỗi đã gặp và cách tránh (đọc trước khi bắt đầu lần đầu trong phiên).
- `references/handoff.md` — mẫu báo cáo; mẫu HUONG-DAN.md + cách mở DaVinci (chỉ khi được yêu cầu timeline).
- `references/multi-clip.md` — **chế độ ghép nhiều clip**: chọn cảnh, cấu trúc chương trình, hộp đồ nghề điểm nhấn.
- `references/example-edl.js` — kịch bản ghép thật đã duyệt (3 clip → vlog 56 s "Ngày nhận xe").
- Template Remotion dùng chung với skill **podcast-style-edit** (video toàn motion graphics từ file tiếng): `Stage.jsx`,
  composition `nen`, `speakers.js`, `envelope.js`, nhánh `project.podcast` trong layout.js — chỉ bật khi `project.podcast`; sửa template thì giữ chúng.
- `assets/montage-template/` + `scripts/new_montage.sh` — template Remotion dựng cả video có tiếng cho chế độ ghép.

