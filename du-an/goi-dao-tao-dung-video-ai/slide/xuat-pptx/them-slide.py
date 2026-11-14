# them-slide.py: thêm slide cho người mới (so sánh đời thường, từ mới, mở cửa sổ lệnh) vào 8 bài.
# Chạy lại được nhiều lần: ghi đè file slide, chỉ chèn id vào bo-slide.json nếu chưa có.
import json, os, html
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FOOT = "Dựng video bằng AI trên máy tính"

def esc(s):
    # cho phép <b>…</b> trong chữ
    return html.escape(s).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")

def ico(name, cls="ico"):
    return f'<div class="{cls}"><x-icon name="{name}"></x-icon></div>'

def ana_slide(n, title, rows, note):
    cells = ['<p class="hd">Trong đời thường</p><p></p><p class="hd">Khi dựng video bằng AI</p>']
    for i, (li, lt, mi, mt) in enumerate(rows):
        cells.append(f'<div class="c" style="--i:{i}">{ico(li)}<p>{esc(lt)}</p></div>'
                     f'<x-icon name="ArrowRight" class="to"></x-icon>'
                     f'<div class="c m" style="--i:{i}">{ico(mi)}<p>{esc(mt)}</p></div>')
    return f'''<section id="hieu-de">
<p class="eyebrow">Hiểu bằng chuyện đời thường</p>
<h2>{esc(title)}</h2>
<div class="ana">
{chr(10).join(cells)}
</div>
<p class="foot">{FOOT} · Bài {n}</p>
<aside>{esc(note)}</aside>
</section>
'''

def gloss_slide(n, items, note):
    gs = "\n".join(f'<div class="g" style="--i:{i}">{ico(ic)}<div><p class="k">{esc(k)}</p><p class="v">{esc(v)}</p></div></div>'
                   for i, (ic, k, v) in enumerate(items))
    return f'''<section id="tu-moi">
<p class="eyebrow">Từ mới của bài {n}</p>
<h2>Gặp những từ này, hiểu đơn giản là</h2>
<div class="gloss">
{gs}
</div>
<p class="foot">{FOOT} · Bài {n} · Không cần thuộc, AI lo phần kỹ thuật</p>
<aside>{esc(note)}</aside>
</section>
'''

MO_LENH = f'''<section id="mo-cua-so-lenh">
<p class="eyebrow">Cài và kiểm tra · bước 0</p>
<h2>Mở cửa sổ lệnh: nơi trợ lý AI làm việc</h2>
<div class="howto">
<div class="os" style="--i:0">
<h3><x-icon name="Laptop"></x-icon>Máy Mac: mở Terminal</h3>
<div class="st"><span class="n">1</span>Nhấn <span class="key">⌘</span> + <span class="key">Phím cách</span> cùng lúc</div>
<div class="st"><span class="n">2</span>Gõ chữ <span class="key">Terminal</span></div>
<div class="st"><span class="n">3</span>Nhấn <span class="key">Enter ↵</span></div>
</div>
<div class="os" style="--i:1">
<h3><x-icon name="Monitor"></x-icon>Máy Windows: mở PowerShell</h3>
<div class="st"><span class="n">1</span>Nhấn phím <span class="key">⊞ Windows</span></div>
<div class="st"><span class="n">2</span>Gõ chữ <span class="key">PowerShell</span></div>
<div class="st"><span class="n">3</span>Nhấn <span class="key">Enter ↵</span></div>
</div>
</div>
<div class="win" style="max-width:1664px">
<div class="bar"><x-shape kind="ellipse" class="dot" style="background:#E8742A"></x-shape><x-shape kind="ellipse" class="dot" style="background:#F2C14E"></x-shape><x-shape kind="ellipse" class="dot" style="background:#8FD3A6"></x-shape><p class="ttl">Cửa sổ hiện ra trông như thế này</p></div>
<div class="term">
<p class="cmd">may-cua-ban ~ % <span style="color:#F7F5F0">▍</span></p>
<p class="dim">← con trỏ nhấp nháy: máy đang chờ bạn gõ. Chữ trước dấu % (hay &gt; trên Windows) là tên máy, mỗi máy một khác.</p>
</div>
</div>
<p class="foot">{FOOT} · Bài 1 · Cửa sổ lệnh chỉ là chỗ gõ chữ, gõ sai không hỏng máy</p>
<aside>Cho học viên tự mở ngay trong buổi, trainer nhìn màn hình chung. Người mới thường sợ cửa sổ đen: nói rõ chỉ cần biết mở nó, việc gõ lệnh để trợ lý AI làm.</aside>
</section>
'''

