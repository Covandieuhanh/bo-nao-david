---
name: dung-video-theo-phong-cach
description: Dựng video tự quay thành bản đăng được ngay (Reels/TikTok/Shorts/YouTube) theo phong cách video mẫu hoặc dự án cũ. Hai chế độ tự chọn — (1) MỘT video nói trước camera → làm sạch (video ngắn: cắt thừa, câu nói lại, khoảng lặng; sửa video lộn ngược, nằm ngang, lật gương) rồi phủ motion graphics: điểm nhấn trên người, cảnh minh hoạ toàn màn hình bằng biểu tượng vẽ, thẻ, màn chốt bằng nguyên văn lời người nói; đổi khung khi cần (dọc → ngang, ngang → dọc bám người nói); (2) NHIỀU video gốc / cảnh vlog → chọn cảnh, ghép thành vlog kiểu chương trình có teaser, chia vòng, phụ đề, âm thanh. Kết bằng bước phát hành: tiêu đề, khung bìa, thumbnail khi video ngang, mẫu số liệu. Không làm bản cho app chỉnh sửa (DaVinci/CapCut). Dùng khi người dùng đưa một hay nhiều video gốc (kèm hoặc không kèm mẫu) và muốn edit, dựng, ghép, làm vlog, thêm hiệu ứng, chữ, ảnh minh hoạ, "giống video này", "theo style này", "edit như mẫu", "ghép mấy video này", "/dung-video-theo-phong-cach" — kể cả khi chỉ gửi file mà không nói rõ.
---
# Dựng video theo phong cách mẫu

**Đọc trước:** `../../chuan-muc-lam-viec.md` · `../quy-tac-chung.md` · hồ sơ `../ho-so-thuong-hieu/lam-video.md` (hoặc `ghep-vlog.md`) — **con số lấy ở hồ sơ, không ghi cứng**.
File khác chỉ đọc ở đúng bước cần (cột "Khối" của công thức). `references/loi-thuong-gap.md` đọc một lần ở đầu phiên.
Skill này là **CÔNG THỨC**: thứ tự khối + quyết định riêng của loại + tiêu chí đạt. Cách làm từng bước nằm trong README của khối;
sửa cách làm → sửa khối, không sửa công thức.

Người dùng đưa **video gốc** (thường dọc 9:16, tiếng Việt) và có thể kèm **video mẫu**. Mục tiêu: video **đăng được ngay**, khớp từng
câu nói; David không cần bản cho app chỉnh sửa (CapCut/DaVinci). Cách làm cốt lõi: **viết code hoạt hình** (Remotion/React) theo token phong cách, gắn cảnh vào
mốc lời Whisper, render clip nền trong suốt rồi ghép lên video gốc.

**Duyệt 4 phần trước** (`../../chuan-muc-lam-viec.md` mục 2), duyệt rồi không hỏi thêm: chạy một mạch từ video gốc tới bản cuối. Khung xuất = khung gốc (bảng "Khung xuất");
video > 3 phút làm đủ gói YouTube (màn kết, chương, teaser, thumbnail khi ngang); chữ bìa, cảnh minh hoạ chính, tuyến nhạc Claude tự chọn
theo khối. Giữa chừng chỉ dừng khi gặp tín hiệu nặng (`thu-thap-yeu-cau`). Báo cáo cuối liệt kê "đã chọn X vì Y" để David sửa ở bản
cuối; nhận góp ý thì sửa đúng chỗ được nêu rồi render lại toàn bộ luôn (`quy-tac-chung.md` mục 8).

## Nhịp làm (mục tiêu: video 10 phút xong trong ~1 giờ)

- **Tự chọn trước, không thử bằng render** (`../thiet-ke-bo-cuc/tu-chon.md`): chẩn đoán → chọn bố cục nền, lớp thông tin, kiểu cảnh →
  `soat-canh.mjs` chặn kiểu lỗi theo khung → chụp thử đủ lớp → render một lần.
- Render và ghép chạy nền; `xem-truoc-ban-dung.py` tự dừng khi render còn chạy hoặc thiếu lớp (không ghép thiếu).
- **Lỗi skill giữa chừng không mổ xẻ tại chỗ**: ghi một dòng vào `kiem-tra/loi-ky-nang.md`, làm tiếp bằng cách đơn giản nhất cho đúng kết
  quả, cuối việc báo David + đề xuất sửa skill.
- Báo mốc giờ ở mỗi bước dài (render, ghép); quá 1,5 lần dự kiến thì nói lý do.

## Luật riêng (kiểm lại trước khi giao)

