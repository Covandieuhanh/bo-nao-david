import SwiftUI
import AppKit
import Quartz
import UniformTypeIdentifiers

// Nhóm loại tệp: mỗi đuôi thuộc đúng một nhóm. "Tất cả" gồm mọi nhóm trừ "Khác".
struct FileGroup { let name: String; let exts: Set<String>; let icon: String; let color: Color; let inAll: Bool }

let fileGroups: [FileGroup] = [
  FileGroup(name: "Word", exts: ["doc","docx","pages","rtf","odt"], icon: "doc.text.fill", color: .blue, inAll: true),
  FileGroup(name: "Excel", exts: ["xls","xlsx","numbers","ods","csv"], icon: "tablecells.fill", color: .green, inAll: true),
  FileGroup(name: "Slide", exts: ["ppt","pptx","pps","ppsx","key","odp"], icon: "rectangle.on.rectangle.angled.fill", color: .orange, inAll: true),
  FileGroup(name: "PDF", exts: ["pdf"], icon: "doc.richtext.fill", color: .red, inAll: true),
  FileGroup(name: "Ghi chú", exts: ["md","txt"], icon: "note.text", color: .purple, inAll: true),
  FileGroup(name: "Khác", exts: ["html","htm","epub","json","xml"], icon: "chevron.left.forwardslash.chevron.right", color: .gray, inAll: false),
]

let docExts: Set<String> = fileGroups.reduce(into: Set<String>()) { $0.formUnion($1.exts) }
let allExts: Set<String> = fileGroups.filter { $0.inAll }.reduce(into: Set<String>()) { $0.formUnion($1.exts) }

func kind(_ ext: String) -> (String, Color) {
  if let g = fileGroups.first(where: { $0.exts.contains(ext) }) { return (g.icon, g.color) }
  return ("doc.fill", .gray)
}

struct FileItem: Identifiable, Hashable {
  let url: URL; let date: Date
  var id: URL { url }
}

@MainActor final class Store: ObservableObject {
  static let shared = Store()
  @Published var files: [FileItem] = []
  @Published var selected: URL?
  @Published var loading = false
  @Published var filter = "Tất cả"
  @Published var q = ""
  // Mở thẳng vào một chế độ: open -a "Mở Tài Liệu" --args -cheDo "Bản in"
  @Published var mode: ViewMode = ViewMode(rawValue: UserDefaults.standard.string(forKey: "cheDo") ?? "") ?? .xem

  private var printModels: [URL: PrintModel] = [:]
  func printModel(_ u: URL) -> PrintModel {
    if let m = printModels[u] { return m }
    let m = PrintModel(url: u); printModels[u] = m; return m
  }
  private var editModels: [URL: EditModel] = [:]
  func editModel(_ u: URL) -> EditModel? {
    if let m = editModels[u] { return m }
    guard let m = EditModel(url: u) else { return nil }
    editModels[u] = m; return m
  }
  func didSave(_ u: URL) { printModels[u] = nil; slideModels[u] = nil }
  func saveCurrent() { if let u = selected { editModels[u]?.save() } }

  // Đang sửa dở mà rời tệp / đổi chế độ / thoát app: hỏi lưu.
  func canLeave() -> Bool {
    guard let u = selected, let m = editModels[u], m.dirty else { return true }
    let a = NSAlert()
    a.messageText = "Lưu thay đổi của \(u.lastPathComponent)?"
    a.addButton(withTitle: "Lưu"); a.addButton(withTitle: "Không lưu"); a.addButton(withTitle: "Huỷ")
    switch a.runModal() {
    case .alertFirstButtonReturn: return m.save()
    case .alertSecondButtonReturn: editModels[u] = nil; return true
    default: return false
    }
  }

