#!/usr/bin/env python3
"""Ghép các đoạn đã chọn từ nhiều video gốc thành MỘT video gốc chung cho bản xem đủ kho hiệu ứng
(thiet-ke-bo-cuc/README.md mục 4a, quy trình thiet-ke-bo-cuc/kho-hieu-ung-tu-video-goc.md).

  python3 -I ghep-doan-kho-hieu-ung.py <doan.json> <thư mục ra> [--doc]

doan.json: {"nguon": {"A": "/đường/dẫn/a.mp4", ...},
            "doan": [{"id": "the-canh", "nguon": "A", "tu": 70.2, "den": 80.4, "hieu_ung": "the-canh", "ghi_chu": "..."}, ...]}
Ra:  <ra>/video-goc.mp4 (khung 1920x1080 hoặc 1080x1920 với --doc, 30 fps, tiếng 48 kHz, nối liền theo thứ tự)
     <ra>/bang-moc.json  — mỗi đoạn: mốc bắt đầu / kết thúc trong video ghép + mốc gốc, để đổi mốc lời gốc sang mốc ghép
     <ra>/bang-moc.md    — bảng mốc đọc được (hiệu ứng · nguồn · mốc gốc · mốc trong video ghép)
Cắt từng đoạn bằng -ss trước -i (nhanh trên nguồn dài, khối 02), mã hoá lại để điểm nối khớp khung; video xoay (điện thoại) được ffmpeg tự xoay.
Khung khác tỉ lệ được thu vừa và thêm viền tối, không cắt mất người.
"""
import json, os, subprocess, sys, tempfile

def chay(lenh):
    r = subprocess.run(lenh, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Lỗi ffmpeg: {' '.join(lenh[:6])}…\n{r.stderr[-1500:]}")
    return r.stdout

def mm_ss(x):
    return f"{int(x // 60):02d}:{x % 60:05.2f}"

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cau_hinh = json.load(open(sys.argv[1], encoding='utf-8'))
    ra = sys.argv[2]
    doc = '--doc' in sys.argv
    W, H = (1080, 1920) if doc else (1920, 1080)
    os.makedirs(ra, exist_ok=True)
    tam = tempfile.mkdtemp(prefix='ghep-kho-')
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x101010,"
          f"fps=30,format=yuv420p,setsar=1")
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
        bang.append({**d, 'file': os.path.basename(src), 'bat_dau': round(moc, 3), 'ket_thuc': round(moc + that, 3), 'lech': round(moc - d['tu'], 3)})
        moc += that
    noi = os.path.join(tam, 'noi.txt')
    with open(noi, 'w') as fh:
        fh.writelines(f"file '{p}'\n" for p in danh_sach)
    chay(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', noi, '-c', 'copy', '-movflags', '+faststart',
          os.path.join(ra, 'video-goc.mp4')])
    json.dump(bang, open(os.path.join(ra, 'bang-moc.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(ra, 'bang-moc.md'), 'w', encoding='utf-8') as fh:
        fh.write('| # | Hiệu ứng | Nguồn | Mốc gốc | Mốc trong video ghép | Ghi chú |\n|---|---|---|---|---|---|\n')
        for i, b in enumerate(bang, 1):
            fh.write(f"| {i} | {b.get('hieu_ung', b['id'])} | {b['file']} | {mm_ss(b['tu'])}–{mm_ss(b['den'])} | "
                     f"{mm_ss(b['bat_dau'])}–{mm_ss(b['ket_thuc'])} | {b.get('ghi_chu', '')} |\n")
    for p in danh_sach + [noi]:
        os.remove(p)
    os.rmdir(tam)
    print(f"Đã ghép {len(bang)} đoạn, dài {moc:.1f} s → {ra}/video-goc.mp4")

if __name__ == '__main__':
    main()
