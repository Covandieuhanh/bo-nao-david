#!/usr/bin/env python3
"""Bot Điều hành (Telegram): trạm điều khiển các phiên Claude trên Mac. Chạy bằng script, KHÔNG cần phiên Claude:
trả lời tức thì, không tốn token. Bot Sổ nhớ (tu-dong-hoa/so-tay/) chỉ còn lo đời sống: ghi sổ, nhắc, thói quen, tin nhắn tổng hợp.

Làm gì:
- Duyệt từ xa: tin 🔐 / ❓ của duyet-tu-xa.py có nút bấm; bấm nút hoặc trả lời (trích) tin → ghi .trang-thai/duyet/<mã>.tra.
- Giao việc: nhắn một câu bình thường → giao-viec.sh (mở phiên Claude hiện trong app). "#N <lời>" hoặc trả lời tin #N → làm tiếp.
  "đóng #N" hoặc nút [Đóng phiên #N] → đóng phiên.
- Nhắn phiên David tự mở: "@<từ khoá hoặc số>: <lời>" → hop-thu-phien.py gui. /phien liệt kê.
- Lệnh: /dang_chay /viec /viec_do /phien /suc_khoe /vang /ve /huong_dan.
- Tin thoại: nghe bằng so-tay/nghe-thoai.sh rồi xử lý như chữ.
Token: ~/.claude/channels/dieu-hanh/.env (TELEGRAM_BOT_TOKEN=…, không lên GitHub). Chỉ nhận tin của David (allowFrom của Sổ nhớ).
Chạy: launchd com.david.dieu-hanh (cai-dat.sh). Thử không cần Telegram: python3 -I bot.py --thu "<tin>".
"""
import glob, json, os, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request

NAO = os.path.expanduser("~/Documents/bo-nao-david")
SO_TAY = os.path.join(NAO, "tu-dong-hoa", "so-tay")
DATA = os.path.expanduser("~/Documents/2-ca-nhan/so-tay")
TT = os.path.join(DATA, ".trang-thai")
DUYET = os.path.join(TT, "duyet")
KENH = os.path.expanduser("~/.claude/channels/dieu-hanh")
LOG = os.path.join(TT, "dieu-hanh.log")
OFFSET = os.path.join(TT, "dieu-hanh-offset")
NHIP = os.path.join(TT, "dieu-hanh-nhip")
PATH = ":".join([os.path.expanduser("~/.bun/bin"), os.path.expanduser("~/.local/bin"), "/opt/homebrew/bin",
                 "/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"])
THU = False          # --thu: in ra thay vì gửi Telegram
DA_IN = []


