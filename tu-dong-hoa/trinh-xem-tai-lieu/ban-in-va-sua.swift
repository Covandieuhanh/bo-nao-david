import SwiftUI
import AppKit
import PDFKit
import CryptoKit

// Hai chế độ thêm cho app Mở Tài Liệu:
// - Bản in: LibreOffice chạy ngầm dàn tài liệu thành PDF đúng khổ giấy, hiện từng trang tách rời + số trang, bấm In.
// - Sửa: Word (docx, doc, rtf, odt) và Ghi chú (md, txt) sửa trong khung soạn chữ; csv sửa dạng bảng ô.
//   Lần lưu đầu giữ bản gốc cạnh file (<tên>.ban-goc.<đuôi>). Excel, Slide, PDF, Pages: nút "Sửa bằng LibreOffice".

enum ViewMode: String, CaseIterable { case xem = "Xem nhanh", banIn = "Bản in", sua = "Sửa" }

let loApp = URL(fileURLWithPath: "/Applications/LibreOffice.app")
let loBin = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
var hasLO: Bool { FileManager.default.isExecutableFile(atPath: loBin) }

let richExts: Set<String> = ["docx", "doc", "rtf", "odt"]
let plainExts: Set<String> = ["md", "txt"]
let csvExts: Set<String> = ["csv"]

func cacheDir(_ url: URL, _ sub: String) -> URL {
  let a = try? url.resourceValues(forKeys: [.contentModificationDateKey, .fileSizeKey])
  let key = "\(url.path)|\(a?.contentModificationDate?.timeIntervalSince1970 ?? 0)|\(a?.fileSize ?? 0)"
  let h = SHA256.hash(data: Data(key.utf8)).map { String(format: "%02x", $0) }.joined().prefix(20)
  return FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0]
    .appendingPathComponent("MoTaiLieu/\(sub)/\(h)")
}

// Chạy LibreOffice ngầm đổi định dạng; mỗi việc một hồ sơ riêng để hai lệnh chạy cùng lúc không khoá nhau.
nonisolated func runLO(_ input: URL, to filter: String, outDir: URL, profile: String) -> Bool {
  let fm = FileManager.default
  try? fm.createDirectory(at: outDir, withIntermediateDirectories: true)
  let prof = fm.urls(for: .cachesDirectory, in: .userDomainMask)[0].appendingPathComponent("MoTaiLieu/\(profile)")
  let p = Process()
  p.executableURL = URL(fileURLWithPath: loBin)
  p.arguments = ["-env:UserInstallation=\(prof.absoluteString)", "--headless", "--norestore",
                 "--convert-to", filter, "--outdir", outDir.path, input.path]
  p.standardOutput = FileHandle.nullDevice; p.standardError = FileHandle.nullDevice
  guard (try? p.run()) != nil else { return false }
  let deadline = Date().addingTimeInterval(120)
  while p.isRunning && Date() < deadline { usleep(100_000) }
  if p.isRunning { p.terminate(); return false }
  return p.terminationStatus == 0
}

// macOS gán viền xám mặc định cho ô bảng không khai viền (bảng chữ ký vô hình hiện viền): bỏ viền mặc định đó.
func boVienMacDinh(_ a: NSAttributedString) {
  let mac = NSColor(calibratedWhite: 0.75, alpha: 1)
  a.enumerateAttribute(.paragraphStyle, in: NSRange(location: 0, length: a.length)) { v, _, _ in
    for b in (v as? NSParagraphStyle)?.textBlocks ?? [] {
      for e in [NSRectEdge.minX, .maxX, .minY, .maxY]
      where b.width(for: .border, edge: e) == 1 && b.borderColor(for: e) == mac {
        b.setWidth(0, type: .absoluteValueType, for: .border, edge: e)
      }
    }
  }
}

// MARK: - Bản in

