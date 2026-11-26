---
description: "Trục tri thức (tầng 0) — cách bộ não David tiếp nhận, xử lý, học và nâng cấp MỌI thông tin, xây dựng theo cách một mô hình AI như Claude được tạo ra: dữ liệu → chưng cất → phản hồi → đánh giá → ra bản. Mọi skill về học, sửa, lưu chỉ trỏ về đây."
---

# Trục tri thức — bộ não David như một bộ não Claude thu nhỏ

Bộ não học thêm bao nhiêu thì **nội dung** tăng lên bấy nhiêu; **trục này không đổi**. Mọi cách học, sửa, lưu ở nơi khác (`chuan-muc-lam-viec.md` mục 4,
`hoc-lien-tuc`, `tai-cau-truc`, học video mẫu) là cách áp dụng trục này cho một việc, không đặt ra cách riêng. Mục đích, giá trị, lằn ranh
mà mọi thứ phục vụ: `david.md` mục 1–3 và sáu luật `AGENTS.md`. Cách **nghĩ** khi làm bất kỳ việc gì (bóc tách, vòng kết quả hoặc vấn đề,
học và thay đổi, kiểm sai) nằm ở [tu-duy-goc.md](tu-duy-goc.md), cùng tầng 0; trục này là khối 3 "học và thay đổi" áp dụng vào chính bộ não.

## 0. Gốc: AI dùng bộ não này là ai
AI (Claude, Codex, Gemini…) mỗi phiên **bắt đầu từ số 0** về David; điều AI biết chỉ là những gì đọc được từ file. Vì vậy:
> **Thước không bao giờ đổi:** một AI mới tinh, đọc ít nhất, vẫn làm đúng như David muốn — và lần sau đúng hơn lần trước.

Mọi quyết định lưu gì, lưu ở đâu, viết thế nào đều trả lời câu này. "Người đọc mới" là **bất kỳ ai** — trí tuệ nhân tạo khác, học viên,
người chưa biết gì về công nghệ — nên mọi file viết đủ từ, đủ nghĩa, không viết tắt (`AGENTS.md` luật 1).

## 1. Mô hình AI được tạo ra thế nào thì bộ não được xây dựng đúng như vậy

| Mô hình AI | Làm gì | Ở bộ não David |
|---|---|---|
| **Dữ liệu huấn luyện** (Pretraining Data) | rất nhiều ví dụ thật, liên tục bổ sung, không sửa dữ liệu cũ | tầng 3: lời David, trường hợp thực tế, số liệu, sổ quyết định, nguồn học |
| **Hiến chương** (Constitution) | vài nguyên tắc ngắn ở cấp cao nhất, dùng để đánh giá mọi thứ khác | tầng 0: trục này + mục đích, giá trị, lằn ranh |
| **Chưng cất** (Distillation) | nén nhiều ví dụ thành quy luật chung, không nhớ từng ví dụ | nhiều trường hợp cùng gốc → một **nguyên lý** + 1–3 trường hợp mẫu (tầng 1) |
| **Tinh chỉnh bằng ví dụ tốt** (Fine-tuning on Demonstrations) | học từ bản mẫu đã được người duyệt | sản phẩm David đã duyệt: trường hợp mẫu, mẫu chuẩn, kịch bản thật |
| **Học từ phản hồi** (Feedback Learning) | nhận xét của người chấm làm thay đổi cách làm | lời David sửa (`tin-hieu.jsonl` trường `david_sua`), số liệu người xem |
| **Bộ đánh giá** (Evals) | bài kiểm cố định, chạy trước khi ra bản, **lỗi nào cũng thành một câu kiểm** | bài kiểm từng bộ, mẫu chuẩn, phép thử người đọc mới |
| **Ra bản có số hiệu** (Versioned Release) | chỉ ra bản khi bản mới bằng hoặc tốt hơn; kém hơn thì quay lại bản trước | mốc `nang-cap-<n>`, quay về `nang-cap-<n>-truoc` |
| **Cửa sổ ngữ cảnh + truy xuất** (Context Window, Retrieval) | khi làm việc chỉ nạp phần cốt lõi, phần còn lại tra cứu khi cần | luôn đọc tầng 0 + skill đúng việc; tra tầng 3 qua `chi-muc.md` |
| **Quên có chọn lọc** (Pruning) | bỏ phần không hữu ích để phần hữu ích rõ hơn | cắt giảm: phần lâu không dùng / số liệu cho thấy vô ích → lưu trữ vào `luu-tru/` |

