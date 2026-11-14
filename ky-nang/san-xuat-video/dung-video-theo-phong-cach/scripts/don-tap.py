#!/usr/bin/env python3
"""Dọn file tạm của một tập sau khi David chốt bản cuối (chốt là dọn luôn, không hỏi lại), rồi đưa tập lên Drive bằng luu-drive.sh.

  python3 -I don-tap.py --xoa <dự án> [...]    David chốt bản cuối → Claude chạy thẳng, KHÔNG gửi danh sách hỏi duyệt
  python3 -I don-tap.py <dự án> [...]          chỉ LIỆT KÊ (xem trước khi cần), không đụng gì
  <dự án> = ~/Movies/tap-<tên> hoặc ~/Movies/vlog/<tên> (vlog ghép: bản cuối nằm ngay ở gốc thư mục).

VIỆC ĐANG DỞ → tự bỏ qua, báo ⏸ để Claude hỏi David riêng phần đó (chỉ lúc này mới hỏi):
  · có tiến trình (render, node, ffmpeg…) đang chạy trong dự án — thường là phiên khác đang làm;
  · có file kịch bản (danh-sach-cat.js, canh.js, phu-de.js, du-an.js, plan.json, cuts.json) sửa SAU video-final.mp4 (chưa render lại = đang làm lại);
  · chưa có video-final.mp4.

Giữ:  1-goc/ · video-final*.mp4 ở gốc mỗi dự án (2-ban-day-du/, clip-X/; trừ bản -khong-teaser) · mọi thứ trong phat-hanh/ · mọi file chữ
      (kịch bản, phụ đề, kế hoạch cắt, bài đăng, số liệu, canh.js…).
Bỏ:   node_modules, .remotion, .cache → xoá hẳn (cài lại được).
      Mọi file hình / tiếng / video còn lại (davinci/media, motion/public, nguon.mp4, src/, cat/, check/, bản cũ…)
      → xoá hẳn (file tạm, dựng lại được từ gốc + kịch bản).
Xong mà không có phần ⏸ → chạy nền: zsh luu-drive.sh <dự án> (lên Drive sao-luu-mac/video, kiểm khớp, xoá trên Mac).
"""
import os, shutil, subprocess, sys, time

MEDIA = {'.mp4', '.mov', '.m4a', '.wav', '.aac', '.mp3', '.mkv', '.webm', '.mxf', '.png', '.jpg', '.jpeg', '.webp',
         '.gif', '.heic', '.tif', '.tiff', '.psd', '.ttf', '.otf', '.woff', '.woff2', '.pack'}
XOA_HAN = {'node_modules', '.remotion', '.cache'}
MOVIES = os.path.realpath(os.path.expanduser('~/Movies'))
VLOG = os.path.join(MOVIES, 'vlog')
KICH_BAN = {'danh-sach-cat.js', 'canh.js', 'phu-de.js', 'du-an.js', 'plan.json', 'cuts.json'}   # sửa sau bản cuối mà chưa render = đang làm lại
GOC_VLOG = set()   # gốc các dự án vlog ghép (bản cuối nằm ngay ở gốc)


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
    return d in GOC_VLOG or b == '2-ban-day-du' or (b.startswith('clip-') and os.path.basename(os.path.dirname(d)) == '3-doan-noi-bat')


DO = {}   # dự án đang dở → lý do


def dang_chay(T):
    o = subprocess.run(['pgrep', '-fl', T], capture_output=True, text=True).stdout.strip()
    return [l for l in o.splitlines() if 'don-tap.py' not in l]


