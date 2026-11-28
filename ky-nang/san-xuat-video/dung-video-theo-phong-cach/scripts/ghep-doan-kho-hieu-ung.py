#!/usr/bin/env python3
"""Ghép các đoạn đã chọn từ nhiều video gốc thành MỘT video gốc chung cho bản xem đủ kho hiệu ứng
(thiet-ke-bo-cuc/README.md mục 4a, quy trình thiet-ke-bo-cuc/kho-hieu-ung-tu-video-goc.md).

  python3 -I ghep-doan-kho-hieu-ung.py <doan.json> <thư mục ra> [--doc] [--chep-loi] [--canh-js <canh.js của dự án>]

doan.json: {"nguon": {"A": "/đường/dẫn/a.mp4", ...},
            "doan": [{"id": "the-canh", "nguon": "A", "tu": 70.2, "den": 80.4, "hieu_ung": "the-canh", "ghi_chu": "..."}, ...]}
Ra:  <ra>/video-goc.mp4 (khung 1920x1080 hoặc 1080x1920 với --doc, 30 fps, tiếng 48 kHz, nối liền theo thứ tự)
     <ra>/bang-moc.json  — mỗi đoạn: mốc bắt đầu / kết thúc trong video ghép + mốc gốc, để đổi mốc lời gốc sang mốc ghép
     <ra>/bang-moc.md    — bảng mốc đọc được (hiệu ứng · nguồn · mốc gốc · mốc trong video ghép)
     --chep-loi: chép lời TỪNG ĐOẠN ngay sau khi cắt (whisper-cli), ghi <ra>/loi/moc-tung-tu.srt và ban-chep-loi.srt theo mốc video ghép.
       Đoạn ngắn cho mốc từ đúng; chép một lượt cả video ghép dài làm mốc trôi tới hơn 1 giây (đo 28/11/2026). Mô hình: biến WHISPER_MODEL
       hoặc ~/whisper-models/ggml-large-v3-turbo.bin.
     --canh-js: thay SCENES và CHAPTERS (mỗi đoạn một chương, tên = hieu_ung) trong canh.js bằng cảnh đã đổi mốc — doan.json là nguồn
       duy nhất của cảnh, sửa cảnh thì sửa ở doan.json rồi chạy lại.
Cắt từng đoạn bằng -ss trước -i (nhanh trên nguồn dài, khối 02), mã hoá lại để điểm nối khớp khung; video xoay (điện thoại) được ffmpeg tự xoay.
Khung khác tỉ lệ được thu vừa và thêm viền tối, không cắt mất người.
"""
import json, os, re, subprocess, sys, tempfile

def chay(lenh):
    r = subprocess.run(lenh, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Lỗi ffmpeg: {' '.join(lenh[:6])}…\n{r.stderr[-1500:]}")
    return r.stdout

def ten_nguon(src):
    """Tên tập chứa tệp (thư mục tap-…) kèm tên tệp, để bảng mốc chỉ đúng nguồn."""
    phan = src.split(os.sep)
    tap = next((x for x in reversed(phan[:-1]) if x.startswith('tap-')), '')
    return f"{tap}/{phan[-1]}" if tap else phan[-1]

def srt_doc(p, lech):
    """Đọc srt, cộng `lech` giây; trả [(bắt đầu, kết thúc, chữ)]."""
    ra = []
    if not os.path.exists(p):
        return ra
    t = lambda m: int(m[0]) * 3600 + int(m[1]) * 60 + int(m[2]) + int(m[3]) / 1000
    for b in re.split(r'\n\s*\n', open(p, encoding='utf-8').read().strip()):
        l = b.strip().split('\n')
        m = re.findall(r'(\d+):(\d+):(\d+)[,.](\d+)', l[1]) if len(l) >= 3 else []
        if len(m) == 2 and ' '.join(l[2:]).strip():   # giữ dấu cách đầu: phu-de.py dùng nó để biết đâu là từ mới
            ra.append((t(m[0]) + lech, t(m[1]) + lech, ' '.join(l[2:]).rstrip()))
    return ra

def srt_ghi(p, dong):
    f = lambda x: f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round(x % 1 * 1000)) % 1000:03d}"
    with open(p, 'w', encoding='utf-8') as fh:
        for i, (a, b, c) in enumerate(dong, 1):
            fh.write(f"{i}\n{f(a)} --> {f(b)}\n{c}\n\n")

BIA = re.compile(r"subscribe|đăng ký kênh|ghiền mì gõ|không bỏ lỡ những video", re.I)   # lời ảo của Whisper (loi-ao-giac.py)

