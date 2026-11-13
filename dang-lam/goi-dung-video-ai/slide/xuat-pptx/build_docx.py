import json, sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor

png = Path(sys.argv[1]); out = Path(sys.argv[2])
meta = json.loads((png / "meta.json").read_text())
d = Document()
st = d.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(11)
d.add_heading("Ghi chú trainer · Dựng video bằng AI trên máy tính", 0)
d.add_paragraph("Đi kèm 8 file slide .pptx cùng thư mục. Mỗi mục: số slide · tiêu đề · ghi chú trainer.")
for n, m in meta.items():
    d.add_heading(m["title"], 1)
    for i, s in enumerate(m["slides"], 1):
        first = s["text"].split("\n")
        head = " · ".join(x for x in first[:2] if x.strip())
        p = d.add_paragraph()
        r = p.add_run(f"Slide {i} · {head}"); r.bold = True; r.font.color.rgb = RGBColor(0xB0, 0x4A, 0x12)
        note = s["note"].replace("Ghi chú trainer:", "").strip()
        d.add_paragraph(note if note else "(không có ghi chú)")
f = out / "ghi-chu-trainer-8-bai.docx"
d.save(f); print(f)
