---
name: quy-tac-cong-cu-cai-dua-vao-ky-nang
description: "Công cụ David đã tải hoặc cài (ví dụ pyannote) là để nâng cao skill; công cụ nào giúp làm việc tốt hơn thì Claude đưa trực tiếp vào skill dựng video, không để không dùng đến (2026-11-07)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbdca2f7-d150-4f29-9b51-a450fb69af85
  modified: 2026-11-07T09:39:59.119Z
---

David tải ứng dụng, mô hình về thiết bị là để nâng cao skill của mình. Công cụ nào giúp làm việc tốt hơn (nhận diện giọng nói, chép lời…) thì Claude đưa hết vào skill dựng video.

**Why:** 07/11/2026 Claude phát hiện pyannote đã cài ở `~/.venvs/pyannote` nhưng `nguoi-noi.py` vẫn tự phân biệt giọng bằng k-means; David nói "đương nhiên đưa hết vào skill".

**How to apply:** khi thấy công cụ đã cài mà skill chưa dùng, Claude đề xuất tích hợp ngay (vẫn diễn giải ngắn trước khi sửa skill), giữ cách cũ làm phương án dự phòng khi công cụ lỗi. Liên quan [[video-kien-truc-ky-nang]].

Nguồn của luật: `ky-nang/chuan-muc-lam-viec.md` mục 3 ("Công cụ David đã cài là để nâng skill"). Ghi nhớ này giữ ngày, lời David, lý do.

Gốc: khối 3 (Học và thay đổi) của tu-duy-goc.md — công cụ đã cài chỉ có giá trị khi được đưa vào skill và làm việc tốt hơn; nằm không thì chưa có thay đổi.
