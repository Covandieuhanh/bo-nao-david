#!/usr/bin/env python3
"""Máy gom: đọc phần MỚI kể từ lần trước ở mọi nguồn của David, ghi một file ngày.

Không gọi AI, không tốn token. Dữ liệu ra chỉ ở máy (~/Documents/2-ca-nhan/so-tay/kho-du-lieu/), không lên GitHub.
Chạy:  python3 -I tu-dong-hoa/thu-thap-du-lieu/gom.py [--lan-dau-ngay N] [--thu]
  --lan-dau-ngay N  lần đầu (chưa có mốc) lấy N ngày gần nhất (mặc định 7)
  --thu             in ra màn hình, không ghi file, không dời mốc
Nguồn và lý do: ky-nang/san-pham-hoa/SKILL.md mục "Nguồn".
"""
import difflib, glob, hashlib, json, os, re, sys, time
from datetime import datetime

HOME = os.path.expanduser("~")
SN = f"{HOME}/Documents/2-ca-nhan/so-tay"
KHO = f"{SN}/kho-du-lieu"
MOC = f"{KHO}/.moc.json"
BAN_SAO = f"{KHO}/.ban-sao"
GIOI_HAN_MUC = 15000      # ký tự tối đa mỗi mục trong file ngày
GIOI_HAN_TIN = 700        # ký tự tối đa mỗi lời David trong phiên

args = sys.argv[1:]
THU = "--thu" in args
LAN_DAU_NGAY = int(args[args.index("--lan-dau-ngay") + 1]) if "--lan-dau-ngay" in args else 7

moc = json.load(open(MOC)) if os.path.exists(MOC) else {}
lan_dau = not moc
nguong = time.time() - LAN_DAU_NGAY * 86400 if lan_dau else 0
moi = {}