Luật chung của video ở `../quy-tac-chung.md`: chữ nguyên văn (1), video dài không cắt (2), không ghi chú kỹ thuật trên video (4), hình,
bộ nhận diện, phát hành. Dưới đây chỉ là luật RIÊNG của skill này.

1. **Motion graphic kể chuyện, tự do sáng tạo** (khối 07 mục 1): chỉ giữ chữ ký nhận diện; còn lại AI sáng tạo theo video — một hình có
   thể diễn tả 1–2 ý hoặc cả video, ý quay lại thì vẽ tiếp lên hình đã có (mạch hình, cảnh tự vẽ `ve`). Không con số cố định.
2. **Mở đầu `hook`** — **không làm mặc định** (khối 06): chỉ khi David yêu cầu, chữ nguyên văn. `du-an.js` ghi
   `topic: '<CHỦ ĐỀ>'` (≤ 3 chữ, trích lời) cho dấu góc + thẻ cuối.
3. **Bố cục tự chọn theo nội dung** (`../thiet-ke-bo-cuc/tu-chon.md` → khối 07 + `../thiet-ke-bo-cuc/bo-cuc.md`): danh mục có sẵn (dùng khi hợp, không bắt buộc — cần hình riêng thì viết cảnh tự vẽ `ve`) — người + phụ đề, `nhan`,
   `bocuc` (`the-canh` thẻ cạnh mặt · `o-nguoi` người vào ô bo góc + nội dung · `chuong` màn chương), `illus` / `diagram` toàn màn hình.
   Hợp nội dung, người xem dễ nhận; dọc mỗi lúc ít thứ. **Điểm nhấn trên người** (`nhan`): làm tối viền / chữ nhấn hay biểu
   tượng cạnh mặt ở câu đắt, không che mặt; không zoom vào / ra. Mọi video đều có điểm nhấn — "dựng nhẹ" vẫn có — nhưng chỉ vài kiểu hợp nội dung nhất.
4. **Màn hành động** (`action`: biểu tượng + tick + `label` cụm việc nguyên văn) đúng lúc người nói giao việc cụ thể.
   **Màn chốt** (`cta`, cuối mọi video): video lùi vào khung bo góc, chữ = **nguyên văn câu David nói cuối video** (quy-tac-chung 1).
   "Vấn đề / Kết quả" và "gỡ" chỉ lên video khi David tự nói trong video; không thì chỉ ở bài đăng. Không tự đặt câu hỏi kêu gọi,
   không hứa "tập sau" khi người nói không hẹn. Ghi câu + lý do vào `ke-hoach-canh.md`.
5. **Làm sạch:** video dài không cắt (quy-tac-chung 2), chỉ sửa chiều hình; video ngắn: cắt thừa đầu/cuối, câu nói lại (giữ lần sau cùng),
   khoảng lặng + tiếng đệm theo hồ sơ; giữ vẫy tay chào cuối.
6. **Lớp phủ không che mặt** (`vi-tri-khuon-mat.sh`); nhân vật nằm thấp → nâng khung (`nang-lop.py`), mức theo hồ sơ.
7. Không làm bản cho app chỉnh sửa (DaVinci/CapCut…), không nhắc trong báo cáo — David chỉ dùng bản render cuối.
   Thư mục `tu-lieu/` chỉ là tên lịch sử, chứa video nguồn và clip trung gian; dọn sau khi David chốt (bước 12).
8. **Học từ 20 video nói trước camera Việt** (`references/hoc-tu-20-video-noi-truoc-camera-vn.md`):
   - **Nhãn số danh sách** (`listItem` {n, of?, text}): người nói đếm ≥ 3 ý → mỗi ý một nhãn đúng lúc nói, text nguyên văn cụm việc.
   - **Thẻ tóm tắt để lưu**: video danh sách / hướng dẫn → `card` variant `steps` ngay trước màn chốt, liệt kê các ý nguyên văn (bỏ bớt chữ).
   - **Thẻ chương + chương YouTube** cho video dài có ý lớn: `CHAPTERS` trong canh.js (mốc + tên trích lời) → `chuong.py`.

## Chọn chế độ (làm đầu tiên)

| Đầu vào | Chế độ | Làm theo |
|---|---|---|
| **1 video gốc** có người nói trước camera | Phủ đồ hoạ lên video gốc (giữ nguyên hình) | Công thức "Làm video" bên dưới |
| **Từ 2 video gốc trở lên**, hoặc clip sự kiện/vlog không nói trước camera | **Ghép nhiều clip**: tự sắp mạch, clip minh hoạ trích đúng câu nói liên quan; tự soát kế hoạch rồi render | `references/nhieu-doan-video.md` (khối 11, hồ sơ `ghep-vlog`) |

