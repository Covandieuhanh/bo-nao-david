# viet_lai_de_hieu.py: viết lại các slide nặng lệnh máy và số kỹ thuật thành lời thường cho người mới.
# Ghi đè đúng file slide trong ../bai-N/slides/. Giữ nguyên ảnh thật và số đo thật.
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = "Dựng video bằng AI trên máy tính"
DOTS = ('<x-shape kind="ellipse" class="dot" style="background:#E8742A"></x-shape>'
        '<x-shape kind="ellipse" class="dot" style="background:#F2C14E"></x-shape>'
        '<x-shape kind="ellipse" class="dot" style="background:#8FD3A6"></x-shape>')
def win(title, body, style=""):
    return f'<div class="win"{style}>\n<div class="bar">{DOTS}<p class="ttl">{title}</p></div>\n<div class="term">\n{body}\n</div>\n</div>'
def fact(icon, k, v, warn=False, i=0):
    return (f'<div class="fact{" warn" if warn else ""}" style="--i:{i}"><div class="ico"><x-icon name="{icon}"></x-icon></div>'
            f'<div><p class="k">{k}</p><p class="v">{v}</p></div></div>')

S = {}

S["bai-1/slides/hai-loai-ai.html"] = f'''<section id="hai-loai-ai">
<p class="eyebrow">Hiểu bộ công cụ</p>
<h2>Hai loại AI: chỉ nói, và tự làm</h2>
<div class="split even">
<div class="stack">
<p class="h3" style="font-size:30px;font-weight:700">AI trò chuyện · chỉ nói cách làm</p>
{win("app chat trên web", '''<p class="ask">Cắt chỗ im lặng trong video giúp tôi</p>
<p class="ai">Bạn mở cửa sổ lệnh, gõ lệnh này, rồi tự cắt từng đoạn…</p>
<p class="mean">bạn phải tự gõ, tự cắt</p>''')}
</div>
<div class="stack">
<p class="h3" style="font-size:30px;font-weight:700;color:#B04A12">Trợ lý AI chạy lệnh · tự làm trên máy</p>
{win("lam-video — trợ lý AI", '''<p class="ask">Cắt chỗ im lặng trong tap-thu</p>
<p class="say">Tôi đã nghe hết video: có một chỗ im lặng <b>2,2 giây</b> sau lời chào.</p>
<p class="ok">✓ Đã cắt, lưu bản mới vào 2-lam/tho.mp4</p>
<p class="mean">bạn chỉ xem kết quả</p>''')}
</div>
</div>
<p class="foot">{F} · Bài 1 · Ví dụ trợ lý chạy lệnh: Claude Code, Codex CLI, Gemini CLI</p>
<aside>Cùng một yêu cầu: AI trò chuyện trả lời cách làm, bạn phải tự làm. Trợ lý chạy lệnh tự chạy công cụ trên máy và báo kết quả bằng lời. Số 2,2 giây là số đo thật trên video thử.</aside>
</section>
'''

