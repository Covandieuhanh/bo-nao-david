---
name: video-style-edit
description: Dựng video tự quay thành bản đăng được ngay (Reels/TikTok/Shorts/YouTube) theo phong cách video mẫu hoặc dự án cũ. Hai chế độ tự chọn — (1) MỘT video nói trước camera → làm sạch (video ngắn: cắt thừa, câu nói lại, khoảng lặng; sửa video lộn ngược, nằm ngang, lật gương) rồi phủ motion graphics: điểm nhấn trên người, cảnh minh hoạ toàn màn hình bằng biểu tượng vẽ, thẻ, màn chốt bằng nguyên văn lời người nói; đổi khung khi cần (dọc → ngang, ngang → dọc bám người nói); (2) NHIỀU video gốc / cảnh vlog → chọn cảnh, ghép thành vlog kiểu chương trình có teaser, chia vòng, zoom dồn, phụ đề, âm thanh. Kết bằng bước phát hành: tiêu đề, khung bìa, thumbnail khi video ngang, mẫu số liệu. Timeline DaVinci/CapCut chỉ khi được yêu cầu. Dùng khi người dùng đưa một hay nhiều video gốc (kèm hoặc không kèm mẫu) và muốn edit, dựng, ghép, làm vlog, thêm hiệu ứng, chữ, ảnh minh hoạ, "giống video này", "theo style này", "edit như mẫu", "ghép mấy video này", "/video-style-edit" — kể cả khi chỉ gửi file mà không nói rõ.
---
# Dựng video theo phong cách mẫu

**Đọc trước:** `../../thoi-quen-lam-viec.md` · `../luat-chung.md` · hồ sơ `../ho-so/lam-video.md` (hoặc `ghep-vlog.md`) — **con số lấy ở hồ sơ, không ghi cứng**.
File khác chỉ đọc ở đúng bước cần (cột "Khối" của công thức). `references/gotchas.md` đọc một lần ở đầu phiên.
Skill này là **CÔNG THỨC**: thứ tự khối + quyết định riêng của loại + tiêu chí đạt. Cách làm từng bước nằm trong README của khối;
sửa cách làm → sửa khối, không sửa công thức.

Người dùng đưa **video gốc** (thường dọc 9:16, tiếng Việt) và có thể kèm **video mẫu**. Mục tiêu: video **đăng được ngay**, khớp từng
câu nói, không cần mở CapCut/DaVinci. Cách làm cốt lõi: **viết code hoạt hình** (Remotion/React) theo token phong cách, gắn cảnh vào
mốc lời Whisper, render clip nền trong suốt rồi ghép lên video gốc.

**Hỏi một lần ở đầu** (`hoi-chuyen-gia`, sau khi chép lời): gộp mọi điểm cần chọn — chữ bìa, câu chốt, cảnh minh hoạ chính, khung xuất —
mỗi điểm 2–3 gợi ý. David "ok" → chạy một mạch; giữa chừng chỉ dừng khi gặp một trong 6 tín hiệu. Giao bản cuối xong, nhận góp ý và
sửa đúng cảnh được nêu (không tự render lại — `thoi-quen-lam-viec.md` mục 3).

## Luật riêng (kiểm lại trước khi giao)

Luật chung của video ở `../luat-chung.md`: chữ nguyên văn (1), video dài không cắt (2), không ghi chú kỹ thuật trên video (4), hình,
bộ nhận diện, phát hành. Dưới đây chỉ là luật RIÊNG của skill này.

1. **Tối giản:** một màn = một ý, một hình, một câu. Mật độ, nhịp, độ dài cảnh theo `../trinh-bay/` và hồ sơ `lam-video` — không con số cố định.
2. **Mở đầu `hook`** — **không làm mặc định** (David 07/11, khối 06): chỉ khi David yêu cầu, chữ nguyên văn. `project.js` ghi
   `topic: '<CHỦ ĐỀ>'` (≤ 3 chữ, trích lời) cho dấu góc + thẻ cuối.
