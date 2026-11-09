#!/usr/bin/env python3
"""ÁP KẾ HOẠCH CẢNH: ap_canh.py <dự án> <ke-hoach-canh.json> <W> [--kiem]

Claude chỉ trích câu nguyên văn (`trich`, `het`, `trich_<khoá>`); script này tìm mốc giây trong check/goc/words.srt rồi ghi:
motion/src/scenes.js (SCENES, CHAPTERS, SIDES) · project.js (topic, tuyen, ytEnd, schedule) · sửa chính tả captions.js (`sua_chu`) ·
images/queries.json (ảnh cần tìm) · <dự án>/ke-hoach-canh.md (bảng cảnh để David đối chiếu khi góp ý).
--kiem: chỉ soát, in lỗi (mã thoát 1 khi có lỗi) — bước kiểm của goi_claude.py.

Kiểu cảnh hợp lệ = kiểu đăng ký trong motion/src/Root.jsx của dự án (thêm kiểu mới vào template là tự hợp lệ ở đây).
Luật soát (luat-chung 1: chữ nguyên văn): câu trích phải tìm được; chữ trên màn hình phải có trong lời; biểu tượng có trong
thư viện; tuyến nhạc có trong hồ sơ; thẻ tít chỉ khi David yêu cầu; màn chốt cuối video; khung ngang từ gốc dọc cần SIDES.
"""
import json, re, sys
from pathlib import Path

APP = Path(__file__).resolve().parents[1]; DV = APP.parent
sys.path.insert(0, str(Path(__file__).parent)); sys.path.insert(0, str(DV / "khoi"))
import loi, hoso  # noqa: E402

CON = {"bocuc": ("kieu", {"the-canh", "o-nguoi", "chuong"}), "illus": ("mode", {"single", "flow", "vs", "count", "list"})}
CHU = {"text", "tieu_de", "label", "quote", "ten", "title", "eyebrow", "name", "subtitle", "lines"}   # chữ trên màn hình
TRUOC = 0.4
SUA = frozenset()
SAU = {"nhan": 3.0, "bocuc": 2.5, "illus": 2.0, "diagram": 2.5, "action": 2.5, "cta": 1.0, "hook": 0.5, "listItem": 2.5,
       "kinetic": 2.0, "lower": 3.0}
TOI_THIEU = {"nhan": 3.0, "bocuc": 3.5, "illus": 3.0, "diagram": 4.0, "action": 5.0, "cta": 4.0, "hook": 2.5, "listItem": 2.5,
             "lower": 3.5}


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
            elif k in CHU and isinstance(v, list) and all(isinstance(x, str) for x in v): out.extend(v)
            elif k == "nhan" and isinstance(v, str): out.append(v)
            else: chu_tren_man(v, out)
    return out


def khoa(o, ten, out):
    if isinstance(o, list):
        for x in o: khoa(x, ten, out)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k == ten and isinstance(v, str): out.append(v)
            else: khoa(v, ten, out)
    return out


def du_an(P):
    s = (Path(P) / "motion/src/project.js").read_text(encoding="utf-8")
    g = lambda k: float(re.search(rf"{k}: *([\d.]+)", s).group(1))
    return g("width"), g("height"), g("duration")


