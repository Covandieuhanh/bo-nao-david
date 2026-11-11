// Sổ việc: tự đo mỗi việc Claude làm (thời gian Claude chạy, token) ở MỌI phiên trên máy,
// dự kiến theo trung bình việc cùng loại, bảng tổng quan có thanh tiến độ, /bao-cao.
// Không hỏi David gì: loại việc lấy từ skill được gọi, hoặc model nhỏ tự gán nhãn.
//
// Dữ liệu: ~/.claude/so-viec/phien/<sid>.json (mỗi phiên tự ghi sổ của mình, không đè nhau)
//          ~/.claude/so-viec/nhap/<sid>.json  (nhập ngược phiên cũ, scripts/nhap-lich-su.py)
import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register, TurnUsage } from 'claude-code'

import type { Account, BigView, Book, GroupRow, LiveRow, Tokens } from '../types'

type $T = EngineInterface

const PANE = 'so-viec'
const TITLE = 'Sổ việc'
const IDLE_CLOSE_MS = 60 * 60 * 1000 // im lặng quá 60 phút: việc cũ coi như xong
const LIVE_MS = 2 * 60 * 1000 // phiên đang chạy phải báo nhịp trong 2 phút
const MAX_JOBS = 3000
const MAX_TURNS = 8000

/** Làm video dưới 3 phút (chỉ chạm skill rồi thôi) không tính là một video. */
const MIN_VIDEO_MS = 3 * 60 * 1000
const VIDEO = new Set(['video-style-edit', 'podcast-style-edit', 'cat-highlight-video', 'dang-da-kenh', 'hoc-video-mau'])

// Skill nào tính là một việc, và tên loại việc của nó.
const SKILL_TYPES: Record<string, string> = {
  'video-style-edit': 'video-style-edit',
  'podcast-style-edit': 'podcast-style-edit',
  'cat-highlight-video': 'cat-highlight-video',
  'dang-da-kenh': 'dang-da-kenh',
  'hoc-video-mau': 'hoc-video-mau',
  'tai-ban': 'tai-ban',
  'plugin-authoring': 'lam-mod',
  'playwright-cli': 'dieu-khien-trinh-duyet',
  'scroll-craft': 'lam-trang-web',
}

// Nhãn cho lượt không gọi skill: model nhỏ chỉ chọn giữa các việc lớn (scripts/nhap-lich-su.py dùng cùng bộ này).
// Không có nhãn video: video chỉ tính khi skill video được gọi.
const LABELS = ['xay-bo-nao', 'bot-telegram', 'tro-chuyen'] as const
const LABEL_HINT =
  'Nhãn: xay-bo-nao = sửa skill, luật, ghi nhớ, bộ não, cấu hình Claude, làm mod hay plugin; ' +
  'bot-telegram = làm hay dùng bot Telegram; tro-chuyen = mọi việc còn lại (hỏi đáp, viết, nghiên cứu, lên kế hoạch). '

/** Bốn việc lớn. Mọi việc nhỏ (skill, nhãn) tự quy về một việc lớn bằng groupOf. */
const GROUPS = [
  { id: 'video', name: 'Làm video' },
  { id: 'telegram', name: 'Bot Telegram' },
  { id: 'bo-nao', name: 'Xây bộ não (skill, luật, mod)' },
  { id: 'tro-chuyen', name: 'Trò chuyện, hỏi đáp, viết, lên kế hoạch' },
] as const
type GroupId = (typeof GROUPS)[number]['id']
const groupName = (g: GroupId) => GROUPS.find(x => x.id === g)!.name

/** Việc nhỏ nào thuộc xây bộ não (gồm nhãn cũ trước khi gom). */
const BRAIN_TYPES = new Set(['xay-bo-nao', 'sua-bo-nao', 'lam-mod', 'tai-ban'])
/** Skill làm việc trên chính Claude: tính là xây bộ não. Skill chỉ là luật chung (hoi-chuyen-gia...) thì không đổi việc. */
const BRAIN_SKILLS = new Set(['tai-ban', 'plugin-authoring', 'skill-creator', 'update-config', 'consolidate-memory', 'keybindings-help', 'fewer-permission-prompts', 'init'])

