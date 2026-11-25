---
description: "Tái bản 3 (14/11), phiên con bộ ghi-nho: bảng từng ghi nhớ (nội dung, bản luật trỏ tới, trùng, còn đúng), việc đã dọn, chéo bộ, hỏi David."
---

# Tái bản 3 — bộ ghi-nho

Phiên điều phối: [tai-ban-3.md](tai-ban-3.md). Đợt trước: [tai-cau-truc-2-ghi-nho.md](tai-cau-truc-2-ghi-nho.md).
Phạm vi: `co-so-tri-thuc/bo-nho/` (ghi nhớ = sổ quyết định: ngày + lời David + lý do; luật hiện hành ở bản luật mỗi ghi nhớ trỏ tới).

**Trước:** 48 ghi nhớ đang dùng + 6 trong `luu-tru/`. **Sau:** 47 đang dùng + 7 trong `luu-tru/`.
Kiểm 14/11: `MEMORY.md` 47 dòng = 47 file; mọi `name:` = tên file; mọi ghi nhớ có dòng "Nhà của luật" hoặc là ghi nhớ việc / tham chiếu;
công cụ kiểm tra liên kết: link gãy 0, mồ côi 0.

## Bảng ghi nhớ

Cột "Bản luật": **có** = trỏ đúng và luật có ở đó · **thêm** = trước không trỏ, nay đã thêm dòng "Nhà của luật" · **sửa** = trỏ sai, đã sửa ·
**—** = ghi nhớ việc / tham chiếu, không chứa luật.

