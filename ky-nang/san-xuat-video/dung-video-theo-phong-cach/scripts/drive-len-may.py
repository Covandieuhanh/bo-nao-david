#!/usr/bin/env python3
"""Máy Windows: xác nhận từng tệp ĐÃ LÊN MÂY Google Drive (chạy bằng Python phía Windows).

Cách dùng: python -I -X utf8 drive-len-may.py <thư mục trên máy> <đường dẫn dưới "My Drive", dùng /> [--cho GIÂY] [--bo TÊN ...]
Đọc bản chép tạm của cơ sở dữ liệu ứng dụng Google Drive (chỉ đọc). Một tệp tính là đã lên mây khi bản ghi cùng đường dẫn có đủ:
mã trên mây thật (không phải mã tạm "local-…"), dung lượng phía mây bằng tệp trên máy, và mã MD5 của tệp trên máy.
Đo 26/11/2026: tệp đang chờ có mã "local-…" và dung lượng 0. Cơ sở dữ liệu này Google không công bố: ứng dụng đổi cấu trúc thì
công cụ trả mã 3 ("không kiểm được"), khi đó không được báo là đã lên mây.
Mã thoát: 0 mọi tệp đã lên mây · 1 còn tệp chưa xác nhận được khi hết giờ chờ · 3 không kiểm được.
"""
import argparse, hashlib, os, shutil, sqlite3, sys, tempfile, time, unicodedata

ap = argparse.ArgumentParser()
ap.add_argument('may'); ap.add_argument('drive')
ap.add_argument('--cho', type=int, default=0)
ap.add_argument('--bo', nargs='*', default=[])          # tên tệp hoặc thư mục bỏ qua
a = ap.parse_args()
chuan = lambda s: unicodedata.normalize('NFC', s)
BO = {x.lower() for x in a.bo} | {'desktop.ini'}


def tep_tren_may():
    ra = {}
    for goc, thu_muc, tep in os.walk(a.may):
        thu_muc[:] = [t for t in thu_muc if t.lower() not in BO]
        for t in tep:
            if t.lower() in BO:
                continue
            p = os.path.join(goc, t)
            h = hashlib.md5()
            with open(p, 'rb') as f:
                for khoi in iter(lambda: f.read(1 << 22), b''):
                    h.update(khoi)
            ra[chuan(os.path.relpath(p, a.may).replace('\\', '/'))] = (os.path.getsize(p), h.hexdigest().encode())
    return ra


def doc_drive():
    """→ {đường dẫn tương đối trong thư mục đích: [(mã, dung lượng phía mây, bản ghi)]}"""
    goc = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'DriveFS')
    tk = [d for d in os.listdir(goc) if d.isdigit()]
    if len(tk) != 1:
        raise RuntimeError('ứng dụng Drive có %d tài khoản, công cụ cần đúng 1' % len(tk))
    tam = tempfile.mkdtemp()
    try:
        for t in ('metadata_sqlite_db', 'metadata_sqlite_db-wal', 'metadata_sqlite_db-shm'):
            p = os.path.join(goc, tk[0], t)
            if os.path.exists(p):
                shutil.copy(p, tam)
        c = sqlite3.connect(os.path.join(tam, 'metadata_sqlite_db'))
        c.text_factory = lambda b: b.decode('utf-8', 'surrogateescape')
        try:
            muc = {r[0]: r for r in c.execute('select stable_id, id, local_title, is_folder, file_size, trashed, is_tombstone from items')}
            cha = dict(c.execute('select item_stable_id, parent_stable_id from stable_parents'))
            dau = '/' + chuan(a.drive.strip('/')) + '/'
            ra = {}
            for s, r in muc.items():
                if r[3] or r[5] or r[6]:
                    continue
                ten, x = [], s
                while x in muc and len(ten) < 40:
                    ten.append(muc[x][2] or ''); x = cha.get(x)
                day = '/' + chuan('/'.join(reversed(ten)))
                # ten[-1] là gốc "My Drive": đường dẫn đích phải bắt đầu ngay dưới gốc
                phan = day.split('/', 2)
                if len(phan) < 3 or not ('/' + phan[2]).startswith(dau):
                    continue
                (ban_ghi,) = c.execute('select proto from items where stable_id=?', (s,)).fetchone()
                if not isinstance(ban_ghi, bytes):
                    ban_ghi = str(ban_ghi).encode('utf-8', 'surrogateescape')
                ra.setdefault(('/' + phan[2])[len(dau):], []).append((str(r[1]), r[4], ban_ghi))
            return ra
        finally:
            c.close()
    finally:
        shutil.rmtree(tam, ignore_errors=True)


def main():
    may = tep_tren_may()
    if not may:
        print('✗ không có tệp nào để kiểm ở ' + a.may); return 3
    het = time.time() + a.cho
    bao = 0
    while True:
        try:
            tren = doc_drive()
        except Exception as e:                       # cấu trúc đổi, tệp đang bị khoá…
            tren, loi = None, e
        if tren is not None:
            con = [t for t, (co, md5) in may.items()
                   if not any(not ma.startswith('local') and cd == co and md5 in bg for ma, cd, bg in tren.get(t, []))]
            if not con:
                print('✓ ĐÃ LÊN MÂY: %d/%d tệp, khớp dung lượng và mã MD5' % (len(may), len(may))); return 0
        if time.time() >= het:
            break
        if time.time() - bao >= 60:
            bao = time.time()
            print('  đợi Drive tải lên… còn %s' % (len(con) if tren is not None else '?'), flush=True)
        time.sleep(10)
    if tren is None:
        print('✗ KHÔNG KIỂM ĐƯỢC trạng thái trên mây: %s' % loi); return 3
    print('✗ CHƯA xác nhận được %d/%d tệp đã lên mây:' % (len(con), len(may)))
    for t in con[:20]:
        print('   - ' + t)
    return 1


sys.exit(main())