/** Việc nhỏ → việc lớn. Việc mới chưa biết tự rơi vào trò chuyện. */
function groupOf(type: string | null | undefined, book?: { isTelegram?: boolean; title?: string }): GroupId | null {
  if (!type) return null
  if (VIDEO.has(type) || type.startsWith('video:')) return 'video'
  if (type === 'bot-telegram' || type.startsWith('telegram:') || book?.isTelegram || /telegram/i.test(book?.title ?? '')) return 'telegram'
  if (BRAIN_TYPES.has(type) || type.startsWith('bo-nao:')) return 'bo-nao'
  return 'tro-chuyen'
}

const view = atom({ plugin: 'so-viec', key: 'view' } as const, null, { shape: 'view-5' })

// ---------- số và chữ ----------

const zero = (): Tokens => ({ input: 0, output: 0, cacheRead: 0, cacheWrite: 0 })
const total = (t: Tokens) => t.input + t.output + t.cacheRead + t.cacheWrite
const sumUsage = (u: TurnUsage) =>
  u.input_tokens + u.output_tokens + u.cache_read_input_tokens + u.cache_creation_input_tokens

function add(t: Tokens, u: TurnUsage) {
  t.input += u.input_tokens
  t.output += u.output_tokens
  t.cacheRead += u.cache_read_input_tokens
  t.cacheWrite += u.cache_creation_input_tokens
}

const mins = (ms: number) => Math.max(0, Math.round(ms / 60000))
const hm = (ms: number) => {
  const m = mins(ms)
  return m >= 60 ? `${Math.floor(m / 60)} giờ ${String(m % 60).padStart(2, '0')} phút` : `${m} phút`
}
const kt = (n: number) =>
  n >= 1e6
    ? `${(n / 1e6).toFixed(1).replace('.', ',')} triệu token`
    : `${Math.round(n / 1000)} nghìn token`

/** Thanh tiến độ bằng chữ: chạy trên mọi giao diện. */
const bar = (frac: number, width: number) => {
  const f = Math.max(0, Math.min(width, Math.round(Math.min(frac, 1) * width)))
  return '█'.repeat(f) + '░'.repeat(width - f)
}
const pct = (frac: number) => `${Math.round(frac * 100)}%`

