---
description: "Tái bản 2 (10/11), phần bộ skill video: các luật thay đổi so với lần 1."
---

# Tái bản 2 — bộ video (10/11/2026)

Gốc: bảng 164 luật của lần 1 (`du-an/nang-cap/tai-cau-truc-video-1.md`, David chấm đạt). File này chỉ ghi phần thay đổi kể từ sau tag `tai-ban-video-1`,
các câu công cụ đo còn phát hiện, và các chỗ bộ video sao chép hoặc lệch so với `chuan-muc-lam-viec.md`, `co-so-tri-thuc/david.md`, `AGENTS.md`, ghi nhớ `co-so-tri-thuc/bo-nho/video-*.md`.
Đợt này không đổi code.

**Công cụ đo bộ video:** trước `dau_ngay 1 · ghi_de 5 · trung 0 · dong 3081`, sau `dau_ngay 0 · ghi_de 0 · trung 0 · dong 3079`.
**kiem-mau.py:** 5/5 ✓ (SSIM 0,982–0,990). 5 dự án mẫu thiếu `chuyen-dong/node_modules` nên người làm xử lý như lần 1: tạo liên kết tạm (symlink) từ
`~/Movies/tap-5-nguyen-tac-tien/2-ban-day-du/chuyen-dong/node_modules` vào `chuyen-dong/node_modules` của từng dự án, chạy kiểm tra, rồi gỡ ngay.

## Bảng luật hiện hành (chỉ dòng đổi / mới)

Trạng thái: sống · trùng · ngược · cũ. Cột "Đã làm" ghi phần đã viết lại trong đợt này.

| # | Luật | Nguồn duy nhất | Nguồn trước | Ngày | Trạng thái | Đã làm |
|---|---|---|---|---|---|---|
| V1 | Cắt cứng ở điểm cắt, **không phóng xen kẽ** (zoom ra vào đột ngột gây khó chịu); zoom dồn chậm vào mặt ở câu then chốt vẫn dùng; `"alt"` / `phong_xen_ke > 1` chỉ dùng khi David yêu cầu | quy-tac-chung §2 | quy-tac-chung §2, khối 02, cat-highlight luật 8 + bước 7A, ho-so-thuong-hieu/doan-noi-bat.md | 10/11 | trùng (lý do sao chép ở 3 chỗ) | lý do chỉ ghi ở quy-tac-chung §2; khối 02, doan-noi-bat.md, luật 8 trỏ về đó. Dòng này thay dòng A-nhịp "phóng xen kẽ 1,08×" của bảng lần 1 |
| V2 | Hỏi một lần; David trả lời "ok" thì làm liên tục tới hết; phần đã định thì không hỏi | thoi-quen §2 | quy-tac-chung §8 (bản sao), thoi-quen §2 | 08/11 | trùng chéo bộ | quy-tac-chung §8 thành dòng trỏ; giữ điểm dừng riêng của video (multi-clip 2b) |
| V3 | Lệnh chạy quá 2 phút thì chạy nền, không thăm dò; không nhập mật khẩu | thoi-quen §3 (mật khẩu: AGENTS luật 5, theo phiên nao) | quy-tac-chung §8, gotchas "Giao tiếp", thoi-quen §3 | 04/11 | trùng chéo bộ (A63 lần 1 để nguồn ở quy-tac-chung) | quy-tac-chung §8 trỏ về thoi-quen và AGENTS luật 5; gotchas trỏ về quy-tac-chung §8 |
| V4 | Không tải video YouTube/TikTok để dựng (học mẫu thì được) | quy-tac-chung §8 | quy-tac-chung §8, gotchas | 04/11 | trùng | gotchas trỏ về |
| V5 | Báo cáo cuối: đã làm · đã kiểm · chưa kiểm · cần xác nhận; báo cáo video thêm mục tên riêng cần xác nhận | thoi-quen §4 (kèm quy-tac-chung §8 phần riêng) | quy-tac-chung §8, thoi-quen §4 | 08/11 | trùng chéo bộ | quy-tac-chung chỉ giữ phần bổ sung |
| V6 | Chỉ dùng hình của chính video (thumbnail, bìa, cảnh chèn) | khối 14 | khối 14; phan-phoi-da-kenh trỏ nhầm sang quy-tac-chung | 05/11 | sống, đường trỏ sai | phan-phoi-da-kenh trỏ về khối 14 |
| V7 | Không đổi cài đặt tài khoản khi chưa duyệt | khối 19 "Luật an toàn" | khối 19, phan-phoi-da-kenh | 06/11 | trùng | phan-phoi-da-kenh trỏ về khối 19 |
| V8 | Tên riêng chưa chắc chắn thì hiển thị đúng tên Whisper nghe được, hỏi ở báo cáo (gotchas) | khối 01 (gotchas ghi lỗi) | gotchas | 04/11 | sống | viết lại câu ví dụ, bỏ chữ "thay cho" (công cụ đo phát hiện nhầm) |
| V9 | Whisper có thể chép đè câu bịa đặt lên câu thật ở cuối video, nên cần đối chiếu lần chạy | gotchas | gotchas | 04/11 | sống | viết lại, bỏ "THAY" in hoa |
| V10 | Giọng văn: người thầy đứng cạnh, dùng câu hỏi tự xét thay vì khẳng định | giong-van | giong-van | — | sống | đổi "thay cho" → "thay vì" |
| V11 | TikTok: link trong mô tả không bấm được, nên ghi tên kênh | khối 19 | khối 19 | — | sống | viết lại, không dùng "thay cho" |
| V12 | Nguồn đã học nằm ở `thiet-ke-bo-cuc/nguon-tham-khao/`, mỗi nguồn một file | phan-tich-video-mau | phan-tich-video-mau (ví dụ tên file có ngày) | — | sống | bỏ ví dụ tên file có ngày |