@MainActor final class PrintModel: ObservableObject {
  enum Status { case loading, ready, failed(String) }
  let url: URL
  @Published var status: Status = .loading
  @Published var page = 1
  @Published var pages = 0
  @Published var paper = ""
  var doc: PDFDocument?
  weak var view: PDFView?

  init(url: URL) { self.url = url; build() }

  private func use(_ d: PDFDocument) {
    doc = d; pages = d.pageCount; page = 1
    if let p = d.page(at: 0) {
      let b = p.bounds(for: .mediaBox)
      let w = Int((b.width / 72 * 25.4).rounded()), h = Int((b.height / 72 * 25.4).rounded())
      let ten = [(210, 297, "A4"), (148, 210, "A5"), (297, 420, "A3"), (216, 279, "Letter")]
        .first { (abs($0.0 - min(w, h)) <= 2 && abs($0.1 - max(w, h)) <= 2) }?.2
      paper = (ten.map { "\($0) " } ?? "") + (w > h ? "ngang" : "dọc") + " · \(w) × \(h) mm"
    }
    status = .ready
  }

  func build() {
    let ext = url.pathExtension.lowercased()
    if ext == "pdf" {
      if let d = PDFDocument(url: url) { use(d) } else { status = .failed("Không đọc được PDF này.") }
      return
    }
    guard hasLO else {
      status = .failed("Chưa có LibreOffice để dàn trang.\nCài bằng lệnh: brew install --cask libreoffice")
      return
    }
    let dir = cacheDir(url, "ban-in")
    let stem = url.deletingPathExtension().lastPathComponent
    let out = dir.appendingPathComponent(stem + ".pdf")
    if let d = PDFDocument(url: out) { use(d); return }
    let src = url
    Task.detached {
      let fm = FileManager.default
      try? fm.createDirectory(at: dir, withIntermediateDirectories: true)
      var input = src
      if ext == "md" {  // LibreOffice đọc Markdown như văn bản thường
        input = dir.appendingPathComponent(stem + ".txt")
        try? fm.removeItem(at: input); try? fm.copyItem(at: src, to: input)
      }
      let profile = fm.urls(for: .cachesDirectory, in: .userDomainMask)[0].appendingPathComponent("MoTaiLieu/lo-profile")
      let p = Process()
      p.executableURL = URL(fileURLWithPath: loBin)
      p.arguments = ["-env:UserInstallation=\(profile.absoluteString)", "--headless", "--norestore",
                     "--convert-to", "pdf", "--outdir", dir.path, input.path]
      p.standardOutput = FileHandle.nullDevice; p.standardError = FileHandle.nullDevice
      try? p.run()
      let deadline = Date().addingTimeInterval(180)
      while p.isRunning && Date() < deadline { try? await Task.sleep(nanoseconds: 200_000_000) }
      if p.isRunning { p.terminate() }
      let ok = fm.fileExists(atPath: out.path)
      await MainActor.run {
        if ok, let d = PDFDocument(url: out) { self.use(d) }
        else { self.status = .failed("LibreOffice không dàn trang được tệp này.") }
      }
    }
  }

  func zoom(_ f: CGFloat) { guard let v = view as? PageView else { return }; v.autoFit = false; v.scaleFactor *= f }
  func fit() { guard let v = view as? PageView else { return }; v.autoFit = true; v.needsLayout = true }
  func go(_ i: Int) { if let v = view, let d = doc, let p = d.page(at: max(0, min(i - 1, d.pageCount - 1))) { v.go(to: p) } }
  func printDoc() { view?.print(with: NSPrintInfo.shared, autoRotate: true) }
}

@MainActor final class PageWatcher: NSObject {
  let m: PrintModel
  init(_ m: PrintModel) { self.m = m }
  @objc func changed(_ n: Notification) {
    guard let v = n.object as? PDFView, let p = v.currentPage, let d = v.document else { return }
    m.page = d.index(for: p) + 1
  }
}

