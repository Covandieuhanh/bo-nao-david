#!/bin/zsh
# MÁY NÀY DỰNG RA GIỐNG MAC CHÍNH CHƯA? — chạy sau cai-cong-cu-video.sh, và mỗi khi đổi phiên bản công cụ.
#   zsh kiem-may.sh                  so công cụ với phien-ban.env + dựng thử bộ thử máy, so với bản chuẩn của Mac
#   zsh kiem-may.sh --tao-chuan <video> [giây bắt đầu]   (CHỈ MAC CHÍNH) cắt 20 s, dựng bằng Mac, lưu làm bản chuẩn
# Bộ thử máy nằm trên Drive: tu-lieu-goc/_bo-thu-may/ (video gốc không lên GitHub). Chỉ định chỗ khác: BO_THU=<thư mục>.
# Dựng thử bằng đúng script của skill: tao-du-an.sh → phan-tich-video.sh (Whisper) → do-mat.sh → xem-truoc.mjs + xuat-video.mjs (Remotion).
# Dự án thử ở ~/Movies/tap-thu-may-<giờ>, xong thì xoá. Kết quả: ĐẠT / LỆCH từng mục, mã thoát 0 = máy dùng được như Mac.
setopt nullglob
HERE=${0:A:h}; REPO=${HERE:h:h}
SK="$REPO/ky-nang/san-xuat-video/dung-video-theo-phong-cach"
source "$HERE/phien-ban.env"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && nvm use -s "$NODE" >/dev/null 2>&1
CACHE=~/.cache/dung-video-theo-phong-cach
LECH=0
dong() { print -r -- "$1"; if [[ $1 == LỆCH* || $1 == THIẾU* ]]; then LECH=1; fi; return 0; }
co() { if [ $2 = 0 ]; then dong "ĐẠT  $1"; else dong "THIẾU $1 — chạy lại cai-cong-cu-video.sh"; fi; }

# ---------- Bộ thử máy ----------
if [ -z "$BO_THU" ]; then
  source "$SK/scripts/drive-chung.sh" 2>/dev/null && tim_drive && BO_THU="$G/tu-lieu-goc/_bo-thu-may"
fi
if [ "$1" = --tao-chuan ]; then
  [[ $OSTYPE == darwin* ]] || { echo "Bản chuẩn chỉ tạo trên Mac chính"; exit 2; }
  [ -n "$BO_THU" ] || { echo "Không thấy Drive — đặt BO_THU=<thư mục>"; exit 2; }
  V=${2:?thiếu video}; T0=${3:-0}
  rm -rf "$BO_THU"; mkdir -p "$BO_THU/chuan"
  ffmpeg -v error -y -ss $T0 -t 20 -i "$V" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 160k "$BO_THU/clip.mp4" || exit 1
  TAO_CHUAN=1
fi
[ -n "$BO_THU" ] && [ -f "$BO_THU/clip.mp4" ] || { echo "⛔ Không thấy bộ thử máy (${BO_THU:-Drive}/clip.mp4). Mở Google Drive, hoặc đặt BO_THU=<thư mục>."; exit 2; }

# ---------- 1. Công cụ đúng bản khoá ----------
print "== 1. Công cụ (so với phien-ban.env)"
ffmpeg -version 2>/dev/null | head -1 | grep -q "version n\?$FFMPEG"; co "ffmpeg $FFMPEG ($(ffmpeg -version 2>/dev/null | head -1 | awk '{print $3}'))" $?
whisper-cli --version 2>&1 | grep -q "$WHISPER_CPP"; co "whisper.cpp $WHISPER_CPP" $?
[ -s ~/whisper-models/ggml-large-v3-turbo.bin ]; co "mô hình Whisper" $?
[ "$(node -v 2>/dev/null)" = "v$NODE" ]; co "node $NODE ($(node -v 2>/dev/null))" $?
python3 -c "import PIL,sys;sys.exit(PIL.__version__!='$PILLOW')" 2>/dev/null; co "Pillow $PILLOW" $?
$CACHE/podcast-venv/bin/python -c "import numpy" 2>/dev/null; co "môi trường podcast (numpy)" $?
~/.venvs/pyannote/bin/python -c "import pyannote.audio,torch,sys;sys.exit(pyannote.audio.__version__!='$PYANNOTE_AUDIO' or not torch.__version__.startswith('$TORCH'))" 2>/dev/null; co "pyannote $PYANNOTE_AUDIO + torch $TORCH" $?
[ -d ~/.cache/torch/pyannote/models--pyannote--speaker-diarization-3.1 ] && dong "ĐẠT  mô hình tách người nói" || print "CHÚ Ý mô hình tách người nói chưa có (podcast nhiều người sẽ đoán theo giọng) — xem cai-cong-cu-video.sh"
if [[ $OSTYPE != darwin* ]]; then
  $CACHE/mat-venv/bin/python -c "import cv2" 2>/dev/null && [ -s $CACHE/face_detection_yunet_2023mar.onnx ] && [ -s $CACHE/face_landmarker.task ]; co "dò mặt (YuNet)" $?
  $CACHE/mat-venv/bin/python -c "import mediapipe" 2>/dev/null && dong "ĐẠT  đo độ mở miệng (MediaPipe)" || print "CHÚ Ý chưa có MediaPipe (máy chip ARM) — dò được mặt, đoán người nói theo miệng kém hơn Mac"
fi
command -v zsh >/dev/null && command -v rsync >/dev/null; co "zsh, rsync" $?

