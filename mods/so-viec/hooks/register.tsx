// Sổ việc: tự đo mỗi việc Claude làm (thời gian Claude chạy, token) ở MỌI phiên trên máy,
// dự kiến theo trung bình việc cùng loại, bảng tổng quan có thanh tiến độ, /bao-cao.
// Không hỏi David gì: loại việc lấy từ skill được gọi, hoặc model nhỏ tự gán nhãn.
//
// Dữ liệu: ~/.claude/so-viec/phien/<sid>.json (mỗi phiên tự ghi sổ của mình, không đè nhau)
//          ~/.claude/so-viec/nhap/<sid>.json  (nhập ngược phiên cũ, scripts/nhap-lich-su.py)
import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register, TurnUsage } from 'claude-code'

import type { Book, Tokens, VideoNow, VideoView } from '../types'

type $T = EngineInterface

const PANE = 'so-viec'
const TITLE = 'Sổ việc'
const IDLE_CLOSE_MS = 60 * 60 * 1000 // im lặng quá 60 phút: việc cũ coi như xong
const LIVE_MS = 2 * 60 * 1000 // phiên đang chạy phải báo nhịp trong 2 phút
const MAX_JOBS = 3000
const MAX_TURNS = 8000

// Skill nào tính là một việc, và tên loại việc của nó.
const SKILL_TYPES: Record<string, string> = {
  'video-style-edit': 'video-style-edit',
  'podcast-style-edit': 'podcast-style-edit',
  'cat-highlight-video': 'cat-highlight-video',
  'dang-da-kenh': 'dang-da-kenh',
  'hoc-video-mau': 'hoc-video-mau',
  'tai-ban': 'tai-ban',
  'playwright-cli': 'dieu-khien-trinh-duyet',
  'plugin-authoring': 'lam-mod',
  'scroll-craft': 'lam-trang-web',
}

// Nhãn cho việc không gọi skill (scripts/nhap-lich-su.py dùng cùng bộ này).
const LABELS = [
  'sua-bo-nao',
  'viet-bai',
  'nghien-cuu',
  'lap-ke-hoach',
  'lam-mod',
  'video-style-edit',
  'podcast-style-edit',
  'cat-highlight-video',
  'dang-da-kenh',
  'hoi-dap',
  'khac',
] as const

const view = atom({ plugin: 'so-viec', key: 'view' } as const, null, { shape: 'view-3' })

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
  return m >= 60 ? `${Math.floor(m / 60)}h${String(m % 60).padStart(2, '0')}` : `${m}p`
}
const kt = (n: number) =>
  n >= 1e9 ? `${(n / 1e9).toFixed(1)}B` : n >= 1e6 ? `${(n / 1e6).toFixed(1)}M` : `${Math.round(n / 1000)}k`

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
const VIDEO = new Set(['video-style-edit', 'podcast-style-edit', 'cat-highlight-video', 'dang-da-kenh', 'hoc-video-mau'])

/** Giới hạn 7 ngày của tài khoản (như trang usage). */
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

