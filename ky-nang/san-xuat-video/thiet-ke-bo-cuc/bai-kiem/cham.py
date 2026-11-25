# Chấm bài kiểm suy luận dựng video (thiet-ke-bo-cuc/bai-kiem/README.md).
#   python3 -I cham.py <bai-lam.json>        — bài làm: [{"id": "d01", "can": "Chia đoạn", "lam": "diagram chuoi, bước đang nói sáng"}, …]
#   python3 -I cham.py --mau                 — in bài làm mẫu (đáp án) để thử công cụ chấm
# Một đoạn ĐẠT khi: (1) "can" có ít nhất một nguyên lý trong dap_an.can; (2) "lam" chạm ít nhất một cách trong dap_an.lam_duoc
# (so theo từ khoá); (3) "lam" không chạm cách nào trong dap_an.khong_lam. Đạt ≥ 8/10 → máy này lập luận được. Đoạn lệch in ra để David chấm.
import json, re, sys, unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
DE = json.loads((HERE / 'de.json').read_text(encoding='utf-8'))
NL = json.loads((HERE.parent / 'nguyen-ly.json').read_text(encoding='utf-8'))['nguyen_ly']

def chuan(t):
    return unicodedata.normalize('NFC', str(t)).lower().strip()

def co(k, lam):   # từ khoá đứng riêng ("nhan" không khớp "nhanh")
    k = k.strip()
    if not re.search(r'\w', k): return k in lam   # ký hiệu như "^"
    return re.search(r'(?<!\w)' + re.escape(k) + r'(?!\w)', lam) is not None

def cham_doan(d, bl):
    lido = []
    can = [chuan(x) for x in bl.get('can', '').replace('+', ',').replace('/', ',').split(',') if x.strip()]
    sai_ten = [c for c in can if c not in {chuan(k) for k in NL}]
    if sai_ten: lido.append(f'tên nguyên lý không có: {", ".join(sai_ten)}')
    ok_can = any(c in [chuan(x) for x in d['dap_an']['can']] for c in can)
    if not ok_can: lido.append(f'nguyên lý chính phải là một trong: {", ".join(d["dap_an"]["can"])}')
    lam = chuan(bl.get('lam', ''))
    ok_lam = any(all(co(k, lam) for k in chuan(c).split('+')) for c in d['dap_an']['lam_duoc'])
    if not ok_lam: lido.append(f'cách làm chưa chạm: {" | ".join(d["dap_an"]["lam_duoc"])}')
    pham = [c for c in d['dap_an'].get('khong_lam', []) if all(co(k, lam) for k in chuan(c).split('+'))]
    if pham: lido.append(f'làm điều không nên: {", ".join(pham)}')
    return ok_can and ok_lam and not pham and not sai_ten, lido

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--mau':
        print(json.dumps([{'id': d['id'], 'can': d['dap_an']['can'][0], 'lam': d['dap_an']['lam_duoc'][0].replace('+', ' ')} for d in DE['doan']], ensure_ascii=False, indent=1))
        return
    if len(sys.argv) < 2:
        print(__doc__ if __doc__ else 'cách dùng: cham.py <bai-lam.json> | --mau'); sys.exit(2)
    bai = {b['id']: b for b in json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))}
    dat = 0
    for d in DE['doan']:
        ok, lido = cham_doan(d, bai.get(d['id'], {}))
        dat += ok
        print(f"{'✓' if ok else '✗'} {d['id']} · {d['loai']}" + ('' if ok else '\n   ' + '\n   '.join(lido)))
    n = len(DE['doan'])
    print(f'\nĐạt {dat}/{n} → ' + ('MÁY NÀY LẬP LUẬN ĐƯỢC' if dat >= DE.get('dat', 8) else 'CHƯA ĐẠT — đọc lại nhu-cau-nguoi-xem.md + truong-hop-da-giai.md, gửi đoạn ✗ cho David chấm'))
    sys.exit(0 if dat >= DE.get('dat', 8) else 1)

if __name__ == '__main__':
    main()
