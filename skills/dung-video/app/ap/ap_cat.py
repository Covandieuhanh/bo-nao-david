#!/usr/bin/env python3
"""LỌC + CẮT. Hai chế độ:
  ap_cat.py <dự án> <W> --liet-ke          → W/de-xuat-cat.txt (đề xuất cắt của clean_suggest, đánh số) + W/ban-loi-tho.txt
  ap_cat.py <dự án> <W> <loc-va-cat.json> [--kiem]
        → W/phieu-loc.md (cổng duyệt 1) + đánh dấu cuts.json (ok) + thêm cắt bỏ phần trước/sau câu trích (làm lại video cũ)
Mốc lấy từ check/clean/words.srt (bản thô) — Claude chỉ trích câu."""
import glob, json, os, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import loi  # noqa: E402


def liet_ke(P, W):
    c = Path(P) / "check/clean"
    d = json.loads((c / "cuts.json").read_text(encoding="utf-8"))
    dong = [f"#{i} [{x['start']:.1f}–{x['end']:.1f}] {x.get('why', '')}: {x.get('text', '')[:220]}" for i, x in enumerate(d["cuts"])]
    Path(W, "de-xuat-cat.txt").write_text("\n".join(dong) + "\n", encoding="utf-8")
    n = loi.ban_loi(c / "words.srt", c / "transcript.srt", Path(W, "ban-loi-tho.txt"))
    dai = loi.doc_srt(c / "words.srt")[-1][1] if loi.doc_srt(c / "words.srt") else 0
    raw = sorted(glob.glob(str(Path(P) / "davinci/media/video_goc_raw.*")) + glob.glob(str(Path(P) / "davinci/media/video_goc.*")))[0]
    env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
    pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", raw],
                        capture_output=True, text=True, env=env).stdout.strip()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{dai / 2:.1f}", "-i", raw, "-frames:v", "1", str(Path(W, "khung-giua.jpg"))], env=env)
    Path(W, "thong-tin.txt").write_text(f"Thời lượng lời: {dai:.0f} giây ({dai / 60:.1f} phút)\nKhung hình gốc (rộng,cao): {pr}\n"
                                        f"Ảnh khung-giua.jpg = 1 khung giữa video ở đúng cỡ gốc (soát chữ/viền in cứng)\n", encoding="utf-8")
    print(f"{len(dong)} đề xuất cắt · {n} dòng lời")


def mm(s):
    return f"{int(s // 60)}:{int(s % 60):02d}"