// Tự phóng vừa bề ngang khung (tối đa 115%), hai bên chừa nền xám để thấy rõ mép trang; bấm phóng tay thì thôi tự phóng.
final class PageView: PDFView {
  var autoFit = true
  override func layout() {
    super.layout()
    guard autoFit, let p = document?.page(at: 0) else { return }
    let w = p.bounds(for: .mediaBox).width
    let s = min(1.15, max(0.2, (bounds.width - 80) / w))
    if abs(scaleFactor - s) > 0.005 { scaleFactor = s }
  }
}

struct PDFPages: NSViewRepresentable {
  let m: PrintModel
  func makeCoordinator() -> PageWatcher { PageWatcher(m) }
  func makeNSView(context: Context) -> PDFView {
    let v = PageView()
    v.document = m.doc
    v.displayMode = .singlePageContinuous
    v.displaysPageBreaks = true
    v.pageBreakMargins = NSEdgeInsets(top: 14, left: 14, bottom: 14, right: 14)
    v.autoScales = false
    v.backgroundColor = NSColor(white: 0.32, alpha: 1)
    v.pageShadowsEnabled = true
    NotificationCenter.default.addObserver(context.coordinator, selector: #selector(PageWatcher.changed(_:)),
                                           name: .PDFViewPageChanged, object: v)
    m.view = v
    return v
  }
  func updateNSView(_ v: PDFView, context: Context) {}
}

struct PrintViewer: View {
  @ObservedObject var m: PrintModel
  var body: some View {
    switch m.status {
    case .loading:
      VStack(spacing: 12) { ProgressView(); Text("Đang dàn trang như khi in…").foregroundStyle(.secondary) }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    case .failed(let msg):
      VStack(spacing: 12) {
        Image(systemName: "printer.fill").font(.system(size: 44)).foregroundStyle(.secondary)
        Text(msg).multilineTextAlignment(.center).foregroundStyle(.secondary).textSelection(.enabled)
      }.frame(maxWidth: .infinity, maxHeight: .infinity)
    case .ready:
      ZStack(alignment: .bottom) {
        PDFPages(m: m)
        bar.padding(.bottom, 14)
      }
    }
  }
  var bar: some View {
    HStack(spacing: 8) {
      Button { m.go(m.page - 1) } label: { Image(systemName: "chevron.up") }.help("Trang trước")
      Text("Trang \(m.page) / \(m.pages)").font(.system(.body, design: .rounded).monospacedDigit()).frame(minWidth: 100)
      Button { m.go(m.page + 1) } label: { Image(systemName: "chevron.down") }.help("Trang sau")
      Divider().frame(height: 18)
      Text(m.paper).foregroundStyle(.secondary)
      Divider().frame(height: 18)
      Button { m.zoom(1 / 1.2) } label: { Image(systemName: "minus.magnifyingglass") }.help("Thu nhỏ")
      Button { m.fit() } label: { Image(systemName: "arrow.up.left.and.down.right.magnifyingglass") }.help("Vừa khung")
      Button { m.zoom(1.2) } label: { Image(systemName: "plus.magnifyingglass") }.help("Phóng to")
      Divider().frame(height: 18)
      Button { m.printDoc() } label: { Label("In…", systemImage: "printer.fill").font(.body.weight(.semibold)) }
        .help("In (⌘P)").keyboardShortcut("p")
    }
    .buttonStyle(.borderless)
    .padding(.horizontal, 14).padding(.vertical, 8)
    .background(.regularMaterial, in: Capsule())
    .shadow(radius: 6, y: 2)
  }
}

// MARK: - Sửa

@MainActor final class EditModel: NSObject, ObservableObject, NSTextViewDelegate {
  enum Kind { case rich, plain, csv }
  let url: URL
  let kind: Kind
  @Published var dirty = false
  @Published var note = ""
  @Published var rows: [[String]] = []
  @Published var ready = true
  var attr = NSAttributedString()
  var docAttrs: [NSAttributedString.DocumentAttributeKey: Any] = [:]
  var text = ""
  var sep: Character = ","
  weak var textView: NSTextView?

