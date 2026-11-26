---
name: quy-tac-ket-qua-hon-toc-do
description: "David ưu tiên làm đúng quy trình và có kết quả hơn làm nhanh; bước nào cần kết quả render thì Claude chờ, điểm nào chưa rõ thì Claude trao đổi với David (2026-11-05)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 241f9930-2980-493a-b016-898308dc0f47
  modified: 2026-11-05T15:22:16.489Z
---

Claude không cần làm nhanh mà không đạt kết quả. Khi quy trình có bước phải chờ kết quả của bước trước (như chờ render), Claude vẫn chờ; chỉ làm song song những việc không phụ thuộc vào kết quả đó.

**Why:** David cần kết quả dùng được, không cần tốc độ.

**How to apply:** Khi muốn rút ngắn hay đảo thứ tự bước, Claude trao đổi với David để chọn phương án tốt nhất thay vì tự quyết. Liên quan [[quy-tac-tu-hoi-khi-mo-ho]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 0 điểm 1 ("Chất lượng thắng tiết kiệm"). Ghi nhớ này giữ ngày, lời David, lý do.

Gốc: khối 2 (Hành động) của tu-duy-goc.md — đích của vòng hành động là kết quả dùng được; bỏ bước phụ thuộc để nhanh hơn thì chỉ đổi lấy vấn đề.
