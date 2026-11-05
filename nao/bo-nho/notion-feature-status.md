---
name: notion-feature-status
description: "Trạng thái tính năng App notion — ĐÃ PIVOT sang V2 (3 trục); model cũ đã xoá sạch. Nguồn sự thật: notion-v2-spec-plan"
metadata:
  node_type: memory
  type: project
  originSessionId: a330419c-6639-476e-ae0e-32d7f3c2d7fd
  modified: 2026-08-12T07:41:50.434Z
---

⚠️ **App đã pivot hoàn toàn sang V2 "3 trục" (2026-08-12).** Toàn bộ model cũ (projects/tasks/sections/subtasks/contacts/transactions/obligations/finance_profiles + CRM/Kanban/Analytics/Tài chính-cũ + mọi route `/tasks //contacts //finance //projects //overview`…) **đã bị gỡ code + drop bảng** trong đợt "dọn luôn". Đừng tham chiếu bảng/route/file cũ — chúng không còn tồn tại. **Nguồn sự thật hiện tại là [[notion-v2-spec-plan]]** (mô tả đầy đủ 9 bảng V2, backend `routes/v2.ts`, frontend `components/v2/*`, Telegram V2, và trạng thái từng pha kể cả Pha 4b dọn kho đã xong).

**Hiện trạng V2 tóm tắt:**
- **9 bảng:** users, settings, notes, people, market_items, money_entries, goals, actions, links (backbone liên kết đa hình). Xem chi tiết trong [[notion-v2-spec-plan]].
- **Nav 4 mục:** Hôm nay · Con người · Thị trường · Tiền + nút nổi "Ghi nhanh" (5 loại). Mobile-first bottom nav.
- **Tài chính = Nhập/Xuất/Tồn** (Tồn = Σ actual in − out; có "Chốt số dư thực tế"/reconcile vì không có bảng số-dư-đầu-kỳ). Dự báo 30 ngày từ money_entries planned.
- **Việc (actions)** danh sách phẳng xếp theo điểm ưu tiên (spec §18); Hoàn thành hỏi Kết quả + Bước tiếp.
- **Con người** hiển thị Mệnh/Vận (numerology, chỉ hiển thị) + Liên kết chéo sang việc/tiền qua `links`.
- **Telegram V2** (`telegram.ts` ~180 dòng): `việc <text>`→action, bắt tiền chi/thu→money_entry, `/homnay` `/sodu` `/help`, bản tin sáng dedup qua `users.daily_brief_on`.

**Hạ tầng vận hành CÒN NGUYÊN (không đụng khi pivot):** launchd 24/7 (`~/.congviec/` + `com.congviec.{postgres,backend,frontend,caffeinate,backup}`, PGDATA `~/.congviec/pgdata`, `ctl.sh`), sao lưu tự động (`npm run backup` → JSON.gz + iCloud, LaunchAgent 12:30), watchdog 300s ping+Telegram. Chi tiết chạy local ở [[notion-local-dev-environment]].

**Còn ngỏ (chưa làm, giữ lean — chỉ làm khi user yêu cầu):** export CSV (spec §26; JSON đã có qua `npm run backup`); UI cấu hình/kết nối lại Telegram trong app (đã gỡ khi dọn, bot vẫn chạy vì token+chat đã ở DB — sửa token phải thêm lại màn settings nhỏ hoặc sửa settings DB trực tiếp).