def quet(T):
    bo_qua, xoa_han, rac = [], [], []
    # dự án chưa có bản cuối → bỏ qua cả thư mục (3-doan-noi-bat: một clip thiếu thì giữ nguồn chung)
    for r, ds, fs in os.walk(T):
        ds[:] = [d for d in ds if d not in XOA_HAN]
        if la_du_an(r) and 'video-final.mp4' not in fs:
            bo_qua.append(r)
    # việc đang dở: tiến trình đang chạy trong dự án, hoặc file chữ sửa sau bản cuối (bỏ qua phat-hanh/, so-lieu: sửa sau là bình thường)
    for r, ds, fs in os.walk(T):
        ds[:] = [d for d in ds if d not in XOA_HAN]
        if la_du_an(r) and 'video-final.mp4' in fs and r not in bo_qua:
            mf = os.path.getmtime(os.path.join(r, 'video-final.mp4'))
            moi = []
            for r2, ds2, fs2 in os.walk(r):
                ds2[:] = [d for d in ds2 if d not in XOA_HAN and d != 'phat-hanh']
                moi += [os.path.join(r2, f) for f in fs2 if f in KICH_BAN and os.path.getmtime(os.path.join(r2, f)) > mf + 120]
            if moi:
                bo_qua.append(r); DO[r] = f'{len(moi)} file sửa sau bản cuối, vd. {os.path.relpath(moi[0], r)}'
    hl = os.path.join(T, '3-doan-noi-bat')
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
        la_tap = os.path.dirname(T) == MOVIES and ten.startswith('tap-')
        la_vlog = os.path.dirname(T) == VLOG
        if not (la_tap or la_vlog) or not os.path.isdir(T):
            print(f'✗ {T}: chỉ dọn ~/Movies/tap-<tên> hoặc ~/Movies/vlog/<tên> — bỏ qua'); continue
        if la_vlog: GOC_VLOG.add(T)
        ch = dang_chay(T)
        if ch:
            print(f'\n== {ten}: ⏸ BỎ QUA CẢ DỰ ÁN — có tiến trình đang chạy (phiên khác đang làm?) → hỏi David\n   ' + '\n   '.join(ch[:3])); continue
        bo_qua, xoa_han, rac = quet(T)
        s_han = sum(du(p) for p in xoa_han)
        s_rac = sum(os.lstat(p).st_size for p in rac)
        # file liên kết cứng với nơi khác (vd. 1-goc) không giải phóng chỗ
        s_that = sum(os.lstat(p).st_size for p in rac if os.lstat(p).st_nlink == 1)
        tong += s_han + s_that
        print(f'\n== {ten}: {co(du(T))} → giải phóng ~{co(s_han + s_that)}')
        for b in bo_qua:
            print(f'   ⏸ bỏ qua {os.path.relpath(b, T) if b != T else "cả dự án"}/ ({DO.get(b, "chưa có video-final.mp4")}) → hỏi David')
        if xoa_han:
            print(f'   xoá hẳn  {co(s_han):>9}  node_modules / .remotion / .cache ({len(xoa_han)} thư mục)')
        nhom = {}
        for p in rac:
            k = os.path.relpath(os.path.dirname(p), T).split(os.sep)
            k = os.sep.join(k[:3])
            n = nhom.setdefault(k, [0, 0]); n[0] += 1; n[1] += os.lstat(p).st_size
        for k, (n, s) in sorted(nhom.items(), key=lambda x: -x[1][1]):
            print(f'   xoá tạm  {co(s):>9}  {k}/ ({n} file)')
        if thuc:
            for p in xoa_han: shutil.rmtree(p, ignore_errors=True)
            for p in rac:
                try: os.remove(p)
                except OSError: pass
            for r, ds, fs in os.walk(T, topdown=False):   # bỏ thư mục rỗng
                if r != T and not os.listdir(r):
                    try: os.rmdir(r)
                    except OSError: pass
            if xoa_han or rac: print('   ✓ đã dọn file tạm')
            if not bo_qua: print(f'   → tiếp: zsh {os.path.dirname(os.path.abspath(__file__))}/luu-drive.sh "{T}"   (chạy nền)')
    print(f'\nTổng giải phóng ~{co(tong)}' + ('' if thuc else ' (CHƯA làm gì — chỉ liệt kê)')
          )


main()
