---
description: "Bài kiểm toàn bộ não: 16 tình huống lấy từ chính những lần David phải sửa và các luật David đã chốt; một AI chưa đọc gì làm bài để đo bộ não có dạy đúng không (thước 1 của trục tri thức)."
---

# Bài kiểm toàn bộ não — người đọc lạnh có làm đúng không

Đây là **bộ đánh giá** của trục tri thức ([../truc-tri-thuc.md](../truc-tri-thuc.md) mục 1 và 6): như bài thi một mô hình trí tuệ nhân tạo phải
qua trước khi ra bản mới. Bài kiểm riêng phần dựng video nằm ở `ky-nang/san-xuat-video/thiet-ke-bo-cuc/bai-kiem/`.

## Các file
- [de.json](de.json) — câu hỏi: tình huống + ba lựa chọn. Người làm bài chỉ được đọc file này.
- `dap-an.json` — đáp án, nhà của luật, lời David làm nguồn. **Người làm bài không mở.**
- [cham.py](cham.py) — máy chấm.

## Khi nào chạy
- Mỗi đợt Nâng cấp: một lần trước khi sửa (điểm nền) và một lần sau khi sửa (`ky-nang/hoc-lien-tuc/SKILL.md` Việc 4). Bản mới chỉ được
  ra khi điểm sau bằng hoặc cao hơn điểm nền.
- Máy mới, hoặc trí tuệ nhân tạo khác bắt đầu dùng bộ não.

## Cách làm
1. Một trí tuệ nhân tạo **chưa đọc gì trong phiên** chỉ được đọc `AGENTS.md` rồi tự tìm file theo chỉ dẫn trong đó (chỉ mục, bản đồ). Không mở `dap-an.json`.
2. Với mỗi câu trong `de.json`, viết một dòng vào `bai-lam.json`: `{"id": "c01", "chon": "A", "vi": "<lý do, nêu file đã dựa vào>"}`.
3. Chấm: `python3 -I cham.py bai-lam.json`. Đạt khi đúng ít nhất 15 trên 16 câu.
4. Câu sai không phải lỗi của người làm bài: đó là chỗ bộ não **dạy chưa rõ**. Sửa nhà của luật mà máy chấm chỉ ra cho rõ hơn, rồi cho
   một trí tuệ nhân tạo chưa đọc gì làm lại.

## Bộ kiểm lớn dần
Lỗi nào David phải sửa (nhắc lại, chỉnh lời, đổi cách làm) → thêm một câu từ chính tình huống đó: câu hỏi vào `de.json`, đáp án + nhà +
lời David vào `dap-an.json` (trục mục 4). Không bỏ câu cũ khi chưa ghi lý do vào sổ. Đổi số câu thì ngưỡng đạt tự theo (số câu trừ 1).

Thử máy chấm: `python3 -I cham.py --mau > /tmp/mau.json && python3 -I cham.py /tmp/mau.json` phải ra đúng hết.
