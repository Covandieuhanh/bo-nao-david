import sys
from deck_lib import *

OUT = sys.argv[1]

# ---------------- Bài 0 · Tổng quan gói ----------------
d = Deck("Bài 0 · Tổng quan gói")
s = d.slide("dark")
eyebrow(s, "Dựng video bằng AI trên máy tính · Tổng quan gói", 2.2)
tx(s, 0.9, 2.7, 11, 1.6, "Từ tư liệu thô đến video hoàn chỉnh", 54, C["paper"], True, HEAD, spacing=1.0)
tx(s, 0.9, 4.75, 10.5, 1.2, "Bạn đưa tư liệu, nói muốn gì, xem và phản hồi. Trợ lý AI trên máy bạn dựng phần còn lại.", 22)
tx(s, 0.9, 6.3, 11, 0.4, "Quy trình · Lộ trình 4 buổi · Phiếu khảo sát và nghiệm thu", 14, C["lgrey"])

s = d.slide("accent")
eyebrow(s, "Cam kết của gói")
tx(s, 0.9, 1.7, 11.5, 2.4, "Bạn tự dựng 1 video bất kì bằng AI trên máy mình, không cần trainer, và đã dựng xong ≥ 4 video.", 40, C["ink"], True, HEAD, spacing=1.1)
card(s, 0.9, 4.6, 5.6, 1.6, "Ra được", "Cắt ghép, phụ đề, chữ, đồ hoạ, nhạc, âm lượng chuẩn, đủ khung cần đăng, clip ngắn, ảnh bìa.", hl=True)
card(s, 6.8, 4.6, 5.6, 1.6, "Chưa đạt thì sao", "Trainer kèm tiếp tới khi đạt cả hai điều kiện.", hl=True)
foot(s, "Tổng quan")

s = d.slide()
eyebrow(s, "Kế hoạch · bộ công cụ"); title(s, "Năm thứ AI dùng để dựng, bốn thứ miễn phí")
items = [("Trợ lý AI chạy lệnh", "Đọc SOP, chạy các công cụ dưới, tự kiểm kết quả. Claude Code, Codex CLI, Gemini CLI: chọn cái đang có."),
         ("ffmpeg", "Cắt, ghép, xoay, đổi khung, gắn phụ đề, lọc tiếng, chuẩn âm lượng, xuất file."),
         ("Whisper", "Chép lời có mốc thời gian để AI “nghe” được video."),
         ("Remotion", "Khi cần đồ hoạ: chữ chuyển động, hình minh hoạ, khung trình bày bằng code."),
         ("SOP", "Quy trình vận hành chuẩn: phong cách, luật, cách làm. AI đọc mỗi lần, sửa dần cho đúng ý.")]
for i, (t, dd) in enumerate(items[:3]): card(s, 0.9 + i * 3.9, 2.25, 3.65, 2.0, t, dd, hl=(i == 0))
for i, (t, dd) in enumerate(items[3:]): card(s, 0.9 + i * 3.9, 4.5, 3.65, 2.0, t, dd, hl=(i == 1))
foot(s, "Quy trình")