const dayStart = (ms: number) => {
  const d = new Date(ms)
  d.setHours(0, 0, 0, 0)
  return d.getTime()
}
const weekStart = (ms: number) => {
  const d = new Date(dayStart(ms))
  const back = (d.getDay() + 6) % 7 // tuần bắt đầu thứ Hai
  return d.getTime() - back * 86400000
}
const ddmm = (ms: number) => {
  const d = new Date(ms)
  return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}`
}

// ---------- sổ của từng phiên ----------

async function dataDir($: $T) {
  return `${(await $.env.get('HOME')) ?? '~'}/.claude/so-viec`
}

async function readBooks($: $T, dir: string): Promise<Book[]> {
  const out: Book[] = []
  for (const sub of ['phien', 'nhap']) {
    const path = `${dir}/${sub}`
    if (!(await $.fs.exists(path))) continue
    for (const f of await $.fs.list(path)) {
      if (f.kind !== 'file' || !f.name.endsWith('.json')) continue
      try {
        out.push(JSON.parse(await $.fs.read(`${path}/${f.name}`)) as Book)
      } catch {
        // file đang ghi dở hoặc hỏng: bỏ qua lần này
      }
    }
  }
  return out
}

/** Phiên đang chạy chưa nạp mod (mở trước khi cài): đọc đuôi lịch sử phiên đó đang ghi. */
type Foreign = { sid: string; title: string; start: number; tokens: number; type: string | null }

function promptOf(d: Record<string, unknown>): string | null {
  if (d.type !== 'user' || d.isMeta || d.isSidechain) return null
  const c = (d.message as { content?: unknown } | undefined)?.content
  let text = ''
  if (typeof c === 'string') text = c
  else if (Array.isArray(c)) {
    if (c.some(b => (b as { type?: string })?.type === 'tool_result')) return null
    text = c.map(b => ((b as { type?: string; text?: string }).type === 'text' ? ((b as { text?: string }).text ?? '') : '')).join(' ')
  } else return null
  text = text.trim()
  if (!text || /^<(local-command|command-stdout|task-notification|system-reminder)/.test(text)) return null
  return text
}

async function scanForeign($: $T, home: string, known: Set<string>, now: number): Promise<Foreign[]> {
  const root = `${home}/.claude/projects`
  const out: Foreign[] = []
  if (!(await $.fs.exists(root))) return out
  for (const p of await $.fs.list(root)) {
    if (p.kind !== 'dir') continue
    for (const f of await $.fs.list(`${root}/${p.name}`)) {
      if (f.kind !== 'file' || !f.name.endsWith('.jsonl') || now - f.mtimeMs > LIVE_MS) continue
      const sid = f.name.slice(0, -6)
      if (known.has(sid)) continue
      try {
        const r = await $.process.run(['tail', '-n', '800', `${root}/${p.name}/${f.name}`], { timeoutMs: 5000 })
        const rows: Record<string, unknown>[] = []
        for (const line of r.stdout.split('\n')) {
          try {
            rows.push(JSON.parse(line) as Record<string, unknown>)
          } catch {
            // dòng đầu bị cắt dở
          }
        }
        let at = -1
        for (let i = rows.length - 1; i >= 0; i--) if (promptOf(rows[i]!) !== null) { at = i; break }
        const from = at >= 0 ? at : 0
        const first = rows[from]
        const start = first && typeof first.timestamp === 'string' ? Date.parse(first.timestamp) : now
        let tokens = 0
        let type: string | null = null
        const cmd = at >= 0 ? /<command-name>\/?([\w:-]+)<\/command-name>/.exec(promptOf(rows[at]!) ?? '') : null
        if (cmd) type = SKILL_TYPES[cmd[1]!.split(':').pop()!] ?? null
        const seen = new Set<string>()
        for (const d of rows.slice(from)) {
          if (d.type !== 'assistant') continue
          const m = d.message as { id?: string; usage?: Record<string, number>; content?: unknown[] }
          if (m?.usage && m.id && !seen.has(m.id)) {
            seen.add(m.id)
            const u = m.usage
            tokens += (u.input_tokens ?? 0) + (u.output_tokens ?? 0) + (u.cache_read_input_tokens ?? 0) + (u.cache_creation_input_tokens ?? 0)
          }
          for (const b of m?.content ?? []) {
            const tb = b as { type?: string; name?: string; input?: { skill?: string } }
            if (tb.type === 'tool_use' && tb.name === 'Skill' && !type)
              type = SKILL_TYPES[String(tb.input?.skill ?? '').split(':').pop() ?? ''] ?? null
          }
        }
        // Lượt này chưa gọi skill: lấy skill gần nhất của phiên (thường là việc đang làm tiếp).
        for (let i = rows.length - 1; i >= 0 && !type; i--) {
          const d = rows[i]!
          if (d.type !== 'assistant') continue
          for (const b of (d.message as { content?: unknown[] })?.content ?? []) {
            const tb = b as { type?: string; name?: string; input?: { skill?: string } }
            if (tb.type === 'tool_use' && tb.name === 'Skill')
              type = SKILL_TYPES[String(tb.input?.skill ?? '').split(':').pop() ?? ''] ?? type
          }
        }
        let title = ''
        const tf =`${root}/${p.name}/${sid}/custom-title.json`
        if (await $.fs.exists(tf)) title = ((JSON.parse(await $.fs.read(tf)) as { customTitle?: string }).customTitle ?? '').slice(0, 40)
        out.push({ sid, title: title || sid.slice(0, 8), start, tokens, type })
      } catch {
        // không đọc được thì bỏ qua lần này
      }
    }
  }
  return out
}

function closeJob(book: Book) {
  if (book.open && book.open.turns > 0) book.jobs.push(book.open)
  book.jobs = book.jobs.slice(-MAX_JOBS)
  book.open = null
}

// ---------- video: gộp mọi skill video, một phiên = một video ----------

/** Loại việc tính là làm video. */
/** Giới hạn 7 ngày của tài khoản đang đăng nhập (như trang usage). */
type Week = { used: number; resetsAt: string } | null

/** Phút và token video của một phiên (gộp sổ mod ghi và sổ nhập ngược cùng phiên). */
function videoOf(list: Book[]) {
  let ms = 0
  let tokens = 0
  for (const b of list)
    for (const j of [...b.jobs, ...(b.open ? [b.open] : [])])
      if (VIDEO.has(j.type)) {
        ms += j.activeMs
        tokens += total(j.tokens)
      }
  return { ms, tokens }
}

/** Token tuần này của một tài khoản: mọi lượt của tài khoản đó từ đầu cửa sổ 7 ngày. Lượt cũ chưa ghi tài khoản: tính cho tài khoản đang dùng. */
function weekTokensOf(books: Book[], acct: string, current: string, from: number) {
  const mineAcct = (a: string | undefined) => (a ? a === acct : acct === current)
  return books.flatMap(b => b.turns).filter(t => t[0] >= from && mineAcct(t[3])).reduce((a, t) => a + t[2], 0)
}

function bigView(books: Book[], mine: string, now: number, accounts: Account[], current: string, foreign: Foreign[] = []): BigView {
  const runs = (b: Book) => b.running !== null && (b.sid === mine || now - b.updatedAt < LIVE_MS)
  const typeNow = (b: Book) => (b.runningType !== undefined ? b.runningType : (b.open?.type ?? null))
  // Việc lớn đang chạy của một khung: lượt này gọi skill / nối tiếp việc đang mở; chưa rõ thì theo việc đang mở.
  const groupNow = (b: Book) => groupOf(typeNow(b), b) ?? groupOf(b.open?.type, b)

  const known = accounts.filter(a => a.perPct)
  const meanPerPct = known.length ? known.reduce((a, x) => a + (x.perPct ?? 0), 0) / known.length : null
  const perPctOf = (acct: string | undefined) => accounts.find(a => a.id === (acct || current))?.perPct ?? meanPerPct
  const pctOf = (tok: number, acct: string | undefined) => {
    const per = perPctOf(acct)
    return per ? tok / per : null
  }
  const weekFrom = (acct: string | undefined) => {
    const a = accounts.find(x => x.id === (acct || current))
    return a ? Date.parse(a.resetsAt) - 7 * 86400000 : now - 7 * 86400000
  }

  const bySid = new Map<string, Book[]>()
  for (const b of books) bySid.set(b.sid, [...(bySid.get(b.sid) ?? []), b])
  const acctOf = (list: Book[]) => list.find(b => b.account)?.account
  const jobsOf = (b: Book) => [...b.jobs, ...(b.open ? [b.open] : [])]

  // Đang làm trên Claude: mọi khung đang chạy (cả khung mở trước khi cài mod).
  const live: LiveRow[] = books
    .filter(runs)
    .map(b => {
      const g = groupNow(b)
      const same = jobsOf(b).filter(j => g && groupOf(j.type, b) === g && b.open === j)
      const ms = same.reduce((a, j) => a + j.activeMs, 0) + (b.running !== null ? now - b.running : 0)
      return { sid: b.sid, title: b.title || b.sid.slice(0, 8), isMine: b.sid === mine, group: g ? groupName(g) : 'đang xác định việc', ms }
    })
    .concat(
      foreign.map(f => ({ sid: f.sid, title: f.title, isMine: false, isNoMod: true, group: f.type && VIDEO.has(f.type) ? groupName('video') : 'chưa rõ việc', ms: now - f.start })),
    )
    .sort((a, b) => Number(b.isMine) - Number(a.isMine))

  // Tổng hợp theo việc lớn: tuần này (theo tuần của tài khoản làm việc đó) và từ đầu.
  const sum = new Map<GroupId, { weekMs: number; weekPct: number; weekTok: number; allMs: number; allTok: number }>()
  for (const g of GROUPS) sum.set(g.id, { weekMs: 0, weekPct: 0, weekTok: 0, allMs: 0, allTok: 0 })
  for (const b of books)
    for (const j of jobsOf(b)) {
      const g = groupOf(j.type, b)
      if (!g) continue
      const x = sum.get(g)!
      const tok = total(j.tokens)
      x.allMs += j.activeMs
      x.allTok += tok
      if (j.lastAt >= weekFrom(b.account)) {
        x.weekMs += j.activeMs
        x.weekTok += tok
        x.weekPct += pctOf(tok, b.account) ?? 0
      }
    }
  const allTok = [...sum.values()].reduce((a, x) => a + x.allTok, 0) || 1
  const groups: GroupRow[] = GROUPS.map(g => {
    const x = sum.get(g.id)!
    return { id: g.id, name: g.name, weekMs: x.weekMs, weekPct: known.length ? x.weekPct : null, weekTokens: x.weekTok, allMs: x.allMs, allShare: (100 * x.allTok) / allTok }
  })

  // Riêng làm video: trung bình một video (một khung = một video, từ 3 phút).
  const isVideoNow = (b: Book) => runs(b) && groupNow(b) === 'video'
  const done = [...bySid.entries()]
    .filter(([, list]) => !list.some(isVideoNow) && !foreign.some(f => list[0]?.sid === f.sid))
    .map(([, list]) => ({ ...videoOf(list), pct: pctOf(videoOf(list).tokens, acctOf(list)) }))
    .filter(v => v.ms >= MIN_VIDEO_MS)
  const withPct = done.filter(v => v.pct !== null)
  const video = done.length
    ? {
        count: done.length,
        ms: done.reduce((a, v) => a + v.ms, 0) / done.length,
        pct: withPct.length ? withPct.reduce((a, v) => a + (v.pct ?? 0), 0) / withPct.length : null,
      }
    : null

  const weeks = accounts
    .map(a => ({ id: a.id, label: a.label, isCurrent: a.id === current, used: Date.parse(a.resetsAt) > now ? a.used : 0, resetsAt: a.resetsAt }))
    .sort((a, b) => Number(b.isCurrent) - Number(a.isCurrent))
  const allMs = books.flatMap(jobsOf).reduce((a, j) => a + j.activeMs, 0)
  const since = Math.min(now, ...books.map(b => b.trackedSince))
  return { at: now, live, weeks, groups, video, since, allMs }
}

const pctText = (p: number | null) => (p === null ? 'chưa rõ' : p < 1 ? `${p.toFixed(1).replace('.', ',')}%` : `${Math.round(p)}%`)
const dayText = (iso: string | number) => {
  const d = new Date(iso)
  return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}`
}

