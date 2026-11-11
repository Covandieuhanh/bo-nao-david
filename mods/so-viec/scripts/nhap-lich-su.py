#!/usr/bin/env python3
"""Nhập ngược lịch sử phiên Claude Code cũ vào Sổ việc.

Đọc ~/.claude/projects/*/<sid>.jsonl, chia lượt và việc theo đúng luật của mod
(skill được gọi = loại việc; còn lại model nhỏ gán nhãn; trả lời ngắn tính vào việc đang làm;
im lặng quá 60 phút thì việc cũ xong), ghi ~/.claude/so-viec/nhap/<sid>.json.
Phiên nào mod đã ghi sổ (phien/<sid>.json) thì chỉ nhập phần trước lúc mod bắt đầu ghi.

Dùng:  python3 -I mods/so-viec/scripts/nhap-lich-su.py          (chạy lại bao nhiêu lần cũng được)
       python3 -I mods/so-viec/scripts/nhap-lich-su.py --khong-gan-nhan   (không gọi model, nhãn = khac)
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime

HOME = os.path.expanduser("~")
PROJECTS = os.path.join(HOME, ".claude", "projects")
DATA = os.path.join(HOME, ".claude", "so-viec")
IDLE_CLOSE_MS = 60 * 60 * 1000
MAX_STEP_MS = 5 * 60 * 1000  # một bước im quá 5 phút trong lượt = đang chờ David, không tính

SKILL_TYPES = {
    "video-style-edit": "video-style-edit",
    "podcast-style-edit": "podcast-style-edit",
    "cat-highlight-video": "cat-highlight-video",
    "dang-da-kenh": "dang-da-kenh",
    "hoc-video-mau": "hoc-video-mau",
    "tai-ban": "tai-ban",
    "playwright-cli": "dieu-khien-trinh-duyet",
    "plugin-authoring": "lam-mod",
    "scroll-craft": "lam-trang-web",
}
# Không có nhãn video: video chỉ tính khi skill video được gọi (giống mod).
LABELS = ["sua-bo-nao", "viet-bai", "nghien-cuu", "lap-ke-hoach", "lam-mod", "hoi-dap", "khac"]


def ms(ts):
    return int(datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp() * 1000)


def prompt_text(d):
    """Văn bản người dùng gõ, hoặc None nếu dòng này không phải lời nhắn mới."""
    if d.get("type") != "user" or d.get("isMeta") or d.get("isSidechain"):
        return None
    c = d.get("message", {}).get("content")
    if isinstance(c, str):
        text = c
    elif isinstance(c, list):
        if any(b.get("type") == "tool_result" for b in c if isinstance(b, dict)):
            return None
        text = " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    else:
        return None
    text = text.strip()
    if not text or text.startswith(("<local-command", "<command-stdout", "<task-notification", "<system-reminder")):
        return None
    return text


def parse(path, cutoff):
    turns, cur, seen = [], None, set()
    for line in open(path, encoding="utf-8"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        ts = d.get("timestamp")
        if not ts:
            continue
        t = ms(ts)
        text = prompt_text(d)
        if text is not None:
            if cur:
                turns.append(cur)
            m = re.search(r"<command-name>/?([\w:-]+)</command-name>", text)
            skill = SKILL_TYPES.get(m.group(1).split(":")[-1]) if m else None
            clean = re.sub(r"<[^>]+>", " ", text)
            cur = {"start": t, "end": t, "active": 0, "text": re.sub(r"\s+", " ", clean).strip(), "skill": skill,
                   "tok": [0, 0, 0, 0]}
            continue
        # Chỉ dòng Claude trả lời và kết quả công cụ đánh dấu lượt còn chạy (bỏ hàng đợi, tiêu đề...).
        if not cur or d.get("type") not in ("assistant", "user"):
            continue
        if t > cur["end"]:
            cur["active"] += min(t - cur["end"], MAX_STEP_MS)  # chờ duyệt lâu không tính
            cur["end"] = t
        if d.get("type") == "assistant":
            msg = d.get("message", {})
            mid = msg.get("id")
            u = msg.get("usage")
            if u and mid not in seen:
                seen.add(mid)
                cur["tok"][0] += u.get("input_tokens", 0) or 0
                cur["tok"][1] += u.get("output_tokens", 0) or 0
                cur["tok"][2] += u.get("cache_read_input_tokens", 0) or 0
                cur["tok"][3] += u.get("cache_creation_input_tokens", 0) or 0
            for b in msg.get("content", []) or []:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                    s = SKILL_TYPES.get(str((b.get("input") or {}).get("skill", "")).split(":")[-1])
                    if s and not cur["skill"]:
                        cur["skill"] = s
    if cur:
        turns.append(cur)
    return [x for x in turns if x["start"] < cutoff]


def classify(texts):
    """Gán nhãn hàng loạt bằng một lần gọi model nhỏ. Lỗi thì trả về {}."""
    if not texts:
        return {}
    items = "\n".join(f"{i}\t{t[:300]}" for i, t in enumerate(texts))
    ask = (
        "Gán cho mỗi tin nhắn dưới đây đúng một nhãn loại việc trong danh sách: " + ", ".join(LABELS) +
        ". Mỗi dòng: số thứ tự, tab, tin nhắn. Chỉ trả về một mảng JSON các nhãn theo đúng thứ tự, không giải thích.\n\n"
        + items
    )
    try:
        out = subprocess.run(["claude", "-p", "--model", "haiku", "--no-session-persistence"], input=ask,
                             capture_output=True, text=True, timeout=600).stdout
        arr = json.loads(out[out.index("["): out.rindex("]") + 1])
        return {i: (a if a in LABELS else "khac") for i, a in enumerate(arr)}
    except Exception as e:  # noqa: BLE001
        print("⚠ Không gán nhãn được bằng model, dùng 'khac':", e)
        return {}


def main():
    label_on = "--khong-gan-nhan" not in sys.argv
    sessions = []
    for proj in sorted(os.listdir(PROJECTS)):
        pdir = os.path.join(PROJECTS, proj)
        if not os.path.isdir(pdir):
            continue
        for f in sorted(os.listdir(pdir)):
            if not f.endswith(".jsonl"):
                continue
            sid = f[:-6]
            cutoff = float("inf")
            live = os.path.join(DATA, "phien", sid + ".json")
            if os.path.exists(live):
                try:
                    cutoff = json.load(open(live))["trackedSince"]
                except Exception:  # noqa: BLE001
                    pass
            turns = parse(os.path.join(pdir, f), cutoff)
            # Phiên đang chạy mà mod chưa ghi sổ: bỏ lượt cuối (đang dở, mod sẽ ghi).
            if cutoff == float("inf") and turns and \
                    datetime.now().timestamp() - os.path.getmtime(os.path.join(pdir, f)) < 600:
                turns = turns[:-1]
            if not turns:
                continue
            title = ""
            tfile = os.path.join(pdir, sid, "custom-title.json")
            if os.path.exists(tfile):
                try:
                    title = json.load(open(tfile)).get("customTitle", "")
                except Exception:  # noqa: BLE001
                    pass
            sessions.append({"sid": sid, "cwd": proj, "title": title or turns[0]["text"][:40], "turns": turns})

    # Lời nhắn cần nhãn: không gọi skill, không phải trả lời ngắn tiếp nối.
    need = []
    for s in sessions:
        for i, t in enumerate(s["turns"]):
            if t["skill"]:
                continue
            prev = s["turns"][i - 1] if i else None
            follow = prev is not None and len(t["text"]) < 40 and t["start"] - prev["end"] < IDLE_CLOSE_MS
            if not follow:
                t["need"] = len(need)
                need.append(t["text"])
    labels = classify(need) if label_on else {}

    os.makedirs(os.path.join(DATA, "nhap"), exist_ok=True)
    n_jobs = n_turns = 0
    for s in sessions:
        jobs, open_, out_turns = [], None, []
        for t in s["turns"]:
            label = labels.get(t["need"]) if "need" in t else None
            if open_ and t["start"] - open_["lastAt"] > IDLE_CLOSE_MS:
                jobs.append(open_)
                open_ = None
            typ = t["skill"] or label or (open_["type"] if open_ else ("khac" if "need" in t else None)) or "khac"
            if not open_ or open_["type"] != typ:
                if open_:
                    jobs.append(open_)
                open_ = {"id": f"{s['sid']}-{t['start']}", "type": typ, "startedAt": t["start"], "lastAt": t["end"],
                         "activeMs": 0, "turns": 0,
                         "tokens": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0}}
            open_["activeMs"] += t["active"]
            open_["turns"] += 1
            open_["lastAt"] = t["end"]
            for k, v in zip(["input", "output", "cacheRead", "cacheWrite"], t["tok"]):
                open_["tokens"][k] += v
            out_turns.append([t["start"], t["start"] + t["active"], sum(t["tok"])])
        if open_:
            jobs.append(open_)
        book = {"v": 1, "sid": s["sid"], "title": s["title"], "cwd": s["cwd"],
                "trackedSince": s["turns"][0]["start"], "updatedAt": s["turns"][-1]["end"],
                "running": None, "open": None, "jobs": jobs, "turns": out_turns}
        with open(os.path.join(DATA, "nhap", s["sid"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(book, fh, ensure_ascii=False)
        n_jobs += len(jobs)
        n_turns += len(out_turns)
    print(f"Đã nhập {len(sessions)} phiên · {n_turns} lượt · {n_jobs} việc · {len(need)} lời nhắn được gán nhãn"
          f"{'' if labels or not need else ' (chưa gán nhãn)'}")


if __name__ == "__main__":
    main()
