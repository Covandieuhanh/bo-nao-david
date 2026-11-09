#!/usr/bin/env python3
"""GỌI AI LÀM MỘT BƯỚC CỦA SKILL, NGAY TRONG THƯ MỤC DỰ ÁN: goi_ai.py <buoc/<id>.json> '<biến JSON>' [góp ý]

Nguyên tắc (David chốt 09/11/2026): cái gì cố định thì app chạy lệnh; cái gì cần phán đoán thì AI làm Y NHƯ khi David dùng skill.
App KHÔNG đặt khuôn JSON, không thêm luật hay vòng lặp riêng: AI (Claude Code hoặc Codex) mở trong thư mục dự án, đọc đúng
SKILL.md + README khối mà bước chỉ tới, tự sửa file dự án (cuts.json, captions.js, scenes.js, ke-hoach-canh.md, phat-hanh.md…)
và tự chạy lệnh kiểm mà khối dặn — đúng như một phiên Claude Code làm theo skill. Skill sửa gì, app tự theo.

Phiếu bước loại "ai": {id, ten, loai:"ai", viec, doc?:[file], ra?:[file phải có sau bước], kiem?:lệnh, nang?, mo_hinh?, suy_nghi?}
"""
import glob, json, os, shutil, subprocess, sys, time
from pathlib import Path

APP = Path(__file__).resolve().parent; DV = APP.parent; REPO = DV.parents[1]
sys.path.insert(0, str(APP))   # python -I không tự thấy file cùng thư mục (han_muc.py) — lỗi 09/11/2026 ở bước AI đầu tiên
ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))

# Công cụ AI được dùng: đọc/sửa file + đúng các lệnh mà skill dùng. Không mạng, không xoá ngoài dự án, không đăng.
CONG_CU = ["Read", "Edit", "Write", "Glob", "Grep", "Bash(node *)", "Bash(python3 *)", "Bash(zsh *)", "Bash(bash *)", "Bash(ffmpeg *)",
           "Bash(ffprobe *)", "Bash(ls *)", "Bash(cat *)", "Bash(head *)", "Bash(tail *)", "Bash(cd *)", "Bash(mkdir *)",
           "Bash(cp *)", "Bash(mv *)", "Bash(grep *)", "Bash(wc *)", "Bash(sed -n *)", "Bash(sips *)", "Bash(open -R *)"]

BOI_CANH = """Bạn đang chạy TỰ ĐỘNG trong app dựng video của David Trần (không có David ngồi trả lời).
- Làm đúng MỘT bước của skill như dưới đây, theo đúng chữ của SKILL.md và README các khối được chỉ — như khi David dùng skill trong Claude Code.
- KHÔNG hỏi lại David: David đã duyệt ở cổng duyệt của app (phiếu lọc + mọi điểm cần chọn). Điểm nào còn mở → chọn đề xuất đứng đầu, ghi rõ giả định vào báo cáo.
- Chỉ làm phần của bước này; bước trước app đã chạy xong, bước sau app sẽ chạy (đừng render cả video, đừng phát hành, đừng dọn tập, trừ khi bước này nói làm).
- Không đăng, không gửi, không xoá file ngoài thư mục dự án. Không đọc mạng trừ khi khối của bước này dùng script có sẵn để tìm ảnh.
- SÁNG TẠO HẾT SỨC CÓ THỂ (David chốt 09/11/2026 — cốt lõi của app): bước này cần phán đoán nên do AI làm. Chỉ dựa trên bộ khung
  (các bước, luật, tiêu chí đạt của skill) và nhận diện lớn của kênh (nền, màu chủ đạo, kiểu vẽ biểu tượng); bên trong thì sáng tạo hoàn
  toàn cho hợp nội dung CHÍNH video này — không dập khuôn, không lặp cách của video trước, danh mục có sẵn chỉ là công cụ, không phải khuôn.
- Luật nội dung vẫn giữ: chữ trên màn hình nguyên văn lời David; không đặt lời vào miệng David; bài đăng theo giọng văn David;
  lằn ranh nghề; không dùng từ "chữa lành"; không che mặt; tiếng Việt đủ dấu.
- Xong thì ghi BÁO CÁO NGẮN (tiếng Việt, ≤ 15 dòng: đã làm gì, giả định gì, còn gì chưa chắc) vào file báo cáo được chỉ."""


def thay(s, b):
    for k, v in b.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def tim_claude():
    for c in [os.environ.get("CLAUDE_BIN"), shutil.which("claude"), os.path.expanduser("~/.local/bin/claude"),
              os.path.expanduser("~/.claude/local/claude")]:
        if c and os.path.exists(c):
            return c
    ds = glob.glob(os.path.expanduser("~/Library/Application Support/Claude/claude-code/*/*/claude.app/Contents/MacOS/claude"))
    if ds:
        return max(ds, key=os.path.getmtime)
    raise SystemExit("Không tìm thấy lệnh claude. Xem app/README.md mục 'Lần đầu'.")


def tim_codex():
    for c in (os.environ.get("CODEX_BIN"), shutil.which("codex"),
              "/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"):
        if c and os.path.exists(c):
            return c
    raise SystemExit("Chưa có Codex CLI. Cài Codex và đăng nhập trên máy này trước.")


def gop_y(W):
    """Mọi góp ý David đã gửi cho video này (sổ W/gop-y.json) — áp cho mọi bước, thắng mọi suy luận."""
    f = Path(W) / "gop-y.json"
    if not f.exists():
        return ""
    return "\n".join(f"- [{x.get('luc')} · {x.get('noi')}] {x.get('david')}" for x in json.loads(f.read_text(encoding="utf-8")))