function report(v: BigView) {
  const L: string[] = ['## Sổ việc: tổng hợp theo việc lớn', '']
  L.push('**Đang làm trên Claude**')
  if (!v.live.length) L.push('- Không có khung nào đang chạy.')
  for (const l of v.live)
    L.push(`- ${l.title}${l.isMine ? ' (khung này)' : ''}${l.isNoMod ? ' (khung mở trước khi cài mod)' : ''}: ${l.group}, đã chạy ${hm(l.ms)}`)
  L.push('', '**Hạn mức tuần của từng tài khoản**')
  if (!v.weeks.length) L.push('- Chưa đọc được hạn mức tuần.')
  for (const w of v.weeks) L.push(`- ${w.label}${w.isCurrent ? ' (đang đăng nhập)' : ''}: đã dùng ${pctText(w.used)}, làm mới ngày ${dayText(w.resetsAt)}`)
  L.push('', '**Tuần này, mỗi việc lớn tốn bao nhiêu**')
  for (const g of v.groups) L.push(`- ${g.name}: ${pctText(g.weekPct)} hạn mức tuần, ${hm(g.weekMs)}`)
  if (v.video) L.push(`- Trung bình một video: ${hm(v.video.ms)}, tốn ${pctText(v.video.pct)} hạn mức tuần (tính từ ${v.video.count} video)`)
  L.push('', `**Từ ${dayText(v.since)} tới giờ** (tổng ${hm(v.allMs)} Claude làm)`)
  for (const g of v.groups) L.push(`- ${g.name}: ${pctText(g.allShare)} tổng token, ${hm(g.allMs)}`)
  L.push('', 'Phần trăm hạn mức tuần là ước tính từ số token, mỗi việc tính theo tài khoản đã làm việc đó.')
  return L.join('\n')
}

