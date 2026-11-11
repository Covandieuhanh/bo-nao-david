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
  /** Token đã dùng trong lượt đang chạy (cộng từng bước). */
  liveTokens?: number
  open: Job | null
  jobs: Job[]
  turns: Turn[]
}

export type VideoNow = {
  sid: string
  title: string
  isMine: boolean
  isRunning: boolean
  /** Phiên mở trước khi cài mod: số liệu đọc từ lịch sử phiên. */
  isNoMod?: boolean
  ms: number
  tokens: number
  /** % giới hạn tuần, ước tính từ token; null khi chưa đọc được giới hạn tuần. */
  pct: number | null
}

export type VideoView = {
  at: number
  live: VideoNow[]
  week: { used: number; resetsAt: string } | null
  weekTokens: number
  avg: { count: number; ms: number; tokens: number; pct: number | null } | null
  /** Còn đủ khoảng bao nhiêu video trong tuần. */
  left: number | null
}

declare module 'claude-code' {
  interface PluginState {
    'so-viec': { view: Shaped<VideoView | null> }
  }
}
