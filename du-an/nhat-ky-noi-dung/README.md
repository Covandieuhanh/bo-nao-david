---
description: "Nhật ký nội dung theo ba hướng nghề: mỗi tập (video, ghi âm) ghi đủ ý tưởng và nội dung vào file của từng hướng, để David tổng hợp lại về sau."
---

# Nhật ký nội dung theo hướng

**Mục tiêu:** không ý nào trong lời David bị trôi. Mỗi tập, sau khi phân hướng (khối 00 mục 0b,
[README](../../ky-nang/san-xuat-video/mo-dun/00-sang-loc-noi-dung/README.md)), mọi ý có giá trị được ghi vào file đúng hướng.
Về sau chỉ cần mở một file là thấy toàn bộ ý của hướng đó qua mọi tập, để gom thành bài, gói, khoá học.

| Hướng | File |
|---|---|
| 1. Tài chính | [huong-1-tai-chinh.md](huong-1-tai-chinh.md) |
| 2. Trainer con người | [huong-2-trainer-con-nguoi.md](huong-2-trainer-con-nguoi.md) |
| 3. Giải pháp công nghệ AI | [huong-3-giai-phap-cong-nghe-ai.md](huong-3-giai-phap-cong-nghe-ai.md) |

## Luật ghi
- **Luôn ghi**, kể cả tập không dựng (⛔ / 🗂) và hướng không ra bản: ý vẫn là nguyên liệu.
- **Chỉ thêm, không sửa mục cũ**; mục mới nhất ở cuối file. Một tập chạm nhiều hướng thì một mục ở mỗi file hướng đó.
- **Đủ ý, không bịa**: mỗi ý một dòng, có lời gốc ngắn (nguyên văn, tối đa 1 câu) và mốc để tìm lại trong tập.
- **Ẩn danh**: khách, người được nhắc tên viết theo vai ("chủ quán", "bạn hướng dẫn viên"). Không ghi giá khách trả, số điện thoại,
  chuyện riêng. Không nêu tên đơn vị phía sau; "đội của mình", "đội công nghệ" thì ghi được (hồ sơ 4.7, hướng 3).
- Ý thuộc **đội đối tác công nghệ** (khách của công ty, giải pháp cụ thể đang làm) ghi bên bộ não Veltrix; ở đây chỉ ghi ý của David.
- Máy gom `san-pham-hoa` đọc các file này làm nguồn "lời trong video" (không phân loại lại).

## Khung một mục
```markdown
## <dd/mm/yyyy> · <tap-…> · <bối cảnh một dòng, ẩn danh>
Bản theo hướng: <dạng, ~phút / không ra bản — lý do> · Trạng thái: <chờ dựng / đã dựng / đã đăng + link>
| Ý | Lời gốc | Mốc | Nỗi đau / mục tiêu | Bán được gì | Dùng cho việc |
|---|---|---|---|---|---|
```
Mốc ghi theo trục ghi ở `phan-huong.md` của tập.
