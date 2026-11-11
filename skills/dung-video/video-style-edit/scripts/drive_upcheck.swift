import Foundation
// In: thư mục. Out: số file chưa tải lên xong + tên vài file.
let root = URL(fileURLWithPath: CommandLine.arguments[1])
var pending = 0, total = 0, sample: [String] = []
let keys: [URLResourceKey] = [.isRegularFileKey, .ubiquitousItemIsUploadedKey, .ubiquitousItemIsUploadingKey]
if let e = FileManager.default.enumerator(at: root, includingPropertiesForKeys: keys) {
  for case let u as URL in e {
    let v = try? u.resourceValues(forKeys: Set(keys))
    guard v?.isRegularFile == true else { continue }
    total += 1
    if v?.ubiquitousItemIsUploaded != true { pending += 1; if sample.count < 3 { sample.append(u.lastPathComponent) } }
  }
}
print("tong=\(total) chua_len=\(pending) \(sample)")
