#!/usr/bin/env python3
"""Bảng thay từ khẩu ngữ → thuật ngữ chuẩn (nguồn duy nhất: co-so-tri-thuc/bang-thuat-ngu.md mục "Thuật ngữ trong văn bản").
Dùng bởi kiem-ngon-tu.py (quét, và --sua để thay). Không đụng vào lời trích trong ngoặc kép (lời David, lời nguồn) và dòng trích dẫn (> ).
Thêm từ mới: thêm một cặp vào THAY (thứ tự: cụm dài trước cụm ngắn) và một dòng vào bảng thuật ngữ."""
import re

# (từ cũ, từ chuẩn) — cụm dài đứng trước cụm ngắn cùng gốc
THAY = [
 ('Không móc được vào', 'Không liên kết được với'), ('móc được vào', 'liên kết được với'), ('móc vào', 'liên kết với'), ('Móc vào', 'Liên kết với'),
 ('Nhà duy nhất của', 'Nguồn duy nhất của'), ('nhà duy nhất của', 'nguồn duy nhất của'), ('nhà duy nhất', 'nguồn duy nhất'), ('Nhà duy nhất', 'Nguồn duy nhất'),
 ('Một ý một nhà', 'Một ý một nguồn duy nhất'), ('một ý một nhà', 'một ý một nguồn duy nhất'), ('mỗi ý chỉ **một nhà**', 'mỗi ý chỉ **một nguồn duy nhất**'),
 ('mỗi ý một nhà', 'mỗi ý một nguồn duy nhất'), ('Mỗi ý một nhà', 'Mỗi ý một nguồn duy nhất'), ('một nhà', 'một nguồn duy nhất'), ('Một nhà', 'Một nguồn duy nhất'),
 ('nhà của', 'nguồn của'), ('Nhà của', 'Nguồn của'), ('Nhà: `', 'Nguồn duy nhất: `'), ('nhà: `', 'nguồn duy nhất: `'), ('(nhà: ', '(nguồn duy nhất: '),
 ('Đã có nhà chưa?', 'Đã có nguồn duy nhất chưa?'), ('có nhà trong', 'có nguồn trong'), ('có nhà', 'có nguồn duy nhất'), ('nhà mới ở', 'nguồn mới ở'), ('nhà mới', 'nguồn mới'),
 ('Đề xuất nhà:', 'Đề xuất nguồn:'), ('nhà nên ở', 'nguồn nên ở'), ('thiếu nhà', 'thiếu nguồn'), ('mất nhà', 'mất nguồn'), ('nhà ở `', 'nguồn ở `'), ('nhà ở khối', 'nguồn ở khối'), ('nhà ở quy-tac', 'nguồn ở quy-tac'), ('nay nhà ở', 'nay nguồn ở'), ('nhà chính', 'nguồn chính'), ('nhà luật', 'nguồn luật'), ('nhà chi tiết', 'nguồn chi tiết'), ('Gộp nhà', 'Gộp nguồn'), ('chốt nhà', 'chốt nguồn'), ('theo nhà', 'theo nguồn'), ('(nhà)', '(nguồn)'), ('đúng nhà', 'đúng nguồn'), ('nhiều nhà', 'nhiều nguồn'), ('nhà chung', 'nguồn chung'), ('nhà riêng của luật', 'nguồn riêng của luật'), ('về nhà nào', 'về nguồn nào'), ('nhà nào', 'nguồn nào'),
 ('Luật đi lên', 'Luật thăng cấp'), ('luật đi lên', 'luật thăng cấp'), ('đi lên tầng', 'thăng cấp lên tầng'), ('biểu đồ đi lên', 'biểu đồ tăng'),
 ('→ tỉa →', '→ cắt giảm →'), ('chưng cất, tỉa, dọn', 'chưng cất, cắt giảm, tái cấu trúc'), ('đề xuất tỉa', 'đề xuất cắt giảm'), ('tỉa:', 'cắt giảm:'), ('Tỉa:', 'Cắt giảm:'), ('(tỉa)', '(cắt giảm)'),
 ('máy gác cổng', 'cổng kiểm soát'), ('Máy gác cổng', 'Cổng kiểm soát'), ('gác cổng', 'cổng kiểm soát'),
 ('người đọc lạnh', 'người đọc mới'), ('Người đọc lạnh', 'Người đọc mới'), ('xem lạnh', 'xem với góc nhìn mới'),
 ('Đến tận nơi xem', 'Kiểm tra tại hiện trường'), ('đến tận nơi xem', 'kiểm tra tại hiện trường'),
 ('sửa tay', 'sửa thủ công'), ('Sửa tay', 'Sửa thủ công'), ('làm tay', 'làm thủ công'), ('ép tay', 'chỉ định thủ công'), ('Ép tay', 'Chỉ định thủ công'), ('bằng tay', 'thủ công'), ('gộp tay', 'gộp thủ công'),
 ('máy kiểm', 'công cụ kiểm tra'), ('Máy kiểm', 'Công cụ kiểm tra'), ('MÁY KIỂM', 'CÔNG CỤ KIỂM TRA'), ('máy chấm', 'công cụ chấm'), ('Máy chấm', 'Công cụ chấm'), ('máy đo', 'công cụ đo'), ('Máy đo', 'Công cụ đo'),
 ('luật đang sống', 'luật hiện hành'), ('Luật đang sống', 'Luật hiện hành'), ('đang sống', 'hiện hành'), ('cùng sống', 'cùng tồn tại'),
 ('câu đắt nhất', 'câu then chốt'), ('câu đắt', 'câu then chốt'), ('Câu đắt', 'Câu then chốt'),
 ('chỗ vấp', 'lỗi đã gặp'), ('chỗ kẹt', 'vướng mắc'), ('Chỗ kẹt', 'Vướng mắc'), ('kẹt ở', 'vướng ở'), ('kẹt việc', 'vướng việc'), ('bị kẹt', 'bị vướng'), ('đang kẹt', 'đang vướng'), ('kẹt', 'vướng'),
 ('làm dở', 'làm chưa xong'), ('Làm dở', 'Làm chưa xong'),
 ('giữ Mac nhẹ', 'giữ dung lượng Mac thấp'), ('Giữ Mac nhẹ', 'Giữ dung lượng Mac thấp'), ('nhẹ máy', 'giải phóng dung lượng máy'), ('nhẹ bộ nhớ', 'giải phóng dung lượng'),
 ('bịa ca', 'bịa đặt trường hợp'), ('bịa', 'bịa đặt'), ('Bịa', 'Bịa đặt'), ('trôi nổi', 'không rõ nguồn gốc'),
 ('file quá nặng', 'file dung lượng quá lớn'), ('file nặng', 'file dung lượng lớn'), ('dựng nặng', 'dựng công phu'),
 ('đụng tới', 'liên quan tới'), ('đụng luật', 'xung đột với luật'), ('đụng tài khoản', 'thao tác tài khoản'), ('đụng skill', 'trùng skill'), ('đụng bộ khác', 'xung đột với bộ khác'), ('đụng David', 'cần David'), ('việc đụng', 'việc liên quan'),
 ('dính tới', 'liên quan tới'), ('dính lỗi', 'mắc lỗi'), ('cũng dính)', 'cũng mắc lỗi)'),
 ('soi bằng', 'xét bằng'), ('Cách soi', 'Cách xét'), ('soi mục tiêu', 'xét mục tiêu'), ('tự soi lỗi', 'tự kiểm lỗi'), ('soi lỗi', 'kiểm lỗi'), ('soi cảnh', 'kiểm cảnh'), ('soi chữ', 'kiểm chữ'), ('soi phụ đề', 'kiểm phụ đề'), ('soi lại', 'kiểm lại'),
 ('lọt qua', 'bị bỏ sót'), ('để lọt', 'bỏ sót'), ('lọt', 'tràn'),
 ('ca thật', 'trường hợp thực tế'), ('Ca thật', 'Trường hợp thực tế'), ('ca mẫu', 'trường hợp mẫu'), ('Ca mẫu', 'Trường hợp mẫu'), ('ca khách', 'trường hợp khách'), ('Ca khách', 'Trường hợp khách'), ('ca cùng gốc', 'trường hợp cùng gốc'),
 ('số cứng', 'số cố định'), ('lịch cứng', 'lịch cố định'), ('mốc cứng', 'mốc cố định'), ('giới hạn cứng', 'giới hạn cố định'),
 ('bắt chước', 'học theo'), ('Bắt chước', 'Học theo'), ('mối nối', 'điểm nối'), ('Mối nối', 'Điểm nối'),
]
REGEX = [
 (r'\b(các|một|nhiều|từng|mỗi|\d+) ca\b', r'\1 trường hợp'), (r'\b(Các|Một|Nhiều|Từng|Mỗi) ca\b', r'\1 trường hợp'),
 (r'\bkhúc\b', 'phân đoạn'), (r'\bKhúc\b', 'Phân đoạn'),
 (r'\bkhuôn\b', 'mẫu'), (r'\bKhuôn\b', 'Mẫu'),
]
# cụm giữ nguyên (không phải khẩu ngữ, hoặc nghĩa khác): thay bằng dấu giữ chỗ trước, trả lại sau
GIU = ['bịa đặt', 'nhà ở xã hội', 'khuôn hình', 'khuôn mặt', 'khuôn khổ', 'khuôn mẫu', 'Khuôn hình', 'Khuôn mặt', 'ca khúc', 'băng dính', 'phần cứng', 'cắt cứng', 'liên kết cứng', 'soi gương', 'soi tỏ', 'kiem-ngon-tu', 'soat', 'soi-']
# từ cũ để quét (chỉ báo, không thay): cụm còn sót sau khi thay
TU_CU = ['móc vào', 'nhà duy nhất', 'một nhà', 'nhà của', 'luật đi lên', 'gác cổng', 'người đọc lạnh', 'đến tận nơi xem', 'sửa tay', 'ép tay', 'bằng tay',
         'máy kiểm', 'máy đo', 'máy chấm', 'đang sống', 'câu đắt', 'chỗ vấp', 'chỗ kẹt', 'làm dở', 'nhẹ máy', 'giữ mac nhẹ', 'trôi nổi', 'file nặng', 'đụng tới',
         'dính tới', 'soi bằng', 'lọt qua', 'ca thật', 'ca mẫu', 'số cứng', 'lịch cứng', 'bắt chước', 'mối nối', 'chỗ kẹt', 'nhà nên ở', 'đề xuất nhà']