# ---------- 2. Dựng thử ----------
print "\n== 2. Dựng thử 20 s (đúng script của skill)"
TEN=thu-may-$(date +%H%M%S)
OUT=$(zsh "$SK/scripts/tao-du-an.sh" "$BO_THU/clip.mp4" "" $TEN 2>&1) || { print -r -- "$OUT"; dong "LỆCH tạo dự án"; exit 1; }
P=${${(f)OUT}[-1]}
dong "ĐẠT  tạo dự án + cài Remotion $REMOTION ($(grep -m1 '"version"' $P/chuyen-dong/node_modules/remotion/package.json | grep -o '[0-9.]*'))"
don_du_an() { rm -rf ~/Movies/tap-$TEN; }
trap don_du_an EXIT
M="$P/kiem-tra/goc"
zsh "$SK/scripts/phan-tich-video.sh" "$P/tu-lieu/video-goc.mp4" "$M" >/dev/null || dong "LỆCH Whisper không chạy"
mkdir -p "$P/kiem-tra/mat/f"
ffmpeg -v error -y -i "$P/tu-lieu/video-goc.mp4" -vf "fps=2,scale=360:-2" -q:v 5 "$P/kiem-tra/mat/f/f_%05d.jpg"
zsh "$SK/scripts/do-mat.sh" "$P/kiem-tra/mat/f" "$P/kiem-tra/mat/khuon-mat.json" >/dev/null 2>&1 || dong "LỆCH dò mặt không chạy"

if [ -n "$TAO_CHUAN" ]; then
  cp "$M/ban-chep-loi.srt" "$BO_THU/chuan/"; cp "$P/kiem-tra/mat/khuon-mat.json" "$BO_THU/chuan/"
  python3 -I "$SK/scripts/phu-de.py" "$P" >/dev/null && cp "$P/chuyen-dong/src/phu-de.js" "$BO_THU/"
  python3 - "$P/chuyen-dong/src/canh.js" "$BO_THU/canh.js" <<'EOF'
import sys
s = open(sys.argv[1], encoding="utf-8").read()
c = """  {id: 'thu-the', type: 'card', start: 1.0, end: 9.0, props: {variant: 'year', eyebrow: 'ĐI LÀM TỪ', from: 2011, to: 2026, toAt: 1.5, fromAt: 3.0, footer: 'Thử máy dựng video', footerAt: 4.5}},
  {id: 'thu-the-2', type: 'card', start: 10.0, end: 18.0, props: {variant: 'year', eyebrow: 'GIỐNG MAC TỪ', from: 2020, to: 2026, toAt: 10.5, fromAt: 12.0, footer: 'Kiểm tra máy mới', footerAt: 13.5}},
"""
s = s.replace("export const SCENES = [\n", "export const SCENES = [\n" + c, 1)
open(sys.argv[2], "w", encoding="utf-8").write(s)
EOF
fi
cp "$BO_THU/canh.js" "$BO_THU/phu-de.js" "$P/chuyen-dong/src/"
CHUP=(thu-the@3 thu-the@7 thu-the-2@15.5 phu-de@4 phu-de@12)
( cd "$P/chuyen-dong" && node xem-truoc.mjs $CHUP >/dev/null 2>"$P/kiem-tra/loi-chup.txt" ) || { tail -5 "$P/kiem-tra/loi-chup.txt"; dong "LỆCH Remotion không chụp được khung"; }
( cd "$P/chuyen-dong" && node xuat-video.mjs thu-the-2 >/dev/null 2>"$P/kiem-tra/loi-xuat.txt" ) || { tail -5 "$P/kiem-tra/loi-xuat.txt"; dong "LỆCH Remotion không xuất được cảnh"; }
[ -s "$P/tu-lieu/thu-the-2.mov" ] && dong "ĐẠT  xuất cảnh ProRes có nền trong ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$P/tu-lieu/thu-the-2.mov" | cut -c1-4) s)"

if [ -n "$TAO_CHUAN" ]; then
  for c in $CHUP; do cp "$P/kiem-tra/chuyen-dong/$c.png" "$BO_THU/chuan/"; done
  { print "Bộ thử máy — tạo trên Mac chính $(date '+%d/%m/%Y %H:%M') từ ${V:t} (giây $T0, 20 s)."
    print "Công cụ lúc tạo: $(ffmpeg -version | head -1 | awk '{print $3}'), whisper $(whisper-cli --version 2>&1 | grep -o '[0-9.]*' | head -1), node $(node -v)"; } > "$BO_THU/README.txt"
  print "\n✅ Đã lưu bản chuẩn ở $BO_THU"; exit 0
fi

# ---------- 3. So với bản chuẩn Mac ----------
print "\n== 3. So với bản chuẩn Mac chính"
[ -s "$M/ban-chep-loi.srt" ] && dong "$(python3 -I "$HERE/so-sanh.py" loi "$BO_THU/chuan/ban-chep-loi.srt" "$M/ban-chep-loi.srt")" || dong "LỆCH chép lời: không có kết quả"
[ -s "$P/kiem-tra/mat/khuon-mat.json" ] && dong "$(python3 -I "$HERE/so-sanh.py" mat "$BO_THU/chuan/khuon-mat.json" "$P/kiem-tra/mat/khuon-mat.json")" || dong "LỆCH dò mặt: không có kết quả"
for c in $CHUP; do
  [ -f "$P/kiem-tra/chuyen-dong/$c.png" ] && dong "$(python3 -I "$HERE/so-sanh.py" hinh "$BO_THU/chuan/$c.png" "$P/kiem-tra/chuyen-dong/$c.png")" || dong "LỆCH thiếu khung $c"
done
print
[ $LECH = 0 ] && print "✅ MÁY NÀY DỰNG GIỐNG MAC CHÍNH — dùng được." || print "⚠ Còn mục LỆCH/THIẾU ở trên — gửi kết quả này cho Claude để sửa."
exit $LECH