| Ghi nhớ | Nội dung chính | Bản luật | Trùng với | Còn đúng | Đã làm |
|---|---|---|---|---|---|
| quy-tac-cong-cu-cai-dua-vao-ky-nang | Công cụ David cài (pyannote) là để nâng skill → đề xuất tích hợp, giữ cách cũ dự phòng (07/11) | có: chuan-muc mục 3 | — | đúng | `name:` theo tên file |
| quy-tac-david-md-chi-dieu-co-dinh | david.md chỉ ghi điều cố định; ý tưởng → danh-sach-y-tuong (12/11) | thiếu câu riêng (gần: quy-uoc-lien-ket "Ghi chú kiến thức") | — | đúng | thêm dòng nhà gần nhất; Chéo bộ 1 |
| quy-tac-duyet-ke-hoach-4-phan | Mọi việc trình 4 phần, duyệt rồi làm trọn; việc tự chạy hiện thành phiên (14/11) | có: chuan-muc mục 2 | chạm goi-y, tu-cai-tien, telegram (mỗi cái đã có đoạn 14/11 trỏ về đây) | đúng, mới nhất | giữ |
| quy-tac-goi-trainer-chung | Gói hướng 3 chỉ dạy một kỹ năng thuần, mọi AI, máy học viên (13/11) | thêm: san-pham-hoa/SKILL | — | đúng | thêm dòng nhà |
| quy-tac-goi-y-de-david-chon | Tài nguyên vào → kết quả ra, không hỏi giữa chừng, báo "chọn X vì Y" (11/11) | có: chuan-muc mục 2 + thu-thap-yeu-cau | duyet-4-phan (khác quyết định: 11/11 trong lúc làm, 14/11 trước khi làm) | đúng phần "sau khi duyệt"; phần "không hỏi trước" đã bị 14/11 thay, file đã ghi | sửa description cho khớp 14/11 |
| quy-tac-hoc-la-bo-sung | Học mẫu chỉ thêm, giữ chặn cũ; khung mới chụp đủ lớp; cửa vào phan-tich-video-mau (08/11) | có: thiet-ke-bo-cuc/README mục 4 | tham-my (10/11 nới, đã ghi) | đúng | giữ |
| quy-tac-ket-qua-hon-toc-do | Kết quả hơn tốc độ; bước cần render thì chờ (05/11) | thêm: chuan-muc mục 0 điểm 1 | — | đúng | thêm dòng nhà |
| quy-tac-khong-tu-chay-viec-cua-david | Không tự Chạy tiếp/Duyệt/Làm lại việc David; việc thử tên `thu-…` (08/11) | có: chuan-muc mục 3 | — | đúng | giữ |
| quy-tac-ky-nang-tu-cai-tien | Sáu luật 12/11: tự học theo số liệu, lời mới nhất thắng, GitHub 100% | có: AGENTS sáu luật + hoc-lien-tuc | duyet-4-phan (14/11 bỏ "chỉ hỏi khi đụng David", đã ghi) | đúng trừ phần đã ghi bị thay | `name:` theo tên file; sửa description (bỏ "chỉ hỏi khi đụng David") |
| quy-tac-mod-tu-chay | Không dùng mod giao diện, chỉ giữ Telegram (13/11, thay 11/11) | thêm: cai-dat-bo-nao.sh + chuan-muc | — | đúng (tên file ngược nội dung: Hỏi David 1) | thêm dòng nhà |
| quy-tac-noi-dung-cua-david | Nội dung của David, skill lo hình; người xem trung tâm (05/11, gộp 10/11) | thêm: quy-tac-chung mục 0, 1 | — | đúng | thêm dòng nhà |
| quy-tac-phien-telegram-tu-chay | Phiên Telegram tự chạy, chỉ hỏi khi đăng/tốn tiền/đẩy đè; Remote Control, hỏi đóng phiên (12/11, 14/11) | có: cong-duyet.py + chuan-muc mục 5 | duyet-4-phan (đã ghi) | đúng | giữ |
| quy-tac-sua-thang-tai-ban | Sửa thẳng câu luật; tái bản toàn bộ một đợt (10/11) | có: chuan-muc mục 4 + tai-cau-truc | — | đúng | giữ |
| quy-tac-thu-bang-doan-ngan | Thử skill bằng đoạn ngắn trọn một ý (09/11) | có: quy-tac-chung mục 8 | — | đúng | giữ |
| quy-tac-tu-hoi-khi-mo-ho | 6 tín hiệu tự dừng hỏi (05/11) | có: thu-thap-yeu-cau "Sáu tín hiệu" | — | đúng | giữ |
| co-so-tri-thuc-github-ban-goc | GitHub là bản gốc, đẩy ngay, đồng bộ 2 chiều, repo + "cập nhật não" (07/11) | thêm: AGENTS luật 6 + huong-dan-cai-dat | — | đúng | thêm dòng nhà |
| co-so-tri-thuc-ho-so-va-bo-loc | Đường dẫn hồ sơ, bộ lọc khối 00, kenh.json, sổ danh mục, đăng MXH | — (tham chiếu) | — | đúng | đường bộ lọc `~/.claude/skills/…` → `ky-nang/…` |
| co-so-tri-thuc-lien-ket-tri-thuc | Bộ não là mạng lưới file nối nhau, không dùng Obsidian (14/11) | có: quy-uoc-lien-ket | — | đúng | giữ |
| co-so-tri-thuc-quy-uoc-dat-ten | Tên từ thuật ngữ kinh doanh tiếng Anh, dịch đúng nghĩa, không ngoại lệ (14/11) | thêm: AGENTS + bang-thuat-ngu | — | đúng | thêm dòng nhà |
| thiet-bi-bo-cuc-thu-muc | Bố cục thư mục Mac chính (11/11) | — (tham chiếu máy) | thiet-bi-don-documents (cùng chủ đề) | sai đường: `David.Claude`, `dang-lam/kho-drive.md`, `_so-danh-muc`, `1-nghe-trainer`, tiền tố `may-`, `sao-luu-mac/Documents` | `name:` theo tên file; viết lại đường theo tên 14/11; **nhận phần gộp** sổ dọn 07/11 |
| thiet-bi-don-documents-2026-11-07 | Dọn ~/Documents 07/11, bỏ App notion | — | thiet-bi-bo-cuc-thu-muc | cũ (David.Claude đổi tên, mk.csv đã xoá 11/11); quyết định "App notion bỏ" vẫn sống | **gộp** vào thiet-bi-bo-cuc-thu-muc, file chuyển `luu-tru/` |
| thiet-bi-van-phong-shop | Văn Phòng Shop là mẫu cho công ty, tách khỏi bộ não (14/11) | — (việc) | — | đúng | giữ |
| video-anh-viet-nam | Nhiều ảnh thật, chỉ Việt Nam (13/11) | có: quy-tac-chung mục 4 | — | đúng | giữ |
| video-ban-chuan-2026-11-06 | 5 video chuẩn, mau.json 5 mẫu (06/11) | — (việc) | doc-khuon (cùng 3 clip mẫu, khác ý) | sai đường `du-an/phat-hanh-cu/` (đã bỏ khỏi repo 07/11) | sửa đường → Drive / kho-drive |
| video-bo-cuc-tu-can | Bỏ số cố định; tránh mọi người, bám người nói; khung gốc thiet-ke-bo-cuc (07/11, 08/11) | có: thiet-ke-bo-cuc | tham-my (đã ghi) | đúng | giữ |
| video-bo-ung-dung | Bỏ app dựng video, dựng trong phiên (10/11) | có: quy-tac-chung mục 8 | — | đúng | `name:` theo tên file |
| video-chi-hinh-cua-chinh-video | Hình bìa chỉ từ chính video đó (05/11) | sửa: "quy-tac-chung 7" không có luật này → khối 14 | — | đúng | sửa đường trỏ |
| video-chu-nguyen-van | Chữ trên video nguyên văn, không tít tự rút (07/11) | có: quy-tac-chung mục 1 + AGENTS luật 3 | — | đúng | giữ |
| video-chu-nhan-nhan-dan | Chữ nhấn kiểu nhãn dán, không chạm mặt (13/11) | có: nhan-dien-chung mục 2 | — | đúng | giữ |
| video-chuyen-qua-drive | Drive chỉ giữ việc của David; Mac chỉ việc đang làm (08/11, 11/11) | thêm: chuan-muc mục 4 "Giữ Mac nhẹ" + kho-drive | thiet-bi-bo-cuc (chuyện xoá Codex, mỗi bên trỏ nhau) | đúng | thêm dòng nhà |
| video-clip-ngan-dung-doc-lap | Clip ngắn đứng độc lập, bốn câu (06/11, 07/11) | có: cat-doan-noi-bat/SKILL | — | đúng | giữ |
| video-dai-khong-cat | Video dài không cắt (05/11) | có: quy-tac-chung mục 2 + khối 00 | — | đúng | giữ |
| video-do-hoa-ke-chuyen | Motion graphics kể chuyện, vẽ tiếp; AI sáng tạo trong khung (07/11, 09/11) | có: chuan-muc đầu file + khối 07 | — | đúng | `name:` theo tên file |
| video-doc-khuon-chu-chinh | Mẫu podcast dọc chữ chính, 3 clip mẫu (06/11, sửa 10/11) | có: cat-doan-noi-bat "Kịch bản highlight podcast (7B)" | nhan-dien-chung (dọc ngắn, trỏ nhau) | đúng | giữ |
| video-hieu-hon-cau-ki | Hiểu hơn cầu kì; bỏ chữ sau người (10/11) | có: quy-tac-chung mục 0 | — | đúng | giữ |
| video-khong-cai-hyperframes | Giữ Remotion, không cài HyperFrames (06/11) | thêm: thiet-ke-bo-cuc/README mục 4 điểm 10 | — | đúng | thêm dòng nhà |
| video-khong-nhan-ky-thuat | Không nhãn ×1,6 / slow-mo | sửa: trỏ SKILL.md (không có) → quy-tac-chung mục 4 | — | đúng | sửa đường trỏ |
| video-khong-tu-xuat | 13/11: góp ý thì render lại toàn bộ, bỏ cổng 1, 2 (thay 05/11) | có: quy-tac-chung mục 8 + phan-phoi-da-kenh | goi-y (khác: 11/11 chung, 13/11 riêng video) | đúng (tên file ngược nội dung: Hỏi David 1) | `name:` theo tên file |
| video-kien-truc-ky-nang | Kiến trúc bộ skill video: hồ sơ, 20 khối, mẫu chuẩn (04/11) | thêm: tong-quan.md | — | đúng | `name:` theo tên file; đường `ky-nang/…`; thêm dòng nhà |
| video-lam-lai-video-cu | Làm lại video kênh cũ (08/11) | thêm: khối 02 "Làm lại video cũ" | — | đúng | thêm dòng nhà |
| video-nhac-theo-tuyen | Tự chọn nhạc theo tuyến; khoảng 23 dB, −14 LUFS (05–08/11) | có: khối 09 + chung.json | — | đúng | giữ |
| video-nhan-dien-chung | Một bộ nhận diện; dọc ngắn bỏ thanh + thẻ cuối (08/11, 10/11) | có: nhan-dien-chung.md + quy-tac-chung mục 5 | doc-khuon (trỏ nhau) | đúng | giữ |
| video-phu-de-mot-cho-chu | Phụ đề dọc 5–8 chữ; mỗi lúc một chỗ chữ (08/11) | có: quy-tac-chung mục 3 | — | đúng | giữ |
| video-podcast-bia-khong-mat | Bìa podcast không mặt (06/11) | có: khối 14 | — | đúng | giữ |
| video-podcast-phu-hinh-30 | Podcast phủ hình khoảng 30% (06/11, 11/11) | thêm: dung-podcast/SKILL | — | đúng | thêm dòng nhà |
| video-tham-my-chi-giu-nhan-dien | Thẩm mỹ chỉ giữ chữ ký nhận diện (10/11) | có: nhan-dien-chung mục 0 | — | đúng | giữ |
| video-thu-muc-xep-theo-tap | ~/Movies xếp theo tập (07/11) | có: noi-luu.sh | — | đúng | `name:` theo tên file; đường `ky-nang/…` |
| video-tu-chon-theo-noi-dung | Tự chẩn đoán rồi chọn trong kho (11/11) | có: thiet-ke-bo-cuc/tu-chon.md | — | đúng | giữ |
| luu-tru/co-so-tri-thuc-kho-bo-nao | (gộp 08/11 vào github-ban-goc) | — | — | lịch sử | giữ |
| luu-tru/video-chuan-am-luong | (gộp 10/11 vào nhac-theo-tuyen) | — | — | lịch sử | giữ |
| luu-tru/video-doc-ngan-khong-thanh | (gộp 10/11 vào nhan-dien-chung) | — | — | lịch sử | giữ |
| luu-tru/video-luon-co-do-hoa-chuyen-dong | (gộp 10/11 vào do-hoa-ke-chuyen) | — | — | lịch sử | giữ |
| luu-tru/video-nguoi-xem-trung-tam | (gộp 10/11 vào noi-dung-cua-david) | — | — | lịch sử | giữ |
| luu-tru/video-quy-trinh-dung-theo-phong-cach | (cũ) | — | — | lịch sử | giữ |
| luu-tru/thiet-bi-don-documents-2026-11-07 | (gộp 14/11 vào thiet-bi-bo-cuc-thu-muc) | — | — | lịch sử | mới chuyển, có ghi chú đầu file |

