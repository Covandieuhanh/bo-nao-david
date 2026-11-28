"""Ghi hook vào ~/.claude/settings.json để đồng bộ 2 chiều bộ não với GitHub:
- SessionStart: kéo bản mới từ GitHub về (dong-bo.sh --keo), rồi đưa bảng chỉ đường bộ não vào phiên (nap-bo-nao.sh)
- SessionEnd: đẩy thay đổi lên (dong-bo-hook.sh, chạy nền)
- PostToolUse + Stop: hộp thư phiên, lời David qua Telegram vào đúng phiên (tu-dong-hoa/so-tay/hop-thu-phien.py)
- PreToolUse: cổng duyệt việc rủi ro cho phiên việc toàn quyền (tu-dong-hoa/so-tay/cong-duyet.py)
- SessionEnd (thứ hai): ghi tín hiệu tự học (tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py)
- PermissionRequest: duyệt từ xa qua Telegram khi David vắng (tu-dong-hoa/so-tay/duyet-tu-xa.py)
Chạy lại nhiều lần không bị trùng. Dùng: python3 -I tu-dong-hoa/cai-hook.py <đường dẫn repo> [--chi-video]"""
import json, os, subprocess, sys
repo = os.path.abspath(sys.argv[1])
p = os.path.expanduser("~/.claude/settings.json")
cfg = json.load(open(p)) if os.path.exists(p) else {}
hooks = cfg.setdefault("hooks", {})
can = {
    # chỉ dòng cảnh báo (⛔ xung đột, ⚠ mất mạng) đi vào phiên để Claude báo David; còn lại im lặng
    "SessionStart": (f'bash "{repo}/tu-dong-hoa/dong-bo.sh" --keo 2>&1 | grep -E "⛔|⚠" ; true', '/tu-dong-hoa/dong-bo.sh" --keo'),
    "SessionEnd": (f'bash "{repo}/tu-dong-hoa/dong-bo-hook.sh"', '/tu-dong-hoa/dong-bo-hook.sh"'),
    # Mọi phiên mới: bảng chỉ đường bộ não + trạng thái việc (David 28/11/2026), sau khi đã kéo bản mới về
    "SessionStart#nap-bo-nao": (f'bash "{repo}/tu-dong-hoa/nap-bo-nao.sh"', '/tu-dong-hoa/nap-bo-nao.sh"'),
}
# Máy chỉ dựng video (--chi-video: Windows/WSL2, Mac khác; David 20/11/2026): chỉ đồng bộ + tự học, bỏ hook Telegram
# (bot, lịch tự chạy chỉ ở Mac chính).
CHI_VIDEO = "--chi-video" in sys.argv
if not CHI_VIDEO:
    # Duyệt từ xa qua Telegram (bot Sổ nhớ): David vắng thì yêu cầu duyệt và câu hỏi chuyển lên Telegram, chờ tối đa 30 phút.
    can["PermissionRequest"] = (f'python3 -I "{repo}/tu-dong-hoa/so-tay/duyet-tu-xa.py"', '/tu-dong-hoa/so-tay/duyet-tu-xa.py"')
    # Hộp thư phiên: lời David gửi qua bot Telegram cho một phiên đang mở, đưa vào sau mỗi bước (PostToolUse) hoặc khi xong lượt (Stop).
    can["PostToolUse"] = (f'python3 -I "{repo}/tu-dong-hoa/so-tay/hop-thu-phien.py"', '/tu-dong-hoa/so-tay/hop-thu-phien.py"')
    can["Stop"] = (f'python3 -I "{repo}/tu-dong-hoa/so-tay/hop-thu-phien.py"', '/tu-dong-hoa/so-tay/hop-thu-phien.py"')
    # Cổng duyệt cho phiên việc toàn quyền giao qua Telegram (chỉ bật khi TELEGRAM_VIEC=1): việc rủi ro hỏi David qua Telegram.
    can["PreToolUse"] = (f'python3 -I "{repo}/tu-dong-hoa/so-tay/cong-duyet.py"', '/tu-dong-hoa/so-tay/cong-duyet.py"')
# Tự học: cuối phiên ghi tín hiệu (lời David sửa, skill dùng, lỗi) cho skill hoc-lien-tuc, không gọi AI.
can["SessionEnd#hoc-lien-tuc"] = (f'python3 -I "{repo}/tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py"', '/tu-dong-hoa/hoc-lien-tuc/ghi-tin-hieu.py"')
cho = {"PermissionRequest": 1800, "PreToolUse": 1800}
for khoa, (cmd, dau) in can.items():
    su_kien = khoa.split("#")[0]
    ds = hooks.setdefault(su_kien, [])
    co = [h for g in ds for h in g.get("hooks", []) if dau in h.get("command", "")]
    for h in co: h["command"] = cmd          # đã có thì cập nhật lệnh theo bản mới
    if not co:
        g = {"hooks": [{"type": "command", "command": cmd, "timeout": cho.get(su_kien, 30)}]}
        if su_kien in ("PermissionRequest", "PostToolUse", "PreToolUse"): g["matcher"] = "*"
        ds.append(g)
    print(f"Hook {su_kien}: {cmd}")
# Tự tóm tắt hội thoại sớm hơn (60 % cửa sổ): hội thoại càng dài Claude càng dễ sót (bài học "1000 giờ Claude", 14/11/2026)
cfg.setdefault("env", {})["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] = "60"
print("Tự tóm tắt hội thoại ở 60 % cửa sổ")
# Tắt tự cập nhật Claude Code: mỗi bản mới là một file mới nên macOS hỏi lại quyền thư mục Tài liệu, làm tắc việc tự chạy.
# Cập nhật tay mỗi sáng thứ 6 trong lịch dong-goi-tuan (David 17/11/2026)
if not CHI_VIDEO:   # máy chỉ dựng video không có lịch thứ 6 → để Claude Code tự cập nhật
    cfg["env"]["DISABLE_AUTOUPDATER"] = "1"
    print("Tắt tự cập nhật Claude Code (cập nhật thứ 6 trong lịch dong-goi-tuan)")
# Mọi phiên mở ra đều bật Remote Control để hiện trong app Claude (điện thoại, claude.ai/code) cho David theo dõi (David 14/11/2026)
cfg["remoteControlAtStartup"] = True
print("Mọi phiên tự bật Remote Control (hiện trong app)")
# Bộ não công ty (Veltrix, kho private riêng): mọi phiên đọc/ghi được, để tự xếp nội dung công ty sang đó (David 18/11/2026)
cty = os.path.expanduser("~/Documents/bo-nao-veltrix")
if os.path.isdir(cty):
    ad = cfg.setdefault("permissions", {}).setdefault("additionalDirectories", [])
    if cty not in ad: ad.append(cty)
    print(f"Mọi phiên ghi được bộ não công ty: {cty}")
json.dump(cfg, open(p, "w"), ensure_ascii=False, indent=2)

subprocess.run([sys.executable, "-I", os.path.join(repo, "tu-dong-hoa", "nhat-ky", "cai.py"),
                "claude-code", "--cau-hinh", p, "--da-cai-bo-nao"], check=True)
