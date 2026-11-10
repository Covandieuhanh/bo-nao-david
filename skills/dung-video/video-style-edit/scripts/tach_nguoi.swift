// TÁCH NGƯỜI KHỎI NỀN bằng Vision của macOS (không cần cài gì) — cho cảnh 'chusau' (chữ sau người, bóng người), khối 07, 10/11/2026.
//   tach_nguoi <video> <giây đầu> <giây cuối> <fps> <thư mục ra>
// Ra: <thư mục>/00000.png … mỗi khung một PNG trong suốt: điểm ảnh người giữ nguyên, nền trong suốt (mép làm mềm nhẹ).
// In ra số khung đã ghi.
import AVFoundation
import CoreImage
import Foundation
import Vision

let a = CommandLine.arguments
guard a.count >= 6, let t0 = Double(a[2]), let t1 = Double(a[3]), let fps = Double(a[4]) else {
  FileHandle.standardError.write("cách dùng: tach_nguoi <video> <đầu> <cuối> <fps> <thư mục ra>\n".data(using: .utf8)!); exit(2)
}
let out = URL(fileURLWithPath: a[5])
try FileManager.default.createDirectory(at: out, withIntermediateDirectories: true)
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
let ctx = CIContext()
let cs = CGColorSpace(name: CGColorSpace.sRGB)!
let req = VNGeneratePersonSegmentationRequest()
req.qualityLevel = .accurate
req.outputPixelFormat = kCVPixelFormatType_OneComponent8
let n = Int(((t1 - t0) * fps).rounded(.up))
var ok = 0
for i in 0..<n {
  let t = CMTime(seconds: t0 + Double(i) / fps, preferredTimescale: 600)
  guard let cg = try? gen.copyCGImage(at: t, actualTime: nil) else { break }
  let img = CIImage(cgImage: cg)
  try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
  var mask = CIImage(color: .clear).cropped(to: img.extent)
  if let pb = req.results?.first?.pixelBuffer {
    let m = CIImage(cvPixelBuffer: pb)
    mask = m.transformed(by: CGAffineTransform(scaleX: img.extent.width / m.extent.width, y: img.extent.height / m.extent.height))
      .clampedToExtent().applyingGaussianBlur(sigma: 1.2).cropped(to: img.extent)
  }
  let cut = img.applyingFilter("CIBlendWithMask", parameters: [
    kCIInputBackgroundImageKey: CIImage(color: .clear).cropped(to: img.extent), kCIInputMaskImageKey: mask])
  let f = out.appendingPathComponent(String(format: "%05d.png", i))
  try ctx.writePNGRepresentation(of: cut, to: f, format: .RGBA8, colorSpace: cs)
  ok += 1
}
print(ok)
