#!/bin/zsh
# Dự án GHÉP NHIỀU CLIP: new_montage.sh <tên-ngắn> <clip1> <clip2> ... [--ref <video mẫu>] [--style-from <dự án cũ>]
# - Chuẩn hoá mỗi clip → motion/public/clips/c1.mp4, c2.mp4… (áp xoay iPhone, 30 fps CFR, AAC 48 kHz stereo; clip câm thì thêm tiếng lặng)
# - Phân tích từng clip vào check/cN/: transcript.srt, words.srt (mốc từng từ), loud.txt (độ lớn mỗi 0,5 s),
#   contact.jpg, half.jpg (lưới khung mỗi 0,5 s, 13 khung/hàng)
# - Chép template Remotion dựng cả video, tạo hiệu ứng âm thanh + nhạc nền, cài npm
# Dòng cuối in đường dẫn dự án.
set -e
export PATH=/opt/homebrew/bin:$PATH
export NVM_DIR="$HOME/.nvm"; [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
SKILL=${0:A:h:h}
MODEL=~/whisper-models/ggml-large-v3-turbo.bin
NAME=${1:?thiếu tên ngắn}; shift
CLIPS=(); REF=""; STYLE_FROM=""
while (( $# )); do
  case "$1" in
    --ref) REF=$2; shift 2;;
    --style-from) STYLE_FROM=$2; shift 2;;
    *) CLIPS+=("$1"); shift;;
  esac
