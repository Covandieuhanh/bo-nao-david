#!/usr/bin/env python3
"""Hook PermissionRequest cho mọi phiên Claude Code trên Mac: David vắng thì gửi yêu cầu duyệt (hoặc câu hỏi nhiều lựa chọn)
lên Telegram qua bot Sổ nhớ, chờ David trả lời qua bot, rồi trả quyết định cho phiên.
- David "vắng" khi: .trang-thai/vang ghi "1" (David nhắn bot "tôi đi vắng"; "tôi về" thì bot ghi "0"), hoặc Mac không có thao tác chuột/phím ≥ 120 giây.
- David đang ngồi máy, hoặc không trả lời trong 30 phút: không quyết, hộp thoại hiện trên máy như thường.
- Bot ghi câu trả lời vào .trang-thai/duyet/<mã>.tra: "ok" · "khong" · hoặc chữ trả lời câu hỏi.
Cài: python3 -I scripts/cai-hook.py <repo> (thêm hook này). Thử: DUYET_THU=1 để coi như David vắng."""
import json, os, random, string, subprocess, sys, time, glob

DATA = os.path.expanduser("~/Documents/2-ca-nhan/so-nho")
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


def gui(tin):
    r = subprocess.run(["bash", os.path.join(GOC, "bao-cao.sh"), "--chi-gui", tin], capture_output=True, text=True, timeout=40)
    return r.returncode == 0


def main():
    try:
        v = json.load(sys.stdin)
    except Exception:
        ra()
    cwd = v.get("cwd", "")
    if cwd.rstrip("/").endswith("so-nho"):
        ra()  # chính bot: không hỏi vòng
    if not os.path.exists(os.path.expanduser("~/.claude/channels/so-nho/.env")):
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
    ma = "".join(random.choice("ABCDEFGHJKMNPQRSTUVWXYZ23456789") for _ in range(4))
    os.makedirs(HANG, exist_ok=True)
    phien = ten_phien(v.get("session_id", "")) or os.path.basename(cwd) or "phiên Claude"

    if cong_cu == "AskUserQuestion" and vao.get("questions"):
        cau = vao["questions"]
        dong = [f"❓ Claude hỏi [{ma}] · {phien}"]
        for i, q in enumerate(cau, 1):
            dong.append(f"\n{i}. {q.get('question', '')}")
            for j, o in enumerate(q.get("options", []), 1):
                dong.append(f"   {j}) {o.get('label', '')}")
        dong.append(f"\nTrả lời: tl {ma} <số lựa chọn hoặc chữ>" + (" (nhiều câu: tl " + ma + " 1,2)" if len(cau) > 1 else ""))
        tin = "\n".join(dong)
    else:
        if cong_cu == "Bash":
            chi_tiet = vao.get("command", "")
        elif cong_cu in ("Edit", "Write", "Read", "NotebookEdit"):
            chi_tiet = vao.get("file_path", "")
        else:
            chi_tiet = json.dumps(vao, ensure_ascii=False)
        tin = f"🔐 Duyệt? [{ma}] · {phien}\nXin: {cong_cu} · {chi_tiet[:400]}\nNhắn: ok {ma}  ·  khong {ma}"

    json.dump({"ma": ma, "luc": time.strftime("%Y-%m-%d %H:%M"), "phien": phien, "cong_cu": cong_cu, "tin": tin},
              open(os.path.join(HANG, ma + ".json"), "w"), ensure_ascii=False)
    if not gui(tin):
        os.remove(os.path.join(HANG, ma + ".json"))
        ra()

    tra_file = os.path.join(HANG, ma + ".tra")
    het = time.time() + CHO_TOI_DA
    while time.time() < het:
        if os.path.exists(tra_file):
            time.sleep(0.3)
            tra = open(tra_file).read().strip()
            for f in glob.glob(os.path.join(HANG, ma + ".*")):
                os.remove(f)
            if cong_cu == "AskUserQuestion" and vao.get("questions"):
                cau = vao["questions"]; phan = [p.strip() for p in tra.split(",")] if len(cau) > 1 else [tra]
                tl = {}
                for i, q in enumerate(cau):
                    p = phan[i] if i < len(phan) else phan[-1]
                    opts = q.get("options", [])
                    tl[q.get("question", "")] = opts[int(p) - 1]["label"] if p.isdigit() and 0 < int(p) <= len(opts) else p
                gui(f"Đã chuyển câu trả lời [{ma}].")
                ra("allow", dau_vao={**vao, "answers": tl})
            if tra.lower() in ("ok", "duyet", "duyệt", "yes", "y", "co", "có"):
                ra("allow")
            ra("deny", thong_bao=f"David từ chối qua Telegram{': ' + tra if tra.lower() not in ('khong', 'không', 'no', 'n') else ''}")
        time.sleep(2)
    for f in glob.glob(os.path.join(HANG, ma + ".*")):
        os.remove(f)
    gui(f"⌛ [{ma}] hết 30 phút chưa có trả lời, yêu cầu chuyển về màn hình Mac.")
    ra()


main()
