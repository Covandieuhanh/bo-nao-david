# Soát điểm cắt bằng độ lớn tiếng thật: kiem-am-luong.py <dự án> [mã phương án]
# Mốc từ của Whisper hay lệch ở chỗ ngắt câu (chữ đầu bị kéo sớm vào khoảng lặng, chữ cuối kéo dài) → cắt theo đó dễ lọt đuôi
# chữ câu trước hoặc mất đầu chữ. Script đọc kiem-tra/goc/am-luong-05.txt (tao-doan-noi-bat.sh tạo, 0,05 s/dòng) và phuong-an.json,
# với mỗi câu in dải độ lớn quanh start/end (█ có tiếng · ▁ lặng) + mốc đề xuất:
#   start → chỗ tiếng bắt đầu sau khoảng lặng chứa/đứng trước mốc Whisper (lặng bắt đầu ≤ start + 0,3 s, dứt ≤ start + 1,8 s)
#   end   → chỗ tiếng dứt ở khoảng lặng ĐẦU TIÊN bắt đầu sau chữ cuối (≥ end − 0,15 s, trong 1 s) — không lấy chỗ ngập
#           ngừng giữa câu (đã gặp: "…nhìn nhận được ‖ mình là ai" — lấy lặng dài nhất sẽ cắt mất "là ai")
# "⚠ nói liền" = không có khoảng lặng ≥ 0,15 s đúng chỗ (câu nối liền câu khác) → giữ mốc Whisper, đối chiếu lời ở bước kiểm
# (cat-doan-noi-bat.py chép lời lại bản cắt). "⚠ lệch > 1 s" = mốc Whisper sai nhiều, xem kỹ dải trước khi theo.
# Chỉ in — Claude sửa phuong-an.json theo đề xuất hợp lý rồi chạy cat-doan-noi-bat.py.
import json, os, sys

P = os.path.expanduser(sys.argv[1]); only = sys.argv[2] if len(sys.argv) > 2 else None
L = [tuple(map(float, l.split())) for l in open(os.path.join(P, "kiem-tra/goc/am-luong-05.txt")) if l.strip()]
lv = sorted(v for _, v in L)
p10, p50 = lv[len(lv) // 10], lv[len(lv) // 2]
THR = p10 + 0.35 * (p50 - p10)   # nền ồn → lời nói: ngưỡng gần phía nền (thu ngoài trời/podcast có nhạc vẫn bắt được)
STEP, MINQ = 0.05, 3              # một khoảng lặng ≥ 3 ô = 0,15 s
idx = lambda t: max(0, min(len(L) - 1, round(t / STEP)))
loud = lambda i: L[i][1] >= THR

def quiet_runs(a, b):
    runs, i0 = [], None
    for i in range(idx(a), idx(b) + 1):
        if not loud(i): i0 = i if i0 is None else i0
        else:
            if i0 is not None and i - i0 >= MINQ: runs.append((i0, i))
            i0 = None
    if i0 is not None and idx(b) + 1 - i0 >= MINQ: runs.append((i0, idx(b) + 1))
    return runs

def strip(t, before, after):
    a, b = idx(t - before), idx(t + after)
    return "".join(("│" if i == idx(t) else "") + ("█" if loud(i) else "▁") for i in range(a, b + 1))

plan = json.load(open(os.path.join(P, "phuong-an.json"), encoding="utf-8"))
print(f"Ngưỡng có tiếng {THR:.1f} dB (nền {p10:.0f}, giữa {p50:.0f}) · │ = mốc hiện tại · mỗi ô 0,05 s")
for opt in plan["options"]:
    if only and opt["id"] != only: continue
    print(f"\n=== Phương án {opt['id']}")
    for k, p in enumerate(opt["pieces"], 1):
        s, e = p["start"], p["end"]
        rs = [r for r in quiet_runs(s - 0.8, s + 1.8) if r[0] <= idx(s + 0.3) and r[1] <= idx(s + 1.8)]
        ss = round(rs[-1][1] * STEP, 2) if rs else None
        re_ = [r for r in quiet_runs(e - 0.15, e + 1.0) if r[0] >= idx(e - 0.15)]
        ee = round(re_[0][0] * STEP, 2) if re_ else None
        far = lambda a, b: "  ⚠ lệch > 1 s" if abs(a - b) > 1 else ""
        fs = f"{ss:.2f}{far(ss, s)}" if ss is not None else "⚠ nói liền"
        fe = f"{ee:.2f}{far(ee, e)}" if ee is not None else "⚠ nói liền"
        print(f"{k}. {p.get('role', '')} «{p.get('text', '')[:60]}»")
        print(f"   start {s:7.2f} → {fs:>10}   {strip(s, 0.8, 1.8)}")
        print(f"   end   {e:7.2f} → {fe:>10}   {strip(e, 1.0, 1.0)}")
