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
export type Turn = [number, number, number, string?]

/** Sổ của một phiên: phien/<sid>.json (mod ghi) hoặc nhap/<sid>.json (nhập ngược). */
export type Book = {
  v: 1
  sid: string
  title: string
  cwd: string
  trackedSince: number
  updatedAt: number
  running: number | null
  /** Tài khoản Claude của lượt gần nhất (8 ký tự đầu mã tài khoản). */
  account?: string
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

/** Sổ hạn mức của một tài khoản Claude: tai-khoan/<mã>.json, cập nhật khi tài khoản đó đang đăng nhập. */
export type Account = {
  id: string
  /** Phần trước @ của email đăng nhập. */
  label: string
  used: number
  resetsAt: string
  /** 1% hạn mức tuần ≈ bao nhiêu token. */
  perPct: number | null
  at: number
}

export type VideoView = {
  at: number
  live: VideoNow[]
  weeks: { id: string; label: string; isCurrent: boolean; used: number; resetsAt: string }[]
  avg: { count: number; ms: number; tokens: number; pct: number | null } | null
  /** Gộp mọi tài khoản: còn đủ khoảng bao nhiêu video. */
  left: number | null
}

declare module 'claude-code' {
  interface PluginState {
    'so-viec': { view: Shaped<VideoView | null> }
  }
}
