---
name: dung-video-theo-phong-cach
description: Dựng video tự quay thành bản đăng được ngay (Reels/TikTok/Shorts/YouTube) theo phong cách video mẫu hoặc dự án cũ. Skill có hai chế độ, tự chọn — (1) MỘT video nói trước camera: làm sạch (video ngắn: cắt phần thừa, câu nói lại, khoảng lặng; sửa video lộn ngược, nằm ngang, lật gương) rồi phủ motion graphics: điểm nhấn trên người, cảnh minh hoạ toàn màn hình bằng biểu tượng vẽ, thẻ, màn chốt bằng nguyên văn lời người nói; đổi khung khi cần (dọc sang ngang, ngang sang dọc bám theo người nói); (2) NHIỀU video gốc / cảnh vlog: chọn cảnh, ghép thành vlog theo kiểu chương trình có teaser, chia vòng, phụ đề, âm thanh. Skill kết thúc bằng bước phát hành: tiêu đề, khung bìa, thumbnail khi video ngang, mẫu số liệu. Skill không làm bản cho app chỉnh sửa (DaVinci/CapCut). Dùng khi người dùng đưa một hay nhiều video gốc (kèm hoặc không kèm mẫu) và muốn edit, dựng, ghép, làm vlog, thêm hiệu ứng, chữ, ảnh minh hoạ, "giống video này", "theo style này", "edit như mẫu", "ghép mấy video này", "/dung-video-theo-phong-cach" — kể cả khi chỉ gửi file mà không nói rõ.
---
# Dựng video theo phong cách mẫu

**Đọc trước:** `../quy-tac-chung.md` (mục 8) · hồ sơ `../ho-so-thuong-hieu/lam-video.md` (hoặc `ghep-vlog.md`).

Người dùng đưa **video gốc** (thường là dọc 9:16, tiếng Việt) và có thể kèm **video mẫu**. Mục tiêu: video **đăng được ngay**, khớp từng
câu nói; David không cần bản cho app chỉnh sửa (CapCut/DaVinci). Cách làm cốt lõi: **viết code hoạt hình** (Remotion/React) theo token phong cách, gắn cảnh vào
mốc thời gian lời nói từ Whisper, render clip nền trong suốt rồi ghép lên video gốc.

**Đã có quy trình nên tự động hoàn toàn** (`../../chuan-muc-lam-viec.md` mục 2): Claude không trình 4 phần, không hỏi thêm, chạy liên tục từ video gốc tới bản cuối. Khung xuất bằng khung gốc (bảng "Khung xuất");
video dài hơn 3 phút làm đủ gói YouTube (màn kết, chương, thumbnail khi ngang; teaser khi video đủ dài, Claude tự quyết định); chữ bìa, cảnh minh hoạ chính, tuyến nhạc do Claude tự chọn
theo khối. Luật về dừng giữa chừng, về báo cáo "đã chọn X vì Y" và về render lại toàn bộ khi có góp ý: `quy-tac-chung.md` mục 8.

## Nhịp làm việc (mục tiêu: video 10 phút hoàn thành trong khoảng 1 giờ)

- **Tự chọn trước, không thử bằng render** (`../thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md` → `../thiet-ke-bo-cuc/huong-dan-lua-chon.md`): đọc `yeu-cau.md` + `them-anh/` → chẩn đoán →
  loại nội dung → bố cục nền, lớp thông tin → mỗi cảnh lập luận "Cần · Vì · Làm" →
  `soat-canh.mjs` chặn kiểu lỗi theo khung → chụp thử đủ lớp → render một lần.
- Render và ghép chạy nền; `xem-truoc-ban-dung.py` tự dừng khi render còn đang chạy hoặc thiếu lớp (không ghép khi thiếu lớp).
- **Lỗi skill gặp giữa chừng không phân tích sâu tại chỗ**: Claude ghi một dòng vào `kiem-tra/loi-ky-nang.md`, làm tiếp bằng cách đơn giản nhất để ra đúng kết
  quả, cuối việc báo David + đề xuất sửa skill.
- Claude báo mốc giờ ở mỗi bước dài (render, ghép); khi vượt quá 1,5 lần thời gian dự kiến thì nêu lý do.

## Luật riêng (kiểm lại trước khi bàn giao)

