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
| Messenger | **Claude in Chrome** (David đăng nhập trong Chrome 14/11) | www.messenger.com |
| Telegram | **Claude in Chrome** | web.telegram.org/a/ |

Cả ba qua Claude in Chrome (lịch mở phiên bằng `claude --chrome`, không cần trình duyệt riêng của app): `tabs_context_mcp`, dùng tab của trang đó nếu có, không có thì tạo tab mới. Zalo báo "đang mở ở tab khác" → bấm đúng nút "Kích hoạt" (không phải gửi tin). Chrome chưa kết nối → chờ 60 giây gọi lại `tabs_context_mcp`, tối đa 5 lần; vẫn chưa thì ghi cảnh báo và dòng `CHUA-DOC-DUOC`. Máy canh bot đã chờ Chrome nối trước khi mở phiên lịch, và tự chạy lại khi bản đủ còn dòng đó. Cuối việc đóng các tab mình mở.

**Zalo** — `get_page_text` ra danh sách (tên · thời gian · dòng cuối). Mở cuộc: chụp màn hình nhỏ (`scale 0.5`) rồi `computer left_click` theo **toạ độ** dòng trong danh sách (bấm theo `ref` của `find` có lúc trúng chữ, không mở cuộc; cuộn danh sách bằng `scroll` khi cần) → đọc bằng `javascript_tool`:
`await new Promise(r=>setTimeout(r,2000)); (document.querySelector('article')?.innerText||'NO').replace(/\/-strong\n\/-heart\n:>\n:o\n:-\(\(\n:-h\n/g,'').slice(-1500)` (bỏ hàng nút cảm xúc; kết quả dài bị cắt thì giảm số). Cuộc dài: tìm `lastIndexOf('Hôm qua')` rồi cắt từ đó. Trong khung có trích dẫn, tên đứng trên khối trích là **người bị trích**, lời ngay dưới là của người kia. Zalo Web không phân biệt tin của David trong chữ: đoán theo ngữ cảnh, dòng xem trước có "Bạn:" là của David.

**Messenger** — danh sách: `javascript_tool` → `[...document.querySelectorAll('[role=row]')].map(r=>r.innerText)`; đường dẫn từng cuộc: `[role=row] a[href]`. Mở cuộc: `navigate` tới `https://www.messenger.com` + href → chờ 3 giây → `get_page_text` (có sẵn "Tin nhắn do Bạn/Tên gửi lúc …").

**Telegram** — `get_page_text` ra danh sách; mã từng cuộc: `[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')+' '+a.innerText.split('\n')[0])`. Cuộc mở ra đứng ở chỗ đọc lần trước, danh sách tin cuộn ảo (chỉ ~20 tin trong trang): dùng **một** lệnh JS mở cuộc, cuộn xuống cuối tới khi có nhãn "Today", rồi cuộn ngược gom tin theo ngày tới khi gặp ngày trước mốc:
```js
const id='<mã>'; const a=document.querySelector(`a[href="#${id}"]`); a.dispatchEvent(new MouseEvent('mousedown',{bubbles:true})); a.click(); await new Promise(r=>setTimeout(r,2500));
const L=document.querySelector('.MessageList'); for(let i=0;i<20;i++){L.scrollTop=L.scrollHeight; await new Promise(r=>setTimeout(r,700)); if([...document.querySelectorAll('.MessageList .sticky-date')].some(d=>d.innerText==='Today')) break;}
const seen=new Map(); for(let i=0;i<15;i++){ document.querySelectorAll('.MessageList .message-date-group').forEach(g=>{const d=g.querySelector('.sticky-date')?.innerText; let who='?'; g.querySelectorAll('.Message').forEach(m=>{const n=m.querySelector('.message-title-name, .sender-title')?.innerText; if(n) who=n; const k=m.getAttribute('data-message-id')||m.id; if(!seen.has(k)) seen.set(k,{d,who:m.classList.contains('own')?'David':who,t:(m.querySelector('.text-content')?.innerText||'[ảnh]').replace(/\n/g,' ').slice(0,200)});});}); if([...seen.values()].some(v=>v.d==='<ngày trước mốc, vd Sunday>')) break; L.scrollTop=Math.max(0,L.scrollTop-500); await new Promise(r=>setTimeout(r,900)); }
[...seen.entries()].sort((x,y)=>parseInt(x[0].replace(/\D/g,''))-parseInt(y[0].replace(/\D/g,''))).filter(([k,v])=>v.d==='Yesterday'||v.d==='Today').map(([k,v])=>v.d[0]+' '+v.who+': '+v.t).join('\n')
```
Kết quả bị cắt thì in theo từng đoạn (`.slice(20)`…). `navigate` tới `#id` không mở được cuộc. Bỏ qua: bot của David (Trợ lý David, Sổ nhớ, BotFather, Hermes), Saved Messages, kênh sưu tầm (Tri thức huyền học, Câu chuyện hay, Học về …) trừ khi có người khác nhắn.

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
CHUA-DOC-DUOC: <nền tảng>   ← chỉ khi có nền tảng không đọc được; máy canh bot thấy dòng này thì tự chạy lại một lần
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
