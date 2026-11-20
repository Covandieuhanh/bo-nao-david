---
description: "Gói 1 dựng video bằng AI, phần 1 quy trình: dựng video bất kì bằng AI trên máy tính, từng bước."
---

# 1. Quy trình: dựng video bất kì bằng AI trên máy tính

Dùng cho **mọi loại video** (nói trước camera, vlog nhiều cảnh, sản phẩm, sự kiện, quay màn hình, ghi âm). Học viên dùng **trợ lý AI chạy lệnh trên máy tính của mình** (Claude Code, Codex CLI, Gemini CLI… chọn cái đang có). AI điều khiển các công cụ dựng miễn phí; người chỉ đưa tư liệu, nói muốn gì, xem và phản hồi.

## Mục tiêu
Từ tư liệu thô → AI dựng ra video hoàn chỉnh: cắt ghép, phụ đề, chữ, đồ hoạ, nhạc, âm lượng chuẩn, đủ các khung cần đăng.

## Kế hoạch: bộ công cụ
| Công cụ | Việc |
|---|---|
| **Trợ lý AI chạy lệnh** | đọc quy trình vận hành chuẩn (SOP), chạy các công cụ dưới, tự kiểm kết quả |
| **ffmpeg** | cắt, ghép, xoay, đổi khung, gắn phụ đề, lọc tiếng, chuẩn âm lượng, xuất file |
| **Whisper** | chép lời có mốc thời gian (để AI "nghe" được video) |
| **Remotion** (khi cần đồ hoạ) | chữ chuyển động, hình minh hoạ, khung trình bày bằng code |
| **Quy trình vận hành chuẩn (SOP)** | phong cách, luật, cách làm: AI đọc mỗi lần, sửa dần cho đúng ý |

## Quy trình: 8 bước dựng một video
| # | Bước | AI làm | Đạt khi |
|---|---|---|---|
| 1 | **Nạp tư liệu** | xếp file vào thư mục tập, đo độ dài, khung, chất lượng | biết có gì trong tay |
| 2 | **Hiểu tư liệu** | chép lời (nếu có tiếng nói), chụp khung hình rải đều để "xem" cảnh | có lời chép + danh sách cảnh |
| 3 | **Kế hoạch sản xuất** | viết dòng thời gian: đoạn giữ, thứ tự cảnh, chỗ chữ, hình, nhạc | người duyệt được kế hoạch trong 2 phút |
| 4 | **Dựng thô** | cắt, ghép theo kế hoạch; bỏ lặng, câu hỏng | mạch xem trơn |
| 5 | **Làm sạch** | xoay, cắt khung, chỉnh sáng màu nhẹ, giảm ồn | hình rõ, tiếng rõ |
| 6 | **Phụ đề, chữ, đồ hoạ** | phụ đề 5–8 chữ mỗi lần; chữ nhấn, hình minh hoạ không che chủ thể | đọc kịp, không rối |
| 7 | **Nhạc, âm thanh** | nhạc thấp dưới giọng, hiệu ứng tiếng nhẹ, chuẩn âm khoảng −14 LUFS | nghe dễ chịu, đều tiếng |
| 8 | **Xuất + tự kiểm** | xuất các khung cần (ngang 16:9, dọc 9:16, vuông), clip ngắn, ảnh bìa từ khung hình; chụp khung kiểm lỗi | file đúng khung, không lỗi |

**Phản hồi** ở bất kì bước nào → AI sửa video **và sửa đúng một câu trong quy trình vận hành chuẩn (SOP)** để lần sau tự đúng.

## Luật dựng
- Chữ trên video lấy **đúng lời trong video** (khi video có người nói); AI không bịa lời.
- Dễ hiểu hơn cầu kì: mỗi video ít kiểu hiệu ứng.
- Không sửa, không xoá file gốc. AI hỏi trước khi xoá hay tốn tiền; không đưa mật khẩu cho AI.

## Đòi hỏi máy
Mac hoặc Windows, RAM ít nhất 16 GB, ổ trống ít nhất 50 GB; tài khoản AI có trợ lý chạy lệnh. Remotion miễn phí cho cá nhân và công ty tối đa 3 người, lớn hơn cần giấy phép (kiểm lại điều khoản lúc dạy).
