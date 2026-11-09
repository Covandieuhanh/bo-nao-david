#!/usr/bin/env python3
"""RÀ SOÁT SKILL ĐỔI SAU KHI CHẠY: ra_soat.py <tên việc>
Với mỗi bước ĐÃ CHẠY của một dự án, cho biết skill có đổi sau lúc bước đó chạy không — để David biết nên "làm lại từ" bước nào.
  · Bước AI: file skill / khối mà phiếu bước nhắc tới, đổi sau lúc bước chạy.
  · Bước máy: các script bước đó gọi (kể cả script nó gọi tiếp, một tầng) + hồ sơ tham số nếu script đọc hồ sơ, có sửa sau lúc chạy không.
  · Phần hình: khung dựng của dự án khác bản mới nhất của skill → gợi ý "Cập nhật khung dựng".
Tiến trình khác sửa skill (phiên Claude Code khác, sync GitHub) đều được thấy vì app và skill dùng chung một thư mục."""
import json, re, sys
from pathlib import Path

APP = Path(__file__).resolve().parent; DV = APP.parent
sys.path.insert(0, str(APP)); sys.path.insert(0, str(APP / "ap"))
import chay, cap_nhat_khung  # noqa: E402

THU_MUC_SCRIPT = [DV / "video-style-edit/scripts", DV / "cat-highlight-video/scripts", APP / "ap", APP / "kiem", DV / "khoi"]


def _ten_script(text):
    return set(re.findall(r"([\w-]+\.(?:py|sh|mjs))", text))


def _tim(ten):
    return [d / ten for d in THU_MUC_SCRIPT if (d / ten).is_file()]


def phu_thuoc_may(ph, b):
    """Tệp skill mà một bước máy dùng: script trong lệnh + script chúng gọi tiếp (một tầng) + hồ sơ nếu có đọc hồ sơ."""
    lenh = " ".join(ph["lenh"] if isinstance(ph["lenh"], list) else [ph["lenh"]])
    lenh = chay.thay(lenh, b)
    tep = {Path(x) for x in re.findall(r"(/[^\s'\"]+\.(?:py|sh|mjs))", lenh) if Path(x).is_file() and str(DV) in x}
    for f in list(tep):
        t = f.read_text(encoding="utf-8", errors="ignore")
        for ten in _ten_script(t):
            tep.update(_tim(ten))
        if "hoso" in t or "ho-so" in t:
            tep.update((DV / "ho-so").glob("*.json"))
    if ph["id"] == "kiem":
        tep.update((APP / "kiem").glob("kiem_*.py"))
    tep.update(Path(chay.thay(x, b)) for x in ph.get("phu_thuoc", []))
    return {f for f in tep if f.exists()}


def ra_soat(ten):
    W = chay.KHO / ten; tt = chay.doc(W / "trang-thai.json"); b = chay.bien(tt)
    cu = []
    for bid in chay.cong_thuc(tt["cong_thuc"])["buoc"]:
        st = tt["buoc"].get(bid, {})
        if st.get("trang_thai") not in ("xong", "loi") or not st.get("ts"):
            continue
        ph = chay.phieu(bid)
        if ph["loai"] == "ai":   # bước AI: skill/khối mà phiếu bước nhắc tới, đổi sau lúc bước chạy
            ten_tep = set(re.findall(r"((?:khoi|trinh-bay|ho-so|video-style-edit|dang-da-kenh|cat-highlight-video|podcast-style-edit)/[\w./-]+\.(?:md|json)|luat-chung\.md)", ph["viec"]))
            doi = [DV / x for x in ten_tep if (DV / x).exists() and (DV / x).stat().st_mtime > st["ts"]]
            if doi:
                cu.append({"id": bid, "ten": ph.get("ten", bid), "tep": sorted(str(x.relative_to(DV)) for x in doi)})
        elif ph["loai"] == "co-dinh":
            doi = [x for x in phu_thuoc_may(ph, b) if x.stat().st_mtime > st["ts"]]
            if doi:
                cu.append({"id": bid, "ten": ph.get("ten", bid), "tep": sorted(str(x.relative_to(DV)) for x in doi)})
    khung = []
    if (Path(tt["P"]) / "motion/src").is_dir():
        khung = [t for *_, t in cap_nhat_khung.khac_biet(tt["P"])]
    return {"buoc_cu": cu, "khung_cu": khung}


if __name__ == "__main__":
    print(json.dumps(ra_soat(sys.argv[1]), ensure_ascii=False, indent=1))
