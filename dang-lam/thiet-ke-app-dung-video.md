# Thiết kế app dựng video (bản nháp chờ David duyệt)

> Ngày 08/11/2026. Trạng thái: **chờ David duyệt**, chưa viết dòng code nào.
> Phạm vi: chỉ chạy trên máy Mac này, chỉ David dùng.

---

## 1. Mục tiêu

- Phần **cố định**: bấm một nút là chạy xong, Claude không phải viết hay đọc lại gì.
- Phần **cần phán đoán**: chỉ phần này mới gọi Claude. Mỗi lần gọi chỉ gửi đúng thứ cần để quyết định.
- **Thêm tiêu chí cố định về sau không phải viết lại app.** App không chứa luật. App chỉ đọc luật từ file, nên thêm luật chỉ là thêm hoặc sửa file.
- **Một nguồn duy nhất.** App và skill dùng chung khối, hồ sơ tham số và thư viện hình. Sửa ở một chỗ thì cả hai cùng đổi.

**Xong khi:** David đưa một video dài vào app, duyệt 2 cổng, nhận được các clip highlight cùng bài đăng. Claude chỉ được gọi ở những bước có đánh dấu "Claude".

---

## 2. Kế hoạch

### 2.1. Nguyên tắc gốc: app là "máy chạy bước", luật nằm ngoài app

App chỉ biết làm 4 việc: đọc danh sách bước, chạy bước, hiện kết quả, chờ David duyệt. Mọi thứ còn lại đều nằm trong file:

| Lớp | Nằm ở | Đã có chưa |
|---|---|---|
| Con số (cắt lặng bao lâu, cỡ chữ, mức nhạc…) | `ho-so/*.json`, đọc qua `hoso.py` | **Đã có** |
| Cách làm từng việc | `khoi/<số>-<tên>/` + script | Đã có, cần thêm phiếu khai báo |
| Thành phần hình (motion graphics) | `thu-vien-hinh/*.jsx` | Đã có, cần thêm danh mục mẫu |
| **Phiếu khai báo bước** (mới) | `khoi/<khối>/buoc.json` | Chưa có |
| **Công thức** cho từng loại video (mới) | `cong-thuc/<loại>.json` | Chưa có |
| **Luật kiểm** (mới) | `kiem/*.py` | Một phần (`kiem-mau.py`, `check_frames.sh`) |
| **Lời nhắc cho Claude** từng bước | trong khối, `khoi/<khối>/loi-nhac.md` | Chưa có, rút từ README khối |

### 2.2. Bốn cách thêm tiêu chí cố định mà không phải sửa app

| Muốn thêm | Làm gì | Sửa app? |
|---|---|---|
| Đổi một con số (ví dụ nhạc thấp hơn giọng 25 dB thay vì 23) | Sửa `ho-so/*.json`. App có màn hình sửa hồ sơ | Không |
| Một luật kiểm mới (ví dụ "chữ không được chạm mép") | Thêm một file vào `kiem/`. App tự chạy mọi file trong thư mục này sau khi render | Không |
| Một bước mới (ví dụ "tự thêm logo chìm") | Thêm thư mục khối, gồm `buoc.json` và script, rồi thêm tên bước vào công thức | Không |
| Một mẫu motion graphics mới | Thêm `.jsx` vào `thu-vien-hinh/` và một dòng vào danh mục mẫu. Claude tự thấy mẫu mới trong danh sách được chọn | Không |

Chỉ khi muốn **đổi cách app hoạt động** (thêm một kiểu màn hình duyệt mới chẳng hạn) mới cần sửa code app.

### 2.3. Phiếu khai báo bước (`buoc.json`): mẫu

```json
{
  "id": "cat-lang",
  "ten": "Cắt khoảng lặng",
  "loai": "co-dinh",
  "can": ["words.srt", "video_goc_raw"],
  "ra": ["video_goc.mp4", "cuts.json"],
  "lenh": "python3 -I scripts/clean_apply.py {du_an}",
  "ho_so": ["cat_lang"]
}
```

