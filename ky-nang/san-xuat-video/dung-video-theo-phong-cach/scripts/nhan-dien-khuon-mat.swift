// Dò mặt bằng Vision của macOS (không cần cài gì): faces <thư mục khung .jpg> <file json ra>
// Mỗi khung: [{x, y, w, h (0–1, gốc trên-trái), m (độ mở miệng / chiều cao mặt)}]
// Thêm 28/11/2026: người ngồi nghiêng / quay đi không dò được mặt thì lấy dáng người (VNDetectHumanRectanglesRequest, nửa thân trên)
// và ước vùng đầu ở phần trên của dáng, ghi kèm "u": 1 (ước lượng, m = 0). Không có bước này thì hiệu ứng đặt đè lên đầu người đó.
import Foundation
import Vision

let args = CommandLine.arguments
let dir = URL(fileURLWithPath: args[1])
let files = try FileManager.default.contentsOfDirectory(at: dir, includingPropertiesForKeys: nil)
  .filter { $0.pathExtension == "jpg" }.sorted { $0.lastPathComponent < $1.lastPathComponent }
var out: [[[String: Double]]] = []
for f in files {
  let req = VNDetectFaceLandmarksRequest()
  let nguoi = VNDetectHumanRectanglesRequest()
  nguoi.upperBodyOnly = true
  try? VNImageRequestHandler(url: f, options: [:]).perform([req, nguoi])
  var faces: [[String: Double]] = []
  for o in req.results ?? [] {
    let b = o.boundingBox
    var m = 0.0
    if let lips = o.landmarks?.innerLips?.normalizedPoints, !lips.isEmpty {
      let ys = lips.map { Double($0.y) }
      m = (ys.max()! - ys.min()!)
    }
    faces.append(["x": Double(b.minX), "y": Double(1 - b.maxY), "w": Double(b.width), "h": Double(b.height), "m": m])
  }
  for o in nguoi.results ?? [] where o.confidence > 0.5 {
    let b = o.boundingBox
    let hw = Double(b.width) * 0.42, hh = Double(b.height) * 0.36
    let hx = Double(b.midX) - hw / 2, hy = Double(1 - b.maxY) + Double(b.height) * 0.04
    let trung = faces.contains { f in   // đã có mặt dò được nằm trong dáng này thì bỏ
      let cx = f["x"]! + f["w"]! / 2, cy = f["y"]! + f["h"]! / 2
      return cx > Double(b.minX) && cx < Double(b.maxX) && cy > Double(1 - b.maxY) && cy < Double(1 - b.minY)
    }
    if !trung { faces.append(["x": hx, "y": hy, "w": hw, "h": hh, "m": 0, "u": 1]) }
  }
  out.append(faces)
}
let data = try JSONSerialization.data(withJSONObject: out)
try data.write(to: URL(fileURLWithPath: args[2]))
print("\(files.count) khung")