Luật chung về video ở `../quy-tac-chung.md`: chữ nguyên văn (1), video dài không cắt (2), không ghi chú kỹ thuật trên video (4), hình,
bộ nhận diện, phát hành. Dưới đây chỉ là luật RIÊNG của skill này.

1. **Motion graphic kể chuyện, tự do sáng tạo** (khối 07 mục 1): chỉ giữ chữ ký nhận diện; phần còn lại AI sáng tạo theo video — một hình có
   thể diễn tả 1–2 ý hoặc cả video; khi ý quay lại thì vẽ tiếp lên hình đã có (mạch hình, cảnh tự vẽ `ve`). Không có con số cố định.
2. **Mở đầu `hook`** — **không làm mặc định** (khối 06): chỉ làm khi David yêu cầu, chữ nguyên văn. `du-an.js` ghi
   `topic: '<CHỦ ĐỀ>'` (tối đa 3 chữ, trích từ lời nói) cho dấu góc + thẻ cuối.
3. **Bố cục tự chọn theo nội dung** (`../thiet-ke-bo-cuc/huong-dan-lua-chon.md`, rồi khối 07 + `../thiet-ke-bo-cuc/bo-cuc.md`): danh mục có sẵn (dùng khi phù hợp, không bắt buộc — khi cần hình riêng thì viết cảnh tự vẽ `ve`) — người + phụ đề, `nhan`,
   `bocuc` (`the-canh` thẻ cạnh mặt · `o-nguoi` người vào ô bo góc + nội dung · `chuong` màn chương), `illus` / `diagram` toàn màn hình.
   Phù hợp nội dung, người xem dễ nhận biết; khung dọc mỗi lúc ít thành phần. **Điểm nhấn trên người** (`nhan`): làm tối viền / chữ nhấn hoặc biểu
   tượng cạnh mặt ở câu then chốt, không che mặt; không zoom vào / ra. Mọi video đều có điểm nhấn — "dựng nhẹ" vẫn có — nhưng chỉ dùng vài kiểu phù hợp nội dung nhất.
4. **Màn hành động** (`action`: biểu tượng + tick + `label` cụm việc nguyên văn) xuất hiện đúng lúc người nói giao việc cụ thể.
   **Màn chốt** (`cta`, cuối mọi video): video thu vào khung bo góc, chữ là **nguyên văn câu David nói cuối video** (quy-tac-chung 1).
   "Vấn đề / Kết quả" và "gỡ" chỉ đưa lên video khi David tự nói trong video; nếu không thì chỉ dùng ở bài đăng. Claude không tự đặt câu hỏi kêu gọi,
   không hứa "tập sau" khi người nói không hẹn. Claude ghi câu + lý do vào `ke-hoach-canh.md`.
5. **Làm sạch:** video dài không cắt (quy-tac-chung 2), chỉ sửa chiều hình; video ngắn: cắt phần thừa đầu/cuối, câu nói lại (giữ lần nói sau cùng),
   khoảng lặng + tiếng đệm theo hồ sơ; giữ cảnh vẫy tay chào cuối.
6. **Lớp phủ không che mặt** (`vi-tri-khuon-mat.sh`); nhân vật nằm thấp trong khung thì nâng khung (`nang-khung.py`), mức nâng theo hồ sơ.
7. Claude không làm bản cho app chỉnh sửa (DaVinci/CapCut…), không nhắc tới trong báo cáo — David chỉ dùng bản render cuối.
   Thư mục `tu-lieu/` chỉ là tên lịch sử, chứa video nguồn và clip trung gian; dọn sau khi David chốt (bước 12).
8. **Học từ 20 video nói trước camera tiếng Việt** (`references/hoc-tu-20-video-noi-truoc-camera-vn.md`):
   - **Nhãn số danh sách** (`listItem` {n, of?, text}): khi người nói đếm từ 3 ý trở lên thì mỗi ý có một nhãn đúng lúc nói, text là nguyên văn cụm việc.
   - **Thẻ tóm tắt để lưu**: video danh sách / hướng dẫn thì dùng `card` variant `steps` ngay trước màn chốt, liệt kê các ý nguyên văn (lược bớt chữ).
   - **Thẻ chương + chương YouTube** cho video dài có ý lớn: `CHAPTERS` trong canh.js (mốc + tên trích từ lời nói), rồi chạy `chuong.py`.

