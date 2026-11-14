import SwiftUI
import AppKit
import WebKit
import CryptoKit

// Trình xem slide riêng: QLPreviewView chỉ hiện file trình chiếu kiểu xem nhanh, không chuyển slide được.
// Cách làm: qlmanage -p -o xuất bản xem HTML (mỗi slide một div.slide) → WKWebView + JS điều hướng.

let slideExts: Set<String> = ["ppt", "pptx", "pps", "ppsx", "pot", "potx", "key", "odp"]

@MainActor final class SlideModel: NSObject, ObservableObject, WKScriptMessageHandler {
  enum Status { case loading, ready, failed }
  let url: URL
  @Published var status: Status = .loading
  @Published var cur = 0
  @Published var n = 0
  var html: URL?
  var root: URL?
  weak var web: WKWebView?

  init(url: URL) { self.url = url; super.init(); build() }

  private func cacheDir() -> URL {
    let a = (try? url.resourceValues(forKeys: [.contentModificationDateKey, .fileSizeKey]))
    let key = "\(url.path)|\(a?.contentModificationDate?.timeIntervalSince1970 ?? 0)|\(a?.fileSize ?? 0)"
    let h = SHA256.hash(data: Data(key.utf8)).map { String(format: "%02x", $0) }.joined().prefix(20)
    return FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask)[0]
      .appendingPathComponent("MoTaiLieu/\(h)")
  }

  nonisolated private static func findHTML(_ dir: URL) -> URL? {
    guard let en = FileManager.default.enumerator(at: dir, includingPropertiesForKeys: nil) else { return nil }
    for case let u as URL in en where u.lastPathComponent == "Preview.html" { return u }
    return nil
  }

  func build() {
    let dir = cacheDir()
    if let h = Self.findHTML(dir) { html = h; root = dir; status = .ready; return }
    let src = url
    Task.detached {
      try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
      let p = Process()
      p.executableURL = URL(fileURLWithPath: "/usr/bin/qlmanage")
      p.arguments = ["-p", "-o", dir.path, src.path]
      p.standardOutput = FileHandle.nullDevice; p.standardError = FileHandle.nullDevice
      try? p.run()
      let deadline = Date().addingTimeInterval(90)
      while p.isRunning && Date() < deadline { try? await Task.sleep(nanoseconds: 200_000_000) }
      if p.isRunning { p.terminate() }
      let h = SlideModel.findHTML(dir)
      await MainActor.run {
        if let h { self.html = h; self.root = dir; self.status = .ready } else { self.status = .failed }
      }
    }
  }

  nonisolated func userContentController(_ c: WKUserContentController, didReceive m: WKScriptMessage) {
    guard let d = m.body as? [String: Any] else { return }
    let cur = d["cur"] as? Int ?? 0, n = d["n"] as? Int ?? 0, action = d["action"] as? String
    Task { @MainActor in
      if action == "show" { self.cur = cur; self.startShow() }
      else { self.cur = cur; if n > 0 { self.n = n } }
    }
  }

  func js(_ s: String) { web?.evaluateJavaScript(s, completionHandler: nil) }
  func next() { js("window.__nav&&__nav.next()") }
  func prev() { js("window.__nav&&__nav.prev()") }
  func first() { js("window.__nav&&__nav.go(0)") }
  func last() { js("window.__nav&&__nav.go(1e9)") }
  func startShow(fromStart: Bool = false) {
    guard status == .ready else { return }
    Slideshow.start(self, from: fromStart ? 0 : cur)
  }
  /// Trình chiếu xong: đưa bản xem cuộn về đúng slide đang chiếu
  func showEnded(at i: Int) { cur = i; js("window.__nav&&__nav.go(\(i))"); web?.window?.makeKeyAndOrderFront(nil) }
}