## 2. Bốn tầng — tầng càng cao càng ít đổi, muốn đổi phải có bằng chứng càng mạnh

| Tầng | Chứa | Đổi khi | Ví dụ |
|---|---|---|---|
| **0 · Trục / gốc** | file này, `tu-duy-goc.md`, khung `mo-hinh-kinh-doanh.md`, mục đích, giá trị, lằn ranh, sáu luật | **nâng cấp** (làm rõ, thêm ví dụ, liên kết thêm, không đổi nghĩa) được; **đổi gốc** (đổi nghĩa) chỉ khi đủ dẫn chứng trong `so-dan-chung-goc.md` và David chốt sau vài ngày | `truc-tri-thuc.md`, `david.md` mục 1–3, `AGENTS.md` sáu luật |
| **1 · Nguyên lý** | lý do làm như vậy; áp dụng được cho nhiều việc | vòng Nâng cấp, khi nhiều trường hợp cùng gốc | `thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md`, `chuan-muc-lam-viec.md` |
| **2 · Quy trình** | các bước của một loại việc | theo tuần, theo góp ý có bằng chứng | các `SKILL.md`, khối `mo-dun/`, hồ sơ tham số |
| **3 · Dữ liệu** | trường hợp thực tế, số liệu, nguồn học, sổ, ghi nhớ, kho | thêm hằng ngày; **chỉ thêm**, không sửa nghĩa dữ liệu cũ | `truong-hop-da-giai.md`, `so-lieu.md`, `nhat-ky-thay-doi.md`, `bo-nho/`, `bo-cuc.md` |

Trong tầng 1–2, mỗi ý chỉ có **một nguồn duy nhất**; nơi khác chỉ có một dòng trỏ về. Tầng 3 được phép có nhiều nguồn, vì là dữ liệu.
Tầng của từng file: bảng [tang.json](tang.json) (mẫu đường dẫn ứng với tầng; chỉ mục `chi-muc.md` hiện tầng). Bộ đánh giá toàn bộ não: [bai-kiem/](bai-kiem/README.md).

## 3. Quy trình cố định cho mọi thông tin mới (6 câu, lần nào cũng áp dụng)
1. **Là gì?** dữ kiện · quyết định của David · cách làm · ví dụ / số liệu; câu trả lời quyết định tầng và loại file.
2. **Phục vụ mục đích nào ở tầng 0?** Không gắn được với mục đích nào thì không lưu (hoặc chỉ ghi `du-an/danh-sach-y-tuong.md`).
3. **Đã có nguồn duy nhất chưa?** Nếu có thì bổ sung hoặc sửa trực tiếp đúng nguồn đó. Nếu chưa thì tạo nguồn mới ở **tầng 3 trước**.
4. **Gốc là gì?** Liên kết với khối nào của [tu-duy-goc.md](tu-duy-goc.md), gốc nào trong khung. Ghi ngắn lý do đúng (lý do giúp AI làm đúng thì viết trong luật; ngày và lời David thì ghi vào sổ).
5. **Liên kết với đâu?** Liên kết tới nguyên lý / nơi dùng, một dòng ở `ban-do/` (quy ước: `quy-uoc-lien-ket.md`). Thông tin không được liên kết tới thì coi như không tồn tại.
6. **Kiểm thế nào?** Câu kiểm, mẫu chuẩn, hay số liệu nào sẽ cho biết thông tin đó hữu ích? Chưa có thì ghi giả thuyết "kỳ vọng Y, đo lại sau N lần".

## 4. Luật thăng cấp (như não ngủ để củng cố)
- Thông tin mới **luôn vào tầng 3 trước**. Thông tin thăng cấp lên tầng 2 khi **lặp ít nhất 2 lần** hoặc David chốt thành cách làm. Thăng cấp lên tầng 1 khi có **ít nhất 3 trường hợp cùng
  gốc** và đã có câu kiểm. Thăng cấp lên tầng 0 chỉ khi David chốt và chờ vài ngày (`david.md` mục 2).
