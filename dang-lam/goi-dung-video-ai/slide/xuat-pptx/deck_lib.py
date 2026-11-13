import os, subprocess
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

C = dict(paper="F7F5F0", ink="15202B", orange="E8742A", rust="B04A12", soft="F2A26B",
         grey="4A5560", lgrey="6B737C", card="FFFDF9", line="E4DED2", dcard="1F2D3A",
         dline="2C3E4F", dtext="C9D3DC", code="0F1720", green="8FD3A8")
HEAD = "Be Vietnam Pro"; BODY = "Arial"; MONO = "Menlo"
FOOT = "Dựng video bằng AI trên máy tính"

def rgb(h): return RGBColor.from_string(h)

class Deck:
    def __init__(self, title):
        self.p = Presentation()
        self.p.slide_width, self.p.slide_height = Inches(13.333), Inches(7.5)
        self.p.core_properties.title = title
        self.p.core_properties.author = "David Trần"
        self.foot = FOOT

    def slide(self, theme="paper"):
        s = self.p.slides.add_slide(self.p.slide_layouts[6])
        bgc = {"paper": C["paper"], "dark": C["ink"], "accent": C["orange"]}[theme]
        f = s.background.fill; f.solid(); f.fore_color.rgb = rgb(bgc)
        s._theme = theme
        return s

    def save(self, path):
        # Quick Look lẫn hình giữa các slide khi id/tên hình trùng: đặt id + tên duy nhất toàn bộ file
        k = 1000
        for si, sl in enumerate(self.p.slides, 1):
            for sh in sl.shapes:
                k += 1
                el = sh._element
                c = el.find('.//{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr')
                if c is not None:
                    c.set('id', str(k)); c.set('name', f's{si}-shape{k}')
            vi_fonts(sl._element)
        self.p.save(path)

def vi_fonts(root):
    # Quick Look coi chữ có dấu (ắ, ụ, ề…) là chữ hệ khác, lấy font ea/cs; trống thì nhảy sang Times.
    # Khai cùng một font cho latin, ea, cs, sym + lang vi-VN thì dấu tiếng Việt hiện đúng.
    from pptx.oxml.ns import qn
    from lxml import etree
    for rPr in root.iter(qn('a:rPr'), qn('a:endParaRPr'), qn('a:defRPr')):
        rPr.set('lang', 'vi-VN')
        lat = rPr.find(qn('a:latin'))
        if lat is None: continue
        f = lat.get('typeface')
        for tag in ('a:ea', 'a:cs', 'a:sym'):
            e = rPr.find(qn(tag))
            if e is None:
                e = etree.Element(qn(tag)); lat.addnext(e) if tag == 'a:ea' else rPr.find(qn('a:ea' if tag == 'a:cs' else 'a:cs')).addnext(e)
            e.set('typeface', f)

def tx(s, x, y, w, h, text, size=20, color=None, bold=False, font=BODY, align=PP_ALIGN.LEFT,
       anchor=MSO_ANCHOR.TOP, spacing=1.3):
    dark = s._theme == "dark"
    color = color or (C["dtext"] if dark else C["grey"])
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    lines = text if isinstance(text, list) else [text]
    for i, ln in enumerate(lines):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align; para.line_spacing = spacing
        if i > 0 and font != MONO: para.space_before = Pt(round(size * 0.35))
        runs = ln if isinstance(ln, list) else [(ln, {})]
        for r in runs:
            if isinstance(r, str): r = (r, {})
            t, o = r
            run = para.add_run(); run.text = t
            ft = run.font; ft.name = o.get("font", font); ft.size = Pt(o.get("size", size))
            ft.bold = o.get("bold", bold); ft.color.rgb = rgb(o.get("color", color))
    return tb

def eyebrow(s, text, y=0.75):
    c = {"dark": C["soft"], "accent": C["ink"]}.get(s._theme, C["rust"])
    tx(s, 0.9, y, 11.5, 0.4, text.upper(), 14, c, True, HEAD)

