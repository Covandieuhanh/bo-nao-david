---
name: tong-hop-tin-nhan
description: Tổng hợp tin nhắn hằng ngày của David từ Zalo, Messenger, Telegram — chỉ đọc, ra bảng việc cần làm / thoả thuận / đời thường, lưu trong sổ nhớ (~/Documents/2-ca-nhan/so-tay/tin-nhan/, không lên GitHub), tự ghi điều mới của từng người / đối tác vào danh-ba.md (trùng điều David đã ghi thì chỉ đánh dấu trùng) và gửi bản gọn về bot Telegram Sổ nhớ; David trả lời bot để gộp người, đánh dấu xong, bỏ qua. Dùng khi lịch hằng ngày chạy, khi David nói "tổng hợp tin", "tổng hợp tin nhắn", "hôm nay ai nhắn gì", "/tong-hop-tin-nhan".
---

# Tổng hợp tin nhắn

**Mục tiêu:** mỗi sáng David biết ngay ai đang chờ mình, mình đã hứa gì, có hạn chót nào — không phải mở 3 ứng dụng; và danh bạ từng người / đối tác tự cập nhật từ tin nhắn, David chỉ còn tự ghi điều không có trong tin (David chốt 14/11/2026).

## Luật cứng

- **Chỉ đọc.** Không gõ vào ô soạn tin, không bấm gửi, không thả cảm xúc, không gọi, không xoá, không rời nhóm.
- Không đăng nhập thay David. Trang đòi đăng nhập → ghi "⚠️ <nền tảng> cần David đăng nhập lại" vào tin gửi bot rồi làm tiếp nền tảng khác.
- Không chép số điện thoại, số tài khoản, địa chỉ nhà, mã OTP vào file hay tin Telegram.
- File chỉ ở `~/Documents/2-ca-nhan/so-tay/tin-nhan/` (gọi tắt `TN/`) và `~/Documents/2-ca-nhan/so-tay/danh-ba.md` (gọi tắt `DB`); cả hai là sổ nhớ, không lên GitHub, sao lưu Drive. Không đưa nội dung tin vào bộ não, ghi nhớ hay GitHub.
- Mở cuộc trò chuyện làm tin hiện "đã xem" → chỉ mở cuộc **có hoạt động mới kể từ lần trước và có thể có việc**; còn lại đọc dòng xem trước trong danh sách là đủ.

## Nguồn và cách đọc

| Nền tảng | Trình duyệt | Trang |
|---|---|---|
| Zalo | **Claude in Chrome** (Zalo Web không chạy trong trình duyệt Claude: thiếu kho lưu trữ bảo mật, tải lại liên tục) | chat.zalo.me |
| Messenger | Trình duyệt Claude (`mcp__Claude_Browser__*`) | www.messenger.com |
| Telegram | Trình duyệt Claude | web.telegram.org/a/ |

Trình duyệt Claude: dùng tab đang mở trang đó (`tabs_context`), không có thì `preview_start` với url. Chrome: `tabs_context_mcp`, dùng tab chat.zalo.me nếu có, không có thì tạo tab mới. Chrome chưa kết nối → ghi cảnh báo, bỏ Zalo lần này.

**Zalo** — `get_page_text` ra danh sách (tên · thời gian · dòng cuối). Mở cuộc: `find` tên → `computer left_click` theo `tai-lieu-tham-khao` (click bằng JS không mở được) → chờ 2 giây → `get_page_text` (ra khung `<article>` của cuộc đó). Danh sách cuộn ảo, `tai-lieu-tham-khao` đổi sau mỗi lần mở: `find` lại, hoặc gõ tên vào ô "Tìm kiếm" rồi bấm kết quả đầu. Zalo Web không phân biệt tin của David trong chữ: đoán theo ngữ cảnh, dòng xem trước có "Bạn:" là của David.

**Messenger** — danh sách: `javascript_tool` → `[...document.querySelectorAll('[role=row]')].map(r=>r.innerText)`; đường dẫn từng cuộc: `[role=row] a[href]`. Mở cuộc: `navigate` tới `https://www.messenger.com` + href → chờ 3 giây → `get_page_text` (có sẵn "Tin nhắn do Bạn/Tên gửi lúc …").

**Telegram** — `get_page_text` ra danh sách. Mở cuộc bằng JS: `a[href="#<id>"]` → `dispatchEvent(new MouseEvent('mousedown',{bubbles:true}))` + `click()` → chờ 2,5 giây → đọc `.MessageList` (lấy ~2.000 ký tự cuối). `navigate` tới `#id` không mở được cuộc. Bỏ qua: bot của David (Trợ lý David, Sổ nhớ, BotFather, Hermes), Saved Messages, kênh sưu tầm (Tri thức huyền học, Câu chuyện hay, Học về …) trừ khi có người khác nhắn.

**Bỏ qua mọi nơi:** quảng cáo, trang tự trả lời, kênh thông báo, sticker/cuộc gọi không kèm chữ (chỉ ghi "gọi nhỡ" nếu người đó gọi ≥2 lần hoặc kèm lời trách).

## Quy trình

