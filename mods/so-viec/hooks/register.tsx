// Sổ việc: tự đo mỗi việc Claude làm (thời gian Claude chạy, token) ở MỌI phiên trên máy,
// dự kiến theo trung bình việc cùng loại, bảng tổng quan có thanh tiến độ, /bao-cao.
// Không hỏi David gì: loại việc lấy từ skill được gọi, hoặc model nhỏ tự gán nhãn.
//
// Dữ liệu: ~/.claude/so-viec/phien/<sid>.json (mỗi phiên tự ghi sổ của mình, không đè nhau)
//          ~/.claude/so-viec/nhap/<sid>.json  (nhập ngược phiên cũ, scripts/nhap-lich-su.py)
import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register, TurnUsage } from 'claude-code'

import type { Avg, Book, Job, Live, Overview, Period, Tokens, Turn } from '../types'

type $T = EngineInterface

const PANE = 'so-viec'
const TITLE = 'Sổ việc'
const IDLE_CLOSE_MS = 60 * 60 * 1000 // im lặng quá 60 phút: việc cũ coi như xong
const BRAIN_GAP_MS = 15 * 60 * 1000 // khoảng nghỉ ≤15 phút giữa hai lượt vẫn tính là đang làm
const BRAIN_DAY_MS = 4 * 60 * 60 * 1000 // luật 4 tiếng việc trí óc mỗi ngày
const LIVE_MS = 2 * 60 * 1000 // phiên đang chạy phải báo nhịp trong 2 phút
const MIN_SAMPLES = 3 // đủ 3 lần cùng loại mới đưa dự kiến
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

const view = atom({ plugin: 'so-viec', key: 'view' } as const, null, { shape: 'view-2' })

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

function averages(jobs: Job[]): Avg[] {
  const by = new Map<string, Job[]>()
  for (const j of jobs) by.set(j.type, [...(by.get(j.type) ?? []), j])
  return [...by.entries()]
    .map(([type, list]) => ({
      type,
      count: list.length,
      activeMs: list.reduce((a, j) => a + j.activeMs, 0) / list.length,
      tokens: list.reduce((a, j) => a + total(j.tokens), 0) / list.length,
    }))
    .sort((a, b) => b.count - a.count)
}

/** Giờ làm việc trí óc trong [from, to): gộp lượt của mọi phiên, nối khoảng nghỉ ≤15 phút. */
function brainMs(turns: Turn[], from: number, to: number) {
  const spans = turns
    .filter(t => t[1] > from && t[0] < to)
    .map(t => [Math.max(t[0], from), Math.min(t[1], to)] as [number, number])
    .sort((a, b) => a[0] - b[0])
  let ms = 0
  let cur: [number, number] | null = null
  for (const s of spans) {
    if (cur && s[0] - cur[1] <= BRAIN_GAP_MS) cur[1] = Math.max(cur[1], s[1])
    else {
      if (cur) ms += cur[1] - cur[0]
      cur = [s[0], s[1]]
    }
  }
  if (cur) ms += cur[1] - cur[0]
  return ms
}

function period(turns: Turn[], jobs: Job[], from: number, to: number): Period {
  return {
    ms: brainMs(turns, from, to),
    tokens: turns.filter(t => t[0] >= from && t[0] < to).reduce((a, t) => a + t[2], 0),
    jobs: jobs.filter(j => j.lastAt >= from && j.lastAt < to).length,
  }
}

