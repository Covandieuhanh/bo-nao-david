#!/usr/bin/env python3
"""Dọn file tạm của một tập sau khi David chốt bản cuối (David chốt 08/11/2026).

  python3 -I don_tap.py ~/Movies/tap-<tên> [...]          chỉ LIỆT KÊ (mặc định), không đụng gì
  python3 -I don_tap.py --xoa ~/Movies/tap-<tên> [...]    thực hiện — CHỈ sau khi David duyệt danh sách

Giữ:  1-goc/ · video-final*.mp4 ở gốc mỗi dự án (2-ban-dai/, clip-X/; trừ bản -khong-teaser) · mọi thứ trong phat-hanh/ · mọi file chữ
      (kịch bản, phụ đề, kế hoạch cắt, bài đăng, số liệu, scenes.js…).
Bỏ:   node_modules, .remotion, .cache → xoá hẳn (cài lại được).
      Mọi file hình / tiếng / video còn lại (davinci/media, motion/public, nguon.mp4, src/, cat/, check/, bản cũ…)
      → Thùng rác (~/.Trash/don-<tập>-<ngày>/), David tự đổ.
Dự án (2-ban-dai, clip-X) chưa có video-final.mp4 → bỏ qua, báo lại. Không đụng ~/Movies/vlog.
"""
import os, shutil, sys, time

MEDIA = {'.mp4', '.mov', '.m4a', '.wav', '.aac', '.mp3', '.mkv', '.webm', '.mxf', '.png', '.jpg', '.jpeg', '.webp',
         '.gif', '.heic', '.tif', '.tiff', '.psd', '.ttf', '.otf', '.woff', '.woff2', '.pack'}
XOA_HAN = {'node_modules', '.remotion', '.cache'}
MOVIES = os.path.realpath(os.path.expanduser('~/Movies'))


def co(n):
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024: return f'{n:.0f} {u}' if u in ('B', 'KB') else f'{n:.1f} {u}'
        n /= 1024
    return f'{n:.1f} TB'


def du(p):
    t = 0
    for r, ds, fs in os.walk(p):
        for f in fs:
            try: t += os.lstat(os.path.join(r, f)).st_size
            except OSError: pass
    return t


def la_du_an(d):  # thư mục dự án cần có bản cuối
    b = os.path.basename(d)
    return b == '2-ban-dai' or (b.startswith('clip-') and os.path.basename(os.path.dirname(d)) == '3-highlight')


def quet(T):
    bo_qua, xoa_han, rac = [], [], []
    # dự án chưa có bản cuối → bỏ qua cả thư mục (3-highlight: một clip thiếu thì giữ nguồn chung)
    for r, ds, fs in os.walk(T):
        ds[:] = [d for d in ds if d not in XOA_HAN]
        if la_du_an(r) and 'video-final.mp4' not in fs:
            bo_qua.append(r)
    hl = os.path.join(T, '3-highlight')
    if os.path.isdir(hl):
        clips = [d for d in os.listdir(hl) if d.startswith('clip-')]
        if not clips or any(os.path.join(hl, c) in bo_qua for c in clips):
            bo_qua = [b for b in bo_qua if not b.startswith(hl + os.sep)] + [hl]
    skip = lambda p: any(p == b or p.startswith(b + os.sep) for b in bo_qua)
    for r, ds, fs in os.walk(T):
        if skip(r):
            ds[:] = []; continue
        for d in list(ds):
            if d in XOA_HAN:
                xoa_han.append(os.path.join(r, d)); ds.remove(d)
        if r == os.path.join(T, '1-goc') or r.startswith(os.path.join(T, '1-goc') + os.sep):
            ds[:] = []; continue
        if 'phat-hanh' in os.path.relpath(r, T).split(os.sep):
            continue
        for f in fs:
            p = os.path.join(r, f)
            if la_du_an(r) and f.startswith('video-final') and f.endswith('.mp4') and 'khong-teaser' not in f:   # vd. video-final-dien-thoai.mp4
                continue
            if os.path.splitext(f)[1].lower() in MEDIA or f.endswith('_tmp'):
                rac.append(p)
    return bo_qua, xoa_han, rac


def main():
    a = sys.argv[1:]
    thuc = '--xoa' in a
    taps = [os.path.realpath(os.path.expanduser(x)) for x in a if x != '--xoa']
    if not taps: sys.exit(__doc__)
    tong = 0
    for T in taps:
        ten = os.path.basename(T)
        if os.path.dirname(T) != MOVIES or not ten.startswith('tap-') or not os.path.isdir(T):
            print(f'✗ {T}: chỉ dọn thư mục ~/Movies/tap-<tên> — bỏ qua'); continue
        bo_qua, xoa_han, rac = quet(T)
        s_han = sum(du(p) for p in xoa_han)
        s_rac = sum(os.lstat(p).st_size for p in rac)
        # file liên kết cứng với nơi khác (vd. 1-goc) không giải phóng chỗ
        s_that = sum(os.lstat(p).st_size for p in rac if os.lstat(p).st_nlink == 1)
        tong += s_han + s_that
        print(f'\n== {ten}: {co(du(T))} → giải phóng ~{co(s_han + s_that)}')
        for b in bo_qua:
            print(f'   ⏸ bỏ qua {os.path.relpath(b, T)}/ (chưa có video-final.mp4)')
        if xoa_han:
            print(f'   xoá hẳn  {co(s_han):>9}  node_modules / .remotion / .cache ({len(xoa_han)} thư mục)')
        nhom = {}
        for p in rac:
            k = os.path.relpath(os.path.dirname(p), T).split(os.sep)
            k = os.sep.join(k[:3])
            n = nhom.setdefault(k, [0, 0]); n[0] += 1; n[1] += os.lstat(p).st_size
        for k, (n, s) in sorted(nhom.items(), key=lambda x: -x[1][1]):
            print(f'   thùng rác {co(s):>9}  {k}/ ({n} file)')
        if thuc:
            for p in xoa_han: shutil.rmtree(p, ignore_errors=True)
            D = os.path.expanduser(f'~/.Trash/don-{ten}-{time.strftime("%Y%m%d-%H%M")}')
            for p in rac:
                q = os.path.join(D, os.path.relpath(p, T)); os.makedirs(os.path.dirname(q), exist_ok=True)
                shutil.move(p, q)
            for r, ds, fs in os.walk(T, topdown=False):   # bỏ thư mục rỗng
                if r != T and not os.listdir(r):
                    try: os.rmdir(r)
                    except OSError: pass
            print(f'   ✓ đã dọn — file tạm ở Thùng rác: {D}')
    print(f'\nTổng giải phóng ~{co(tong)}' + ('' if thuc else ' (CHƯA làm gì — chạy lại với --xoa sau khi David duyệt)')
          + ('\nĐổ Thùng rác để lấy lại chỗ.' if thuc else ''))


main()