  init?(url: URL) {
    let e = url.pathExtension.lowercased()
    if richExts.contains(e) { kind = .rich } else if plainExts.contains(e) { kind = .plain }
    else if csvExts.contains(e) { kind = .csv } else { return nil }
    self.url = url
    super.init()
    load()
  }

  var backupURL: URL {
    url.deletingPathExtension().appendingPathExtension("ban-goc").appendingPathExtension(url.pathExtension)
  }

  static func readText(_ u: URL) -> String {
    (try? String(contentsOf: u, encoding: .utf8))
      ?? (try? String(contentsOf: u, encoding: .isoLatin1)) ?? ""
  }

  func load() {
    switch kind {
    case .rich:
      if viaLO {
        // docx/doc/odt: LibreOffice đổi sang RTF (giữ giãn dòng, lề, bảng) rồi mới đọc; macOS đọc thẳng docx hay mất giãn dòng.
        ready = false
        let src = url, dir = cacheDir(url, "sua")
        let rtf = dir.appendingPathComponent(url.deletingPathExtension().lastPathComponent + ".rtf")
        Task.detached {
          let ok = FileManager.default.fileExists(atPath: rtf.path) || runLO(src, to: "rtf", outDir: dir, profile: "lo-sua")
          await MainActor.run { self.read(ok ? rtf : src); self.ready = true }
        }
      } else { read(url) }
    case .plain:
      text = Self.readText(url)
    case .csv:
      let s = Self.readText(url)
      let first = s.prefix { $0 != "\n" && $0 != "\r\n" }
      sep = first.filter { $0 == ";" }.count > first.filter { $0 == "," }.count ? ";" : ","
      rows = parseCSV(s, sep)
      let w = max(1, rows.map(\.count).max() ?? 1)
      if rows.isEmpty { rows = [[""]] }
      rows = rows.map { $0 + Array(repeating: "", count: w - $0.count) }
    }
  }

  var viaLO: Bool { hasLO && ["docx", "doc", "odt"].contains(url.pathExtension.lowercased()) }

  func read(_ u: URL) {
    var da: NSDictionary?
    if let a = try? NSAttributedString(url: u, options: [:], documentAttributes: &da) { boVienMacDinh(a); attr = a }
    else { note = "Không đọc được tệp để sửa." }
    docAttrs = (da as? [NSAttributedString.DocumentAttributeKey: Any]) ?? [:]
  }

  // Khổ giấy để khung soạn chữ ngắt dòng gần giống bản in.
  var textWidth: CGFloat {
    let paper = (docAttrs[.paperSize] as? NSValue)?.sizeValue ?? NSSize(width: 595, height: 842)
    let l = (docAttrs[.leftMargin] as? CGFloat) ?? 72, r = (docAttrs[.rightMargin] as? CGFloat) ?? 72
    return max(300, paper.width - l - r)
  }

  func textDidChange(_ n: Notification) { if !dirty { dirty = true } }
  func changed() { if !dirty { dirty = true } }