_Q = re.compile(r'("[^"]*"|“[^”]*”|`[^`]*`)')   # lời trích và mã inline: giữ nguyên

def _thay_doan(s):
    for i, g in enumerate(GIU): s = s.replace(g, f'\x00{i}\x00')
    for a, b in THAY: s = s.replace(a, b)
    for a, b in REGEX: s = re.sub(a, b, s)
    for i, g in enumerate(GIU): s = s.replace(f'\x00{i}\x00', g)
    return s

def thay_dong(d, bao_ve_trich=True):
    if bao_ve_trich and d.lstrip().startswith('>'): return d
    if not bao_ve_trich: return _thay_doan(d)
    phan = _Q.split(d)
    return ''.join(p if i % 2 else _thay_doan(p) for i, p in enumerate(phan))

def dong_ap_dung(d, loai):
    """Dòng nào được thay/quét: file mã chỉ chú thích và thông báo; file khác mọi dòng."""
    if loai != 'code': return True
    t = d.lstrip()
    return t.startswith(('#', '//', '"""', '* ', '/*')) or 'print(' in d or 'echo ' in d or 'sys.exit(' in d or 'console.log(' in d

def thay_van_ban(s, loai):
    """loai: 'md' (bảo vệ trích), 'json' (thay hết trong chuỗi), 'code' (chỉ dòng chú thích và thông báo)."""
    ra = []
    for d in s.split('\n'):
        t = d.lstrip()
        if loai == 'code':
            ra.append(thay_dong(d, bao_ve_trich=False) if dong_ap_dung(d, loai) else d)
        elif loai == 'json': ra.append(thay_dong(d, bao_ve_trich=False))
        else: ra.append(thay_dong(d, bao_ve_trich=True))
    return '\n'.join(ra)
