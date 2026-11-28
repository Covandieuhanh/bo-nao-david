#!/usr/bin/env python3
"""Chặn hiệu ứng tự chế, không có hình mẫu (David 28/11/2026: "đã học từ hình mẫu thì mọi thứ chuẩn đúng theo hình mẫu …
đừng sáng tạo và thêm linh tinh nữa" — chỉ giữ hiệu ứng có mẫu).

  python3 -I kiem-hieu-ung-co-mau.py <canh.js>

Đọc danh sách lưu trữ ở thiet-ke-bo-cuc/hieu-ung-luu-tru.json. In cảnh dùng hiệu ứng lưu trữ (lỗi) và cảnh dùng hiệu ứng có mẫu nhưng
chưa đo giao diện (cảnh báo). Mã thoát 1 nếu có lỗi. Sửa: chọn hiệu ứng có mẫu hợp nội dung, không có thì để người và phụ đề.
"""
import json, os, re, subprocess, sys

GOC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # ky-nang/san-xuat-video
LUU = json.load(open(os.path.join(GOC, 'thiet-ke-bo-cuc', 'hieu-ung-luu-tru.json'), encoding='utf-8'))


def doc_canh(p):
    js = open(p, encoding='utf-8').read()
    k = re.search(r'export const SCENES = (\[.*?\n\]);', js, flags=re.S).group(1)
    try:
        return json.loads(k)
    except ValueError:
        r = subprocess.run(['node', '-e', 'process.stdout.write(JSON.stringify(' + k + '))'], capture_output=True, text=True)
        return json.loads(r.stdout)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    loi, bao = [], []
    for c in doc_canh(sys.argv[1]):
        t, p = c['type'], c.get('props', {})
        if t in LUU['loai']:
            loi.append(f"{c['id']}: loại '{t}' tự chế, không có mẫu")
        elif t == 've' and p.get('ve') in LUU['ve']:
            loi.append(f"{c['id']}: cảnh tự vẽ '{p['ve']}' không có mẫu")
        elif t == 've' and p.get('ve') == 'DuongMay' and not (p.get('ten_the') or p.get('cau')):
            loi.append(f"{c['id']}: DuongMay chỉ còn thẻ tên và câu đắt (mẫu The Diary Of A CEO); kiểu này tự chế")
        if t == 'bocuc' and isinstance(p.get('noi_dung'), dict) and p['noi_dung'].get('type') in LUU['loai']:
            loi.append(f"{c['id']}: nội dung lồng '{p['noi_dung']['type']}' tự chế, không có mẫu")
        k = f"{t}:{p.get('kieu', 'o-nguoi')}" if t == 'bocuc' else ''
        if k in LUU['chua_do_mau']:
            bao.append(f"{c['id']}: {k} chưa đo giao diện mẫu ({LUU['chua_do_mau'][k]})")
    for x in loi:
        print('!  ' + x)
    for x in bao:
        print('?  ' + x)
    print(f"Hiệu ứng không có mẫu: {len(loi)} · chưa đo mẫu: {len(bao)}")
    sys.exit(1 if loi else 0)


if __name__ == '__main__':
    main()
