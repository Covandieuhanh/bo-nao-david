---
name: luat-mod-tu-chay
description: "Mod, plugin cài thêm bắt buộc tự hoạt động khi cần, không đợi David gõ lệnh; việc ≥3 bước tự lập kế hoạch bằng goal-meter (2026-11-11)"
metadata:
  type: feedback
---

Mọi mod hay plugin thêm vào Claude Code phải tự chạy đúng lúc cần, không phải David yêu cầu mới làm. Lệnh `/...` của mod chỉ để xem chi tiết.

**Why:** 11/11/2026, sau khi cài Sổ việc và 3 mod cộng đồng (savvy-progress, collision-guard, goal-meter), David nói: "tất cả các mod hay plugin thêm vào bắt buộc phải tự động hoạt động khi cần chứ không phải yêu cầu thì mới làm". Lúc đó savvy-progress chỉ tự mở bảng với trợ lý con `savvy-*`, goal-meter chỉ chạy khi gõ `/goal`. David "Ok, ghi luật" cho cách để goal-meter tự hiện tiến độ ở mọi việc nhiều bước.

**How to apply:** cài mod mới thì kiểm phần nào cần gọi mới chạy, chỉnh cho tự chạy bằng tuỳ chọn của mod (savvy-progress: `pluginConfigs` → `autoOpen: any` trong `~/.claude/settings.json`) hoặc bằng luật làm việc; không được thì báo David. Việc từ 3 bước: gọi `mcp__goal-meter__tasks` (`plan`/`start`/`done`). Liên quan [[luat-cong-cu-cai-dua-vao-skill]].

Nhà của luật: `skills/thoi-quen-lam-viec.md` mục 3 ("Mod phải tự chạy khi cần", "Việc từ 3 bước trở lên"). Danh sách mod: `mods/README.md`. Ghi nhớ này giữ ngày, lời David, lý do.
