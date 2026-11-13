# App Mở Tài Liệu (macOS)

Xem mọi tài liệu trên Mac không cần Office: docx, xlsx, pptx, pdf, pages, numbers, key, csv, txt…
Tự liệt kê tài liệu ở Desktop, Documents, Downloads; lọc Word / Excel / Slide / PDF; tìm theo tên; kéo thả; Open With.

- `main.swift`: danh sách file, xem bằng Quick Look (`QLPreviewView`).
- `slides.swift`: trình xem slide riêng cho pptx/ppt/key/odp, vì Quick Look không chuyển slide được.
  `qlmanage -p -o` xuất bản xem HTML vào `~/Library/Caches/MoTaiLieu/`, hiện bằng WKWebView kèm thanh điều hướng:
  cuộn xem hết · ‹ › · Home/End · số slide · Trình chiếu (phím F, Esc thoát, bấm nửa phải/trái để sang slide) · toàn màn hình.

**Cài / build lại** (cần Command Line Tools, có `swiftc`): chép thư mục này về máy rồi chạy
```bash
bash scripts/mo-tai-lieu/build.sh
```
App ra ở `~/Applications/Mở Tài Liệu.app`. Chỉ xem, không sửa: nút "Mở bằng app gốc" để sửa.
