---
description: "Tái bản 3 toàn bộ bộ não (mở 14/11): file theo dõi chung của phiên điều phối — máy đo lúc mở, file từng phiên con, chéo bộ, hỏi David, kiểm chung."
---

# Tái bản 3 — toàn bộ bộ não (mở 14/11/2026)

David duyệt 4 phần 14/11: 4 phiên con chạy cùng lúc · `co-so-tri-thuc/david.md` để nguyên, chỉ ghi chỗ lệch · việc thật là đoạn ngắn `thu-tai-ban-3`. Mốc trước: `tai-ban-3-truoc`. Skill: [tai-cau-truc](../../ky-nang/tai-cau-truc/SKILL.md). Đợt 2 ([tai-cau-truc-2.md](tai-cau-truc-2.md)) xong nội dung 10/11 nhưng chưa gắn tag: ghi bù vào lịch sử khi đóng đợt 3.

Luật thêm cho đợt này: mọi file viết lại giữ khối `description:` và link ([quy-uoc-lien-ket.md](../../co-so-tri-thuc/quy-uoc-lien-ket.md)); phiên con không commit, không chạy `dong-bo.sh`.

## File của từng phiên con
- [tai-ban-3-video.md](tai-ban-3-video.md)
- [tai-ban-3-hoi.md](tai-ban-3-hoi.md)
- [tai-ban-3-nao.md](tai-ban-3-nao.md)
- [tai-ban-3-ghi-nho.md](tai-ban-3-ghi-nho.md)

## Công cụ đo lúc mở
```

## Bộ video — 50 file bản luật · mốc tái bản gần nhất: tai-ban-video-1
  dau_ngay 11/30 · ghi_de 0/15 · trung 2/8 · sua 7/40 · dong 3450/4000
  File chồng nhiều nhất:
   - ky-nang/san-xuat-video/mo-dun/04-khung-hinh/README.md: 2 dấu ngày · 0 câu ghi đè · 85 dòng
   - ky-nang/san-xuat-video/quy-tac-chung.md: 2 dấu ngày · 0 câu ghi đè · 123 dòng
   - ky-nang/san-xuat-video/thiet-ke-bo-cuc/tu-chon.md: 2 dấu ngày · 0 câu ghi đè · 97 dòng
   - ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md: 1 dấu ngày · 0 câu ghi đè · 206 dòng
   - ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/loi-thuong-gap.md: 1 dấu ngày · 0 câu ghi đè · 243 dòng
   - ky-nang/san-xuat-video/mo-dun/07-canh-minh-hoa/README.md: 1 dấu ngày · 0 câu ghi đè · 181 dòng
  Câu trùng ở nhiều file (2): (3 câu đầu, --chi-tiet để xem hết)
   - "tự chọn cách trình bày: trước kịch bản cảnh, chẩn đoán + chọn theo ../thiet ke bo cuc/tu c…" ở ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md, ky-nang/san-xuat-video/dung-podcast/SKILL.md
   - "lớp thông tin, kiểu cảnh theo dạng câu nói; ghi "đã chọn x vì y" vào kế hoạch cảnh.…" ở ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md, ky-nang/san-xuat-video/dung-podcast/SKILL.md
  ⇒ bộ video dưới ngưỡng.

## Bộ hoi — 1 file bản luật · mốc tái bản gần nhất: chưa có
  dau_ngay 0/8 · ghi_de 0/4 · trung 0/3 · sua 4/15 · dong 88/300
  File chồng nhiều nhất:
  ⇒ bộ hoi dưới ngưỡng.

## Bộ nao — 5 file bản luật · mốc tái bản gần nhất: chưa có
  dau_ngay 5/15 · ghi_de 2/6 · trung 0/4 · sua 30/25 · dong 242/600
  File chồng nhiều nhất:
   - AGENTS.md: 0 dấu ngày · 1 câu ghi đè · 65 dòng
   - co-so-tri-thuc/chi-dan-toan-cuc.md: 0 dấu ngày · 1 câu ghi đè · 8 dòng
   - co-so-tri-thuc/david.md: 3 dấu ngày · 0 câu ghi đè · 51 dòng
   - ky-nang/chuan-muc-lam-viec.md: 2 dấu ngày · 0 câu ghi đè · 114 dòng
  ⇒ bộ nao vượt ngưỡng: sua 30 > 25

⇒ NÊN TÁI BẢN TOÀN BỘ (skill tai-cau-truc): vượt ngưỡng ở nao (sua 30 > 25)
```

## Chéo bộ (phiên điều phối gom và chốt nguồn)
- Giao phiên não: luật "nội dung là của David, không khuôn lời" mất nguồn nên về `chuan-muc-lam-viec.md` mục 0; "chờ ok" thành "duyệt"; luật `quy-tac-david-md-chi-dieu-co-dinh` về chuan-muc mục 4; AGENTS luật 2 và chi-dan-toan-cuc rút còn câu tóm + trỏ chuan-muc mục 2.
- Giao phiên ghi nhớ: viết lại thân các ghi nhớ còn chồng lớp (`quy-tac-goi-y-de-david-chon`, `quy-tac-phien-telegram-tu-chay`, `quy-tac-ky-nang-tu-cai-tien`, `video-khong-tu-xuat`, `video-podcast-phu-hinh-30`, `video-bo-cuc-tu-can`, `video-kien-truc-ky-nang`), `.gitignore` cho `luu-tru/thiet-bi-*`, chép lại mô tả ở `ban-do/`.
- Để nguyên: `tu-dong-hoa/so-tay/README.md` còn dấu ngày (ngoài ba bộ, không đo); `du-an/danh-gia-luat.md` là biên bản cũ.
- Ghi nhớ trỏ bản luật theo số mục: kiểm lại bằng `grep -n "mục [0-9]" co-so-tri-thuc/bo-nho/*.md` sau khi các phiên xong.