Bốn ghi nhớ cùng đụng "khi nào hỏi / duyệt" (goi-y 11/11, tu-cai-tien 12/11, telegram 12/11, duyet-4-phan 14/11) **không gộp**: mỗi cái ghi một
quyết định khác, ba cái cũ đã có đoạn 14/11 trỏ về duyet-4-phan. Không ghi nhớ nào bị bỏ quyết định mà không có quyết định mới hơn thay.

## Chéo bộ

1. **nao** — `quy-tac-david-md-chi-dieu-co-dinh`: câu "david.md chỉ ghi điều cố định đã chốt; ý tưởng, góp ý đang cân nhắc ghi
   `du-an/danh-sach-y-tuong.md`, chỉ đưa vào david.md khi David chốt" chưa có trong bản luật (quy-uoc-lien-ket chỉ có "ý tưởng chưa chốt
   ở danh-sach-y-tuong"). Đề xuất nguồn: `ky-nang/chuan-muc-lam-viec.md` mục 4 (Cuối việc, chỗ ghi góp ý).
2. **điều phối** — ghi nhớ trỏ bản luật theo **số mục** (quy-tac-chung mục 0–5, 8; chuan-muc mục 0, 2–5; thiet-ke-bo-cuc/README mục 4
   điểm 10; nhan-dien-chung mục 0, 2). Đã khớp bản trên đĩa lúc 14/11 (sau sửa của phiên video). Phiên nào đổi số mục khi viết lại thì
   kiểm lại: `grep -n "mục [0-9]" co-so-tri-thuc/bo-nho/*.md`.
