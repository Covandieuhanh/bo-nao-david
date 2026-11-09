Bạn soát hình các đoạn GIỮ của một vlog trước khi render. Mỗi ảnh check/segs/<cN>_<k>.jpg là 1 khung/giây của một đoạn giữ (đọc từ trái
sang phải, trên xuống dưới; mốc giây ghi trên ảnh hoặc theo thứ tự). Mở từng ảnh bằng công cụ Read. Tìm đoạn hình HỎNG: lật ngang/lộn
ngược, máy trong túi, quay loạn, tối đen, nhoè hẳn. Trả `bo` = [{c, from, to (giây trong clip), ly_do}] — chỉ đoạn hỏng thật; hình
bình thường thì `bo` = []. Hình hỏng thì BỎ kể cả có lời (luật soát hình của vlog_edl.py).