  func scan() {
    loading = true
    let home = FileManager.default.homeDirectoryForCurrentUser
    let roots = ["Desktop","Documents","Downloads"].map { home.appendingPathComponent($0) }
    Task.detached {
      var out: [FileItem] = []
      let keys: [URLResourceKey] = [.contentModificationDateKey, .isRegularFileKey]
      for r in roots {
        guard let en = FileManager.default.enumerator(at: r, includingPropertiesForKeys: keys,
          options: [.skipsHiddenFiles, .skipsPackageDescendants]) else { continue }
        for case let u as URL in en {
          let p = u.path
          if p.contains("/node_modules/") || p.contains("/.git/") || p.contains("/Library/") { en.skipDescendants(); continue }
          guard docExts.contains(u.pathExtension.lowercased()) else { continue }
          let v = try? u.resourceValues(forKeys: Set(keys))
          if v?.isRegularFile == true { out.append(FileItem(url: u, date: v?.contentModificationDate ?? .distantPast)) }
          if out.count > 5000 { break }
        }
      }
      out.sort { $0.date > $1.date }; let result = out
      await MainActor.run {
        // Giữ các tệp mở từ ngoài (Open With, kéo thả) không nằm trong ba thư mục quét.
        let found = Set(result.map(\.url))
        let extra = self.files.filter { !found.contains($0.url) && !$0.url.path.hasPrefix(NSHomeDirectory() + "/Desktop") && !$0.url.path.hasPrefix(NSHomeDirectory() + "/Documents") && !$0.url.path.hasPrefix(NSHomeDirectory() + "/Downloads") }
        self.files = extra + result; self.loading = false
      }
    }
  }

  func open(_ url: URL) {
    guard canLeave() else { return }
    if !files.contains(where: { $0.url == url }) {
      files.insert(FileItem(url: url, date: Date()), at: 0)
    }
    selected = url
  }

  private var slideModels: [URL: SlideModel] = [:]
  func slideModel(_ u: URL) -> SlideModel {
    if let m = slideModels[u] { return m }
    let m = SlideModel(url: u); slideModels[u] = m; return m
  }

  func startShow(fromStart: Bool) {
    guard let u = selected, slideExts.contains(u.pathExtension.lowercased()) else { NSSound.beep(); return }
    slideModel(u).startShow(fromStart: fromStart)
  }

  func pickFile() {
    let p = NSOpenPanel()
    p.allowsMultipleSelection = false; p.canChooseDirectories = false
    if p.runModal() == .OK, let u = p.url { open(u) }
  }
}

struct QLView: NSViewRepresentable {
  let url: URL?
  func makeNSView(context: Context) -> QLPreviewView {
    let v = QLPreviewView(frame: .zero, style: .normal)!
    v.autostarts = true; return v
  }
  func updateNSView(_ v: QLPreviewView, context: Context) {
    if (v.previewItem as? URL) != url { v.previewItem = url as NSURL? }
  }
}

struct ContentView: View {
  @ObservedObject var s = Store.shared

  let groups: [(String, Set<String>)] = [("Tất cả", allExts)] + fileGroups.map { ($0.name, $0.exts) }

  var shown: [FileItem] {
    let exts = groups.first { $0.0 == s.filter }?.1 ?? allExts
    return s.files.filter { f in
      exts.contains(f.url.pathExtension.lowercased()) &&
      (s.q.isEmpty || f.url.lastPathComponent.localizedCaseInsensitiveContains(s.q))
    }
  }