let navJS = #"""
(function(){
  const slides=[...document.querySelectorAll('div.slide')];
  const post=(o)=>{try{webkit.messageHandlers.nav.postMessage(o)}catch(e){}};
  const SHOW=!!window.__show;            // true: cửa sổ trình chiếu toàn màn hình
  if(!slides.length){post({cur:0,n:0});return;}
  const W=slides[0].offsetWidth||959, H=slides[0].offsetHeight||540;
  let cur=Math.max(0,Math.min(slides.length-1,window.__start||0)), black=false;
  const st=document.createElement('style'); document.head.appendChild(st);
  let hud=null, hudT=0, curT=0;
  if(SHOW){
    hud=document.createElement('div');
    hud.style.cssText='position:fixed;right:28px;bottom:22px;padding:8px 16px;border-radius:999px;background:rgba(0,0,0,.55);color:#fff;font:600 18px -apple-system,Arial;z-index:99;transition:opacity .4s;opacity:0;pointer-events:none';
    document.body.appendChild(hud);
  }
  function flash(){ if(!hud) return; hud.textContent=(cur+1)+' / '+slides.length; hud.style.opacity=1; clearTimeout(hudT); hudT=setTimeout(()=>hud.style.opacity=0,1500); }
  function layout(){
    const vw=innerWidth, vh=innerHeight;
    if(!SHOW){
      const z=Math.min((vw-56)/W, 3);
      st.textContent=`body{background:#2b2f36!important;margin:0;padding:24px 0 90px}
        div.slide{zoom:${z};margin:0 auto 22px!important;box-shadow:0 6px 24px rgba(0,0,0,.4)!important}`;
    } else {
      const z=Math.min(vw/W, vh/H);
      st.textContent=`html,body{height:100%;overflow:hidden}
        body{background:#000!important;margin:0;display:flex;align-items:center;justify-content:center}
        div.slide{zoom:${z};margin:0!important;box-shadow:none!important}`;
      slides.forEach((s,i)=>s.style.display=(i===cur&&!black?'':'none'));
    }
  }
  function report(){post({cur:cur,n:slides.length});}
  function go(i){
    const n=Math.max(0,Math.min(slides.length-1,i));
    if(SHOW && i>=slides.length && cur===slides.length-1){ post({action:'exit',cur:cur}); return; }  // qua slide cuối: kết thúc
    cur=n; black=false;
    if(SHOW){layout(); flash();} else {slides[cur].scrollIntoView({behavior:'smooth',block:'start'});}
    report();
  }
  function onScroll(){
    if(SHOW) return;
    const mid=innerHeight*0.35; let best=slides.length-1;
    for(let i=0;i<slides.length;i++){const r=slides[i].getBoundingClientRect(); if(r.bottom>mid){best=i;break;}}
    if(best!==cur){cur=best;report();}
  }
  addEventListener('resize',()=>{layout(); if(!SHOW) slides[cur].scrollIntoView({block:'start'});});
  addEventListener('scroll',onScroll,{passive:true});
  addEventListener('keydown',e=>{
    const k=e.key;
    if(SHOW){
      if(['ArrowRight','ArrowDown','PageDown',' ','Enter','n'].includes(k)){go(cur+1);}
      else if(['ArrowLeft','ArrowUp','PageUp','Backspace','p'].includes(k)){go(cur-1);}
      else if(k==='Home'){go(0);} else if(k==='End'){go(slides.length-1);}
      else if(k==='Escape'||k==='q'){post({action:'exit',cur:cur});}
      else if(k==='b'||k==='.'){black=!black;layout();}
      else if(/^[0-9]$/.test(k)){ window.__num=(window.__num||'')+k; clearTimeout(window.__numT); window.__numT=setTimeout(()=>{window.__num='';},1200); }
      else return;
      if(k==='Enter'&&window.__num){ go(parseInt(window.__num)-1); window.__num=''; }
      e.preventDefault(); return;
    }
    if(k==='ArrowRight'||k==='PageDown'){go(cur+1);e.preventDefault();}
    else if(k==='ArrowLeft'||k==='PageUp'){go(cur-1);e.preventDefault();}
    else if(k==='Home'){go(0);e.preventDefault();}
    else if(k==='End'){go(slides.length-1);e.preventDefault();}
    else if(k==='f'||k==='F5'||(k==='Enter'&&(e.metaKey))){post({action:'show',cur:cur});e.preventDefault();}
  });
  if(SHOW){
    addEventListener('click',e=>{ (e.clientX<innerWidth/3)?go(cur-1):go(cur+1); });
    addEventListener('contextmenu',e=>{e.preventDefault();go(cur-1);});
    addEventListener('mousemove',()=>{ document.body.style.cursor='default'; clearTimeout(curT); curT=setTimeout(()=>document.body.style.cursor='none',1500); });
    document.body.style.cursor='none';
  }
  window.__nav={go:go,next:()=>go(cur+1),prev:()=>go(cur-1)};
  layout(); if(!SHOW) slides[cur].scrollIntoView({block:'start'}); else flash(); report();
})();
"""#

struct SlideWeb: NSViewRepresentable {
  @ObservedObject var m: SlideModel
  func makeNSView(context: Context) -> WKWebView {
    let cfg = WKWebViewConfiguration()
    cfg.userContentController.add(m, name: "nav")
    cfg.userContentController.addUserScript(WKUserScript(source: navJS, injectionTime: .atDocumentEnd, forMainFrameOnly: true))
    let w = WKWebView(frame: .zero, configuration: cfg)
    m.web = w
    if let h = m.html, let r = m.root { w.loadFileURL(h, allowingReadAccessTo: r) }
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) { w.window?.makeFirstResponder(w) }
    return w
  }
  func updateNSView(_ w: WKWebView, context: Context) {}
  static func dismantleNSView(_ w: WKWebView, coordinator: ()) {
    w.configuration.userContentController.removeScriptMessageHandler(forName: "nav")
  }
}

struct SlideViewer: View {
  @ObservedObject var m: SlideModel
  var body: some View {
    switch m.status {
    case .loading:
      VStack(spacing: 12) { ProgressView(); Text("Đang chuẩn bị slide…").foregroundStyle(.secondary) }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    case .failed:
      QLView(url: m.url)  // không xuất được bản xem: quay về cách xem nhanh
    case .ready:
      ZStack(alignment: .bottom) {
        SlideWeb(m: m)
        bar.padding(.bottom, 14)
      }
    }
  }

  var bar: some View {
    HStack(spacing: 6) {
      Button { m.first() } label: { Image(systemName: "backward.end.fill") }.help("Slide đầu (Home)")
      Button { m.prev() } label: { Image(systemName: "chevron.left") }.help("Slide trước (←)")
      Text(m.n > 0 ? "Slide \(m.cur + 1) / \(m.n)" : "…")
        .font(.system(.body, design: .rounded).monospacedDigit()).frame(minWidth: 110)
      Button { m.next() } label: { Image(systemName: "chevron.right") }.help("Slide sau (→)")
      Button { m.last() } label: { Image(systemName: "forward.end.fill") }.help("Slide cuối (End)")
      Divider().frame(height: 18)
      Button { m.startShow() } label: {
        Label("Trình chiếu", systemImage: "play.fill").font(.body.weight(.semibold))
      }.help("Trình chiếu toàn màn hình từ slide này (⌘↩ hoặc F). Esc để thoát")
      Button { m.startShow(fromStart: true) } label: { Image(systemName: "play.rectangle") }
        .help("Trình chiếu từ slide đầu (⇧⌘↩)")
    }
    .buttonStyle(.borderless)
    .padding(.horizontal, 14).padding(.vertical, 8)
    .background(.regularMaterial, in: Capsule())
    .shadow(radius: 6, y: 2)
  }
}


// Cửa sổ trình chiếu: không viền, phủ kín màn hình, nền đen; Esc / qua slide cuối thì đóng.
final class ShowWindow: NSWindow {
  override var canBecomeKey: Bool { true }
  override var canBecomeMain: Bool { true }
}

@MainActor final class Slideshow: NSObject, WKScriptMessageHandler, NSWindowDelegate {
  static var current: Slideshow?
  let model: SlideModel
  let win: ShowWindow
  var cur: Int
  var prevOptions: NSApplication.PresentationOptions = []

  static func start(_ m: SlideModel, from i: Int) {
    current?.close()
    current = Slideshow(m, from: i)
  }

  init(_ m: SlideModel, from i: Int) {
    model = m; cur = i
    let screen = m.web?.window?.screen ?? NSScreen.main ?? NSScreen.screens[0]
    win = ShowWindow(contentRect: screen.frame, styleMask: [.borderless], backing: .buffered, defer: false, screen: screen)
    super.init()
    win.setFrame(screen.frame, display: true)
    win.backgroundColor = .black
    win.isReleasedWhenClosed = false
    win.level = .normal
    win.collectionBehavior = [.fullScreenAuxiliary, .canJoinAllSpaces]
    win.delegate = self
    let cfg = WKWebViewConfiguration()
    cfg.userContentController.add(self, name: "nav")
    cfg.userContentController.addUserScript(WKUserScript(source: "window.__show=true;window.__start=\(i);", injectionTime: .atDocumentStart, forMainFrameOnly: true))
    cfg.userContentController.addUserScript(WKUserScript(source: navJS, injectionTime: .atDocumentEnd, forMainFrameOnly: true))
    let w = WKWebView(frame: screen.frame, configuration: cfg)
    w.setValue(false, forKey: "drawsBackground")
    win.contentView = w
    if let h = m.html, let r = m.root { w.loadFileURL(h, allowingReadAccessTo: r) }
    prevOptions = NSApp.presentationOptions
    NSApp.presentationOptions = [.hideDock, .hideMenuBar]
    win.makeKeyAndOrderFront(nil)
    NSApp.activate(ignoringOtherApps: true)
    win.makeFirstResponder(w)
  }

  nonisolated func userContentController(_ c: WKUserContentController, didReceive msg: WKScriptMessage) {
    guard let d = msg.body as? [String: Any] else { return }
    let i = d["cur"] as? Int ?? 0, action = d["action"] as? String
    Task { @MainActor in
      self.cur = i
      if action == "exit" { self.close() }
    }
  }

  func close() {
    NSApp.presentationOptions = prevOptions
    (win.contentView as? WKWebView)?.configuration.userContentController.removeScriptMessageHandler(forName: "nav")
    win.orderOut(nil)
    model.showEnded(at: cur)
    if Slideshow.current === self { Slideshow.current = nil }
  }

  func windowDidResignKey(_ n: Notification) {}
}