  @discardableResult func save() -> Bool {
    let fm = FileManager.default
    do {
      if !fm.fileExists(atPath: backupURL.path) { try fm.copyItem(at: url, to: backupURL) }
      switch kind {
      case .rich:
        guard let ts = textView?.textStorage else { return false }
        if viaLO {
          // Ghi RTF rồi để LibreOffice đổi về đúng định dạng gốc, thay tệp gốc một lần.
          var a = docAttrs; a[.documentType] = NSAttributedString.DocumentType.rtf; a.removeValue(forKey: .readOnly)
          let tmp = fm.temporaryDirectory.appendingPathComponent("MoTaiLieu-luu-\(UUID().uuidString)")
          try fm.createDirectory(at: tmp, withIntermediateDirectories: true)
          defer { try? fm.removeItem(at: tmp) }
          let stem = url.deletingPathExtension().lastPathComponent, ext = url.pathExtension.lowercased()
          let rtf = tmp.appendingPathComponent(stem + ".rtf")
          try ts.data(from: NSRange(location: 0, length: ts.length), documentAttributes: a).write(to: rtf)
          let filter = ["docx": "docx:MS Word 2007 XML", "doc": "doc:MS Word 97", "odt": "odt"][ext]!
          let out = tmp.appendingPathComponent(stem + "." + ext)
          guard runLO(rtf, to: filter, outDir: tmp, profile: "lo-sua"), fm.fileExists(atPath: out.path) else {
            throw NSError(domain: "MoTaiLieu", code: 1, userInfo: [NSLocalizedDescriptionKey: "LibreOffice không ghi được tệp. Tệp gốc chưa bị đổi."])
          }
          _ = try fm.replaceItemAt(url, withItemAt: out)
          let cache = cacheDir(url, "sua"); try? fm.createDirectory(at: cache, withIntermediateDirectories: true)
          try? fm.copyItem(at: rtf, to: cache.appendingPathComponent(stem + ".rtf"))
          break
        }
        let types: [String: NSAttributedString.DocumentType] =
          ["docx": .officeOpenXML, "doc": .docFormat, "rtf": .rtf, "odt": .openDocument]
        var a = docAttrs
        a[.documentType] = types[url.pathExtension.lowercased()] ?? .officeOpenXML
        a.removeValue(forKey: .readOnly)
        let data = try ts.data(from: NSRange(location: 0, length: ts.length), documentAttributes: a)
        try data.write(to: url, options: .atomic)
      case .plain:
        try (textView?.string ?? text).write(to: url, atomically: true, encoding: .utf8)
      case .csv:
        try serializeCSV(rows, sep).write(to: url, atomically: true, encoding: .utf8)
      }
      dirty = false
      let f = DateFormatter(); f.dateFormat = "HH:mm"
      note = "Đã lưu \(f.string(from: Date())) · bản gốc: \(backupURL.lastPathComponent)"
      Store.shared.didSave(url)
      return true
    } catch {
      let a = NSAlert(); a.messageText = "Không lưu được"; a.informativeText = error.localizedDescription; a.runModal()
      return false
    }
  }

  // Định dạng chữ cho phần đang chọn (hoặc chữ sắp gõ khi không chọn gì).
  func apply(_ f: (NSFont) -> NSFont) {
    guard let tv = textView, let ts = tv.textStorage else { return }
    let r = tv.selectedRange()
    if r.length == 0 {
      let cur = (tv.typingAttributes[.font] as? NSFont) ?? NSFont.systemFont(ofSize: 12)
      tv.typingAttributes[.font] = f(cur); return
    }
    guard tv.shouldChangeText(in: r, replacementString: nil) else { return }
    ts.beginEditing()
    ts.enumerateAttribute(.font, in: r) { v, sub, _ in
      ts.addAttribute(.font, value: f((v as? NSFont) ?? NSFont.systemFont(ofSize: 12)), range: sub)
    }
    ts.endEditing(); tv.didChangeText()
  }

  func toggle(_ t: NSFontTraitMask) {
    guard let tv = textView else { return }
    let r = tv.selectedRange()
    let sample = (r.length > 0 ? tv.textStorage?.attribute(.font, at: r.location, effectiveRange: nil)
                               : tv.typingAttributes[.font]) as? NSFont
    let on = sample.map { NSFontManager.shared.traits(of: $0).contains(t) } ?? false
    apply { on ? NSFontManager.shared.convert($0, toNotHaveTrait: t) : NSFontManager.shared.convert($0, toHaveTrait: t) }
  }

  func size(_ d: CGFloat) { apply { NSFontManager.shared.convert($0, toSize: max(6, $0.pointSize + d)) } }
}