3. **Bố cục tự cân** (David chốt 07/11; khối 07 + `../trinh-bay/bo-cuc.md`): mỗi đoạn chọn từ danh mục — người + phụ đề, `nhan`,
   `bocuc` (`the-canh` thẻ cạnh mặt · `o-nguoi` người vào ô bo góc + nội dung · `chuong` màn chương), `illus` / `diagram` toàn màn hình.
   Hợp nội dung, người xem dễ nhận; dọc mỗi lúc ít thứ. **Điểm nhấn trên người** (`nhan`): zoom dồn / làm tối viền / chữ nhấn hay biểu
   tượng cạnh mặt ở câu đắt, không che mặt. Mọi video đều có motion graphics trộn nhiều loại — "dựng nhẹ" vẫn có.
4. **Màn hành động** (`action`: biểu tượng + tick + `label` cụm việc nguyên văn) đúng lúc người nói giao việc cụ thể.
   **Màn chốt** (`cta`, cuối mọi video): video lùi vào khung bo góc, chữ = **nguyên văn câu David nói cuối video** (luat-chung 1).
   "Vấn đề / Kết quả" và "gỡ" chỉ lên video khi David tự nói trong video; không thì chỉ ở bài đăng. Không tự đặt câu hỏi kêu gọi,
   không hứa "tập sau" khi người nói không hẹn. Ghi câu + lý do vào `ke-hoach-canh.md`.
5. **Làm sạch:** video dài không cắt (luat-chung 2), chỉ sửa chiều hình; video ngắn: cắt thừa đầu/cuối, câu nói lại (giữ lần sau cùng),
   khoảng lặng + tiếng đệm theo hồ sơ; giữ vẫy tay chào cuối.
6. **Lớp phủ không che mặt** (`face_place.sh`); nhân vật nằm thấp → nâng khung (`lift.py`), mức theo hồ sơ.
7. Mặc định KHÔNG làm timeline DaVinci/CapCut, không nhắc DaVinci trong báo cáo (chỉ khi được yêu cầu — khối 18).
   Thư mục `davinci/media/` chỉ là tên chứa video nguồn và clip trung gian.
8. **Học từ 20 video nói trước camera Việt** (`references/hoc-tu-20-video-noi-truoc-camera-vn.md`, David duyệt 04/11):
   - **Nhãn số danh sách** (`listItem` {n, of?, text}): người nói đếm ≥ 3 ý → mỗi ý một nhãn đúng lúc nói, text nguyên văn cụm việc.
   - **Thẻ tóm tắt để lưu**: video danh sách / hướng dẫn → `card` variant `steps` ngay trước màn chốt, liệt kê các ý nguyên văn (bỏ bớt chữ).
   - **Thẻ chương + chương YouTube** cho video dài có ý lớn: `CHAPTERS` trong scenes.js (mốc + tên trích lời) → `chapters.py`.

## Chọn chế độ (làm đầu tiên)

| Đầu vào | Chế độ | Làm theo |
|---|---|---|
| **1 video gốc** có người nói trước camera | Phủ đồ hoạ lên video gốc (giữ nguyên hình) | Công thức "Làm video" bên dưới |
| **Từ 2 video gốc trở lên**, hoặc clip sự kiện/vlog không nói trước camera | **Ghép nhiều clip**: tự sắp mạch, clip minh hoạ trích đúng câu nói liên quan; **duyệt kế hoạch trước khi render** | `references/multi-clip.md` (khối 11, hồ sơ `ghep-vlog`) |

Video mẫu không tính vào số video gốc. Gửi cả thư mục → mọi video trong đó là video gốc theo thứ tự tên file (chế độ ghép); chỉ hỏi
khi không rõ file nào là mẫu. "Giống video trước" → lấy token phong cách từ `~/Movies/tap-<tên>/2-ban-dai/motion/src` của dự án đó.

## Đầu vào