Video mẫu không tính vào số video gốc. Gửi cả thư mục → mọi video trong đó là video gốc theo thứ tự tên file (chế độ ghép); chỉ hỏi
khi không rõ file nào là mẫu. "Giống video trước" → lấy token phong cách từ `~/Movies/tap-<tên>/2-ban-day-du/chuyen-dong/src` của dự án đó.

## Đầu vào

- **Video gốc**: đường dẫn file (chế độ ghép: nhiều file).
- **Video mẫu**: file video hoặc bản quay màn hình. Chỉ có link YouTube/TikTok → tải bản 720p **chỉ để học** vào thư mục tạm, học xong
  xoá (`../thiet-ke-bo-cuc/README.md` mục 4); hoặc 4–8 ảnh chụp các cảnh tiêu biểu. Không có mẫu → phong cách mặc định của template. Học phong cách mẫu không đụng chữ ký nhận diện (khối 10).
- Yêu cầu thêm của David (thông điệp chính, tên, chỗ muốn nhấn) luôn ưu tiên hơn suy luận.
- **Khung xuất**: cùng khung video gốc; chỉ đổi khi David **nói rõ khung** ("làm dọc", "xuất ngang"). Yêu cầu khác làm trong khung gốc — **tập trung vào một vùng / bỏ rác quanh chủ thể** (màn hình điện thoại, laptop, vật) → **khung chủ thể**
  (`khung-chu-the.py`, khối 04): chủ thể thành khung bo góc trên nền kênh, phần còn lại cho bảng ghi chú + cảnh — không cắt-phóng cả khung:

| Gốc → xuất | Cách làm | Ở đâu |
|---|---|---|
| dọc → dọc, ngang → ngang | Bình thường | — |
| **dọc → ngang** (pillar) | Video dọc giữ nguyên, đặt giữa khung 1920×1080. Hai bên nền + chữ cùng phong cách: **trái** = chủ đề, người nói, từ khoá ý đang nói; **phải** = danh sách ý tích dần theo lời. Thẻ/chữ ra ô cột trái (không đè mặt); cảnh toàn màn hình thay video ở cột giữa | Khối 04, 07, 17 |
| **ngang → dọc** (reframe) | Cắt khung 9:16 bám **người đang nói**, nhảy cắt khi lời chuyển (không chia đôi). **Giữ nguyên thời lượng và mọi lời** (vẫn làm sạch ở bước 3). Cảnh không người / phải thấy cả khung → `wide`: cả khung ngang giữa nền mờ | Khối 04 |