func parseCSV(_ s: String, _ sep: Character) -> [[String]] {
  var rows: [[String]] = [], row: [String] = [], f = "", q = false
  let c = Array(s); var i = 0
  while i < c.count {
    let ch = c[i]
    if q {
      if ch == "\"" { if i + 1 < c.count && c[i + 1] == "\"" { f.append("\""); i += 1 } else { q = false } }
      else { f.append(ch) }
    } else if ch == "\"" { q = true }
    else if ch == sep { row.append(f); f = "" }
    else if ch == "\n" || ch == "\r\n" || ch == "\r" { row.append(f); f = ""; rows.append(row); row = [] }
    else { f.append(ch) }
    i += 1
  }
  if !f.isEmpty || !row.isEmpty { row.append(f); rows.append(row) }
  return rows
}

func serializeCSV(_ rows: [[String]], _ sep: Character) -> String {
  rows.map { r in
    r.map { v in
      v.contains(sep) || v.contains("\"") || v.contains("\n") || v.contains("\r")
        ? "\"" + v.replacingOccurrences(of: "\"", with: "\"\"") + "\"" : v
    }.joined(separator: String(sep))
  }.joined(separator: "\n") + "\n"
}

// Khung soạn chữ: nền trắng, cột chữ rộng đúng phần in được của trang, có thước (căn lề, giãn dòng, danh sách).
final class PageTextView: NSTextView {
  var pageWidth: CGFloat = 451
  override func setFrameSize(_ s: NSSize) {
    super.setFrameSize(s)
    let side = max(24, (s.width - pageWidth) / 2)
    if abs(textContainerInset.width - side) > 0.5 { textContainerInset = NSSize(width: side, height: 36) }
  }
}

struct TextEditorView: NSViewRepresentable {
  let m: EditModel
  func makeNSView(context: Context) -> NSScrollView {
    let sv = NSTextView.scrollableTextView()
    let old = sv.documentView as! NSTextView
    let tv = PageTextView(frame: old.frame)
    tv.minSize = NSSize(width: 0, height: 0)
    tv.maxSize = NSSize(width: CGFloat.greatestFiniteMagnitude, height: CGFloat.greatestFiniteMagnitude)
    tv.isVerticallyResizable = true; tv.isHorizontallyResizable = false
    tv.autoresizingMask = [.width]
    tv.allowsUndo = true
    tv.isAutomaticQuoteSubstitutionEnabled = false
    tv.isAutomaticDashSubstitutionEnabled = false
    tv.isAutomaticSpellingCorrectionEnabled = false
    tv.drawsBackground = true; tv.backgroundColor = .white
    if m.kind == .rich {
      tv.isRichText = true; tv.importsGraphics = true
      tv.usesFontPanel = true; tv.usesRuler = true
      tv.pageWidth = m.textWidth
      tv.textContainer?.widthTracksTextView = false
      tv.textContainer?.containerSize = NSSize(width: m.textWidth, height: CGFloat.greatestFiniteMagnitude)
      tv.textStorage?.setAttributedString(m.attr)
      tv.textColor = nil
      sv.hasHorizontalRuler = true; sv.rulersVisible = true
      tv.isRulerVisible = true
    } else {
      tv.isRichText = false
      tv.pageWidth = 760
      tv.textContainer?.widthTracksTextView = false
      tv.textContainer?.containerSize = NSSize(width: 760, height: CGFloat.greatestFiniteMagnitude)
      tv.font = NSFont.systemFont(ofSize: 15)
      tv.textColor = .black
      tv.string = m.text
    }
    tv.insertionPointColor = .black
    tv.delegate = m
    sv.documentView = tv
    sv.backgroundColor = .white
    m.textView = tv
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) { tv.window?.makeFirstResponder(tv) }
    return sv
  }
  func updateNSView(_ v: NSScrollView, context: Context) {}
}