function videoView(books: Book[], mine: string, now: number, week: Week, foreign: Foreign[] = [], account = ''): VideoView {
  const runs = (b: Book) => b.running !== null && (b.sid === mine || now - b.updatedAt < LIVE_MS)
  const typeNow = (b: Book) => (b.runningType !== undefined ? b.runningType : (b.open?.type ?? null))
  const isVideoNow = (b: Book) => runs(b) && VIDEO.has(typeNow(b) ?? '')

  // Gộp theo phiên.
  const bySid = new Map<string, Book[]>()
  for (const b of books) bySid.set(b.sid, [...(bySid.get(b.sid) ?? []), b])

  // Tuần: tổng token mọi phiên từ đầu cửa sổ 7 ngày, chia % đã dùng = token cho 1%.
  const from = week ? Date.parse(week.resetsAt) - 7 * 86400000 : now - 7 * 86400000
  // Chỉ token của tài khoản đang đăng nhập (% tuần là của tài khoản này). Lượt cũ chưa ghi tài khoản: coi là tài khoản này.
  const same = (a: string | undefined) => !account || !a || a === account
  const liveTok =
    books.filter(b => runs(b) && same(b.account)).reduce((a, b) => a + (b.liveTokens ?? 0), 0) +
    foreign.reduce((a, f) => a + f.tokens, 0)
  const weekTokens =
    books.flatMap(b => b.turns).filter(t => t[0] >= from && same(t[3])).reduce((a, t) => a + t[2], 0) + liveTok
  const perPct = week && week.used >= 0.5 ? weekTokens / week.used : null
  const pct = (tok: number) => (perPct ? tok / perPct : null)

  // Video đã xong: mỗi phiên có việc video và không còn đang làm video.
  const done = [...bySid.entries()]
    .filter(([, list]) => !list.some(isVideoNow) && !foreign.some(f => list[0]?.sid === f.sid))
    .map(([, list]) => videoOf(list))
    .filter(v => v.ms > 0)
  const avg = done.length
    ? {
        count: done.length,
        ms: done.reduce((a, v) => a + v.ms, 0) / done.length,
        tokens: done.reduce((a, v) => a + v.tokens, 0) / done.length,
        pct: pct(done.reduce((a, v) => a + v.tokens, 0) / done.length),
      }
    : null

  // Video đang làm: phiên nào đang chạy việc video (cả phiên chưa có mod).
  const live: VideoNow[] = [...bySid.entries()]
    .filter(([sid, list]) => list.some(isVideoNow) || (sid === mine && videoOf(list).ms > 0))
    .map(([sid, list]) => {
      const v = videoOf(list)
      const b = list.find(isVideoNow)
      const run = b && b.running !== null ? now - b.running : 0
      const tokens = v.tokens + (b?.liveTokens ?? 0)
      return { sid, title: list.find(x => x.title)?.title ?? sid.slice(0, 8), isMine: sid === mine, isRunning: !!b, ms: v.ms + run, tokens, pct: pct(tokens) }
    })
    .concat(
      foreign
        .filter(f => f.type && VIDEO.has(f.type))
        .map(f => ({ sid: f.sid, title: f.title, isMine: false, isRunning: true, isNoMod: true, ms: now - f.start, tokens: f.tokens, pct: pct(f.tokens) })),
    )
    .sort((a, b) => Number(b.isMine) - Number(a.isMine))

  const left = week && avg?.pct ? Math.max(0, Math.floor((100 - week.used) / avg.pct)) : null
  return { at: now, live, week: week ? { used: week.used, resetsAt: week.resetsAt } : null, weekTokens, avg, left }
}

const pctText = (p: number | null) => (p === null ? '?' : p < 1 ? `${p.toFixed(1)}%` : `${Math.round(p)}%`)

function report(v: VideoView) {
  const lines = ['## Sổ việc: video', '']
  for (const l of v.live)
    lines.push(`- **${l.isMine ? 'Khung này' : l.title}**${l.isNoMod ? ' (chưa có mod)' : ''}: ${hm(l.ms)} · ${pctText(l.pct)} tuần${v.avg ? ` (TB ${hm(v.avg.ms)} · ${pctText(v.avg.pct)})` : ''}`)
  if (v.live.length) lines.push('')
  lines.push(v.week ? `**Tuần này:** ${pctText(v.week.used)} đã dùng${v.left !== null ? ` · còn đủ ~${v.left} video` : ''}` : `**Tuần này:** ${kt(v.weekTokens)} token`)
  lines.push(v.avg ? `**TB 1 video:** ${hm(v.avg.ms)} · ${pctText(v.avg.pct)} token tuần (từ ${v.avg.count} video)` : '**TB 1 video:** chưa có video nào xong.')
  lines.push('', 'Một video = mọi việc video trong một phiên (dựng, cắt highlight, đăng). % tuần là ước tính từ token.')
  return lines.join('\n')
}

// ---------- sổ của phiên này (biến của module, nạp lại sau mỗi lần tải lại) ----------

let me: Book | null = null
let path = ''
let dir = ''

