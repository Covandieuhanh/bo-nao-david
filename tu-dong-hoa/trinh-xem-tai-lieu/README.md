---
description: "App Mở Tài Liệu trên macOS: xem, xem bản in (từng trang như khi in), sửa trực tiếp docx, md, txt, csv; không cần Office."
---

# App Mở Tài Liệu (macOS)

Ba chế độ ở thanh trên cùng (⌘1 · ⌘2 · ⌘3):

| Chế độ | Làm gì |
|---|---|
| **Xem nhanh** | Xem bằng Quick Look; slide có trình xem riêng (dưới). |
| **Bản in** | LibreOffice chạy ngầm dàn tài liệu thành PDF đúng khổ giấy (lưu tạm ở `~/Library/Caches/MoTaiLieu/ban-in/`): từng trang tách rời trên nền xám, "Trang x / n", khổ giấy (A4 dọc · 210 × 297 mm), phóng to / thu nhỏ, nút In (⌘P). Áp cho Word, Excel, Slide, Ghi chú, csv; PDF hiện thẳng. |
| **Sửa** | Word (docx, doc, rtf, odt): khung soạn chữ rộng đúng phần in được của trang, thước (căn lề, giãn dòng, danh sách), đậm · nghiêng · gạch chân · cỡ chữ · phông · căn lề. Ghi chú (md, txt): sửa chữ thường. csv: bảng ô, thêm dòng / cột. Lưu ⌘S. Excel, Slide, PDF, Pages: nút "Sửa bằng LibreOffice" để giữ công thức, bố cục. |

- **Lưu an toàn:** lần lưu đầu giữ bản gốc cạnh tệp (`<tên>.ban-goc.<đuôi>`). Rời tệp, đổi chế độ hay thoát app khi chưa lưu thì app hỏi Lưu / Không lưu / Huỷ.
- **Word đi qua LibreOffice** (docx, doc, odt → RTF để sửa → về định dạng gốc), vì macOS đọc thẳng docx làm mất giãn dòng (hợp đồng 5 trang thành 4). Thử trên hợp đồng 5 trang: lưu xong vẫn 5 trang, giữ lề, giãn dòng, bảng chữ ký không viền; ngắt dòng có thể dời một dòng ở vài câu. Đầu trang / chân trang, hình nổi có thể mất: xem lại ở Bản in sau khi lưu.
- Không có LibreOffice: Bản in báo cần cài; Word sửa và lưu bằng bộ đọc của macOS (kém chính xác hơn).
- `ban-in-va-sua.swift`: hai chế độ Bản in và Sửa. Mở thẳng một chế độ: `open -a "Mở Tài Liệu" <tệp> --args -cheDo "Bản in"`.

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

**Cài / build lại** (cần Command Line Tools, có `swiftc`; cài LibreOffice trước: `brew install --cask libreoffice`): chép thư mục này về máy rồi chạy
```bash
bash tu-dong-hoa/trinh-xem-tai-lieu/dung.sh
```
App ra ở `~/Applications/Mở Tài Liệu.app`. 