3. **nao** — `bao-cao-trang-thai.md` dòng app dựng video nhắc `video-bo-app` nên đã sửa thành `video-bo-ung-dung` (chỉ đường trỏ).
   `du-an/danh-gia-luat.md` (biên bản cũ) còn `video-khong-tu-render`, `video-kien-truc-skill`: để nguyên như tái bản 2.
4. **nao / điều phối** — `.gitignore`: thêm dòng `co-so-tri-thuc/bo-nho/luu-tru/thiet-bi-*` để ghi nhớ `thiet-bi-` chuyển lưu trữ vẫn
   không lên GitHub. Các trang `ban-do/` chép mô tả ghi nhớ: đã chuyển dòng `thiet-bi-don-documents` sang mục Lưu trữ của
   `ban-do/bo-nao-va-tu-dong-hoa.md`; mô tả của `quy-tac-ky-nang-tu-cai-tien`, `quy-tac-goi-y-de-david-chon`, `thiet-bi-bo-cuc-thu-muc`
   đã đổi nên chữ ở bản đồ hơi lệch (link không gãy) — phiên giữ bản đồ chép lại nếu muốn.
5. **video** — giữa chừng công cụ kiểm tra báo 2 mồ côi là file mới của phiên video (`nhat-ky-thay-doi.md` của phan-phoi-da-kenh,
   phan-tich-video-mau); lần kiểm cuối 14/11 đã về 0.

## Hỏi David