// ---------- sổ của phiên này (biến của module, nạp lại sau mỗi lần tải lại) ----------

let me: Book | null = null
let path = ''
let dir = ''

// Sổ của phiên này: nạp lại sau mỗi lần mod tải lại.
/** Tài khoản Claude đang đăng nhập (trong ~/.claude.json): 8 ký tự đầu mã tài khoản, tên là phần trước @ của email. Chỉ lưu trên máy. */
async function whoAmI($: $T): Promise<{ id: string; label: string }> {
  try {
    const home = (await $.env.get('HOME')) ?? ''
    const cfg = JSON.parse(await $.fs.read(`${home}/.claude.json`)) as { oauthAccount?: { accountUuid?: string; emailAddress?: string } }
    const id = (cfg.oauthAccount?.accountUuid ?? '').slice(0, 8)
    return { id, label: (cfg.oauthAccount?.emailAddress ?? '').split('@')[0] || `tài khoản ${id}` }
  } catch {
    return { id: '', label: 'tài khoản chưa rõ' }
  }
}
const accountOf = async ($: $T) => (await whoAmI($)).id

/** Sổ hạn mức của mọi tài khoản đã đăng nhập trên máy: ~/.claude/so-viec/tai-khoan/<mã>.json. */
async function readAccounts($: $T, base: string): Promise<Account[]> {
  const out: Account[] = []
  const d = `${base}/tai-khoan`
  if (!(await $.fs.exists(d))) return out
  for (const f of await $.fs.list(d)) {
    if (f.kind !== 'file' || !f.name.endsWith('.json')) continue
    try {
      out.push(JSON.parse(await $.fs.read(`${d}/${f.name}`)) as Account)
    } catch {
      // đang ghi dở: bỏ qua lần này
    }
  }
  return out
}

