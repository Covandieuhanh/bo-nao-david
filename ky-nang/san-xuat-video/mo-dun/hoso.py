"""Đọc HỒ SƠ THAM SỐ (san-xuat-video/ho-so): load('lam-video') → chung.json gộp với lam-video.json (khoá loại ghi đè, gộp sâu).
Mọi script lấy con số từ đây — đổi tham số chỉ sửa file hồ sơ, không sửa code. get(cfg, 'cat_lang.dai.min_s', 1.2) có mặc định."""
import json, os
D = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "ho-so-thuong-hieu")
def _merge(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = _merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out
def load(loai):
    c = json.load(open(os.path.join(D, "chung.json"), encoding="utf-8"))
    p = os.path.join(D, loai + ".json")
    return _merge(c, json.load(open(p, encoding="utf-8"))) if os.path.exists(p) else c
def get(cfg, path, default=None):
    for k in path.split("."):
        if not isinstance(cfg, dict) or k not in cfg: return default
        cfg = cfg[k]
    return cfg
def dump(loai, dst):
    """Chép hồ sơ đã gộp vào dự án (motion/src/hoso.json) cho khung dựng đọc."""
    json.dump(load(loai), open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2: dump(sys.argv[1], sys.argv[2]); print(sys.argv[2])
    else: print(json.dumps(load(sys.argv[1] if len(sys.argv) > 1 else "chung"), ensure_ascii=False, indent=1))