S["bai-1/slides/bo-cong-cu.html"] = f'''<section id="bo-cong-cu">
<p class="eyebrow">Hiểu bộ công cụ</p>
<h2>Bốn công cụ miễn phí, AI điều khiển giúp bạn</h2>
<div class="cards two">
<div class="card" style="--i:0"><div class="row"><x-icon name="Scissors" style="width:48px;height:48px;color:#B04A12"></x-icon><h3>ffmpeg · cái kéo của video</h3></div>
<p class="d">Cắt, ghép, đổi cỡ, chỉnh âm lượng. Ví dụ AI dùng nó đo được: video thử dài <b>21 giây</b>, khung ngang.</p></div>
<div class="card" style="--i:1"><div class="row"><x-icon name="Mic" style="width:48px;height:48px;color:#B04A12"></x-icon><h3>Whisper · người ghi chép</h3></div>
<p class="d">Nghe video rồi chép ra chữ, ghi cả giây. Ví dụ: giây 9 → 11: “Bước 2, cho 2 muỗng cà phê.”</p></div>
<div class="card" style="--i:2"><div class="row"><x-icon name="Palette" style="width:48px;height:48px;color:#B04A12"></x-icon><h3>Node.js + Remotion · hoạ sĩ</h3></div>
<div class="row"><div class="scr" style="width:320px;height:180px"><p class="stk" style="left:24px;top:24px;font-size:26px">Bước 1</p><p class="lbl" style="left:24px;top:92px;width:280px;font-size:24px">Tráng phin bằng nước sôi</p></div><p class="cap grow">Vẽ chữ chuyển động, thẻ số bước, khung trình bày.</p></div></div>
<div class="card" style="--i:3"><div class="row"><x-icon name="Cog" style="width:48px;height:48px;color:#B04A12"></x-icon><h3>Python · người làm việc vặt</h3></div>
<p class="d">Làm các việc nhỏ lặp lại: đổi tên file, đếm chữ, gom kết quả. Bạn không cần đụng tới.</p></div>
</div>
<p class="foot">{F} · Bài 1 · Bạn không dùng trực tiếp: AI dùng thay bạn</p>
<aside>Học viên không cần tự dùng các công cụ này. Chỉ cần biết mỗi cái làm việc gì để hiểu AI đang báo gì. Remotion miễn phí cho cá nhân và công ty từ 3 người trở xuống.</aside>
</section>
'''

S["bai-1/slides/cach-cai.html"] = f'''<section id="cach-cai">
<p class="eyebrow">Cài và kiểm tra</p>
<h2>Cách cài khuyên dùng: để AI tự cài</h2>
<div class="split">
<div class="steps">
<div class="step" style="--i:0"><p class="n">1</p><p class="s">Vào trang nodejs.org, tải bản có chữ <b>LTS</b>, bấm cài như cài phần mềm thường.</p></div>
<div class="step" style="--i:1"><p class="n">2</p><p class="s">Cài trợ lý AI theo trang chính thức của nó. Mật khẩu bạn tự gõ.</p></div>
<div class="step" style="--i:2"><p class="n">3</p><p class="s">Tạo thư mục lam-video, mở trợ lý AI trong đó (như bên phải).</p></div>
<div class="step" style="--i:3"><p class="n">4</p><p class="s">Dán câu giao việc, đọc AI giải thích, đồng ý từng bước.</p></div>
</div>
{win("Cửa sổ lệnh · bạn gõ, máy trả lời", '''<p class="cmd">$ node -v</p>
<p class="mean">hỏi máy: Node.js cài chưa? Máy đáp v24.18.0 là đã cài</p>
<p class="cmd">$ mkdir lam-video</p>
<p class="mean">tạo thư mục tên lam-video</p>
<p class="cmd">$ cd lam-video</p>
<p class="mean">đi vào thư mục đó</p>
<p class="cmd">$ claude <span style="color:#7F92A4">(hoặc codex, gemini)</span></p>
<p class="mean">gọi trợ lý AI ra làm việc</p>
<p class="ok">✓ Trợ lý AI đã sẵn sàng trong lam-video</p>''')}
</div>
<p class="foot">{F} · Bài 1 · Biểu mẫu 01 · Chỉ cần gõ đúng 4 dòng này một lần</p>
<aside>Bước 3 và 4 làm đúng như cửa sổ bên phải. Gõ tên trợ lý đang dùng: claude, codex hoặc gemini. Mật khẩu tài khoản AI học viên tự gõ.</aside>
</section>
'''

