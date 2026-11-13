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
  @Published var present = false
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
    let cur = d["cur"] as? Int ?? 0, n = d["n"] as? Int ?? 0, pres = d["present"] as? Bool ?? false
    Task { @MainActor in self.cur = cur; self.n = n; self.present = pres }
  }

  func js(_ s: String) { web?.evaluateJavaScript(s, completionHandler: nil) }
  func next() { js("window.__nav&&__nav.next()") }
  func prev() { js("window.__nav&&__nav.prev()") }
  func first() { js("window.__nav&&__nav.go(0)") }
  func last() { js("window.__nav&&__nav.go(1e9)") }
  func togglePresent() { js("window.__nav&&__nav.setPresent(\(!present))") }
}

let navJS = #"""
(function(){
  const slides=[...document.querySelectorAll('div.slide')];
  const post=(o)=>{try{webkit.messageHandlers.nav.postMessage(o)}catch(e){}};
  if(!slides.length){post({cur:0,n:0,present:false});return;}
  const W=slides[0].offsetWidth||959, H=slides[0].offsetHeight||540;
  let cur=0, present=false;
  const st=document.createElement('style'); document.head.appendChild(st);
  function layout(){
    const vw=innerWidth, vh=innerHeight;
    if(!present){
      const z=Math.min((vw-56)/W, 3);
      st.textContent=`body{background:#2b2f36!important;margin:0;padding:24px 0 90px}
        div.slide{zoom:${z};margin:0 auto 22px!important;box-shadow:0 6px 24px rgba(0,0,0,.4)!important}`;
      slides.forEach(s=>s.style.display='');
    } else {
      const z=Math.min((vw-24)/W,(vh-80)/H);
      st.textContent=`html,body{height:100%;overflow:hidden}
        body{background:#0b0d10!important;margin:0;display:flex;align-items:center;justify-content:center;padding-bottom:56px;box-sizing:border-box}
        div.slide{zoom:${z};margin:0!important;box-shadow:none!important}`;
      slides.forEach((s,i)=>s.style.display=(i===cur?'':'none'));
    }
  }
  function report(){post({cur:cur,n:slides.length,present:present});}
  function go(i){
    cur=Math.max(0,Math.min(slides.length-1,i));
    if(present){layout();} else {slides[cur].scrollIntoView({behavior:'smooth',block:'start'});}
    report();
  }
  function onScroll(){
    if(present) return;
    const mid=innerHeight*0.35; let best=slides.length-1;
    // slide đầu tiên còn chiếm phần trên màn hình
    for(let i=0;i<slides.length;i++){const r=slides[i].getBoundingClientRect(); if(r.bottom>mid){best=i;break;}}
    if(best!==cur){cur=best;report();}
  }
  function setPresent(v){present=!!v; layout(); if(!present) slides[cur].scrollIntoView({block:'start'}); report();}
  addEventListener('resize',()=>{layout(); if(!present) slides[cur].scrollIntoView({block:'start'});});
  addEventListener('scroll',onScroll,{passive:true});
  addEventListener('keydown',e=>{
    const k=e.key;
    if(k==='ArrowRight'||k==='PageDown'||(present&&(k==='ArrowDown'||k===' '||k==='Enter'))){go(cur+1);e.preventDefault();}
    else if(k==='ArrowLeft'||k==='PageUp'||(present&&k==='ArrowUp')){go(cur-1);e.preventDefault();}
    else if(k==='Home'){go(0);e.preventDefault();}
    else if(k==='End'){go(slides.length-1);e.preventDefault();}
    else if(k==='Escape'&&present){setPresent(false);}
    else if(k==='f'||k==='F5'){setPresent(!present);e.preventDefault();}
  });
  addEventListener('click',e=>{ if(present){ (e.clientX<innerWidth/3)?go(cur-1):go(cur+1); } });
  window.__nav={go:go,next:()=>go(cur+1),prev:()=>go(cur-1),setPresent:setPresent};
  layout(); report();
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
      Button { m.togglePresent() } label: {
        Label(m.present ? "Xem cuộn" : "Trình chiếu", systemImage: m.present ? "list.bullet.rectangle" : "play.rectangle.fill")
      }.help("Bật/tắt trình chiếu (phím F, Esc để thoát)")
      Button { NSApp.keyWindow?.toggleFullScreen(nil) } label: { Image(systemName: "arrow.up.left.and.arrow.down.right") }
        .help("Toàn màn hình")
    }
    .buttonStyle(.borderless)
    .padding(.horizontal, 14).padding(.vertical, 8)
    .background(.regularMaterial, in: Capsule())
    .shadow(radius: 6, y: 2)
  }
}