def ghi(s):
    os.makedirs(TT, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(time.strftime("%F %T ") + s.replace("\n", " ")[:300] + "\n")


def doc_env(p, k):
    try:
        for l in open(p):
            if l.startswith(k + "="):
                return l.split("=", 1)[1].strip().strip("'\"")
    except Exception:
        pass
    return ""


TOKEN = doc_env(os.path.join(KENH, ".env"), "TELEGRAM_BOT_TOKEN")


def chat_david():
    c = doc_env(os.path.join(KENH, ".env"), "TELEGRAM_CHAT_ID")
    if c:
        return c
    try:
        return str(json.load(open(os.path.expanduser("~/.claude/channels/so-tay/access.json")))["allowFrom"][0])
    except Exception:
        return ""


CHAT = chat_david()


def api(lenh, **thong_so):
    if THU:
        DA_IN.append((lenh, thong_so)); print(f"[{lenh}] {thong_so.get('text', '')}{' ' + str(thong_so.get('reply_markup')) if thong_so.get('reply_markup') else ''}")
        return {"ok": True, "result": {}}
    for k, v in list(thong_so.items()):
        if isinstance(v, (dict, list)):
            thong_so[k] = json.dumps(v, ensure_ascii=False)
    du_lieu = urllib.parse.urlencode(thong_so).encode()
    cho = int(thong_so.get("timeout", 0)) + 20
    with urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/{lenh}", data=du_lieu, timeout=cho) as r:
        return json.load(r)


def gui(chu, nut=None, tra_loi_cho=None):
    chu = chu.strip() or "(trống)"
    for i in range(0, len(chu), 3800):
        p = {"chat_id": CHAT, "text": chu[i:i + 3800]}
        if nut and i + 3800 >= len(chu):
            p["reply_markup"] = {"inline_keyboard": nut}
        if tra_loi_cho and i == 0:
            p["reply_to_message_id"] = tra_loi_cho
        try:
            api("sendMessage", **p)
        except Exception as e:
            ghi(f"gui loi {e}")


def chay(lenh, gioi_han=120):
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE") and k != "TELEGRAM_STATE_DIR"}
    env["PATH"] = PATH
    try:
        r = subprocess.run(lenh, capture_output=True, text=True, timeout=gioi_han, cwd=NAO, env=env)
        return (r.stdout + ("\n" + r.stderr if r.returncode and r.stderr else "")).strip()
    except subprocess.TimeoutExpired:
        return "Lệnh chạy quá lâu, đã dừng chờ."
    except Exception as e:
        return f"Lỗi chạy lệnh: {e}"


def khong_dau(s):
    s = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").strip()


# ---------- Duyệt từ xa ----------

def cho_duyet():
    """Yêu cầu đang chờ: [(mã, dữ liệu)], bỏ yêu cầu đã có câu trả lời."""
    ds = []
    for f in sorted(glob.glob(os.path.join(DUYET, "*.json")), key=os.path.getmtime):
        ma = os.path.basename(f)[:-5]
        if os.path.exists(os.path.join(DUYET, ma + ".tra")):
            continue
        try:
            ds.append((ma, json.load(open(f))))
        except Exception:
            pass
    return ds


DONG_Y = {"ok", "oke", "okay", "duyet", "dong y", "duoc", "cho phep", "lam di", "yes", "y", "co", "uh", "u"}
TU_CHOI = {"khong", "ko", "k", "no", "n", "dung", "tu choi", "thoi", "huy"}


def chuan_tra(du_lieu, chu):
    """Đổi lời David thành nội dung file .tra: xin phép → ok / khong <lý do>; câu hỏi → nguyên văn."""
    if du_lieu.get("cong_cu") == "AskUserQuestion":
        return chu.strip()
    k = khong_dau(chu).rstrip(".! ")
    if k in DONG_Y:
        return "ok"
    dau = k.split(" ", 1)[0].strip(",.;:!")
    if k in TU_CHOI or dau in ("khong", "ko", "dung", "thoi"):
        ly_do = chu.strip().split(" ", 1)[1].strip(" ,.;:") if " " in chu.strip() else ""
        return ("khong " + ly_do).strip()
    return None


def ghi_tra(ma, noi_dung):
    if not os.path.exists(os.path.join(DUYET, ma + ".json")):
        return False
    with open(os.path.join(DUYET, ma + ".tra"), "w") as f:
        f.write(noi_dung)
    ghi(f"duyet {ma}: {noi_dung[:60]}")
    return True


def bao_da_tra(ma, noi_dung, du_lieu):
    if du_lieu.get("cong_cu") == "AskUserQuestion":
        return f"Đã gửi câu trả lời của anh cho Claude ({ma})."
    return f"Đã cho phép ({ma})." if noi_dung == "ok" else f"Đã từ chối ({ma})."


# ---------- Xử lý tin ----------

HUONG_DAN = """Bot Điều hành: điều khiển các phiên Claude trên Mac (ghi nhớ, nhắc việc, thói quen vẫn nhắn bot Sổ nhớ).

• Nhắn một câu bình thường → giao việc cho Claude (mở phiên mới, xem trong app Claude).
• #N <lời> (hoặc trả lời tin #N) → nhắn tiếp cho việc #N.
• đóng #N → đóng phiên việc #N.
• @<tên hoặc số phiên>: <lời> → nhắn cho phiên anh tự mở (xem số bằng /phien).
• Tin 🔐 ❓ → bấm nút, hoặc trả lời tin đó.
• /dang_chay · /viec · /viec_do · /phien · /suc_khoe
• /vang (đi vắng: mọi yêu cầu duyệt lên đây ngay) · /ve (ở máy)"""

LENH = [("dang_chay", "Claude đang làm gì"), ("viec", "Việc đã giao gần đây"), ("viec_do", "Việc dở, chờ anh quyết"),
        ("phien", "Phiên đang mở (để nhắn @số)"), ("suc_khoe", "Sức khoẻ hai bot"), ("vang", "Tôi đi vắng"),
        ("ve", "Tôi ở máy"), ("huong_dan", "Cách dùng bot")]


def viec_gan_day(n=8):
    try:
        dong = [l for l in open(os.path.join(DATA, "viec-da-giao.md")) if re.match(r"^\| \d+ \|", l)]
    except Exception:
        return "Chưa có việc nào."
    ra = []
    for l in dong[-n:]:
        c = [x.strip() for x in l.split("|")]
        ra.append(f"#{c[1]} · {c[3][:70]} · {c[5]}")
    return "Việc đã giao gần đây:\n" + "\n".join(ra)


def viec_do():
    try:
        t = open(os.path.join(NAO, "bao-cao-trang-thai.md")).read()
    except Exception:
        return "Không đọc được bao-cao-trang-thai.md."
    bo = ""
    try:
        bo = khong_dau(open(os.path.join(DATA, "bo-qua.md")).read())
    except Exception:
        pass

    def muc(ten):
        m = re.search(r"^## " + re.escape(ten) + r".*?$(.*?)(?=^## |\Z)", t, re.M | re.S)
        return m.group(1) if m else ""
    dang = []
    for l in muc("Đang làm dở").splitlines():
        if l.startswith("|") and not re.match(r"^\|\s*-", l) and "Việc" not in l.split("|")[1]:
            ten = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", l.split("|")[1]).strip()
            if ten and khong_dau(ten)[:30] not in bo:
                dang.append("• " + ten[:110])
    hoi = [l.strip() for l in muc("Câu hỏi còn mở với David").splitlines() if l.strip().startswith(("-", "1", "2", "3", "4", "5"))]
    return ("Đang làm dở:\n" + "\n".join(dang[:15]) if dang else "Không có việc dở.") + \
           ("\n\nCâu hỏi chờ anh:\n" + "\n".join(h[:200] for h in hoi[:8]) if hoi else "")


def suc_khoe():
    kq = chay(["bash", os.path.join(SO_TAY, "viec-dang-chay.sh")], 60)
    i = kq.find("## Sức khoẻ bot")
    so_nho = kq[i:].strip() if i >= 0 else "(không đọc được phần sức khoẻ bot Sổ nhớ)"
    return so_nho + f"\n\nBot Điều hành: đang chạy (đã nhận lệnh này)."


BAI_DANG = re.compile(r"\b(loc lai|loc trung|sua bai|bai dang)\b")


def giao(chu):
    if BAI_DANG.search(khong_dau(chu)):   # bài Facebook cá nhân: kèm bối cảnh để phiên làm đúng chỗ
        chu = (f"Bài đăng Facebook cá nhân (du-an/lich-dang-bai.md): {chu}. Lọc lại = chạy bước 0 của "
               f"tu-dong-hoa/lich/loi-giao/lich-dang-tuan.md rồi bù bài nếu có bài bị bỏ.")
    return chay(["bash", os.path.join(SO_TAY, "giao-viec.sh"), chu], 60) or "Đã giao."


def xu_ly(chu, tra_loi=None, ma_tin=None):
    """chu: lời David; tra_loi: chữ của tin David đang trích (nếu có)."""
    chu = chu.strip()
    if not chu:
        return
    k = khong_dau(chu)

    # 1. Trả lời (trích) một tin 🔐 ❓ hoặc tin #N.
    if tra_loi:
        m = re.search(r"Mã yêu cầu: ([A-Z0-9]{4})", tra_loi)
        if m:
            ma = m.group(1); f = os.path.join(DUYET, ma + ".json")
            if not os.path.exists(f):
                return gui("Yêu cầu này đã hết hạn hoặc đã được xử lý.")
            d = json.load(open(f)); nd = chuan_tra(d, chu)
            if nd is None:
                nd = "khong " + chu   # xin phép mà trả lời bằng câu dài: coi là từ chối kèm lời dặn, để Claude đọc
            ghi_tra(ma, nd); return gui(bao_da_tra(ma, nd, d))
        m = re.match(r"^#(\d+)\b", tra_loi.strip())
        if m:
            return gui(chay(["bash", os.path.join(SO_TAY, "giao-viec.sh"), "--tiep", m.group(1), chu], 60))

    # 2. Lệnh.
    if chu.startswith("/"):
        lenh = chu[1:].split()[0].split("@")[0].lower()
        if lenh in ("start", "huong_dan", "help"):
            return gui(HUONG_DAN)
        if lenh == "dang_chay":
            return gui(chay(["bash", os.path.join(SO_TAY, "viec-dang-chay.sh"), "--gon"], 60))
        if lenh == "viec":
            return gui(viec_gan_day())
        if lenh == "viec_do":
            return gui(viec_do())
        if lenh == "phien":
            ds = chay(["python3", "-I", os.path.join(SO_TAY, "hop-thu-phien.py"), "ds"], 30)
            return gui((ds or "Không có phiên Claude nào đang mở.") + "\n\nNhắn: @số: lời của anh")
        if lenh == "suc_khoe":
            return gui(suc_khoe())
        if lenh in ("vang", "ve"):
            open(os.path.join(TT, "vang"), "w").write("1" if lenh == "vang" else "0")
            return gui("Đã ghi anh đi vắng: mọi yêu cầu duyệt chuyển lên đây ngay." if lenh == "vang"
                       else "Đã ghi anh ở máy: chỉ chuyển yêu cầu khi Mac không có thao tác 2 phút.")
        return gui("Không có lệnh này.\n\n" + HUONG_DAN)

    if k in ("toi di vang", "di vang", "vang"):
        return xu_ly("/vang")
    if k in ("toi ve", "toi ve roi", "toi o may", "toi o may roi"):
        return xu_ly("/ve")

    # 3. #N <lời> · đóng #N.
    m = re.match(r"^(?:dong|dong phien)\s*(?:viec\s*)?#?(\d+)$", k)
    if m:
        return gui(chay(["bash", os.path.join(SO_TAY, "giao-viec.sh"), "--dung", m.group(1)], 30))
    m = re.match(r"^#(\d+)[\s:,.-]+(.+)$", chu, re.S)
    if m:
        return gui(chay(["bash", os.path.join(SO_TAY, "giao-viec.sh"), "--tiep", m.group(1), m.group(2).strip()], 60))

    # 4. @phiên: lời.
    m = re.match(r"^@([^:]{0,60}):\s*(.+)$", chu, re.S)
    if m:
        kq = chay(["python3", "-I", os.path.join(SO_TAY, "hop-thu-phien.py"), "gui", m.group(1).strip(), m.group(2).strip()], 30)
        if kq.startswith("DA_GUI"):
            return gui(kq.split(":", 1)[1].strip())
        if kq.startswith("CHUA_RO"):
            return gui(kq.split(":", 1)[1].strip() + "\n\nNhắn lại: @số: lời của anh")
        return gui(kq.split(":", 1)[-1].strip())

    # 5. Câu trả lời ngắn cho yêu cầu duyệt đang chờ.
    cho = cho_duyet()
    ngan = len(chu) <= 40
    if cho and ngan:
        if len(cho) == 1:
            ma, d = cho[0]; nd = chuan_tra(d, chu)
            if nd is not None:
                ghi_tra(ma, nd); return gui(bao_da_tra(ma, nd, d))
        else:
            return gui("Đang có nhiều yêu cầu chờ, anh bấm nút ở đúng tin, hoặc trả lời (trích) tin đó:\n" +
                       "\n".join(f"• {ma} · {d.get('phien', '')} · {d.get('cong_cu', '')}" for ma, d in cho))
    if (len(k) < 12 and not BAI_DANG.search(k)) or k in DONG_Y or k in TU_CHOI:
        return gui("Không có yêu cầu nào đang chờ anh. Muốn giao việc cho Claude thì nhắn rõ việc cần làm.")

    # 6. Còn lại: giao việc mới cho Claude.
    return gui(giao(chu))


def nghe_thoai(file_id):
    try:
        f = api("getFile", file_id=file_id)["result"]["file_path"]
        noi = os.path.join(KENH, "inbox", f"{int(time.time())}-{os.path.basename(f)}")
        os.makedirs(os.path.dirname(noi), exist_ok=True)
        urllib.request.urlretrieve(f"https://api.telegram.org/file/bot{TOKEN}/{f}", noi)
        return chay(["bash", os.path.join(SO_TAY, "nghe-thoai.sh"), noi], 300)
    except Exception as e:
        ghi(f"nghe thoai loi {e}")
        return ""


def bam_nut(q):
    data = q.get("data", ""); tin = q.get("message") or {}
    phan = data.split("|")
    tl = ""
    if phan[0] == "d" and len(phan) == 3:
        ma, chon = phan[1], phan[2]
        f = os.path.join(DUYET, ma + ".json")
        if not os.path.exists(f) or os.path.exists(os.path.join(DUYET, ma + ".tra")):
            tl = "Yêu cầu này đã hết hạn hoặc đã được xử lý."
        else:
            d = json.load(open(f))
            ghi_tra(ma, chon); tl = bao_da_tra(ma, chon, d)
    elif phan[0] == "dong" and len(phan) == 2:
        tl = chay(["bash", os.path.join(SO_TAY, "giao-viec.sh"), "--dung", phan[1]], 30)
    try:
        api("answerCallbackQuery", callback_query_id=q["id"], text=tl[:190])
        if tin.get("message_id"):
            api("editMessageReplyMarkup", chat_id=CHAT, message_id=tin["message_id"], reply_markup={"inline_keyboard": []})
    except Exception as e:
        ghi(f"bam nut loi {e}")
    gui("→ " + tl, tra_loi_cho=tin.get("message_id"))


def mot_cap_nhat(u):
    if "callback_query" in u:
        q = u["callback_query"]
        if str(q.get("from", {}).get("id")) != CHAT:
            return
        return bam_nut(q)
    m = u.get("message") or {}
    if str(m.get("from", {}).get("id")) != CHAT:
        if m:
            ghi(f"bo qua tin tu nguoi la {m.get('from', {}).get('id')}")
        return
    chu = m.get("text") or m.get("caption") or ""
    am = m.get("voice") or m.get("audio")
    if am and not chu:
        chu = nghe_thoai(am["file_id"])
        if not chu:
            return gui("Em nghe chưa rõ, anh nhắn lại giúp em.")
        gui(f"🎤 {chu}")
    tra = (m.get("reply_to_message") or {}).get("text") or ""
    ghi(f"tin: {chu[:120]}")
    xu_ly(chu, tra, m.get("message_id"))


def main():
    global THU
    if len(sys.argv) >= 3 and sys.argv[1] == "--thu":
        THU = True
        xu_ly(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        return
    if not TOKEN or not CHAT:
        ghi("chua co token hoac chat David"); time.sleep(300); return
    try:
        api("setMyCommands", commands=[{"command": c, "description": d} for c, d in LENH])
    except Exception as e:
        ghi(f"setMyCommands loi {e}")
    ghi("bot dieu hanh bat dau")
    off = int(open(OFFSET).read().strip() or 0) if os.path.exists(OFFSET) else 0
    while True:
        open(NHIP, "w").write(str(int(time.time())))
        try:
            kq = api("getUpdates", offset=off, timeout=50, allowed_updates=["message", "callback_query"])
        except Exception as e:
            ghi(f"getUpdates loi {e}"); time.sleep(10); continue
        for u in kq.get("result", []):
            off = u["update_id"] + 1
            open(OFFSET, "w").write(str(off))   # ghi trước khi xử lý: lỗi giữa chừng không lặp lại lệnh giao việc
            try:
                mot_cap_nhat(u)
            except Exception as e:
                ghi(f"xu ly loi {e}")
                gui(f"Bot Điều hành gặp lỗi khi xử lý tin này: {e}")


if __name__ == "__main__":
    main()
