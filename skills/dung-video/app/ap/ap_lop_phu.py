#!/usr/bin/env python3
"""ÁP LỚP PHỦ HIGHLIGHT (skill 7A): ap_lop_phu.py <dự án highlight> <lop-phu.json> [--kiem]
Claude TRÍCH câu nguồn cho từng lớp phủ (pow cú chốt, action, chips, illus, diagram…); script tìm mốc trong words.srt nguồn, đổi sang
TS(<giây nguồn>) của edl.js, soát: kiểu có trong Show.jsx, câu nằm trong clip, chữ nguyên văn (chữ đã sửa chính tả được tính), rồi ghi
vào OVERLAYS + sửa chính tả SUBS + tô từ khoá (hl) + kiểu màn chốt. Luôn áp lên edl.goc.js (bản hl_edl.py sinh) → chạy lại không nhân đôi."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import loi  # noqa: E402
from hl_chung import pa, DV  # noqa: E402

KHONG = {"hud", "outro", "teaserTag", "title", "round", "pinTitle"}   # nhận diện / vlog — hl_edl tự đặt hoặc không dùng cho highlight
CHU = {"text", "quote", "label", "name", "tieu_de", "title", "lines"}
SAU = {"pow": 1.6, "action": 2.5, "illus": 2.2, "diagram": 2.5, "chips": 2.0}
KIND = {"comment", "save", "follow", "share", "moi"}


def kieu_ov():
    s = re.sub(r"//[^\n]*", "", (DV / "video-style-edit/assets/montage-template/src/Show.jsx").read_text(encoding="utf-8"))
    m = re.search(r"const TYPES = \{(.*?)\};", s, re.S)
    return set(re.findall(r"(?:^|[{,])\s*(\w+)\s*:", m.group(1), re.M)) - KHONG


def chu(o, out):
    if isinstance(o, list):
        for x in o: chu(x, out)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in CHU and isinstance(v, str): out.append(v)
            elif k in CHU and isinstance(v, list) and all(isinstance(x, str) for x in v): out.extend(v)
            else: chu(v, out)
    return out


def giai(o, T, moc, loi_ds, nhan, gan):
    if isinstance(o, list): return [giai(x, T, moc, loi_ds, nhan, gan) for x in o]
    if not isinstance(o, dict): return o
    r = {}
    for k, v in o.items():
        if k == "trich" or k.startswith("trich_"):
            t = loi.tim(v, T, gan=gan)
            if not t: loi_ds.append(f"{nhan}: không tìm thấy «{v}» ({k})"); continue
            r["at" if k == "trich" else k[6:]] = f"__TS__{t[0]:.2f}"; moc.append(t[0])
        else:
            r[k] = giai(v, T, moc, loi_ds, nhan, gan)
    return r


def main():
    H, kp = Path(sys.argv[1]), sys.argv[2]; kiem = "--kiem" in sys.argv
    kh = json.loads(Path(kp).read_text(encoding="utf-8")); P = pa(H)
    T = loi.tu(H / "check/goc/words.srt"); KIEU = kieu_ov(); loi_ds = []
    sua = kh.get("sua_chu", []); SUA = frozenset(t for x in sua for t in loi.chuan(x.get("dung", "")))
    vung = {o["id"]: [(p["start"], p["end"]) for p in o["pieces"]] for o in P["options"]}
    ket = {}
    for c in kh.get("clips", []):
        cid = c.get("id")
        if cid not in vung: loi_ds.append(f"không có clip {cid} trong phuong-an.json (chỉ: {list(vung)})"); continue
        trong = lambda t: any(a - 0.3 <= t <= b + 0.3 for a, b in vung[cid])
        ovs = []
        for j, ov in enumerate(c.get("overlays", []), 1):
            nhan = f"clip {cid} lớp {j} ({ov.get('type')})"
            if ov.get("type") not in KIEU: loi_ds.append(f"{nhan}: kiểu không có trong khung ghép (chỉ: {sorted(KIEU)})"); continue
            a = loi.tim(ov.get("trich", ""), T)
            if not a: loi_ds.append(f"{nhan}: không tìm thấy câu trích «{ov.get('trich')}»"); continue
            if not trong(a[0]): loi_ds.append(f"{nhan}: câu «{ov.get('trich')}» không nằm trong các câu của clip {cid}"); continue
            moc = [a[1]]; props = giai(ov.get("props", {}), T, moc, loi_ds, nhan, a[0])
            if ov.get("het"):
                h = loi.tim(ov["het"], T, sau=a[0] - 1, gan=a[0])
                if not h: loi_ds.append(f"{nhan}: không tìm thấy câu kết «{ov['het']}»"); continue
                end = f"__TS__{h[1]:.2f}"
            else:
                end = f"__TSP__{max(moc):.2f}__{SAU.get(ov['type'], 2.0)}"
            for t in chu(props, []):
                if loi.co_trong_loi(t, T, a[0], a[1], them=SUA) < 0.6 and loi.co_trong_loi(t, T, 0, 1e9, 0, them=SUA) < 0.85:
                    loi_ds.append(f"{nhan}: chữ «{t}» không nguyên văn lời — chỉ chọn câu, bỏ bớt chữ đầu/cuối, viết hoa")
            ovs.append({"type": ov["type"], "start": f"__TS__{max(0, a[0] - 0.1):.2f}", "end": end, **props})
        if c.get("cta_kind") and c["cta_kind"] not in KIND: loi_ds.append(f"clip {cid}: cta_kind chỉ: {sorted(KIND)}")
        ket[cid] = (ovs, c.get("hl", []), c.get("cta_kind"))
    print(f"{sum(len(v[0]) for v in ket.values())} lớp phủ · {len(loi_ds)} lỗi")
    for x in loi_ds: print("✗", x)
    if loi_ds: sys.exit(1)
    if kiem: return
    for cid, (ovs, hl, kind) in ket.items():
        E = H / f"clip-{cid}" / "motion/src"; s = (E / "edl.goc.js").read_text(encoding="utf-8")
        js = ",\n".join("  " + json.dumps(o, ensure_ascii=False) for o in ovs)
        js = re.sub(r'"__TS__([\d.]+)"', r"TS(\1)", js)
        js = re.sub(r'"__TSP__([\d.]+)__([\d.]+)"', r"TS(\1) + \2", js)
        i = s.index("export const OVERLAYS = ["); j = s.index("\n];", i)
        if js: s = s[:j] + "\n" + js + "," + s[j:]
        def dong(m):   # SUBS: sửa chính tả + tô từ khoá
            t = m.group(2)
            for x in sua:
                if x.get("sai"): t = t.replace(x["sai"], x["dung"])
            h = [k for k in hl if k.lower() in t.lower()]
            return f'{m.group(1)}text: {json.dumps(t, ensure_ascii=False)}, hl: {json.dumps(h, ensure_ascii=False)}}}'
        a = s.index("export const SUBS = ["); b = s.index("\n];", a)
        s = s[:a] + re.sub(r'(\{start: [\d.]+, end: [\d.]+, )text: "((?:[^"\\]|\\.)*)", hl: \[[^\]]*\]\}', dong, s[a:b]) + s[b:]
        if kind: s = re.sub(r"(export const CTA = \{text: .*?, kind: )'\w+'", rf"\1'{kind}'", s, count=1)
        (E / "edl.js").write_text(s, encoding="utf-8")
        print(f"clip {cid}: {len(ovs)} lớp phủ, tô {len(hl)} từ khoá" + (f", màn chốt {kind}" if kind else ""))


if __name__ == "__main__":
    main()