// Sổ của phiên này: nạp lại sau mỗi lần mod tải lại.
/** Tài khoản Claude đang đăng nhập: 8 ký tự đầu mã tài khoản trong ~/.claude.json (không lưu email). */
async function accountOf($: $T): Promise<string> {
  try {
    const home = (await $.env.get('HOME')) ?? ''
    const cfg = JSON.parse(await $.fs.read(`${home}/.claude.json`)) as { oauthAccount?: { accountUuid?: string } }
    return (cfg.oauthAccount?.accountUuid ?? '').slice(0, 8)
  } catch {
    return ''
  }
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
  const usage = await $.session.usage().catch(() => null)
  const seven = usage?.rateLimits.find(r => r.kind === 'seven_day')
  const week: Week = seven ? { used: seven.percentUsed, resetsAt: seven.resetsAt ?? new Date(now + 7 * 86400000).toISOString() } : null
  const v = videoView(books, book.sid, now, week, foreign, await accountOf($))
  await update($, view, () => v)

  const wk = v.week ? `tuần ${pctText(v.week.used)}` : ''
  const cur = v.live.find(l => l.isMine)
  if (!cur) {
    $.ui.status(`Sổ việc · ${wk}`)
    return
  }
  const t = v.avg ? `${mins(cur.ms)}/${mins(v.avg.ms)}p` : `${mins(cur.ms)}p`
  const p = v.avg ? `${pctText(cur.pct)}/${pctText(v.avg.pct)}` : pctText(cur.pct)
  $.ui.status(`Video ${t} · ${p} tuần · ${wk}`)
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
    await $.command.register({ name: 'bao-cao', description: 'Sổ việc: video đang làm, % tuần, trung bình 1 video' })
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
    if (text !== '') {
      if (!book.title) book.title = text.replace(/\s+/g, ' ').slice(0, 40)
      // Trả lời ngắn khi đang có việc ("ok", "làm đi"): vẫn là việc đó.
      const isFollowUp = isFresh && text.length < 40
      if (isFollowUp) book.runningType = open.type
      else {
        const hint = open ? `Việc đang làm: ${open.type}. ` : ''
        pending.set(
          e.turnId,
          `${hint}Tin nhắn mới của người dùng (chọn đúng nhãn của việc đang làm nếu đây là tiếp nối): ${text.slice(0, 2000)}`,
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
    const type = SKILL_TYPES[e.skill]
    if (type && currentTurn) {
      skillOfTurn.set(currentTurn, type)
      // Báo ngay loại việc, để bảng có thanh khi lượt dài (render) còn đang chạy.
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
    const type = skill ?? label ?? book.open?.type ?? 'khac'
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
    const w = Math.max(8, Math.min(24, (e.props.bodyColumns ?? 40) - 18))
    const over = (f: number) => (f > 1 ? 'warning' : undefined)

    return (
      <Box flexDirection="column">
        {v.live.map(l => (
          <Box flexDirection="column" key={l.sid}>
            <Text bold>
              🎬 {l.isMine ? 'Video đang làm' : l.title}
              {l.isNoMod ? <Text dimColor> (chưa có mod)</Text> : ''}
            </Text>
            <Text color={v.avg ? over(l.ms / v.avg.ms) : undefined}>
              {bar(v.avg ? l.ms / v.avg.ms : 0, w)} {hm(l.ms)}
              {v.avg ? ` / TB ${hm(v.avg.ms)}` : ''}
            </Text>
            <Text color={v.avg?.pct && l.pct !== null ? over(l.pct / v.avg.pct) : undefined}>
              {bar(v.avg?.pct && l.pct !== null ? l.pct / v.avg.pct : 0, w)} {pctText(l.pct)}
              {v.avg ? ` / TB ${pctText(v.avg.pct)}` : ''} tuần
            </Text>
            <Text> </Text>
          </Box>
        ))}
        <Text bold>Tuần này</Text>
        {v.week ? (
          <Text color={v.week.used >= 80 ? 'warning' : undefined}>
            {bar(v.week.used / 100, w)} {pctText(v.week.used)} đã dùng
          </Text>
        ) : (
          <Text dimColor>{kt(v.weekTokens)} token</Text>
        )}
        {v.left !== null && <Text dimColor>còn đủ ~{v.left} video</Text>}
        <Text> </Text>
        <Text bold>TB 1 video</Text>
        {v.avg ? (
          <Text>
            {hm(v.avg.ms)} · {pctText(v.avg.pct)} token tuần <Text dimColor>(từ {v.avg.count} video)</Text>
          </Text>
        ) : (
          <Text dimColor>Chưa có video nào xong.</Text>
        )}
      </Box>
    )
  })
}
