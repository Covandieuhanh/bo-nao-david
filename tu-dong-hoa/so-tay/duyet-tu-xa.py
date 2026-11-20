#!/usr/bin/env python3
"""Hook PermissionRequest cho mọi phiên Claude Code trên Mac: David vắng thì gửi yêu cầu duyệt (hoặc câu hỏi nhiều lựa chọn)
lên Telegram qua bot Điều hành (tu-dong-hoa/dieu-hanh/bot.py, có nút bấm; chưa cài thì bot Sổ nhớ), chờ David trả lời, rồi trả quyết định cho phiên.
- David "vắng" khi: .trang-thai/vang ghi "1" (David nhắn bot "tôi đi vắng"; "tôi về" thì bot ghi "0"), hoặc Mac không có thao tác chuột/phím ≥ 120 giây.
- David đang ngồi máy, hoặc không trả lời trong 30 phút: không quyết, hộp thoại hiện trên máy như thường.
- Bot ghi câu trả lời vào .trang-thai/duyet/<mã>.tra: "ok" · "khong" · hoặc chữ trả lời câu hỏi.
Cài: python3 -I tu-dong-hoa/cai-hook.py <repo> (thêm hook này). Thử: DUYET_THU=1 để coi như David vắng."""
import json, os, random, string, subprocess, sys, time, glob

DATA = os.path.expanduser("~/Documents/2-ca-nhan/so-tay")
TT = os.path.join(DATA, ".trang-thai")
HANG = os.path.join(TT, "duyet")
GOC = os.path.dirname(os.path.abspath(__file__))
CHO_TOI_DA = 1800
VANG_SAU = 120


def ra(quyet=None, thong_bao=None, dau_vao=None):
    if quyet:
        d = {"behavior": quyet}
        if thong_bao: d["message"] = thong_bao
        if dau_vao is not None: d["updatedInput"] = dau_vao
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PermissionRequest", "decision": d}}, ensure_ascii=False))
    sys.exit(0)


def ranh_roi():
    try:
        o = subprocess.run(["/usr/sbin/ioreg", "-c", "IOHIDSystem"], capture_output=True, text=True, timeout=5).stdout
        for l in o.splitlines():
            if "HIDIdleTime" in l:
                return int(l.split()[-1]) / 1e9
    except Exception:
        pass
    return 0


def ten_phien(sid):
    try:
        return json.load(open(os.path.expanduser(f"~/.claude/so-viec/phien/{sid}.json"))).get("title") or ""
    except Exception:
        return ""


def loi_gan_nhat(duong):
    """Đoạn chữ gần nhất Claude viết trong phiên (thường là lời giải thích vì sao cần làm bước này)."""
    try:
        dong = open(duong, encoding="utf-8").read().splitlines()[-60:]
    except Exception:
        return ""
    for l in reversed(dong):
        try:
            d = json.loads(l)
        except Exception:
            continue
        m = d.get("message") or {}
        if d.get("type") == "assistant" and isinstance(m.get("content"), list):
            chu = " ".join(x.get("text", "") for x in m["content"] if x.get("type") == "text").strip()
            if chu:
                return " ".join(chu.split())[:1200]
    return ""