def loi_nhac(ph, b, gop):
    d = [f"# Bước: {ph['ten']}", "", thay(ph["viec"], b), "",
         f"Thư mục dự án ($P): {b['P']}", f"Skill dựng video: {DV}  (SKILL = {DV}/video-style-edit/scripts, khối = {DV}/khoi/)",
         f"Thư mục việc của app ($W, có tuỳ chọn, phiếu lọc, góp ý): {b['W']}",
         f"Ghi báo cáo vào: {b['W']}/bao-cao/{ph['id']}.md"]
    for f in ph.get("doc", []):
        p = Path(thay(f, b))
        if p.exists():
            d += ["", f"=== {p.name} ===", p.read_text(encoding="utf-8", errors="ignore")[:60000]]
    so = gop_y(b["W"])
    if so:
        d += ["", "=== GÓP Ý CỦA DAVID CHO VIDEO NÀY (luôn áp dụng) ===", so]
    if gop:
        d += ["", "=== GÓP Ý MỚI NHẤT — bước này chạy lại để sửa đúng ý này, giữ nguyên phần còn lại ===", gop]
    return "\n".join(d)


def goi_claude(prompt, b, ph):
    cmd = [tim_claude(), "-p", "--model", ph.get("mo_hinh", "opus"), "--effort", ph.get("suy_nghi", "high"),
           "--permission-mode", "acceptEdits", "--allowedTools", *CONG_CU,
           "--add-dir", str(DV), "--add-dir", b["W"], "--add-dir", str(REPO / "nao"), "--add-dir", os.path.expanduser("~/Movies/_so-danh-muc"),
           "--setting-sources", "", "--no-session-persistence", "--output-format", "stream-json", "--verbose",
           "--append-system-prompt", BOI_CANH]
    # stream-json: đọc từng dòng → ghi hạn mức còn lại ngay khi Claude báo (han_muc.py), lưu cả luồng để xem AI đã làm gì
    import han_muc
    d = None; luong = Path(b["W"]) / "log" / f"{ph['id']}.claude.jsonl"
    loi_f = open(Path(b["W"]) / "log" / f"{ph['id']}.claude.err", "w+")
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=loi_f, text=True, cwd=b["P"], env=ENV)
    p.stdin.write(prompt); p.stdin.close()
    t0 = time.time()
    with open(luong, "w", encoding="utf-8") as lg:
        for dong in p.stdout:
            lg.write(dong)
            x = han_muc.doc_dong(dong)
            if x and x.get("type") == "result":
                d = x
            if time.time() - t0 > ph.get("gioi_han_s", 3600):
                p.kill(); raise SystemExit("AI chạy quá giờ cho phép của bước.")
    p.wait()
    if d is None:
        loi_f.seek(0); raise SystemExit(f"Claude không trả kết quả:\n{loi_f.read()[-2000:]}")
    if d.get("is_error"):
        raise SystemExit(f"Claude báo lỗi: {d.get('result')}")
    return d.get("result", ""), {"usage": d.get("usage"), "cost": d.get("total_cost_usd"), "luot": d.get("num_turns")}


def goi_codex(prompt, b, ph):
    with open(Path(b["W"]) / "log" / f"{ph['id']}.codex.jsonl", "w") as lg:
        cmd = [tim_codex(), "exec", "--skip-git-repo-check", "--ephemeral", "--sandbox", "workspace-write", "--json", "--color", "never",
               "-C", b["P"], "--add-dir", b["W"], "-o", str(Path(b["W"]) / "log" / f"{ph['id']}.codex.txt")]
        if b.get("AI_MODEL"): cmd += ["-m", b["AI_MODEL"]]
        cmd += ["-c", "model_reasoning_effort=" + json.dumps(ph.get("suy_nghi", "high")), "-"]
        r = subprocess.run(cmd, input=BOI_CANH + "\n\n" + prompt, stdout=lg, stderr=subprocess.STDOUT, text=True, env=ENV,
                           timeout=ph.get("gioi_han_s", 3600))
    if r.returncode:
        raise SystemExit("Codex không hoàn thành bước — xem log/" + ph["id"] + ".codex.jsonl")
    out = Path(b["W"]) / "log" / f"{ph['id']}.codex.txt"
    return out.read_text() if out.exists() else "", {}


def main():
    ph = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); b = json.loads(sys.argv[2]); gop = sys.argv[3] if len(sys.argv) > 3 else None
    W = Path(b["W"]); (W / "bao-cao").mkdir(parents=True, exist_ok=True); (W / "log").mkdir(exist_ok=True)
    prompt = loi_nhac(ph, b, gop); ai = b.get("AI", "claude"); t0 = time.time()
    print(f"{ai} làm bước «{ph['ten']}» trong {b['P']}", flush=True)
    kq, tk = (goi_codex if ai == "codex" else goi_claude)(prompt, b, ph)
    giay = round(time.time() - t0)
    with open(W / "token.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"buoc": ph["id"], "provider": ai, "giay": giay, **tk}, ensure_ascii=False) + "\n")
    print(f"{ai}: {giay} s · {tk.get('luot') or '?'} lượt\n{kq[-3000:]}", flush=True)
    thieu = [x for x in (thay(f, b) for f in ph.get("ra", [])) if not Path(x).exists() or Path(x).stat().st_mtime < t0 - 1]
    if thieu:
        raise SystemExit("AI chưa tạo/cập nhật: " + ", ".join(thieu))
    if ph.get("kiem"):
        r = subprocess.run(["zsh", "-c", thay(ph["kiem"], b)], capture_output=True, text=True, env=ENV)
        print(r.stdout[-3000:], r.stderr[-1500:])
        if r.returncode:
            raise SystemExit("Lệnh kiểm sau bước AI chưa đạt — xem log.")


if __name__ == "__main__":
    main()