`loai` nhận một trong ba giá trị:
- `co-dinh`: chạy script.
- `claude`: gọi Claude, nhận về file kế hoạch.
- `duyet`: dừng lại chờ David bấm duyệt.

Với bước `claude`, phiếu ghi thêm hai thứ: Claude được đọc những file nào, và Claude phải trả về file theo khuôn nào.

### 2.4. Công thức (`cong-thuc/highlight.json`): mẫu

```json
["chep-loi", "loc-noi-dung", "CONG-1", "chon-khoanh-khac", "cat-clip",
 "cat-lang", "phu-de", "khung-doc", "nhan-manh", "chon-nhac", "tranh-che",
 "dung", "kiem", "viet-bai", "CONG-2"]
```

Muốn đổi thứ tự hay bỏ một bước thì chỉ sửa danh sách này.

### 2.5. Claude không viết code, chỉ ra "bản kế hoạch"

Đây là chỗ tiết kiệm token nhiều nhất. Ví dụ bước cảnh minh hoạ, Claude chỉ trả về:

```json
[{"tu": 81.2, "den": 84.0, "mau": "Illus", "bieu_tuong": "nguoi-dan-doi",
  "chu": "nguyên văn lời David"}]
```

Sau đó app kiểm file này đúng khuôn, đúng luật (chữ phải nguyên văn, mẫu phải có trong thư viện) rồi tự dựng bằng các mẫu sẵn có. Nếu kiểm sai, app gửi lỗi lại cho Claude, tối đa 1 lần; vẫn sai thì báo David.

Cách gọi Claude: dùng `claude -p` (Claude Code chạy ngầm) để tính vào gói Claude của David, không mất thêm tiền API.

### 2.6. Xếp loại 21 khối hiện có

| Khối | Cố định (script) | Cần Claude |
|---|---|---|
| 00 Lọc nội dung | ghi sổ danh mục | chấm theo bộ lọc, ra phiếu lọc → **cổng 1** |
| 01 Chép lời | Whisper, pyannote, ảnh khung | — |
| 02 Làm sạch | đo lặng, cắt, sửa chiều hình | chọn câu nói lại (script đề xuất, Claude chốt) |
| 03 Phụ đề | chia cụm, cỡ, vị trí | đánh dấu từ cần tô màu theo nghĩa |
| 04 Khung hình | đổi khung, nâng khung theo mặt | — |
| 05 Tránh che người | dò mặt, đặt lớp phủ | — |
| 06 Mở đầu | dựng thẻ tít, teaser | chọn câu chạm |
| 07 Cảnh minh hoạ | dựng từ mẫu | chọn chỗ, chọn mẫu, chọn lời nguyên văn |
| 08 Kết thúc | thẻ cuối, màn kết | chọn câu chốt |
| 09 Âm thanh | cân −20/−14 LUFS, trộn nhạc | chọn bài nhạc theo tuyến |
| 10 Nhận diện | toàn bộ | — |
| 11 Ghép cảnh | dựng theo edl | hiểu clip, giữ/bỏ, xếp thứ tự |
| 12 Sân khấu podcast | sóng âm, người nói | đặt tên các ý đang bàn |
| 13 Chọn khoảnh khắc | cắt và kiểm lời | chọn ý theo 4 câu |
| 14 Thumbnail | dựng ảnh | chọn khung, chọn chữ |
| 15 Phát hành | chương YouTube | tiêu đề, mô tả, bình luận ghim (giọng David) |
| 16 Số liệu | — | đọc ảnh chụp số liệu |
| 17 Dựng + kiểm tra | toàn bộ | — |
| 19 Đăng bài | **để ngoài app** (cần trình duyệt, cần David duyệt) | |
| 20 Hộp thư | **để ngoài app** | |

Ước tính: khoảng 2/3 công việc là cố định.

### 2.7. Phần vẫn làm bằng Claude Code như hiện tại

Học video mẫu, sửa luật, thêm khối hoặc mẫu mới, đăng bài. Đây là phần **sửa chính bộ não** nên giữ trong Claude Code.