- **Lời David mới được xếp vào tầng theo bậc:** ghi sổ (tầng 3) và cách làm (tầng 2) kèm một câu kiểm ngay trong ngày; thăng cấp lên tầng 1 chỉ khi công cụ thăng cấp
  (`tu-dong-hoa/hoc-lien-tuc/thang-cap.py`) đề xuất đủ ba trường hợp cùng gốc và David chốt. AI không đưa một lời nói đơn lẻ trực tiếp vào tầng 1
  (trường hợp 25/11/2026: năm luật được đưa vào tầng 1 trong một ngày).
- **Lỗi nào David phải sửa cũng thành một câu kiểm** của bộ đó (video: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/de.json`), để
  bản sau không lặp lại. Bộ kiểm chỉ tăng thêm, không bỏ câu khi chưa có lý do ghi sổ.
- Chiều ngược lại cũng có luật: luật tầng 1–2 lâu không dùng hoặc số liệu cho thấy không hữu ích thì AI đề xuất cắt giảm (David duyệt), rồi chuyển vào `luu-tru/`.

## 5. Ba vòng học (cùng một trục, khác nhịp)
| Vòng | Như AI | Khi | Làm | Ở đâu |
|---|---|---|---|---|
| **Mỗi việc** | phản hồi tức thì | khi xong một việc | David sửa gì → sửa trực tiếp đúng nguồn + một dòng sổ; lỗi → câu kiểm | `chuan-muc-lam-viec.md` mục 4 |
| **Mỗi tuần** | tinh chỉnh nhỏ | sáng thứ 6 | gom tín hiệu lặp, học hình mẫu có số liệu, sửa quy trình | `hoc-lien-tuc` Việc 1–3 |
| **Nâng cấp** | một vòng huấn luyện + đánh giá + ra bản | công cụ đo báo trùng / rối, ít nhất 10 video có số liệu mới, hoặc David yêu cầu | đo trước → chưng cất → cắt giảm → dọn dẹp → đo sau → ra bản | `hoc-lien-tuc` Việc 4, dọn dẹp: `tai-cau-truc` |

## 6. Bốn thước đo không đổi (dùng để chấm mọi bản)
1. **Người đọc mới làm đúng** — bài kiểm của bộ đạt, không thấp hơn bản trước.
2. **Kết quả thực tế tốt lên** — người xem (nhắn "gỡ", giữ chân), David phải sửa ít đi.
3. **Một ý một nguồn duy nhất** — công cụ đo chồng chéo không báo trùng / rối.
4. **Bằng chứng thắng** — lời David mới nhất thắng; tầng càng cao càng cần bằng chứng mạnh; không có bằng chứng thì ghi giả thuyết, không đoán.

## 7. Đổi trục
**Nâng cấp khác đổi gốc** (David 25/11/2026: "đã là gốc rồi thì sẽ rất ít khi thay đổi, chỉ có nâng cấp và cải tiến để tối ưu hơn thôi, còn để dẫn đến trường hợp thay đổi vào gốc thì phải dựa vào rất nhiều lần tương tác và các dẫn chứng cụ thể"):
- **Nâng cấp:** làm rõ câu chữ, thêm ví dụ, thêm liên kết, gắn thêm một lớp lên gốc có sẵn (như gắn ba hướng nghề lên ba phạm trù). Nghĩa cũ được giữ nguyên.
- **Đổi gốc:** đổi nghĩa một câu gốc. Việc này phải có nhiều lần tương tác và dẫn chứng cụ thể ghi ở [so-dan-chung-goc.md](so-dan-chung-goc.md), David chốt sau vài ngày.
- **Cổng kiểm soát gốc:** `tu-dong-hoa/cong-kiem-soat-goc.py` chạy trong `dong-bo.sh --push`: file tầng 0 thay đổi mà sổ dẫn chứng không có dòng tương ứng (ngày, file, loại, lời David) thì không cho push.

Trục chỉ đổi khi David nói rõ, sau vài ngày cân nhắc; khi đổi thì viết lại đúng câu ở đây, lý do ghi vào ghi nhớ `quy-tac-truc-tri-thuc`.
Mọi thay đổi khác của bộ não (học nguồn mới, đổi luật, thêm skill) đi **qua** trục, không sửa trục.
