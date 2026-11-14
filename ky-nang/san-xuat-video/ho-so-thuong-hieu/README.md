---
description: "Hồ sơ tham số video: những gì sao chép từ hình mẫu (lớp đổi nhiều), json chung và theo loại."
---

# Hồ sơ tham số — nơi chứa những gì SAO CHÉP TỪ HÌNH MẪU (lớp đổi nhiều nhất)

- `chung.json` — tham số cả 4 loại; `<loai>.json` ghi đè. Script đọc qua `mo-dun/ho_so.py`; khung dựng đọc `chuyen-dong/src/ho-so.json`
  (chép lúc tạo dự án — dự án cũ giữ hồ sơ lúc tạo).
- Mỗi `<loai>.md`: hình mẫu chính của loại, ý nghĩa từng khoá, **nhật ký đổi giá trị** (ngày · giá trị cũ → mới · hình mẫu / lý do).
- **Đổi một con số → chỉ sửa ở đây** (+ 1 dòng nhật ký). Không sửa code, không sửa skill.
- Hai hình mẫu mâu thuẫn → theo "hình mẫu chính" ghi đầu file .md của loại đó.