Mọi dòng còn lại của bảng lần 1 giữ nguyên nguồn duy nhất, không đổi.

## Chéo bộ

Bộ `nao` (`ky-nang/chuan-muc-lam-viec.md`):
1. **§4 "Video đã chốt hoặc đã đăng: dọn file tạm bằng `don-tap.py --xoa`…"** là luật riêng của video, nguồn nằm ở khối 17 (B64 lần 1). Đề xuất: thoi-quen §4 rút gọn còn một dòng trỏ "dọn file tạm video: khối 17", bỏ "(chốt 08/11/2026)".
2. §3 và §2 là nguồn của "lệnh nền / mật khẩu / hỏi một lần / báo cáo"; bộ video nay trỏ về đó (V2, V3, V5). Phiên `nao` không được đổi số mục 2–4 khi chưa báo, vì quy-tac-chung §8 trỏ theo số mục.

Ghi nhớ (`co-so-tri-thuc/bo-nho/`, phiên ghi-nho):
3. `video-luon-co-motion-graphics`: "mỗi video trộn nhiều loại điểm nhấn" và "nới luật 2 trạng thái" mâu thuẫn với quy-tac-chung §4 / §0 "chỉ vài kiểu hợp nội dung" (David "Đồng ý cả 5", câu 1, lần 1). Cần sửa ghi nhớ theo bản luật.
4. `video-motion-ke-chuyen`: "chỉ giữ cái lớn: nền, màu chủ đạo, biểu tượng cùng một kiểu vẽ" lệch so với `nhan-dien-chung.md` mục 0 (chữ ký gồm thành phần cố định, màu cam và hai font; nền và kiểu hình được tự do). Cần sửa theo nhan-dien-chung.
5. `video-bo-cuc-tu-can-bang` điểm 1 "không chép màu, font hay kiểu chuyển động của họ" đã được `video-tham-my-chi-giu-nhan-dien` thay thế; câu cũ vẫn còn, chỉ có dòng "Sửa 10/11" ghi chồng lên. Cần viết lại điểm 1.
6. `video-chu-nguyen-van`: "không làm thẻ tít mở đầu mặc định" thiếu phần highlight (thẻ tiêu đề là cụm nguyên văn then chốt nhất, khối 06 và cat-highlight luật 7). Cần thêm vế highlight.
7. `video-doc-mau-chu-chinh` ở đoạn đầu còn câu "màn hình cuối 3 giây mời xem bản đầy đủ" dù ngay bên dưới đã ghi là bỏ. Cần viết lại đoạn đầu.
8. `video-kien-truc-skill`: "kiem-mau.py (4 dự án mẫu)" trong khi `mau.json` hiện có 5. Cần sửa số hoặc bỏ số.
9. `video-chi-hinh-cua-chinh-video`: "Đã ghi vào quy-tac-chung 7 + khối 14" nhưng quy-tac-chung không có luật này, nguồn duy nhất là khối 14.
10. `video-podcast-phu-hinh-30`: "Thay luật 'ít mà sâu'…" và `video-nhac-theo-tuyen` "sửa 08/11, thay câu cũ…", `video-chuan-am-luong` "Thay luật…" đều là lời kể lịch sử trong ghi nhớ; nội dung khớp bản luật, chỉ cần viết gọn.
11. Không cần ghi nhớ mới cho "bỏ phóng xen kẽ" (luật nằm trong quy-tac-chung §2, chỉ thuộc một bộ).

Skill `tai-cau-truc` (không thuộc bộ nào trong `bo.json`):
12. `do-chong-cheo.py`: mẫu `thay cho` trong `GHI_DE` phát hiện nhầm cách nói thông thường ("ghi tên kênh thay cho link"). Đợt này đã viết lại câu để chỉ số về 0, nhưng nên bỏ `thay cho` khỏi regex hoặc chỉ phát hiện "thay cho luật".

## Hỏi David

Bộ video không có chỗ mâu thuẫn nào phải hỏi: mọi chỗ đổi đều có bên thắng rõ ràng (lời David 10/11 "bỏ 1 giữ 2"; thói quen chung là nguồn duy nhất
của luật dùng chung). Câu duy nhất có thể đưa vào lượt hỏi chung (phiên điều phối quyết định có hỏi hay không):
- **Luật "Video ngắn đổi gì đó mỗi 1–3 s (nhịp chữ phụ đề, phóng, chữ to, cắt)"** (quy-tac-chung §2) vẫn có chữ "phóng". Sau khi bỏ phóng
  xen kẽ, "phóng" chỉ còn là zoom dồn chậm ở câu then chốt. ➡️ Đề xuất: giữ nguyên chữ (zoom dồn vẫn là một cách đổi nhịp), không hỏi. · Khác:
  bỏ "phóng" khỏi danh sách để tránh hiểu nhầm.