def dien_giai(cong_cu, vao, chi_tiet, boi_canh, phien):
    """Nhờ Haiku viết lại yêu cầu bằng tiếng Việt dễ hiểu; lỗi hoặc quá 40 giây thì dùng câu mẫu."""
    mau = {"Bash": "Claude muốn chạy một lệnh trên máy", "Edit": f"Claude muốn sửa file {os.path.basename(chi_tiet)}",
           "Write": f"Claude muốn tạo hoặc ghi đè file {os.path.basename(chi_tiet)}", "Read": f"Claude muốn đọc file {os.path.basename(chi_tiet)}",
           "WebFetch": "Claude muốn mở một trang web", "WebSearch": "Claude muốn tìm trên mạng"}.get(cong_cu, f"Claude muốn dùng công cụ {cong_cu}")
    mo_ta = vao.get("description", "")
    du_phong = mau + (f": {mo_ta}" if mo_ta else "") + "."
    loi = f"""Viết lại yêu cầu cấp quyền dưới đây cho David (người không rành kỹ thuật) bằng tiếng Việt tự nhiên, đầy đủ ý, như người trợ lý giải thích.
Đúng 3 dòng, không markdown, không lời chào:
Việc muốn làm: <Claude định làm gì, nói bằng việc đời thường, không dùng tên lệnh>
Để làm gì: <vì sao cần, dựa vào bối cảnh>
Rủi ro: <có xoá/ghi đè/gửi/đăng/tốn tiền gì không; không có thì ghi "thấp, không xoá hay gửi gì">

Phiên đang làm: {phien}
Công cụ: {cong_cu}
Chi tiết: {chi_tiet[:1500]}
Mô tả Claude ghi kèm: {mo_ta}
Lời Claude vừa nói trong phiên: {boi_canh[-1000:]}"""
    # Bỏ dấu "đang ở trong phiên Claude" để gọi được một phiên Haiku riêng.
    env = {k: val for k, val in os.environ.items() if not k.startswith("CLAUDE") and k not in ("TELEGRAM_STATE_DIR",)}
    env.update({"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1", "ENABLE_CLAUDEAI_MCP_SERVERS": "false"})
    try:
        r = subprocess.run([os.path.expanduser("~/.local/bin/claude"), "-p", "--model", "haiku", "--setting-sources", "project",
                            "--tools", ""], input=loi, capture_output=True, text=True, timeout=40, cwd="/tmp", env=env)
        kq = r.stdout.strip()
        if r.returncode == 0 and "Việc muốn làm" in kq:
            return kq
        open(os.path.join(TT, "dien-giai.log"), "a").write(f"{time.strftime('%F %T')} rc={r.returncode} {r.stderr[-300:]} {kq[:200]}\n")
    except Exception as e:
        open(os.path.join(TT, "dien-giai.log"), "a").write(f"{time.strftime('%F %T')} loi {e}\n")
    return du_phong




def gui(tin, nut=None):
    """Gửi qua bot Điều hành (bao-cao.sh mặc định); nut = inline_keyboard, bot Điều hành nhận bấm nút và ghi <mã>.tra."""
    lenh = ["bash", os.path.join(GOC, "bao-cao.sh"), "--chi-gui"] + (["--nut", json.dumps(nut, ensure_ascii=False)] if nut else []) + [tin]
    # Không vào hàng chờ gửi lại: yêu cầu duyệt hết hạn thì tin gửi muộn chỉ gây nhầm.
    r = subprocess.run(lenh, capture_output=True, text=True, timeout=60, env={**os.environ, "BAO_CAO_KHONG_CHO": "1"})
    return r.returncode == 0



