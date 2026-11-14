# Tìm & tải ảnh giấy phép mở từ Openverse (không cần key).
#   search <dự án> <queries.json>   queries.json = [{"key": "02", "q": "waiter restaurant"}, ...]
#       → images/candidates.json + images/thumbs/<key>_<i>.jpg + images/sheets/<key>.jpg (8 ảnh/hàng, đánh số 0–7 từ trái)
#   fetch <dự án> <picks.json>       picks.json = {"02": 5, "05": 0, ...}  (key → số thứ tự ảnh trong hàng)
#       → motion/public/photos/<key>.jpg + images/credits.tsv
# Openverse chậm (10–30 s/lượt) nên chạy tuần tự; lượt lỗi tự thử lại. Openverse không trả lời (đã gặp: quá giờ cả
# loạt) → tự chuyển sang tìm thẳng trên Wikimedia Commons (chỉ giữ CC0 / PD / CC BY / CC BY-SA — dùng thương mại được).
import json, os, re, subprocess, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import UA, curl, node_env, wiki_thumb

def wikimedia(q):
    params = urllib.parse.urlencode({"action": "query", "generator": "search", "gsrsearch": q + " filetype:bitmap",
        "gsrnamespace": 6, "gsrlimit": 20, "prop": "imageinfo", "iiprop": "url|size|extmetadata", "format": "json"})
    out = subprocess.run(["curl", "-s", "-f", "-m", "60", "-A", UA, "https://commons.wikimedia.org/w/api.php?" + params],
                         capture_output=True).stdout
    pages = sorted(json.loads(out)["query"]["pages"].values(), key=lambda p: p.get("index", 0))
    items = []
    for p in pages:
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        if re.search(r"NC|ND", lic) or not re.match(r"(CC0|CC BY|Public domain|PD)", lic, re.I): continue
        if ii.get("width", 0) < 1000: continue
        name, ver = (("cc0", "1.0") if lic.upper().startswith("CC0") else ("pdm", "") if lic.lower().startswith(("public", "pd"))
                     else (lic[3:].split()[0].lower(), (lic.split()[-1] if re.search(r"\d", lic) else "")))
        items.append({"id": p["pageid"], "title": re.sub(r"^File:|\.\w+$", "", p["title"]), "url": ii["url"],
                      "creator": re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()[:60] or None,
                      "license": name, "license_version": ver, "foreign_landing_url": ii["descriptionurl"],
                      "width": ii["width"], "height": ii["height"], "source": "wikimedia"})
        if len(items) == 8: break
    return items

def search(project, qfile):
    img = os.path.join(project, "images")
    os.makedirs(os.path.join(img, "thumbs"), exist_ok=True)
    os.makedirs(os.path.join(img, "sheets"), exist_ok=True)
    cpath = os.path.join(img, "candidates.json")
    res = json.load(open(cpath)) if os.path.exists(cpath) else {}
    ov_down = False
    for q in json.load(open(qfile)):
        # ẢNH CHỈ TẠI VIỆT NAM, NGƯỜI VIỆT (David 13/11/2026): từ khoá chưa có Việt Nam thì tự thêm "Vietnam"
        if not re.search(r"viet ?nam|việt nam|hanoi|hà nội|saigon|sài gòn|ho chi minh", q["q"], re.I): q["q"] += " Vietnam"
        params = urllib.parse.urlencode({"q": q["q"], "license_type": "commercial", "page_size": 8, "mature": "false", "size": "large"})
        items = None
        for attempt in range(0 if ov_down else 2):   # Openverse đã hỏng ở từ khoá trước → khỏi chờ lại
            try:
                data = json.load(urllib.request.urlopen(urllib.request.Request(
                    "https://api.openverse.org/v1/images/?" + params, headers={"User-Agent": UA}), timeout=90))
                items = [{k: r.get(k) for k in ("id", "title", "url", "creator", "license", "license_version",
                                                "foreign_landing_url", "width", "height", "source")} for r in data.get("results", [])]
                break
            except Exception as e:
                time.sleep(3)
        if not items:
            ov_down = True
            try: items = wikimedia(q["q"]); print(q["key"], "Openverse lỗi → Wikimedia Commons")
            except Exception: items = None
        if not items:
            print(q["key"], "LỖI tìm", q["q"]); continue
        res[q["key"]] = {"q": q["q"], "items": items}
        json.dump(res, open(cpath, "w"), ensure_ascii=False, indent=1)
        args, filt = [], ""
        for i in range(8):
            dst = os.path.join(img, "thumbs", f"{q['key']}_{i}.jpg")
            if os.path.exists(dst): os.remove(dst)
            if i < len(items):
                curl(wiki_thumb(items[i]["url"], 500), dst, 60); time.sleep(0.4)
            ok = os.path.exists(dst) and subprocess.run(["ffprobe", "-v", "error", dst], env=node_env(), capture_output=True).returncode == 0
            args += ["-i", dst] if ok else ["-f", "lavfi", "-i", "color=gray:s=240x180"]
            filt += f"[{i}:v]scale=240:180:force_original_aspect_ratio=decrease,pad=240:180:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1[v{i}];"
        subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-filter_complex",
                        filt + "".join(f"[v{i}]" for i in range(8)) + "hstack=inputs=8", "-frames:v", "1",
                        os.path.join(img, "sheets", f"{q['key']}.jpg")], env=node_env())
        print(q["key"], q["q"], len(items), "ảnh")

def fetch(project, pfile):
    img = os.path.join(project, "images")
    res = json.load(open(os.path.join(img, "candidates.json")))
    photos = os.path.join(project, "motion/public/photos")
    os.makedirs(photos, exist_ok=True)
    cpath = os.path.join(img, "credits.tsv")
    credits = {}
    if os.path.exists(cpath):
        for l in open(cpath).read().splitlines():
            if l.strip(): credits[l.split("\t")[0]] = l
    for key, i in json.load(open(pfile)).items():
        it = res[key]["items"][i]
        raw = os.path.join(img, f"{key}.raw")
        u = wiki_thumb(it["url"], 1280) if (it.get("width") or 0) > 1280 else it["url"]
        if not curl(u, raw, 120):
            print(key, "LỖI tải"); continue
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-frames:v", "1", "-vf", "scale='min(1600,iw)':-2",
                        "-q:v", "3", os.path.join(photos, f"{key}.jpg")], env=node_env())
        lic = (it["license"] or "").upper() + (" " + it["license_version"] if it.get("license_version") else "")
        lic = "CC0 1.0" if lic.startswith("CC0") else ("Public Domain" if lic.startswith("PDM") else "CC " + lic)
        credits[key] = f"{key}\t\"{it['title']}\" — {it['creator'] or 'không rõ tác giả'} — {lic} — {it['foreign_landing_url']}"
        print(key, "ok", lic)
        time.sleep(0.5)
    open(cpath, "w").write("\n".join(credits[k] for k in sorted(credits)) + "\n")

if __name__ == "__main__":
    {"search": search, "fetch": fetch}[sys.argv[1]](os.path.expanduser(sys.argv[2]), sys.argv[3])