S["bai-1/slides/kiem-tra.html"] = f'''<section id="kiem-tra">
<p class="eyebrow">Cài và kiểm tra</p>
<h2>Kiểm tra cài xong, sửa lỗi hay gặp</h2>
<div class="split even">
{win("Nhờ AI kiểm giúp", '''<p class="ask">Kiểm tra giúp tôi ffmpeg và Whisper đã cài đúng chưa</p>
<p class="say">Tôi đã thử chạy cả hai.</p>
<p class="ok">✓ ffmpeg chạy được (công cụ cắt ghép)</p>
<p class="ok">✓ Whisper chạy được (công cụ chép lời)</p>
<p class="mean">thấy hai dấu ✓ là đạt, không cần làm gì thêm</p>''')}
<table class="data" style="font-size:25px">
<tr><th style="width:44%">Máy báo (tiếng Anh)</th><th style="width:56%">Nghĩa là · cách sửa</th></tr>
<tr><td>command not found</td><td>Máy chưa thấy công cụ. Đóng mở lại cửa sổ lệnh; vẫn lỗi thì dán nguyên dòng lỗi cho AI.</td></tr>
<tr><td>Whisper chạy rất lâu</td><td>Máy đang dùng bản chép lời nặng. Nhờ AI dùng bản nhẹ (small) khi thử.</td></tr>
<tr><td>No space left on device</td><td>Hết chỗ trống trong máy. Xoá file tạm, chỉ giữ bản gốc và bản cuối.</td></tr>
<tr><td>Permission denied</td><td>Máy không cho phép. Đừng tự cấp quyền: hỏi AI vì sao cần.</td></tr>
</table>
</div>
<p class="foot">{F} · Bài 1 · Biểu mẫu 01 · Gặp lỗi lạ: chép nguyên dòng lỗi, dán cho AI</p>
<aside>Có hai bản Whisper: whisper-cli (bản whisper.cpp) hoặc whisper (bản Python). Máy cài bản nào thì AI kiểm bằng lệnh đó. Gặp lỗi, không sửa thay: hướng dẫn học viên dán lỗi cho AI và đọc cách nó sửa.</aside>
</section>
'''

S["bai-3/slides/do.html"] = f'''<section id="do">
<p class="eyebrow">Việc 1 · Đo</p>
<h2>Đo tư liệu gốc trước khi làm gì khác</h2>
<div class="split even">
<div class="facts">
{fact("RectangleHorizontal", "Khung ngang", "Quay điện thoại nằm ngang, nét cao (1920x1080).", i=0)}
{fact("Film", "Rất mượt", "60 ảnh mỗi giây, như mọi điện thoại đời mới.", i=1)}
{fact("Timer", "Dài 6 phút 48 giây", "Nặng 516 MB, cỡ 100 bức ảnh chụp điện thoại.", i=2)}
{fact("Volume1", "Tiếng hơi nhỏ", "Nhỏ hơn mức chuẩn trên mạng: phải nâng ở bước âm thanh.", warn=True, i=3)}
</div>
{win("AI báo kết quả đo · bằng lời thường", '''<p class="ask">Đo giúp tôi video trong tap-thu/1-goc</p>
<p class="say">Video của bạn: <b>ngang</b>, nét, <b>60 hình/giây</b>, dài <b>6:48</b>.</p>
<p class="say">Âm lượng <b>−22,6</b>, nhỏ hơn mức chuẩn <b>−14</b>. Tôi sẽ nâng lên ở bước âm thanh.</p>
<p class="mean">số âm lượng càng gần 0 càng to; −14 là mức YouTube, TikTok dùng</p>
<p class="cmd sm">công cụ AI đã dùng: ffprobe, ffmpeg (bạn không cần gõ)</p>''')}
</div>
<p class="foot">{F} · Bài 3 · Số đo thật của tư liệu gốc</p>
<aside>Đây là số đo thật của file quay bằng máy DJI. Thành phẩm cuối được nâng lên −14,1, xem ở bài 6. Giải thích: âm lượng đo bằng số âm, gần 0 là to.</aside>
</section>
'''