## Công thức — Làm video (1 video nói trước camera) · hồ sơ `lam-video`
| # | Bước | Khối | Lệnh chính |
|---|---|---|---|
| 1 | Môi trường *(bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) | `zsh $SKILL/scripts/kiem-moi-truong.sh` |
| 2 | Tạo dự án *(bước nhẹ)* | — | `zsh $SKILL/scripts/tao-du-an.sh "<video gốc>" "<video mẫu>" <tên>` (mục dưới) |
| 3 | Làm sạch (luật 5) | [02](../mo-dun/02-lam-sach/README.md) | `phan-tich-lam-sach.sh` → sửa diem-cat.json → `ap-dung-lam-sach.py` |
| 4 | Đổi khung (nếu cần) + nâng khung | [04](../mo-dun/04-khung-hinh/README.md) | `rekhung-*` / `dat-dau-ra.py` · `nang-lop.py "$P" apply` |
| 5 | Chép lời + hiểu video *(bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) | `phan-tich-video.sh` |
| 6 | Phụ đề | [03](../mo-dun/03-phu-de/README.md) | `phu-de.py` → sửa từng dòng |
| 6b | **Chẩn đoán → tự chọn**: bố cục nền (khung gốc / khung chủ thể / pillar), lớp thông tin (bảng ghi chú chạy `GHI_CHU`, chương), kiểu cảnh | [`tu-chon.md`](../thiet-ke-bo-cuc/tu-chon.md) · [04](../mo-dun/04-khung-hinh/README.md) | `chan-doan.py` → (`khung-chu-the.py luoi` → `apply`) |
| 7 | Phong cách (video mẫu / dự án cũ) · **tuyến nội dung → nhạc** (`project.tuyen`, bắt buộc, ghi sau clean_apply) | [10](../mo-dun/10-nhan-dien-thuong-hieu/README.md) · [09](../mo-dun/09-am-thanh/README.md) | phong-cach.md → chu-de.js |
| 8 | Kịch bản: bố cục tự cân · điểm nhấn · màn chốt nguyên văn | [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · ([06](../mo-dun/06-phan-mo-dau/README.md) chỉ khi được yêu cầu) | canh.js + ke-hoach-canh.md |
| 9 | Tránh che người | [05](../mo-dun/05-tranh-che-chu-the/README.md) | `vi-tri-khuon-mat.sh` |
| 10 | Chụp thử → render → kiểm bản cuối (+ âm thanh) | [17](../mo-dun/17-kiem-soat-chat-luong/README.md) · [09](../mo-dun/09-am-thanh/README.md) | `xem-truoc.mjs` → `xuat-video.mjs` → `xem-truoc-ban-dung.py` → `kiem-khung-hinh.sh` |
| 11 | Phát hành: tiêu đề, khung bìa, màn kết/chương/teaser (YouTube video dài), thumbnail (ngang), số liệu | [15](../mo-dun/15-xuat-ban/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [14](../mo-dun/14-anh-thu-nho/README.md) · [16](../mo-dun/16-phan-tich-so-lieu/README.md) | `doan-gioi-thieu.py` · `chuong.py` · `anh-thu-nho.sh` |
| 12 | David chốt bản cuối → dọn file tạm luôn (`--xoa`, không hỏi; chỉ hỏi phần ⏸ đang dở) → đưa tập lên Drive, xoá trên Mac | [17](../mo-dun/17-kiem-soat-chat-luong/README.md) | `don-tap.py` → `luu-drive.sh` (nền) |

Bước đánh dấu *(bước nhẹ)*: nhắc đổi mô hình rẻ hơn theo `chuan-muc-lam-viec.md` mục 3.

### Tạo dự án

```bash
zsh $SKILL/scripts/tao-du-an.sh "<video gốc>" "<video mẫu>" <tên-ngắn>
```
Tạo `~/Movies/tap-<tên>/2-ban-day-du/` (gốc tự đặt vào `tap-<tên>/1-goc/`; tên `vlog-…` → `~/Movies/vlog/<tên>/`) với cấu trúc chuẩn
(cuối file), chép video, chép template Remotion vào `chuyen-dong/`, điền thông số vào `chuyen-dong/src/du-an.js`, cài gói npm. Dòng cuối là `$P`.

## Bảng phụ thuộc (sửa X → chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| diem-cat.json (làm sạch) | ap-dung-lam-sach.py → nang-lop.py apply → phan-tich-video.sh → phu-de.py → dời mốc canh.js → vi-tri-khuon-mat.sh → render |
| canh.js (mốc / loại cảnh) | vi-tri-khuon-mat.sh → `node xuat-video.mjs <id>` → xem-truoc-ban-dung.py |
| phu-de.js | `node xuat-video.mjs phu-de` → xem-truoc-ban-dung.py |
| chu-de.js / brand | render lại tất cả |
| du-an.js (topic, ytEnd, schedule) — ghi lại SAU clean_apply (nó viết đè du-an.js) | `node xuat-video.mjs the-cuoi` → xem-truoc-ban-dung.py |
| video-hoan-chinh (teaser) | chuong.py |
| hồ sơ lam-video | chạy lại khối dùng khoá đó (bảng khoá trong ho-so-thuong-hieu/lam-video.md) |

## Tiêu chí đạt (soát trước khi giao)
- Không thẻ tít mở đầu trừ khi được yêu cầu · có điểm nhấn, vài kiểu hợp nội dung, video không rối · không che mặt, không chữ to tự do đè người
- Bố cục hợp nội dung (xem stills: người / ý có rõ không) · phụ đề đúng chữ, không bị đè · tiếng Việt đủ dấu · không gì lọt vùng đỏ
- Màn chốt nguyên văn + thẻ cuối (video dọc ngắn: màn chốt trên hình, không thẻ cuối, không thanh thời gian — `../thu-vien-tai-nguyen/nhan-dien-chung.md` mục 1) · (YouTube video dài) màn kết, chương, teaser · thumbnail nếu ngang · phat-hanh.md + so-lieu.md
- Âm lượng theo chuẩn chung, tiếng rè không tăng so nguồn; thời lượng đúng

## Sửa theo góp ý

David thường nói kiểu "cảnh 2:08 chữ to quá", "đổi hình thợ hồ", "bỏ cảnh AI". Sửa đúng chỗ trong `canh.js`/component/ảnh →
đổi mốc thì chạy lại `python3 -I $SKILL/scripts/vi-tri-khuon-mat.py "$P"` → `node xuat-video.mjs <id>` (chỉ cảnh đó) → `xem-truoc-ban-dung.py` →
kiểm khung quanh mốc đó. Đổi phong cách toàn bộ → sửa `chu-de.js`, render lại tất cả.
"Giữ lại đoạn bị cắt"/"cắt thêm đoạn X" → đổi mốc bản cuối sang mốc thô bằng `cac-doan.json`, sửa `diem-cat.json`, lưu bản `cac-doan.json`
cũ, chạy `ap-dung-lam-sach.py`, dời mốc mọi cảnh (`start`, `end`, `at`…) theo bảng mới. Chỉ render lại cảnh có mối đổi nằm **bên trong**
nó, rồi `xem-truoc-ban-dung.py`.
Ghi góp ý đúng một chỗ: khối/skill bị ảnh hưởng + một dòng `references/nhat-ky-thay-doi.md`.

## Cấu trúc dự án

```
~/Movies/tap-<tên>/2-ban-day-du/
├── tu-lieu/           # video-goc.mp4 (bản sạch), video-goc-tho.*, <id>.mov (ProRes 4444 alpha), khung-an-toan.png
├── chuyen-dong/                  # dự án Remotion (src/canh.js, chu-de.js, phong-chu.js, thanh-phan/, public/anh/)
├── hinh-anh/                  # tu-khoa-tim.json, ung-vien.json, anh-nho/, bang-anh/, anh-chon.json, ghi-cong.tsv
├── tai-lieu-tham-khao/                     # video mẫu + phân tích
├── kiem-tra/                   # khung kiểm tra; doi-khung/ = ke-hoach.json, canh-quay.jpg; lam-sach/ = diem-cat.json, diem-cat.md, cac-doan.json
├── phat-hanh/              # phat-hanh.md (tiêu đề, mô tả) · anh-thu-nho-1.jpg · anh-thu-nho-2.jpg (+ @160 xem cỡ điện thoại)
├── phong-cach.md · ke-hoach-canh.md · nguon-anh.txt (nguồn ảnh để dán vào mô tả bài đăng) · so-lieu.md
└── video-hoan-chinh.mp4          # BẢN CUỐI
```

## Xong khi
1. Không hỏi giữa chừng trừ tín hiệu nặng; khung xuất đúng khung gốc trừ khi David yêu cầu đổi; báo cáo có "đã chọn X vì Y".
2. Chữ trên video (kể cả màn chốt) là nguyên văn lời David; không thẻ tít trừ khi được yêu cầu.
3. Video dài để nguyên; video ngắn làm sạch mà không mất ý.
4. Có motion graphics hợp nội dung (vài kiểu, không rối), bố cục tự cân, không che mặt, không gì lọt vùng đỏ.
5. Phụ đề đúng chữ, đủ dấu, không bị đè; âm lượng đạt chuẩn chung.
6. Đã chụp kiểm đúng các mốc dễ lỗi trước khi giao.
7. Đủ gói phát hành (tiêu đề, khung bìa, thumbnail nếu ngang, mẫu số liệu); David không phải sửa lại vì trái luật đã chốt.
8. Sau khi David chốt: đã chạy `don-tap.py --xoa` rồi `luu-drive.sh`; tập đã lên Drive `sao-luu-mac/video`, đã xoá trên Mac, đã ghi loại vào `du-an/kho-drive.md`; phần ⏸ (đang dở) đã hỏi David.

## Tài liệu kèm (chỉ đọc khi bước cần, cân nhắc đổi luật hoặc gỡ lỗi)

- `references/loi-thuong-gap.md` — lỗi đã gặp và cách tránh (đọc một lần đầu phiên).
- `references/phan-tich-phong-cach.md` — đọc video mẫu thành token phong cách; bảng font Google có tiếng Việt.
- `references/thiet-ke-canh.md` — các loại cảnh có sẵn, khi nào dùng loại nào, vùng an toàn.
- `references/vi-du-canh.js` — kịch bản 17 cảnh thật đã duyệt.
- `references/nhat-ky-thay-doi.md` — sổ quyết định theo ngày + lý do.
- `references/ban-giao.md` — mẫu báo cáo.
- `references/nhieu-doan-video.md` + `references/vi-du-danh-sach-cat.js` — chế độ ghép nhiều clip; kịch bản ghép thật đã duyệt.
- `../mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` — mẫu số liệu sau đăng.
- Template Remotion dùng chung với **dung-podcast**: `san-khau.jsx`, composition `nen`, `nguoi-noi.js`, `duong-bao-am.js`, nhánh
  `project.podcast` trong bo-cuc.js — chỉ bật khi `project.podcast`; sửa template thì giữ chúng.
- `assets/khuon-dung-ghep/` + `scripts/tao-dung-ghep.sh` — template dựng cả video có tiếng cho chế độ ghép.
