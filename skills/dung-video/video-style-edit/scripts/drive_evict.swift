import Foundation
// Giải phóng bản cache trên Mac của file Drive đã lên mây (file vẫn còn trên Drive).
var ok = 0, fail = 0
for arg in CommandLine.arguments.dropFirst() {
  let e = FileManager.default.enumerator(at: URL(fileURLWithPath: arg), includingPropertiesForKeys: [.isRegularFileKey, .ubiquitousItemIsUploadedKey])
  while let u = e?.nextObject() as? URL {
    let v = try? u.resourceValues(forKeys: [.isRegularFileKey, .ubiquitousItemIsUploadedKey])
    guard v?.isRegularFile == true, v?.ubiquitousItemIsUploaded == true else { continue }
    do { try FileManager.default.evictUbiquitousItem(at: u); ok += 1 } catch { fail += 1 }
  }
}
print("giai_phong=\(ok) loi=\(fail)")
