#!/usr/bin/env python3
"""ÁP KẾ HOẠCH CẢNH: ap_canh.py <dự án> <ke-hoach-canh.json> [--kiem]

Claude chỉ trích câu nguyên văn (`trich`, `het`, `trich_<khoá>`); script này tìm mốc giây trong check/goc/words.srt rồi ghi
motion/src/scenes.js (SCENES + CHAPTERS), project.js (topic, tuyen), sửa chính tả captions.js (`sua_chu`).
--kiem: chỉ soát, in lỗi (mã thoát 1 khi có lỗi) — dùng làm bước kiểm của goi_claude.py.

Luật soát (luat-chung 1: chữ nguyên văn): câu trích phải tìm được; chữ trên màn hình phải có trong lời quanh cảnh;
biểu tượng, kiểu cảnh phải có trong thư viện; tuyến nhạc phải có trong hồ sơ. Thêm luật soát → thêm vào LUAT dưới đây.
"""
import json, re, sys
from pathlib import Path

APP = Path(__file__).resolve().parents[1]; DV = APP.parent
sys.path.insert(0, str(Path(__file__).parent)); sys.path.insert(0, str(DV / "khoi"))
import loi, hoso  # noqa: E402

KIEU = {"nhan": None, "bocuc": {"the-canh", "o-nguoi", "chuong"}, "illus": {"single", "flow", "vs", "count", "list"},
        "action": None, "cta": None}
CHU = ("text", "tieu_de", "label", "quote", "ten")       # khoá chứa chữ hiện trên màn hình → soát nguyên văn
TRUOC, SAU_MAC_DINH = 0.4, {"nhan": 3.0, "bocuc": 2.5, "illus": 2.0, "action": 2.5, "cta": 1.0}
TOI_THIEU = {"nhan": 3.0, "bocuc": 3.5, "illus": 3.0, "action": 5.0, "cta": 4.0}


def giai(o, T, moc, loi_ds, cid, sau, gan):
    """Đổi mọi khoá trich / trich_X trong props (lồng nhau) thành mốc giây; gom các mốc vào `moc`."""
    if isinstance(o, list):
        return [giai(x, T, moc, loi_ds, cid, sau, gan) for x in o]
    if not isinstance(o, dict):
        return o
    out = {}
    for k, v in o.items():
        if k == "trich" or k.startswith("trich_"):
            dich = "at" if k == "trich" else k[6:]
            r = loi.tim(v, T, sau=sau, gan=gan)
            if not r:
                loi_ds.append(f"cảnh {cid}: không tìm thấy câu trích «{v}» ({k}) — trích đúng nguyên văn trong BẢN LỜI")
                continue
            out[dich] = round(r[0], 2); moc.append(r[1])
        else:
            out[k] = giai(v, T, moc, loi_ds, cid, sau, gan)
    return out


def chu_tren_man(o, out):
    if isinstance(o, list):
        for x in o: chu_tren_man(x, out)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in CHU and isinstance(v, str): out.append(v)
            elif k == "nhan" and isinstance(v, str): out.append(v)
            else: chu_tren_man(v, out)
    return out


def bieu_tuong_dung(o, out):
    if isinstance(o, list):
        for x in o: bieu_tuong_dung(x, out)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k == "icon" and isinstance(v, str): out.append(v)
            else: bieu_tuong_dung(v, out)
    return out