- **Video gốc**: đường dẫn file (chế độ ghép: nhiều file).
- **Video mẫu**: file video hoặc bản quay màn hình. Chỉ có link YouTube/TikTok → tải bản 720p **chỉ để học** vào thư mục tạm, học xong
  xoá (David chốt 08/11, `../trinh-bay/README.md` mục 4); hoặc 4–8 ảnh chụp các cảnh tiêu biểu. Không có mẫu → phong cách mặc định của template (đã duyệt).
- Yêu cầu thêm của người dùng (thông điệp chính, tên, chỗ muốn nhấn) luôn ưu tiên hơn suy luận.
- **Khung xuất**: mặc định cùng khung video gốc; chỉ đổi khi người dùng nói:

| Gốc → xuất | Cách làm | Ở đâu |
|---|---|---|
| dọc → dọc, ngang → ngang | Bình thường | — |
| **dọc → ngang** (pillar) | Video dọc giữ nguyên, đặt giữa khung 1920×1080. Hai bên nền + chữ cùng phong cách: **trái** = chủ đề, người nói, từ khoá ý đang nói; **phải** = danh sách ý tích dần theo lời. Thẻ/chữ ra ô cột trái (không đè mặt); cảnh toàn màn hình thay video ở cột giữa | Khối 04, 07, 17 |
| **ngang → dọc** (reframe) | Cắt khung 9:16 bám **người đang nói**, nhảy cắt khi lời chuyển (không chia đôi). **Giữ nguyên thời lượng và mọi lời** (vẫn làm sạch ở bước 3). Cảnh không người / phải thấy cả khung → `wide`: cả khung ngang giữa nền mờ | Khối 04 |

## Công thức — Làm video (1 video nói trước camera) · hồ sơ `lam-video`
| # | Bước | Khối | Lệnh chính |
|---|---|---|---|
| 1 | Môi trường *(bước nhẹ)* | [01](../khoi/01-chep-loi/README.md) | `zsh $SKILL/scripts/check_env.sh` |
| 2 | Tạo dự án *(bước nhẹ)* | — | `zsh $SKILL/scripts/new_project.sh "<video gốc>" "<video mẫu>" <tên>` (mục dưới) |
| 3 | Làm sạch (luật 5) | [02](../khoi/02-lam-sach/README.md) | `clean_analyze.sh` → sửa cuts.json → `clean_apply.py` |
| 4 | Đổi khung (nếu cần) + nâng khung | [04](../khoi/04-khung-hinh/README.md) | `reframe_*` / `set_output.py` · `lift.py "$P" apply` |
| 5 | Chép lời + hiểu video *(bước nhẹ)* → **hỏi một lần** | [01](../khoi/01-chep-loi/README.md) | `analyze_video.sh` |
| 6 | Phụ đề | [03](../khoi/03-phu-de/README.md) | `captions.py` → sửa từng dòng |
| 7 | Phong cách (video mẫu / dự án cũ) · **tuyến nội dung → nhạc** (`project.tuyen`, bắt buộc, ghi sau clean_apply) | [10](../khoi/10-nhan-dien/README.md) · [09](../khoi/09-am-thanh/README.md) | style.md → theme.js |
| 8 | Kịch bản: bố cục tự cân · điểm nhấn · màn chốt nguyên văn | [07](../khoi/07-canh-minh-hoa/README.md) · [08](../khoi/08-ket-thuc/README.md) · ([06](../khoi/06-mo-dau/README.md) chỉ khi được yêu cầu) | scenes.js + ke-hoach-canh.md |
| 9 | Tránh che người | [05](../khoi/05-tranh-che-nguoi/README.md) | `face_place.sh` |
| 10 | Chụp thử → render → kiểm bản cuối (+ âm thanh) | [17](../khoi/17-dung-kiem-tra/README.md) · [09](../khoi/09-am-thanh/README.md) | `preview.mjs` → `render.mjs` → `render_preview.py` → `check_frames.sh` |
| 11 | Phát hành: tiêu đề, khung bìa, màn kết/chương/teaser (YouTube video dài), thumbnail (ngang), số liệu | [15](../khoi/15-phat-hanh/README.md) · [08](../khoi/08-ket-thuc/README.md) · [14](../khoi/14-thumbnail/README.md) · [16](../khoi/16-so-lieu/README.md) | `teaser.py` · `chapters.py` · `thumbnail.sh` |
| — | Timeline DaVinci / CapCut (chỉ khi được yêu cầu) | [18](../khoi/18-xuat-app-dung/README.md) | `build_timeline.py` / `build_capcut.py` |

