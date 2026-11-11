#!/bin/bash
# In ra mọi việc Claude đang có trên Mac, cho bot Sổ nhớ trả lời "đang chạy gì?".
# Nguồn: tiến trình Claude đang sống (app Claude, terminal, việc giao qua Telegram) + tiến trình con (render, ffmpeg…)
#        + dữ liệu phiên của app Claude (tên, tóm tắt lượt cuối) + đoạn Claude viết gần nhất trong phiên.
DATA="$HOME/Documents/2-ca-nhan/so-nho"
python3 -I - "$DATA" <<'PY'
import json, glob, os, re, subprocess, sys, time

data = sys.argv[1]
now = time.time()
APP = os.path.expanduser("~/Library/Application Support/Claude/claude-code-sessions")
PROJ = os.path.expanduser("~/.claude/projects")

ps = subprocess.run(["ps", "-axo", "pid=,ppid=,etime=,command="], capture_output=True, text=True).stdout.splitlines()
P, con = {}, {}
for l in ps:
    p = l.split(None, 3)
    if len(p) < 4: continue
    pid, pp = int(p[0]), int(p[1]); P[pid] = (pp, p[2], p[3]); con.setdefault(pp, []).append(pid)

def hau_due(pid):
    out = []
    for k in con.get(pid, []):
        out.append(k); out += hau_due(k)
    return out

def moi_truong(pid):
    try:
        e = subprocess.run(["ps", "eww", "-p", str(pid)], capture_output=True, text=True, timeout=5).stdout
    except Exception:
        return {}
    return dict(re.findall(r"\b(CLAUDE_CODE_HOST_SESSION_ID|TELEGRAM_STATE_DIR)=(\S+)", e))

meta = {}
for f in glob.glob(os.path.join(APP, "*", "*", "local_*.json")):
    try:
        d = json.load(open(f)); meta[d.get("sessionId")] = d
    except Exception:
        pass

def ve_viec(cmd):
    c = cmd
    if "ffmpeg" in c: return "ffmpeg (ghép/xuất video)"
    if "remotion" in c and "render" in c: return "Remotion render"
    if "chrome-headless-shell" in c: return None
    m = re.search(r"(\S+\.py)\b", c)
    if m and "Python" in c: return f"python {os.path.basename(m.group(1))}"
    if re.search(r"\bnode\b|npx", c): return "node " + " ".join(c.split()[1:3])[:60]
    return None

def loi_cuoi(cli_sid, cwd):
    f = os.path.join(PROJ, re.sub(r"[^A-Za-z0-9]", "-", cwd), f"{cli_sid}.jsonl")
    try:
        dong = open(f, encoding="utf-8").read().splitlines()[-80:]; tuoi = now - os.path.getmtime(f)
    except Exception:
        return "", None
    for l in reversed(dong):
        try: d = json.loads(l)
        except Exception: continue
        m = d.get("message") or {}
        if d.get("type") == "assistant" and isinstance(m.get("content"), list):
            t = " ".join(x.get("text", "") for x in m["content"] if x.get("type") == "text").strip()
            if t: return " ".join(t.split())[:300], tuoi
    return "", tuoi

dong_ra, thay = [], set()
for pid, (pp, et, cmd) in P.items():
    if not re.search(r"(/|^)claude( |$)", cmd.split(" --")[0]) or "disclaimer" in cmd: continue
    env = moi_truong(pid)
    if "TELEGRAM_STATE_DIR" in env: continue                    # chính bot
    if " -p" in cmd and "--name" not in cmd and "Telegram #" not in cmd: continue  # phiên phụ (viết diễn giải…)
    con_chau = hau_due(pid)
    viec = [v for v in (ve_viec(P[k][2]) for k in con_chau) if v]
    chay_lenh = [k for k in con_chau if re.search(r"zsh -c|bash -c", P[k][2])]
    hsid = env.get("CLAUDE_CODE_HOST_SESSION_ID", "")
    m = meta.get(hsid, {})
    if m.get("isArchived"): continue
    ten = m.get("title") or (re.search(r"--name '?([^']+)", cmd).group(1) if "--name" in cmd else "phiên terminal")
    cwd = m.get("cwd") or ""
    tom = (m.get("postTurnSummary") or {}).get("status_detail", "")
    can = (m.get("postTurnSummary") or {}).get("needs_action", "")
    loi, tuoi = loi_cuoi(m.get("cliSessionId", ""), cwd) if m else ("", None)
    hd = m.get("lastActivityAt", 0) / 1000
    if chay_lenh or (tuoi is not None and tuoi < 90):
        trang = "ĐANG LÀM" + (f": {', '.join(sorted(set(viec)))}" if viec else (" (đang chạy lệnh)" if chay_lenh else " (đang nghĩ/viết)"))
        if chay_lenh:
            trang += f" · lệnh đã chạy {P[chay_lenh[0]][1]}"
    else:
        trang = "chờ / nghỉ" + (f" · hoạt động cuối {time.strftime('%H:%M', time.localtime(hd))}" if hd else "")
    s = f"- {ten} · {trang}"
    if tom: s += f"\n  Tình trạng: {tom}"
    if can: s += f"\n  Cần anh: {can}"
    if loi: s += f"\n  Claude vừa viết: {loi}"
    dong_ra.append((0 if trang.startswith("ĐANG") else 1, -hd, s))

print("## Các phiên Claude đang mở trên Mac")
print("\n".join(s for *_, s in sorted(dong_ra)) or "Không có phiên nào đang mở")

man = subprocess.run(["screen", "-ls"], capture_output=True, text=True).stdout
dang_giao = sorted(re.findall(r"\.viec-(\d+)\s", man), key=int)
print("\n## Việc giao qua Telegram đang chạy")
print(", ".join("#" + s for s in dang_giao) if dang_giao else "Không có")
PY
echo; echo "## Sức khoẻ bot"
TT="$DATA/.trang-thai"; read -r LUC PH TG < "$TT/nhip" 2>/dev/null
echo "Kiểm lần cuối: $( [ -n "$LUC" ] && echo "$(( ($(date +%s) - LUC) )) giây trước · $PH · $TG" || echo "chưa có")"
echo "Tự mở lại hôm nay: $(grep -c "^$(date +%F).*mo phien bot" "$TT/canh-bot.log" 2>/dev/null) lần · cảnh báo gần nhất: $(grep "canh bao" "$TT/canh-bot.log" 2>/dev/null | tail -1 | cut -c1-60)"
echo; echo "## Việc dở và chờ David quyết: đọc TRANG-THAI-HIEN-TAI.md (bảng 'Đang làm dở', mục 'Câu hỏi còn mở')"
