# Ali Abdaal + Joseph Video Editing (học 10/11/2026)

David duyệt: "ok học đầy đủ đi, càng nhiều tài nguyên để tuỳ ý sáng tạo càng tốt". Từ lần này thẩm mỹ chỉ giữ **chữ ký nhận diện**
(`thu-vien-hinh/nhan-dien-chung.md` mục 0); học cả nền, kết cấu, kiểu hình, chữ nhấn.

## 1. Nguồn (xem bằng bảng khung 3–6 s; phụ đề YouTube bị chặn 429 nên chưa nghe lời giải thích)
- Ali Abdaal — "Brutally Honest Advice About Productivity in 26 Minutes" (BNRfzI6E1Es), 0:00–4:00 · người nói ngang.
- Ali Abdaal — "How to Learn So Fast People Assume You're Naturally Gifted (with AI)" (szVXpM7VVMg), 0:00–5:00.
- Joseph Video Editing — "How to Edit VIRAL Talking Head Videos Using ONLY Claude! (New Minimal Style)" (g9xoKm5DEeU), 0:00–5:00.
- Joseph Video Editing — "17 Design Tips for Video Editors!" (Zgf3Fcrnq4E), cả bài.
- Joseph Video Editing — "How to Edit Premium YouTube Videos Using Opus 5.5!" (lyoEyYMU20Q), 0:00–6:00.
- File tải về đã xoá sau khi cắt khung.

## 2. Học được
| # | Điều học được | Nguồn | Loại | Thành phần |
|---|---|---|---|---|
| 1 | Tít to đứng giữa nền và người, đầu người che phần dưới chữ — chiều sâu | Ali 0:00 | bố cục, chiều sâu | `chusau` (có code) |
| 2 | Bóng người một màu trên nền giấy, chữ phía sau | Joseph minimal 3:00–5:00 | nền, kiểu hình | `chusau` `bong` (có code) |
| 3 | Mục lục 1-2-3 hiện dần cạnh người trong ô, mục cũ mờ | Ali 0:15–0:40 | thứ tự hiện | `bocuc` `muc-luc` (có code) |
| 4 | Thanh tiến trình nối các mẹo, mẹo hiện tại sáng, thẻ tên mẹo | Ali (2) 0:00–3:00 | nối cảnh, nhịp | `bocuc` `tien-trinh` (có code) |
| 5 | Hình vẽ phấn ở mảng tối cạnh người, lớn dần suốt nhiều phút (đường cong → 1, 2, 3 → quy tắc 2 phút) | Ali 1:00–4:00 | bố cục, mạch hình | `bocuc` `canh-nguoi` + `mach.js` (có code) |
| 6 | Người làm mờ phía sau, đồ hoạ nổi giữa khung — không cắt hẳn sang nền khác | Joseph (cả 3 video) | nền | `phong: 'nguoi-mo'` (có code) |
| 7 | Hai font: chữ thường + một từ nghiêng có chân màu nhấn ("You *won't* need") | Joseph minimal, 17 tips | chữ nhấn | `*từ*` → font phụ `NHAN` (có code) |
| 8 | Kết cấu giấy / hạt cho cảnh lắng | Joseph minimal | nền | `phong: 'hat'`, nền giấy của `bong` (có code) |
| 9 | Mỗi khung một tiêu điểm; tương phản bằng cỡ / màu / hình; màu 60-30-10 | Joseph 17 tips | nguyên tắc | câu soát ở khối 17 |
| 10 | Đặt chỗ: một vật thì giữa, vật + chữ thì mỗi thứ một bên; tâm khung dành cho người hoặc vật chính | Joseph 17 tips ("placing rules") | bố cục | đã khớp `cho.js`, ghi để nhớ |
| 11 | Hàng nhãn viên thuốc có biểu tượng bật quanh người | Ali (2) 2:00 | bố cục | chưa code |
| 12 | Cảnh đời thường toàn khung + người nói ô nhỏ góc + chữ trích dưới trái | Ali 4:00+ | bố cục | chưa code (cần cảnh quay thêm) |
| 13 | Một đường kẻ chạy xuyên nhiều cảnh | Joseph minimal | nét riêng | chưa code (làm bằng `ve` + `mach.js`) |
| 14 | Ảnh tài liệu, tô màu dòng đang nói · trước / sau hai khung | Ali, Joseph | minh chứng | chưa code |

## 3. Không lấy
- Cảnh màn hình ứng dụng gõ chữ giả lập (Ali (2)): chữ trên màn hình phải là lời David, không dựng lời giả.
- Số liệu lớn tự đặt ("4.5 billion tokens"): chỉ dùng số David nói.

## 4. Đối chiếu chặn cũ (đã chụp thử ngang `tap-5-nguyen-tac-tien` + dọc `tap-thoi-quen-nho`, bản sao tạm)
| Thành phần | Mặt | Phụ đề | Dấu góc | Thanh thời gian | Vùng an toàn | Ngang | Dọc |
|---|---|---|---|---|---|---|---|
| `chusau` | cố ý để người che chữ; chữ không đè mặt | trên dải phụ đề | dưới dấu góc | không chạm | trong | đạt | đạt |
| `chusau` `bong` | — | dấu góc, thanh vẫn hiện trên nền giấy | đạt | đạt | trong | đạt | đạt (nên 1 dòng) |
| `muc-luc` | người trong ô | — | đạt | ô người chạm sát thanh (giống `o-nguoi` cũ) | trong | đạt | đạt |
| `tien-trinh` | — | — | đạt | đạt | trong | đạt | đạt |
| `canh-nguoi` | không đè ai (cho.js); thiếu chỗ → `o-nguoi` | — | đạt | đạt | trong | đạt | tự thành `o-nguoi` |
| `phong` | — | — | đạt | đạt | — | đạt | đạt |

**Kiểm không phá:** 10 cảnh cũ (6 ngang, 4 dọc) chụp bằng skill trước khi sửa và sau khi sửa: trùng từng điểm ảnh.
Chưa kiểm: render video thật có cảnh mới; vlog ghép và podcast chưa có các kiểu này.
