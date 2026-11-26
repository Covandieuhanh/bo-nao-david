---
description: "Thiết kế khung video podcast: hình học hai khung, vùng an toàn, sân khấu, sóng âm."
---

# Thiết kế video podcast

Hình học hai khung nằm ở `chuyen-dong/src/khung-podcast.js` (PF). Dọc 1080×1920: vùng an toàn x 70–900, y 210–1420.
Ngang 1920×1080: x 96–1824, y 54–1026 — **thiết kế toàn khung**, không chia cột.

## Sân khấu nền (`san-khau.jsx`, composition `nen`) — luôn chạy

| Phần | Dọc (y) | Ngang | Dữ liệu |
|---|---|---|---|
| Tên chương trình (chỉ khi David cung cấp) + tên tập | 226– | trái trên, y 70– | `STAGE.show`, `STAGE.title` |
| **Ý đang bàn** — chữ lớn 2 dòng, dòng 2 màu nhấn | 560–900 | trái, y 300–600, rộng 1180 | `TOPICS` (tự ẩn khi có lớp phủ) |
| Vòng micro chuyển động theo giọng | — | phải, tâm (1560, 400) | `duong-bao-am.js` |
| Tên người nói (chỉ khi biết tên) | 1020– | dưới vòng micro | `STAGE.speakers` |
| Sóng âm — màu theo người đang nói (cam 0, xanh 1), khi lặng thì xám | 1135–1255 | y 680–810, 96 cột | `duong-bao-am.js`, `nguoi-noi.js` |
| Phụ đề | đáy 1374 | đáy 982 | `phu-de.js` (lớp phu-de) |
| **Thanh thời gian**: đã chạy · thanh · "còn m:ss" | 1386–1416 | 996–1026 | tự tính (lớp phu-de) |

Phụ đề + thanh thời gian nằm ở lớp trên cùng nên không cảnh nào che được. Nền: tối + quầng sáng cam di chuyển chậm + lưới di chuyển rất chậm.

## Lớp phủ trên sân khấu
- Thẻ, chữ lớn, hook, tên (`card`, `kinetic`, `hook`, `lower`): vẽ trên dải 830×435 như skill gốc; `Place` đặt căn trái vùng an
  toàn theo `PF.ov` — dọc: 0,88× tại y 480; ngang: 1,08× tại y 175 (x 96–992, tránh vòng micro) — số chính xác ở `khung-podcast.js` `PF.ov`. Ý đang bàn tự ẩn lúc đó.
- Toàn màn hình: che sân khấu (trừ phụ đề + thanh thời gian). Dọc: mọi loại. Ngang: `montage`, `gens`, `build` có bản ngang
  (toan-man-hinh-ngang.jsx); `recap`, `converge`, `master` chưa có — không dùng ở khung ngang (khi cần thì Claude viết bản ngang trước).
- Giới hạn đáy của cảnh toàn màn hình: khối 12.

## Chọn cảnh cho lời nói
Ưu tiên như `$BASE/references/thiet-ke-canh.md`, thêm:
1. Đổi chủ đề / câu hỏi mở ra đoạn mới thì `TOPICS` đổi ngay tại mốc đó (trích phần chính), hoặc dùng `card quote`.
2. Câu có cấu trúc (tầng bậc, mốc, so sánh, trước và sau) thì dùng `diagram` (khối 07); lời nói nhắc tới người / nơi / tổ chức có thật thì dùng `diagram` `anh`.
3. Con số / mốc / tên riêng thì dùng `card` (`ages`, `year`, `years4`, `daily`, `vs`…) hoặc `illus` `count`.
4. Liệt kê, các bước thì dùng `card steps` (tối đa 4 mục) hoặc `build` / `montage` (toàn màn hình).
5. Người nói tự giới thiệu tên thì dùng `lower` (tên + vai trò) — chỉ khi có trong lời nói.
6. Câu cuối thì dùng màn chốt `cta` nguyên văn (khối 08).

## Nhịp
- Hình phủ **khoảng 30 % thời lượng**, cân theo nội dung (`phu_hinh_muc_tieu`, podcast SKILL): một màn một ý, một hình. Sân khấu (ý
  đang bàn + sóng âm) đã đủ "sống" giữa các cảnh, không cần lấp kín. Thẻ: chữ ngắn, hình là chính.
- `TOPICS` phủ từ 0 s đến hết, đổi **thưa** theo ý lớn (40–90 s); không lặp nguyên văn chữ của cảnh đang hiện hoặc sắp hiện.
- Không để hai cảnh cùng kiểu liền nhau (khối 07); không chồng 2 lớp phủ.
