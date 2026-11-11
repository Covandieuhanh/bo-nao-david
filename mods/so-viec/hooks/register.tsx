// Sổ việc: tự đo mỗi việc Claude làm (thời gian Claude chạy, token),
// dự kiến theo trung bình các việc cùng loại, báo cáo bằng /bao-cao.
// Không hỏi David gì: loại việc lấy từ skill được gọi, hoặc model nhỏ tự gán nhãn.
import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register, TurnUsage } from 'claude-code'

import type { Avg, Job, Tokens, View } from '../types'

type $T = EngineInterface

const PANE = 'so-viec'
const TITLE = 'Sổ việc'
const IDLE_CLOSE_MS = 60 * 60 * 1000 // im lặng quá 60 phút: việc cũ coi như xong
const BRAIN_GAP_MS = 15 * 60 * 1000 // khoảng nghỉ giữa hai lượt ≤15 phút vẫn tính là đang làm
const BRAIN_DAY_MS = 4 * 60 * 60 * 1000 // luật 4 tiếng việc trí óc mỗi ngày
const MIN_SAMPLES = 3 // đủ 3 lần cùng loại mới đưa dự kiến
const MAX_JOBS = 3000

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

// Nhãn cho việc không gọi skill.
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

const view = atom({ plugin: 'so-viec', key: 'view' } as const, null, { shape: 'view-1' })

// ---------- lưu trữ qua nhiều phiên ----------

type Day = { date: string; ms: number; lastEndAt: number }

const zero = (): Tokens => ({ input: 0, output: 0, cacheRead: 0, cacheWrite: 0 })
const total = (t: Tokens) => t.input + t.output + t.cacheRead + t.cacheWrite

const getOpen = async ($: $T) => ((await $.store.get('open')) as Job | undefined) ?? null
const setOpen = async ($: $T, job: Job | null) =>
  job ? $.store.set('open', job) : $.store.delete('open')
const getJobs = async ($: $T) => ((await $.store.get('jobs')) as Job[] | undefined) ?? []

