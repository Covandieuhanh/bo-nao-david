# Bàn giao

## Báo cáo cho người dùng (tiếng Việt, ngắn)
1. Bản cuối: đường dẫn `video-final.mp4` (đã gửi file), thời lượng.
2. Danh sách cảnh theo mốc: `0:14 chữ to "KỂ CHUYỆN VỀ NGHỀ."`, `0:36–0:48 toàn màn hình: các nghề 02→07`...
3. Đã kiểm tra: khung hình trong vùng an toàn, âm lượng như gốc, dấu tiếng Việt.
   Chưa kiểm tra: đăng thử thật trên nền tảng (khuyên đăng riêng tư một lần).
4. Ảnh cần ghi nguồn: dán nội dung `nguon-anh.txt` vào mô tả bài đăng (video không có màn hình nguồn ảnh ở cuối;
   chỉ thêm bằng `credits_card.py --card` khi người dùng yêu cầu).
5. Muốn chỉnh: nói mốc thời gian + điều muốn đổi. (Không nhắc DaVinci/timeline trừ khi người dùng đã yêu cầu.)

## Mẫu `davinci/HUONG-DAN.md` (chỉ khi người dùng yêu cầu timeline)

```markdown
# Mở trong DaVinci Resolve
1. DaVinci Resolve → New Project → mở project.
2. File → Import → Timeline… (Shift+Cmd+I) → chọn `timeline.fcpxml`.
3. Để tick "Automatically import source clips into media pool" → OK.
4. Clip đỏ (offline) → chuột phải trong Media Pool → Relink Selected Clips… → chọn thư mục `media`.
Timeline nằm ngang thay vì dọc → Timeline Settings → bỏ "Use Project Settings" → <W> x <H>.

| Track | Nội dung |
|---|---|
| V1 + A1 | Video gốc + tiếng |
| V2 | Cảnh toàn màn hình: <id...> |
| V3 | Thẻ thông tin: <id...> |
| V4 | Chữ to / tên người nói: <id...> |
| V5 | Khung an toàn (tắt sẵn — bật để kiểm tra khi tự dời clip, tắt trước khi xuất) |
| Cuối | 5 giây nguồn ảnh (chỉ khi đã làm `--card`) |

Đổi chữ/số/màu của hoạt hình: nhờ Claude sửa rồi render lại cảnh đó (clip cùng tên tự cập nhật trong Resolve).
Xuất: trang Deliver → H.264 MP4, <W>x<H> → Add to Render Queue → Render All.
```

## Mở DaVinci (khi người dùng muốn tự chỉnh)
```bash
open -a "DaVinci Resolve"; open -R "$P/davinci/timeline.fcpxml"
```
Bản App Store không import tự động được — hướng dẫn người dùng 4 bước ở trên.