### 2.8. Công nghệ (Claude chọn, David không cần quyết)

- Trang web chạy trên máy (localhost), mở bằng trình duyệt.
- Phần máy chủ viết bằng Python, vì phần lớn script đã viết bằng Python. Remotion (Node) vẫn giữ nguyên để render.
- Code app nằm trong repo, ở `skills/dung-video/app/`, nên được đẩy lên GitHub như mọi script khác. Dự án video vẫn nằm ở `~/Movies`.

---

## 3. Quy trình: một lần dùng app

1. Mở app, kéo video vào, chọn loại video (hoặc để Claude đoán).
2. App chạy phần cố định đầu tiên: chép lời, nhận người nói, ảnh khung.
3. Claude lọc nội dung → **cổng 1**: David xem phiếu lọc, bấm Duyệt hoặc ghi góp ý.
4. App chạy lần lượt các bước theo công thức. Mỗi bước `claude` hiện kế hoạch ngắn; David có thể xem hoặc cho chạy tiếp.
5. App dựng, render, chạy toàn bộ luật kiểm trong `kiem/`.
6. Xem bản nháp. Nếu có góp ý bằng chữ, Claude **chỉ sửa file kế hoạch**, app render lại đúng phần bị đổi.
7. **Cổng 2:** duyệt bản cuối và bài đăng. Phần đăng làm tiếp bằng Claude Code (khối 19).

Mỗi bước đều ghi lại kết quả, nên lỗi ở bước nào thì chạy lại từ bước đó, không phải làm lại từ đầu.

---

## 4. Thực thi (checklist)

### Đợt 0: Chuẩn bị nền (chưa có giao diện)
- [ ] Viết khuôn chung cho `buoc.json`
- [ ] Viết `buoc.json` cho các khối dùng trong highlight (01, 02, 03, 04, 05, 08, 09, 13, 15, 17)
- [ ] Viết `cong-thuc/highlight.json`
- [ ] Viết danh mục mẫu cho `thu-vien-hinh/` (tên mẫu, nhận gì)
- [ ] Rút `loi-nhac.md` và khuôn đầu ra cho các bước Claude của highlight
- [ ] Gom luật kiểm hiện có vào `kiem/`
- [ ] Viết "máy chạy bước" dạng lệnh: `chay highlight <video>`
- **Xong khi:** chạy một lệnh ra được clip highlight giống bản do skill làm.

### Đợt 1: Giao diện cho highlight
- [ ] Màn hình kéo thả, danh sách bước có trạng thái
- [ ] Màn hình cổng 1 và cổng 2
- [ ] Màn hình xem bản nháp và ô góp ý
- [ ] Màn hình sửa hồ sơ tham số
- **Xong khi:** David tự làm trọn một video highlight trong app.

### Đợt 2: Làm video (một video nói trước camera)
- [ ] `buoc.json` cho 06, 07, 10, 14 và `cong-thuc/lam-video.json`
- **Xong khi:** một video dài và các clip ra từ app.

### Đợt 3: Podcast · Đợt 4: Ghép vlog
- [ ] Mỗi loại: thêm bước còn thiếu và một công thức. **Không sửa app.** Đây cũng là phép thử xem nguyên tắc ở mục 2.2 có đúng không.

### Giữ skill và app khớp nhau
- [ ] Sửa skill để gọi cùng máy chạy bước, nhờ đó Claude Code cũng đỡ token.
- [ ] Thêm vào `thoi-quen-lam-viec.md`: thêm luật cố định thì thêm theo một trong 4 cách ở mục 2.2.

---

## 5. Chờ David quyết

1. Đợt đầu làm **highlight** (đề xuất, vì loại này cố định nhất), hay loại khác?
2. Ở bước Claude, app nên **dừng lại cho David xem kế hoạch**, hay **chạy thẳng, chỉ dừng ở 2 cổng** (đề xuất: chạy thẳng)?
3. Cho phép sửa skill ở Đợt 0 (thêm `buoc.json`, `cong-thuc/`, `kiem/`) không? Phần này không đổi cách skill đang chạy, chỉ thêm file.
