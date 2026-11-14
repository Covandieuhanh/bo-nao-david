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
  /** Khung dùng bot Telegram (tên khung hoặc tin nhắn từ Telegram): mọi việc không phải video tính vào bot Telegram. */
  isTelegram?: boolean
  open: Job | null
  jobs: Job[]
  turns: Turn[]
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

/** Một khung đang chạy. */
export type LiveRow = {
  sid: string
  title: string
  isMine: boolean
  isNoMod?: boolean
  /** Tên việc lớn đang làm. */
  group: string
  ms: number
}

/** Một việc lớn: tuần này tốn bao nhiêu, từ đầu chiếm bao nhiêu. */
export type GroupRow = {
  id: string
  name: string
  weekMs: number
  /** Phần trăm hạn mức tuần, ước tính; null khi chưa đo được tài khoản nào. */
  weekPct: number | null
  weekTokens: number
  allMs: number
  /** Phần trăm trong tổng token từ đầu. */
  allShare: number
}

export type BigView = {
  at: number
  live: LiveRow[]
  weeks: { id: string; label: string; isCurrent: boolean; used: number; resetsAt: string }[]
  groups: GroupRow[]
  video: { count: number; ms: number; pct: number | null } | null
  since: number
  allMs: number
}

declare module 'claude-code' {
  interface PluginState {
    'so-viec': { view: Shaped<BigView | null> }
  }
}
