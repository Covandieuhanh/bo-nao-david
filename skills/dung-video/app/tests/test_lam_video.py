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

class Usage(unittest.TestCase):
 def test_doc_usage(self):
  import json,subprocess;sys.path.insert(0,str(A));import han_muc
  chu="Current session: 27% used · resets Nov 10 at 3:10am (Asia/Saigon)\nCurrent week (all models): 90% used · resets Nov 13 at 1pm (Asia/Saigon)"
  with tempfile.TemporaryDirectory() as t:
   han_muc.KHO=Path(t);han_muc.F=Path(t)/'_han-muc.json'
   han_muc._claude=lambda:('claude',{})
   that=subprocess.run
   subprocess.run=lambda *a,**k:subprocess.CompletedProcess(a,0,json.dumps({'result':chu}),'')
   try:d=han_muc.lam_moi()
   finally:subprocess.run=that
   self.assertEqual((d['five_hour']['dung'],d['seven_day']['dung']),(27,90))
   from datetime import datetime;from zoneinfo import ZoneInfo
   m=datetime.fromtimestamp(d['seven_day']['mo_lai'],ZoneInfo('Asia/Saigon'));self.assertEqual((m.day,m.hour,m.minute),(13,13,0))
class XoaSua(unittest.TestCase):
 def test_chan_xoa_dung_chung_va_doi_ten(self):
  import json;sys.path.insert(0,str(A));import giao_dien as g
  with tempfile.TemporaryDirectory() as t:
   T=Path(t);g.KHO=T/'_app';g.MOVIES=T
   tap=T/'tap-x';(tap/'1-goc').mkdir(parents=True);(tap/'2-ban-dai').mkdir();(tap/'3-highlight').mkdir()
   def viec(ten,P,video):(g.KHO/ten).mkdir(parents=True);(g.KHO/ten/'trang-thai.json').write_text(json.dumps({'ten':ten,'cong_thuc':'lam-video','video':video,'P':str(P),'buoc':{},'tuy_chon':{}}))
   viec('dai',tap/'2-ban-dai',str(tap/'1-goc/a.mov'));viec('hl',tap/'3-highlight',str(tap/'2-ban-dai'))
   r=g.thu_xoa('dai',3)
   self.assertEqual([Path(x['duong_dan']).name for x in r['xoa']],['dai','1-goc'])
   self.assertEqual(r['chan'][0]['dang_dung'],['hl'])               # bản dài đang là nguồn của highlight → không xoá
   self.assertEqual([Path(x['duong_dan']).name for x in g.thu_xoa('hl',3)['xoa']],['hl','3-highlight'])   # highlight không đụng file gốc
   self.assertEqual(g.thu_xoa('dai',1)['xoa'][0]['duong_dan'],str(g.KHO/'dai'))
   g.sua_viec('hl','hl-moi',{'yeu_cau':'mới','P':'không được đổi'})
   tt=json.loads((g.KHO/'hl-moi/trang-thai.json').read_text())
   self.assertEqual((tt['ten'],tt['tuy_chon']['yeu_cau'],tt['P']),('hl-moi','mới',str(tap/'3-highlight')))
