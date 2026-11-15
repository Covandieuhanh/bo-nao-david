#!/usr/bin/env python3
"""Hook SessionEnd (không gọi AI, không tốn token): đọc nhật ký phiên vừa xong, ghi TÍN HIỆU để skill hoc-lien-tuc gom cuối tuần.
Tín hiệu: skill đã dùng · lời David sửa/nhắc lại/không hài lòng (trích ngắn) · lỗi công cụ (tổng + theo tên công cụ) · số lượt.
Ghi vào ~/.claude/hoc-lien-tuc/tin-hieu.jsonl (ở lại máy: có trích lời chat, không đưa GitHub).
Dùng tay: python3 -I ghi-tin-hieu.py <transcript.jsonl>   (hook thì đọc JSON từ stdin)."""
import json, os, re, sys, time

RA = os.path.expanduser("~/.claude/hoc-lien-tuc/tin-hieu.jsonl")
SUA = re.compile(r"(sai|chưa đúng|không đúng|không phải|nhắc lại|đã bảo|đã nói|sao vẫn|sao lại|lại nữa|lần nữa|làm lại|"
                 r"không được|tệ|chán|tốn token|lâu quá|chậm|nhầm|thiếu|bỏ cái|đừng|không cần|vẫn còn|vẫn chưa)", re.I)


def chu(noi_dung):
    if isinstance(noi_dung, str):
        return noi_dung
    if isinstance(noi_dung, list):
        return " ".join(b.get("text", "") for b in noi_dung if isinstance(b, dict) and b.get("type") == "text")
    return ""


def main():
    if len(sys.argv) > 1:
        tp, sid = sys.argv[1], os.path.basename(sys.argv[1])[:-6]
        cwd = ""
    else:
        try:
            d = json.load(sys.stdin)
        except Exception:
            return
        tp, sid, cwd = d.get("transcript_path", ""), d.get("session_id", ""), d.get("cwd", "")
    if not tp or not os.path.exists(tp):
        return
    skill, sua, loi, luot, tieu_de = {}, [], 0, 0, ""
    ten_cc, loi_cc = {}, {}  # id lệnh → tên công cụ; tên công cụ → số lỗi
    for l in open(tp, encoding="utf-8", errors="ignore"):
        try:
            o = json.loads(l)
        except Exception:
            continue
        t = o.get("type")
        if t == "ai-title":
            tieu_de = o.get("aiTitle") or o.get("title") or tieu_de
        m = o.get("message") or {}
        if t == "user":
            c = m.get("content")
            if isinstance(c, list) and any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("is_error"):
                        loi += 1
                        ten = ten_cc.get(b.get("tool_use_id"), "?")
                        loi_cc[ten] = loi_cc.get(ten, 0) + 1
                continue
            s = chu(c).strip()
            if not s or s.startswith(("<", "[", "Đây là việc David giao")) or "system-reminder" in s[:200] or len(s) > 2000:
                continue
            luot += 1
            if SUA.search(s):
                sua.append(s[:300])
        elif t == "assistant":
            for b in m.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    ten_cc[b.get("id")] = b.get("name", "?")
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                    k = (b.get("input") or {}).get("skill", "?")
                    skill[k] = skill.get(k, 0) + 1
    if luot == 0:
        return
    os.makedirs(os.path.dirname(RA), exist_ok=True)
    with open(RA, "a", encoding="utf-8") as f:
        f.write(json.dumps({"luc": time.strftime("%Y-%m-%d %H:%M"), "phien": sid, "tieu_de": tieu_de, "cwd": cwd,
                            "luot_david": luot, "skill": skill, "loi_cong_cu": loi, "loi_theo_cong_cu": loi_cc, "david_sua": sua[-15:]},
                           ensure_ascii=False) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
