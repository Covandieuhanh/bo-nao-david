#!/usr/bin/env python3
"""Người dọn kho skill (học từ "curator" của Hermes), không gọi AI: đếm skill nào được dùng, skill nào lâu không dùng,
skill nào bị David sửa nhiều; in bảng ngắn cho skill hoc-lien-tuc. Nguồn: ~/.claude/hoc-lien-tuc/tin-hieu.jsonl + danh sách skill trong repo.
Dùng: python3 -I dem-ky-nang.py [số ngày, mặc định 30]"""
import datetime as dt, glob, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TH = os.path.expanduser("~/.claude/hoc-lien-tuc/tin-hieu.jsonl")
# Tên cũ → tên hiện hành (đổi tên skill thì thêm một dòng ở đây, để tín hiệu cũ vẫn đếm đúng skill).
TEN_CU = {"dang-da-kenh": "phan-phoi-da-kenh", "video-style-edit": "dung-video-theo-phong-cach",
          "hoi-chuyen-gia": "thu-thap-yeu-cau"}


def main():
    ngay = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    tu = (dt.datetime.now() - dt.timedelta(days=ngay)).strftime("%Y-%m-%d")
    co = sorted({os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{REPO}/ky-nang/**/SKILL.md", recursive=True)})
    dung, sua, ngoai, loi = {k: 0 for k in co}, {}, {}, {}
    try:
        dong = open(TH, encoding="utf-8").read().splitlines()
    except OSError:
        dong = []
    theo_phien = {}  # một phiên có thể được ghi nhiều lần (mở lại, tóm tắt): giữ dòng cuối
    for l in dong:
        try:
            o = json.loads(l)
        except Exception:
            continue
        if o.get("luc", "") >= tu:
            theo_phien[o.get("phien") or l] = o
    for o in theo_phien.values():
        for k, n in (o.get("skill") or {}).items():
            k = TEN_CU.get(k.split(":")[-1], k.split(":")[-1])
            dich = dung if k in dung else ngoai
            dich[k] = dich.get(k, 0) + n
            if o.get("david_sua"):
                sua[k] = sua.get(k, 0) + len(o["david_sua"])
        for c, n in (o.get("loi_theo_cong_cu") or {}).items():
            loi[c] = loi.get(c, 0) + n
    print(f"Skill trong {ngay} ngày qua ({len(theo_phien)} phiên có tín hiệu, đã gộp dòng trùng):")
    for k in sorted(dung, key=lambda x: -dung[x]):
        nhan = "  ← không dùng" if dung[k] == 0 else ""
        print(f"- {k}: dùng {dung[k]} lần, David sửa trong phiên đó {sua.get(k, 0)} câu{nhan}")
    if ngoai:
        print("Skill có sẵn của Claude (ngoài bộ): " + ", ".join(f"{k} {n}" for k, n in sorted(ngoai.items(), key=lambda x: -x[1])))
    if loi:
        print("Lỗi công cụ theo tên: " + ", ".join(f"{k} {n}" for k, n in sorted(loi.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
