---
name: video-bo-ung-dung
description: "Công cụ dựng video: Claude dựng trực tiếp trong phiên Claude bằng Remotion theo skill; bỏ ứng dụng localhost:8765 (tốn token), không cài HyperFrames / Motion Studio, chỉ học ý tưởng (06/11, 10/11; gộp 15/11)"
metadata:
  type: project
---

Ngày 10/11/2026 David bỏ ứng dụng dựng video (`ky-nang/san-xuat-video/app/`, localhost:8765, LaunchAgent tự chạy, chế độ giữ Mac luôn hoạt động).
Mã nguồn, script `scripts/app-video.sh` và tài liệu thiết kế đã được xoá khỏi repo (lịch sử GitHub vẫn lưu); LaunchAgent đã được gỡ.

**Why:** David nhận thấy việc xây dựng và chạy ứng dụng khi làm video tốn nhiều token hơn so với làm trực tiếp trong phiên Claude.

**How to apply:** Claude luôn dựng video trực tiếp trong phiên Claude, theo skill (`phan-phoi-da-kenh` rồi chuyển sang skill dựng). Claude không đề xuất dựng lại
ứng dụng hay công cụ tự động hoá tương tự trừ khi David yêu cầu. Thư mục dữ liệu cũ của ứng dụng `~/Movies/_app/` được giữ nguyên (David tự quyết định).
Liên quan [[quy-tac-thu-bang-doan-ngan]], [[quy-tac-khong-tu-chay-viec-cua-david]].

Nguồn của luật: `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8 ("Dựng ngay trong phiên Claude"). Ghi nhớ này lưu ngày, lời David và lý do.

## Gộp từ `video-bo-ung-dung` (15/11/2026, vòng tự học hằng tuần: giảm số ghi nhớ xuống 40)

David chốt 2026-11-06: **không cài** HyperFrames và Motion Studio; bộ skill video vẫn dùng Remotion. Claude đã học ý tưởng và tự viết lại, không sao chép mã nguồn: luật chuyển động "đã vào là đứng yên" (khối 07), 3 sơ đồ `xay-tang`, `doi-trang-thai`, `chuyen-giao`, `soat-canh.mjs` (khối 17), `chu-tren-man.mjs` (khối 03).

**Why:** hai bộ có cùng cách render (Chrome chạy nền và FFmpeg), tốc độ gần bằng nhau; bộ hiện tại đã mạnh hơn ở dấu tiếng Việt, ở việc tránh che mặt và ở độ trọn vẹn của quy trình. Motion Studio tự kích hoạt khi người dùng nhắn yêu cầu làm video nên xung đột với skill hiện có; Motion Studio còn thêm hook vào cài đặt Claude Code và khoá HyperFrames ở phiên bản cũ.

**How to apply:** Claude không đề xuất đổi công cụ dựng trừ khi David thấy hình ảnh còn thiếu rõ ràng; kiểu chuyển động mới được vẽ vào `thu-vien-tai-nguyen/`. Liên quan [[video-kien-truc-ky-nang]].

Nguồn của luật: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` mục 4 điểm 10. Ghi nhớ này lưu ngày, lời David và lý do.

Gốc: khối 2 (Hành động) của tu-duy-goc.md — giả định dựng ứng dụng riêng sẽ đỡ việc đã sai vì tốn token hơn, nên quay lại kế hoạch và dựng thẳng trong phiên.