## Chọn chế độ (làm đầu tiên)

| Đầu vào | Chế độ | Làm theo |
|---|---|---|
| **1 video gốc** có người nói trước camera | Phủ đồ hoạ lên video gốc (giữ nguyên hình) | Công thức "Làm video" bên dưới |
| **Nhiều file của cùng một buổi nói / cùng cảnh** (máy quay tách file, buổi 1:1, bài giảng) | **Nối file thành một video gốc** (`ffmpeg -f concat`, bỏ đoạn theo `phan-huong.md` của tập — khối 00) rồi làm như 1 video — mẫu này có đủ kho | Công thức "Làm video" |
| **Một buổi nói dài nhiều chủ đề**, cần cắt đoạn thừa và **tách thành nhiều video theo hướng công việc** | Làm sạch + chép lời cả buổi một lần → phân hướng (`phan-huong.md`, khối 00) → `tach-video.py` → mỗi video một dự án, dựng như 1 video | `references/tach-theo-huong.md` |
| **Nhiều cảnh khác nhau** (vlog, sự kiện, clip minh hoạ chen vào lời nói), hoặc clip không nói trước camera | **Ghép nhiều clip**: tự sắp mạch, clip minh hoạ trích đúng câu nói liên quan; tự rà soát kế hoạch rồi render | `references/nhieu-doan-video.md` (khối 11, hồ sơ `ghep-vlog`) |

Mọi chế độ đều qua bước **chẩn đoán → tự chọn** (`../thiet-ke-bo-cuc/huong-dan-lua-chon.md`, bước 0: không chép kịch bản tập trước). Render đầy đủ bị
chặn tới khi `ke-hoach-canh.md` có mục `## Chẩn đoán` và video không chỉ có một kiểu lớp phủ (`soat-canh.mjs`).

Video mẫu không tính vào số video gốc. Khi người dùng gửi cả thư mục thì mọi video trong đó là video gốc theo thứ tự tên file (chế độ ghép); Claude chỉ hỏi
khi không rõ file nào là mẫu. Với yêu cầu "Giống video trước", Claude lấy token phong cách từ `~/Movies/tap-<tên>/2-ban-day-du/chuyen-dong/src` của dự án đó.

## Đầu vào

- **Video gốc**: đường dẫn file (chế độ ghép: nhiều file).
- **Video mẫu**: file video hoặc bản quay màn hình. Khi chỉ có link YouTube/TikTok thì Claude tải bản 720p **chỉ để học** vào thư mục tạm, học xong
  thì xoá (`../thiet-ke-bo-cuc/README.md` mục 4); hoặc dùng 4–8 ảnh chụp các cảnh tiêu biểu. Không có mẫu thì dùng phong cách mặc định của template. Học phong cách mẫu không tác động tới chữ ký nhận diện (khối 10).
- Yêu cầu thêm của David (thông điệp chính, tên, chỗ muốn nhấn) luôn được ưu tiên hơn suy luận.
- **Khung xuất**: cùng khung với video gốc; chỉ đổi khi David **nói rõ khung** ("làm dọc", "xuất ngang"). Yêu cầu khác làm trong khung gốc — yêu cầu **tập trung vào một vùng / bỏ phần thừa quanh chủ thể** (màn hình điện thoại, laptop, vật) thì dùng **khung chủ thể**
  (khối 04), không cắt và phóng to cả khung:

| Gốc → xuất | Cách làm | Ở đâu |
|---|---|---|
| dọc → dọc, ngang → ngang | Bình thường | — |
| **dọc → ngang** (pillar) | Video dọc giữ nguyên, đặt giữa khung 1920×1080. Hai bên là nền + chữ cùng phong cách: **trái** = chủ đề, người nói, từ khoá của ý đang nói; **phải** = danh sách ý tích luỹ dần theo lời nói. Thẻ/chữ hiện ở ô cột trái (không đè mặt); cảnh toàn màn hình thay video ở cột giữa | Khối 04, 07, 17 |
| **ngang → dọc** (reframe) | Cắt khung 9:16 bám **người đang nói**, cắt nhảy khi lượt lời chuyển (không chia đôi). **Giữ nguyên thời lượng và mọi lời nói** (vẫn làm sạch ở bước 3). Cảnh không có người / phải thấy cả khung → `wide`: cả khung ngang đặt giữa nền mờ | Khối 04 |

