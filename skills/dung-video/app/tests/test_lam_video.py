import shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
A=Path(__file__).resolve().parents[1]
LOI='một hai ba bốn năm sáu bảy tám chín mười mười một mười hai mười ba mười bốn mười lăm mười sáu'.split(' ')
@unittest.skipUnless(shutil.which('ffmpeg'),'cần ffmpeg')
class AmGoc(unittest.TestCase):
 def test_keo_to_ca_bai_khong_bao_re(self):
  with tempfile.TemporaryDirectory() as t:
   P=Path(t);(P/'motion/src').mkdir(parents=True);(P/'davinci/media').mkdir(parents=True)
   (P/'motion/src/project.js').write_text('export const project = {duration: 3};')
   g=P/'davinci/media/video_goc.mp4'
   subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','sine=f=300:d=3','-f','lavfi','-i','anoisesrc=a=0.002:d=3','-filter_complex',
                   'amix=inputs=2,volume=0.1','-c:a','aac','-b:a','192k',str(g)],check=True)
   subprocess.run(['ffmpeg','-v','error','-i',str(g),'-af','volume=10dB','-c:a','aac','-b:a','192k',str(P/'video-final.mp4')],check=True)
   r=subprocess.run([sys.executable,'-I',str(A/'kiem/kiem_am_goc.py'),str(P)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout)
class CongThuc(unittest.TestCase):
 """Mọi công thức khớp skill: mọi bước có phiếu, bước AI chỉ tới file skill có thật, lời nhắc không sót biến."""
 def setUp(self):
  import json;sys.path.insert(0,str(A));import chay,goi_ai;self.chay,self.goi_ai,self.json=chay,goi_ai,json
  self.ds=list(dict.fromkeys(b for p in sorted((A/'cong-thuc').glob('*.json')) for b in json.loads(p.read_text())['buoc']))   # mọi công thức
 def test_moi_buoc_co_phieu_khong_trung(self):
  self.assertEqual(len(self.ds),len(set(self.ds)))
  for b in self.ds:self.chay.phieu(b)
 def test_buoc_ai_tro_dung_file_skill(self):
  import re
  for b in self.ds:
   ph=self.chay.phieu(b)
   if ph['loai']!='ai':continue
   for f in re.findall(r"`((?:khoi|trinh-bay|ho-so|video-style-edit|dang-da-kenh|cat-highlight-video|podcast-style-edit)/[\w./-]+)`",ph['viec']):
    self.assertTrue((A.parent/f.rstrip('/')).exists(),f'{b}: {f}')
 def test_loi_nhac_khong_sot_bien(self):
  b={k:'X' for k in ('APP','DV','S','HL','P','W','VIDEO','TEN','HO_SO','TAP','KHUNG','HOOK','AI','AI_MODEL')}
  with tempfile.TemporaryDirectory() as t:
   b['W']=t
   for x in self.ds:
    ph=self.chay.phieu(x)
    if ph['loai']=='ai':self.assertNotRegex(self.goi_ai.loi_nhac(ph,b,None),r"\{[A-Z_]+\}",x)
class HanMuc(unittest.TestCase):
 def test_doc_su_kien(self):
  import json,os;sys.path.insert(0,str(A));import han_muc
  with tempfile.TemporaryDirectory() as t:
   han_muc.KHO=Path(t);han_muc.F=Path(t)/'_han-muc.json'
   han_muc.doc_dong(json.dumps({'type':'rate_limit_event','rate_limit_info':{'unifiedWindows':{'five_hour':{'utilization':0.82,'resetsAt':1,'status':'allowed'},'seven_day':{'utilization':0.5,'resetsAt':2}}}}))
   d=han_muc.doc();self.assertEqual((d['five_hour']['dung'],d['seven_day']['dung']),(82,50))
   han_muc.doc_dong('{"type":"assistant"}');self.assertEqual(han_muc.doc()['five_hour']['dung'],82)
