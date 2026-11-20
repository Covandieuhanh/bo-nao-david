---
description: "Trục tri thức (tầng 0) — cách bộ não David tiếp nhận, xử lý, học và nâng cấp MỌI thông tin, dựng theo cách một mô hình AI như Claude được làm ra: dữ liệu → chưng cất → phản hồi → đánh giá → ra bản. Mọi skill học / sửa / lưu chỉ trỏ về đây."
---

# Trục tri thức — bộ não David như một bộ não Claude thu nhỏ

Học thêm bao nhiêu thì **nội dung** dày lên; **trục này không đổi**. Mọi cách học, sửa, lưu ở nơi khác (`chuan-muc-lam-viec.md` mục 4,
`hoc-lien-tuc`, `tai-cau-truc`, học video mẫu) là cách áp trục này cho một việc, không đặt ra cách riêng. Mục đích, giá trị, lằn ranh
mà mọi thứ phục vụ: `david.md` mục 1–3 và sáu luật `AGENTS.md`.

## 0. Gốc: AI dùng bộ não này là ai
AI (Claude, Codex, Gemini…) mỗi phiên **bắt đầu từ số 0** về David; thứ nó biết chỉ là những gì đọc được từ file. Vì vậy:
> **Thước không bao giờ đổi:** một AI mới tinh, đọc ít nhất, vẫn làm đúng như David muốn — và lần sau đúng hơn lần trước.

Mọi quyết định lưu gì, lưu ở đâu, viết thế nào đều trả lời câu này.

## 1. Mô hình AI được làm ra thế nào → bộ não làm y vậy

| Mô hình AI | Làm gì | Ở bộ não David |
|---|---|---|
| **Dữ liệu huấn luyện** (Pretraining Data) | rất nhiều ví dụ thật, cứ thêm vào, không sửa cái cũ | tầng 3: lời David, ca thật, số liệu, sổ quyết định, nguồn học |
| **Hiến chương** (Constitution) | vài nguyên tắc nhỏ đứng trên, dùng để chấm mọi thứ khác | tầng 0: trục này + mục đích, giá trị, lằn ranh |
| **Chưng cất** (Distillation) | nén nhiều ví dụ thành quy luật chung, không nhớ từng ví dụ | nhiều ca cùng gốc → một **nguyên lý** + 1–3 ca mẫu (tầng 1) |
| **Tinh chỉnh bằng ví dụ tốt** (Fine-tuning on Demonstrations) | học từ bản mẫu đã được người duyệt | sản phẩm David đã duyệt: ca mẫu, mẫu chuẩn, kịch bản thật |
| **Học từ phản hồi** (Feedback Learning) | lời người chấm làm đổi cách làm | lời David sửa (`tin-hieu.jsonl` trường `david_sua`), số liệu người xem |
| **Bộ đánh giá** (Evals) | bài kiểm cố định, chạy trước khi ra bản, **lỗi nào cũng thành một câu kiểm** | bài kiểm từng bộ, mẫu chuẩn, phép thử người đọc lạnh |
| **Ra bản có số hiệu** (Versioned Release) | chỉ ra bản khi bằng hoặc tốt hơn; kém thì quay lại | mốc `nang-cap-<n>`, quay về `nang-cap-<n>-truoc` |
| **Cửa sổ ngữ cảnh + truy xuất** (Context Window, Retrieval) | lúc làm chỉ nạp phần lõi, còn lại tra khi cần | luôn đọc tầng 0 + skill đúng việc; tra tầng 3 qua `chi-muc.md` |
| **Quên có chọn lọc** (Pruning) | bỏ cái không giúp để cái giúp rõ hơn | tỉa: cái lâu không dùng / số liệu cho thấy vô ích → cất `luu-tru/` |

## 2. Bốn tầng — tầng càng cao càng ít đổi, đổi phải có bằng chứng càng mạnh

| Tầng | Chứa | Đổi khi | Ví dụ |
|---|---|---|---|
| **0 · Trục** | file này, mục đích, giá trị, lằn ranh, sáu luật | gần như không; David chốt sau vài ngày | `truc-tri-thuc.md`, `david.md` mục 1–3, `AGENTS.md` sáu luật |
| **1 · Nguyên lý** | vì sao làm vậy; áp được cho nhiều việc | vòng Nâng cấp, khi nhiều ca cùng gốc | `thiet-ke-bo-cuc/nguoi-xem-can-gi.md`, `chuan-muc-lam-viec.md` |
| **2 · Quy trình** | các bước của một loại việc | theo tuần, theo góp ý có bằng chứng | các `SKILL.md`, khối `mo-dun/`, hồ sơ tham số |
| **3 · Dữ liệu** | ca thật, số liệu, nguồn học, sổ, ghi nhớ, kho | thêm hằng ngày; **chỉ thêm**, không sửa nghĩa cái cũ | `giai-mau.md`, `so-lieu.md`, `nhat-ky-thay-doi.md`, `bo-nho/`, `bo-cuc.md` |