def title(s, text, y=1.15, size=34, w=11.5):
    c = C["paper"] if s._theme == "dark" else C["ink"]
    tx(s, 0.9, y, w, 1.2, text, size, c, True, HEAD, spacing=1.15)

def foot(s, extra=""):
    c = {"dark": C["lgrey"], "accent": C["ink"]}.get(s._theme, C["lgrey"])
    tx(s, 0.9, 6.85, 11.5, 0.3, FOOT + (" · " + extra if extra else ""), 11, c)

def _border(cell, color):
    from pptx.oxml.ns import qn
    from lxml import etree
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        ln = etree.SubElement(tcPr, qn(tag), w=str(Pt(1.25)) if color else "0")
        if color:
            sf = etree.SubElement(ln, qn("a:solidFill")); etree.SubElement(sf, qn("a:srgbClr"), val=color)
        else:
            etree.SubElement(ln, qn("a:noFill"))
    # thứ tự chuẩn: border trước fill
    for f in tcPr.findall(qn("a:solidFill")): tcPr.remove(f); tcPr.append(f)

def box(s, x, y, w, h, fill, line=None, radius=0.08):
    # Ô nền là bảng 1 ô (không dùng hình vẽ): Quick Look lẫn hình vẽ giống nhau giữa các slide
    gt = s.shapes.add_table(1, 1, Inches(x), Inches(y), Inches(w), Inches(h)).table
    gt.columns[0].width = Inches(w); gt.rows[0].height = Inches(h)
    tbl = gt._tbl; tblPr = tbl.tblPr
    for a in ("firstRow", "bandRow"): tblPr.set(a, "0")
    c = gt.cell(0, 0); c.fill.solid(); c.fill.fore_color.rgb = rgb(fill)
    c.text_frame.paragraphs[0].text = ""
    _border(c, line)
    return gt

def card(s, x, y, w, h, t, d, hl=False, dsize=15, icon=None):
    dark = s._theme == "dark"
    if hl: fill, line, tc, dc = C["ink"], None, C["soft"], C["dtext"]
    elif dark: fill, line, tc, dc = C["dcard"], C["dline"], C["soft"], C["dtext"]
    else: fill, line, tc, dc = C["card"], C["line"], C["rust"], C["grey"]
    box(s, x, y, w, h, fill, line)
    dx = 0
    if icon: pic(s, icon, x + 0.25, y + 0.18, 0.42, tc); dx = 0.58
    tx(s, x + 0.25 + dx, y + 0.24, w - 0.5 - dx, 0.4, t, 13 if len(t) > 18 else 14, tc, True, HEAD)
    tx(s, x + 0.25, y + 0.72 if icon else y + 0.62, w - 0.5, h - 0.9, d, dsize, dc)

