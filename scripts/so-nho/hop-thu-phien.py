#!/usr/bin/env python3
"""Hộp thư phiên: chuyển lời David (qua bot Telegram) vào một phiên Claude Code bất kỳ trên Mac, kể cả phiên mở trong app.

Hai vai:
1) Gửi (bot gọi):  python3 -I hop-thu-phien.py gui "<tên hoặc từ khoá phiên>" "<lời David>"
   Tìm phiên đang mở có tên khớp, bỏ lời vào .trang-thai/hop-phien/<mã phiên>/. In kết quả cho bot đọc.
   python3 -I hop-thu-phien.py ds   → liệt kê phiên đang mở (số thứ tự, tên) để bot hỏi lại khi không rõ.
2) Nhận (hook PostToolUse và Stop của mọi phiên, đọc JSON ở stdin): có thư cho phiên này thì đưa vào phiên.
   - PostToolUse: thêm lời David vào ngữ cảnh ngay sau bước vừa xong (phiên đang làm việc dài vẫn nhận).
   - Stop: chặn dừng, bảo Claude làm tiếp theo lời David (phiên vừa xong lượt).
   Phiên đang nghỉ hẳn (không làm gì) thì chưa nhận được: bot báo David mở phiên trên app/điện thoại.
"""
import json, os, re, subprocess, sys, time, glob

DATA = os.path.expanduser("~/Documents/2-ca-nhan/so-nho")
HOP = os.path.join(DATA, ".trang-thai", "hop-phien")
APP = os.path.expanduser("~/Library/Application Support/Claude/claude-code-sessions")
GOC = os.path.dirname(os.path.abspath(__file__))


def phien_dang_mo():
    """Các phiên Claude đang chạy: (mã phiên CLI, tên, đang bận?)"""
    ps = subprocess.run(["ps", "-axo", "pid=,ppid=,command="], capture_output=True, text=True).stdout.splitlines()
    P, con = {}, {}
    for l in ps:
        p = l.split(None, 2)
        if len(p) < 3: continue
        P[int(p[0])] = (int(p[1]), p[2]); con.setdefault(int(p[1]), []).append(int(p[0]))
    meta = {}
    for f in glob.glob(os.path.join(APP, "*", "*", "local_*.json")):
        try:
            d = json.load(open(f)); meta[d.get("sessionId")] = d
        except Exception:
            pass
    ra = []
    for pid, (pp, cmd) in P.items():
        dau = cmd.split(" --")[0]
        if not re.search(r"(/|^)claude( |$)", dau) or "disclaimer" in cmd: continue
        try:
            env = subprocess.run(["ps", "eww", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
        except Exception:
            continue
        if "TELEGRAM_STATE_DIR=" in env: continue
        if " -p" in cmd.split(" --remote-control")[0]: continue
        h = re.search(r"CLAUDE_CODE_HOST_SESSION_ID=(\S+)", env)
        m = meta.get(h.group(1)) if h else None
        if m and m.get("isArchived"): continue
        if m:
            sid, ten = m.get("cliSessionId"), m.get("title") or "phiên app"
        else:
            s = re.search(r"--(?:session-id|resume) (\S+)", cmd); rc = re.search(r"--remote-control=(.+?)( --|$)", cmd)
            if not s: continue
            sid, ten = s.group(1), (rc.group(1) if rc else "phiên terminal")
        ban = any(re.search(r"zsh -c|bash -c", P[k][1]) for k in con.get(pid, []))
        ra.append((sid, ten, ban))
    return ra


def khong_dau(s):
    import unicodedata
    s = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def gui(tu_khoa, loi):
    ds = phien_dang_mo()
    if not ds:
        print("KHONG_CO_PHIEN: không có phiên Claude nào đang mở trên Mac."); return
    k = khong_dau(tu_khoa)
    so = re.fullmatch(r"\s*(\d+)\s*", tu_khoa)
    if so and 1 <= int(so.group(1)) <= len(ds):
        khop = [ds[int(so.group(1)) - 1]]
    else:
        tu = [w for w in re.findall(r"\w+", k) if len(w) > 2]
        diem = [(sum(w in khong_dau(t) for w in tu), (sid, t, b)) for sid, t, b in ds]
        cao = max(d for d, _ in diem) if diem else 0
        khop = [x for d, x in diem if d == cao and d > 0]
        # Không chỉ rõ phiên mà chỉ có đúng một phiên đang bận thì gửi cho phiên đó.
        if not khop and len([x for x in ds if x[2]]) == 1:
            khop = [x for x in ds if x[2]]
    if len(khop) != 1:
        print("CHUA_RO: chưa rõ phiên nào. Các phiên đang mở:")
        for i, (sid, t, b) in enumerate(ds, 1): print(f"{i}. {t}{' (đang làm)' if b else ''}")
        return
    sid, ten, ban = khop[0]
    os.makedirs(os.path.join(HOP, sid), exist_ok=True)
    open(os.path.join(HOP, sid, f"{time.time():.3f}.txt"), "w").write(loi)
    if ban:
        print(f"DA_GUI: lời của anh sẽ tới phiên \"{ten}\" ngay sau bước nó đang chạy (lệnh dài như render thì đợi lệnh xong).")
    else:
        print(f"DA_GUI_CHO: phiên \"{ten}\" đang nghỉ, lời đã để sẵn; phiên nhận khi làm bước tiếp theo. "
              f"Muốn nó làm ngay thì anh mở phiên này trong app Claude (trên Mac hoặc điện thoại) và nhắn một chữ bất kỳ.")


def nhan():
    try:
        v = json.load(sys.stdin)
    except Exception:
        return
    sid = v.get("session_id", "")
    d = os.path.join(HOP, sid)
    if not sid or not os.path.isdir(d): return
    thu = sorted(glob.glob(os.path.join(d, "*.txt")))
    if not thu: return
    loi = []
    for f in thu:
        try:
            loi.append(open(f).read().strip()); os.remove(f)
        except Exception:
            pass
    if not loi: return
    noi = ("David nhắn cho phiên này qua Telegram (lời của chính David, làm theo như David gõ ở đây; "
           "nếu đổi kế hoạch thì đổi ngay, xong báo lại bằng scripts/so-nho/bao-cao.sh):\n- " + "\n- ".join(loi))
    try:
        subprocess.run(["bash", os.path.join(GOC, "bao-cao.sh"), "--chi-gui", "📨 Phiên Claude đã nhận lời anh: " + loi[-1][:120]],
                       capture_output=True, timeout=30)
    except Exception:
        pass
    if v.get("hook_event_name") == "Stop":
        print(json.dumps({"decision": "block", "reason": noi}, ensure_ascii=False))
    else:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": noi}}, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "gui":
        gui(sys.argv[2] if len(sys.argv) > 2 else "", sys.argv[3] if len(sys.argv) > 3 else "")
    elif len(sys.argv) >= 2 and sys.argv[1] == "ds":
        for i, (sid, t, b) in enumerate(phien_dang_mo(), 1): print(f"{i}. {t}{' (đang làm)' if b else ''}")
    else:
        nhan()