Trong tầng 1–2 mỗi ý chỉ **một nhà**; nơi khác một dòng trỏ. Tầng 3 được nhiều, vì là dữ liệu.

## 3. Đường đi cố định của mọi thông tin mới (6 câu, lần nào cũng vậy)
1. **Là gì?** dữ kiện · quyết định của David · cách làm · ví dụ / số liệu → quyết định tầng và loại file.
2. **Phục vụ mục đích nào ở tầng 0?** Không gắn được → không lưu (hoặc chỉ ghi `du-an/danh-sach-y-tuong.md`).
3. **Đã có nhà chưa?** Có → bổ sung / sửa thẳng đúng nhà đó. Chưa → nhà mới ở **tầng 3 trước**.
4. **Gốc là gì?** Ghi ngắn vì sao đúng (lý do giúp AI làm đúng thì viết trong luật; ngày + lời David thì vào sổ).
5. **Nối vào đâu?** Link tới nguyên lý / nơi dùng, một dòng ở `ban-do/` (quy ước: `quy-uoc-lien-ket.md`). Không ai nối tới = không tồn tại.
6. **Kiểm thế nào?** Câu kiểm, mẫu chuẩn, hay số liệu nào sẽ cho biết nó giúp? Chưa có → ghi giả thuyết "kỳ vọng Y, đo lại sau N lần".

## 4. Luật đi lên (như não ngủ để củng cố)
- Thông tin mới **luôn vào tầng 3 trước**. Lên tầng 2 khi **lặp ≥ 2 lần** hoặc David chốt thành cách làm. Lên tầng 1 khi **≥ 3 ca cùng
  gốc** và đã có câu kiểm. Lên tầng 0 chỉ khi David chốt và chờ vài ngày (`david.md` mục 2).
- **Lỗi nào David phải sửa cũng thành một câu kiểm** của bộ đó (video: `ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/de.json`), để
  bản sau không lặp lại. Bộ kiểm chỉ lớn lên, không bỏ câu khi chưa có lý do ghi sổ.
- Đi xuống cũng có luật: luật tầng 1–2 lâu không dùng hoặc số liệu cho thấy không giúp → đề xuất tỉa (David duyệt), cất `luu-tru/`.

## 5. Ba vòng học (cùng một trục, khác nhịp)
| Vòng | Như AI | Khi | Làm | Ở đâu |
|---|---|---|---|---|
| **Mỗi việc** | phản hồi tức thì | xong một việc | David sửa gì → sửa thẳng đúng nhà + một dòng sổ; lỗi → câu kiểm | `chuan-muc-lam-viec.md` mục 4 |
| **Mỗi tuần** | tinh chỉnh nhỏ | sáng thứ 6 | gom tín hiệu lặp, học hình mẫu có số liệu, sửa quy trình | `hoc-lien-tuc` Việc 1–3 |
| **Nâng cấp** | một vòng huấn luyện + đánh giá + ra bản | máy đo báo trùng / rối, ≥ 10 video có số liệu mới, hoặc David gọi | đo trước → chưng cất → tỉa → dọn → đo sau → ra bản | `hoc-lien-tuc` Việc 4, dọn: `tai-cau-truc` |

## 6. Bốn thước không đổi (chấm mọi bản)
1. **Người đọc lạnh làm đúng** — bài kiểm của bộ đạt, không thấp hơn bản trước.
2. **Kết quả thật tốt lên** — người xem (nhắn "gỡ", giữ chân), David phải sửa ít đi.
3. **Một ý một nhà** — máy đo chồng chéo không báo trùng / rối.
4. **Bằng chứng thắng** — lời David mới nhất thắng; tầng càng cao càng cần bằng chứng mạnh; không có bằng chứng thì ghi giả thuyết, không đoán.

## 7. Đổi trục
Trục chỉ đổi khi David nói rõ, sau vài ngày cân nhắc; đổi thì viết lại đúng câu ở đây, lý do vào ghi nhớ `quy-tac-truc-tri-thuc`.
Mọi thay đổi khác của bộ não (học nguồn mới, đổi luật, thêm skill) đi **qua** trục, không sửa trục.
