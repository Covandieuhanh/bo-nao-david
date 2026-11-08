# App dựng video tiết kiệm token

> Bản 2, 08/11/2026: đã làm bản đầu. Code ở `skills/dung-video/app/`, cách dùng ở [app/README.md](../skills/dung-video/app/README.md).

## 1. Mục tiêu

- Tiết kiệm token tối đa để làm được nhiều video, mà kết quả vẫn như bản skill render mới nhất.
- Phần cố định bấm nút là chạy; Claude chỉ làm phần phán đoán.
- Thêm tiêu chí cố định về sau không phải viết lại app.

**Xong khi:** David làm trọn một video thật trong app, chỉ duyệt 2 cổng, kết quả ngang bản skill, và số token mỗi video thấp hơn hẳn.

## 2. Kế hoạch: đo trước, rồi dựng

### 2.1. Token đang tốn ở đâu (đo từ lịch sử phiên trên máy)
| Phiên dựng video | Lượt Claude | Token đọc lại | Token viết |
|---|---|---|---|
| Làm video DJI 07/11 | 157 | ~36 triệu | ~113 nghìn |
| Làm "5 nguyên tắc tiền" 08/11 | 91 | ~18 triệu | ~56 nghìn |
| Ghép vlog | 110 | ~20 triệu | ~68 nghìn |

Ba nguồn tốn: (1) **mỗi lượt đọc lại cả cuộc trò chuyện**, phiên càng dài càng đắt; (2) **Claude tự dò mốc giây** từng câu (nhiều lượt `find.py`); (3) **đọc ảnh chụp kiểm tra** (10–64 ảnh mỗi phiên) và sửa đi sửa lại.

### 2.2. Cách app cắt ba nguồn đó
- Mỗi video chỉ **3 lần gọi Claude**, mỗi lần gửi đúng thứ cần: lọc + cắt · kịch bản cảnh · gói phát hành. Ước tính khoảng 35 nghìn token vào cho video 14 phút.
- **Claude trích câu, máy tìm mốc.** Phép thử trên 5 video đã duyệt: 284/285 mốc tìm lại đúng tới 0,05 giây.
- Kiểm bằng máy, không bằng mắt Claude: `soat_canh.mjs` + thư mục luật kiểm `kiem/`. David xem bản cuối ở cổng 2.
- Gọi bằng chính Claude Code trên máy (`claude -p`), nên tính vào gói của David.

### 2.3. App không chứa luật
| Muốn thêm | Làm | Sửa app? |
|---|---|---|
| Con số | `ho-so/*.json` | Không |
| Luật kiểm | thả `app/kiem/kiem_<tên>.py` | Không |
| Bước | `app/buoc/<id>.json` + tên vào `app/cong-thuc/<loại>.json` | Không |
| Biểu tượng, tuyến nhạc | thư viện hình / hồ sơ (Claude tự thấy) | Không |
| Luật dựng, lọc, phát hành | README khối (lời nhắc chèn thẳng file) | Không |
| Bước cần Claude hay không | đổi `loai` trong phiếu bước | Không |

### 2.4. Xếp loại các bước của công thức `lam-video`
Máy (14 bước): kiểm công cụ · tạo dự án · chép lời thô + đề xuất cắt · ghi phiếu lọc · làm sạch + nâng khung · chép lời bản sạch + phụ đề nháp · tìm mốc + ghi kịch bản · tránh che mặt · soát cảnh · render · luật kiểm · thumbnail/teaser/chương. Claude (3 bước): lọc + cắt · kịch bản cảnh · phát hành. David (2 cổng): phiếu lọc · bản cuối.

## 3. Quy trình một lần dùng
1. `python3 -I skills/dung-video/app/giao_dien.py` → mở http://localhost:8765 → **+ Việc mới**: chọn video, đặt tên tập.
2. Máy chép lời, đề xuất cắt → Claude lọc → **cổng 1**: David duyệt phiếu lọc hoặc ghi góp ý (Claude làm lại đúng bước đó).
3. Máy làm sạch, chép lời → Claude lên kịch bản cảnh (trích câu) → máy tìm mốc, soát nguyên văn; sai thì Claude sửa một lần.
4. Máy tránh che mặt, soát cảnh, render, chạy luật kiểm → Claude viết gói phát hành → máy làm thumbnail, teaser, chương.
5. **Cổng 2:** xem video ngay trong app + kết quả kiểm + bài đăng. Góp ý thì Claude sửa kịch bản cảnh rồi máy render lại.

## 4. Thực thi

### Đã xong (08/11)
- [x] Đo token từ lịch sử phiên
- [x] Máy chạy bước, gọi Claude theo khuôn JSON (có kiểm + sửa một lần), ghi token mỗi lần gọi
- [x] Công thức `lam-video`: 17 bước, 3 lời nhắc chèn thẳng README khối 00, 07, 08, 15, bộ cục, giọng văn
- [x] Tìm mốc từ câu trích + soát chữ nguyên văn: thử trên 5 video đã duyệt, không báo nhầm
- [x] Ghi kịch bản: dựng lại kịch bản "Sự tập trung" từ câu trích ra 18/18 cảnh giống bản duyệt, `soat_canh` không lỗi
- [x] Luật kiểm: âm lượng −14 LUFS, thời lượng, chữ nguyên văn (đạt trên video đã duyệt)
- [x] Giao diện: danh sách việc, việc mới, các bước, 2 cổng duyệt có góp ý, xem video, làm lại từ một bước
- [x] Chạy thật trên một clip 36 giây: các bước máy chạy đúng, 2 bước Claude đóng vai bằng tay

### Việc tiếp theo
- [ ] **David đăng nhập lệnh `claude` của app một lần** (`app/README.md` mục "Lần đầu")
- [ ] Chạy một video thật trọn quy trình, so với bản skill làm, ghi số token thật
- [ ] Thêm công thức `highlight` (cắt clip dọc từ video dài người nói)
- [ ] Góp ý ở cổng 2: chỉ render lại cảnh bị đổi, thay vì render cả video
- [ ] Sau đó: công thức podcast, ghép vlog

### Giới hạn hiện tại
- Chữ/viền in cứng trong hình video cũ cần nhìn hình: vẫn làm bằng Claude Code.
- Kịch bản dùng 5 kiểu cảnh có sẵn (nhan, bocuc, illus, action, cta). Kiểu mới cần code thêm như hiện nay.