## Công thức — Làm video (1 video nói trước camera) · hồ sơ `lam-video`
| # | Bước | Khối | Lệnh chính |
|---|---|---|---|
| 1 | Môi trường *(bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) | `zsh $SKILL/scripts/kiem-moi-truong.sh` |
| 2 | Tạo dự án *(bước nhẹ)* | — | `zsh $SKILL/scripts/tao-du-an.sh "<video gốc>" "<video mẫu>" <tên>` (mục dưới) |
| 3 | Làm sạch (luật 5) | [02](../mo-dun/02-lam-sach/README.md) | `phan-tich-lam-sach.sh` → sửa diem-cat.json → `ap-dung-lam-sach.py` |
| 4 | Đổi khung (nếu cần) + nâng khung | [04](../mo-dun/04-khung-hinh/README.md) | `phan-tich-doi-khung.sh` + `ke-hoach-doi-khung.py sheet|apply` / `dat-dau-ra.py` · `nang-khung.py "$P" apply` |
| 5 | Chép lời + hiểu video *(bước nhẹ)* | [01](../mo-dun/01-phien-am/README.md) | `phan-tich-video.sh` |
| 6 | Phụ đề | [03](../mo-dun/03-phu-de/README.md) | `phu-de.py` → sửa từng dòng |
| 6b | **Chẩn đoán → tự chọn**: yêu cầu người dùng, loại nội dung, bố cục nền (khung gốc / khung chủ thể / pillar), lớp thông tin (bảng ghi chú chạy `GHI_CHU`, chương), mỗi cảnh Cần · Vì · Làm | [`nhu-cau-nguoi-xem.md`](../thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md) · [`huong-dan-lua-chon.md`](../thiet-ke-bo-cuc/huong-dan-lua-chon.md) · [04](../mo-dun/04-khung-hinh/README.md) | `chan-doan.py` → (`khung-chu-the.py luoi` → `apply`) |
| 7 | Phong cách (video mẫu / dự án cũ) · **tuyến nội dung → nhạc** (`project.tuyen`, bắt buộc, ghi sau ap-dung-lam-sach.py) | [10](../mo-dun/10-nhan-dien-thuong-hieu/README.md) · [09](../mo-dun/09-am-thanh/README.md) | phong-cach.md → chu-de.js |
| 8 | Kịch bản: bố cục tự cân · điểm nhấn · màn chốt nguyên văn | [07](../mo-dun/07-canh-minh-hoa/README.md) · [08](../mo-dun/08-phan-ket/README.md) · ([06](../mo-dun/06-phan-mo-dau/README.md) chỉ khi được yêu cầu) | canh.js + ke-hoach-canh.md |
| 9 | Tránh che người | [05](../mo-dun/05-tranh-che-chu-the/README.md) | `vi-tri-khuon-mat.sh` |
| 10 | Chụp thử → render → kiểm bản cuối (+ âm thanh) | [17](../mo-dun/17-kiem-soat-chat-luong/README.md) · [09](../mo-dun/09-am-thanh/README.md) | `xem-truoc.mjs` → `xuat-video.mjs` → `xem-truoc-ban-dung.py` → `kiem-khung-hinh.sh` |
| 11 | Phát hành: tiêu đề, khung bìa, màn kết/chương/teaser (YouTube video dài), thumbnail (ngang), số liệu | [15](../mo-dun/15-xuat-ban/README.md) · [08](../mo-dun/08-phan-ket/README.md) · [14](../mo-dun/14-anh-thu-nho/README.md) · [16](../mo-dun/16-phan-tich-so-lieu/README.md) | `doan-gioi-thieu.py` · `chuong.py` · `anh-thu-nho.sh` |
| 12 | Bàn giao bản cuối ngay khi hoàn thành, **tải đủ toàn bộ lên Drive** (David 25/11/2026; không chờ duyệt trước khi bàn giao, cây quy trình lá A6) → David góp ý (lá B13: sửa, tải bản mới lên, xoá bản cũ) hoặc chốt → David chốt thì tự dọn dẹp, đưa dự án lên Drive, xoá bản gốc theo quy trình (`../quy-tac-chung.md` mục 8) | [17](../mo-dun/17-kiem-soat-chat-luong/README.md) | `cho-dang.sh gui <tập>` → `don-tap.py --xoa <dự án>` → `luu-drive.sh <dự án>` (nền) |