Bước nhẹ: tới đó nhắc một dòng "bước này nhẹ, bạn có thể đổi mô hình rẻ hơn" — không tự đổi.

### Tạo dự án

```bash
zsh $SKILL/scripts/new_project.sh "<video gốc>" "<video mẫu>" <tên-ngắn>
```
Tạo `~/Movies/tap-<tên>/2-ban-dai/` (gốc tự đặt vào `tap-<tên>/1-goc/`; tên `vlog-…` → `~/Movies/vlog/<tên>/`) với cấu trúc chuẩn
(cuối file), chép video, chép template Remotion vào `motion/`, điền thông số vào `motion/src/project.js`, cài gói npm. Dòng cuối là `$P`.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| cuts.json (làm sạch) | clean_apply.py → lift.py apply → analyze_video.sh → captions.py → dời mốc scenes.js → face_place.sh → render |
| scenes.js (mốc / loại cảnh) | face_place.sh → `node render.mjs <id>` → render_preview.py |
| captions.js | `node render.mjs phu-de` → render_preview.py |
| theme.js / brand | render lại tất cả |
| project.js (topic, ytEnd, schedule) — ghi lại SAU clean_apply (nó viết đè project.js) | `node render.mjs the-cuoi` → render_preview.py |
| video-final (teaser) | chapters.py |
| hồ sơ lam-video | chạy lại khối dùng khoá đó (bảng khoá trong ho-so/lam-video.md) |

## Tiêu chí đạt (soát trước khi giao)
- Không thẻ tít mở đầu trừ khi được yêu cầu · có trộn nhiều loại điểm nhấn (người + phụ đề / `nhan` / cảnh toàn màn hình), không che mặt, không chữ to tự do đè người
- Bố cục hợp nội dung (xem stills: người / ý có rõ không) · phụ đề đúng chữ, không bị đè · tiếng Việt đủ dấu · không gì lọt vùng đỏ
- Màn chốt nguyên văn + thẻ cuối · (YouTube video dài) màn kết, chương, teaser · thumbnail nếu ngang · phat-hanh.md + so-lieu.md
- Âm lượng theo chuẩn chung, tiếng rè không tăng so nguồn; thời lượng đúng

## Sửa theo góp ý

Người dùng thường nói kiểu "cảnh 2:08 chữ to quá", "đổi hình thợ hồ", "bỏ cảnh AI". Sửa đúng chỗ trong `scenes.js`/component/ảnh →
đổi mốc thì chạy lại `python3 -I $SKILL/scripts/face_place.py "$P"` → `node render.mjs <id>` (chỉ cảnh đó) → `render_preview.py` →
kiểm khung quanh mốc đó. Đổi phong cách toàn bộ → sửa `theme.js`, render lại tất cả. Đã có timeline → chạy lại `build_timeline.py`.
"Giữ lại đoạn bị cắt"/"cắt thêm đoạn X" → đổi mốc bản cuối sang mốc thô bằng `segments.json`, sửa `cuts.json`, lưu bản `segments.json`
cũ, chạy `clean_apply.py`, dời mốc mọi cảnh (`start`, `end`, `at`…) theo bảng mới. Chỉ render lại cảnh có mối đổi nằm **bên trong**
nó, rồi `render_preview.py` (+ `build_timeline.py` nếu đã làm timeline).
Ghi góp ý đúng một chỗ: khối/skill bị ảnh hưởng + một dòng `references/changelog.md`.

## Cấu trúc dự án