1. **Đổi tên 2 ghi nhớ có tên ngược nội dung:** `quy-tac-mod-tu-chay` (nội dung: không dùng mod giao diện) và `video-khong-tu-xuat`
   (nội dung: góp ý thì render lại toàn bộ). **Đề xuất:** đổi thành `quy-tac-khong-dung-mod-giao-dien` và `video-gop-y-render-lai`,
   phiên điều phối làm khi mọi phiên con xong (để không đụng file bộ khác đang viết lại), sửa mọi đường trỏ cùng lúc.
2. **Ghi nhớ việc đã xong** `video-ban-chuan-2026-11-06`, `video-lam-lai-video-cu` (tái bản 2 đã hỏi, chưa có trả lời). **Đề xuất:** giữ,
   vì bộ mẫu chuẩn và cách bỏ dấu vết kênh cũ còn dùng; chuyển `luu-tru/` khi có bộ mẫu mới.

## Đã viết lại

- `name:` 9 ghi nhớ đổi theo tên file (tên cũ trước chuẩn hoá 14/11: `-skill`, `-app`, `may-`, `motion-`, `-render`, `movies-`).
- Gộp `thiet-bi-don-documents-2026-11-07` → `thiet-bi-bo-cuc-thu-muc`; bản cũ ở `bo-nho/luu-tru/`.
- Sửa đường trỏ: `video-ban-chuan` (phat-hanh-cu), `video-chi-hinh` (khối 14), `video-khong-nhan-ky-thuat` (quy-tac-chung mục 4),
  `~/.claude/skills/…` → `ky-nang/…` ở 3 ghi nhớ, đường cũ trong `thiet-bi-bo-cuc-thu-muc`.
- Thêm dòng "Nhà của luật" ở 13 ghi nhớ còn thiếu.
- `MEMORY.md`: bỏ dòng ghi nhớ đã gộp, viết lại dòng thư mục máy; 47 dòng khớp 47 file.

## Việc thêm của phiên điều phối (14/11) — viết lại thân ghi nhớ còn chồng lớp

Thân mỗi ghi nhớ nay là trạng thái hiện hành; ngày + lời David nguyên văn chuyển xuống mục `## Sổ` cuối file (không bỏ lời nào).
- `quy-tac-goi-y-de-david-chon`: thân = trình 4 phần gọn theo mặc định skill + "chọn X vì Y", duyệt rồi không hỏi giữa chừng; sổ 06/11 · 11/11 · 14/11.
- `quy-tac-phien-telegram-tu-chay`: hai đoạn nối 14/11 (Remote Control + hỏi đóng phiên; 4 phần trước) gộp vào thân; sổ 11/11 · 12/11 · 14/11 #14 · 14/11 #22.
- `quy-tac-ky-nang-tu-cai-tien`: thân = sáu luật hiện hành (sửa skill qua 4 phần); bản đầu 12/11 "chỉ hỏi khi đụng David" vào sổ.
- `video-khong-tu-xuat`: thân = làm một mạch, góp ý render lại toàn bộ; 05/11 và lời 13/11 vào sổ.
- `video-podcast-phu-hinh-30`, `quy-tac-mod-tu-chay`, `video-phu-de-mot-cho-chu`, `co-so-tri-thuc-quy-uoc-dat-ten`: câu "thay luật…" chuyển vào sổ / Why.
- `video-bo-cuc-tu-can`: viết lại thành 5 điểm hiện hành; điểm 4 "zoom… bám người nói" thì **khung cắt** bám người nói, không hiệu ứng zoom (theo `quy-tac-chung.md` mục 4); sổ 07/11 · 08/11 · 10/11 · 13/11.
- `quy-tac-hoc-la-bo-sung` ("Từ 10/11"), `video-clip-ngan-dung-doc-lap` ("Chốt thêm 07/11"), `video-tham-my-chi-giu-nhan-dien` ("Thay phần…"), `co-so-tri-thuc-ho-so-va-bo-loc` ("Từ 13/11"): bỏ câu nối, giữ ngày trong ngoặc.
- `video-kien-truc-ky-nang`, `quy-tac-sua-thang-tai-ban`: thêm trỏ sổ đổi giá trị hồ sơ `ky-nang/san-xuat-video/ho-so-thuong-hieu/nhat-ky-thay-doi.md`.
- Mô tả đổi của 6 ghi nhớ (`goi-y`, `phien-telegram`, `tu-cai-tien`, `khong-tu-xuat`, `bo-cuc-tu-can`, `thiet-bi-bo-cuc-thu-muc`) đã chép lại vào `ban-do/bo-nao-va-tu-dong-hoa.md`, `ban-do/san-xuat-video.md`.
- `.gitignore` đã có `co-so-tri-thuc/bo-nho/luu-tru/thiet-bi-*`. Chưa đổi tên 2 ghi nhớ (chờ David, Hỏi David 1).
