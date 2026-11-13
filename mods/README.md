# Mod của Claude Code

> **Đã gỡ hết 13/11/2026** theo lời David (ghi nhớ `luat-mod-tu-chay`): không cài mod nào, `scripts/install.sh` chỉ cài Telegram. Phần dưới giữ làm lưu trữ; mã Sổ việc còn ở `so-viec/`.

Mod là plugin chạy trong Claude Code (tab Code của app, terminal): vẽ bảng, dòng trên ô nhập, lệnh `/...`, chặn hay theo dõi việc Claude làm.
Cài ở cấp người dùng Mac nên **mọi phiên, mọi tài khoản Claude** trên máy đều có. Mod chỉ nạp khi phiên mở: cài xong phải mở phiên mới.
Không chạy trên chat claude.ai và app điện thoại.



| Mod | Của ai | Làm gì | Lệnh |
|---|---|---|---|
| [so-viec](so-viec/README.md) | David (repo này) | Video đang làm, % giới hạn tuần đã dùng, trung bình 1 video mất bao lâu và tốn bao nhiêu % tuần | `/so-viec`, `/bao-cao` |
| savvy-progress | johnnyvizz/claude-kit | Bảng các trợ lý con đang chạy: model, tiến độ, token, chi phí ước tính. Tự mở khi có trợ lý con chạy (`autoOpen: any` trong `pluginConfigs` của `~/.claude/settings.json`) | `/agents-info` |
| collision-guard | nateherkai/claude-code-mods | Trước khi sửa file mà khung khác vừa sửa trong 30 phút: hỏi sửa tiếp / chuyển sang worktree / huỷ | `/guard` |
| goal-meter | nateherkai/claude-code-mods | Thanh tiến độ và giờ dự kiến xong trên ô nhập. Tự hiện ở mọi việc từ 3 bước vì Claude lập kế hoạch bằng công cụ của nó (`skills/thoi-quen-lam-viec.md` mục 3), không cần `/goal` | `/goals` |

## Cài

- `so-viec`: repo này là chợ plugin `david-claude` (`.claude-plugin/marketplace.json`), cài `so-viec@david-claude`. Plugin đọc thẳng từ `mods/so-viec`: sửa code trong repo rồi mở phiên mới là có bản mới, không cài lại.
- Mod cộng đồng: `claude plugin marketplace add <chủ>/<repo>` rồi `claude plugin install <mod>@<chợ> --scope user`. Bản cài là bản chép, chỉ đổi khi chạy `claude plugin update`.

## Luật với mod cộng đồng

Đọc hết mã nguồn trước khi cài và trước mỗi lần cập nhật. Chỉ cài khi không truy cập mạng, không gửi dữ liệu đi, không chạy lệnh lạ.

Lần đọc 11/11/2026 (savvy-progress `c871c15`, collision-guard và goal-meter `33a936f`):
- Không gọi mạng, không gửi dữ liệu đi. Dữ liệu ở `~/.claude/mods-data/` và kho riêng của mod.
- Lệnh chạy trên máy: `git ls-files` (collision-guard: file có trong git không), `tail` (goal-meter: đọc vài dòng cuối lịch sử phiên).
- savvy-progress thêm một dòng vào lời giao việc cho trợ lý con tên `savvy-*`; goal-meter chèn lời nhắc ẩn cho Claude khi chạy `/goal`.
- Giấy phép MIT.

## Gỡ

`claude plugin uninstall <mod>@<chợ>`.