1. Đọc trước:
   - bản tổng hợp gần nhất trong `TN/` → mốc lần trước, việc còn tồn;
   - `TN/ghi-chu.md` → việc David đã báo xong/bỏ (không nhắc lại), cuộc bị bỏ qua, người ưu tiên;
   - các dòng `tên trên mạng` trong `~/Documents/2-ca-nhan/so-tay/danh-ba.md` → gộp mọi tên trên Zalo/Messenger/Telegram của cùng một người thành **một dòng, ghi tên trong sổ** (ví dụ "Long Phạm (Zalo + Telegram)"). Mục `## <người>` trong `danh-ba.md` cho thêm bối cảnh để xếp việc đúng; không chép chi tiết riêng tư từ đó vào bản tổng hợp.
2. Đọc danh sách 3 nền tảng, lọc cuộc có tin mới sau mốc đó (lần đầu: 24 giờ qua).
3. Mở các cuộc đã lọc, đọc phần mới.
4. Viết `TN/tong-hop-YYYY-MM-DD.md` theo khuôn dưới. Việc tồn hôm trước chưa thấy xong (và không có trong `ghi-chu.md`) thì chép sang, ghi "(từ dd/mm)". Hai tên giống nhau rõ ràng mà chưa gộp (Rex (2)54 / Rex (2)) thì gộp và thêm dòng "❓ Gộp: … — sai thì nhắn bot" cuối tin.
5. **Ghi danh bạ** (`DB`) — mỗi người / đối tác có điều mới đáng nhớ (việc, hẹn, thoả thuận, con số đã chốt, hoàn cảnh, mong muốn, thay đổi công việc):
   - Ghi dưới `## <tên trong sổ>` (đã gộp ở bước 1), cuối mục, dạng `- YYYY-MM-DD · điều cần nhớ · (từ tin Zalo/Messenger/Telegram)`; ngày là ngày của tin. Một điều một dòng, ≤ 1 câu, nói rõ ai làm gì.
   - Người chưa có mục → tạo `## <tên hiển thị>` cuối file kèm dòng `- tên trên mạng · <Nền tảng>: <tên> · (máy ghi <ngày>, chờ David xác nhận)`. Tin trong nhóm → ghi cho người nói, không tạo mục cho nhóm.
   - **Chống trùng:** trước khi ghi, đọc mọi dòng của người đó. Cùng ý với dòng David tự ghi (dòng không có `(từ tin …)`) → **không ghi**, đưa vào mục "Trùng" của bản tổng hợp kèm ngày dòng cũ. Cùng ý với dòng máy đã ghi hôm trước → bỏ qua, không báo. Chỉ ghi điều mới hoặc đổi (hẹn dời, giá đổi → ghi dòng mới nói rõ "dời từ …").
   - Không ghi: lời chào, sticker, chuyện vặt, quảng cáo, cuộc trong mục "Bỏ qua" của `ghi-chu.md`, số điện thoại / số tài khoản / địa chỉ nhà / OTP / mật khẩu.
   - Chỉ thêm dòng; không sửa, không xoá dòng có sẵn.
6. Gửi bản gọn về bot: `bash tu-dong-hoa/so-tay/bao-cao.sh --chi-gui "<tin>"` (chạy ở thư mục bộ não). Tin ≤ 3.500 ký tự, chữ thường không markdown.
7. Báo cuối phiên một dòng: số cuộc đã đọc, số việc, số dòng ghi danh bạ / số trùng, gửi bot được hay lỗi.

## Khuôn file

```
# Tổng hợp tin nhắn — dd/mm/yyyy
Nguồn · mốc từ … tới … · chỉ đọc.

## 1. Việc David cần làm
| # | Người | Nền tảng | Việc | Gấp (Cao/Vừa/Thấp/Chờ) |

## 2. Quyết định / thoả thuận mới
## 3. Gia đình, đời thường
## 4. Bỏ qua được
## 5. Đã ghi danh bạ
- <Người>: <điều> (Zalo)
### Trùng với điều David đã ghi (không ghi lại)
- <Người>: <điều> — đã có dòng dd/mm
## Cảnh báo (đăng nhập hết hạn, không đọc được…)
```

Xếp "Gấp": có hạn chót gần hoặc người nhắn lại nhiều lần = Cao · đang chờ David trả lời = Vừa · David đang chờ người khác = Chờ.

## Khuôn tin Telegram

```
📬 Tin nhắn dd/mm (Zalo · Messenger · Telegram)

🔴 Cần làm
1. <Người> (<nền tảng>): <việc, ≤1 dòng>
…
⏳ Đang chờ người khác: <Người>: <việc>; …
🤝 Thoả thuận mới: …
🏠 Đời thường: …
📇 Danh bạ: ghi <n> điều cho <Người A>, <Người B>… · trùng điều anh đã ghi: <Người>: <điều> (dd/mm); …
⚠️ <cảnh báo nếu có>

Bản đủ: tin-nhan/tong-hop-YYYY-MM-DD.md
Trả lời bot: "1 xong" · "A và B là một người" · "bỏ qua X" · "thêm 2 vào việc cần làm" · "danh bạ A ghi sai: …"
```

Số thứ tự đánh liên tục trong cả tin (Cần làm 1–n, Đang chờ tiếp n+1…) để David trả lời theo số.

Không có gì mới → gửi một dòng "📬 dd/mm: không có tin mới cần xử lý."
