# 1. Quy trình toàn bộ: một lần quay → đủ video cho mọi kênh

Đây là hệ học viên sẽ **sở hữu và tự chạy** khi học xong. Rút từ hệ David đang dùng hằng ngày (`skills/dung-video/`, skill `dang-da-kenh`), bỏ phần riêng của David, giữ khung.

## Mục tiêu
Học viên quay **một lần** bằng điện thoại → AI tự làm ra **bản dài có phụ đề + motion graphics, 1–3 clip dọc, thumbnail, bài đăng từng kênh**. Học viên chỉ quay, xem, góp ý, bấm đăng.

## Kế hoạch: hệ gồm 4 phần
| Phần | Là gì | Học viên làm ở bài |
|---|---|---|
| **Bộ não** | hồ sơ người làm kênh, giọng văn, nhận diện (màu, chữ), luật kênh | 2, 4 |
| **Máy** | Claude Code + công cụ dựng chạy trên máy học viên (ffmpeg, Whisper, Python, Node, Remotion) | 3 |
| **Bộ skill** | quy trình từng bước để AI làm theo: lọc, dựng, cắt, phát hành | 6–11 |
| **Sổ** | sổ danh mục video + số liệu để biết video nào ra kết quả | 11, 12 |

## Quy trình: 9 bước của một video
| # | Bước | Ai làm | Ra gì |
|---|---|---|---|
| 0 | **Chuẩn bị**: ghi 3 dòng (khoảnh khắc chạm nỗi đau · chỗ kẹt và cách gỡ · câu hỏi người xem mang về) | học viên | 3 dòng |
| 1 | **Quay** bằng điện thoại theo chuẩn quay (bài 5) | học viên | file gốc |
| 2 | **Nhận + chép lời**: AI chuyển giọng nói thành chữ, đo độ dài, khung, chất lượng | AI | lời chép có mốc giây |
| 3 | **Lọc**: video thuộc nhóm nội dung nào, có đáng làm không, bán được gì, đăng kênh nào | AI | phiếu lọc |
| 4 | **Dựng bản dài**: làm sạch, phụ đề, khung hình, cảnh minh hoạ, chữ nhấn, màn chốt nguyên văn, nhạc, chuẩn âm | AI | `video-final.mp4` |
| 5 | **Cắt clip dọc**: chọn ý trọn đứng độc lập, khung 9:16 bám người nói | AI | 1–3 clip |
| 6 | **Phát hành**: tiêu đề, mô tả, chương, thumbnail, bài từng kênh, bình luận ghim | AI | `phat-hanh.md` + ảnh |
| 7 | **Xem + góp ý**: học viên xem bản cuối, góp ý bằng lời → AI sửa đúng chỗ, dựng lại | học viên → AI | bản đạt |
| 8 | **Đăng + đo**: học viên đăng (hoặc hẹn giờ); sau 24 giờ / 7 ngày AI đọc số liệu, đề xuất video sau | học viên + AI | sổ số liệu |

**Luật giữ chất lượng** (lấy từ hệ David):
- Chữ trên video lấy **nguyên văn lời người nói**, AI không đặt lời vào miệng.
- Video dài để nguyên mạch kể; clip ngắn chỉ trích từ đó.
- Mỗi video ít kiểu hiệu ứng, ưu tiên dễ hiểu hơn cầu kì.
- Góp ý thì sửa **đúng một chỗ** trong skill để lần sau tự đúng, không sửa tay từng video.

## Thực thi: thời gian một video khi đã thạo
| Việc | Học viên | Máy |
|---|---|---|
| Ghi 3 dòng + quay 10 phút | ~20 phút | — |
| Chép lời, lọc, dựng, cắt, phát hành | gửi file, chờ | 30–90 phút tuỳ máy |
| Xem, góp ý, đăng | ~15 phút | dựng lại nếu cần |

## Đòi hỏi tối thiểu (nói rõ trước khi bán)
- Máy tính: Mac (chip M) hoặc Windows mạnh, RAM ≥ 16 GB, trống ≥ 50 GB.
- Tài khoản Claude trả phí có Claude Code (học viên tự đăng ký, tự trả).
- Điện thoại quay được 1080p, mic cài áo nếu có.
- Remotion (phần dựng đồ hoạ) miễn phí cho cá nhân và công ty ≤ 3 người; công ty lớn hơn phải mua giấy phép: kiểm tra lại điều khoản trước khi bán.