### Tạo dự án
`$SKILL` trong mọi lệnh của skill này: `SKILL=~/Documents/bo-nao-david/ky-nang/san-xuat-video/dung-video-theo-phong-cach` (thiết bị đã cài
bộ não: `~/.claude/skills/dung-video-theo-phong-cach` trỏ tới cùng thư mục). Khi không có video mẫu thì để `""`.

```bash
zsh $SKILL/scripts/tao-du-an.sh "<video gốc>" "<video mẫu>" <tên-ngắn>
```
Script tạo `~/Movies/tap-<tên>/2-ban-day-du/` (gốc tự đặt vào `tap-<tên>/1-goc/`; tên `vlog-…` thì vào `~/Movies/vlog/<tên>/`) với cấu trúc chuẩn
(cuối file), chép video, chép template Remotion vào `chuyen-dong/`, điền thông số vào `chuyen-dong/src/du-an.js`, cài gói npm. Dòng cuối là `$P`.

## Bảng phụ thuộc (sửa X thì chạy lại Y)
| Sửa | Chạy lại |
|---|---|
| diem-cat.json (làm sạch) | ap-dung-lam-sach.py → nang-khung.py apply → phan-tich-video.sh → phu-de.py → dời mốc canh.js → vi-tri-khuon-mat.sh → render |
| canh.js (mốc / loại cảnh) | vi-tri-khuon-mat.sh → `node xuat-video.mjs <id>` → xem-truoc-ban-dung.py |
| phu-de.js | `node xuat-video.mjs phu-de` → xem-truoc-ban-dung.py |
| chu-de.js / brand | render lại tất cả |
| du-an.js (topic, ytEnd, schedule) — ghi lại SAU ap-dung-lam-sach.py (script này ghi đè du-an.js) | `node xuat-video.mjs the-cuoi` → xem-truoc-ban-dung.py |
| video-hoan-chinh (teaser) | chuong.py |
| hồ sơ lam-video | chạy lại khối dùng khoá đó (bảng khoá trong ho-so-thuong-hieu/lam-video.md) |

## Tiêu chí đạt (rà soát trước khi bàn giao)
- Không có thẻ tiêu đề mở đầu trừ khi được yêu cầu · có điểm nhấn, vài kiểu phù hợp nội dung, video không rối · không che mặt, không có chữ lớn tự do đè lên người
- Bố cục phù hợp nội dung (xem ảnh tĩnh: người / ý có rõ không) · phụ đề đúng chữ, không bị đè · tiếng Việt đủ dấu · không có gì tràn vùng đỏ
- Màn chốt nguyên văn + thẻ cuối (video dọc ngắn: màn chốt trên hình, không thẻ cuối, không thanh thời gian — `../thu-vien-tai-nguyen/nhan-dien-chung.md` mục 1) · (YouTube video dài) màn kết, chương, teaser · thumbnail nếu xuất ngang · phat-hanh.md + so-lieu.md
- Âm lượng theo chuẩn chung, tiếng rè không tăng so với nguồn; thời lượng đúng

## Sửa theo góp ý

David thường góp ý kiểu "cảnh 2:08 chữ to quá", "đổi hình thợ hồ", "bỏ cảnh AI". Claude sửa đúng chỗ trong `canh.js`/component/ảnh;
nếu đổi mốc thì chạy lại `python3 -I $SKILL/scripts/vi-tri-khuon-mat.py "$P"`; sau đó chạy `node xuat-video.mjs <id>` (chỉ cảnh đó), rồi `xem-truoc-ban-dung.py`, rồi
kiểm khung hình quanh mốc đó. Đổi phong cách toàn bộ thì sửa `chu-de.js`, render lại tất cả.
Với yêu cầu "Giữ lại đoạn bị cắt"/"cắt thêm đoạn X", Claude đổi mốc bản cuối sang mốc thô bằng `cac-doan.json`, sửa `diem-cat.json`, lưu bản `cac-doan.json`
cũ, chạy `ap-dung-lam-sach.py`, dời mốc mọi cảnh (`start`, `end`, `at`…) theo bảng mới. Chỉ render lại cảnh có điểm thay đổi nằm **bên trong**
cảnh đó, rồi chạy `xem-truoc-ban-dung.py`.

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

