#!/usr/bin/env python3
"""Máy kiểm liên kết của bộ não (luật: co-so-tri-thuc/quy-uoc-lien-ket.md).

- Báo link gãy (link tương đối tới file không có, [[ghi-nho]] không có) → trả mã lỗi 1.
- Báo file mồ côi (không file nào nối tới, chỉ mục không tính) và file thiếu mô tả → chỉ cảnh báo.
- Sinh lại co-so-tri-thuc/chi-muc.md: mỗi file một dòng (đường dẫn, mô tả, số nối tới).

Dùng:
  python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py           kiểm + sinh chỉ mục
  python3 tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py --chi-tiet  liệt kê đủ từng file mồ côi / thiếu mô tả
"""
import os, re, sys, glob

GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CHI_MUC = "co-so-tri-thuc/chi-muc.md"

# File nạp mỗi phiên, hồ sơ David, trang GitHub, file bị chép thành lời nhắc: không thêm khối mô tả vào file, mô tả ghi ở đây.
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
# Cửa vào: không cần ai nối tới.
GOC_VAO = {"AGENTS.md", "CLAUDE.md", "README.md", CHI_MUC}
BO_QUA_THU_MUC = ("/.git/", "/node_modules/", "/.obsidian/", "/assets/")

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def ds_file():
    out = []
    for f in glob.glob(f"{GOC}/**/*.md", recursive=True):
        if any(b in f for b in BO_QUA_THU_MUC) or os.path.islink(f):
            continue
        out.append(os.path.relpath(f, GOC))
    return sorted(out)


def mo_ta(rel, text):
    if rel in MIEN_MO_TA:
        return MIEN_MO_TA[rel], True
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        m = re.search(r"^description:\s*(.+)$", text[4:end], re.M)
        if m:
            return m.group(1).strip().strip('"').strip("'"), True
    for l in text.splitlines():  # dự phòng: tiêu đề đầu tiên
        if l.startswith("# "):
            return l[2:].strip(), False
    return "", False


def main():
    chi_tiet = "--chi-tiet" in sys.argv
    files = ds_file()
    fset = set(files)
    stem = {}
    for f in files:
        stem.setdefault(os.path.splitext(os.path.basename(f))[0], []).append(f)
    toi = {f: set() for f in files}
    gay = []
    desc = {}
    for f in files:
        text = open(os.path.join(GOC, f), encoding="utf-8", errors="ignore").read()
        desc[f] = mo_ta(f, text)
        body = CODE.sub("", text)
        for m in LINK.finditer(body):
            t = m.group(1).split("#")[0].split("?")[0]
            if not t or re.match(r"^[a-z]+:", t) or t.startswith(("~", "/", "<", "$")):
                continue
            dich = os.path.normpath(os.path.join(os.path.dirname(f), t))
            if os.path.exists(os.path.join(GOC, dich)):
                if os.path.isdir(os.path.join(GOC, dich)):
                    for cand in ("README.md", "SKILL.md"):
                        if os.path.join(dich, cand) in fset:
                            dich = os.path.join(dich, cand)
                            break
                if dich in toi and dich != f:
                    toi[dich].add(f)
            else:
                gay.append((f, t))
        for m in WIKI.finditer(body):
            ten = m.group(1).strip()
            ten = os.path.splitext(ten)[0] if ten.endswith(".md") else ten
            ung = stem.get(os.path.basename(ten))
            if not ung:
                gay.append((f, f"[[{ten}]]"))
                continue
            for d in ung:
                if d != f:
                    toi[d].add(f)

    # Chỉ mục không tính là nối tới.
    for f in toi:
        toi[f].discard(CHI_MUC)
    mo_coi = [f for f in files if not toi[f] and f not in GOC_VAO]
    thieu = [f for f in files if not desc[f][1] and f != CHI_MUC]

    # Sinh chỉ mục.
    nhom = {}
    for f in files:
        if f == CHI_MUC:
            continue
        nhom.setdefault(f.split("/")[0] if "/" in f else "(gốc)", []).append(f)
    dong = [
        "---",
        "description: Chỉ mục tự sinh của bộ não — mỗi file .md một dòng (đường dẫn, mô tả, số file nối tới); Claude grep file này trước khi tìm toàn repo.",
        "---",
        "",
        "# Chỉ mục bộ não",
        "",
        "> Máy tự sinh (`tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py`), **không sửa tay**: sửa mô tả ở đầu từng file. Cách dùng: `grep -i \"<từ khoá>\" co-so-tri-thuc/chi-muc.md`. Luật: [quy-uoc-lien-ket.md](quy-uoc-lien-ket.md).",
        "",
    ]
    for g in sorted(nhom):
        dong.append(f"## {g}")
        dong.append("")
        for f in nhom[g]:
            rel = os.path.relpath(f, os.path.dirname(CHI_MUC))
            d = desc[f][0].replace("\n", " ")
            dong.append(f"- [{f}]({rel}) — {d} · ←{len(toi[f])}")
        dong.append("")
    noi_dung = "\n".join(dong)
    p = os.path.join(GOC, CHI_MUC)
    cu = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    if cu != noi_dung:
        open(p, "w", encoding="utf-8").write(noi_dung)

    print(f"Liên kết: {len(files)} file · link gãy {len(gay)} · mồ côi {len(mo_coi)} · thiếu mô tả {len(thieu)}")
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