def doc(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def doi(p):
    """True nếu file đổi kể từ lần trước (theo mtime + kích thước)."""
    try:
        st = os.stat(p)
    except OSError:
        return False
    k = f"{st.st_mtime:.0f}:{st.st_size}"
    cu = moc.get("f", {}).get(p)
    moi.setdefault("f", {})[p] = k
    if cu == k:
        return False
    if cu is None and lan_dau and st.st_mtime < nguong:
        return False
    return True


def ban_sao(p):
    return f"{BAN_SAO}/{hashlib.md5(p.encode()).hexdigest()}.txt"


def dong_them(p):
    """Các dòng mới thêm hoặc sửa so với bản sao lần trước (file chưa có bản sao: cả file)."""
    nay = doc(p)
    cu = doc(ban_sao(p))
    moi.setdefault("sao", {})[p] = nay
    if not cu:
        return nay.strip()
    them = [l[1:] for l in difflib.unified_diff(cu.splitlines(), nay.splitlines(), lineterm="", n=0)
            if l.startswith("+") and not l.startswith("+++")]
    return "\n".join(x for x in them if x.strip())


def cat(s, n=GIOI_HAN_MUC):
    return s if len(s) <= n else s[:n] + f"\n… (cắt bớt {len(s) - n} ký tự, đọc file gốc nếu cần)"


muc = []  # (tiêu đề, nội dung)

# 1. Phiên Claude: chỉ lời David (người dùng gõ), bỏ thông báo máy và phiên bot Sổ nhớ (nội dung bot đã ghi vào sổ nhớ).
BO_DU_AN = ("so-tay", "so-nho", "scratch-workspaces", "-private-tmp", "-private-var")  # tmp: lời máy nhờ Haiku viết lại yêu cầu duyệt
BO_LOI = ("<", "This session is being continued", "[Request interrupted", "Làm việc trong thư mục", "[TOM-TAT", "[HOI-THOI", "[CHO-DUYET", "[TU-HOC", "Caveat:")
phien_txt = []
for f in sorted(glob.glob(f"{HOME}/.claude/projects/*/*.jsonl"), key=os.path.getmtime):
    if any(b in f for b in BO_DU_AN):
        continue
    try:
        st = os.stat(f)
    except OSError:
        continue
    vt = moc.get("jsonl", {}).get(f)
    if vt is None and lan_dau and st.st_mtime < nguong:
        moi.setdefault("jsonl", {})[f] = st.st_size
        continue
    vt = vt or 0
    if st.st_size < vt:
        vt = 0
    loi = []
    with open(f, "rb") as fh:
        fh.seek(vt)
        for raw in fh:
            try:
                d = json.loads(raw)
            except ValueError:
                continue
            if d.get("type") != "user" or d.get("isMeta"):
                continue
            c = d.get("message", {}).get("content")
            if isinstance(c, list):
                c = " ".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
            if not isinstance(c, str):
                continue
            c = c.strip()
            if len(c) < 12 or c.startswith(BO_LOI):   # bỏ "ok", "chuyển": không có ý
                continue
            m = re.search(r"Yêu cầu nguyên văn của David:\s*(.*)", c, flags=re.S)   # việc giao qua Telegram: chỉ giữ lời David
            if m:
                c = "[Telegram] " + m.group(1)
            elif c.startswith(("Đây là việc David giao", "Viết lại yêu cầu cấp quyền", "Thử ")):
                continue
            c = re.sub(r"^David (trả lời|nhắn) qua Telegram:\s*", "[Telegram] ", c)
            c = re.sub(r"<pasted_content[^>]*>.*?</pasted_content[^>]*>", "[đoạn dán]", c, flags=re.S)
            gio = (d.get("timestamp") or "")[:16].replace("T", " ")
            loi.append(f"- {gio} · {c[:GIOI_HAN_TIN].replace(chr(10), ' ')}")
        moi.setdefault("jsonl", {})[f] = fh.tell()
    if loi:
        du_an = os.path.basename(os.path.dirname(f)).replace("-Users-moon-", "").replace("-Users-moon", "~")
        phien_txt.append(f"### Phiên {os.path.basename(f)[:8]} ({du_an})\n" + "\n".join(loi))
if phien_txt:
    muc.append(("Lời David trong các phiên Claude", cat("\n\n".join(phien_txt), 40000)))

# 2. Sổ nhớ (bot Telegram ghi): phần mới thêm.
for ten in ["danh-sach-viec.md", "y-tuong.md", "kien-thuc.md", "lich-hen.md", "nhom.md", "viec-da-giao.md", "bao-cao-claude.md"]:
    p = f"{SN}/{ten}"
    if doi(p):
        t = dong_them(p)
        if t:
            muc.append((f"Sổ nhớ · {ten}", t))
for p in sorted(glob.glob(f"{SN}/nhat-ky/*.md")):
    if doi(p):
        t = dong_them(p)
        if t:
            muc.append((f"Nhật ký · {os.path.basename(p)}", t))

# 3. Tổng hợp tin nhắn (Zalo, Messenger, Telegram) đã làm sẵn mỗi sáng.
for p in sorted(glob.glob(f"{SN}/tin-nhan/tong-hop-*.md")):
    if doi(p):
        t = dong_them(p)
        if t:
            muc.append((f"Tin nhắn · {os.path.basename(p)}", t))

# 4. Video: lời nói (chép lời bản gốc), bài đăng, số liệu. Bỏ bản trùng nội dung (bản sạch, clip con).
da_thay = set(moc.get("bam_loi", []))
for p in sorted(glob.glob(f"{HOME}/Movies/**/check/goc/transcript.srt", recursive=True)):
    if "/thu-" in p or not doi(p):
        continue
    chu = " ".join(l.strip() for l in doc(p).splitlines()
                   if l.strip() and not l.strip().isdigit() and "-->" not in l)
    bam = hashlib.md5(chu[:2000].encode()).hexdigest()
    if bam in da_thay:
        continue
    da_thay.add(bam)
    muc.append((f"Lời trong video · {p.replace(HOME + '/Movies/', '')}", chu))
moi["bam_loi"] = sorted(da_thay)
for p in sorted(glob.glob(f"{HOME}/Movies/**/dang-bai.md", recursive=True) + glob.glob(f"{HOME}/Movies/**/so-lieu.md", recursive=True)
                + [f"{HOME}/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md"]):
    if doi(p):
        if p.endswith("so-lieu.md") and not re.search(r"Lượt xem\s*\|\s*[\d.,]+", doc(p)):
            continue                          # mẫu số liệu chưa điền: chưa có gì để học
        t = dong_them(p)
        if t:
            muc.append((f"Video · {p.replace(HOME + '/Movies/', '')}", t))

# (Không gom tín hiệu tự học ~/.claude/hoc-lien-tuc: trùng lời David trong phiên ở mục 1.)

# ---- ghi
ngay = datetime.now().strftime("%Y-%m-%d")
dau = (f"# Kho gom {ngay}\n\nPhần mới kể từ {moc.get('luc', f'{LAN_DAU_NGAY} ngày trước (lần đầu)')} tới "
       f"{datetime.now():%Y-%m-%d %H:%M}. Dữ liệu thô, chỉ ở máy. Phân loại: skill san-pham-hoa việc 1.\n")
than = "\n".join(f"\n## {i}. {tieu}\n\n{nd if len(nd) > GIOI_HAN_MUC and tieu.startswith('Lời David trong') else cat(nd)}\n" for i, (tieu, nd) in enumerate(muc, 1)) or "\nKhông có gì mới.\n"
ra = dau + than

if THU:
    print(ra[:6000]); print("\n".join(f"  · {t} ({len(n)} ký tự)" for t, n in muc)); print(f"\n[thử] {len(muc)} mục, {len(ra)} ký tự, không ghi.")
    sys.exit(0)

os.makedirs(f"{KHO}/ngay", exist_ok=True); os.makedirs(BAN_SAO, exist_ok=True)
out = f"{KHO}/ngay/{ngay}.md"
if muc:
    if os.path.exists(out):                   # chạy lần hai trong ngày: nối thêm
        ra = doc(out) + f"\n---\n\nThêm lúc {datetime.now():%H:%M}\n" + than
    open(out, "w", encoding="utf-8").write(ra)
for p, nd in moi.pop("sao", {}).items():
    open(ban_sao(p), "w", encoding="utf-8").write(nd)
moi["luc"] = datetime.now().strftime("%Y-%m-%d %H:%M")
for k in ("f", "jsonl"):
    moi[k] = {**moc.get(k, {}), **moi.get(k, {})}
json.dump(moi, open(MOC, "w"), ensure_ascii=False, indent=0)
print(f"{out} · {len(muc)} mục · {len(ra)} ký tự" if muc else "Không có gì mới")
