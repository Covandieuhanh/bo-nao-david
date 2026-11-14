---
name: tong-hop-tin-nhan
description: Tổng hợp tin nhắn hằng ngày của David từ Zalo, Messenger, Telegram — chỉ đọc, ra bảng việc cần làm / thoả thuận / đời thường, lưu ở máy (tin-nhan/, không lên GitHub) và gửi bản gọn về bot Telegram Sổ nhớ. Dùng khi lịch hằng ngày chạy, khi David nói "tổng hợp tin", "tổng hợp tin nhắn", "hôm nay ai nhắn gì", "/tong-hop-tin-nhan".
---

# Tổng hợp tin nhắn

**Mục tiêu:** mỗi sáng David biết ngay ai đang chờ mình, mình đã hứa gì, có hạn chót nào — không phải mở 3 ứng dụng.

## Luật cứng

- **Chỉ đọc.** Không gõ vào ô soạn tin, không bấm gửi, không thả cảm xúc, không gọi, không xoá, không rời nhóm.
- Không đăng nhập thay David. Trang đòi đăng nhập → ghi "⚠️ <nền tảng> cần David đăng nhập lại" vào tin gửi bot rồi làm tiếp nền tảng khác.
- Không chép số điện thoại, số tài khoản, địa chỉ nhà, mã OTP vào file hay tin Telegram.
- File chỉ ở `tin-nhan/` (đã chặn trong `.gitignore`). Không đưa nội dung tin vào bộ não, ghi nhớ hay GitHub.
- Mở cuộc trò chuyện làm tin hiện "đã xem" → chỉ mở cuộc **có hoạt động mới kể từ lần trước và có thể có việc**; còn lại đọc dòng xem trước trong danh sách là đủ.

## Nguồn và cách đọc

| Nền tảng | Trình duyệt | Trang |
|---|---|---|
| Zalo | **Claude in Chrome** (Zalo Web không chạy trong trình duyệt Claude: thiếu kho lưu trữ bảo mật, tải lại liên tục) | chat.zalo.me |
| Messenger | Trình duyệt Claude (`mcp__Claude_Browser__*`) | www.messenger.com |
| Telegram | Trình duyệt Claude | web.telegram.org/a/ |

Trình duyệt Claude: dùng tab đang mở trang đó (`tabs_context`), không có thì `preview_start` với url. Chrome: `tabs_context_mcp`, dùng tab chat.zalo.me nếu có, không có thì tạo tab mới. Chrome chưa kết nối → ghi cảnh báo, bỏ Zalo lần này.

**Zalo** — `get_page_text` ra danh sách (tên · thời gian · dòng cuối). Mở cuộc: `find` tên → `computer left_click` theo `ref` (click bằng JS không mở được) → chờ 2 giây → `get_page_text` (ra khung `<article>` của cuộc đó). Danh sách cuộn ảo, `ref` đổi sau mỗi lần mở: `find` lại, hoặc gõ tên vào ô "Tìm kiếm" rồi bấm kết quả đầu. Zalo Web không phân biệt tin của David trong chữ: đoán theo ngữ cảnh, dòng xem trước có "Bạn:" là của David.

**Messenger** — danh sách: `javascript_tool` → `[...document.querySelectorAll('[role=row]')].map(r=>r.innerText)`; đường dẫn từng cuộc: `[role=row] a[href]`. Mở cuộc: `navigate` tới `https://www.messenger.com` + href → chờ 3 giây → `get_page_text` (có sẵn "Tin nhắn do Bạn/Tên gửi lúc …").

**Telegram** — `get_page_text` ra danh sách. Mở cuộc bằng JS: `a[href="#<id>"]` → `dispatchEvent(new MouseEvent('mousedown',{bubbles:true}))` + `click()` → chờ 2,5 giây → đọc `.MessageList` (lấy ~2.000 ký tự cuối). `navigate` tới `#id` không mở được cuộc. Bỏ qua: bot của David (Trợ lý David, Sổ nhớ, BotFather, Hermes), Saved Messages, kênh sưu tầm (Tri thức huyền học, Câu chuyện hay, Học về …) trừ khi có người khác nhắn.

**Bỏ qua mọi nơi:** quảng cáo, trang tự trả lời, kênh thông báo, sticker/cuộc gọi không kèm chữ (chỉ ghi "gọi nhỡ" nếu người đó gọi ≥2 lần hoặc kèm lời trách).

## Quy trình

1. Mở bản tổng hợp gần nhất trong `tin-nhan/` (nếu có) để biết mốc lần trước và việc còn tồn.
2. Đọc danh sách 3 nền tảng, lọc cuộc có tin mới sau mốc đó (lần đầu: 24 giờ qua).
3. Mở các cuộc đã lọc, đọc phần mới.
4. Viết `tin-nhan/tong-hop-YYYY-MM-DD.md` theo khuôn dưới. Việc tồn hôm trước chưa thấy xong thì chép sang, ghi "(từ dd/mm)".
5. Gửi bản gọn về bot: `bash scripts/so-nho/bao-cao.sh --chi-gui "<tin>"` (chạy ở thư mục bộ não). Tin ≤ 3.500 ký tự, chữ thường không markdown.
6. Báo cuối phiên một dòng: số cuộc đã đọc, số việc, gửi bot được hay lỗi.

## Khuôn file

```
# Tổng hợp tin nhắn — dd/mm/yyyy
Nguồn · mốc từ … tới … · chỉ đọc.

## 1. Việc David cần làm
| # | Người | Nền tảng | Việc | Gấp (Cao/Vừa/Thấp/Chờ) |

## 2. Quyết định / thoả thuận mới
## 3. Gia đình, đời thường
## 4. Bỏ qua được
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
⚠️ <cảnh báo nếu có>

Bản đủ: tin-nhan/tong-hop-YYYY-MM-DD.md
```

Không có gì mới → gửi một dòng "📬 dd/mm: không có tin mới cần xử lý."