// Bảng ô cho csv.
@MainActor final class CSVTable: NSObject, NSTableViewDataSource, NSTableViewDelegate, NSTextFieldDelegate {
  let m: EditModel
  weak var table: NSTableView?
  init(_ m: EditModel) { self.m = m }
  static func colName(_ i: Int) -> String {
    var n = i, s = ""
    repeat { s = String(UnicodeScalar(65 + n % 26)!) + s; n = n / 26 - 1 } while n >= 0
    return s
  }
  func syncColumns() {
    guard let t = table else { return }
    let w = m.rows.first?.count ?? 1
    while t.tableColumns.count > w + 1 { t.removeTableColumn(t.tableColumns.last!) }
    while t.tableColumns.count < w + 1 {
      let i = t.tableColumns.count
      let c = NSTableColumn(identifier: .init(i == 0 ? "so" : "\(i - 1)"))
      c.title = i == 0 ? "" : Self.colName(i - 1)
      c.width = i == 0 ? 44 : 140
      t.addTableColumn(c)
    }
    t.reloadData()
  }
  func numberOfRows(in t: NSTableView) -> Int { m.rows.count }
  func tableView(_ t: NSTableView, viewFor col: NSTableColumn?, row: Int) -> NSView? {
    guard let id = col?.identifier.rawValue else { return nil }
    let f = NSTextField()
    f.isBordered = false; f.drawsBackground = false; f.lineBreakMode = .byTruncatingTail
    if id == "so" { f.stringValue = "\(row + 1)"; f.isEditable = false; f.textColor = .secondaryLabelColor; f.alignment = .right; return f }
    let c = Int(id) ?? 0
    f.stringValue = c < m.rows[row].count ? m.rows[row][c] : ""
    f.isEditable = true; f.tag = c; f.delegate = self
    return f
  }
  func controlTextDidEndEditing(_ n: Notification) {
    guard let f = n.object as? NSTextField, let t = table else { return }
    let r = t.row(for: f), c = f.tag
    guard r >= 0, r < m.rows.count, c < m.rows[r].count, m.rows[r][c] != f.stringValue else { return }
    m.rows[r][c] = f.stringValue; m.changed()
  }
}

struct CSVEditorView: NSViewRepresentable {
  @ObservedObject var m: EditModel
  func makeCoordinator() -> CSVTable { CSVTable(m) }
  func makeNSView(context: Context) -> NSScrollView {
    let t = NSTableView()
    t.usesAlternatingRowBackgroundColors = true
    t.gridStyleMask = [.solidVerticalGridLineMask, .solidHorizontalGridLineMask]
    t.columnAutoresizingStyle = .noColumnAutoresizing
    t.allowsColumnReordering = false
    t.dataSource = context.coordinator; t.delegate = context.coordinator
    context.coordinator.table = t
    context.coordinator.syncColumns()
    let sv = NSScrollView(); sv.documentView = t
    sv.hasVerticalScroller = true; sv.hasHorizontalScroller = true
    return sv
  }
  func updateNSView(_ v: NSScrollView, context: Context) { context.coordinator.syncColumns() }
}

