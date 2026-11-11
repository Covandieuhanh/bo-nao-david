import { expect, test } from 'claude-code/testing'

const usage = { input_tokens: 1000, output_tokens: 2000, cache_read_input_tokens: 10000, cache_creation_input_tokens: 500, model: 'm' }

test('ba việc cùng skill thì có dự kiến và báo cáo', async ($, on) => {
  on('command.register', () => ({ value: { command: 'x' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('turn.start', (_, e) => ({ turnId: e.turnId }))
  on('skill.prompt', (_, e) => ({ text: e.text }))
  on('turn.complete', () => ({ text: '' }))
  on('model.classify', () => ({ value: 'hoi-dap' }))
  let now = Date.UTC(2026, 10, 11, 8)
  on('clock.now', () => ({ value: (now += 1000) }))
  on('clock.every', () => ({ value: {} }))
  on('ui.status', () => ({ value: undefined }))
  const kv = new Map<string, unknown>()
  on('store.get', (_, e) => ({ value: kv.get((e as { key: string }).key) }))
  on('store.set', (_, e) => { const a = e as { key: string; value: unknown }; kv.set(a.key, a.value); return { value: undefined } })
  on('store.delete', (_, e) => { kv.delete((e as { key: string }).key); return { value: undefined } })

  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true } as never)

  const job = async (n: number, skill?: string) => {
    const turnId = `t${n}`
    await $.turn.start({ text: skill ? '' : 'giải thích cái này giúp tôi được không nhé', turnId })
    if (skill) await $.skill.prompt({ skill, text: 'x', frontmatter: {}, source: 'userSettings' } as never)
    await $.turn.complete({ answer: '', durationMs: 60000 * n, isAborted: false, turnId, reason: 'answer', usage } as never)
  }
  // Xen việc khác vào giữa để mỗi lần skill là một việc riêng.
  await job(1, 'video-style-edit')
  await job(2)
  await job(3, 'video-style-edit')
  await job(4)
  await job(5, 'video-style-edit')
  await job(6)

  const r = await $.command.run({ command: 'bao-cao', args: '' } as never)
  expect(r.text).toContain('| video-style-edit | 3 | 3p | 14k |')
  expect(r.text).toContain('| hoi-dap | 2 |')

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ plugin: 'so-viec', component: 'Pane', requestId: 'so-viec', surface,
      props: { title: 'Sổ việc', isFocused: false, bodyColumns: 40, placement: 'dock', scroll: { offset: 0, bodyRows: 20 }, view: {} } } as never)
    expect((await ui.find({ type: 'Text', text: /hoi-dap/ }))?.text).toBe('hoi-dap')
    expect((await ui.find({ type: 'Text', text: /Việc trí óc/ }))?.text).toContain('/ 4h')
    await ui.unmount()
  }
})