ICON_DIR = os.path.expanduser("~/Library/Caches/slide-icons")
def pic(s, name, x, y, size, color):
    # Biểu tượng Lucide thành ảnh PNG (icons.mjs), lưu sẵn để lần sau khỏi vẽ lại
    os.makedirs(ICON_DIR, exist_ok=True)
    f = f"{ICON_DIR}/{name}-{color}.png"
    if not os.path.exists(f):
        subprocess.run(["node", os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons.mjs"), ICON_DIR, f"{name}:{color}"], check=True)
    return s.shapes.add_picture(f, Inches(x), Inches(y), Inches(size), Inches(size))

def tile(s, x, y, w, h, icon, t, d, dark_tile=False, tsize=17, dsize=14):
    # Ô có biểu tượng lớn ở trên: dùng cho hình tổng quan, từ mới
    fill, line = (C["ink"], None) if dark_tile else (C["card"], C["line"])
    ic, tc, dc = (C["soft"], C["paper"], C["dtext"]) if dark_tile else (C["rust"], C["ink"], C["grey"])
    box(s, x, y, w, h, fill, line)
    pic(s, icon, x + 0.3, y + 0.28, 0.62, ic)
    tx(s, x + 0.3, y + 1.05, w - 0.6, 0.5, t, tsize, tc, True, HEAD)
    if d: tx(s, x + 0.3, y + 1.05 + tsize / 40, w - 0.6, h - 1.2 - tsize / 40, d, dsize, dc)

def gloss(s, x, y, items, colw=5.6, rowh=1.25, cols=2):
    # Từ mới: biểu tượng + thuật ngữ + nghĩa đời thường
    for i, (ic, k, v) in enumerate(items):
        cx, cy = x + (i % cols) * (colw + 0.35), y + (i // cols) * rowh
        box(s, cx, cy + 0.02, 0.72, 0.72, C["ink"])
        pic(s, ic, cx + 0.13, cy + 0.15, 0.46, C["soft"])
        tx(s, cx + 0.95, cy, colw - 0.95, 0.4, k, 17, C["ink"], True, HEAD)
        tx(s, cx + 0.95, cy + 0.42, colw - 0.95, rowh - 0.45, v, 14, C["grey"])

def code(s, x, y, w, h, text, size=12, label=None):
    box(s, x, y, w, h, C["code"], None, 0.04)
    yy = y + 0.18
    if label:
        tx(s, x + 0.25, yy, w - 0.5, 0.3, label, 11, C["lgrey"], True, MONO); yy += 0.35
    tx(s, x + 0.25, yy, w - 0.5, h - (yy - y) - 0.1, text.split("\n"), size, C["soft"], font=MONO, spacing=1.35)

def table(s, x, y, w, rows, colw, size=13, rowh=0.42, head=True):
    n, m = len(rows), len(rows[0])
    gt = s.shapes.add_table(n, m, Inches(x), Inches(y), Inches(w), Inches(rowh * n)).table
    tot = sum(colw)
    for j, cw in enumerate(colw): gt.columns[j].width = Emu(int(Inches(w) * cw / tot))
    for i, r in enumerate(rows):
        for j, val in enumerate(r):
            cell = gt.cell(i, j); cell.fill.solid()
            ishead = head and i == 0
            cell.fill.fore_color.rgb = rgb(C["ink"] if ishead else (C["card"] if i % 2 else "F1EEE7"))
            cell.margin_left = cell.margin_right = Inches(0.12); cell.margin_top = cell.margin_bottom = Inches(0.06)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = cell.text_frame; tf.word_wrap = True
            para = tf.paragraphs[0]; para.text = ""; para.line_spacing = 1.2
            run = para.add_run(); run.text = str(val)
            run.font.size = Pt(size); run.font.name = HEAD if ishead else BODY
            run.font.bold = ishead or (j == 0 and not ishead and m > 2)
            run.font.color.rgb = rgb(C["paper"] if ishead else (C["ink"] if j == 0 else C["grey"]))
    return gt

def checks(s, x, y, w, items, size=17, gap=0.55, done=None):
    dark = s._theme == "dark"
    for i, it in enumerate(items):
        ok = done and done[i]
        mark = "☑" if ok else "☐"
        mc = C["green"] if ok else (C["soft"] if dark else C["orange"])
        tc = C["paper"] if dark else C["ink"]
        tx(s, x, y + i * gap, w, gap, [[(mark + "  ", {"color": mc, "size": size + 2, "font": BODY}), (it, {"color": tc})]], size)

def steps(s, x, y, w, items, size=17, gap=0.78, start=1):
    dark = s._theme == "dark"
    for i, (t, d) in enumerate(items):
        yy = y + i * gap
        tx(s, x, yy - 0.04, 0.6, 0.6, f"{start + i:02d}", size + 4, C["orange"], True, HEAD)
        tc = C["paper"] if dark else C["ink"]; dc = C["dtext"] if dark else C["grey"]
        tx(s, x + 0.75, yy + 0.02, w - 0.75, gap, [[(t, {"bold": True, "color": tc, "font": HEAD}), ("  " + d if d else "", {"color": dc})]], size)
