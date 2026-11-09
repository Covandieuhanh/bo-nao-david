"""Sửa rồi AI xem lại ảnh mới. Hết số vòng vẫn chưa đạt: dừng, không giao như đã đạt."""
import json, time, os
from pathlib import Path

def chay(tt, ph, log, mot_buoc, bien, chay_lenh, thay):
    b = bien(tt); W = Path(b["W"]); review = ph["duyet_lai"]
    result = W / ("duyet-chup-thu.json" if "chup-thu" in review else "duyet-hinh.json")
    folder = W / "duyet-chat-luong" / review; folder.mkdir(parents=True, exist_ok=True)
    for lan in range(ph.get("so_vong_sua", 2) + 1):
        kq = json.loads(result.read_text())
        (folder / f"{time.time_ns()}-{lan}.json").write_text(json.dumps(kq, ensure_ascii=False, indent=1))
        if kq.get("can_xu_ly_ngoai_ke_hoach"):
            with open(log,"a") as f: f.write("\nCần sửa ngoài kế hoạch cảnh: " + "; ".join(kq["can_xu_ly_ngoai_ke_hoach"]) + "\n")
            return "loi"
        if kq.get("dat") is True:
            (W / ("duyet-chup-thu.md" if "chup-thu" in review else "duyet-hinh.md")).write_text("# AI duyệt chất lượng\n\n✅ Đã xem và đạt trên bản hiện tại.\n\n" + kq.get("nhan_xet", ""))
            return "xong"
        if lan == ph.get("so_vong_sua", 2):
            with open(log, "a") as f: f.write("\nCHƯA ĐẠT sau các vòng sửa. Dừng để xử lý, chưa chuyển sang phát hành hoặc David duyệt.\n")
            return "loi"
        if not kq.get("ke_hoach"):
            with open(log, "a") as f: f.write("\nAI chưa đạt nhưng thiếu kế hoạch sửa; cần sửa khuôn hoặc code.\n")
            return "loi"
        commands = ph["lenh"] if isinstance(ph["lenh"], list) else [ph["lenh"]]
        for command in commands:
            if chay_lenh(thay(command, b), log) != 0: return "loi"
        # Cùng validator + cache đầu vào/ảnh của bước gốc. Ảnh mới khác → phải đánh giá lại.
        old = os.environ.get("APP_DUYET_MOI")
        os.environ["APP_DUYET_MOI"] = "1"
        try:
            if mot_buoc(tt, review) != "xong": return "loi"
        finally:
            if old is None: os.environ.pop("APP_DUYET_MOI", None)
            else: os.environ["APP_DUYET_MOI"] = old
    return "loi"
