import { expect, test } from 'claude-code/testing'

const usage = { input_tokens: 1000, output_tokens: 2000, cache_read_input_tokens: 10000, cache_creation_input_tokens: 500, model: 'm' }
const PANE = { plugin: 'so-viec', component: 'Pane', requestId: 'so-viec',
  props: { title: 'Sổ việc', isFocused: false, bodyColumns: 44, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} } } as const
const tok = (n: number) => ({ input: 0, output: 0, cacheRead: n, cacheWrite: 0 })

test('chỉ còn video: đang làm, % tuần, TB 1 video', { timeoutMs: 30000 }, async ($, on) => {
  let now = new Date(2026, 10, 11, 9).getTime()
  const files = new Map<string, string>()
  const book = (sid: string, jobs: object[], turns: number[][]) => ({ v: 1, sid, title: sid, cwd: '/x', trackedSince: now - 86400000,
    updatedAt: now - 86400000, running: null, open: null, jobs, turns })
  // Hai video đã xong: 30 và 50 phút, 2M và 4M token. Một việc không phải video.
  files.set('/h/.claude/so-viec/nhap/v1.json', JSON.stringify(book('v1', [
    { id: 'a', type: 'video-style-edit', startedAt: 0, lastAt: 0, activeMs: 20 * 60000, turns: 3, tokens: tok(1_500_000) },
    { id: 'b', type: 'dang-da-kenh', startedAt: 0, lastAt: 0, activeMs: 10 * 60000, turns: 1, tokens: tok(500_000) },
  ], [[now - 3600000, now - 3000000, 2_000_000]])))
  files.set('/h/.claude/so-viec/nhap/v2.json', JSON.stringify(book('v2', [
    { id: 'c', type: 'cat-highlight-video', startedAt: 0, lastAt: 0, activeMs: 50 * 60000, turns: 5, tokens: tok(4_000_000) },
  ], [[now - 7200000, now - 4000000, 4_000_000]])))
  files.set('/h/.claude/so-viec/nhap/k1.json', JSON.stringify(book('k1', [
    { id: 'd', type: 'sua-bo-nao', startedAt: 0, lastAt: 0, activeMs: 99 * 60000, turns: 5, tokens: tok(9_000_000) },
  ], [[now - 9000000, now - 8000000, 9_000_000]])))

  on('command.register', () => ({ value: { command: 'x' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('ui.status', () => ({ value: undefined }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('turn.start', (_, e) => ({ turnId: e.turnId }))
  on('skill.prompt', (_, e) => ({ text: e.text }))
  on('turn.complete', () => ({ text: '' }))
  on('model.classify', () => ({ value: 'hoi-dap' }))
  on('clock.now', () => ({ value: (now += 1000) }))
  on('clock.every', () => ({ value: {} }))
  on('store.delete', () => ({ value: undefined }))
  on('env.get', () => ({ value: '/h' }))
  on('session.id', () => ({ value: 'phien-nay' }))
  on('session.cwd', () => ({ value: '/x' }))
  // Tuần đã dùng 30%: tổng token tuần 15M + phiên này → 1% ≈ 0,5M.
  on('session.usage', () => ({ value: { startedAt: now, context: {}, rateLimits: [{ kind: 'seven_day', percentUsed: 30, resetsAt: new Date(now + 3 * 86400000).toISOString() }] } }))
  on('fs.exists', (_, e) => {
    const p = (e as { path: string }).path
    return { value: files.has(p) || [...files.keys()].some(k => k.startsWith(p + '/')) }
  })
  on('fs.read', (_, e) => ({ value: files.get((e as { path: string }).path) ?? '' }))
  on('fs.write', (_, e) => { const a = e as { path: string; text: string }; files.set(a.path, a.text); return { value: undefined } })
  on('fs.list', (_, e) => {
    const p = (e as { path: string }).path + '/'
    return { value: [...files.keys()].filter(k => k.startsWith(p) && !k.slice(p.length).includes('/'))
      .map(k => ({ name: k.slice(p.length), kind: 'file', size: 1, mtimeMs: 0, isLink: false })) }
  })

  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true } as never)
  // Khung này đang dựng video: một lượt 20 phút đã xong, lượt mới đang chạy.
  await $.turn.start({ text: 'dựng video thói quen nhỏ theo skill nhé', turnId: 't1' })
  await $.skill.prompt({ skill: 'video-style-edit', text: 'x', frontmatter: {}, source: 'userSettings' } as never)
  now += 20 * 60000
  await $.turn.complete({ answer: '', durationMs: 20 * 60000, isAborted: false, turnId: 't1', reason: 'answer', usage } as never)
  await $.turn.start({ text: 'ok', turnId: 't2' })

  const r = await $.command.run({ command: 'bao-cao', args: '' } as never)
  console.log(r.text)
  expect(r.text).toContain('**TB 1 video:** 40p')
  expect(r.text).toContain('(từ 2 video)')
  expect(r.text).toContain('**Tuần này:** 30% đã dùng')
  expect(r.text).toContain('**Khung này**: 20p')
  expect(r.text).not.toContain('4h')

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface } as never)
    expect((await ui.find({ type: 'Text', text: /Video đang làm/ }))?.text).toBeTruthy()
    expect((await ui.find({ type: 'Text', text: /đã dùng/ }))?.text).toMatch(/^[█░]+ 30% đã dùng$/)
    expect((await ui.find({ type: 'Text', text: /từ 2 video/ }))?.text).toBeTruthy()
    await ui.unmount()
  }
})
