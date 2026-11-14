#!/usr/bin/env python3
"""Quét repo tìm bí mật trước khi đẩy. Chỉ in tên file và số dòng, không in giá trị. Có phát hiện thì dừng (exit 1)."""
import os
import re
import sys

MAU = {
    "khoá Anthropic": r"sk-ant-[A-Za-z0-9_-]{10,}",
    "khoá OpenAI": r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}",
    "token GitHub": r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}",
    "khoá Google": r"AIza[0-9A-Za-z_-]{30,}|ya29\.[0-9A-Za-z_-]{20,}",
    "token Telegram": r"\b\d{8,10}:[A-Za-z0-9_-]{30,}",
    "token Slack": r"xox[baprs]-[A-Za-z0-9-]{10,}",
    "khoá AWS": r"\bAKIA[0-9A-Z]{16}\b",
    "khoá riêng": r"BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY",
    "JWT": r"\beyJ[A-Za-z0-9_-]{15,}\.eyJ[A-Za-z0-9_-]{15,}\.",
    "chuỗi kết nối có mật khẩu": r"\b(?:postgres|postgresql|mysql|mongodb)://[^\s:/]+:[^\s@]+@",
    "gán mật khẩu": r"(?i)(?:password|passwd|mật khẩu|api[_-]?key|client_secret|secret_key)[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9!@#$%^&*_+./-]{8,}",
    "số căn cước": r"(?i)(?:CCCD|căn cước|CMND)\D{0,12}\d{9,12}",
}
MAU = {k: re.compile(v) for k, v in MAU.items()}
TEN_CAM = re.compile(r"(?i)^(\.env(\..*)?|mk\.csv|\.claude\.json.*|cookies?.*|.*\.(pem|key|p12|jsonl|sqlite|mp4|mov))$")
# Tài liệu mẫu của skill dieu-khien-trinh-duyet có mật khẩu ví dụ, không phải bí mật thật.
BO_QUA = (os.path.join("ky-nang", "dieu-khien-trinh-duyet") + os.sep,)
THU_MUC_BO_QUA = {".git", "node_modules"}


def main(goc):
    loi = []
    so_file = 0
    for thu_muc, con, cac_file in os.walk(goc):
        con[:] = [c for c in con if c not in THU_MUC_BO_QUA]
        for ten in cac_file:
            duong = os.path.join(thu_muc, ten)
            tuong_doi = os.path.relpath(duong, goc)
            if tuong_doi == os.path.join("tu-dong-hoa", "quet-bi-mat.py"):
                continue
            so_file += 1
            if TEN_CAM.match(ten):
                loi.append((tuong_doi, 0, "tên file bị cấm"))
                continue
            if os.path.islink(duong) or tuong_doi.startswith(BO_QUA):
                continue
            try:
                with open(duong, encoding="utf8") as f:
                    for so, dong in enumerate(f, 1):
                        for nhan, mau in MAU.items():
                            if mau.search(dong):
                                loi.append((tuong_doi, so, nhan))
            except (UnicodeDecodeError, OSError):
                continue  # file nhị phân
    print(f"Đã quét {so_file} file.")
    if loi:
        print("DỪNG — nghi có bí mật:")
        for f, so, nhan in loi:
            print(f"  {f}:{so} — {nhan}")
        return 1
    print("Không phát hiện bí mật.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