const dateOf = (ms: number) => {
  const d = new Date(ms)
  const p = (n: number) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`
}

const getDay = async ($: $T, now: number): Promise<Day> => {
  const day = (await $.store.get('day')) as Day | undefined
  return day && day.date === dateOf(now) ? day : { date: dateOf(now), ms: 0, lastEndAt: 0 }
}

async function closeJob($: $T, job: Job) {
  if (job.turns === 0) return
  const jobs = await getJobs($)
  jobs.push(job)
  await $.store.set('jobs', jobs.slice(-MAX_JOBS))
}

function averageOf(jobs: Job[], type: string): Avg | null {
  const same = jobs.filter(j => j.type === type)
  if (same.length < MIN_SAMPLES) return null
  const sum = same.reduce(
    (a, j) => ({ ms: a.ms + j.activeMs, tok: a.tok + total(j.tokens) }),
    { ms: 0, tok: 0 },
  )
  return { count: same.length, activeMs: sum.ms / same.length, tokens: sum.tok / same.length }
}

// ---------- hiển thị ----------

const mins = (ms: number) => Math.max(0, Math.round(ms / 60000))
const hm = (ms: number) => {
  const m = mins(ms)
  return m >= 60 ? `${Math.floor(m / 60)}h${String(m % 60).padStart(2, '0')}` : `${m}p`
}
const kt = (n: number) => (n >= 1e6 ? `${(n / 1e6).toFixed(1)}M` : `${Math.round(n / 1000)}k`)

async function refresh($: $T, runningSince: number | null) {
  const now = await $.clock.now()
  const current = await getOpen($)
  const jobs = await getJobs($)
  const day = await getDay($, now)
  const live = runningSince ? now - runningSince : 0
  const v: View = {
    current,
    runningSince,
    avg: current ? averageOf(jobs, current.type) : null,
    todayMs: day.ms + live,
    recent: jobs.slice(-5).reverse(),
  }
  await update($, view, () => v)

  const brain = `hôm nay ${hm(v.todayMs)}/4h`
  if (!current) {
    $.ui.status(`Sổ việc · ${brain}`)
    return
  }
  const ms = current.activeMs + live
  const tok = total(current.tokens)
  const time = v.avg ? `${mins(ms)}/${mins(v.avg.activeMs)}p` : `${mins(ms)}p`
  const tokens = v.avg ? `${kt(tok)}/${kt(v.avg.tokens)} token` : `${kt(tok)} token`
  $.ui.status(`${current.type} · ${time} · ${tokens} · ${brain}`)
}

// ---------- báo cáo ----------

async function report($: $T) {
  const jobs = await getJobs($)
  if (jobs.length === 0) return 'Sổ việc chưa có việc nào xong.'
  const types = [...new Set(jobs.map(j => j.type))]
  const rows = types
    .map(type => {
      const same = jobs.filter(j => j.type === type)
      const ms = same.map(j => j.activeMs)
      const tok = same.map(j => total(j.tokens))
      const avg = (xs: number[]) => xs.reduce((a, b) => a + b, 0) / xs.length
      return {
        type,
        n: same.length,
        line:
          `| ${type} | ${same.length} | ${hm(avg(ms))} | ${kt(avg(tok))} | ` +
          `${hm(Math.min(...ms))} – ${hm(Math.max(...ms))} | ${kt(Math.min(...tok))} – ${kt(Math.max(...tok))} |`,
      }
    })
    .sort((a, b) => b.n - a.n)
  const note = rows.some(r => r.n < MIN_SAMPLES)
    ? `\n\nLoại có dưới ${MIN_SAMPLES} lần: chưa đưa dự kiến.`
    : ''
  return (
    '## Sổ việc: trung bình theo loại việc\n\n' +
    '| Loại việc | Số lần | Thời gian TB | Token TB | Nhanh – chậm | Ít – nhiều token |\n' +
    '|---|---|---|---|---|---|\n' +
    rows.map(r => r.line).join('\n') +
    note +
    '\n\nThời gian = lúc Claude thật sự làm, không tính lúc chờ duyệt.'
  )
}

// ---------- móc vào sự kiện ----------

export const register: Register = on => {
  // Mỗi lượt của luồng chính: loại việc đang chờ gán và skill gọi trong lượt.
  const pending = new Map<string, string>()
  const skillOfTurn = new Map<string, string>()
  let currentTurn: string | null = null
  let runningSince: number | null = null
  let lastTurnStart: number | null = null

  on('session.start', async ($, e, next) => {
    const now = await $.clock.now()
    const open = await getOpen($)
    if (open && now - open.lastAt > IDLE_CLOSE_MS) {
      await closeJob($, open)
      await setOpen($, null)
    }
    await $.command.register({ name: 'bao-cao', description: 'Sổ việc: trung bình thời gian và token theo loại việc' })
    await $.command.register({ name: 'so-viec', description: 'Mở bảng Sổ việc cạnh khung chat' })
    void $.ui.open({ id: PANE, title: TITLE })
    $.clock.every(15000, () => {
      if (runningSince !== null) void refresh($, runningSince)
    })
    await refresh($, null)
    return next(e)
  })

  on('command.run', { command: 'bao-cao' }, async $ => ({ text: await report($) }))
  on('command.run', { command: 'so-viec' }, async $ => {
    await $.ui.open({ id: PANE, title: TITLE })
    return { text: 'Đã mở bảng Sổ việc.' }
  })

  on('turn.start', async ($, e, next) => {
    if (e.agentId !== undefined) return next(e)
    const now = await $.clock.now()
    currentTurn = e.turnId
    runningSince = now
    lastTurnStart = now

    const text = e.text.trim()
    if (text !== '') {
      const open = await getOpen($)
      // Trả lời ngắn khi đang có việc ("ok", "làm đi"): vẫn là việc đó.
      const isFollowUp = open !== null && text.length < 40 && now - open.lastAt < IDLE_CLOSE_MS
      if (!isFollowUp) {
        const hint = open ? `Việc đang làm: ${open.type}. ` : ''
        pending.set(
          e.turnId,
          `${hint}Tin nhắn mới của người dùng (chọn đúng nhãn của việc đang làm nếu đây là tiếp nối): ${text.slice(0, 2000)}`,
        )
      }
    }
    void refresh($, runningSince)
    return next(e)
  })

  on('skill.prompt', async ($, e, next) => {
    const type = SKILL_TYPES[e.skill]
    if (type && currentTurn) skillOfTurn.set(currentTurn, type)
    return next(e)
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    const usage: TurnUsage | undefined = e.usage
    const now = await $.clock.now()

    // Token của trợ lý con cộng vào việc đang mở; thời gian thì không (chạy song song).
    if (e.agentId !== undefined) {
      const open = await getOpen($)
      if (open && usage) {
        add(open.tokens, usage)
        await setOpen($, open)
      }
      return result
    }

    const skill = skillOfTurn.get(e.turnId)
    // Lượt đã trả lời xong (next ở trên), giờ mới gán nhãn: không làm chậm câu trả lời.
    const ask = skill ? undefined : pending.get(e.turnId)
    const label = ask ? await $.model.classify(ask, LABELS).catch(() => undefined) : undefined
    pending.delete(e.turnId)
    skillOfTurn.delete(e.turnId)

    let open = await getOpen($)
    if (open && now - open.lastAt - e.durationMs > IDLE_CLOSE_MS) {
      await closeJob($, open)
      open = null
    }
    const type = skill ?? label ?? open?.type ?? 'khac'
    if (!open || open.type !== type) {
      if (open) await closeJob($, open)
      open = {
        id: e.turnId,
        type,
        startedAt: now - e.durationMs,
        lastAt: now,
        activeMs: 0,
        turns: 0,
        tokens: zero(),
      }
    }
    open.activeMs += e.durationMs
    open.turns += 1
    open.lastAt = now
    if (usage) add(open.tokens, usage)
    await setOpen($, open)

    // Giờ làm việc trí óc hôm nay: thời lượng lượt + khoảng nghỉ ngắn trước nó.
    const day = await getDay($, now)
    const startedAt = lastTurnStart ?? now - e.durationMs
    const gap = day.lastEndAt ? startedAt - day.lastEndAt : 0
    day.ms += e.durationMs + (gap > 0 && gap <= BRAIN_GAP_MS ? gap : 0)
    const wasUnder = day.ms - e.durationMs < BRAIN_DAY_MS
    day.lastEndAt = now
    await $.store.set('day', day)
    if (wasUnder && day.ms >= BRAIN_DAY_MS) $.ui.toast('Sổ việc: hôm nay đã đủ 4 tiếng việc trí óc.')

    if (currentTurn === e.turnId) {
      currentTurn = null
      runningSince = null
    }
    await refresh($, runningSince)
    return result
  })

  on('session.end', async ($, e, next) => {
    // Phiên đóng chưa chắc việc xong (có thể mở lại); để mở, 60 phút im lặng thì tự đóng.
    return next(e)
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    const v = await read($, view)
    const now = await $.clock.now()
    if (!v) return <Text dimColor>Đang tải…</Text>
    const live = v.runningSince ? now - v.runningSince : 0
    const cur = v.current

    return (
      <Box flexDirection="column">
        <Text bold>Việc đang làm</Text>
        {!cur && <Text dimColor>Chưa có việc nào.</Text>}
        {cur && <Text>{cur.type}{v.runningSince ? ' · đang chạy' : ''}</Text>}
        {cur && (
          <Text>
            Thời gian: {hm(cur.activeMs + live)}
            {v.avg ? ` / dự kiến ${hm(v.avg.activeMs)}` : ' (chưa đủ dữ liệu)'}
          </Text>
        )}
        {cur && (
          <Text>
            Token: {kt(total(cur.tokens))}
            {v.avg ? ` / trung bình ${kt(v.avg.tokens)}` : ''}
          </Text>
        )}
        {cur && v.avg && <Text dimColor>Dựa trên {v.avg.count} lần trước cùng loại</Text>}
        <Text> </Text>
        <Text bold>Hôm nay</Text>
        <Text color={v.todayMs >= BRAIN_DAY_MS ? 'warning' : undefined}>
          Việc trí óc: {hm(v.todayMs)} / 4h
        </Text>
        <Text> </Text>
        <Text bold>Việc xong gần đây</Text>
        {v.recent.length === 0 && <Text dimColor>Chưa có.</Text>}
        {v.recent.map(j => (
          <Text dimColor>
            {dateOf(j.startedAt).slice(5)} {j.type} · {hm(j.activeMs)} · {kt(total(j.tokens))}
          </Text>
        ))}
        <Text> </Text>
        <Text dimColor>/bao-cao để xem trung bình theo loại việc</Text>
      </Box>
    )
  })
}

function add(t: Tokens, u: TurnUsage) {
  t.input += u.input_tokens
  t.output += u.output_tokens
  t.cacheRead += u.cache_read_input_tokens
  t.cacheWrite += u.cache_creation_input_tokens
}
