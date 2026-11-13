import SwiftUI
import AppKit
import Quartz
import UniformTypeIdentifiers

let docExts: Set<String> = ["doc","docx","pages","rtf","txt","md","odt",
  "xls","xlsx","csv","numbers","ods","ppt","pptx","pps","ppsx","key","odp","pdf","html","htm","epub","json","xml"]

func kind(_ ext: String) -> (String, Color) {
  switch ext {
  case "doc","docx","pages","rtf","odt","txt","md": return ("doc.text.fill", .blue)
  case "xls","xlsx","csv","numbers","ods": return ("tablecells.fill", .green)
  case "ppt","pptx","key","odp": return ("rectangle.on.rectangle.angled.fill", .orange)
  case "pdf": return ("doc.richtext.fill", .red)
  default: return ("doc.fill", .gray)
  }
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
      await MainActor.run { self.files = result; self.loading = false }
    }
  }

  func open(_ url: URL) {
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

  let groups: [(String, Set<String>)] = [
    ("Tất cả", docExts),
    ("Word", ["doc","docx","pages","rtf","odt","txt","md"]),
    ("Excel", ["xls","xlsx","csv","numbers","ods"]),
    ("Slide", ["ppt","pptx","key","odp"]),
    ("PDF", ["pdf"])]

  var shown: [FileItem] {
    let exts = groups.first { $0.0 == s.filter }?.1 ?? docExts
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
        List(shown, selection: $s.selected) { f in
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
          if slideExts.contains(u.pathExtension.lowercased()) {
            SlideViewer(m: s.slideModel(u)).id(u)
          } else {
            QLView(url: u)
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
        ToolbarItemGroup {
          Button { s.pickFile() } label: { Label("Chọn file", systemImage: "folder") }
          Button { s.scan() } label: { Label("Làm mới", systemImage: "arrow.clockwise") }
          if let u = s.selected, slideExts.contains(u.pathExtension.lowercased()) {
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
        CommandMenu("Trình chiếu") {
          Button("Trình chiếu từ slide đang xem") { Store.shared.startShow(fromStart: false) }
            .keyboardShortcut(.return, modifiers: .command)
          Button("Trình chiếu từ slide đầu") { Store.shared.startShow(fromStart: true) }
            .keyboardShortcut(.return, modifiers: [.command, .shift])
        }
      }
  }
}
