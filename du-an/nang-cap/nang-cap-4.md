---
description: "Tái bản 4 (20/11/2026): đổi công cụ đo sang đo trùng lặp / chồng chéo (bỏ ngưỡng số dòng, thêm gan_trung) và gộp các ý trùng của bộ video về một nguồn duy nhất."
---

# Nâng cấp 4 (lúc mở gọi là "tái bản 4") — 20/11/2026

> Cùng ngày David đổi "tái bản" thành vòng **Nâng cấp** (`ky-nang/hoc-lien-tuc/SKILL.md` Việc 4). Đợt này đã làm bước Dọn + máy đo;
> tag đóng mốc là `nang-cap-4`, gắn sau khi David chấm việc thật.

**Lý do:** công cụ đo báo "NÊN TÁI BẢN TOÀN BỘ: vượt ngưỡng ở video (dong 4005 > 4000)" sau khi thêm tầng tư duy dựng video
(`thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md`, `nguyen-ly.json`, `huong-dan-lua-chon.md`, `truong-hop-da-giai.md`, `bai-kiem/`, cổng `soat-canh.mjs`).
David: *"bộ não và các phần cần học chắc chắn sẽ ngày càng tăng lên, tái bản chỉ là gom các bản trùng hay ý trùng theo nhiều cách
khác nhau về một hoặc là gỡ rối, chứ yêu cầu phải 4000 dòng thì tôi thấy sẽ bị hạn chế"*. Mốc so sánh trước: tag `tai-ban-4-truoc`.