struct EditorView: View {
  @ObservedObject var m: EditModel
  var body: some View {
    VStack(spacing: 0) {
      HStack(spacing: 10) {
        switch m.kind {
        case .rich:
          Group {
            Button { m.toggle(.boldFontMask) } label: { Image(systemName: "bold") }.help("Đậm (⌘B)")
            Button { m.toggle(.italicFontMask) } label: { Image(systemName: "italic") }.help("Nghiêng (⌘I)")
            Button { m.textView?.underline(nil) } label: { Image(systemName: "underline") }.help("Gạch chân (⌘U)")
            Divider().frame(height: 16)
            Button { m.size(-1) } label: { Image(systemName: "textformat.size.smaller") }.help("Chữ nhỏ hơn")
            Button { m.size(1) } label: { Image(systemName: "textformat.size.larger") }.help("Chữ to hơn")
            Button { m.textView?.window?.makeFirstResponder(m.textView); NSFontManager.shared.orderFrontFontPanel(nil) } label: { Image(systemName: "textformat") }.help("Phông chữ")
            Divider().frame(height: 16)
            Button { m.textView?.alignLeft(nil) } label: { Image(systemName: "text.alignleft") }.help("Căn trái")
            Button { m.textView?.alignCenter(nil) } label: { Image(systemName: "text.aligncenter") }.help("Căn giữa")
            Button { m.textView?.alignRight(nil) } label: { Image(systemName: "text.alignright") }.help("Căn phải")
            Button { m.textView?.alignJustified(nil) } label: { Image(systemName: "text.justify") }.help("Căn đều")
            Button { m.textView?.orderFrontListPanel(nil) } label: { Image(systemName: "list.bullet") }.help("Danh sách")
          }
        case .plain:
          Text("Sửa chữ thường").foregroundStyle(.secondary)
        case .csv:
          Button { let w = m.rows.first?.count ?? 1; m.rows.append(Array(repeating: "", count: w)); m.changed() } label: { Label("Thêm dòng", systemImage: "plus") }
          Button { m.rows = m.rows.map { $0 + [""] }; m.changed() } label: { Label("Thêm cột", systemImage: "plus.square.on.square") }
          Button { if m.rows.count > 1 { m.rows.removeLast(); m.changed() } } label: { Label("Xoá dòng cuối", systemImage: "minus") }
        }
        Spacer()
        Text(m.dirty ? "● Chưa lưu" : m.note).foregroundStyle(m.dirty ? .orange : .secondary).lineLimit(1)
        Button { m.save() } label: { Label("Lưu", systemImage: "square.and.arrow.down").font(.body.weight(.semibold)) }
          .disabled(!m.dirty).help("Lưu (⌘S)")
      }
      .buttonStyle(.borderless)
      .padding(.horizontal, 12).padding(.vertical, 7)
      .background(.bar)
      if m.kind == .rich {
        Text("Lưu qua LibreOffice giữ khổ giấy, lề, giãn dòng, bảng; đầu trang/chân trang và hình nổi có thể mất. Xem lại ở Bản in sau khi lưu. Bản gốc tự giữ ở \(m.backupURL.lastPathComponent).")
          .font(.caption).foregroundStyle(.secondary).padding(.horizontal, 12).padding(.vertical, 4)
          .frame(maxWidth: .infinity, alignment: .leading).background(.bar)
      }
      Divider()
      if !m.ready {
        VStack(spacing: 12) { ProgressView(); Text("Đang mở để sửa…").foregroundStyle(.secondary) }
          .frame(maxWidth: .infinity, maxHeight: .infinity)
      } else {
      switch m.kind {
      case .rich, .plain: TextEditorView(m: m)
      case .csv: CSVEditorView(m: m)
      }
      }
    }
  }
}

struct ExternalEditPanel: View {
  let url: URL
  var body: some View {
    VStack(spacing: 14) {
      Image(systemName: "pencil.and.outline").font(.system(size: 48)).foregroundStyle(.secondary)
      Text("Loại tệp này sửa bằng LibreOffice để giữ đúng công thức, bố cục, hình.")
        .foregroundStyle(.secondary).multilineTextAlignment(.center)
      if hasLO {
        Button {
          NSWorkspace.shared.open([url], withApplicationAt: loApp, configuration: NSWorkspace.OpenConfiguration())
        } label: { Label("Sửa bằng LibreOffice", systemImage: "square.and.pencil") }.controlSize(.large)
      } else {
        Text("Chưa có LibreOffice. Cài: brew install --cask libreoffice").font(.caption).textSelection(.enabled)
        Button { NSWorkspace.shared.open(url) } label: { Label("Mở bằng app gốc", systemImage: "arrow.up.forward.app") }
          .controlSize(.large)
      }
    }.frame(maxWidth: .infinity, maxHeight: .infinity).padding()
  }
}
