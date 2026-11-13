import json, sys, re, unicodedata
from pathlib import Path
from pptx import Presentation
from pptx.util import Emu

png = Path(sys.argv[1]); out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
meta = json.loads((png / "meta.json").read_text())

def slug(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

for n, m in meta.items():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)  # 16:9
    prs.core_properties.title = m["title"]
    prs.core_properties.author = "David Trần"
    blank = prs.slide_layouts[6]
    for i, s in enumerate(m["slides"], 1):
        sl = prs.slides.add_slide(blank)
        sl.shapes.add_picture(str(png / f"bai-{n}-{i:02d}.png"), 0, 0, prs.slide_width, prs.slide_height)
        continue  # khong ghi chu: Quick Look treo khi co notes
        if s["note"]: notes.append(s["note"])
        notes.append("Nội dung slide:\n" + s["text"])
        sl.notes_slide.notes_text_frame.text = "\n\n".join(notes)
    name = slug(m["title"].replace("·", " "))
    f = out / f"{name}.pptx"
    prs.save(f)
    print(f.name, len(m["slides"]), "slide")