## 1. Công cụ đo mới (`ky-nang/tai-cau-truc/do-chong-cheo.py`, `bo.json`)
- Công cụ chỉ cảnh báo khi có trùng lặp / chồng chéo: `dau_ngay` · `ghi_de` · `trung` · **`gan_trung`** (mới).
- `gan_trung` = cặp dòng ở hai file khác nhau có chung > 50 % số chữ (Jaccard), dòng có ít nhất 12 chữ; bỏ qua mô tả đầu file, khối ``` và phần `code` / địa chỉ link
  (mục lục lặp lại mô tả, đường dẫn code lặp lại là đúng thiết kế).
- `dong` chỉ được in ra (thể hiện độ lớn); `sua` chuyển sang `nhac` (in một dòng nhắc, không cảnh báo).
- Ngưỡng `gan_trung`: video 30 · hỏi 5 · não 6 (mức sau tái bản: 16 · 0 · 2, cộng thêm khoảng dự phòng cho nội dung học thêm).

## 2. Số đo

| Bộ | Trước | Sau |
|---|---|---|
| video | dấu ngày 12 · ghi đè 0 · trùng 0 · gần trùng 49 · 4005 dòng | dấu ngày 3 (ngày đo số liệu) · 0 · 0 · gần trùng 16 · 3986 dòng |
| hỏi | 0 · 0 · 0 · 0 | không đổi |
| não | 4 · 0 · 0 · 2 | không đổi — 2 cặp là `chi-dan-toan-cuc.md` tóm tắt luật 1–2 của `AGENTS.md`, có chủ đích (file này được nạp ở mọi phiên ngoài repo) |

## 3. Bảng luật đã gộp (luật · nguồn duy nhất · nơi cũ nay chỉ trỏ tới)

| Luật | Nguồn duy nhất | Nơi cũ (nay một dòng trỏ tới hoặc bỏ) |
|---|---|---|
| Cách chạy một công thức: SKILL là công thức, sửa cách làm → sửa khối; số liệu lấy ở hồ sơ; đọc trước; lỗi thường gặp đọc một lần; file khác đọc đúng bước | `quy-tac-chung.md` mục 8 | 3 SKILL dựng (dòng 7–10) |
| Bước đơn giản → nhắc đổi sang mô hình rẻ hơn | `quy-tac-chung.md` mục 8 (gốc `chuan-muc-lam-viec.md` mục 3) | 3 SKILL dựng; `phan-phoi-da-kenh` còn một dòng trỏ tới |
| Ghi góp ý ở đúng một vị trí + một dòng sổ | `quy-tac-chung.md` mục 8 | `dung-video`, `dung-podcast` mục "Sửa theo góp ý" |
| Chỉ dừng giữa chừng khi có tín hiệu nặng; báo cáo "đã chọn X vì Y"; góp ý → render lại toàn bộ | `quy-tac-chung.md` mục 8 | `dung-video`, `dung-podcast` đoạn mở đầu |
| Bàn giao bản cuối: `cho-dang`, dọn, lưu Drive, xoá trên Mac | `quy-tac-chung.md` mục 8 dòng cuối (cách làm: khối 17) | `dung-video` bước 12, `tong-quan.md` |
| Bố cục tự cân bằng, không có con số bắt buộc, khung ngang tự do / khung dọc ít thành phần | `thiet-ke-bo-cuc/README.md` mục 2 | `quy-tac-chung.md` mục 4 |
| Lằn ranh theo từng hướng (đã gộp đủ: công dụng sức khoẻ của sản phẩm, chi tiết lộ danh tính, tên gói dịch vụ) | khối 00 mục 3 (gốc `chien-luoc-nghe-nghiep.md` 4.7) | `quy-tac-chung.md` mục 1, `giong-thuong-hieu-david.md` mục 6 |
| Kiểu dẫn dắt Không · Gợi mở · Mời: tỉ lệ, câu kết, giá (gộp "số hoá" cho bài công nghệ) | khối 08 | khối 00 mục 5, khối 15, `giong-thuong-hieu-david.md` mục 5 |
| Thẻ tiêu đề `hook` chỉ dùng khi David yêu cầu | khối 06 | khối 07 bước 2, `thiet-ke-canh.md` "Mở đầu 3 giây" |
| Whisper bịa đặt câu ở phân đoạn không có lời → bỏ | `quy-tac-chung.md` mục 1 | khối 13 (giữ ý riêng: không dùng làm câu chọn) |
| Khung chủ thể (khung bo góc trên nền kênh, phần còn lại dành cho bảng ghi chú) | khối 04 | `dung-video` mục "Đầu vào" |
| Kiểm âm thanh bản cuối (−14 LUFS, đỉnh, tiếng rè so với giọng) | khối 17 (chuẩn khối 09) | `dung-podcast` bước 9 |
| Phát hành: phat-hanh.md, thumbnail khi khung ngang + YouTube | `quy-tac-chung.md` mục 7 | `dung-podcast` bước 10, `nhieu-doan-video.md` |
| Cắt phân đoạn từ nguồn dài bằng `-ss -t` rồi `concat` | khối 02 | `loi-thuong-gap.md` |
| Dấu chồng lên chữ to Barlow → `VN` | `dung-video.../loi-thuong-gap.md` | `dung-podcast/.../loi-thuong-gap.md` (giữ chi tiết riêng "LỰC") |
| Đáy cảnh toàn màn hình podcast (dọc y < 1240, ngang y < 790) | khối 12 | `thiet-ke-podcast.md` |
| Học thêm: gắn vào nguyên lý, thêm dòng bảng 4c | `thiet-ke-bo-cuc/README.md` mục 4 | `nhu-cau-nguoi-xem.md` mục 6, `huong-dan-lua-chon.md` cuối (giữ luật riêng: không có dòng ở bảng 4c thì không được chọn) |

Ngày trong bản luật (9 vị trí: `quy-tac-chung.md` mục 0, `dung-video` bảng chế độ, khối 00, 01, 02, 03, 04, 17, `phan-phoi-da-kenh`)
được chuyển về sổ `dung-video-theo-phong-cach/references/nhat-ky-thay-doi.md` và `phan-phoi-da-kenh/references/nhat-ky-thay-doi.md`.

**Không đổi:** tầng tư duy 20/11 (nội dung `nhu-cau-nguoi-xem.md`, `nguyen-ly.json`, `huong-dan-lua-chon.md`, `truong-hop-da-giai.md`, `bai-kiem/`, `soat-canh.mjs`);
mọi code; mục "Xong khi" của các skill; kho (`bo-cuc.md`, `am-thanh.md`, `nguon-tham-khao/`).

**16 cặp gần trùng còn lại (đúng thiết kế):** dòng "Đọc trước" và dòng trỏ tới sổ của từng skill · "Xong khi" của mỗi skill đứng độc lập · bảng công thức
và chuỗi "sửa thì chạy lại" của từng công thức · giải thích tham số ở hồ sơ · Đầu ra khối 01 = Đầu vào khối 03.

## 4. Ghi nhớ
46 file: dòng gần trùng chỉ là dòng cuối chuẩn "Nhà của luật … Ghi nhớ này giữ ngày, lời David, lý do". Cập nhật
`quy-tac-sua-thang-tai-ban` (công cụ đo đo trùng lặp / chồng chéo, không đo độ dài) + dòng MEMORY.md.

## 5. Kiểm
- **Đủ luật:** từng dòng bảng mục 3 có nguồn duy nhất; luật ở nơi cũ chỉ còn một dòng trỏ tới. Hai vị trí nguồn mới được bổ sung cho đủ (khối 00 lằn ranh
  thêm 3 mục từ `quy-tac-chung`; khối 08 thêm câu Mời "số hoá" từ `giong-thuong-hieu-david`), không thêm luật mới.
- **Công cụ đo:** mọi bộ đều "Chưa cần tái bản" (video 3 · 0 · 0 · 16/30; hỏi 0; não 4 · 0 · 0 · 2/6).
- **Liên kết:** `kiem-tra-lien-ket.py` cho kết quả link gãy 0.
- **Bài kiểm suy luận:** `cham.py --mau` cho kết quả công cụ chấm 10/10. Nội dung tư duy không đổi (chỉ gộp đoạn "Học thêm"), nên chưa làm lại bài.
- **Hình ảnh giữ nguyên:** không đổi dòng code dựng nào (chỉ `.md` + công cụ đo). `kiem-mau.py` **không chạy được**: 5 dự án mẫu trong `mau.json`
  không còn trên Mac (đã chuyển lên Drive). Kiểm cảnh dự án cũ `tap-gan-ket-bang-cong-viec`: P0 "chưa chẩn đoán" như dự kiến với
  kế hoạch cảnh cũ (công cụ kiểm cảnh không đổi).
- **Việc thực tế:** chưa làm — chờ David chấm một clip ngắn trọn một ý. Tag `tai-ban-4` được gắn sau khi David chấm đạt.
