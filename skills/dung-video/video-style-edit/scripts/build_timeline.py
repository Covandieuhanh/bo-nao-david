# Timeline FCPXML cho DaVinci Resolve: build_timeline.py <dự án>
# V1 video gốc (+ tiếng) · V2 cảnh toàn màn hình · V3 thẻ · V4 chữ to/tên · V5 khung an toàn (tắt sẵn) · cuối: nguồn ảnh
import os, sys, urllib.parse
from xml.sax.saxutils import quoteattr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load, nframes

P = os.path.expanduser(sys.argv[1])
d = load(P); pr, scenes, out_ = d["project"], d["scenes"], d["out"]
M = os.path.join(P, "davinci/media")
FN, FD, W, H = pr["fpsNum"], pr["fpsDen"], out_["width"], out_["height"]   # khung xuất (pillar: ngang)
FULL = {"montage", "recap", "converge", "master"}
LANE = lambda t: 1 if t in FULL else 2 if t == "card" else 3
CREDIT_SEC = 5
fr = lambda s: round(s * FN / FD)
t = lambda n: f"{n * FD}/{FN}s"
url = lambda n: "file://" + urllib.parse.quote(os.path.join(M, n))
still = lambda i, n: (f'<asset id="{i}" name="{n[:-4]}" start="0s" duration="0s" hasVideo="1" format="fmtStill">'
                      f'<media-rep kind="original-media" src="{url(n)}"/></asset>')

src = out_["base"]; src_n = nframes(os.path.join(M, src))
res = [f'<format id="fmt" name="FFVideoFormatRateUndefined" frameDuration="{FD}/{FN}s" width="{W}" height="{H}"/>',
       f'<format id="fmtStill" name="FFVideoFormatRateUndefined" width="{W}" height="{H}"/>',
       f'<asset id="src" name="video_goc" start="0s" duration="{t(src_n)}" hasVideo="1" hasAudio="1" format="fmt" '
       f'audioSources="1" audioChannels="2" audioRate="48000"><media-rep kind="original-media" src="{url(src)}"/></asset>']
conn, markers = [], []
if os.path.exists(os.path.join(M, "khung_an_toan.png")):
    res.append(still("guide", "khung_an_toan.png"))
    conn.append(f'<video ref="guide" lane="4" offset="0s" start="0s" duration="{t(src_n)}" name="khung_an_toan" enabled="0"/>')
for s in scenes:
    n = nframes(os.path.join(M, s["id"] + ".mov"))
    res.append(f'<asset id="{s["id"]}" name="{s["id"]}" start="0s" duration="{t(n)}" hasVideo="1" format="fmt">'
               f'<media-rep kind="original-media" src="{url(s["id"] + ".mov")}"/></asset>')
    conn.append(f'<asset-clip ref="{s["id"]}" lane="{LANE(s["type"])}" offset="{t(fr(s["start"]))}" start="0s" duration="{t(n)}" name="{s["id"]}"/>')
    markers.append(f'<marker start="{t(fr(s["start"]))}" duration="{t(1)}" value={quoteattr(s["id"])}/>')
if os.path.exists(os.path.join(M, "phu_de.mov")):   # phụ đề: track trên cùng
    n = nframes(os.path.join(M, "phu_de.mov"))
    res.append(f'<asset id="phude" name="phu_de" start="0s" duration="{t(n)}" hasVideo="1" format="fmt">'
               f'<media-rep kind="original-media" src="{url("phu_de.mov")}"/></asset>')
    conn.append(f'<asset-clip ref="phude" lane="5" offset="0s" start="0s" duration="{t(n)}" name="phu_de"/>')
tail, total = "", src_n
if os.path.exists(os.path.join(M, "nguon_anh.png")):
    res.append(still("credits", "nguon_anh.png"))
    tail = f'<video ref="credits" offset="{t(src_n)}" start="0s" duration="{t(fr(CREDIT_SEC))}" name="nguon_anh"/>'
    total += fr(CREDIT_SEC)
J = lambda xs, k: ("\n" + " " * k).join(xs)
name = os.path.basename(P.rstrip("/"))
xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.9">
 <resources>
  {J(res, 2)}
 </resources>
 <library>
  <event name="{name}">
   <project name="{name}">
    <sequence format="fmt" duration="{t(total)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
     <spine>
      <asset-clip ref="src" offset="0s" start="0s" duration="{t(src_n)}" name="video_goc" format="fmt" tcFormat="NDF">
       {J(markers, 7)}
       {J(conn, 7)}
      </asset-clip>
      {tail}
     </spine>
    </sequence>
   </project>
  </event>
 </library>
</fcpxml>
'''
out = os.path.join(P, "davinci/timeline.fcpxml")
open(out, "w", encoding="utf-8").write(xml)
import xml.dom.minidom; xml.dom.minidom.parse(out)
print(out, len(scenes), "cảnh, XML hợp lệ")
