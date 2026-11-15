---
description: "App Mở Tài Liệu trên macOS: xem docx, xlsx, pptx, pdf… không cần Office."
---

# App Mở Tài Liệu (macOS)

Xem mọi tài liệu trên Mac không cần Office: docx, xlsx, pptx, pdf, pages, numbers, key, csv, txt…
Tự liệt kê tài liệu ở Desktop, Documents, Downloads; lọc theo nhóm, mỗi đuôi tệp đúng một nhóm: Word (doc, docx, pages, rtf, odt) · Excel (xls, xlsx, numbers, ods, csv) · Slide (ppt, pptx, pps, ppsx, key, odp) · PDF · Ghi chú (md, txt) · Khác (html, epub, json, xml; không tính vào "Tất cả"), mỗi nhóm biểu tượng và màu riêng; tìm theo tên; kéo thả; Open With.

- `main.swift`: danh sách file, xem bằng Quick Look (`QLPreviewView`).
- `trinh-chieu.swift`: trình xem slide riêng cho pptx/ppt/key/odp, vì Quick Look không chuyển slide được.
  `qlmanage -p -o` xuất bản xem HTML vào `~/Library/Caches/MoTaiLieu/`, hiện bằng WKWebView.
  - **Xem cuộn:** cuộn hết slide · ‹ › · Home/End · số slide.
  - **Trình chiếu** (nút ▶ ở thanh dưới hoặc trên cùng, menu Trình chiếu, ⌘↩ từ slide đang xem, ⇧⌘↩ từ slide đầu, phím F):
    cửa sổ không viền phủ kín màn hình, nền đen, ẩn Dock và menu. → / phím cách / Enter / bấm chuột: slide sau ·
    ← / chuột phải / bấm nửa trái: slide trước · gõ số + Enter: nhảy tới slide đó · B: màn đen · Esc: thoát
    (qua slide cuối cũng thoát), bản xem cuộn về đúng slide vừa chiếu. Chuột tự ẩn, số slide hiện thoáng ở góc.

**Cài / build lại** (cần Command Line Tools, có `swiftc`): chép thư mục này về máy rồi chạy
```bash
bash tu-dong-hoa/trinh-xem-tai-lieu/dung.sh
```
App ra ở `~/Applications/Mở Tài Liệu.app`. Chỉ xem, không sửa: nút "Mở bằng app gốc" để sửa.