def _whisper(wav, of, them):
    mo = os.environ.get('WHISPER_MODEL', os.path.expanduser('~/whisper-models/ggml-large-v3-turbo.bin'))
    r = subprocess.run(['whisper-cli', '-m', mo, '-l', 'vi', '-f', wav, '-mc', '0', *them, '-osrt', '-of', of, '-np'],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Lỗi whisper-cli: {r.stderr[-800:]}")
    return of + '.srt'

def chep_loi(mp4, tam, moc, dai, src=None, tu=0.0):
    """Chép lời một đoạn đã cắt; trả (dòng câu, dòng từ) theo mốc video ghép, bỏ phần lấn sang đoạn sau.
    Đoạn ngắn đôi khi ra lời ảo cả đoạn ("Hãy subscribe cho kênh…"): chép lại từ nguồn kèm 15 giây ngữ cảnh phía trước rồi lấy đúng khúc."""
    wav = os.path.join(tam, 'am.wav')
    for lan, dem in enumerate((0.0, 15.0)):
        if lan and not src:
            break
        dau = 0.0 if not lan else min(dem, tu)
        if not lan:
            chay(['ffmpeg', '-v', 'error', '-y', '-i', mp4, '-vn', '-ac', '1', '-ar', '16000', wav])
        else:
            chay(['ffmpeg', '-v', 'error', '-y', '-ss', str(tu - dau), '-t', str(dai + dau + 2), '-i', src, '-vn', '-ac', '1', '-ar', '16000', wav])
        lech = moc - dau
        ra = []
        for ten, them in (('cau', []), ('tu', ['-ml', '1', '-sow'])):
            f = _whisper(wav, os.path.join(tam, ten), them)
            ra.append([(max(a, moc), min(b, moc + dai), c) for a, b, c in srt_doc(f, lech) if moc - 0.05 <= a < moc + dai - 0.05])
            os.remove(f)
        if not any(BIA.search(c) for _, _, c in ra[0]) and ra[1]:
            break
        print(f"  lời ảo ở đoạn bắt đầu {moc:.1f} s — chép lại kèm ngữ cảnh", file=sys.stderr)
    os.remove(wav)
    if any(BIA.search(c) for _, _, c in ra[0]):
        sys.exit(f"Đoạn bắt đầu {moc:.1f} s vẫn ra lời ảo sau khi chép lại — nghe và chép tay")
    return ra

def mm_ss(x):
    return f"{int(x // 60):02d}:{x % 60:05.2f}"

MOC = {'start', 'end', 'at', 'at_hay', 'tu', 'gach', 'sang_tu', 'dau_at', 'nho_at', 'tieu_at'}

def la_moc(k):
    return k in MOC or k.endswith('At') or k.endswith('_at')

def doi_moc(x, lech, tu, den):
    """Cộng `lech` vào mọi khoá mốc (start, end, at, …At, …_at, tu, gach); mốc phải nằm trong đoạn [tu, den]."""
    if isinstance(x, list):
        return [doi_moc(v, lech, tu, den) for v in x]
    if isinstance(x, dict):
        ra = {}
        for k, v in x.items():
            if la_moc(k) and isinstance(v, (int, float)) and not isinstance(v, bool):
                if not (tu - 0.01 <= v <= den + 0.01):
                    sys.exit(f"Mốc {k}={v} nằm ngoài đoạn {tu}–{den} (cảnh {x.get('id', '')})")
                ra[k] = round(v + lech, 3)
            else:
                ra[k] = doi_moc(v, lech, tu, den)
        return ra
    return x

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cau_hinh = json.load(open(sys.argv[1], encoding='utf-8'))
    # Lá B15 bước 4: đoạn dùng lại cho hiệu ứng khác chỉ khi nội dung thật sự hợp — cảnh báo để người dựng xem lại, không chặn
    ds = cau_hinh['doan']
    chong = [f"{a['id']} và {b['id']} (nguồn {a['nguon']}, chồng {min(a['den'], b['den']) - max(a['tu'], b['tu']):.1f} giây)"
             for i, a in enumerate(ds) for b in ds[i + 1:]
             if a['nguon'] == b['nguon'] and min(a['den'], b['den']) - max(a['tu'], b['tu']) > 0.5]
    if chong:
        print('Cảnh báo — đoạn dùng chung lời, kiểm lại nội dung có hợp với từng hiệu ứng không:\n  ' + '\n  '.join(chong), file=sys.stderr)
    ra = sys.argv[2]
    doc = '--doc' in sys.argv
    W, H = (1080, 1920) if doc else (1920, 1080)
    os.makedirs(ra, exist_ok=True)
    tam = tempfile.mkdtemp(prefix='ghep-kho-')
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x101010,"
          f"fps=30,format=yuv420p,setsar=1")
    co_loi = '--chep-loi' in sys.argv
    loi_cau, loi_tu = [], []
    danh_sach, bang, moc = [], [], 0.0
    for i, d in enumerate(cau_hinh['doan']):
        src = cau_hinh['nguon'][d['nguon']]
        dai = round(d['den'] - d['tu'], 3)
        if dai <= 0:
            sys.exit(f"Đoạn {d['id']}: 'den' phải lớn hơn 'tu'")
        out = os.path.join(tam, f"{i:03d}.mp4")
        chay(['ffmpeg', '-v', 'error', '-y', '-ss', str(d['tu']), '-i', src, '-t', str(dai), '-vf', vf,
              '-af', 'aresample=48000,aformat=channel_layouts=stereo', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
              '-c:a', 'aac', '-b:a', '192k', '-shortest', out])
        that = float(chay(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out]).strip())
        danh_sach.append(out)
        if co_loi:
            c, t = chep_loi(out, tam, moc, that, src, d['tu'])
            loi_cau += c; loi_tu += t
        bang.append({**d, 'file': ten_nguon(src), 'bat_dau': round(moc, 3), 'ket_thuc': round(moc + that, 3), 'lech': round(moc - d['tu'], 3)})
        moc += that
    noi = os.path.join(tam, 'noi.txt')
    with open(noi, 'w') as fh:
        fh.writelines(f"file '{p}'\n" for p in danh_sach)
    chay(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', noi, '-c', 'copy', '-movflags', '+faststart',
          os.path.join(ra, 'video-goc.mp4')])
    json.dump(bang, open(os.path.join(ra, 'bang-moc.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(ra, 'bang-moc.md'), 'w', encoding='utf-8') as fh:
        fh.write('| # | Hiệu ứng | Nguồn | Mốc gốc | Mốc trong bản xem | Ghi chú |\n|---|---|---|---|---|---|\n')
        for i, b in enumerate(bang, 1):
            fh.write(f"| {i} | {b.get('hieu_ung', b['id'])} | {b['file']} | {mm_ss(b['tu'])}–{mm_ss(b['den'])} | "
                     f"{mm_ss(b['bat_dau'])}–{mm_ss(b['ket_thuc'])} | {b.get('ghi_chu', '')} |\n")
    # Cảnh viết theo MỐC GỐC trong từng đoạn ("canh": [{id, type, start, end, props}]) → đổi sang mốc video ghép, ghi canh-ghep.js
    canh = []
    for b in bang:
        for c in b.get('canh', []):
            canh.append(doi_moc(c, b['lech'], b['tu'], b['den']))
    if canh:
        with open(os.path.join(ra, 'canh-ghep.js'), 'w', encoding='utf-8') as fh:
            fh.write('// Tự sinh bởi ghep-doan-kho-hieu-ung.py — mốc đã đổi sang video ghép. Chép vào SCENES của canh.js\n')
            fh.write('export const SCENES_GHEP = ' + json.dumps(canh, ensure_ascii=False, indent=1) + ';\n')
    if co_loi:
        os.makedirs(os.path.join(ra, 'loi'), exist_ok=True)
        srt_ghi(os.path.join(ra, 'loi', 'ban-chep-loi.srt'), loi_cau)
        srt_ghi(os.path.join(ra, 'loi', 'moc-tung-tu.srt'), loi_tu)
        print(f"Lời từng đoạn: {len(loi_cau)} câu, {len(loi_tu)} từ → {ra}/loi/")
    if '--canh-js' in sys.argv:
        cj = sys.argv[sys.argv.index('--canh-js') + 1]
        js = open(cj, encoding='utf-8').read()
        chuong = [{'at': b['bat_dau'], 'text': b.get('hieu_ung', b['id'])} for b in bang]
        js = re.sub(r'export const SCENES = \[.*?\n\];', lambda m: 'export const SCENES = ' + json.dumps(canh, ensure_ascii=False, indent=1) + ';', js, count=1, flags=re.S)
        js = re.sub(r'export const CHAPTERS = \[.*?\];', lambda m: 'export const CHAPTERS = ' + json.dumps(chuong, ensure_ascii=False) + ';', js, count=1, flags=re.S)
        open(cj, 'w', encoding='utf-8').write(js)
        print(f"Đã ghi {len(canh)} cảnh, {len(chuong)} chương vào {cj}")
        if co_loi:
            # chữ trên hình về đúng lúc nói (khop-chu-voi-loi.py), rồi ghi mốc đã khớp ngược về doan.json để doan.json vẫn là nguồn duy nhất
            subprocess.run([sys.executable, '-I', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'khop-chu-voi-loi.py'),
                            cj, os.path.join(ra, 'loi', 'moc-tung-tu.srt'), '--sua'])
            js = open(cj, encoding='utf-8').read()
            moi = json.loads(re.search(r'export const SCENES = (\[.*?\n\]);', js, flags=re.S).group(1))
            theo = {d['id']: [] for d in cau_hinh['doan']}
            for c in moi:
                b = next(b for b in bang if b['bat_dau'] - 0.05 <= c['start'] < b['ket_thuc'])
                theo[b['id']].append(doi_moc(c, -b['lech'], -1e9, 1e9))
            for d in cau_hinh['doan']:
                if theo[d['id']]:
                    d['canh'] = theo[d['id']]
            json.dump(cau_hinh, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            print(f"Đã ghi mốc đã khớp lời về {sys.argv[1]}")
    for p in danh_sach + [noi]:
        os.remove(p)
    os.rmdir(tam)
    print(f"Đã ghép {len(bang)} đoạn, dài {moc:.1f} s → {ra}/video-goc.mp4")

if __name__ == '__main__':
    main()
