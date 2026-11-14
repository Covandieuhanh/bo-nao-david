---
description: "Tái bản 2 (10/11), phần bộ skill video: luật đổi so với lần 1."
---

# Tái bản 2 — bộ video (10/11/2026)

Gốc: bảng 164 luật của lần 1 (`du-an/tai-cau-truc-video-1.md`, David chấm đạt). File này chỉ ghi phần đổi từ sau tag `tai-ban-video-1`,
câu máy đo còn bắt, và chỗ bộ video chép / lệch với `chuan-muc-lam-viec.md`, `co-so-tri-thuc/david.md`, `AGENTS.md`, ghi nhớ `co-so-tri-thuc/bo-nho/video-*.md`.
Không đổi code.

**Máy đo bộ video:** trước `dau_ngay 1 · ghi_de 5 · trung 0 · dong 3081` → sau `dau_ngay 0 · ghi_de 0 · trung 0 · dong 3079`.
**kiem-mau.py:** 5/5 ✓ (SSIM 0,982–0,990). 5 dự án mẫu thiếu `chuyen-dong/node_modules` → như lần 1: nối tạm (symlink)
`~/Movies/tap-5-nguyen-tac-tien/2-ban-day-du/chuyen-dong/node_modules` vào `chuyen-dong/node_modules` của từng dự án, chạy, rồi gỡ ngay.

## Bảng luật đang sống (chỉ dòng đổi / mới)

Trạng thái: sống · trùng · ngược · cũ. Cột "Đã làm" = viết lại trong đợt này.

| # | Luật | Nhà | Nguồn trước | Ngày | Trạng thái | Đã làm |
|---|---|---|---|---|---|---|
| V1 | Cắt cứng ở mối cắt, **không phóng xen kẽ** (zoom giật ra giật vào khó chịu); zoom dồn chậm vào mặt ở câu đắt vẫn dùng; `"alt"` / `phong_xen_ke > 1` chỉ khi David yêu cầu | quy-tac-chung §2 | quy-tac-chung §2, khối 02, cat-highlight luật 8 + bước 7A, ho-so-thuong-hieu/doan-noi-bat.md | 10/11 | trùng (lý do chép 3 chỗ) | lý do chỉ ở quy-tac-chung §2; khối 02, doan-noi-bat.md, luật 8 trỏ về. Thay dòng A-nhịp "phóng xen kẽ 1,08×" của bảng lần 1 |
| V2 | Hỏi một lần, "ok" chạy một mạch, phần đã định không hỏi | thoi-quen §2 | quy-tac-chung §8 (chép lại), thoi-quen §2 | 08/11 | trùng chéo bộ | quy-tac-chung §8 thành dòng trỏ; giữ điểm dừng riêng video (multi-clip 2b) |
| V3 | Lệnh > 2 phút chạy nền, không thăm dò; không nhập mật khẩu | thoi-quen §3 (mật khẩu: AGENTS luật 5, theo phiên nao) | quy-tac-chung §8, gotchas "Giao tiếp", thoi-quen §3 | 04/11 | trùng chéo bộ (A63 lần 1 để nhà ở quy-tac-chung) | quy-tac-chung §8 trỏ thoi-quen + AGENTS luật 5; gotchas trỏ quy-tac-chung §8 |
| V4 | Không tải video YouTube/TikTok để dựng (học mẫu thì được) | quy-tac-chung §8 | quy-tac-chung §8, gotchas | 04/11 | trùng | gotchas trỏ |
| V5 | Báo cáo cuối: đã làm · đã kiểm · chưa kiểm · cần xác nhận; video thêm tên riêng cần xác nhận | thoi-quen §4 (+ quy-tac-chung §8 phần riêng) | quy-tac-chung §8, thoi-quen §4 | 08/11 | trùng chéo bộ | quy-tac-chung chỉ giữ phần thêm |
| V6 | Chỉ hình của chính video (thumbnail, bìa, cảnh chèn) | khối 14 | khối 14; phan-phoi-da-kenh trỏ nhầm sang quy-tac-chung | 05/11 | sống, đường trỏ sai | phan-phoi-da-kenh trỏ khối 14 |
| V7 | Không đổi cài đặt tài khoản khi chưa duyệt | khối 19 "Luật an toàn" | khối 19, phan-phoi-da-kenh | 06/11 | trùng | phan-phoi-da-kenh trỏ khối 19 |
| V8 | Tên riêng chưa chắc → hiện đúng tên Whisper nghe, hỏi ở báo cáo (gotchas) | khối 01 (gotchas ghi lỗi) | gotchas | 04/11 | sống | viết lại câu ví dụ, bỏ chữ "thay cho" (máy đo bắt nhầm) |
| V9 | Whisper có thể đè câu bịa lên câu thật cuối video → đối chiếu lần chạy | gotchas | gotchas | 04/11 | sống | viết lại, bỏ "THAY" in hoa |
| V10 | Giọng: người thầy đứng cạnh, câu hỏi tự soi thay vì khẳng định | giong-van | giong-van | — | sống | đổi "thay cho" → "thay vì" |
| V11 | TikTok: link mô tả không bấm được → ghi tên kênh | khối 19 | khối 19 | — | sống | viết lại không dùng "thay cho" |
| V12 | Nguồn đã học nằm ở `thiet-ke-bo-cuc/nguon-tham-khao/`, mỗi nguồn một file | phan-tich-video-mau | phan-tich-video-mau (ví dụ tên file có ngày) | — | sống | bỏ ví dụ tên file có ngày |