done
(( ${#CLIPS} >= 1 )) || { echo "Cần ít nhất 1 clip"; exit 1; }
source "$SKILL/scripts/noi_luu.sh"; P=$(noi_luu "$NAME")   # hl-<tên>-<id> → tap-<tên>/3-highlight/clip-<id>; vlog-<tên> → vlog/<tên>
[ -e "$P" ] && { echo "Đã có $P — chọn tên khác"; exit 1; }
mkdir -p "${P:h}"
mkdir -p "$P"/{src,check,ref}
cp -RL "$SKILL/assets/montage-template" "$P/motion"   # -L: chép BẢN THẬT thư viện hình (src/lib — phụ đề, nhận diện, màn chốt, biểu tượng, màn kết, minh hoạ)
python3 -I "$SKILL/../khoi/hoso.py" ghep-vlog "$P/motion/src/hoso.json" >/dev/null   # hồ sơ tham số (highlight: hl_edl.py ghi đè)
echo 'export default {};' > "$P/motion/src/guard.js"   # lớp phủ tự chuyển toàn màn hình — overlay_guard.py ghi đè
mkdir -p "$P/motion/public/sfx"; cp "$SKILL/assets/sfx/ting.wav" "$SKILL/assets/sfx/tua.wav" "$P/motion/public/sfx/"   # ting màn chốt · vút chuyển cảnh highlight
C="$P/motion/public/clips"; mkdir -p "$C" "$P/motion/public/sfx"
[ -n "$REF" ] && cp "$REF" "$P/ref/mau.${REF:e}"
[ -n "$STYLE_FROM" ] && echo "$STYLE_FROM" > "$P/ref/style-from.txt"

: > "$P/clips.tsv"
i=0
for f in "${CLIPS[@]}"; do
  i=$((i+1)); id=c$i; O="$P/check/$id"; mkdir -p "$O"
  cp "$f" "$P/src/"
  ENC=(-c:v libx264 -preset fast -crf 17 -g 10 -pix_fmt yuv420p -r 30 -movflags +faststart)
  if ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$f" | grep -q .; then
    # Cân GIỌNG từng clip về −20 LUFS (người dùng chỉ ra 2026-11-04: vlog Haruku 3 clip −17 / −34 / −23 LUFS → nhạc lấn lời ở clip
    # nhỏ, người xem phải chỉnh âm lượng giữa các phần). Gain tuyến tính (không nén), chặn đỉnh bằng alimiter; tối đa +18 dB.
    G=$(ffmpeg -nostats -i "$f" -af ebur128 -f null - 2>&1 | awk '/ I: /{v=$2} END{g=-20-v; if(g>18)g=18; if(g<-10)g=-10; printf "%.1f", g}')
    ffmpeg -v error -y -i "$f" -map 0:v:0 -map 0:a:0 $ENC -af "volume=${G}dB,alimiter=limit=0.95:level=disabled" -c:a aac -b:a 192k -ar 48000 -ac 2 "$C/$id.mp4"
  else
    ffmpeg -v error -y -i "$f" -f lavfi -i anullsrc=r=48000:cl=stereo -map 0:v:0 -map 1:a -shortest $ENC -c:a aac -b:a 192k "$C/$id.mp4"
  fi
  WH=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$C/$id.mp4")
  DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$C/$id.mp4")
  printf "%s\t%s\t%s\t%.2fs\n" $id "${f:t}" $WH $DUR >> "$P/clips.tsv"
  # Lời nói: đoạn câu + mốc từng từ. Whisper hay BỊA câu ("Hãy subscribe cho kênh…") khi không có lời → đối chiếu loud.txt
  ffmpeg -v error -y -i "$C/$id.mp4" -vn -ac 1 -ar 16000 "$O/a.wav"
  # Quay ngoài trời (gió, bước chân, đám đông) → Whisper bịa "Hãy subscribe…" cả clip. Lọc ồn + cân tiếng RIÊNG cho bản chép lời
  # (a.wav giữ nguyên cho loud.txt) và -mc 0 (không mang ngữ cảnh câu bịa sang đoạn sau) — vlog leo núi 2026-11-03: 10/48 clip hết bịa.
  ffmpeg -v error -y -i "$O/a.wav" -af "highpass=f=120,lowpass=f=6000,afftdn=nf=-25,dynaudnorm" "$O/w.wav"
  # LOI_SAN=<thư mục có words.srt + transcript.srt CỦA CHÍNH FILE NÀY> (highlight: clip c1 = video nguồn đã chép lời ở check/goc)
  # → dùng lại, không cho Whisper chép lại cả video dài cho từng clip (10/11/2026: tập 14 phút mất ~30 phút mỗi clip).
  if [[ -n "$LOI_SAN" && "$id" == c1 && -s "$LOI_SAN/words.srt" && -s "$LOI_SAN/transcript.srt" ]]; then
    cp "$LOI_SAN/words.srt" "$O/words.srt"; cp "$LOI_SAN/transcript.srt" "$O/transcript.srt"
  else
  whisper-cli -m $MODEL -l vi -f "$O/w.wav" -mc 0 -osrt -of "$O/transcript" -np >/dev/null 2>&1 || true
  whisper-cli -m $MODEL -l vi -f "$O/w.wav" -mc 0 -ml 1 -sow -osrt -of "$O/words" -np >/dev/null 2>&1 || true
  fi
  rm -f "$O/w.wav"
  ffmpeg -v error -i "$O/a.wav" -af "asetnsamples=8000,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null - \
    | grep RMS | awk -F= '{printf "%.1fs %d dB\n", (NR-1)*0.5, $2}' > "$O/loud.txt"
  rm -f "$O/a.wav"
  # Hình: 24 khung trải đều + lưới mỗi 0,5 s (mỗi ảnh tối đa 26 khung = 13 s)
  STEP=$(python3 -c "print(max(0.5, $DUR / 24))")
  ffmpeg -v error -y -i "$C/$id.mp4" -vf "fps=1/$STEP,scale=270:-2,tile=6x4:padding=4:color=white" -frames:v 1 "$O/contact.jpg"
  k=0; t=0
  while python3 -c "exit(0 if $t < $DUR - 0.6 or $t == 0 else 1)"; do   # phần dư < 0,6 s không ra khung nào → ffmpeg lỗi, bỏ
    ffmpeg -v error -y -ss $t -t 13 -i "$C/$id.mp4" -vf "fps=2,scale=180:-2,tile=13x2:padding=2" -frames:v 1 "$O/half_$(printf %02d $k).jpg"
    k=$((k+1)); t=$((t+13))
  done
done

( cd "$P/motion" && npm install --no-fund --no-audit >/dev/null 2>&1 && npm approve-scripts esbuild >/dev/null 2>&1 || true
  node make-audio.mjs >/dev/null )
echo "Clip (id · file gốc · kích thước · thời lượng):"; cat "$P/clips.tsv"
echo "$P"
