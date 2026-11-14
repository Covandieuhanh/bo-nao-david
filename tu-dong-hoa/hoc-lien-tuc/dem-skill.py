#!/usr/bin/env python3
"""Người dọn kho skill (học từ "curator" của Hermes), không gọi AI: đếm skill nào được dùng, skill nào lâu không dùng,
skill nào bị David sửa nhiều; in bảng ngắn cho skill hoc-lien-tuc. Nguồn: ~/.claude/hoc-lien-tuc/tin-hieu.jsonl + danh sách skill trong repo.
Dùng: python3 -I dem-skill.py [số ngày, mặc định 30]"""
import datetime as dt, glob, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TH = os.path.expanduser("~/.claude/hoc-lien-tuc/tin-hieu.jsonl")


def main():
    ngay = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    tu = (dt.datetime.now() - dt.timedelta(days=ngay)).strftime("%Y-%m-%d")
    co = sorted({os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{REPO}/ky-nang/**/SKILL.md", recursive=True)})
    dung, sua, phien = {k: 0 for k in co}, {}, 0
    try:
        dong = open(TH, encoding="utf-8").read().splitlines()
    except OSError:
        dong = []
    for l in dong:
        try:
            o = json.loads(l)
        except Exception:
            continue
        if o.get("luc", "") < tu:
            continue
        phien += 1
        for k, n in (o.get("skill") or {}).items():
            k = k.split(":")[-1]
            dung[k] = dung.get(k, 0) + n
            if o.get("david_sua"):
                sua[k] = sua.get(k, 0) + len(o["david_sua"])
    print(f"Skill trong {ngay} ngày qua ({phien} phiên có tín hiệu):")
    for k in sorted(dung, key=lambda x: -dung[x]):
        nhan = "  ← không dùng" if dung[k] == 0 else ""
        print(f"- {k}: dùng {dung[k]} lần, David sửa trong phiên đó {sua.get(k, 0)} câu{nhan}")


if __name__ == "__main__":
    main()
