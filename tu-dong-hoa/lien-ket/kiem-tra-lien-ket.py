#!/usr/bin/env python3
"""Công cụ kiểm tra liên kết (luật: co-so-tri-thuc/quy-uoc-lien-ket.md).

- Báo link gãy (link tương đối tới file không có, [[ghi-nho]] không có) → trả mã lỗi 1.
- Báo file mồ côi (không file nào nối tới, chỉ mục không tính) và file thiếu mô tả → chỉ cảnh báo.
- Sinh lại chỉ mục: mỗi file một dòng (đường dẫn, mô tả, số nối tới).

Hai kho:
  - bộ não (mặc định): chỉ mục co-so-tri-thuc/chi-muc.md, bản đồ ở ban-do/.
  - kho khác (--goc <thư mục>, ví dụ sổ tay riêng chỉ trên máy): chỉ mục chi-muc.md và bản đồ ban-do.md ở gốc kho.

Mô tả một file lấy theo thứ tự: khối `description:` đầu file → bảng MIEN_MO_TA (chỉ bộ não) → chữ sau " — " ở dòng
bản đồ nối tới file đó (hoặc tới thư mục chứa nó) → tiêu đề đầu tiên (tính là thiếu mô tả).
Link tới một thư mục tính là nối tới mọi file .md nằm thẳng trong thư mục đó (dùng cho sổ theo tháng, theo ngày).

Phần riêng Mac chính (tu-dong-hoa/phan-rieng-mac.txt, repo riêng tư; David 20/11/2026): không vào chỉ mục, không tính vào đồ thị
chung (để chỉ mục giống nhau ở mọi máy); file chung KHÔNG được link vào phần riêng (máy khác sẽ gãy) — ghi bằng chữ `đường/dẫn`.
Link tới ghi nhớ riêng máy (thiet-bi-*, không lên GitHub) thiếu thì bỏ qua.

Dùng:
  python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py                      kiểm bộ não + sinh chỉ mục
  python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py --goc ~/Documents/2-ca-nhan/so-tay
  thêm --chi-tiet để liệt kê từng file mồ côi / thiếu mô tả
"""
import os, re, sys, glob

NAO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Bộ não — file nạp mỗi phiên, hồ sơ David, trang GitHub, file bị chép thành lời nhắc: không thêm khối mô tả, mô tả ghi ở đây.
MIEN_MO_TA = {
    "AGENTS.md": "Cửa vào cho mọi AI: thứ tự đọc, sáu luật không được phá, bảng chọn skill theo việc.",
    "CLAUDE.md": "Cấu hình Claude Code của repo: nạp AGENTS.md.",
    "co-so-tri-thuc/chi-dan-toan-cuc.md": "Luật chung của David cho mọi phiên Claude (bản gốc của ~/.claude/CLAUDE.md), nạp hồ sơ david.md.",
    "co-so-tri-thuc/david.md": "Hồ sơ David Trần cho Claude: là ai, cách làm việc, luật cá nhân, bảng tra mục 4–9 (nghề, nội dung, CCL, huyền học).",
    "co-so-tri-thuc/ho-so-ca-nhan.md": "Hồ sơ thấu hiểu bản thân David: tính cách, điểm mạnh, điểm cần cải thiện, nguyên tắc, động cơ.",
    "README.md": "Trang đầu repo bo-nao-david trên GitHub: bộ não dùng chung của David, cấu trúc, cách dùng.",
    "tu-dong-hoa/so-tay/quy-tac-bot.md": "Luật bot Sổ nhớ Telegram (chép thành CLAUDE.md của bot): ghi gì, trả lời thế nào, tin nhắn tổng hợp.",
    "co-so-tri-thuc/bo-nho/MEMORY.md": "Mục lục bộ nhớ Claude Code: mỗi ghi nhớ một dòng, nhóm quy tắc / bộ não / video / thiết bị.",
}
BO_QUA = ("/node_modules/", "/assets/")
# Dữ liệu thô chép lại từ nơi khác (kho gom theo ngày): không kiểm link bên trong.
THO = ("kho-du-lieu/ngay/",)

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def cau_hinh():
    if "--goc" in sys.argv:
        goc = os.path.abspath(os.path.expanduser(sys.argv[sys.argv.index("--goc") + 1]))
        la_nao = goc == NAO
    else:
        goc, la_nao = NAO, True
    if la_nao:
        return goc, "co-so-tri-thuc/chi-muc.md", lambda f: f.startswith("ban-do/"), MIEN_MO_TA, {"AGENTS.md", "CLAUDE.md", "README.md"}
    return goc, "chi-muc.md", lambda f: f == "ban-do.md", {}, {"CLAUDE.md", "ban-do.md"}