async function mine($: $T): Promise<Book> {
  if (me) return me
  dir = await dataDir($)
  const sid = await $.session.id()
  path = `${dir}/phien/${sid}.json`
  const now = await $.clock.now()
  if (await $.fs.exists(path)) {
    try {
      me = JSON.parse(await $.fs.read(path)) as Book
    } catch {
      me = null
    }
  }
  if (!me) {
    me = {
      v: 1, sid, title: '', cwd: await $.session.cwd(), trackedSince: now,
      updatedAt: now, running: null, runningType: null, open: null, jobs: [], turns: [],
    }
    // Bản 0.1 lưu trong kho của mod; phần trước lúc này do scripts/nhap-lich-su.py nhập ngược.
    for (const k of ['jobs', 'open', 'day']) await $.store.delete(k)
  }
  return me
}

async function save($: $T) {
  if (!me) return
  me.updatedAt = await $.clock.now()
  me.turns = me.turns.slice(-MAX_TURNS)
  // Tên khung chat app đặt (nếu có) thay cho câu nhắn đầu.
  const proj = me.cwd.replace(/[^A-Za-z0-9]/g, '-')
  const tfile = `${dir.replace(/\/so-viec$/, '')}/projects/${proj}/${me.sid}/custom-title.json`
  try {
    if (await $.fs.exists(tfile)) {
      const t = (JSON.parse(await $.fs.read(tfile)) as { customTitle?: string }).customTitle
      if (t) me.title = t.slice(0, 40)
    }
  } catch {
    // không có tên thì giữ câu nhắn đầu
  }
  await $.fs.write(path, JSON.stringify(me))
}

async function refresh($: $T) {
  const book = await mine($)
  const now = await $.clock.now()
  const books = await readBooks($, dir)
  const home = dir.replace(/\/\.claude\/so-viec$/, '')
  const foreign = await scanForeign($, home, new Set(books.map(b => b.sid)), now).catch(() => [])

  // Ghi sổ hạn mức của tài khoản đang đăng nhập.
  const who = await whoAmI($)
  const usage = await $.session.usage().catch(() => null)
  const seven = usage?.rateLimits.find(r => r.kind === 'seven_day')
  if (seven && who.id) {
    const resetsAt = seven.resetsAt ?? new Date(now + 7 * 86400000).toISOString()
    const from = Date.parse(resetsAt) - 7 * 86400000
    const live = books.filter(b => b.running !== null && (!b.account || b.account === who.id)).reduce((a, b) => a + (b.liveTokens ?? 0), 0)
    const tokens = weekTokensOf(books, who.id, who.id, from) + live + foreign.reduce((a, f) => a + f.tokens, 0)
    const acct: Account = { id: who.id, label: who.label, used: seven.percentUsed, resetsAt, perPct: seven.percentUsed >= 0.5 ? tokens / seven.percentUsed : null, at: now }
    await $.fs.write(`${dir}/tai-khoan/${who.id}.json`, JSON.stringify(acct))
  }
  const v = bigView(books, book.sid, now, await readAccounts($, dir), who.id, foreign)
  await update($, view, () => v)

  const w = v.weeks.find(x => x.isCurrent)
  const me1 = v.live.find(l => l.isMine)
  $.ui.status(`${me1 ? `${me1.group}, ${hm(me1.ms)}` : 'Sổ việc'}${w ? ` · hạn mức tuần đã dùng ${pctText(w.used)}` : ''}`)
}

// ---------- móc vào sự kiện ----------