## Hỏi David (gom một lần)
David trả lời 14/11, chọn cả 4 đề xuất:
1. Ken Burns: luật không zoom chỉ áp hình quay; ảnh minh hoạ và chuyển động trong đồ hoạ vẫn được trôi chậm thì phiên video viết rõ.
2. `david.md` mục 3.1: giữ một câu đủ ý, bỏ dấu ngày "(14/11/2026)" thì phiên điều phối đã sửa.
3. Đổi tên `quy-tac-mod-tu-chay` thành `quy-tac-khong-dung-mod-giao-dien`, `video-khong-tu-xuat` thành `video-gop-y-render-lai` rồi phiên điều phối làm sau khi phiên ghi nhớ xong.
4. Skill cũ `hoi-chuyen-gia` (đồng bộ từ claude.ai): David tự tắt trên claude.ai.
Câu nhỏ không cần hỏi (theo đề xuất phiên con): giữ ghi nhớ `video-ban-chuan-2026-11-06`, `video-lam-lai-video-cu` tới khi có bộ mẫu mới; dòng "Sáu luật nền" ở david.md để nguyên.


## Kiểm chung
- [x] Đủ luật: 4 bảng (video 78 · hỏi 24 · não 35 · ghi nhớ 48), mọi dòng "sống" có nguồn duy nhất; luật "nội dung là của David" đã có nguồn duy nhất lại (chuan-muc mục 0)
- [x] Công cụ đo: video 0·0·0, hỏi 0·0·0, não ghi đè 0 · trùng 0 · 2 dấu ngày là ngày dữ kiện trong david.md; "sua 31" về 0 khi gắn tag `tai-ban-3`
- [x] Mẫu chuẩn (15/11): 5 mẫu podcast chạy được. 3 clip dọc giữ nguyên (SSIM 0,976 / 0,980 / 0,976). 2 bản podcast ngang đổi hình (`podcast-dai-trainer` 0,873, `podcast-dai-muc-tieu` 0,876) vì đúng luật "mỗi lúc một chỗ chữ" (08/11, sau `chuan.jpg` 06/11): phụ đề nhường khi cảnh / chữ chính hiện, còn lại nằm sát đáy. Các lớp khác như cũ. David duyệt chốt (15/11): hai bản ngang đã thành `chuan.jpg` mới.
  Cách dựng lại dự án mẫu (Mac không giữ): chép `motion/` từ Drive `sao-luu-mac/video/<tap>/{2-ban-dai,3-highlight/clip-X}` về `~/Movies/<tap>/{2-ban-day-du,3-doan-noi-bat/clip-X}/chuyen-dong` (bỏ `thumb`), đổi tên file `captions→phu-de, scenes→canh, project→du-an, placement→vi-tri, speakers→nguoi-noi, envelope→duong-bao-am, highlight→doan-noi-bat, output→dau-ra`, sửa `from './project.js'` trong `canh.js`, tạo `tu-lieu/` rỗng, `npm install` theo `package.json` của `khuon-remotion` rồi liên kết `node_modules`. Chạy xong thì xoá.
- [x] Việc thật `thu-tai-ban-3`: clip dọc 46 s (`~/Movies/tap-thu-tai-ban-3/3-doan-noi-bat/clip-A/video-hoan-chinh.mp4`, −13,8 LUFS). David chấm (15/11): "Đạt, đóng mốc"

## Đóng mốc (15/11/2026)
- Tag `tai-ban-3`, dòng đợt 3 (kèm ghi bù đợt 2) trong `ky-nang/tai-cau-truc/lich-su.md`; ngưỡng `bo.json` giữ nguyên (sau tag mọi bộ dưới ngưỡng).
- [x] Công cụ kiểm tra liên kết 0 / 0

## Lỗi tìm ra khi chạy việc thật (có từ chuẩn hoá tên 14/11, không do tái bản)
- `cat-doan-noi-bat.py`, `danh-sach-cat-doan-noi-bat.py` gọi `import pauses` nhưng file đã đổi thành `khoang-lang.py` (tên có gạch nối không import được) thì đã sửa: nạp theo đường dẫn.
- `tao-doan-noi-bat.sh` lấy `tu-lieu/video-goc.mp4` của dự án gốc — với bản dài kiểu "khung chủ thể" thì file này đã có khung bo góc trên nền tối, cắt dọc bị lệch mặt. Việc thật dùng `video-goc-tho.MP4` (hình quay gốc) + tiếng đã cân. nay đã sửa (15/11): có `video-goc-tho.*` cùng độ dài thì hình lấy từ bản thô, tiếng lấy từ bản đã cân; lệch quá 0,5 s (bản dài đã làm sạch / cắt, ví dụ `tap-cuoc-goi-hop-tac`) thì báo và dùng `video-goc.mp4` như cũ.
- `kiem-mau.py` dòng 43: bỏ `makedirs`, chỉ giữ lối tắt `tu-lieu` nay đã sửa (15/11).
