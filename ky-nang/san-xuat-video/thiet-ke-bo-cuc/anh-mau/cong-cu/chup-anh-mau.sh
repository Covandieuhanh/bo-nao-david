#!/bin/zsh
# Chụp lại ảnh mẫu từng kiểu (thiet-ke-bo-cuc/bo-cuc.md mục "Ảnh mẫu"): mẫu thử + người giả, khung dọc và ngang.
#   zsh chup-anh-mau.sh [lọc]     — lọc: chỉ chụp kiểu có id chứa chữ này (vd. dung-hay). Thêm kiểu mới: thêm một dòng ở canh-mau.mjs.
# Cần: node + npm, ffmpeg, python3 có Pillow (pip install pillow). Chạy được trên Mac, Linux, Windows qua WSL2.
set -e
HERE=${0:A:h}; OUT=${HERE:h}; KHUON=${HERE:h:h:h}/dung-video-theo-phong-cach/assets/mau-remotion
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
python3 "$HERE/nguoi-gia.py" "$T"
node "$HERE/canh-mau.mjs" > "$T/canh.js"
DUR=$(node -e "const s=require('fs').readFileSync('$T/canh.js','utf8');const a=JSON.parse(s.match(/SCENES = (\[.*\]);/)[1]);console.log(Math.ceil(a[a.length-1].end+8))")
ARGS=$(node -e "const s=require('fs').readFileSync('$T/canh.js','utf8');const a=JSON.parse(s.match(/SCENES = (\[.*\]);/)[1]);console.log(a.filter(x=>x.id.includes('${1:-}')).map(x=>x.id+'@'+(x.start+3.6)).join(' '))")
for o in doc ngang; do
  D=$T/$o; mkdir -p $D/tu-lieu; cp -RL "$KHUON" $D/chuyen-dong; mkdir -p $D/chuyen-dong/public/anh; cp $T/anh1.jpg $T/anh2.jpg $D/chuyen-dong/public/anh/
  if [ $o = doc ]; then WH="width: 1080, height: 1920"; M='{cx: 0.5, cy: 0.36, w: 0.22, h: 0.15}'; SC=480:-1; else WH="width: 1920, height: 1080"; M='{cx: 0.66, cy: 0.36, w: 0.124, h: 0.26}'; SC=800:-1; fi
  ffmpeg -v error -y -loop 1 -i $T/nguoi-$o.jpg -t $DUR -r 30 -c:v libx264 -preset ultrafast -pix_fmt yuv420p $D/tu-lieu/video-goc.mp4
  echo "export default {fpsNum: 30, fpsDen: 1, $WH, duration: $DUR, source: 'video-goc.mp4', topic: 'Ảnh mẫu'};" > $D/chuyen-dong/src/du-an.js
  grep -v '^//PHUDE' $T/canh.js > $D/chuyen-dong/src/canh.js
  node -e "const s=require('fs').readFileSync('$T/canh.js','utf8');const a=JSON.parse(s.match(/SCENES = (\[.*\]);/)[1]);console.log('const m = $M; export default {'+a.map(x=>JSON.stringify(x.id)+': m').join(', ')+'};')" > $D/chuyen-dong/src/mat.js
  python3 -I "$KHUON/../../../mo-dun/ho_so.py" lam-video $D/chuyen-dong/src/ho-so.json >/dev/null
  ( cd $D/chuyen-dong && npm install --no-fund --no-audit >/dev/null 2>&1 && node xem-truoc.mjs ${=ARGS} >/dev/null )
  for f in $D/kiem-tra/chuyen-dong/*.png; do n=${${f:t:r}%@*}; t=${${f:t:r}#*@}
    ffmpeg -v error -y -ss $t -i $D/tu-lieu/video-goc.mp4 -i $f -filter_complex "[0:v][1:v]overlay,scale=$SC" -frames:v 1 -q:v 6 "$OUT/$n-$o.jpg"; done
  echo "✓ $o: $(ls $D/kiem-tra/chuyen-dong | wc -l | tr -d ' ') ảnh → $OUT"
done
# phụ đề từ khoá to: chỉ ở phụ đề dọc ngắn (video dọc ≤ 90 s, không cảnh nào đè)
if [ -z "${1:-}" ] || [[ phu-de == *${1}* ]]; then
  D=$T/doc/chuyen-dong; sed -i.bak 's/duration: [0-9]*/duration: 60/' $D/src/du-an.js; sed -i.bak 's/^export const SCENES = .*/export const SCENES = [];/' $D/src/canh.js
  echo "export default [{start: 30, end: 34, text: 'bản nháp rẻ hơn khoảng 5 lần mà vẫn giữ chuyển động', hl: ['^5 lần', '+giữ']}];" > $D/src/phu-de.js
  ( cd $D && node xem-truoc.mjs phu-de@31.5 >/dev/null )
  ffmpeg -v error -y -ss 31.5 -i $T/doc/tu-lieu/video-goc.mp4 -i $T/doc/kiem-tra/chuyen-dong/phu-de@31.5.png -filter_complex "[0:v][1:v]overlay,scale=480:-1" -frames:v 1 -q:v 6 "$OUT/phu-de-tu-khoa-to-doc.jpg"
  echo "✓ phụ đề từ khoá to"
fi