S["bai-4/slides/tim-lang.html"] = f'''<section id="tim-lang">
<p class="eyebrow">Dựng thô · việc 1</p>
<h2>Tìm chỗ im lặng: AI nghe từng giây, không đoán bằng mắt</h2>
{win("AI báo chỗ im lặng · video thử 21 giây", '''<p class="say">Tôi tìm thấy <b>2 chỗ im lặng</b>:</p>
<p class="say">① Giây 4,1 → 6,3: im <b>2,2 giây</b> sau lời chào → <b>nên cắt</b>.</p>
<p class="say">② Giây 11,3 → 11,9: im <b>0,6 giây</b> giữa câu nói vấp → cắt cùng câu vấp ở việc 2.</p>''')}
<div class="tl">
<div class="track"><div class="seg blue" style="width:196px">nói</div><div class="seg cut" style="width:106px">im 2,2s</div><div class="seg blue" style="width:237px">nói</div><div class="seg cut" style="width:30px"></div><div class="seg blue" style="width:330px">nói</div><div class="seg cut" style="width:100px">im</div></div>
<div class="ruler" style="width:1023px"><p>0s</p><p>4,1</p><p>6,3</p><p>11,3</p><p>11,9</p><p>21,1s</p></div>
</div>
<p class="pt">Ô xanh là lúc có người nói, ô xám là lúc im. Bạn chỉ cần nhìn: ô xám dài là chỗ người xem dễ chán.</p>
<p class="foot">{F} · Bài 4 · Ví dụ trên video thử 21 giây</p>
<aside>AI dùng ffmpeg đo: tiếng nhỏ hơn mức −35 coi là im, im từ nửa giây trở lên mới tính. Học viên chỉ cần đọc ba con số: bắt đầu, kết thúc, kéo dài bao lâu.</aside>
</section>
'''

S["bai-4/slides/dung-tho.html"] = f'''<section id="dung-tho">
<p class="eyebrow">Dựng thô · ví dụ thật</p>
<h2>Cắt clip 61 giây từ tư liệu 6:48</h2>
<div class="split" style="grid-template-columns:1fr 340px">
<div class="stack">
<div class="tl">
<p class="name">Tư liệu gốc · 6:48 (ô cam là đoạn giữ, ô xám là đoạn bỏ)</p>
<div class="track"><div class="seg cut" style="width:260px">bỏ</div><div class="seg" style="width:78px">giữ</div><div class="seg cut" style="width:50px"></div><div class="seg" style="width:75px">giữ</div><div class="seg cut" style="width:420px">bỏ</div></div>
<div class="ruler" style="width:899px"><p>0:00</p><p>1:44</p><p>2:15</p><p>2:35</p><p>3:05</p><p>6:48</p></div>
</div>
<div class="doc" style="animation-delay:150ms"><p class="head">Kế hoạch cắt · AI viết, bạn duyệt</p><div class="bd"><p class="li" style="color:#15202B">Giữ đoạn 1:44–2:15 và 2:35–3:05, bỏ đoạn giữa vì lạc ý. Tít: “QUY CHUẨN, HỢP PHÁP” (đúng lời nói ở 1:51).</p></div></div>
{win("AI báo đã làm", '''<p class="ok">✓ Lấy đoạn 1 (phút 1:44 → 2:15)</p>
<p class="ok">✓ Lấy đoạn 2 (phút 2:35 → 3:05)</p>
<p class="ok">✓ Nối hai đoạn → clip 61 giây</p>''', ' style="animation-delay:300ms"')}
</div>
<div class="stack" style="align-items:center">
<img src="/_blob/b68320ed178c236ec09f0ca355e12382" alt="Clip dọc 61 giây sau khi cắt ghép" style="width:300px;height:533px;object-fit:cover;border-radius:24px">
<p class="cap">Kết quả: clip dọc 61 giây</p>
</div>
</div>
<p class="foot">{F} · Bài 4 · Mốc phút theo kế hoạch cắt thật</p>
<aside>Bỏ đoạn nối 2:15–2:35 vì không thuộc ý “quy chuẩn, hợp pháp”. Clip ghép hai đoạn liền ý, cắt thẳng ở chỗ nối.</aside>
</section>
'''

