// Dò mặt bằng Vision của macOS (không cần cài gì): faces <thư mục khung .jpg> <file json ra>
// Mỗi khung: [{x, y, w, h (0–1, gốc trên-trái), m (độ mở miệng / chiều cao mặt)}]
import Foundation
import Vision

let args = CommandLine.arguments
let dir = URL(fileURLWithPath: args[1])
let files = try FileManager.default.contentsOfDirectory(at: dir, includingPropertiesForKeys: nil)
  .filter { $0.pathExtension == "jpg" }.sorted { $0.lastPathComponent < $1.lastPathComponent }
var out: [[[String: Double]]] = []
for f in files {
  let req = VNDetectFaceLandmarksRequest()
  try? VNImageRequestHandler(url: f, options: [:]).perform([req])
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
  out.append(faces)
}
let data = try JSONSerialization.data(withJSONObject: out)
try data.write(to: URL(fileURLWithPath: args[2]))
print("\(files.count) khung")
