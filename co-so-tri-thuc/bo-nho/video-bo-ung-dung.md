---
name: video-bo-ung-dung
description: "Công cụ dựng: dựng thẳng trong phiên Claude bằng Remotion theo skill; bỏ app localhost:8765 (tốn token), không cài HyperFrames / Motion Studio, chỉ học ý (06/11, 10/11; gộp 15/11)"
metadata:
  type: project
---

Ngày 10/11/2026 David bỏ app dựng video (`ky-nang/san-xuat-video/app/`, localhost:8765, LaunchAgent tự chạy, chế độ giữ Mac thức).
Code, script `scripts/app-video.sh`, tài liệu thiết kế đã xoá khỏi repo (lịch sử GitHub còn giữ); LaunchAgent đã gỡ.

**Why:** David thấy xây và chạy app khi làm video tốn token hơn so với làm ngay trong phiên Claude.

**How to apply:** dựng video luôn làm trực tiếp trong phiên Claude, theo skill (`phan-phoi-da-kenh` → skill dựng). Không đề xuất dựng lại
app hay công cụ tự động tương tự trừ khi David yêu cầu. Thư mục dữ liệu cũ của app `~/Movies/_app/` để nguyên (David tự quyết).
Liên quan [[quy-tac-thu-bang-doan-ngan]], [[quy-tac-khong-tu-chay-viec-cua-david]].

Nhà của luật: `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8 ("Dựng ngay trong phiên Claude"). Ghi nhớ này giữ ngày, lời David, lý do.

## Gộp từ `video-bo-ung-dung` (15/11/2026, tự học tuần: giảm ghi nhớ về 40)

David chốt 2026-11-06: **không cài** HyperFrames + Motion Studio, bộ skill video vẫn dùng Remotion. Đã học ý và tự viết lại, không chép code: luật chuyển động "đã vào là đứng yên" (khối 07), 3 sơ đồ `xay-tang`, `doi-trang-thai`, `chuyen-giao`, `soat-canh.mjs` (khối 17), `chu-tren-man.mjs` (khối 03).

**Why:** cùng cách render (Chrome chạy ngầm + FFmpeg), tốc độ gần bằng nhau; bộ hiện tại đã mạnh hơn ở dấu tiếng Việt, tránh che mặt và trọn quy trình. Motion Studio tự kích hoạt khi nhắn làm video nên đụng skill hiện có, còn thêm hook vào cài đặt Claude Code và khóa HyperFrames ở bản cũ.

**How to apply:** không đề xuất đổi công cụ dựng trừ khi David thấy hình còn thiếu rõ ràng; kiểu chuyển động mới vẽ vào `thu-vien-tai-nguyen/`. Liên quan [[video-kien-truc-ky-nang]].

Nhà của luật: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/README.md` mục 4 điểm 10. Ghi nhớ này giữ ngày, lời David, lý do.
