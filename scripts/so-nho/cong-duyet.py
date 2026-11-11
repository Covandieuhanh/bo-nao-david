#!/usr/bin/env python3
"""Cổng duyệt (hook PreToolUse) cho phiên việc giao qua Telegram, chạy toàn quyền (bypassPermissions).
Chỉ bật trong phiên có biến TELEGRAM_VIEC=1 (giao-viec.sh đặt). Thao tác thường chạy luôn; thao tác RỦI RO thì hỏi David
qua Telegram bằng tiếng Việt và chờ: David "đồng ý" thì cho chạy, như David bấm cho phép trên Mac; "không" hoặc 30 phút
không trả lời thì chặn, Claude nhận lý do và làm cách khác hoặc hỏi lại.

Việc rủi ro (David chốt 11/11/2026): đăng hoặc gửi ra ngoài · xoá vĩnh viễn · đẩy đè lên GitHub · sửa cấu hình hệ thống
hoặc cấu hình Claude · cài hoặc gỡ phần mềm · việc tốn tiền.
Thử: echo '<json>' | TELEGRAM_VIEC=1 CONG_DUYET_THU=1 python3 -I cong-duyet.py  (THU: chỉ in kết luận, không hỏi)."""
import importlib.util, json, os, re, sys

GOC = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser("~")

BASH_RUI_RO = [
    (r"(^|[;&|]\s*|\s)(sudo|doas)\s", "chạy lệnh với quyền quản trị máy"),
    (r"(^|[;&|]\s*)rm\s", "xoá file (không vào thùng rác, không lấy lại được)"),
    (r"\bfind\b.*\s-delete\b", "xoá file hàng loạt"),
    (r"\bgit\s+push\b.*(\s-f\b|--force)", "đẩy đè lên GitHub (xoá lịch sử trên GitHub)"),
    (r"\bgit\s+(reset\s+--hard|clean\s+-[a-z]*f|branch\s+-D|push\s+\S+\s+--delete|push\s+\S+\s+:)", "xoá thay đổi hoặc nhánh git"),
    (r"\b(brew|port)\s+(install|uninstall|remove|reinstall|upgrade)\b", "cài hoặc gỡ phần mềm"),
    (r"\b(npm|pnpm|yarn|bun)\s+(i|install|add|remove|uninstall)\s+(-g|--global)\b", "cài phần mềm cho cả máy"),
    (r"\bpip3?\s+(install|uninstall)\b(?!.*--target)", "cài hoặc gỡ gói Python"),
    (r"\b(curl|wget)\b[^|]*\|\s*(ba|z)?sh\b", "tải và chạy chương trình từ mạng"),
    (r"\bclaude\s+plugin\s+(install|uninstall|enable|disable)\b", "cài hoặc tắt plugin Claude"),
    (r"\b(launchctl\s+(bootstrap|bootout|load|unload|enable|disable)|crontab\s|defaults\s+write|pmset\s|systemsetup|networksetup|scutil\s|csrutil|spctl|tccutil|nvram)\b", "sửa cấu hình hệ thống"),
    (r"\bchmod\s+-R|\bchown\s", "đổi quyền file hàng loạt"),
    (r"\bdiskutil\s+(erase|partition|unmount)", "đụng tới ổ đĩa"),
    (r"\bosascript\b.*(System Events|keystroke|delete|empty trash)", "điều khiển app khác trên máy"),
    (r"\b(gh\s+(release|repo\s+delete|pr\s+merge)|gh\s+api\s+-X\s*(DELETE|POST|PUT))", "thao tác lên GitHub"),
    (r"\bplaywright-cli\b.*\b(click|press|fill|type)\b", "bấm hoặc điền trên trang web (có thể là đăng bài hoặc gửi)"),
    (r"\b(sendmail|mail\s+-s|telegram.*sendMessage)\b(?!.*so-nho/bao-cao)", "gửi tin ra ngoài"),
    (r"\b(purchase|checkout|payment|thanh-toan|stripe)\b", "việc có thể tốn tiền"),
]
DUONG_CAU_HINH = [
    (HOME + "/.claude/settings", "sửa cấu hình Claude"), (HOME + "/.claude.json", "sửa cấu hình Claude"),
    (HOME + "/.claude/plugins", "sửa plugin Claude"), (HOME + "/Library/LaunchAgents", "sửa chương trình tự chạy của máy"),
    (HOME + "/.zshrc", "sửa cấu hình terminal"), (HOME + "/.zprofile", "sửa cấu hình terminal"),
    (HOME + "/.ssh", "sửa khoá bảo mật SSH"), (HOME + "/.claude/channels", "sửa cấu hình bot Telegram"),
    ("/etc/", "sửa cấu hình hệ thống"), ("/Library/", "sửa cấu hình hệ thống"),
]
CONG_CU_RUI_RO = r"(send|post|publish|delete|remove|purchase|pay|transfer|share|invite|archive|trash)"