def lap(P, kh, tc):
    T = loi.tu(Path(P) / "check/goc/words.srt")
    cfg = hoso.load("lam-video"); loi_ds = []; canh = []; ICON = set(loi.bieu_tuong()); KIEU = loi.kieu_canh(Path(P) / "motion/src/Root.jsx")
    tuyen = hoso.get(cfg, "nhac.tuyen") or {}
    if kh.get("tuyen") not in tuyen:
        loi_ds.append(f"tuyen '{kh.get('tuyen')}' không có trong hồ sơ: {list(tuyen)}")
    anh_keys = {a["key"] for a in kh.get("anh", [])}
    global SUA   # chữ đúng sau khi sửa lỗi Whisper nghe nhầm (vd "White Spa" thay "Wild Spa") — hợp lệ trên màn hình
    SUA = frozenset(t for x in kh.get("sua_chu", []) for t in loi.chuan(x.get("dung", "")))
    sau = 0.0
    for c in kh.get("canh", []):
        cid, typ = c.get("id", "?"), c.get("type")
        if typ not in KIEU:
            loi_ds.append(f"cảnh {cid}: kiểu '{typ}' không có trong template (chỉ: {sorted(KIEU)})"); continue
        if typ == "hook" and not tc.get("hook"):
            loi_ds.append(f"cảnh {cid}: thẻ tít mở đầu (hook) chỉ làm khi David yêu cầu — bỏ cảnh này"); continue
        p = c.get("props", {})
        if typ in CON and p.get(CON[typ][0]) not in CON[typ][1]:
            loi_ds.append(f"cảnh {cid}: {typ} {CON[typ][0]} '{p.get(CON[typ][0])}' không có (chỉ: {sorted(CON[typ][1])})")
        for ic in khoa(p, "icon", []):
            if ic not in ICON: loi_ds.append(f"cảnh {cid}: biểu tượng '{ic}' không có trong thư viện")
        for ph in khoa(p, "photo", []):
            if Path(ph).stem not in anh_keys: loi_ds.append(f"cảnh {cid}: ảnh '{ph}' không có trong danh sách `anh` cần tìm")
        r = loi.tim(c.get("trich", ""), T, sau=max(0, sau - 30))
        if not r:
            loi_ds.append(f"cảnh {cid}: không tìm thấy câu trích mở cảnh «{c.get('trich')}»"); continue
        a = max(0.0, r[0] - TRUOC) if typ != "hook" else 0.0
        moc = [r[1]]
        props = giai(p, T, moc, loi_ds, cid, sau=r[0] - 2, gan=r[0])
        if typ in ("nhan", "kinetic", "listItem") and "at" not in props: props["at"] = round(r[0], 2)
        if c.get("het"):
            h = loi.tim(c["het"], T, sau=r[0] - 1, gan=r[0])
            if not h: loi_ds.append(f"cảnh {cid}: không tìm thấy câu kết cảnh «{c['het']}»"); continue
            b = h[1] + 0.6
        else:
            b = max(moc) + SAU.get(typ, 2.5)
        b = max(b, a + TOI_THIEU.get(typ, 3.0))
        for t in chu_tren_man(props, []):
            if loi.co_trong_loi(t, T, a, b, them=SUA) < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0, them=SUA) < 0.85:   # quanh cảnh, hoặc thẻ tóm tắt cả video
                loi_ds.append(f"cảnh {cid}: chữ «{t}» không phải nguyên văn lời — chỉ được chọn câu, bỏ bớt chữ đầu/cuối, viết hoa")
        canh.append({"id": cid, "type": typ, "start": round(a, 2), "end": round(b, 2), "props": props, "_trich": c.get("trich")})
        sau = r[0]
    canh.sort(key=lambda c: c["start"])
    for x, y in zip(canh, canh[1:]):            # không chồng cảnh: cảnh trước nhường cảnh sau
        if x["end"] > y["start"] - 0.05:
            x["end"] = round(y["start"] - 0.05, 2)
            if x["end"] - x["start"] < 1.5:
                loi_ds.append(f"cảnh {x['id']} bị cảnh {y['id']} đè, chỉ còn {x['end'] - x['start']:.1f} s — dời hoặc bỏ một cảnh")
    if not canh or canh[-1]["type"] != "cta":
        loi_ds.append("thiếu màn chốt `cta` ở cuối (nguyên văn câu người nói cuối video)")
    chuong = []
    for ch in kh.get("chuong", []):
        r = loi.tim(ch["trich"], T)
        if not r: loi_ds.append(f"chương «{ch.get('text')}»: không tìm thấy câu trích"); continue
        chuong.append({"at": round(r[0], 2), "text": ch["text"]})
    chuong.sort(key=lambda c: c["at"])
    if chuong: chuong[0]["at"] = 0          # luật YouTube: chương đầu 0:00
    sides = None
    if tc.get("khung") == "ngang":
        if not kh.get("sides"):
            loi_ds.append("khung xuất ngang từ gốc dọc: thiếu `sides` (eyebrow, title, speaker, keywords, points)")
        else:
            sides = giai(kh["sides"], T, [], loi_ds, "sides", 0, None)
    return canh, chuong, sides, loi_ds


def ghi_scenes(P, canh, chuong, sides):
    f = Path(P) / "motion/src/scenes.js"; s = f.read_text(encoding="utf-8")
    sach = [{k: v for k, v in c.items() if not k.startswith("_")} for c in canh]
    i = s.index("export const SCENES = "); j = s.index("\n];", i) + 3
    s = s[:i] + "export const SCENES = " + json.dumps(sach, ensure_ascii=False, indent=1) + ";" + s[j:]
    for ten, gt in (("CHAPTERS", chuong), ("SIDES", sides)):
        s = re.sub(rf"export const {ten} = .*?;\n", lambda m: f"export const {ten} = " + json.dumps(gt, ensure_ascii=False) + ";\n",
                   s, count=1, flags=re.S)
    f.write_text(s, encoding="utf-8")