**Chuẩn bắt buộc** gồm các mục dưới đây. Với bản cuối, đối chiếu đoạn cắt với âm thanh gốc tại chỗ nối và các câu có điều kiện, phủ định hoặc số liệu. Xem lại các mốc đồ họa xuất hiện để xác nhận nhân vật, vật thể hoặc chữ đang mang thông tin vẫn nhìn rõ. Ghi mốc đã kiểm trong bàn giao.

**Phạm vi sáng tạo** gồm cách minh họa, bố cục và nhịp xuất hiện đồ họa theo nội dung, trong giới hạn nhận diện và vùng an toàn. Ghi lựa chọn đáng kể cùng lý do giúp người xem, sau khi bản cuối qua chuẩn bắt buộc.

1. Claude không hỏi giữa chừng, trừ khi có tín hiệu nặng; khung xuất đúng khung gốc trừ khi David yêu cầu đổi; báo cáo có "đã chọn X vì Y".
2. Chữ trên video (kể cả màn chốt) là nguyên văn lời David; không có thẻ tiêu đề trừ khi được yêu cầu.
3. Video dài được để nguyên; video ngắn được làm sạch mà không mất ý.
4. Có motion graphics phù hợp nội dung (vài kiểu, không rối), bố cục tự cân, không che mặt, không có gì tràn vùng đỏ.
5. Phụ đề đúng chữ, đủ dấu, không bị đè; âm lượng đạt chuẩn chung.
6. Đã chụp kiểm tra đúng các mốc dễ lỗi trước khi bàn giao.
7. Đủ gói phát hành (tiêu đề, khung bìa, thumbnail nếu xuất ngang, mẫu số liệu); David không phải sửa lại vì vi phạm luật đã chốt.
8. Đã bàn giao bản cuối ngay khi hoàn thành, tải đủ toàn bộ lên Drive `thanh-pham/<tập>/` (cả bản xem dung lượng thấp; `_buoi-<buổi>/` khi tách theo hướng), đã so khớp. Sau khi David chốt: bản cuối ở `~/Movies/cho-dang/<tập>/` và Drive `thanh-pham/<tập>/` (✅ trên trang `localhost:8765/mac`); đã chạy `don-tap.py --xoa` rồi `luu-drive.sh`; tập đã lên Drive `sao-luu-mac/video`, đã xoá trên Mac, đã ghi loại vào `du-an/kho-drive.md`; phần ⏸ (làm chưa xong) đã hỏi David.

## Tài liệu kèm (chỉ đọc khi bước cần, khi cân nhắc đổi luật hoặc gỡ lỗi)

- `references/loi-thuong-gap.md` — lỗi đã gặp và cách tránh (đọc một lần ở đầu phiên).
- `references/doan-thu.md` — dựng đoạn thử ngắn cho David xem trước khi dựng cả video.
- `references/tach-theo-huong.md` — tách một buổi dài thành nhiều video theo hướng (`tach-video.py`).
- `references/phan-tich-phong-cach.md` — đọc video mẫu thành token phong cách; bảng font Google có tiếng Việt.
- `references/thiet-ke-canh.md` — các loại cảnh có sẵn, khi nào dùng loại nào, vùng an toàn.
- `references/vi-du-canh.js` — kịch bản 17 cảnh thật đã duyệt.
- `references/nhat-ky-thay-doi.md` — sổ quyết định theo ngày + lý do.
- `references/ban-giao.md` — mẫu báo cáo.
- `references/nhieu-doan-video.md` + `references/vi-du-danh-sach-cat.js` — chế độ ghép nhiều clip; kịch bản ghép thật đã duyệt.
- `../mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` — mẫu số liệu sau khi đăng.
- Template Remotion dùng chung với **dung-podcast**: `san-khau.jsx`, composition `nen`, `nguoi-noi.js`, `duong-bao-am.js`, nhánh
  `project.podcast` trong bo-cuc.js — chỉ bật khi `project.podcast`; khi sửa template thì giữ nguyên các phần này.
- `assets/mau-dung-ghep/` + `scripts/tao-dung-ghep.sh` — template dựng cả video có tiếng cho chế độ ghép.