export const register: Register = on => {
  let lastTurnStart: number | null = null
  const pending = new Map<string, string>()
  const skillOfTurn = new Map<string, string>()
  let currentTurn: string | null = null

  on('session.start', async ($, e, next) => {
    const book = await mine($)
    const now = await $.clock.now()
    if (book.open && now - book.open.lastAt > IDLE_CLOSE_MS) closeJob(book)
    book.running = null
    book.runningType = null
    await save($)
    await $.command.register({ name: 'bao-cao', description: 'Sổ việc: tổng hợp theo việc lớn (video, bot Telegram, xây bộ não, trò chuyện)' })
    await $.command.register({ name: 'so-viec', description: 'Mở bảng Sổ việc cạnh khung chat' })
    void $.ui.open({ id: PANE, title: TITLE })
    // Nhịp 15 giây: báo phiên này còn chạy, đọc lại sổ mọi phiên.
    $.clock.every(15000, () => {
      void (async () => {
        if (me?.running != null) await save($)
        await refresh($)
      })()
    })
    await refresh($)
    return next(e)
  })

  on('command.run', { command: 'bao-cao' }, async $ => {
    await refresh($)
    const o = await read($, view)
    return { text: o ? report(o) : 'Sổ việc chưa có dữ liệu.' }
  })
  on('command.run', { command: 'so-viec' }, async $ => {
    await $.ui.open({ id: PANE, title: TITLE })
    return { text: 'Đã mở bảng Sổ việc.' }
  })

  on('turn.start', async ($, e, next) => {
    if (e.agentId !== undefined) return next(e)
    const book = await mine($)
    const now = await $.clock.now()
    currentTurn = e.turnId
    lastTurnStart = now
    book.running = now

    const text = e.text.trim()
    const open = book.open
    const isFresh = open !== null && now - open.lastAt < IDLE_CLOSE_MS
    book.runningType = text === '' && isFresh ? open.type : null
    if (/plugin:telegram|telegram/i.test(text) || /telegram/i.test(book.title)) book.isTelegram = true
    if (text !== '') {
      if (!book.title) book.title = text.replace(/\s+/g, ' ').slice(0, 40)
      // Trả lời ngắn khi đang có việc ("ok", "làm đi"): vẫn là việc đó.
      const isFollowUp = isFresh && text.length < 40
      if (isFollowUp) book.runningType = open.type
      else {
        const hint = open ? `Việc đang làm: ${open.type}. ` : ''
        pending.set(
          e.turnId,
          `${LABEL_HINT}${hint}Tin nhắn mới của người dùng (chọn đúng nhãn của việc đang làm nếu đây là tiếp nối): ${text.slice(0, 2000)}`,
        )
      }
    }
    await save($)
    void refresh($)
    return next(e)
  })

  // Mỗi lần gọi model (cả trợ lý con): cộng token ngay, thanh token chạy theo trong lúc lượt dài.
  on('turn.step', async function* ($, e, next) {
    const result = yield* next(e)
    if (result.usage) {
      const book = await mine($)
      book.liveTokens = (book.liveTokens ?? 0) + sumUsage(result.usage)
      await save($)
    }
    return result
  })

  on('skill.prompt', async ($, e, next) => {
    // Skill biết trước, hoặc tự xếp skill mới: nằm trong bộ skill video → video; telegram → bot Telegram; skill làm trên chính Claude → xây bộ não.
    let type: string | undefined = SKILL_TYPES[e.skill]
    if (!type) {
      const name = e.skill.split(':').pop() ?? e.skill
      let real = ''
      try {
        if (e.path) real = (await $.fs.stat(e.path, { resolve: true })).realPath ?? ''
      } catch {
        // không đọc được đường dẫn thì xếp theo tên
      }
      if (real.includes('/dung-video/')) type = `video:${name}`
      else if (e.skill.startsWith('telegram:') || e.pluginName === 'telegram') type = `telegram:${name}`
      else if (BRAIN_SKILLS.has(name)) type = `bo-nao:${name}`
    }
    if (type && currentTurn) {
      skillOfTurn.set(currentTurn, type)
      // Báo ngay loại việc, để bảng đổi ngay cả khi lượt dài (render) còn đang chạy.
      const book = await mine($)
      book.runningType = type
      await save($)
      void refresh($)
    }
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    const usage: TurnUsage | undefined = e.usage
    const now = await $.clock.now()
    const book = await mine($)

    // Token của trợ lý con cộng vào việc đang mở; thời gian thì không (chạy song song).
    if (e.agentId !== undefined) {
      if (usage) book.liveTokens = Math.max(0, (book.liveTokens ?? 0) - sumUsage(usage))
      if (book.open && usage) {
        add(book.open.tokens, usage)
        const last = book.turns[book.turns.length - 1]
        if (last) last[2] += sumUsage(usage)
        await save($)
      }
      return result
    }

    // Lượt đã trả lời xong (next ở trên), giờ mới gán nhãn: không làm chậm câu trả lời.
    const skill = skillOfTurn.get(e.turnId)
    const ask = skill ? undefined : pending.get(e.turnId)
    const label = ask ? await $.model.classify(ask, LABELS).catch(() => undefined) : undefined
    pending.delete(e.turnId)
    skillOfTurn.delete(e.turnId)

    if (book.open && now - book.open.lastAt - e.durationMs > IDLE_CLOSE_MS) closeJob(book)
    const type = skill ?? label ?? book.open?.type ?? 'tro-chuyen'
    if (!book.open || book.open.type !== type) {
      closeJob(book)
      book.open = {
        id: e.turnId, type, startedAt: now - e.durationMs, lastAt: now,
        activeMs: 0, turns: 0, tokens: zero(),
      }
    }
    const job = book.open
    job.activeMs += e.durationMs
    job.turns += 1
    job.lastAt = now
    if (usage) add(job.tokens, usage)
    book.account = await accountOf($)
    book.turns.push([lastTurnStart ?? now - e.durationMs, now, usage ? sumUsage(usage) : 0, book.account])
    if (currentTurn === e.turnId) {
      currentTurn = null
      book.running = null
      book.runningType = null
      book.liveTokens = 0
    }
    await save($)

    await refresh($)
    return result
  })

  on('session.end', async ($, e, next) => {
    // Phiên đóng chưa chắc việc xong (có thể mở lại); 60 phút im lặng thì tự đóng.
    if (me) {
      me.running = null
      await save($)
    }
    return next(e)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const v = await read($, view)
    if (!v) return <Text dimColor>Đang tải…</Text>
    const w = Math.max(8, Math.min(20, (e.props.bodyColumns ?? 40) - 24))
    const maxWeek = Math.max(0.0001, ...v.groups.map(g => g.weekPct ?? g.weekMs))

    return (
      <Box flexDirection="column">
        <Text bold>Đang làm trên Claude</Text>
        {v.live.length === 0 && <Text dimColor>Không có khung nào đang chạy.</Text>}
        {v.live.map(l => (
          <Text key={l.sid}>
            {l.title}
            <Text dimColor>
              {l.isMine ? ' (khung này)' : ''}
              {l.isNoMod ? ' (mở trước khi cài mod)' : ''} · {l.group}, đã chạy {hm(l.ms)}
            </Text>
          </Text>
        ))}
        <Text> </Text>
        <Text bold>Hạn mức tuần</Text>
        {v.weeks.length === 0 && <Text dimColor>Chưa đọc được hạn mức tuần.</Text>}
        {v.weeks.map(x => (
          <Box flexDirection="column" key={x.id}>
            <Text>
              {x.label}
              <Text dimColor>
                {x.isCurrent ? ' (đang đăng nhập)' : ''} · làm mới ngày {dayText(x.resetsAt)}
              </Text>
            </Text>
            <Text color={x.used >= 80 ? 'warning' : undefined}>
              {bar(x.used / 100, w)} đã dùng {pctText(x.used)}
            </Text>
          </Box>
        ))}
        <Text> </Text>
        <Text bold>Tuần này, mỗi việc lớn tốn bao nhiêu</Text>
        {v.groups.map(g => (
          <Box flexDirection="column" key={g.id}>
            <Text>{g.name}</Text>
            <Text>
              {bar((g.weekPct ?? g.weekMs) / maxWeek, w)} {pctText(g.weekPct)} hạn mức · {hm(g.weekMs)}
            </Text>
            {g.id === 'video' && v.video && (
              <Text dimColor>
                Trung bình một video: {hm(v.video.ms)}, {pctText(v.video.pct)} hạn mức (từ {v.video.count} video)
              </Text>
            )}
          </Box>
        ))}
        <Text> </Text>
        <Text bold>Từ {dayText(v.since)} tới giờ</Text>
        {v.groups.map(g => (
          <Text key={g.id}>
            {bar(g.allShare / 100, w)} {pctText(g.allShare)} <Text dimColor>{g.name}</Text>
          </Text>
        ))}
        <Text dimColor>Phần trăm là phần trong tổng token. /bao-cao để in bản chữ.</Text>
      </Box>
    )
  })
}
