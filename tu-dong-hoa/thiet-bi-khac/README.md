---
description: "Thiết bị khác dựng video giống Mac chính (Windows qua WSL2, Mac khác): khoá phiên bản công cụ, cài một lệnh, thiết bị tự kiểm tra so với bản chuẩn của Mac."
---

# Thiết bị khác dựng video giống Mac chính

**David chốt 20/11/2026:** thiết bị nào của David (Mac hay Windows) cũng lấy bộ não và skill trên GitHub về rồi dựng video ra kết quả như Mac chính. Thiết bị nào cũng đẩy lên GitHub được (cùng tài khoản David). Thiết bị khác **chỉ làm video**; bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ ở Mac chính.

| File | Việc |
|---|---|
| [phien-ban.env](phien-ban.env) | Phiên bản khoá của từng công cụ (đo trên Mac chính). Đổi phiên bản chỉ làm ở Mac chính |
| [cai-cong-cu-video.sh](cai-cong-cu-video.sh) | Cài đúng các phiên bản đó: Mac (brew), Windows qua WSL2 hoặc Linux (apt và bản dựng sẵn) |
| [kiem-tra-thiet-bi.sh](kiem-tra-thiet-bi.sh) | So công cụ với bản khoá, dựng thử 20 s bằng đúng script của skill, so với bản chuẩn của Mac → ĐẠT / LỆCH |
| [so-sanh.py](so-sanh.py) | Thước đo so sánh: chữ chép lời, khung mặt, khung hình (SSIM) |

Cách cài trên từng thiết bị: [huong-dan-cai-dat.md](../../huong-dan-cai-dat.md) mục 2 (Mac) và 3 (Windows).

## Phần nào giống hệt, phần nào gần giống

- **Giống hệt**: kịch bản cảnh, luật, skill (cùng repo); khung dựng Remotion, React, phông chữ (khoá trong `package-lock.json` của mẫu); Node; mô hình Whisper (có mã băm checksum để kiểm tra). Khung hình Remotion so bằng SSIM đạt ít nhất 0,98.
- **Gần giống, có thước đo**:
  - Dò mặt: Mac dùng Vision (chỉ Mac có). Thiết bị khác dùng YuNet và MediaPipe, quy đổi theo thước đo của Vision bằng `he-so-mat.json`. Đo ngày 20/11/2026: khớp khoảng 90% số mặt, độ trùng khung khoảng 0,8. Phần lệch là mặt quay nghiêng: Vision bỏ sót, thiết bị khác vẫn phát hiện được.
  - Chép lời: cùng mô hình nhưng phần cứng khác, nên có thể lệch vài chữ (ngưỡng ít nhất 90%).
  - ffmpeg trên Linux là bản dựng sẵn cùng nhánh 9.0.
- **Chỉ Mac có**: tự kiểm tra Drive đã tải lên đám mây xong chưa. Thiết bị khác vẫn chép lên Drive và so khớp từng file, nhưng không tự xoá bản trên thiết bị.

## Đã thử (20/11/2026)

| Thiết bị | Kết quả |
|---|---|
| Mac chính, so với bản chuẩn của chính nó | Đạt toàn bộ: chép lời 100%, mặt 100%, khung hình SSIM 1,0000 |
| Ubuntu 24.04 chip ARM (máy ảo trên Mac) | Cài từ đầu không lỗi; **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**: chép lời 97,6%, mặt 89% (độ trùng 0,79), khung hình SSIM 0,996–0,9998 |
| Ubuntu 24.04 x86 như thiết bị Windows (giả lập trên Mac) | Cài từ đầu không lỗi, có MediaPipe; dò mặt 89%. Whisper và Remotion chậm hoặc dừng đột ngột do giả lập chip, không phải do skill; thiết bị Windows thật không chạy giả lập |
| Thiết bị Windows thật (Windows 11, WSL2 Ubuntu 24.04, card NVIDIA RTX 5060), 20/11/2026 | Cài từ đầu không lỗi; **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**: chép lời 100% (87/87 chữ), mặt 89% (độ trùng 0,79), khung hình SSIM 0,9957–0,9998. Whisper dựng kèm CUDA: chép 20 s mất 5 s (chạy bằng CPU mất 35 s) |

Thiết bị mới: lần đầu cài, chạy `kiem-tra-thiet-bi.sh` để xác nhận.

**Card NVIDIA trên Windows (WSL2):** `cai-cong-cu-video.sh` chỉ dựng whisper kèm CUDA khi có `nvcc`. Card thế hệ mới (RTX 50) cần CUDA ít nhất 12.8; gói `nvidia-cuda-toolkit` của Ubuntu là bản 12.0 nên không dùng được. Cài 3 gói từ kho NVIDIA `wsl-ubuntu` (bản đầy đủ `cuda-toolkit` tải rất chậm): `sudo apt-get install -y --no-install-recommends cuda-nvcc-12-9 cuda-cudart-dev-12-9 libcublas-dev-12-9`, thêm `/usr/local/cuda-12.9/bin` vào PATH, xoá `~/.local/bin/whisper-cli` rồi chạy lại `cai-cong-cu-video.sh` (RTX 50: `CUDAARCHS=120`).

## Việc của Mac chính

- **Nâng phiên bản công cụ** (Remotion, ffmpeg…): cài phiên bản mới, dựng thử, sửa `phien-ban.env`, `package.json` và `package-lock.json` của mẫu. Sau đó tạo lại bản chuẩn: `zsh tu-dong-hoa/thiet-bi-khac/kiem-tra-thiet-bi.sh --tao-chuan <video người nói rõ mặt> <giây bắt đầu>`, rồi đẩy GitHub. Thiết bị khác chạy lại `cai-cong-cu-video.sh` rồi `kiem-tra-thiet-bi.sh`.
- **Đo lại hệ số dò mặt** khi đổi cách dò: `~/.cache/dung-video-theo-phong-cach/mat-venv/bin/python ky-nang/san-xuat-video/dung-video-theo-phong-cach/scripts/do-he-so-mat.py <video> …`
- Bộ thử thiết bị (đoạn 20 s và bản chuẩn) nằm trên Drive `tu-lieu-goc/_bo-thu-may/`, không đưa lên GitHub (vì là video gốc).

## Nhiều thiết bị cùng đẩy

Đầu phiên Claude kéo về, cuối phiên đẩy lên; git tự gộp khi hai thiết bị sửa khác chỗ. Nếu hai thiết bị sửa trùng một dòng, `dong-bo.sh` huỷ lần gộp (không mất bản nào) và ghi `~/.claude/logs/xung-dot-nao.txt`. Đầu phiên sau, Claude thấy cảnh báo ⛔ và gộp thủ công giúp David.