def hoi_david(v, ly_do="", het_gio_ve_may=True):
    """Gửi David yêu cầu (xin phép hoặc câu hỏi) qua Telegram, chờ trả lời. Trả về chữ David trả lời, hoặc None."""
    cwd = v.get("cwd", "")
    cong_cu = v.get("tool_name", "?")
    vao = v.get("tool_input") or {}
    ma = "".join(random.choice("ABCDEFGHJKMNPQRSTUVWXYZ23456789") for _ in range(4))
    os.makedirs(HANG, exist_ok=True)
    phien = ten_phien(v.get("session_id", "")) or os.path.basename(cwd) or "phiên Claude"

    boi_canh = loi_gan_nhat(v.get("transcript_path", ""))
    if cong_cu == "AskUserQuestion" and vao.get("questions"):
        cau = vao["questions"]
        dong = [f"❓ Claude đang hỏi anh (phiên: {phien})"]
        if boi_canh:
            dong.append(f"\nBối cảnh: {boi_canh[-500:]}")
        for i, q in enumerate(cau, 1):
            dong.append(f"\n{('Câu ' + str(i) + ': ') if len(cau) > 1 else ''}{q.get('question', '')}")
            for j, o in enumerate(q.get("options", []), 1):
                mo_ta = o.get("description", "")
                dong.append(f"  {j}. {o.get('label', '')}" + (f" — {mo_ta}" if mo_ta else ""))
        if len(cau) > 1:
            dong.append(f"\nAnh trả lời lần lượt từng câu, cách nhau dấu phẩy (ví dụ: 1, 2), hoặc viết ý của anh.")
        else:
            dong.append(f"\nAnh trả lời bằng số lựa chọn (ví dụ: 1), hoặc viết ý của anh.")
        dong.append(f"(Mã yêu cầu: {ma}, chỉ cần ghi khi có nhiều yêu cầu cùng lúc)")
        tin = "\n".join(dong)
        nut = None
        if len(cau) == 1 and cau[0].get("options"):
            nut = [[{"text": f"{j}. {o.get('label', '')}"[:60], "callback_data": f"d|{ma}|{j}"}] for j, o in enumerate(cau[0]["options"], 1)]
    else:
        if cong_cu == "Bash":
            chi_tiet = vao.get("command", "")
        elif cong_cu in ("Edit", "Write", "Read", "NotebookEdit"):
            chi_tiet = vao.get("file_path", "")
        else:
            chi_tiet = json.dumps(vao, ensure_ascii=False)
        giai_thich = dien_giai(cong_cu, vao, chi_tiet, boi_canh, phien)
        if ly_do:
            giai_thich += f"\nVì sao phải hỏi: {ly_do}"
        tin = (f"🔐 Claude cần anh cho phép (phiên: {phien})\n\n{giai_thich}\n\n"
               f"Chi tiết kỹ thuật: {cong_cu} · {chi_tiet[:300]}\n\n"
               f"Anh bấm nút, hoặc trả lời tin này \"không\" kèm lý do.\n(Mã yêu cầu: {ma}, chỉ cần ghi khi có nhiều yêu cầu cùng lúc)")
        nut = [[{"text": "✅ Đồng ý", "callback_data": f"d|{ma}|ok"}, {"text": "❌ Từ chối", "callback_data": f"d|{ma}|khong"}]]

    json.dump({"ma": ma, "luc": time.strftime("%Y-%m-%d %H:%M"), "phien": phien, "cong_cu": cong_cu, "tin": tin},
              open(os.path.join(HANG, ma + ".json"), "w"), ensure_ascii=False)
    if not gui(tin, nut):
        os.remove(os.path.join(HANG, ma + ".json"))
        return None

    tra_file = os.path.join(HANG, ma + ".tra")
    het = time.time() + CHO_TOI_DA
    while time.time() < het:
        if os.path.exists(tra_file):
            time.sleep(0.3)
            tra = open(tra_file).read().strip()
            for f in glob.glob(os.path.join(HANG, ma + ".*")):
                os.remove(f)
            return tra
        time.sleep(2)
    for f in glob.glob(os.path.join(HANG, ma + ".*")):
        os.remove(f)
    gui(f"⌛ Hết 30 phút anh chưa trả lời yêu cầu {ma}." + (" Câu hỏi chuyển về màn hình Mac, Claude chờ ở đó." if het_gio_ve_may else " Claude không làm bước đó."))
    return None


def dong_y(tra):
    return (tra or "").strip().lower() in ("ok", "duyet", "duyệt", "yes", "y", "co", "có", "đồng ý", "dong y", "được", "duoc")


def main():
    try:
        v = json.load(sys.stdin)
    except Exception:
        ra()
    cwd = v.get("cwd", "")
    if cwd.rstrip("/").endswith("so-tay"):
        ra()  # chính bot: không hỏi vòng
    if not os.path.exists(os.path.expanduser("~/.claude/channels/so-tay/.env")):
        ra()
    try:
        bao_vang = open(os.path.join(TT, "vang")).read().strip() == "1"
    except Exception:
        bao_vang = False
    vang = os.environ.get("DUYET_THU") == "1" or bao_vang or ranh_roi() >= VANG_SAU
    if not vang:
        ra()

    cong_cu = v.get("tool_name", "?")
    vao = v.get("tool_input") or {}
    tra = hoi_david(v)
    if tra is None:
        ra()
    if cong_cu == "AskUserQuestion" and vao.get("questions"):
        cau = vao["questions"]; phan = [p.strip() for p in tra.split(",")] if len(cau) > 1 else [tra]
        tl = {}
        for i, q in enumerate(cau):
            p = phan[i] if i < len(phan) else phan[-1]
            opts = q.get("options", [])
            tl[q.get("question", "")] = opts[int(p) - 1]["label"] if p.isdigit() and 0 < int(p) <= len(opts) else p
        ra("allow", dau_vao={**vao, "answers": tl})
    if dong_y(tra):
        ra("allow")
    ra("deny", thong_bao=f"David từ chối qua Telegram{': ' + tra if tra.lower() not in ('khong', 'không', 'no', 'n') else ''}")

if __name__ == "__main__":
    main()