def ap(P, W, kp, kiem):
    kh = json.loads(Path(kp).read_text(encoding="utf-8"))
    c = Path(P) / "check/clean"
    if not (c / "cuts.json").exists():     # podcast: giữ nguyên toàn bộ (không làm sạch) — chỉ ghi phiếu lọc, lời ở check/goc
        c = Path(P) / "check/goc"
    T = loi.tu(c / "words.srt")
    d = json.loads((c / "cuts.json").read_text(encoding="utf-8")) if (c / "cuts.json").exists() else {"cuts": []}; loi_ds = []
    cat = kh.get("cat", {})
    for i in cat.get("giu_de_xuat", []):
        if not 0 <= i < len(d["cuts"]): loi_ds.append(f"không có đề xuất cắt #{i}")
    them = []
    if cat.get("bo_truoc"):
        r = loi.tim(cat["bo_truoc"], T)
        if r: them.append({"start": 0, "end": round(r[0] - 0.15, 2), "why": "app: bỏ phần trước câu mở", "ok": True, "text": cat["bo_truoc"]})
        else: loi_ds.append(f"không tìm thấy câu bo_truoc «{cat['bo_truoc']}»")
    if cat.get("bo_sau"):
        r = loi.tim(cat["bo_sau"], T, sau=T[len(T) // 2][0] if T else 0)
        if r: them.append({"start": round(r[1] + 0.6, 2), "end": round(T[-1][1] + 5, 2), "why": "app: bỏ phần sau câu kết", "ok": True, "text": cat["bo_sau"]})
        else: loi_ds.append(f"không tìm thấy câu bo_sau «{cat['bo_sau']}»")
    moc = {}
    lc = kh.get("loc", {})
    for k in ("van_de", "giai_phap", "thuc_thi"):
        q = (lc.get("ba_phan") or {}).get(k)
        if q:
            r = loi.tim(q, T); moc[k] = mm(r[0]) if r else "?"
            if not r: loi_ds.append(f"ba_phan.{k}: không tìm thấy «{q}»")
        else:
            moc[k] = "THIẾU"
    for x in lc.get("lan_ranh", []):
        r = loi.tim(x.get("trich", ""), T); x["moc"] = mm(r[0]) if r else "?"
    if cat.get("khung_trong") and not re.fullmatch(r"\d+:\d+:\d+:\d+", cat["khung_trong"].strip()):
        loi_ds.append(f"khung_trong '{cat['khung_trong']}' phải dạng rộng:cao:x:y (pixel của khung gốc), hoặc để trống")
    for o in cat.get("orient") or []:
        if o not in ("180", "cw", "ccw", "mirror"): loi_ds.append(f"orient '{o}' chỉ được: 180 · cw · ccw · mirror")
    dx = kh.get("de_xuat_dung", {})
    if dx.get("cau_chot") and not loi.tim(dx["cau_chot"], T): loi_ds.append(f"cau_chot: không tìm thấy «{dx['cau_chot']}»")
    for x in loi_ds: print("✗", x)
    if loi_ds: sys.exit(1)
    if kiem: return
    for i, x in enumerate(d["cuts"]): x["ok"] = i in set(cat.get("giu_de_xuat", []))
    d["cuts"] = [x for x in d["cuts"] if not str(x.get("why", "")).startswith("app:")] + them
    if cat.get("orient") is not None: d["orient"] = cat["orient"]
    Path(W, "khung-trong.txt").write_text((cat.get("khung_trong") or "").strip() + "\n", encoding="utf-8")
    if c.name == "clean": (c / "cuts.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    dm = lc.get("diem", {}); tong = sum(dm.values()) if dm else "?"
    lr = "; ".join(f"⚠️ {x['moc']} «{x['trich']}» — {x.get('rui_ro', '')}" for x in lc.get("lan_ranh", [])) or "không"
    cat_md = [f"- #{i}: {d['cuts'][i].get('why')} [{d['cuts'][i]['start']:.1f}–{d['cuts'][i]['end']:.1f}]" for i in cat.get("giu_de_xuat", [])]
    cat_md += [f"- {x['why']}: [{x['start']:.1f}–{x['end']:.1f}] «{x['text']}»" for x in them]
    lv = kh.get("loai_video") or {}
    tt = json.loads((Path(W) / "trang-thai.json").read_text(encoding="utf-8")) if (Path(W) / "trang-thai.json").exists() else {}
    ct = tt.get("cong_thuc", ""); hop = {"lam-video": "noi-truoc-camera", "podcast": "podcast-tieng", "ghep-vlog": "vlog-canh"}.get(ct)
    ten_loai = {"noi-truoc-camera": "1 người nói trước camera", "vlog-canh": "vlog / cảnh sự kiện (dựng bằng Ghép vlog)",
                "podcast-tieng": "podcast chỉ có tiếng", "khac": "khác"}
    canh_bao_loai = (f"> ⚠️ **Loại video thật: {ten_loai.get(lv.get('loai'), lv.get('loai'))}** — {lv.get('ly_do', '')}. Việc này đang dùng công thức "
                     f"`{ct}`, không khớp. Nên Huỷ việc này và tạo việc mới đúng loại (hoặc vẫn duyệt nếu David muốn).\n\n"
                     if hop and lv.get("loai") and lv["loai"] != hop else
                     (f"**Loại video:** {ten_loai.get(lv.get('loai'), '')} — {lv.get('ly_do', '')}\n\n" if lv.get("loai") else ""))
    md = f"""# Phiếu lọc — {Path(P).parent.name}

{canh_bao_loai}**Kết luận:** {lc.get('ket_luan', '?')} · **{tong}/10** (Gốc {dm.get('goc', '?')} · Tệp {dm.get('tep', '?')} · Hành động {dm.get('hanh_dong', '?')} · Tương tác {dm.get('tuong_tac', '?')} · Nhân hiệu {dm.get('nhan_hieu', '?')})

**Lý do:** {lc.get('ly_do', '')}

**Lằn ranh:** {lr}

**Nhánh:** {lc.get('nhanh', '')}

**Đề xuất:** {lc.get('de_xuat', '')}

**3 phần:** Vấn đề {moc['van_de']} · Giải pháp {moc['giai_phap']} · Thực thi {moc['thuc_thi']}

**Câu mở:** «{lc.get('cau_mo', '')}»

## Đề xuất dựng (David đổi được bằng góp ý)
- **Câu chốt (màn chốt cuối video):** «{kh.get('de_xuat_dung', {}).get('cau_chot', '') or 'không có câu kêu gọi — kết ở câu chốt ý'}»
- **Ý chính sẽ minh hoạ:** {'; '.join(kh.get('de_xuat_dung', {}).get('y_chinh', [])) or '—'}
- **Chữ thumbnail (nếu video ngang):** {kh.get('de_xuat_dung', {}).get('chu_thumbnail', '') or '—'}
- **Chiều hình:** {', '.join(cat.get('orient') or []) or 'đúng chiều'} · **Chữ/viền in cứng:** {('cắt khung ' + cat['khung_trong']) if cat.get('khung_trong') else 'không có'}

## Cắt khi làm sạch
{chr(10).join(cat_md) or '- không cắt (video dài để nguyên)'}

## Cần David quyết
{chr(10).join('- ' + q for q in lc.get('hoi', [])) or '- không'}
"""
    Path(W, "phieu-loc.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--liet-ke" in a: liet_ke(a[0], a[1])
    else: ap(a[0], a[1], a[2], "--kiem" in a)