  var body: some View {
    NavigationSplitView {
      VStack(spacing: 8) {
        Picker("", selection: $s.filter) {
          ForEach(groups, id: \.0) { Text($0.0).tag($0.0) }
        }.pickerStyle(.segmented).labelsHidden().padding(.horizontal, 8)
        List(shown, selection: Binding(get: { s.selected }, set: { n in if n != s.selected, s.canLeave() { s.selected = n } })) { f in
          let k = kind(f.url.pathExtension.lowercased())
          HStack {
            Image(systemName: k.0).foregroundStyle(k.1).frame(width: 20)
            VStack(alignment: .leading, spacing: 2) {
              Text(f.url.lastPathComponent).lineLimit(1)
              Text(f.url.deletingLastPathComponent().path.replacingOccurrences(of: NSHomeDirectory(), with: "~"))
                .font(.caption).foregroundStyle(.secondary).lineLimit(1).truncationMode(.middle)
            }
          }.tag(f.url)
        }
        .overlay { if s.loading { ProgressView("Đang tìm tài liệu…") } }
      }
      .searchable(text: $s.q, placement: .sidebar, prompt: "Tìm tên file")
      .navigationSplitViewColumnWidth(min: 260, ideal: 320)
    } detail: {
      Group {
        if let u = s.selected {
          switch s.mode {
          case .xem:
            if slideExts.contains(u.pathExtension.lowercased()) {
              SlideViewer(m: s.slideModel(u)).id(u)
            } else {
              QLView(url: u)
            }
          case .banIn:
            PrintViewer(m: s.printModel(u)).id(u)
          case .sua:
            if let em = s.editModel(u) { EditorView(m: em).id(u) } else { ExternalEditPanel(url: u).id(u) }
          }
        } else {
          VStack(spacing: 12) {
            Image(systemName: "doc.viewfinder").font(.system(size: 56)).foregroundStyle(.secondary)
            Text("Chọn file bên trái, hoặc kéo thả file vào đây").foregroundStyle(.secondary)
            Button("Chọn file…") { s.pickFile() }.controlSize(.large)
          }.frame(maxWidth: .infinity, maxHeight: .infinity)
        }
      }
      .toolbar {
        ToolbarItem(placement: .principal) {
          Picker("Chế độ", selection: Binding(get: { s.mode }, set: { n in if n != s.mode, s.canLeave() { s.mode = n } })) {
            ForEach(ViewMode.allCases, id: \.self) { Text($0.rawValue).tag($0) }
          }.pickerStyle(.segmented).labelsHidden().frame(width: 280)
          .help("Xem nhanh · Bản in (từng trang như khi in) · Sửa trực tiếp")
        }
        ToolbarItemGroup {
          Button { s.pickFile() } label: { Label("Chọn file", systemImage: "folder") }
          Button { s.scan() } label: { Label("Làm mới", systemImage: "arrow.clockwise") }
          if s.mode == .xem, let u = s.selected, slideExts.contains(u.pathExtension.lowercased()) {
            Button { s.startShow(fromStart: false) } label: { Label("Trình chiếu", systemImage: "play.fill") }
              .help("Trình chiếu toàn màn hình (⌘↩)")
          }
          if let u = s.selected {
            Button { NSWorkspace.shared.activateFileViewerSelecting([u]) } label: { Label("Hiện trong Finder", systemImage: "magnifyingglass") }
            Button { NSWorkspace.shared.open(u) } label: { Label("Mở bằng app gốc", systemImage: "arrow.up.forward.app") }
          }
        }
      }
      .navigationTitle(s.selected?.lastPathComponent ?? "Mở Tài Liệu")
    }
    .onDrop(of: [.fileURL], isTargeted: nil) { providers in
      for p in providers {
        _ = p.loadObject(ofClass: URL.self) { u, _ in
          if let u { Task { @MainActor in Store.shared.open(u) } }
        }
      }
      return true
    }
    .onAppear { if s.files.isEmpty { s.scan() } }
    .frame(minWidth: 900, minHeight: 600)
  }
}

final class AppDelegate: NSObject, NSApplicationDelegate {
  func application(_ app: NSApplication, open urls: [URL]) {
    if let u = urls.first { Task { @MainActor in Store.shared.open(u) } }
  }
  func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
    MainActor.assumeIsolated { Store.shared.canLeave() } ? .terminateNow : .terminateCancel
  }
  func applicationShouldTerminateAfterLastWindowClosed(_ s: NSApplication) -> Bool { true }
}

@main struct MoTaiLieuApp: App {
  @NSApplicationDelegateAdaptor(AppDelegate.self) var delegate
  var body: some Scene {
    WindowGroup { ContentView() }
      .commands {
        CommandGroup(replacing: .newItem) {
          Button("Mở file…") { Store.shared.pickFile() }.keyboardShortcut("o")
        }
        CommandGroup(replacing: .saveItem) {
          Button("Lưu") { Store.shared.saveCurrent() }.keyboardShortcut("s")
        }
        CommandMenu("Chế độ") {
          Button("Xem nhanh") { if Store.shared.canLeave() { Store.shared.mode = .xem } }.keyboardShortcut("1")
          Button("Bản in") { if Store.shared.canLeave() { Store.shared.mode = .banIn } }.keyboardShortcut("2")
          Button("Sửa") { if Store.shared.canLeave() { Store.shared.mode = .sua } }.keyboardShortcut("3")
        }
        CommandMenu("Trình chiếu") {
          Button("Trình chiếu từ slide đang xem") { Store.shared.startShow(fromStart: false) }
            .keyboardShortcut(.return, modifiers: .command)
          Button("Trình chiếu từ slide đầu") { Store.shared.startShow(fromStart: true) }
            .keyboardShortcut(.return, modifiers: [.command, .shift])
        }
      }
  }
}