for part, rows in [("1–4", [["#", "Bước", "AI làm", "Đạt khi"],
        ["1", "Nạp tư liệu", "Xếp file vào thư mục tập, đo độ dài, khung, chất lượng", "Biết có gì trong tay"],
        ["2", "Hiểu tư liệu", "Chép lời, chụp khung hình rải đều để “xem” cảnh", "Có lời chép + danh sách cảnh"],
        ["3", "Kế hoạch sản xuất", "Dòng thời gian: đoạn giữ, thứ tự cảnh, chỗ chữ, hình, nhạc", "Duyệt được trong 2 phút"],
        ["4", "Dựng thô", "Cắt, ghép theo kế hoạch; bỏ lặng, câu hỏng", "Mạch xem trơn"]]),
        ("5–8", [["#", "Bước", "AI làm", "Đạt khi"],
        ["5", "Làm sạch", "Xoay, cắt khung, chỉnh sáng màu nhẹ, giảm ồn", "Hình rõ, tiếng rõ"],
        ["6", "Phụ đề, chữ, đồ hoạ", "Phụ đề 5–8 chữ mỗi lần; chữ nhấn, hình không che chủ thể", "Đọc kịp, không rối"],
        ["7", "Nhạc, âm thanh", "Nhạc thấp dưới giọng, tiếng nhẹ, chuẩn âm khoảng −14 LUFS", "Nghe dễ chịu, đều tiếng"],
        ["8", "Xuất + tự kiểm", "Ngang, dọc, vuông, clip ngắn, ảnh bìa; chụp khung kiểm lỗi", "Đúng khung, không lỗi"]])]:
    s = d.slide()
    eyebrow(s, f"Quy trình · bước {part}"); title(s, "8 bước dựng một video")
    table(s, 0.9, 2.2, 11.5, rows, [0.5, 2.4, 5.6, 3.0], size=15, rowh=0.8)
    foot(s, "Quy trình")

s = d.slide("dark")
eyebrow(s, "Phản hồi và luật dựng"); title(s, "Mỗi phản hồi sửa video và sửa một câu trong SOP")
tx(s, 0.9, 2.2, 11.5, 0.9, "Phản hồi ở bất kì bước nào → AI sửa video, rồi sửa đúng một câu trong SOP để lần sau tự đúng.", 20)
card(s, 0.9, 3.6, 3.65, 2.4, "Lời thật", "Chữ trên video lấy đúng lời trong video. AI không bịa lời.")
card(s, 4.8, 3.6, 3.65, 2.4, "Dễ hiểu hơn cầu kì", "Mỗi video ít kiểu hiệu ứng.")
card(s, 8.7, 3.6, 3.65, 2.4, "An toàn", "Không sửa, không xoá file gốc. AI hỏi trước khi xoá hay tốn tiền. Không đưa mật khẩu cho AI.")
foot(s, "Quy trình")

s = d.slide()
eyebrow(s, "Đòi hỏi máy"); title(s, "Kiểm máy trước khi nhận học viên")
for i, (t, dd) in enumerate([("Hệ điều hành", "Mac hoặc Windows"), ("RAM", "≥ 16 GB"), ("Ổ trống", "≥ 50 GB"), ("AI", "Tài khoản có trợ lý chạy lệnh")]):
    box(s, 0.9 + i * 2.92, 2.3, 2.7, 2.1, C["card"], C["line"])
    tx(s, 1.1 + i * 2.92, 2.5, 2.3, 0.4, t.upper(), 13, C["rust"], True, HEAD)
    tx(s, 1.1 + i * 2.92, 3.0, 2.3, 1.3, dd, 26 if len(dd) < 12 else 18, C["ink"], True, HEAD)
tx(s, 0.9, 4.9, 11.5, 1.2, "Remotion miễn phí cho cá nhân và công ty ≤ 3 người, lớn hơn cần giấy phép (kiểm lại điều khoản lúc dạy). Máy không đủ thì nói thẳng, không nhận.", 17)
foot(s, "Quy trình")

s = d.slide()
eyebrow(s, "Lộ trình"); title(s, "4 buổi 1:1 online, 90 phút, khoảng 4 tuần")
table(s, 0.9, 2.2, 11.5, [["Buổi", "Bài", "Kết quả"],
    ["1", "1, 2", "Máy cài xong, AI dựng được video thử 30 giây"],
    ["2", "3, 4", "Video đầu tiên của học viên: dựng thô, sạch hình tiếng"],
    ["3", "5, 6", "Video đầu tiên có phụ đề, chữ, đồ hoạ, nhạc"],
    ["4", "7, 8 + nghiệm thu", "Xuất đủ khung; học viên tự dựng 1 video trước mặt trainer"],
    ["Kèm tới khi đạt", "nhắn tin", "Đủ 4 video"]], [1.8, 2.4, 7.3], size=16, rowh=0.62)