function overview(books: Book[], mine: string, now: number, foreign: Foreign[] = []): Overview {
  const closed = books.flatMap(b => b.jobs)
  const avgs = averages(closed)
  const avgOf = (type: string) => avgs.find(a => a.type === type && a.count >= MIN_SAMPLES) ?? null
  // Lượt đang chạy tính tới bây giờ, để giờ hôm nay chạy theo.
  // Phiên này biết chắc mình đang chạy; phiên khác phải báo nhịp trong 2 phút.
  const runs = (b: Book) => b.running !== null && (b.sid === mine || now - b.updatedAt < LIVE_MS)
  const turns = books.flatMap(b => (runs(b) ? [...b.turns, [b.running ?? now, now, 0] as Turn] : b.turns))
  const withOpen = [...closed, ...books.flatMap(b => (b.open ? [b.open] : []))]

  // Chưa đủ lần cùng loại: so với trung bình mọi việc, để vẫn có thanh.
  const overall: Avg | null =
    closed.length >= MIN_SAMPLES
      ? {
          type: 'chung',
          count: closed.length,
          activeMs: closed.reduce((a, j) => a + j.activeMs, 0) / closed.length,
          tokens: closed.reduce((a, j) => a + total(j.tokens), 0) / closed.length,
        }
      : null

  const live: Live[] = books
    .filter(b => b.sid === mine || runs(b))
    .map((b): Live => {
      const isRun = runs(b)
      const run = isRun ? now - (b.running ?? now) : 0
      // Đang chạy: loại việc của lượt này (skill vừa gọi, hoặc tiếp nối việc đang mở).
      const type =
        isRun && b.runningType !== undefined ? b.runningType : (b.open?.type ?? null)
      const isSame = !isRun || (type !== null && type === b.open?.type)
      const own = type ? avgOf(type) : null
      return {
        sid: b.sid,
        title: b.title || b.sid.slice(0, 8),
        isMine: b.sid === mine,
        isRunning: isRun,
        type: type ?? (isRun ? 'đang xác định loại việc' : null),
        ms: (isSame ? (b.open?.activeMs ?? 0) : 0) + run,
        tokens: (isSame && b.open ? total(b.open.tokens) : 0) + (isRun ? (b.liveTokens ?? 0) : 0),
        avg: own ?? overall,
        basis: own ? 'loai' : overall ? 'chung' : null,
      }
    })
    .concat(
      foreign.map((f): Live => {
        const own = f.type ? avgOf(f.type) : null
        return {
          sid: f.sid, title: f.title, isMine: false, isRunning: true, isNoMod: true,
          type: f.type ?? 'chưa rõ loại việc', ms: now - f.start, tokens: f.tokens,
          avg: own ?? overall, basis: own ? 'loai' : overall ? 'chung' : null,
        }
      }),
    )
    .sort((a, b) => Number(b.isMine) - Number(a.isMine))

  const allTurns = books.flatMap(b => b.turns)
  return {
    at: now,
    live,
    today: period(turns, withOpen, dayStart(now), now + 1),
    week: period(turns, withOpen, weekStart(now), now + 1),
    total: {
      ms: brainMs(turns, 0, now + 1),
      tokens: allTurns.reduce((a, t) => a + t[2], 0),
      jobs: closed.length,
      sessions: books.length,
      since: Math.min(now, ...allTurns.map(t => t[0])),
    },
    avgs,
    recent: [...closed].sort((a, b) => b.lastAt - a.lastAt).slice(0, 10),
  }
}

// ---------- báo cáo ----------

function report(o: Overview) {
  const max = Math.max(1, ...o.avgs.map(a => a.tokens))
  const rows = o.avgs.map(
    a =>
      `| ${a.type} | ${a.count} | ${hm(a.activeMs)} | ${kt(a.tokens)} | \`${bar(a.tokens / max, 12)}\` |`,
  )
  const live = o.live
    .filter(l => l.type)
    .map(l => {
      const t = l.avg ? ` (${pct(l.ms / l.avg.activeMs)} dự kiến)` : ''
      return `- ${l.isMine ? '**Khung này**' : l.title}: ${l.type} · ${hm(l.ms)}${t} · ${kt(l.tokens)} token`
    })
  return [
    '## Sổ việc: tổng quan mọi phiên Claude Code trên máy',
    '',
    live.length ? '**Đang làm**\n' + live.join('\n') + '\n' : '',
    `**Hôm nay:** ${hm(o.today.ms)}/4h \`${bar(o.today.ms / BRAIN_DAY_MS, 16)}\` ${pct(o.today.ms / BRAIN_DAY_MS)} · ${kt(o.today.tokens)} token · ${o.today.jobs} việc`,
    `**Tuần này:** ${hm(o.week.ms)} · ${kt(o.week.tokens)} token · ${o.week.jobs} việc`,
    `**Từ ${ddmm(o.total.since)}:** ${o.total.sessions} phiên · ${o.total.jobs} việc xong · ${hm(o.total.ms)} · ${kt(o.total.tokens)} token`,
    '',
    '| Loại việc | Số lần | Thời gian TB | Token TB | So token |',
    '|---|---|---|---|---|',
    ...rows,
    '',
    `Dự kiến chỉ đưa khi loại việc có từ ${MIN_SAMPLES} lần. Thời gian = lúc Claude thật sự làm; giờ trong ngày gộp mọi phiên, nối khoảng nghỉ ≤15 phút.`,
  ].join('\n')
}

// ---------- sổ của phiên này (biến của module, nạp lại sau mỗi lần tải lại) ----------

let me: Book | null = null
let path = ''
let dir = ''

