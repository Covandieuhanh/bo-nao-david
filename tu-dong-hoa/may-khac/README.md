---
description: "Máy khác dựng video giống Mac chính (Windows qua WSL2, Mac khác): khoá phiên bản công cụ, cài một lệnh, máy tự kiểm so với bản chuẩn của Mac."
---

# Máy khác dựng video giống Mac chính

**David chốt 20/11/2026:** máy nào của David (Mac hay Windows) cũng lấy bộ não, skill trên GitHub về và dựng video ra kết quả như Mac chính. Máy nào cũng đẩy lên GitHub được (cùng tài khoản David). Máy khác **chỉ làm video**; bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ ở Mac chính.

| File | Việc |
|---|---|
| [phien-ban.env](phien-ban.env) | Phiên bản khoá của từng công cụ (đo trên Mac chính). Đổi bản chỉ làm ở Mac chính |
| [cai-cong-cu-video.sh](cai-cong-cu-video.sh) | Cài đúng các bản đó: Mac (brew), Windows qua WSL2 / Linux (apt + bản dựng sẵn) |
| [kiem-may.sh](kiem-may.sh) | So công cụ với bản khoá, dựng thử 20 s bằng đúng script của skill, so với bản chuẩn Mac → ĐẠT / LỆCH |
| [so-sanh.py](so-sanh.py) | Thước so: chữ chép lời, khung mặt, khung hình (SSIM) |

Cách cài từng máy: [huong-dan-cai-dat.md](../../huong-dan-cai-dat.md) mục 2 (Mac) và 3 (Windows).

## Cái gì giống hệt, cái gì gần giống

- **Giống hệt**: kịch bản cảnh, luật, skill (cùng repo); khung dựng Remotion, React, font (khoá trong `package-lock.json` của khuôn); Node; mô hình Whisper (mã kiểm). Khung hình Remotion so SSIM ≥ 0,98.
- **Gần giống, có thước đo**:
  - Dò mặt: Mac dùng Vision (chỉ Mac có). Máy khác dùng YuNet + MediaPipe, quy đổi theo thước Vision bằng `he-so-mat.json`. Đo 20/11/2026: khớp khoảng 90% số mặt, độ trùng khung khoảng 0,8. Phần lệch là mặt quay nghiêng: Vision bỏ sót, máy khác vẫn bắt.
  - Chép lời: cùng mô hình nhưng phần cứng khác, nên có thể lệch vài chữ (ngưỡng ≥ 90%).
  - ffmpeg trên Linux là bản dựng sẵn cùng nhánh 9.0.
- **Chỉ Mac có**: tự kiểm Drive đã tải lên mây xong chưa. Máy khác vẫn chép lên Drive và so khớp từng file, nhưng không tự xoá bản trên máy.

## Đã thử (20/11/2026)

| Máy | Kết quả |
|---|---|
| Mac chính, so với bản chuẩn của chính nó | Đạt hết: chép lời 100%, mặt 100%, khung hình SSIM 1,0000 |
| Ubuntu 24.04 chip ARM (máy ảo trên Mac) | Cài từ đầu không lỗi; **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**: chép lời 97,6%, mặt 89% (độ trùng 0,79), khung hình SSIM 0,996–0,9998 |
| Ubuntu 24.04 x86 như máy Windows (giả lập trên Mac) | Cài từ đầu không lỗi, có MediaPipe; dò mặt 89%. Whisper và Remotion chậm hoặc sập do giả lập chip, không phải do skill; máy Windows thật không chạy giả lập |
| Máy Windows thật (Windows 11, WSL2 Ubuntu 24.04, card NVIDIA RTX 5060), 20/11/2026 | Cài từ đầu không lỗi; **"MÁY NÀY DỰNG GIỐNG MAC CHÍNH"**: chép lời 100% (87/87 chữ), mặt 89% (độ trùng 0,79), khung hình SSIM 0,9957–0,9998. Whisper dựng kèm CUDA: chép 20 s mất 5 s (CPU 35 s) |

Máy mới: lần đầu cài, chạy `kiem-may.sh` để xác nhận.

**Card NVIDIA trên Windows (WSL2):** `cai-cong-cu-video.sh` chỉ dựng whisper kèm CUDA khi có `nvcc`. Card đời mới (RTX 50) cần CUDA ≥ 12.8; gói `nvidia-cuda-toolkit` của Ubuntu là 12.0 nên không dùng được. Cài 3 gói từ kho NVIDIA `wsl-ubuntu` (bản đầy đủ `cuda-toolkit` tải rất chậm): `sudo apt-get install -y --no-install-recommends cuda-nvcc-12-9 cuda-cudart-dev-12-9 libcublas-dev-12-9`, thêm `/usr/local/cuda-12.9/bin` vào PATH, xoá `~/.local/bin/whisper-cli` rồi chạy lại `cai-cong-cu-video.sh` (RTX 50: `CUDAARCHS=120`).

## Việc của Mac chính

- **Nâng công cụ** (Remotion, ffmpeg…): cài bản mới, dựng thử, sửa `phien-ban.env` / `package.json` + `package-lock.json` của khuôn. Sau đó tạo lại bản chuẩn: `zsh tu-dong-hoa/may-khac/kiem-may.sh --tao-chuan <video người nói rõ mặt> <giây bắt đầu>`, rồi đẩy GitHub. Máy khác chạy lại `cai-cong-cu-video.sh` + `kiem-may.sh`.
- **Đo lại hệ số dò mặt** khi đổi cách dò: `~/.cache/dung-video-theo-phong-cach/mat-venv/bin/python ky-nang/san-xuat-video/dung-video-theo-phong-cach/scripts/do-he-so-mat.py <video> …`
- Bộ thử máy (đoạn 20 s + bản chuẩn) nằm trên Drive `tu-lieu-goc/_bo-thu-may/`, không lên GitHub (video gốc).

## Nhiều máy cùng đẩy

Đầu phiên kéo về, cuối phiên đẩy lên, git tự gộp khi hai máy sửa khác chỗ. Nếu hai máy sửa trùng một dòng, `dong-bo.sh` huỷ lần gộp (không mất bản nào) và ghi `~/.claude/logs/xung-dot-nao.txt`. Đầu phiên sau, Claude thấy cảnh báo ⛔ và gộp tay giúp David.
