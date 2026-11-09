#!/usr/bin/env python3
"""ÁP PHƯƠNG ÁN HIGHLIGHT: ap_chon_y.py <dự án highlight> <chon-y.json> [--kiem]
Claude chọn ý theo 4 câu và TRÍCH câu (trich_dau / trich_cuoi); script tìm mốc trong check/goc/words.srt → phuong-an.json đúng khuôn
của skill (cut_highlight.py, loud_check.py, hl_edl.py đọc) + ke-hoach-cat.md (4 câu chọn ý + lời đọc nối + mốc, để David đối chiếu).
Soát: câu trích tìm được, thứ tự trong câu đúng, tít và câu màn chốt nguyên văn, câu màn chốt ≤ 55 ký tự, đủ 4 câu chọn ý."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import loi  # noqa: E402

VAI = {"CHAM", "BOICANH", "BUOC", "HANHDONG", "KEUGOI", "KETQUA", "CHUYEN"}


def mm(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


def main():
    H, kp = Path(sys.argv[1]), sys.argv[2]; kiem = "--kiem" in sys.argv
    kh = json.loads(Path(kp).read_text(encoding="utf-8"))
    T = loi.tu(H / "check/goc/words.srt"); W_ = loi.doc_srt(H / "check/goc/words.srt")
    sua = frozenset(t for x in kh.get("sua_chu", []) for t in loi.chuan(x.get("dung", "")))
    loi_ds = []; ra = {"options": [], "endcard": kh.get("endcard") or {}}
    if not (kh.get("endcard") or {}).get("title"):
        loi_ds.append("thiếu endcard.title (tên tập gốc, chữ của bản gốc) cho thẻ cuối 'Bản đầy đủ trên kênh …'")
    ids = set()
    for o in kh.get("options", []):
        oid = o.get("id", "?")
        if oid in ids: loi_ds.append(f"trùng mã phương án {oid}")
        ids.add(oid)
        for k in ("boi_canh", "y_tron", "mang_ve", "chua_lai"):
            if not (o.get("chon_y") or {}).get(k):
                loi_ds.append(f"{oid}: thiếu câu chọn ý `{k}` — thiếu một câu thì chọn lại ý (luật gốc của skill)")
        if o.get("tit") and loi.co_trong_loi(o["tit"], T, 0, 1e9, 0, them=sua) < 0.85:
            loi_ds.append(f"{oid}: tít «{o['tit']}» không phải nguyên văn — tít là cụm nguyên văn đắt nhất của clip")
        pieces = []
        for i, p in enumerate(o.get("pieces", []), 1):
            a = loi.tim(p.get("trich_dau", ""), T)
            if not a:
                loi_ds.append(f"{oid} câu {i}: không tìm thấy trich_dau «{p.get('trich_dau')}»"); continue
            b = loi.tim(p.get("trich_cuoi", ""), T, sau=a[0], gan=a[0])
            if not b or b[1] <= a[0]:
                loi_ds.append(f"{oid} câu {i}: không tìm thấy trich_cuoi «{p.get('trich_cuoi')}» sau trich_dau"); continue
            if p.get("role") not in VAI:
                loi_ds.append(f"{oid} câu {i}: role '{p.get('role')}' không có (chỉ: {sorted(VAI)})")
            text = " ".join(t for s, e, t in W_ if a[0] - 0.01 <= s < b[1] - 0.01).strip()   # tới HẾT cụm trích cuối
            x = {"start": round(a[0], 2), "end": round(b[1], 2), "role": p.get("role"), "tone": p.get("tone", "soi"), "text": text}
            for k in ("zoom", "cta"):
                if p.get(k): x[k] = True
            if p.get("cta_text"):
                if len(p["cta_text"].replace("**", "")) > 55:
                    loi_ds.append(f"{oid} câu {i}: cta_text dài {len(p['cta_text'])} ký tự > 55 — chọn vế trọn ý, nguyên văn")
                if loi.co_trong_loi(p["cta_text"], T, a[0], b[1], them=sua) < 0.85:
                    loi_ds.append(f"{oid} câu {i}: cta_text «{p['cta_text']}» không nguyên văn câu này")
                x["cta_text"] = p["cta_text"]
            pieces.append(x)
        if not pieces:
            loi_ds.append(f"{oid}: không có câu nào"); continue
        ra["options"].append({**{k: v for k, v in o.items() if k not in ("pieces",)}, "pieces": pieces})
    if not ra["options"]:
        loi_ds.append("không có phương án nào")
    print(f"{len(ra['options'])} clip · {sum(len(o['pieces']) for o in ra['options'])} câu · {len(loi_ds)} lỗi")
    for x in loi_ds: print("✗", x)
    if loi_ds: sys.exit(1)
    if kiem: return
    (H / "phuong-an.json").write_text(json.dumps(ra, ensure_ascii=False, indent=1), encoding="utf-8")
    d = [f"# Kế hoạch cắt highlight — {H.parent.name}", "", f"Thẻ cuối: «Bản đầy đủ trên kênh …» · tập gốc **{ra['endcard'].get('title')}**", ""]
    for o in ra["options"]:
        dai = sum(p["end"] - p["start"] for p in o["pieces"])
        d += [f"## Clip {o['id']} — tít «{o.get('tit', '')}» · ~{dai:.0f} s", ""]
        d += [f"- **{k}**: {o['chon_y'][k]}" for k in ("boi_canh", "y_tron", "mang_ve", "chua_lai")]
        d += ["", "Lời đọc nối (theo thứ tự phát):"]
        d += [f"{i}. [{mm(p['start'])}–{mm(p['end'])}] {p['role']}/{p['tone']}{' · màn chốt' if p.get('cta') else ''}: {p['text']}"
              for i, p in enumerate(o["pieces"], 1)]
        d.append("")
    (H / "ke-hoach-cat.md").write_text("\n".join(d), encoding="utf-8")
    print("\n".join(d))


if __name__ == "__main__":
    main()