// Sổ của phiên này: nạp lại sau mỗi lần mod tải lại.
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
  const o = overview(books, book.sid, now, foreign)
  await update($, view, () => o)

  const brain = `hôm nay ${hm(o.today.ms)}/4h`
  const cur = o.live.find(l => l.isMine)
  if (!cur?.type) {
    $.ui.status(`Sổ việc · ${brain}`)
    return
  }
  const time = cur.avg ? `${mins(cur.ms)}/${mins(cur.avg.activeMs)}p` : `${mins(cur.ms)}p`
  const tok = cur.avg ? `${kt(cur.tokens)}/${kt(cur.avg.tokens)} token` : `${kt(cur.tokens)} token`
  $.ui.status(`${cur.type} · ${time} · ${tok} · ${brain}`)
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
    await $.command.register({ name: 'bao-cao', description: 'Sổ việc: tổng quan mọi phiên, trung bình theo loại việc' })
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
    book.turns.push([lastTurnStart ?? now - e.durationMs, now, usage ? sumUsage(usage) : 0])
    if (currentTurn === e.turnId) {
      currentTurn = null
      book.running = null
      book.runningType = null
      book.liveTokens = 0
    }
    await save($)

    const before = view ? await read($, view) : null
    await refresh($)
    const after = await read($, view)
    if (before && after && before.today.ms < BRAIN_DAY_MS && after.today.ms >= BRAIN_DAY_MS)
      $.ui.toast('Sổ việc: hôm nay đã đủ 4 tiếng việc trí óc.')
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
    const o = await read($, view)
    if (!o) return <Text dimColor>Đang tải…</Text>
    const w = Math.max(8, Math.min(24, (e.props.bodyColumns ?? 40) - 16))
    const max = Math.max(1, ...o.avgs.map(a => a.tokens))
    const over = (f: number) => (f > 1 ? 'warning' : undefined)

    return (
      <Box flexDirection="column">
        <Text bold>Đang làm</Text>
        {o.live.every(l => !l.type) && <Text dimColor>Chưa có việc nào đang mở.</Text>}
        {o.live
          .filter(l => l.type)
          .map(l => (
            <Box flexDirection="column" key={l.sid}>
              <Text>
                {l.isMine ? '▶ Khung này' : `▷ ${l.title}`} · {l.type}
                {l.isNoMod ? <Text dimColor> (chưa có mod)</Text> : ''}
                {l.isRunning ? <Text dimColor> · đang chạy</Text> : ''}
              </Text>
              {l.avg ? (
                <Text color={over(l.ms / l.avg.activeMs)}>
                  {bar(l.ms / l.avg.activeMs, w)} {hm(l.ms)}/{hm(l.avg.activeMs)}
                </Text>
              ) : (
                <Text dimColor>{hm(l.ms)}</Text>
              )}
              {l.avg ? (
                <Text color={over(l.tokens / l.avg.tokens)}>
                  {bar(l.tokens / l.avg.tokens, w)} {kt(l.tokens)}/{kt(l.avg.tokens)}
                </Text>
              ) : (
                <Text dimColor>{kt(l.tokens)} token</Text>
              )}
              <Text dimColor>
                {l.basis === 'loai'
                  ? `so với TB ${l.avg?.count} lần cùng loại`
                  : l.basis === 'chung'
                    ? `chưa đủ ${MIN_SAMPLES} lần cùng loại: so với TB mọi việc`
                    : 'chưa có dữ liệu để so'}
                {l.isNoMod ? ' · đọc từ lịch sử phiên' : ''}
              </Text>
            </Box>
          ))}
        <Text> </Text>
        <Text bold>Hôm nay</Text>
        <Text color={over(o.today.ms / BRAIN_DAY_MS)}>
          {bar(o.today.ms / BRAIN_DAY_MS, w)} {hm(o.today.ms)}/4h
        </Text>
        <Text dimColor>
          {kt(o.today.tokens)} token · {o.today.jobs} việc
        </Text>
        <Text bold>Tuần này</Text>
        <Text dimColor>
          {hm(o.week.ms)} · {kt(o.week.tokens)} token · {o.week.jobs} việc
        </Text>
        <Text bold>Từ {ddmm(o.total.since)}</Text>
        <Text dimColor>
          {o.total.sessions} phiên · {o.total.jobs} việc · {hm(o.total.ms)} · {kt(o.total.tokens)} token
        </Text>
        <Text> </Text>
        <Text bold>Theo loại việc (token TB)</Text>
        {o.avgs.length === 0 && <Text dimColor>Chưa có việc nào xong.</Text>}
        {o.avgs.slice(0, 10).map(a => (
          <Box flexDirection="column" key={a.type}>
            <Text>
              {a.type} <Text dimColor>×{a.count} · {hm(a.activeMs)}</Text>
            </Text>
            <Text dimColor={a.count < MIN_SAMPLES}>
              {bar(a.tokens / max, w)} {kt(a.tokens)}
            </Text>
          </Box>
        ))}
        <Text> </Text>
        <Text bold>10 việc gần nhất</Text>
        {o.recent.map(j => (
          <Text dimColor>
            {ddmm(j.lastAt)} {j.type} · {hm(j.activeMs)} · {kt(total(j.tokens))}
          </Text>
        ))}
        <Text> </Text>
        <Text dimColor>/bao-cao: bản đầy đủ trong khung chat</Text>
      </Box>
    )
  })
}
