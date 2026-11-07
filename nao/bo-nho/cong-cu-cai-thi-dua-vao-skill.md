---
name: cong-cu-cai-thi-dua-vao-skill
description: "Công cụ David đã tải/cài (vd. pyannote) là để nâng skill — giúp việc tốt hơn thì đưa thẳng vào skill dựng video, không để nằm không (2026-11-07)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbdca2f7-d150-4f29-9b51-a450fb69af85
  modified: 2026-11-07T09:39:59.119Z
---

David tải ứng dụng, mô hình về máy là để gia tăng skill của mình. Công cụ nào giúp việc tốt hơn (nhận diện giọng nói, chép lời…) thì đưa hết vào skill dựng video.

**Why:** 07/11/2026 Claude phát hiện pyannote đã cài ở `~/.venvs/pyannote` nhưng `speakers.py` vẫn tự đoán giọng bằng k-means; David nói "đương nhiên đưa hết vào skill".

**How to apply:** khi thấy công cụ đã cài mà skill chưa dùng, đề xuất tích hợp luôn (vẫn diễn giải ngắn trước khi sửa skill), giữ cách cũ làm dự phòng khi công cụ lỗi. Liên quan [[video-skill-architecture]].
