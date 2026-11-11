import { expect, test } from 'claude-code/testing'

const usage = { input_tokens: 1000, output_tokens: 2000, cache_read_input_tokens: 10000, cache_creation_input_tokens: 500, model: 'm' }
const PANE = { plugin: 'so-viec', component: 'Pane', requestId: 'so-viec',
  props: { title: 'Sổ việc', isFocused: false, bodyColumns: 44, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} } } as const

test('tổng quan gộp phiên này với phiên khác, có thanh tiến độ', async ($, on) => {
  let now = new Date(2026, 10, 11, 9).getTime()
  const files = new Map<string, string>()
  // Một phiên khác đang chạy, đã ghi sổ.
  const other = { v: 1, sid: 'khac-1', title: 'Phiên dựng video', cwd: '/x', trackedSince: now - 3600000, updatedAt: now,
    running: now - 120000, open: { id: 'o', type: 'cat-highlight-video', startedAt: now - 600000, lastAt: now - 120000, activeMs: 300000, turns: 2,
    tokens: { input: 0, output: 0, cacheRead: 50000, cacheWrite: 0 } }, jobs: [], turns: [[now - 600000, now - 300000, 50000]] }
  files.set('/h/.claude/so-viec/phien/khac-1.json', JSON.stringify(other))

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
  on('session.cwd', () => ({ value: '/Users/moon/Documents/David.Claude' }))
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

  const job = async (n: number, skill?: string) => {
    const turnId = `t${n}`
    await $.turn.start({ text: skill ? '' : 'giải thích cái này giúp tôi được không nhé', turnId })
    if (skill) await $.skill.prompt({ skill, text: 'x', frontmatter: {}, source: 'userSettings' } as never)
    now += 60000 * n
    await $.turn.complete({ answer: '', durationMs: 60000 * n, isAborted: false, turnId, reason: 'answer', usage } as never)
  }
  await job(1, 'video-style-edit')
  await job(2)
  await job(3, 'video-style-edit')
  await job(4)
  await job(5, 'video-style-edit')
  await job(6)

  expect(files.has('/h/.claude/so-viec/phien/phien-nay.json')).toBe(true)
  // Phiên kia vẫn báo nhịp.
  files.set('/h/.claude/so-viec/phien/khac-1.json', JSON.stringify({ ...other, updatedAt: now }))
  const r = await $.command.run({ command: 'bao-cao', args: '' } as never)
  expect(r.text).toContain('| video-style-edit | 3 | 3p | 14k |')
  expect(r.text).toContain('Phiên dựng video: cat-highlight-video')
  expect(r.text).toContain('2 phiên')

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface } as never)
    expect((await ui.find({ type: 'Text', text: /Phiên dựng video/ }))?.text).toContain('cat-highlight-video')
    expect((await ui.find({ type: 'Text', text: /\/4h/ }))?.text).toMatch(/[█░]+ \S+\/4h/)
    await ui.unmount()
  }
})