```
~/Movies/tap-<tên>/2-ban-dai/
├── davinci/                 # tên lịch sử; chỉ thành "gói DaVinci" khi người dùng yêu cầu timeline
│   ├── media/               # video_goc.mp4 (bản sạch), video_goc_raw.* (bản thô), <id>.mov (ProRes 4444 alpha), khung_an_toan.png
│   └── timeline.fcpxml · HUONG-DAN.md   # chỉ khi được yêu cầu
├── motion/                  # dự án Remotion (src/scenes.js, theme.js, fonts.js, components/, public/photos/)
├── images/                  # queries.json, candidates.json, thumbs/, sheets/, picks.json, credits.tsv
├── ref/                     # video mẫu + phân tích
├── check/                   # khung kiểm tra; reframe/ = plan.json, shots.jpg; clean/ = cuts.json, cuts.md, segments.json
├── phat-hanh/              # phat-hanh.md (tiêu đề, mô tả) · thumb-1.jpg · thumb-2.jpg (+ @160 xem cỡ điện thoại)
├── style.md · ke-hoach-canh.md · nguon-anh.txt (nguồn ảnh để dán vào mô tả bài đăng) · so-lieu.md
└── video-final.mp4          # BẢN CUỐI
```

## Xong khi
1. Đã hỏi một lần ở đầu, gộp mọi điểm cần chọn; sau "ok" chạy một mạch.
2. Chữ trên video (kể cả màn chốt) là nguyên văn lời David; không thẻ tít trừ khi được yêu cầu.
3. Video dài để nguyên; video ngắn làm sạch mà không mất ý.
4. Có motion graphics nhiều loại, bố cục tự cân, không che mặt, không gì lọt vùng đỏ.
5. Phụ đề đúng chữ, đủ dấu, không bị đè; âm lượng đạt chuẩn chung.
6. Đã chụp kiểm đúng các mốc dễ lỗi trước khi giao.
7. Đủ gói phát hành (tiêu đề, khung bìa, thumbnail nếu ngang, mẫu số liệu); David không phải sửa lại vì trái luật đã chốt.

## Tài liệu kèm (chỉ đọc khi bước cần, cân nhắc đổi luật hoặc gỡ lỗi)

- `references/gotchas.md` — lỗi đã gặp và cách tránh (đọc một lần đầu phiên).
- `references/style-analysis.md` — đọc video mẫu thành token phong cách; bảng font Google có tiếng Việt.
- `references/scene-design.md` — các loại cảnh có sẵn, khi nào dùng loại nào, vùng an toàn.
- `references/example-scenes.js` — kịch bản 17 cảnh thật đã duyệt.
- `references/changelog.md` — sổ quyết định theo ngày + lý do.
- `references/handoff.md` — mẫu báo cáo; mẫu HUONG-DAN.md (chỉ khi được yêu cầu timeline).
- `references/multi-clip.md` + `references/example-edl.js` — chế độ ghép nhiều clip; kịch bản ghép thật đã duyệt.
- `../khoi/16-so-lieu/mau-so-lieu.md` — mẫu số liệu sau đăng.
- Template Remotion dùng chung với **podcast-style-edit**: `Stage.jsx`, composition `nen`, `speakers.js`, `envelope.js`, nhánh
  `project.podcast` trong layout.js — chỉ bật khi `project.podcast`; sửa template thì giữ chúng.
- `assets/montage-template/` + `scripts/new_montage.sh` — template dựng cả video có tiếng cho chế độ ghép.

## Nhật ký
- 2026-11-08 · chuẩn hoá (`dang-lam/chuan-hoa-skill.md` bước 3): hỏi một lần đầu thay "chạy một mạch không hỏi" (N1); bỏ con số cố định (N6), thẻ tít mặc định (N2), chữ "2 trạng thái" (C3), ví dụ cũ hướng sức khoẻ; màn chốt nguyên văn, không tự đặt câu kêu gọi (N4); đọc trước 3 file, luật chung trỏ `luat-chung`; đánh dấu bước nhẹ 1·2·5; rút mô tả; thêm "Xong khi"; video mẫu chỉ có link → được tải 720p chỉ để học, học xong xoá (khớp `trinh-bay`). Chi tiết các quyết định trước: `references/changelog.md`.
