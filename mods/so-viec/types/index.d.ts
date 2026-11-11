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

export type Avg = { count: number; activeMs: number; tokens: number }

export type View = {
  current: Job | null
  runningSince: number | null
  avg: Avg | null
  todayMs: number
  recent: Job[]
}

declare module 'claude-code' {
  interface PluginState {
    'so-viec': { view: Shaped<View | null> }
  }
}
