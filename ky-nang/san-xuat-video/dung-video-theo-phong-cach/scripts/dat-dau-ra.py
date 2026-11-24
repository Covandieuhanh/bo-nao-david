# Đổi khung xuất: dat-dau-ra.py <dự án> pillar|same
#   pillar: gốc dọc → xuất ngang 1920×1080 (video giữa, hai bên chữ) — ghi chuyen-dong/src/dau-ra.js
#   same:   xuất cùng khung video gốc (mặc định)
# Gốc ngang → xuất dọc KHÔNG dùng file này: chạy phan-tich-doi-khung.sh + ke-hoach-doi-khung.py (biến video gốc thành dọc).
import os, sys

P, mode = os.path.expanduser(sys.argv[1]), sys.argv[2]
val = "{layout: 'pillar', width: 1920, height: 1080, base: 'nen-ngang.mp4'}" if mode == "pillar" else "null"
open(os.path.join(P, "chuyen-dong", "src", "dau-ra.js"), "w").write(
    "// Khung xuất khi KHÁC khung video gốc — scripts/dat-dau-ra.py tự điền. null = xuất cùng khung với video gốc.\n"
    f"export default {val};\n")
print("output:", val)
