"""Ai nói lúc nào bằng pyannote (speaker-diarization-3.1) — chạy bằng ~/.venvs/pyannote/bin/python.
diarize.py <file tiếng> <ra.json> [số người: 0 = tự đếm]
Ra: {"count": n, "turns": [{"start", "end", "spk"}]} — spk đánh số theo thứ tự xuất hiện (người nói đầu = 0).
speakers.py gọi script này trước; lỗi (thiếu venv, thiếu mô hình) thì speakers.py quay về cách đoán theo giọng cũ."""
import json, os, sys, warnings
warnings.filterwarnings("ignore")
os.environ.setdefault("HF_HUB_OFFLINE", "1")          # mô hình đã tải sẵn ở ~/.cache/torch/pyannote — không cần mạng
import torch
# torch ≥ 2.6 chỉ nạp các lớp được cho phép; mô hình pyannote 3.x lưu kèm vài lớp siêu dữ liệu → cho phép đúng các lớp đó
from torch.torch_version import TorchVersion
from pyannote.audio.core.task import Specifications, Problem, Resolution
torch.serialization.add_safe_globals([TorchVersion, Specifications, Problem, Resolution])
from pyannote.audio import Pipeline

src, out = sys.argv[1], sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 0
pipe = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")
if pipe is None:
    sys.exit("không nạp được pyannote/speaker-diarization-3.1")
if torch.backends.mps.is_available():
    pipe.to(torch.device("mps"))
ann = pipe(src, **({"num_speakers": n} if n > 0 else {}))
order, turns = [], []
for seg, _, lab in ann.itertracks(yield_label=True):
    if lab not in order: order.append(lab)
    turns.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "spk": order.index(lab)})
json.dump({"count": len(order), "turns": turns}, open(out, "w"))
print(f"pyannote: {len(order)} người · {len(turns)} lượt")