Mọi dòng còn lại của bảng lần 1 giữ nguyên nhà, không đổi.

## Chéo bộ

Bộ `nao` (`ky-nang/chuan-muc-lam-viec.md`):
1. **§4 "Video đã chốt hoặc đã đăng: dọn file tạm bằng `don-tap.py --xoa`…"** là luật riêng video, nhà ở khối 17 (B64 lần 1). Đề xuất: thoi-quen §4 rút còn một dòng trỏ "dọn file tạm video: khối 17", bỏ "(chốt 08/11/2026)".
2. §3 và §2 là nhà của "lệnh nền / mật khẩu / hỏi một lần / báo cáo" — bộ video nay trỏ về đó (V2, V3, V5). Phiên `nao` đừng đổi số mục 2–4 mà không báo, vì quy-tac-chung §8 trỏ theo số mục.

Ghi nhớ (`co-so-tri-thuc/bo-nho/`, phiên ghi-nho):
3. `video-luon-co-motion-graphics`: "mỗi video trộn nhiều loại điểm nhấn" + "nới luật 2 trạng thái" — ngược quy-tac-chung §4 / §0 "chỉ vài kiểu hợp nội dung" (David "Đồng ý cả 5", câu 1, lần 1). Sửa ghi nhớ theo bản luật.
4. `video-motion-ke-chuyen`: "chỉ giữ cái lớn: nền, màu chủ đạo, biểu tượng cùng một kiểu vẽ" — lệch `nhan-dien-chung.md` mục 0 (chữ ký = thành phần cố định + cam + hai font; nền, kiểu hình tự do). Sửa theo nhan-dien-chung.
5. `video-bo-cuc-tu-can` điểm 1 "không chép màu, font hay kiểu chuyển động của họ" — đã bị `video-tham-my-chi-giu-nhan-dien` thay; câu cũ vẫn còn, chỉ có dòng "Sửa 10/11" chồng lên. Viết lại điểm 1.
6. `video-chu-nguyen-van`: "không làm thẻ tít mở đầu mặc định" thiếu phần highlight (thẻ tít = cụm nguyên văn đắt nhất, khối 06 + cat-highlight luật 7). Thêm vế highlight.
7. `video-doc-khuon-chu-chinh` đoạn đầu còn "màn hình cuối 3 giây mời xem bản đầy đủ" dù ngay dưới ghi đã bỏ. Viết lại đoạn đầu.
8. `video-kien-truc-skill`: "kiem-mau.py (4 dự án mẫu)" — `mau.json` hiện 5. Sửa số hoặc bỏ số.
9. `video-chi-hinh-cua-chinh-video`: "Đã ghi vào quy-tac-chung 7 + khối 14" — quy-tac-chung không có, nhà là khối 14.
10. `video-podcast-phu-hinh-30`: "Thay luật 'ít mà sâu'…" và `video-nhac-theo-tuyen` "sửa 08/11, thay câu cũ…", `video-chuan-am-luong` "Thay luật…" — lời kể lịch sử trong ghi nhớ; khớp bản luật, chỉ cần gọn.
11. Không cần ghi nhớ mới cho "bỏ phóng xen kẽ" (luật nằm trong quy-tac-chung §2, một bộ).

Skill `tai-cau-truc` (không thuộc bộ nào trong `bo.json`):
12. `do-chong-cheo.py`: mẫu `thay cho` trong `GHI_DE` bắt nhầm cách nói thường ("ghi tên kênh thay cho link"). Đợt này đã viết lại câu để về 0, nhưng nên bỏ `thay cho` khỏi regex hoặc chỉ bắt "thay cho luật".

## Hỏi David

Không có chỗ ngược trong bộ video mà phải hỏi: mọi chỗ đổi đều có bên thắng rõ (lời David 10/11 "bỏ 1 giữ 2"; thói quen chung là nhà
của luật dùng chung). Câu duy nhất có thể đưa vào lượt hỏi chung (phiên điều phối quyết có hỏi không):
- **Luật "Video ngắn đổi gì đó mỗi 1–3 s (nhịp chữ phụ đề, phóng, chữ to, cắt)"** (quy-tac-chung §2) vẫn có chữ "phóng". Sau khi bỏ phóng
  xen kẽ, "phóng" chỉ còn là zoom dồn chậm ở câu đắt. ➡️ Đề xuất: giữ nguyên chữ (zoom dồn vẫn là một cách đổi nhịp), không hỏi. · Khác:
  bỏ "phóng" khỏi danh sách cho khỏi hiểu nhầm.
