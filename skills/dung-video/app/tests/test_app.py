import ast,json,sys,tempfile,unittest
from pathlib import Path
A=Path(__file__).resolve().parents[1];sys.path.insert(0,str(A))
import chat_luong,nha_cung_cap,goi_claude,chay
class Kiem(unittest.TestCase):
 def flow(self,reviews,maxround=2):
  with tempfile.TemporaryDirectory() as tmp:
   W=Path(tmp);(W/'duyet-hinh.json').write_text(json.dumps(reviews[0]));called=[]
   def review(tt,bid):
    called.append('review');(W/'duyet-hinh.json').write_text(json.dumps(reviews[min(called.count('review'),len(reviews)-1)]));return 'xong'
   def run(*args):called.append('repair');return 0
   result=chat_luong.chay({},dict(duyet_lai='duyet-hinh',so_vong_sua=maxround,lenh='repair'),W/'log',review,lambda tt:{'W':tmp},run,lambda s,b:s)
   return result,called
 def test_sua_phai_xem_lai(self):
  r,c=self.flow([{'dat':False,'ke_hoach':{'canh':[]}},{'dat':True}]);self.assertEqual((r,c),('xong',['repair','review']))
 def test_khong_dat_dung(self):
  r,c=self.flow([{'dat':False,'ke_hoach':{'canh':[]}}]);self.assertEqual(r,'loi');self.assertEqual(c.count('review'),2)
 def test_thieu_ke_hoach_dung(self):self.assertEqual(self.flow([{'dat':False}]),('loi',[]))
 def test_da_dat_khong_render(self):self.assertEqual(self.flow([{'dat':True}]),('xong',[]))
 def test_provider(self):
  self.assertEqual(nha_cung_cap.cau_hinh({'AI':'codex'}),'codex')
  with self.assertRaises(ValueError):nha_cung_cap.cau_hinh({'AI':'other'})
 def test_tat_ca_loi_nhac(self):
  for p in (A/'buoc').glob('*.json'):
   d=json.loads(p.read_text())
   if d.get('loai')=='claude':
    h=goi_claude.loi_he_thong(d,{'HO_SO':'lam-video'});self.assertNotIn('{{',h,p.name)
 def test_cong_thuc(self):
  for p in (A/'cong-thuc').glob('*.json'):
   for bid in json.loads(p.read_text())['buoc']:
    ph=chay.phieu(bid)
    if ph.get('duyet_lai'):self.assertEqual(chay.phieu(ph['duyet_lai'])['loai'],'claude')
 def test_python(self):
  for p in A.rglob('*.py'):ast.parse(p.read_text(),filename=str(p))
class Khuon(unittest.TestCase):
 def test_sai_boolean(self):
  from kiem_khuon import kiem
  with self.assertRaises(ValueError):kiem({'dat':'true'},{'type':'object','properties':{'dat':{'type':'boolean'}}})
 def test_thieu_bat_buoc(self):
  from kiem_khuon import kiem
  with self.assertRaises(ValueError):kiem({}, {'type':'object','required':['dat']})
class BaoVe(unittest.TestCase):
 def test_loi_ngoai_ke_hoach_khong_duoc_qua(self):
  with tempfile.TemporaryDirectory() as tmp:
   W=Path(tmp);(W/'duyet-hinh.json').write_text(json.dumps({'dat':True,'can_xu_ly_ngoai_ke_hoach':['sửa template']}))
   def no(*a):raise AssertionError('không được chạy render')
   r=chat_luong.chay({},dict(duyet_lai='duyet-hinh',lenh='repair'),W/'log',no,lambda tt:{'W':tmp},no,no)
   self.assertEqual(r,'loi')
 def test_kiem_ky_thuat_loi_phai_dung(self):
  from unittest.mock import patch
  import runpy,subprocess
  with tempfile.TemporaryDirectory() as tmp:
   with patch.object(sys,'argv',['chay_kiem.py',tmp,tmp]), patch('glob.glob',return_value=['kiem_vi_du.py']), patch('subprocess.run',return_value=subprocess.CompletedProcess([],1,'không đạt','')):
    with self.assertRaises(SystemExit) as err:runpy.run_path(str(A/'kiem/chay_kiem.py'),run_name='__main__')
    self.assertEqual(err.exception.code,1)
 def test_khong_bo_canh_sau_moc_40(self):
  from unittest.mock import patch
  import runpy,subprocess
  with tempfile.TemporaryDirectory() as tmp:
   P=Path(tmp);(P/'motion/src').mkdir(parents=True);(P/'check').mkdir()
   C=[dict(id=str(i),start=i*4,end=i*4+3) for i in range(45)]
   (P/'motion/src/scenes.js').write_text('export const SCENES = '+json.dumps(C)+'\n];')
   # Input scene JSON closes with ] on a separate line as in generated scenes.js.
   (P/'motion/src/scenes.js').write_text('export const SCENES = '+json.dumps(C)[:-1]+'\n];')
   (P/'motion/src/project.js').write_text('export default {duration: 185};')
   calls=[]
   def fake(cmd,**kw):calls.append(cmd);(P/'check/sheet.jpg').write_bytes(b'fixture');return subprocess.CompletedProcess(cmd,0)
   with patch.object(sys,'argv',['to_kiem_tra.py',tmp]),patch('subprocess.run',side_effect=fake):runpy.run_path(str(A/'ap/to_kiem_tra.py'),run_name='__main__')
   self.assertGreater(len(calls),1)
   self.assertIn('178.6',[v for cmd in calls for v in cmd])
if __name__=='__main__':unittest.main()