def lap(P, kh):
    T = loi.tu(Path(P) / "check/goc/words.srt")
    cfg = hoso.load("lam-video"); loi_ds = []; canh = []; ICON = set(loi.bieu_tuong())
    if kh.get("tuyen") not in (hoso.get(cfg, "nhac.tuyen") or {}):
        loi_ds.append(f"tuyen '{kh.get('tuyen')}' không có trong hồ sơ: {list((hoso.get(cfg, 'nhac.tuyen') or {}).keys())}")
    sau = 0.0
    for c in kh.get("canh", []):
        cid, typ = c.get("id", "?"), c.get("type")
        if typ not in KIEU:
            loi_ds.append(f"cảnh {cid}: kiểu '{typ}' không có (chỉ: {list(KIEU)})"); continue
        p = c.get("props", {})
        k2 = p.get("kieu") if typ == "bocuc" else p.get("mode") if typ == "illus" else None
        if KIEU[typ] and k2 not in KIEU[typ]:
            loi_ds.append(f"cảnh {cid}: {typ} kiểu '{k2}' không có (chỉ: {sorted(KIEU[typ])})")
        for ic in bieu_tuong_dung(p, []):
            if ic not in ICON:
                loi_ds.append(f"cảnh {cid}: biểu tượng '{ic}' không có trong thư viện")
        r = loi.tim(c.get("trich", ""), T, sau=max(0, sau - 30))
        if not r:
            loi_ds.append(f"cảnh {cid}: không tìm thấy câu trích mở cảnh «{c.get('trich')}»"); continue
        a = max(0.0, r[0] - TRUOC); moc = [r[1]]
        props = giai(p, T, moc, loi_ds, cid, sau=r[0] - 2, gan=r[0])
        if typ == "nhan" and "at" not in props: props["at"] = round(r[0], 2)
        if c.get("het"):
            h = loi.tim(c["het"], T, sau=r[0] - 1, gan=r[0])
            if not h: loi_ds.append(f"cảnh {cid}: không tìm thấy câu kết cảnh «{c['het']}»"); continue
            b = h[1] + 0.6
        else:
            b = max(moc) + SAU_MAC_DINH[typ]
        b = max(b, a + TOI_THIEU[typ])
        for t in chu_tren_man(props, []):
            tl = loi.co_trong_loi(t, T, a, b)          # quanh cảnh ≥ 60%, hoặc (thẻ tóm tắt) cả video ≥ 85%
            if tl < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0) < 0.85:
                loi_ds.append(f"cảnh {cid}: chữ «{t}» không phải nguyên văn lời quanh cảnh ({int(tl * 100)}% từ có trong lời) — "
                              f"chỉ được chọn câu, bỏ bớt chữ đầu/cuối, viết hoa")
        canh.append({"id": cid, "type": typ, "start": round(a, 2), "end": round(b, 2), "props": props})
        sau = r[0]
    canh.sort(key=lambda c: c["start"])
    for x, y in zip(canh, canh[1:]):            # không chồng cảnh: cảnh trước nhường cảnh sau
        if x["end"] > y["start"] - 0.05:
            x["end"] = round(y["start"] - 0.05, 2)
            if x["end"] - x["start"] < 1.5:
                loi_ds.append(f"cảnh {x['id']} bị cảnh {y['id']} đè, chỉ còn {x['end'] - x['start']:.1f} s — dời hoặc bỏ một cảnh")
    if canh and canh[-1]["type"] != "cta":
        loi_ds.append("thiếu màn chốt `cta` ở cuối (nguyên văn câu người nói cuối video)")
    chuong = []
    for ch in kh.get("chuong", []):
        r = loi.tim(ch["trich"], T)
        if not r: loi_ds.append(f"chương «{ch.get('text')}»: không tìm thấy câu trích"); continue
        chuong.append({"at": round(r[0], 2), "text": ch["text"]})
    chuong.sort(key=lambda c: c["at"])
    if chuong: chuong[0]["at"] = 0          # luật YouTube: chương đầu 0:00
    return canh, chuong, loi_ds


def ghi_scenes(P, canh, chuong):
    f = Path(P) / "motion/src/scenes.js"; s = f.read_text(encoding="utf-8")
    i = s.index("export const SCENES = "); j = s.index("\n];", i) + 3
    s = s[:i] + "export const SCENES = " + json.dumps(canh, ensure_ascii=False, indent=1) + ";" + s[j:]
    s = re.sub(r"export const CHAPTERS = .*?;\n", lambda m: "export const CHAPTERS = " + json.dumps(chuong, ensure_ascii=False) + ";\n",
               s, count=1, flags=re.S)
    f.write_text(s, encoding="utf-8")


def ghi_du_an(P, topic, tuyen):
    f = Path(P) / "motion/src/project.js"; s = f.read_text(encoding="utf-8")
    for k, v in (("tuyen", tuyen), ("topic", topic)):
        v = json.dumps(v, ensure_ascii=False)
        s = re.sub(rf",\s*{k}: *('[^']*'|\"[^\"]*\")", "", s)
        s = s.replace("};", f", {k}: {v}}};", 1)
    f.write_text(s, encoding="utf-8")


def sua_phu_de(P, sua):
    f = Path(P) / "motion/src/captions.js"; s = f.read_text(encoding="utf-8"); n = 0
    for x in sua:
        if x.get("sai") and x["sai"] != x.get("dung"):
            n += s.count(x["sai"]); s = s.replace(x["sai"], x["dung"])
    f.write_text(s, encoding="utf-8")
    return n


def main():
    P, kh_p = sys.argv[1], sys.argv[2]; kiem = "--kiem" in sys.argv
    kh = json.loads(Path(kh_p).read_text(encoding="utf-8"))
    canh, chuong, loi_ds = lap(P, kh)
    print(f"{len(canh)} cảnh · {len(chuong)} chương · {len(loi_ds)} lỗi")
    for x in loi_ds: print("✗", x)
    if loi_ds:
        sys.exit(1)
    if kiem:
        return
    ghi_scenes(P, canh, chuong); ghi_du_an(P, kh.get("topic", ""), kh["tuyen"])
    print(f"sửa chính tả phụ đề: {sua_phu_de(P, kh.get('sua_chu', []))} chỗ")


if __name__ == "__main__":
    main()