S["bai-6/slides/nhac.html"] = f'''<section id="nhac">
<p class="eyebrow">Nhạc và âm lượng</p>
<h2>Nhạc nhỏ hơn giọng, cả video to vừa đúng chuẩn</h2>
<div class="split even">
<div class="stack">
<p class="name" style="font-size:24px;font-weight:700;color:#4A5560">Độ to đo thật (thanh càng dài càng to)</p>
<div class="row" style="gap:16px"><p class="pt" style="width:220px">Tư liệu gốc</p><div style="width:200px;height:44px;background:#9CC3E6;border-radius:8px"></div><p class="pt">nhỏ (−22,6)</p></div>
<div class="row" style="gap:16px"><p class="pt" style="width:220px">Bản dài 7:10</p><div style="width:340px;height:44px;background:#E8742A;border-radius:8px"></div><p class="pt">chuẩn (−14,1)</p></div>
<div class="row" style="gap:16px"><p class="pt" style="width:220px">Clip dọc 61 giây</p><div style="width:344px;height:44px;background:#E8742A;border-radius:8px"></div><p class="pt">chuẩn (−13,9)</p></div>
<p class="cap">Như nhạc quán cà phê: nghe rõ khi người nói ngừng, nhỏ lại khi người nói.</p>
</div>
{win("AI báo sau khi chỉnh tiếng", '''<p class="say">Tiếng gốc <b>nhỏ</b> (−22,6). Tôi đã nâng lên.</p>
<p class="say">Bản cuối to <b>−14,1</b>: đúng mức YouTube, TikTok dùng.</p>
<p class="say">Nhạc nền đặt thấp dưới giọng nói.</p>
<p class="ok">✓ Đạt chuẩn, tiếng không bị rè, không bị vỡ</p>
<p class="mean">đọc một con số: gần −14 là đạt</p>''')}
</div>
<p class="foot">{F} · Bài 6 · Đơn vị đo độ to gọi là LUFS; −14 là mức chung của YouTube, Spotify</p>
<aside>Số đo thật: gốc nhỏ −22,6, bản dài sau dựng −14,1, clip −13,9. Luôn yêu cầu AI đo lại bản cuối và báo con số. Giải thích bằng chuyện đổi kênh TV: kênh to kênh nhỏ thì khó chịu.</aside>
</section>
'''

S["bai-7/slides/lenh-xuat.html"] = f'''<section id="lenh-xuat">
<p class="eyebrow">AI xuất file thế nào</p>
<h2>Đọc báo cáo xuất file của AI trong một phút</h2>
<div class="split even">
<div class="facts">
{fact("RectangleVertical", "Bản dọc", "AI cắt một khung đứng quanh người nói, rồi phóng to cho vừa màn hình điện thoại.", i=0)}
{fact("Square", "Bản vuông", "AI cắt một ô vuông quanh người nói.", i=1)}
{fact("ImagePlay", "Ảnh bìa", "AI chụp một khung hình rõ mặt nhất trong video (ở giây 5,9).", i=2)}
</div>
{win("AI báo đã xuất", '''<p class="ok">✓ ban-doc.mp4 · khung đứng, người ở giữa</p>
<p class="ok">✓ ban-vuong.mp4 · ô vuông quanh người</p>
<p class="ok">✓ anh-bia.jpg · khung hình ở giây 5,9</p>
<p class="mean">mở bản dọc xem thử: người có nằm giữa khung không? Lệch thì nói AI</p>
<p class="cmd sm">trong lệnh AI chạy: crop = cắt khung · scale = đổi cỡ · -ss = giây lấy ảnh</p>''')}
</div>
<p class="foot">{F} · Bài 7 · Bạn không cần gõ lệnh, chỉ cần kiểm kết quả bằng mắt</p>
<aside>Giải thích một lần để học viên đọc được báo cáo của AI và phát hiện khi AI cắt sai vị trí (ví dụ khung đứng lệch làm mất người).</aside>
</section>
'''

for p, h in S.items():
    open(os.path.join(ROOT, p), "w").write(h)
    print("viết lại", p)