def danh_gia(ten, vao):
    """Trả về lý do rủi ro (chuỗi) hoặc '' nếu thao tác thường."""
    if ten == "Bash":
        lenh = vao.get("command", "")
        if "scripts/so-nho/bao-cao.sh" in lenh and not re.search(r"\brm\s", lenh):
            return ""
        for mau, ly_do in BASH_RUI_RO:
            if re.search(mau, lenh, re.I):
                if ly_do.startswith("xoá file") and re.fullmatch(r"\s*rm\s+(-[a-z]+\s+)*(/tmp/|/private/tmp/|\./?tmp/|\S*/(tam|tmp|cache|\.cache)/)\S*\s*", lenh):
                    continue  # dọn file tạm thì không hỏi
                return ly_do
        if re.search(r"(>|>>|\btee\b|\bcp\b|\bmv\b)\s*\S*(" + "|".join(re.escape(d) for d, _ in DUONG_CAU_HINH) + ")", lenh.replace("~", HOME)):
            return "ghi vào file cấu hình máy hoặc Claude"
        return ""
    if ten in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
        f = os.path.abspath(os.path.expanduser(vao.get("file_path", "")))
        for d, ly_do in DUONG_CAU_HINH:
            if f.startswith(d):
                return ly_do
        return ""
    if ten.startswith("mcp__") and re.search(CONG_CU_RUI_RO, ten.split("__")[-1], re.I):
        return "thao tác ra ngoài máy (" + ten.split("__")[-1] + ")"
    return ""


def ra(quyet, ly_do):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": quyet,
                                             "permissionDecisionReason": ly_do}}, ensure_ascii=False))
    sys.exit(0)


def main():
    if os.environ.get("TELEGRAM_VIEC") != "1":
        return
    try:
        v = json.load(sys.stdin)
    except Exception:
        return
    ly_do = danh_gia(v.get("tool_name", ""), v.get("tool_input") or {})
    if not ly_do:
        return
    if os.environ.get("CONG_DUYET_THU") == "1":
        print("RUI_RO: " + ly_do); return
    spec = importlib.util.spec_from_file_location("duyet", os.path.join(GOC, "duyet-tu-xa.py"))
    d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
    tra = d.hoi_david(v, ly_do=ly_do, het_gio_ve_may=False)
    if tra is None:
        ra("deny", "David chưa trả lời qua Telegram trong 30 phút nên chưa được làm bước này. Báo David bằng bao-cao.sh và làm phần khác.")
    if d.dong_y(tra):
        ra("allow", "David đã đồng ý qua Telegram.")
    ra("deny", "David không đồng ý qua Telegram" + (f": {tra}" if tra.lower() not in ("khong", "không", "no", "n") else "") +
       ". Đừng thử lại cách này; làm cách khác hoặc hỏi David.")


if __name__ == "__main__":
    main()