tx(s, 0.9, 6.1, 11.5, 0.6, "Giữa hai buổi: học viên dựng tư liệu thật của mình, gửi kết quả; trainer phản hồi trong 24 giờ.", 16)
foot(s, "Lộ trình")

s = d.slide()
eyebrow(s, "Quy trình một học viên"); title(s, "Năm bước từ kiểm máy tới lời chứng")
steps(s, 0.9, 2.3, 11.5, [("Kiểm máy", "15 phút: máy, RAM, ổ trống, AI đang dùng."),
    ("Phiếu khảo sát đầu vào", "Phần A của phiếu."),
    ("4 buổi theo giáo trình", "Mỗi buổi ghi: đã làm gì · kết quả · vấn đề · bài tập."),
    ("Nghiệm thu", "Học viên tự dựng 1 video, trainer chỉ xem."),
    ("Sau gói", "Lời chứng + số trước/sau.")], size=18, gap=0.82)
foot(s, "Lộ trình")

s = d.slide()
eyebrow(s, "Phiếu · A. Khảo sát đầu vào"); title(s, "Bốn câu hỏi trước buổi 1")
qa = [("Máy", "Mac / Windows · RAM · ổ trống"), ("AI", "Đang dùng AI nào, bản trả phí có trợ lý chạy lệnh chưa?"),
      ("Video hay làm", "Nói trước camera · vlog · sản phẩm · sự kiện · quay màn hình · ghi âm · khác"),
      ("Hiện dựng bằng gì", "App nào, mất bao lâu một video?")]
