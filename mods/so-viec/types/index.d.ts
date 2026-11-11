export type Tokens = { input: number; output: number; cacheRead: number; cacheWrite: number }

export type Job = {
  id: string
  type: string
  startedAt: number
  lastAt: number
  activeMs: number
  turns: number
  tokens: Tokens
}

/** Một lượt: [bắt đầu, kết thúc, tổng token]. */
export type Turn = [number, number, number]

/** Sổ của một phiên: phien/<sid>.json (mod ghi) hoặc nhap/<sid>.json (nhập ngược). */
export type Book = {
  v: 1
  sid: string
  title: string
  cwd: string
  trackedSince: number
  updatedAt: number
  running: number | null
  /** Loại việc của lượt đang chạy, khi đã biết (skill vừa gọi, tiếp nối). */
  runningType?: string | null
  open: Job | null
  jobs: Job[]
  turns: Turn[]
}

export type Avg = { type: string; count: number; activeMs: number; tokens: number }

export type Live = {
  sid: string
  title: string
  isMine: boolean
  isRunning: boolean
  type: string | null
  ms: number
  tokens: number
  avg: Avg | null
  basis: 'loai' | 'chung' | null
}

export type Period = { ms: number; tokens: number; jobs: number }

export type Overview = {
  at: number
  live: Live[]
  today: Period
  week: Period
  total: Period & { sessions: number; since: number }
  avgs: Avg[]
  recent: Job[]
}

declare module 'claude-code' {
  interface PluginState {
    'so-viec': { view: Shaped<Overview | null> }
  }
}
