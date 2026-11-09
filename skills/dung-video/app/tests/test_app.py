import ast,json,sys,tempfile,unittest
from pathlib import Path
A=Path(__file__).resolve().parents[1];sys.path.insert(0,str(A))
import chay
class Kiem(unittest.TestCase):
 def test_cong_thuc(self):
  for p in (A/'cong-thuc').glob('*.json'):
   for bid in json.loads(p.read_text())['buoc']:
    ph=chay.phieu(bid)
    self.assertIn(ph['loai'],('ai','co-dinh','duyet'),bid)   # không còn kiểu cũ (khuôn JSON)
    if ph['loai']=='ai':self.assertTrue(ph.get('viec'),bid)
 def test_python(self):
  for p in A.rglob('*.py'):ast.parse(p.read_text(),filename=str(p))
class BaoVe(unittest.TestCase):
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
   that=subprocess.run
   def fake(cmd,**kw):
    if cmd[0]=='node':return that(cmd,**kw)   # đọc scenes.js bằng node thật (canh_js)
    calls.append(cmd);(P/'check/sheet.jpg').write_bytes(b'fixture');return subprocess.CompletedProcess(cmd,0)
   with patch.object(sys,'argv',['to_kiem_tra.py',tmp]),patch('subprocess.run',side_effect=fake):runpy.run_path(str(A/'ap/to_kiem_tra.py'),run_name='__main__')
   self.assertGreater(len(calls),1)
   self.assertIn('178.6',[v for cmd in calls for v in cmd])
if __name__=='__main__':unittest.main()