D = {
1: dict(after="muc-tieu",
  title="Trợ lý AI giống người thợ phụ ngồi ngay tại máy bạn",
  rows=[("Phone", "Gọi điện hỏi thợ: thợ <b>chỉ cách</b>, bạn tự làm", "MessageCircle", "AI trò chuyện trên web: <b>chỉ nói</b> cách làm"),
        ("House", "Thợ <b>đến tận nhà</b>, tự cầm đồ nghề làm", "Bot", "Trợ lý AI chạy lệnh: <b>tự làm</b> trên máy, xin phép trước"),
        ("Wrench", "Hộp đồ nghề: kéo, băng dính, sổ ghi", "Scissors", "Bộ công cụ miễn phí: <b>ffmpeg</b> cắt ghép, <b>Whisper</b> chép lời"),
        ("DoorOpen", "Cửa ra vào để thợ vào nhà", "SquareTerminal", "<b>Cửa sổ lệnh</b>: nơi trợ lý AI vào làm việc")],
  note="Nói chậm từng dòng, trái trước phải sau. Hỏi học viên: bạn đã dùng loại AI nào? Phần lớn mới dùng AI trò chuyện, bài này đổi sang loại tự làm.",
  gloss=[("SquareTerminal", "Cửa sổ lệnh (Terminal / PowerShell)", "Ô cửa sổ để gõ chữ ra lệnh cho máy. Bạn chỉ cần mở nó."),
         ("Keyboard", "Lệnh", "Một dòng chữ bảo máy làm một việc. AI tự gõ, bạn chỉ đọc rồi đồng ý."),
         ("Bot", "Trợ lý AI chạy lệnh", "Claude Code, Codex hoặc Gemini CLI. Nghe bạn nói, tự làm, báo kết quả."),
         ("Scissors", "ffmpeg", "Công cụ cắt, ghép, đổi cỡ video và âm thanh. Miễn phí."),
         ("Mic", "Whisper", "Công cụ nghe video rồi chép ra chữ. Miễn phí, chạy trên máy bạn."),
         ("FileText", "File .srt", "File chữ ghi từng câu nói kèm giây bắt đầu và giây kết thúc.")],
  gnote="Không bắt học viên nhớ tên công cụ. Chỉ cần biết: thấy chữ ffmpeg là AI đang cắt ghép, thấy Whisper là AI đang chép lời."),
2: dict(after="muc-tieu",
  title="SOP giống công thức nấu ăn dán trên tủ lạnh",
  rows=[("BookOpen", "Công thức nấu ăn: ai đọc cũng nấu ra <b>cùng một vị</b>", "FileText", "<b>SOP</b>: AI đọc mỗi lần, dựng ra <b>cùng một phong cách</b>"),
        ("Archive", "Ba ngăn bếp: đồ sống · đang sơ chế · món đã bày", "FolderOpen", "Ba ngăn thư mục: <b>1-goc</b> · <b>2-lam</b> · <b>3-xuat</b>"),
        ("Utensils", "Gọi món: “cho tôi bát phở tái, ít hành”", "MessageSquareText", "<b>Câu giao việc</b>: “Dựng tap-thu, dọc, 30 giây”"),
        ("PencilLine", "Khách chê mặn → đầu bếp <b>sửa luôn công thức</b>", "RefreshCw", "<b>Phản hồi</b> → AI sửa video và sửa một câu trong SOP")],
  note="Hình ảnh công thức nấu ăn giúp học viên hiểu vì sao phải viết SOP: không có công thức thì mỗi lần nấu một vị.",
  gloss=[("FileText", "SOP (quy trình vận hành chuẩn)", "Sổ tay cách làm. AI đọc nó trước mỗi lần dựng."),
         ("FileCode", "AGENTS.md · CLAUDE.md · GEMINI.md", "Tên file sổ tay. Mỗi trợ lý AI tự tìm đọc đúng tên của nó."),
         ("FolderOpen", "Thư mục tập", "Một video, một thư mục riêng, trong có ba ngăn."),
         ("MessageSquareText", "Câu giao việc", "Một câu nói rõ: tư liệu nào, ra gì, khung nào, dài bao nhiêu."),
         ("RefreshCw", "Phản hồi", "Bạn xem rồi nói chỗ chưa ưng. AI sửa và ghi nhớ vào SOP."),
         ("Type", "Tên không dấu", "Viết tap-khai-truong thay cho “Tập khai trương”: máy đọc không lỗi.")],
  gnote="Nhấn mạnh: SOP viết bằng tiếng Việt bình thường, không phải lập trình."),
3: dict(after="muc-tieu",
  title="AI không có mắt: nó hiểu video như người đọc hồ sơ",
  rows=[("Ruler", "Cân, đo nguyên liệu trước khi nấu", "Gauge", "<b>Đo</b>: dài bao lâu, ngang hay dọc, nét không, to hay nhỏ"),
        ("NotebookPen", "Thư ký ghi biên bản cuộc họp", "Mic", "<b>Nghe</b>: Whisper chép lời, ghi giây của từng câu"),
        ("Images", "Lật album ảnh để biết chuyện gì xảy ra", "Camera", "<b>Xem</b>: chụp vài khung hình rải đều rồi mô tả"),
        ("Search", "Đọc lại biên bản, sửa chữ ghi nhầm", "SpellCheck", "<b>Soát lời chép</b>: sửa tên riêng, từ chuyên ngành")],
  note="Giải thích vì sao cần bước này: AI chỉ đọc được chữ và số. Ba việc đo, nghe, xem biến video thành chữ và số để AI hiểu.",
  gloss=[("Video", "Tư liệu", "Video hay ghi âm gốc bạn quay, chưa sửa gì."),
         ("Monitor", "1920x1080", "Độ nét: số điểm ảnh ngang × dọc. Số càng lớn càng nét."),
         ("Film", "Hình/giây", "Mỗi giây có bao nhiêu ảnh. 30 hay 60 là mượt."),
         ("Volume2", "LUFS", "Đơn vị đo độ to. Video trên mạng xã hội to khoảng −14."),
         ("Image", "Khung hình", "Một ảnh chụp ra từ video, như bấm dừng rồi chụp màn hình."),
         ("FileText", "Lời chép", "Toàn bộ chữ người nói trong video, có giờ phút giây.")],
  gnote="Các con số chỉ để hiểu AI đang báo gì. Học viên không cần tự đo."),
4: dict(after="muc-tieu",
  title="Dựng thô giống nhặt rau: bỏ phần héo, giữ phần ngon",
  rows=[("ClipboardList", "Lên thực đơn trước khi nấu", "ListOrdered", "<b>Kế hoạch sản xuất</b>: giữ đoạn nào, theo thứ tự nào"),
        ("Leaf", "Nhặt bỏ lá héo, cọng già", "Scissors", "<b>Cắt</b> khoảng lặng dài và câu nói vấp"),
        ("Droplets", "Rửa sạch rau", "Sparkles", "<b>Làm sạch</b>: xoay đúng chiều, chỉnh sáng, giảm ồn"),
        ("CookingPot", "Xếp món ra đĩa liền mạch", "Film", "<b>Ghép cảnh</b>: nối các đoạn, cắt thẳng là mặc định")],
  note="Nhấn mạnh thứ tự: duyệt kế hoạch trước, AI mới được cắt. Người duyệt chỉ cần đọc cột phải và nói đồng ý hay đổi.",
  gloss=[("Film", "Dựng thô", "Bản ghép đầu tiên: đã cắt gọn, chưa có chữ, chưa có nhạc."),
         ("Pause", "Khoảng lặng", "Đoạn không ai nói. Dài quá thì người xem chán."),
         ("MessageSquareX", "Câu nói vấp", "Nói hỏng rồi nói lại. Giữ câu nói đủ, bỏ câu hỏng."),
         ("Slice", "Cắt thẳng", "Cảnh này hết là cảnh sau hiện ngay, không hiệu ứng."),
         ("Blend", "Mờ dần", "Cảnh cũ mờ đi, cảnh mới hiện lên. Dùng khi đổi chủ đề."),
         ("ListOrdered", "Kế hoạch sản xuất", "Bảng giây nào giữ, giây nào bỏ. AI viết, bạn duyệt.")],
  gnote="Cho học viên xem bản dựng thô trước và sau để thấy khác biệt, không cần giải thích lệnh."),
5: dict(after="muc-tieu",
  title="Phụ đề giống dòng chữ karaoke",
  rows=[("MicVocal", "Chữ karaoke hiện theo lời hát, từng đoạn ngắn", "Captions", "<b>Phụ đề</b>: chữ chạy theo lời nói, mỗi lần 5–8 chữ"),
        ("Highlighter", "Bút dạ quang tô câu quan trọng trong sách", "Sparkle", "<b>Chữ nhấn</b>: vài chữ lớn ở chỗ quan trọng nhất"),
        ("Frame", "Dán nhãn lên ảnh nhưng không đè lên mặt người", "ShieldCheck", "<b>Vùng an toàn</b>: chữ không che mặt, không bị nút app che"),
        ("FileCheck", "Sửa bản gốc thì mọi bản in đều đúng", "PencilLine", "<b>Sửa lời chép</b> một chỗ, mọi chữ trên video đúng theo")],
  note="Mở điện thoại một video TikTok bất kỳ cho học viên xem chỗ nút thích, bình luận che chữ: đó là lý do có vùng an toàn.",
  gloss=[("Captions", "Phụ đề", "Chữ chạy theo lời nói ở dưới hay giữa màn hình."),
         ("Rows3", "Cụm", "Một nhóm 5–8 chữ hiện cùng lúc. Ngắn để kịp đọc."),
         ("Sparkle", "Chữ nhấn", "Vài chữ thật lớn, lấy đúng lời người nói, ở chỗ quan trọng."),
         ("ShieldCheck", "Vùng an toàn", "Phần màn hình không bị tên kênh, nút bấm của app che."),
         ("Contrast", "Tương phản", "Chữ sáng trên nền tối hoặc ngược lại, nhìn là đọc được."),
         ("Quote", "Nguyên văn", "Đúng từng chữ người nói. AI không tự thêm lời.")],
  gnote="Cho học viên đọc to một cụm phụ đề: đọc kịp trong 2 giây là đạt."),
6: dict(after="muc-tieu",
  title="Đồ hoạ giống tranh minh hoạ trong sách thiếu nhi",
  rows=[("BookImage", "Sách có tranh đúng trang đang kể", "Image", "<b>Hình minh hoạ</b> hiện đúng lúc người nói nhắc tới"),
        ("Coffee", "Nhạc quán cà phê: có nhưng không át tiếng nói chuyện", "Music", "<b>Nhạc nền</b> thấp dưới giọng nói"),
        ("Radio", "Mọi bài trên đài phát thanh to bằng nhau", "Gauge", "<b>Chuẩn âm lượng</b>: video không to hơn, không nhỏ hơn video khác"),
        ("Handshake", "Mượn đồ phải xin phép, ghi tên người cho mượn", "BadgeCheck", "<b>Bản quyền</b>: chỉ dùng ảnh, nhạc được phép, ghi nguồn")],
  note="Luật vàng của bài: ít mà đúng lúc. Hỏi học viên nhớ video nào nhiều hiệu ứng quá làm rối mắt.",
  gloss=[("Shapes", "Đồ hoạ (motion graphics)", "Chữ, hình, biểu tượng chuyển động trên video."),
         ("Smile", "Biểu tượng", "Hình vẽ đơn giản như cái chuông, ngôi nhà. Không lo bản quyền."),
         ("Camera", "Ảnh thật", "Ảnh chụp nơi chốn, đồ vật thật. Phải có giấy phép dùng."),
         ("ChartNoAxesColumn", "Khung trình bày", "Bảng, dòng thời gian, so sánh số. AI vẽ bằng code."),
         ("Copyright", "Bản quyền · giấy phép CC", "Quyền dùng ảnh, nhạc. CC là loại giấy phép cho dùng miễn phí kèm ghi nguồn."),
         ("Volume2", "−14 LUFS", "Mức to chung của YouTube, TikTok. AI tự chỉnh về mức này.")],
  gnote="Giải thích LUFS bằng chuyện đổi kênh TV: kênh này to, kênh kia nhỏ thì khó chịu. Chuẩn chung giúp video không bị vậy."),
7: dict(after="muc-tieu",
  title="Xuất nhiều khung giống may áo nhiều cỡ từ một tấm vải",
  rows=[("Shirt", "Một tấm vải, may ba cỡ áo", "MonitorSmartphone", "Một bản dựng, xuất <b>ba khung</b>: ngang, dọc, vuông"),
        ("Ruler", "Thợ may đo theo người mặc, không cắt bừa", "ScanFace", "<b>Bản dọc</b> bám theo người nói, không cắt chính giữa"),
        ("BookOpenText", "Trích một chương hay để đọc thử", "Clapperboard", "<b>Clip ngắn</b>: một ý trọn, người lạ xem vẫn hiểu"),
        ("Book", "Bìa sách: nhìn là biết sách nói gì", "ImagePlay", "<b>Ảnh bìa</b>: khung hình rõ mặt, tối đa 5 chữ")],
  note="Cầm điện thoại dọc và ngang cho học viên thấy: cùng video nhưng mỗi nơi đăng cần một cỡ khung khác.",
  gloss=[("RectangleHorizontal", "Ngang 16:9", "Khung nằm ngang. Đăng YouTube, website."),
         ("RectangleVertical", "Dọc 9:16", "Khung đứng như màn hình điện thoại. Đăng TikTok, Reels, Shorts."),
         ("Square", "Vuông 1:1", "Khung vuông. Đăng bài Facebook."),
         ("Crop", "Cắt khung (crop)", "Cắt bớt hai bên để đổi ngang thành dọc."),
         ("Clapperboard", "Clip ngắn", "Đoạn 30–90 giây trích từ video dài."),
         ("ImagePlay", "Ảnh bìa (thumbnail)", "Ảnh hiện trước khi người xem bấm vào video.")],
  gnote="Ba khung là đủ cho mọi nơi đăng. Không cần nhớ số, chỉ cần nói ngang, dọc hay vuông."),
8: dict(after="muc-tieu",
  title="Giống dạy người học việc: nhắc một lần, ghi vào sổ",
  rows=[("GraduationCap", "Lần đầu dạy kỹ từng bước", "ListChecks", "<b>8 bước</b> đã nằm sẵn trong SOP"),
        ("MessageCircle", "Lần sau chỉ cần dặn một câu", "Bot", "<b>Một câu giao việc</b>, AI chạy trọn 8 bước"),
        ("NotebookPen", "Sai chỗ nào ghi vào sổ, lần sau khỏi nhắc", "RefreshCw", "<b>Phản hồi</b> → sửa một câu SOP, video sau tự đúng"),
        ("Brush", "Nấu xong thì dọn bếp", "HardDrive", "<b>Dọn máy</b>: xoá file tạm, giữ gốc và bản cuối")],
  note="Bài cuối: cho học viên thấy họ đã có người học việc riêng. Càng phản hồi, người học việc càng giỏi.",
  gloss=[("Workflow", "Chạy một mạch", "AI tự làm hết 8 bước, không dừng hỏi từng bước."),
         ("ClipboardList", "Báo cáo bàn giao", "AI báo: file ở đâu, đã chọn gì, chỗ nào cần bạn xác nhận."),
         ("ListChecks", "Danh sách kiểm soát chất lượng", "Bảng việc cần kiểm trước khi dùng video."),
         ("FileX", "File tạm", "File AI tạo ra giữa chừng. Xong video thì xoá được."),
         ("HardDrive", "GB · MB", "Đơn vị đo file nặng bao nhiêu. 1 GB = 1.000 MB."),
         ("BadgeCheck", "Nghiệm thu", "Buổi bạn tự dựng một video, trainer chỉ ngồi xem.")],
  gnote="Ôn lại từ mới của cả khoá trong 5 phút trước khi nghiệm thu."),
}

for n, d in D.items():
    sd = os.path.join(ROOT, f"bai-{n}", "trang-trinh-chieu")
    files = {"hieu-de": ana_slide(n, d["title"], d["rows"], d["note"]),
             "tu-moi": gloss_slide(n, d["gloss"], d["gnote"])}
    if n == 1: files["mo-cua-so-lenh"] = MO_LENH
    for k, v in files.items():
        open(os.path.join(sd, k + ".html"), "w").write(v)
    dj = os.path.join(ROOT, f"bai-{n}", "bo-slide.json"); deck = json.load(open(dj))
    o = deck["order"]
    for k in ("tu-moi", "hieu-de"):  # chèn ngược để ra thứ tự: mục tiêu → hiểu dễ → từ mới
        if k not in o: o.insert(o.index(d["after"]) + 1, k)
    if n == 1 and "mo-cua-so-lenh" not in o: o.insert(o.index("cach-cai"), "mo-cua-so-lenh")
    json.dump(deck, open(dj, "w"), ensure_ascii=False, separators=(",", ":"))
    print(n, o)