for i, (t, dd) in enumerate(qa):
    card(s, 0.9 + (i % 2) * 5.85, 2.25 + (i // 2) * 2.2, 5.6, 1.95, f"{i + 1} · {t}", dd, dsize=17)
foot(s, "Phiếu khảo sát và nghiệm thu")

s = d.slide()
eyebrow(s, "Phiếu · B. Trước / sau"); title(s, "Điền cột Trước ở buổi 1, cột Sau khi nghiệm thu")
table(s, 0.9, 2.4, 11.5, [["Chỉ số", "Trước", "Sau"],
    ["Thời gian công cho 1 video (giờ)", "", ""],
    ["Số video dựng được / tháng", "", ""],
    ["Tự tin tự dựng (1–10)", "", ""]], [6.5, 2.5, 2.5], size=18, rowh=0.9)
foot(s, "Phiếu khảo sát và nghiệm thu")

s = d.slide("dark")
eyebrow(s, "Phiếu · C. Nghiệm thu"); title(s, "Đủ cả 3 mới xong gói")
checks(s, 0.9, 2.5, 11.5, ["Tự dựng 1 video từ tư liệu mới, trainer chỉ ngồi xem",
    "≥ 4 video đã dựng xong bằng cách này", "Lời chứng (ẩn danh nếu muốn) + số trước/sau"], size=24, gap=0.95)
foot(s, "Phiếu khảo sát và nghiệm thu")

s = d.slide()
eyebrow(s, "Việc trainer chuẩn bị"); title(s, "Trước khách đầu tiên")
items = ["Bộ biểu mẫu: thiết lập hệ thống, SOP, hướng dẫn công việc, danh sách kiểm soát chất lượng",
         "Thử hướng dẫn thiết lập + SOP trên một máy Mac sạch và một máy Windows",
         "Bộ tư liệu thử (vài clip ngắn: nói, vlog, quay màn hình) cho buổi 1",
         "Kết quả mẫu để demo: video trainer đã dựng ở từng bước",
         "Chốt giá + kèm tiếp tối đa bao lâu",
         "Học viên thử đầu tiên"]
checks(s, 0.9, 2.2, 11.5, items, size=18, gap=0.68, done=[True, False, False, False, False, False])
foot(s, "Lộ trình")
d.save(f"{OUT}/bai-0-tong-quan-goi.pptx")

# ---------------- Bộ biểu mẫu ----------------
d = Deck("Bộ biểu mẫu cho học viên")
s = d.slide("dark")
eyebrow(s, "Dựng video bằng AI trên máy tính · Bộ biểu mẫu", 1.0)
tx(s, 0.9, 1.45, 11, 1.0, "Bốn biểu mẫu học viên dùng khi làm", 44, C["paper"], True, HEAD)
rows = [("01 · Hướng dẫn thiết lập hệ thống", "Bài 1", "Cài trợ lý AI và công cụ dựng trên Mac / Windows"),
        ("02 · Quy trình vận hành chuẩn (SOP)", "Bài 2, 8", "AI dựng trọn 8 bước bằng một câu"),
        ("03 · Hướng dẫn công việc", "Bài 3–7", "Câu giao việc khi làm hoặc sửa từng bước"),
        ("04 · Danh sách kiểm soát chất lượng", "Bài 8", "Kiểm bản AI bàn giao trước khi dùng")]
for i, (t, b, dd) in enumerate(rows):
    card(s, 0.9 + (i % 2) * 5.85, 2.75 + (i // 2) * 1.95, 5.6, 1.75, f"{t} · {b}", dd, dsize=17)
foot(s, "Bộ biểu mẫu")

s = d.slide()
eyebrow(s, "Biểu mẫu 01 · Hướng dẫn thiết lập hệ thống"); title(s, "Cần những gì, để làm gì")
table(s, 0.9, 2.1, 11.5, [["Công cụ", "Việc", "Giá"],
    ["Trợ lý AI chạy lệnh (chọn 1)", "Đọc SOP, chạy công cụ, làm trọn 8 bước", "Theo gói AI đang trả"],
    ["ffmpeg", "Cắt, ghép, đổi khung, gắn phụ đề, chuẩn âm lượng", "Miễn phí"],
    ["Whisper", "Chép lời có mốc thời gian (chạy trên máy)", "Miễn phí"],
    ["Node.js", "Chạy trợ lý AI và Remotion", "Miễn phí"],
    ["Python", "Các bước tự động nhỏ", "Miễn phí"],
    ["Remotion", "Dựng chữ, hình minh hoạ bằng code", "Miễn phí cá nhân, công ty ≤ 3 người"]], [3.2, 5.0, 3.3], size=14, rowh=0.6)
tx(s, 0.9, 6.45, 11.5, 0.35, "Lệnh và tên gói đổi theo thời gian: trainer kiểm lại trang chính thức trước mỗi khoá.", 13, C["rust"], True)
foot(s, "Biểu mẫu 01")

s = d.slide()
eyebrow(s, "Biểu mẫu 01 · Cách 1 (khuyên dùng)"); title(s, "Để AI tự cài, bạn đọc và đồng ý từng lệnh")
steps(s, 0.9, 2.2, 5.2, [("Cài Node.js", "từ nodejs.org, bản LTS."),
    ("Cài trợ lý AI", "theo trang chính thức; tự gõ mật khẩu, không đưa ai."),
    ("Tạo thư mục lam-video", "mở trợ lý AI trong đó, dán câu bên phải.")], size=16, gap=1.2)
code(s, 6.5, 2.2, 5.9, 3.6, "Kiểm tra máy tôi đã có ffmpeg, Python,\nWhisper chưa. Thiếu cái nào thì cài,\nGIẢI THÍCH từng lệnh trước khi chạy\nvà hỏi tôi đồng ý. Xong thì chạy thử:\nchép lời một file mẫu 10 giây\nvà báo kết quả.", 15, "Câu dán cho trợ lý AI")
foot(s, "Biểu mẫu 01")

s = d.slide()
eyebrow(s, "Biểu mẫu 01 · Cách 2"); title(s, "Tự cài bằng lệnh")
code(s, 0.9, 2.1, 5.6, 2.6, "/bin/bash -c \"$(curl -fsSL https://raw.\n  githubusercontent.com/Homebrew/install/\n  HEAD/install.sh)\"\nbrew install ffmpeg node python pipx\npipx install openai-whisper", 12, "Mac · Terminal")
code(s, 6.8, 2.1, 5.6, 2.6, "winget install Gyan.FFmpeg\nwinget install OpenJS.NodeJS.LTS\nwinget install Python.Python.3.12\npip install -U openai-whisper", 12, "Windows · PowerShell")
code(s, 0.9, 4.95, 11.5, 1.65, "npm install -g @anthropic-ai/claude-code\nnpm install -g @openai/codex\nnpm install -g @google/gemini-cli", 12, "Trợ lý AI · chọn 1, kiểm lại lệnh trên trang chính thức")
foot(s, "Biểu mẫu 01")

s = d.slide()
eyebrow(s, "Biểu mẫu 01 · Kiểm tra và lỗi hay gặp"); title(s, "In ra chữ, không báo lỗi là đạt")
code(s, 0.9, 2.1, 5.2, 2.3, "ffmpeg -version\nwhisper --help\n\n# bản whisper.cpp:\nwhisper-cli --help", 14, "Kiểm tra cài xong")
tx(s, 0.9, 4.65, 5.2, 1.2, "Đạt rồi thì chép biểu mẫu 02 vào thư mục lam-video (Bài 2).", 16)
card(s, 6.5, 2.1, 5.9, 1.3, "“command not found”", "Đóng mở lại Terminal / PowerShell; vẫn lỗi thì nhờ AI sửa đường dẫn.")
card(s, 6.5, 3.6, 5.9, 1.3, "Whisper chậm", "Dùng --model small khi thử, medium khi làm thật.")
card(s, 6.5, 5.1, 5.9, 1.3, "Hết ổ đĩa", "Mỗi tập xong chỉ giữ bản gốc + bản cuối.")
foot(s, "Biểu mẫu 01")

s = d.slide()
eyebrow(s, "Biểu mẫu 02 · Quy trình vận hành chuẩn (SOP)"); title(s, "Lưu đúng tên để AI tự đọc, rồi điền phong cách")
for i, (a, f) in enumerate([("Claude Code", "CLAUDE.md"), ("Codex", "AGENTS.md"), ("Gemini CLI", "GEMINI.md")]):
    card(s, 0.9, 2.15 + i * 1.15, 3.8, 1.0, a, f, dsize=16)
tx(s, 0.9, 5.7, 3.8, 1.0, "Giao việc chỉ cần nói: “Dựng tap-ten-video”.", 15, C["ink"], True)
box(s, 5.0, 2.15, 7.4, 4.45, C["card"], C["line"])
tx(s, 5.25, 2.35, 7.0, 0.4, "1. PHONG CÁCH (HỌC VIÊN ĐIỀN, SỬA DẦN)", 13, C["rust"], True, HEAD)
tx(s, 5.25, 2.85, 7.0, 3.7, ["Màu chính: …… · màu phụ: ……", "Kiểu chữ: tiêu đề …… · phụ đề ……",
    "Phụ đề: có / không · vị trí: dưới / giữa · cỡ: ……", "Dấu góc (tên / logo nhỏ): ……",
    "Nhạc: vui / lắng / không nhạc", "Khung xuất mặc định: ngang 16:9 · dọc 9:16 · vuông",
    "Video nói: giữ nguyên mạch / cắt gọn câu hỏng và khoảng lặng"], 16, C["ink"], spacing=1.45)
foot(s, "Biểu mẫu 02")

s = d.slide()
eyebrow(s, "Biểu mẫu 02 · 2. Thư mục"); title(s, "Mỗi video một thư mục tập, ba ngăn")
code(s, 0.9, 2.1, 7.0, 4.4, "lam-video/\n├── AGENTS.md        SOP này\n├── nhac/            nhạc miễn phí bản quyền\n└── tap-<ten-video>/\n    ├── 1-goc/       tư liệu gốc\n    ├── 2-lam/       loi.srt, canh.md,\n    │                ke-hoach.md, file tạm\n    └── 3-xuat/      ban-ngang.mp4, ban-doc.mp4,\n                     clip-1.mp4…, anh-bia.jpg", 14)
card(s, 8.2, 2.1, 4.2, 1.35, "1-goc", "Không sửa, không xoá.", hl=True)
card(s, 8.2, 3.6, 4.2, 1.35, "2-lam", "Chỗ AI làm việc. Xong tập thì xoá file tạm.")
card(s, 8.2, 5.1, 4.2, 1.35, "3-xuat", "Bản cuối để đăng.")
foot(s, "Biểu mẫu 02")

s = d.slide()
eyebrow(s, "Biểu mẫu 02 · 3. Khi tôi nói “Dựng tap-…”"); title(s, "Làm một mạch 8 bước")
L = [("Nạp", "đo độ dài, khung, chất lượng file trong 1-goc/."),
     ("Hiểu", "chép lời → loi.srt; chụp khung, mô tả cảnh → canh.md."),
     ("Kế hoạch", "→ ke-hoach.md. Video > 5 phút hoặc nhiều cảnh: cho xem trước."),
     ("Dựng thô", "bằng ffmpeg, theo kế hoạch.")]
R = [("Làm sạch", "xoay, cắt khung, sáng màu nhẹ, giảm ồn."),
     ("Phụ đề, chữ, đồ hoạ", "5–8 chữ mỗi lần; chữ nhấn đúng lời; không che."),
     ("Nhạc, âm thanh", "thấp dưới giọng; loudnorm khoảng −14 LUFS."),
     ("Xuất + tự kiểm", "các khung → 3-xuat/; chụp 6 khung kiểm lỗi; tự sửa.")]
steps(s, 0.9, 2.15, 5.7, L, size=14, gap=1.0)
steps(s, 6.8, 2.15, 5.7, R, size=14, gap=1.0, start=5)
tx(s, 0.9, 6.3, 11.5, 0.4, "Xong báo ngắn: file ở đâu, đã chọn gì vì sao, chỗ cần tôi xác nhận.", 14, C["rust"], True)
foot(s, "Biểu mẫu 02")

s = d.slide("dark")
eyebrow(s, "Biểu mẫu 02 · 4. Luật"); title(s, "Bốn luật AI giữ mỗi lần dựng")
for i, (t, dd) in enumerate([("Lời thật", "Chữ trên video lấy đúng lời trong video; không bịa lời."),
        ("Ít kiểu", "Dễ hiểu hơn cầu kì: mỗi video ít kiểu hiệu ứng."),
        ("An toàn", "Không sửa, không xoá 1-goc/. Hỏi trước khi xoá file khác hay tốn tiền. Không hỏi, không lưu mật khẩu."),
        ("Tự sửa SOP", "Phản hồi → sửa video, rồi sửa đúng một câu trong SOP, báo câu đã sửa.")]):
    card(s, 0.9 + (i % 2) * 5.85, 2.2 + (i // 2) * 2.2, 5.6, 1.95, t, dd, dsize=16)
foot(s, "Biểu mẫu 02")

blocks = [
  ("Nạp và hiểu tư liệu", "Đo độ dài, khung, chất lượng các file trong\n[tap-…/1-goc]. Chép lời (tiếng Việt) có mốc\nthời gian, liệt kê chữ không chắc. Chụp khung\nhình mỗi [10] giây, mô tả từng cảnh một dòng."),
  ("Kế hoạch sản xuất", "Tôi muốn ra: [video gì, dài bao nhiêu, khung\nnào, không khí gì]. Viết kế hoạch dạng bảng:\ngiây bắt đầu – kết thúc – cảnh / lời – chữ –\nhình – nhạc. Chưa dựng, cho tôi xem trước."),
  ("Dựng thô", "Dựng thô theo kế hoạch. Cắt khoảng lặng\n> [1] giây và câu nói hỏng rồi nói lại.\nChuyển cảnh: cắt thẳng, chỉ dùng mờ dần\nkhi đổi chủ đề."),
  ("Làm sạch", "Kiểm và sửa: chiều xoay, khung lệch, chỗ tối\nhay cháy sáng, tiếng ồn nền, tiếng to nhỏ\nkhông đều. Sửa nhẹ, giữ màu tự nhiên.\nBáo đã sửa gì."),
  ("Phụ đề và chữ", "Thêm phụ đề 5–8 chữ mỗi lần, [vị trí], không\nche mặt / sản phẩm. Thêm chữ nhấn ở [3] chỗ\nquan trọng nhất, lấy ĐÚNG lời trong video,\n≤ 6 chữ."),
  ("Đồ hoạ, hình minh hoạ, nhạc", "Đề xuất 2–3 chỗ cần hình minh hoạ, tôi chọn\nrồi mới làm. Nhạc nền từ thư mục nhac/ hợp\nkhông khí [vui / lắng], thấp dưới giọng,\nchuẩn âm khoảng −14 LUFS."),
  ("Xuất nhiều khung", "Xuất: [ngang 16:9 / dọc 9:16 bám chủ thể /\nvuông]. Cắt [1–3] clip ngắn 30–90 giây, mỗi\nclip một ý trọn. Ảnh bìa: khung rõ mặt / rõ\nsản phẩm nhất, ≤ 5 chữ. Chụp khung kiểm lỗi."),
  ("Sửa theo phản hồi", "Phản hồi của tôi: [phản hồi]. Sửa video,\nrồi sửa đúng một câu trong SOP để lần sau\ntự đúng. Cho tôi xem câu đã sửa.")]
for k in range(0, 8, 2):
    s = d.slide()
    eyebrow(s, f"Biểu mẫu 03 · Hướng dẫn công việc ({k // 2 + 1}/4)")
    title(s, "Câu giao việc từng bước: thay phần trong [ ]")
    for j in range(2):
        t, c = blocks[k + j]
        code(s, 0.9 + j * 5.85, 2.2, 5.6, 3.7, c.replace("\n", " "), 15, t.upper())
    foot(s, "Biểu mẫu 03")

s = d.slide()
eyebrow(s, "Biểu mẫu 04 · Danh sách kiểm soát chất lượng"); title(s, "Kiểm một video trước khi dùng")
cols = [("Trước khi giao AI", ["Tư liệu ở tap-<ten>/1-goc/, tên không dấu", "Biết muốn ra gì: loại · dài · khung · không khí", "SOP đã có phong cách"]),
        ("Xem bản AI giao", ["Mạch trơn, không mất đoạn chính", "Hình đúng chiều, đủ sáng, không lệch", "Tiếng rõ, nhạc không lấn giọng", "Phụ đề đúng, đọc kịp, không che", "Chữ nhấn, đồ hoạ đúng lúc", "Bản dọc vẫn rõ chủ thể", "Clip ngắn đứng riêng vẫn hiểu", "Ảnh bìa rõ khi nhỏ"]),
        ("Sau khi xong", ["Phản hồi đã sửa vào SOP, không chỉ sửa video", "Giữ gốc + bản cuối, xoá file tạm trong 2-lam/"])]
xs = [(0.9, 3.5), (4.6, 4.3), (9.1, 3.3)]
for (x, w), (t, its) in zip(xs, cols):
    box(s, x, 2.1, w, 4.55, C["card"], C["line"])
    tx(s, x + 0.2, 2.25, w - 0.4, 0.4, t.upper(), 13, C["rust"], True, HEAD)
    checks(s, x + 0.2, 2.75, w - 0.4, its, size=13, gap=0.47 if len(its) > 4 else 0.85)
foot(s, "Biểu mẫu 04")
d.save(f"{OUT}/bo-bieu-mau.pptx")
print("ok")