def ghi_du_an(P, gt):
    f = Path(P) / "motion/src/project.js"; s = f.read_text(encoding="utf-8")
    for k, v in gt.items():
        s = re.sub(rf",\s*{k}: *('[^']*'|\"[^\"]*\"|[\d.]+)", "", s)
        if v not in (None, ""):
            s = s.replace("};", f", {k}: {json.dumps(v, ensure_ascii=False)}}};", 1)
    f.write_text(s, encoding="utf-8")


def sua_phu_de(P, sua):
    f = Path(P) / "motion/src/captions.js"; s = f.read_text(encoding="utf-8"); n = 0
    for x in sua:
        if x.get("sai") and x["sai"] != x.get("dung"):
            n += s.count(x["sai"]); s = s.replace(x["sai"], x["dung"])
    f.write_text(s, encoding="utf-8")
    return n


def mm(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


def ghi_ke_hoach(P, kh, canh, chuong, ytend):
    d = [f"# Kế hoạch cảnh — {Path(P).parent.name}", "",
         f"Chủ đề (dấu góc): **{kh.get('topic')}** · Nhạc: tuyến `{kh.get('tuyen')}` — {kh.get('ly_do_tuyen', '')}",
         f"Màn kết YouTube: {f'{ytend} s' if ytend else 'không (video ≤ 3 phút)'} · Chương: {len(chuong)}", "",
         "| # | Mốc | Kiểu | Chữ trên màn hình | Câu trích (mở cảnh) |", "|---|---|---|---|---|"]
    for i, c in enumerate(canh, 1):
        chu = " / ".join(t.replace("\n", " ") for t in chu_tren_man(c["props"], []))[:120]
        kieu = c["type"] + (f" {c['props'].get('kieu') or c['props'].get('mode') or c['props'].get('variant') or ''}").rstrip()
        d.append(f"| {i} | {mm(c['start'])}–{mm(c['end'])} | {kieu} | {chu} | «{c.get('_trich', '')}» |")
    if kh.get("anh"):
        d += ["", "## Ảnh minh hoạ cần tìm"] + [f"- `{a['key']}`: {a['q']}" for a in kh["anh"]]
    (Path(P) / "ke-hoach-canh.md").write_text("\n".join(d) + "\n", encoding="utf-8")


def main():
    P, kh_p, W = sys.argv[1], sys.argv[2], sys.argv[3]; kiem = "--kiem" in sys.argv
    kh = json.loads(Path(kh_p).read_text(encoding="utf-8"))
    tt = json.loads((Path(W) / "trang-thai.json").read_text(encoding="utf-8")); tc = tt.get("tuy_chon", {})
    canh, chuong, sides, loi_ds = lap(P, kh, tc)
    print(f"{len(canh)} cảnh · {len(chuong)} chương · {len(kh.get('anh', []))} ảnh cần tìm · {len(loi_ds)} lỗi")
    for x in loi_ds: print("✗", x)
    if loi_ds:
        sys.exit(1)
    if kiem:
        return
    w, h, dur = du_an(P)
    ytend = hoso.get(hoso.load("lam-video"), "youtube.man_ket_s", 20) if dur > 180 else None   # khối 08: video > 3 phút
    ghi_scenes(P, canh, chuong, sides)
    ghi_du_an(P, {"topic": kh.get("topic", ""), "tuyen": kh["tuyen"], "ytEnd": ytend, "schedule": tc.get("lich") or None})
    q = Path(P) / "images/queries.json"
    if kh.get("anh"):
        q.parent.mkdir(exist_ok=True); q.write_text(json.dumps(kh["anh"], ensure_ascii=False, indent=1), encoding="utf-8")
    elif q.exists():
        q.unlink()
    ghi_ke_hoach(P, kh, canh, chuong, ytend)
    (Path(P) / "check").mkdir(exist_ok=True)
    (Path(P) / "check/app-sua-chu.json").write_text(json.dumps(kh.get("sua_chu", []), ensure_ascii=False), encoding="utf-8")
    print(f"sửa chính tả phụ đề: {sua_phu_de(P, kh.get('sua_chu', []))} chỗ · màn kết YouTube: {ytend or 'không'}")


if __name__ == "__main__":
    main()
