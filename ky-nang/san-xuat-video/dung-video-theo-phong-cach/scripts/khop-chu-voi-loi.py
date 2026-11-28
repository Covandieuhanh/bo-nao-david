#!/usr/bin/env python3
"""Khớp chữ trên hình với lời nói: mỗi chữ hiện ĐÚNG LÚC người nói nói ra nó (nguyên lý "Đúng lúc", huong-dan-lua-chon.md bước 4b).

  python3 -I khop-chu-voi-loi.py <canh.js> <moc-tung-tu.srt> [--sua]

- Đọc SCENES trong canh.js; mọi mục có chữ (text, label, chu, ten, value, lon) kèm `at`, và cặp `<khoá>` + `<khoá>_at` (ví dụ nhan + nhan_at).
- Tìm cụm chữ đầu của mục (tối đa 3 từ, bỏ dấu *) trong bản mốc từng từ quanh cảnh, lấy lần nói gần `at` nhất.
- In mục lệch (hiện sớm hơn lời quá 0,25 giây hoặc trễ quá 0,6 giây) và mục không tìm thấy trong lời (chữ không nguyên văn — luật 3 — hoặc lời chép sai).
- --sua: dời `at` về lúc nói trừ 0,05 giây (khoá cùng mục trùng giá trị `at` cũ như sang_tu dời theo), ghi lại canh.js. Mục đã khai
  `"khop": false` thì giữ nguyên (mốc theo cử chỉ hoặc hình, không theo lời).
Bản mốc từng từ phải là của CHÍNH video sẽ xuất. Video ghép nhiều đoạn: dùng bản chép từng đoạn (`ghep-doan-kho-hieu-ung.py --chep-loi`).
"""
import json, re, subprocess, sys, unicodedata

CHU = ('text', 'chu', 'ten', 'lon', 'value', 'label')   # value trước label: mốc thời gian, cột hiện lúc nói con số
SOM, TRE, TRUOC = 0.25, 0.6, 0.05

def chuan(s):
    return re.sub(r'[^\w]', '', unicodedata.normalize('NFC', s.lower()))

def doc_tu(p):
    ra = []
    for b in re.split(r'\n\s*\n', open(p, encoding='utf-8').read().strip()):
        l = b.strip().split('\n')
        m = re.match(r'(\d+):(\d+):(\d+)[,.](\d+)', l[1]) if len(l) >= 3 else None
        if not m:
            continue
        t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + int(m[4]) / 1000
        for x in ' '.join(l[2:]).split():
            if chuan(x):
                ra.append((t, chuan(x)))
    return ra

def tim(tu, cum, at):
    """Lần nói cụm `cum` gần `at` nhất; khớp ít nhất 2/3 từ đầu (1/1 khi cụm một từ)."""
    can = len(cum) if len(cum) < 3 else 2
    hop = []
    for i in range(len(tu)):
        khop = sum(1 for j, w in enumerate(cum) if i + j < len(tu) and tu[i + j][1] == w)
        if tu[i][1] == cum[0] and khop >= can or khop >= max(can, len(cum)):
            hop.append(tu[i][0])
    return min(hop, key=lambda x: abs(x - at)) if hop else None

def muc(o, ra):
    if isinstance(o, dict):
        if o.get('khop') is not False:
            for k in CHU:
                if isinstance(o.get(k), str) and isinstance(o.get('at'), (int, float)):
                    ra.append((o, k, 'at'))
                    break
            for k, v in o.items():
                if isinstance(v, str) and isinstance(o.get(k + '_at'), (int, float)):
                    ra.append((o, k, k + '_at'))
        for v in o.values():
            muc(v, ra)
    elif isinstance(o, list):
        for v in o:
            muc(v, ra)

def doc_canh(js):
    """SCENES trong canh.js: JSON (bản ghép tự sinh) hoặc object JavaScript viết tay (đọc qua node)."""
    m = re.search(r'export const SCENES = (\[.*?\n\]);', js, flags=re.S)
    try:
        return m, json.loads(m.group(1))
    except ValueError:
        r = subprocess.run(['node', '-e', 'process.stdout.write(JSON.stringify(' + m.group(1) + '))'], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit('Không đọc được SCENES: ' + r.stderr[-600:])
        return m, json.loads(r.stdout)

def thay_moc(khoi, chu, kt, cu, moi):
    """Đổi `kt: cu` gần chuỗi `chu` nhất ngay trong file (giữ chú thích, cách viết của file); trả khối mới hoặc None."""
    q = json.dumps(chu, ensure_ascii=False)[1:-1]
    so = re.escape(f'{cu:g}') + (r'(?:\.0+)?' if float(cu).is_integer() else '') + r'(?![\d.])'   # 220 viết trong file là 220.0
    mau = re.compile(r'(["\']?\b' + re.escape(kt) + r'\b["\']?\s*:\s*)' + so)
    vt = [mm.start() for mm in re.finditer(re.escape(q), khoi)]
    best = None
    for v in vt:
        for mm in mau.finditer(khoi, max(0, v - 400), v + 400 + len(q)):
            d = abs(mm.start() - v)
            if best is None or d < best[0]:
                best = (d, mm)
    if not best:
        return None
    mm = best[1]
    return khoi[:mm.start()] + mm.group(1) + f'{moi:g}' + khoi[mm.end():]

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cj, sua = sys.argv[1], '--sua' in sys.argv
    TU = doc_tu(sys.argv[2])
    js = open(cj, encoding='utf-8').read()
    m, SC = doc_canh(js)
    khoi = m.group(1)
    lech = khong = da_sua = 0
    for c in SC:
        tu = [x for x in TU if c['start'] - 2 <= x[0] <= c['end'] + 1]
        ra = []
        muc(c.get('props', {}), ra)
        for o, k, kt in ra:
            cum = [chuan(x) for x in o[k].replace('*', '').split() if chuan(x)][:3]
            if not cum:
                continue
            at = o[kt]
            g = tim(tu, cum, at)
            if g is None:
                khong += 1
                print(f'?  {c["id"]:22} "{o[k]}" ({kt} {at}): không thấy trong lời — chữ phải nguyên văn, hoặc lời chép sai')
                continue
            d = at - g
            if d < -SOM or d > TRE:
                lech += 1
                moi = round(g - TRUOC, 2)
                print(f'!  {c["id"]:22} "{o[k]}" {kt} {at} — lời {g:.2f} (lệch {d:+.1f})' + (f' → {moi}' if sua else ''))
                if sua:
                    for kk, vv in list(o.items()):
                        if isinstance(vv, (int, float)) and not isinstance(vv, bool) and abs(vv - at) < 1e-6:
                            k2 = thay_moc(khoi, o[k], kk, vv, moi)
                            if k2 is None:
                                print(f'   ↳ không tìm được chỗ ghi {kk} trong file — sửa tay')
                                continue
                            khoi = k2
                            o[kk] = moi
                    da_sua += 1
                    if moi < c['start'] + 0.1:
                        print(f'   ↳ mốc mới trước lúc cảnh bắt đầu ({c["start"]}): dời start của cảnh hoặc chọn đoạn rộng hơn')
    print(f'Mục lệch: {lech} · không thấy trong lời: {khong}' + (f' · đã sửa {da_sua}' if sua else ''))
    if sua and da_sua:
        js = js[:m.start(1)] + khoi + js[m.end(1):]
        open(cj, 'w', encoding='utf-8').write(js)
    sys.exit(1 if (lech and not sua) or khong else 0)

if __name__ == '__main__':
    main()