def doc_rieng(goc):
    p = os.path.join(goc, "tu-dong-hoa", "phan-rieng-mac.txt")
    if not os.path.exists(p):
        return ()
    return tuple(l.strip() for l in open(p, encoding="utf-8") if l.strip() and not l.startswith("#"))


def ds_file(goc):
    out = []
    for f in glob.glob(f"{goc}/**/*.md", recursive=True):
        rel = os.path.relpath(f, goc)
        if any(p.startswith(".") for p in rel.split(os.sep)) or any(b in f for b in BO_QUA) or os.path.islink(f):
            continue
        out.append(rel)
    return sorted(out)


def mo_ta_dau_file(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        m = re.search(r"^description:\s*(.+)$", text[4:end], re.M)
        if m:
            return m.group(1).strip().strip('"').strip("'").replace('\\"', '"')
    return None


def tieu_de(text):
    for l in text.splitlines():
        if l.startswith("# "):
            return l[2:].strip()
    return ""


def tang_cua(goc, f, _c={}):
    """Tầng của file theo co-so-tri-thuc/tang.json (trục tri thức mục 2); không có bảng thì None."""
    import fnmatch, json
    if 'q' not in _c:
        p = os.path.join(goc, "co-so-tri-thuc", "tang.json")
        _c['q'] = json.load(open(p, encoding="utf-8"))["quy_tac"] if os.path.exists(p) else []
    for mau, t in _c['q']:
        if fnmatch.fnmatch(f, mau) or (mau.endswith("/**") and f.startswith(mau[:-2])) or (mau.startswith("**/") and fnmatch.fnmatch(os.path.basename(f), mau[3:])):
            return t
    return None

def main():
    goc, chi_muc, la_ban_do, mien, goc_vao = cau_hinh()
    goc_vao = goc_vao | {chi_muc}
    chi_tiet = "--chi-tiet" in sys.argv
    RIENG = doc_rieng(goc) if goc == NAO else ()
    # phần riêng Mac + ghi nhớ riêng máy (thiet-bi-*, không lên GitHub): ngoài chỉ mục để chỉ mục ở mọi máy giống hệt nhau
    la_rieng = lambda f: (goc == NAO and os.path.basename(f).startswith("thiet-bi-")) or \
        any(f == r.rstrip("/") or (r.endswith("/") and f.startswith(r)) for r in RIENG)
    tat_ca = [f for f in ds_file(goc) if f != chi_muc]
    files = [f for f in tat_ca if not la_rieng(f)]          # phần chung: vào chỉ mục, đồ thị
    rieng = [f for f in tat_ca if la_rieng(f)]              # phần riêng (chỉ có trên Mac chính): chỉ kiểm link gãy
    fset = set(files)
    stem = {}
    for f in files:
        stem.setdefault(os.path.splitext(os.path.basename(f))[0], []).append(f)
    toi = {f: set() for f in files}
    mo_ta_ban_do = {}
    gay = []
    text = {f: open(os.path.join(goc, f), encoding="utf-8", errors="ignore").read() for f in files}

    def noi(nguon, dich, dong=None):
        if dich in toi and dich != nguon:
            toi[dich].add(nguon)
            if dong and la_ban_do(nguon) and " — " in dong and dich not in mo_ta_ban_do:
                mo_ta_ban_do[dich] = dong.split(" — ", 1)[1].strip()

    for f in rieng:
        text[f] = open(os.path.join(goc, f), encoding="utf-8", errors="ignore").read()
    for f in files + rieng:
        if f.startswith(THO):
            continue
        chung = f not in rieng
        for dong in CODE.sub("", text[f]).splitlines():
            for m in LINK.finditer(dong):
                t = m.group(1).split("#")[0].split("?")[0]
                if not t or re.match(r"^[a-z]+:", t) or t.startswith(("~", "/", "<", "$")):
                    continue
                dich = os.path.normpath(os.path.join(os.path.dirname(f), t))
                duong = os.path.join(goc, dich)
                if os.path.basename(dich).startswith("thiet-bi-"):
                    continue                                    # ghi nhớ riêng máy: máy khác không có là đúng, không tính
                elif chung and (la_rieng(dich) or la_rieng(dich + "/")):
                    gay.append((f, t + "  (phần riêng Mac — ghi bằng chữ `…`, đừng link)"))
                elif not os.path.exists(duong):
                    gay.append((f, t))
                elif not chung:
                    continue                                    # link từ phần riêng: chỉ cần không gãy
                elif os.path.isdir(duong):
                    con = [c for c in fset if os.path.dirname(c) == dich]
                    for cand in ("README.md", "SKILL.md"):
                        if os.path.join(dich, cand) in fset:
                            con = [os.path.join(dich, cand)]
                            break
                    for c in con:
                        noi(f, c, dong)
                else:
                    noi(f, dich, dong)
            for m in WIKI.finditer(dong) if chung else ():
                ten = m.group(1).strip()
                ten = ten[:-3] if ten.endswith(".md") else ten
                ung = stem.get(os.path.basename(ten))
                if not ung:
                    gay.append((f, f"[[{ten}]]"))
                for d in ung or []:
                    noi(f, d)

    desc = {}
    for f in files:
        d = mo_ta_dau_file(text[f]) or mien.get(f) or mo_ta_ban_do.get(f)
        desc[f] = (d, True) if d else (tieu_de(text[f]), False)
    mo_coi = [f for f in files if not toi[f] and f not in goc_vao]
    thieu = [f for f in files if not desc[f][1]]

    nhom = {}
    for f in files:
        nhom.setdefault(f.split("/")[0] if "/" in f else "(gốc)", []).append(f)
    ten_kho = "bộ não" if goc == NAO else os.path.basename(goc)
    luat = "[quy-uoc-lien-ket.md](quy-uoc-lien-ket.md)" if goc == NAO else "`co-so-tri-thuc/quy-uoc-lien-ket.md` trong bộ não"
    dong = [
        "---",
        f"description: Chỉ mục tự sinh của {ten_kho} — mỗi file .md một dòng (đường dẫn, tầng theo trục tri thức, mô tả, số file nối tới); Claude grep file này trước khi tìm toàn bộ.",
        "---",
        "",
        f"# Chỉ mục {ten_kho}",
        "",
        f"> Máy tự sinh (`tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py`), **không sửa tay**. Cách dùng: `grep -i \"<từ khoá>\" {chi_muc}`. Luật: {luat}.",
        "",
    ]
    for g in sorted(nhom):
        dong += [f"## {g}", ""]
        for f in nhom[g]:
            rel = os.path.relpath(f, os.path.dirname(chi_muc) or ".")
            t = tang_cua(goc, f)
            dong.append(f"- [{f}]({rel}) — " + (f"tầng {t} · " if t is not None else "") + f"{desc[f][0]} · ←{len(toi[f])}")
        dong.append("")
    noi_dung = "\n".join(dong)
    p = os.path.join(goc, chi_muc)
    if not os.path.exists(p) or open(p, encoding="utf-8").read() != noi_dung:
        open(p, "w", encoding="utf-8").write(noi_dung)

    print(f"Liên kết {ten_kho}: {len(files) + 1} file · link gãy {len(gay)} · mồ côi {len(mo_coi)} · thiếu mô tả {len(thieu)}")
    for f, t in gay:
        print(f"  ✗ gãy: {f} → {t}")
    if chi_tiet:
        for f in mo_coi:
            print(f"  · mồ côi: {f}")
        for f in thieu:
            print(f"  · thiếu mô tả: {f}")
    elif mo_coi or thieu:
        print("  (thêm --chi-tiet để xem từng file mồ côi / thiếu mô tả)")
    sys.exit(1 if gay else 0)


if __name__ == "__main__":
    main()
