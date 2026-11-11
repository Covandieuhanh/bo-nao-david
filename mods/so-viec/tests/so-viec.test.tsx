import { expect, test } from 'claude-code/testing'

const usage = { input_tokens: 1000, output_tokens: 2000, cache_read_input_tokens: 10000, cache_creation_input_tokens: 500, model: 'm' }
const PANE = { plugin: 'so-viec', component: 'Pane', requestId: 'so-viec',
  props: { title: 'Sổ việc', isFocused: false, bodyColumns: 44, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} } } as const
const tok = (n: number) => ({ input: 0, output: 0, cacheRead: n, cacheWrite: 0 })

test('tổng hợp theo việc lớn, gộp mọi tài khoản, chữ đầy đủ', { timeoutMs: 30000 }, async ($, on) => {
  let now = new Date(2026, 10, 11, 9).getTime()
  const files = new Map<string, string>()
  const book = (sid: string, jobs: object[], turns: number[][]) => ({ v: 1, sid, title: sid, cwd: '/x', trackedSince: now - 86400000,
    updatedAt: now - 86400000, running: null, open: null, jobs, turns })
  // Hai video đã xong: 30 và 50 phút, 2M và 4M token. Một việc không phải video.
  files.set('/h/.claude/so-viec/nhap/v1.json', JSON.stringify(book('v1', [
    { id: 'a', type: 'video-style-edit', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 20 * 60000, turns: 3, tokens: tok(1_500_000) },
    { id: 'b', type: 'dang-da-kenh', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 10 * 60000, turns: 1, tokens: tok(500_000) },
  ], [[now - 3600000, now - 3000000, 2_000_000]])))
  files.set('/h/.claude/so-viec/nhap/v2.json', JSON.stringify(book('v2', [
    { id: 'c', type: 'cat-highlight-video', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 50 * 60000, turns: 5, tokens: tok(4_000_000) },
  ], [[now - 7200000, now - 4000000, 4_000_000]])))
  files.set('/h/.claude/so-viec/nhap/k1.json', JSON.stringify(book('k1', [
    { id: 'd', type: 'sua-bo-nao', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 99 * 60000, turns: 5, tokens: tok(9_000_000) },
  ], [[now - 9000000, now - 8000000, 9_000_000]])))

  // Tài khoản khác cũng dùng máy này trong tuần: không được tính vào % tuần của tài khoản đang đăng nhập.
  files.set('/h/.claude/so-viec/nhap/k2.json', JSON.stringify({ account: 'bbbbbbbb', ...book('k2', [
    { id: 'e', type: 'sua-bo-nao', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 60000, turns: 1, tokens: tok(30_000_000) },
  ], [[now - 5000000, now - 4900000, 30_000_000, 'bbbbbbbb']]) }))
  // Video làm bằng tài khoản kia: 60 phút, 5 triệu token; tài khoản kia 1% ≈ 1 triệu token → 5%.
  files.set('/h/.claude/so-viec/nhap/v3.json', JSON.stringify({ ...book('v3', [
    { id: 'f', type: 'podcast-style-edit', startedAt: now - 3600000, lastAt: now - 3000000, activeMs: 60 * 60000, turns: 2, tokens: tok(5_000_000) },
  ], [[now - 6000000, now - 5500000, 5_000_000, 'bbbbbbbb']]), account: 'bbbbbbbb' }))
  files.set('/h/.claude/so-viec/tai-khoan/bbbbbbbb.json', JSON.stringify({ id: 'bbbbbbbb', label: 'tai-khoan-hai', used: 40,
    resetsAt: new Date(now + 2 * 86400000).toISOString(), perPct: 1_000_000, at: now }))
  files.set('/h/.claude.json', JSON.stringify({ oauthAccount: { accountUuid: 'aaaaaaaa-1111-2222-3333-444444444444', emailAddress: 'david.mot@example.com' } }))

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
  // Video: v1 (2 triệu, tài khoản này) 4% + v2 (4 triệu) 8% + v3 (5 triệu, tài khoản kia) 5% + khung này đang làm.
  expect(r.text).toContain('- Làm video: 17% hạn mức tuần')
  expect(r.text).toContain('- Trung bình một video: 47 phút, tốn 6% hạn mức tuần (tính từ 3 video)')
  // sua-bo-nao (nhãn cũ) tự quy về xây bộ não: k1 9 triệu = 18%, k2 30 triệu của tài khoản kia = 30%.
  expect(r.text).toContain('- Xây bộ não (skill, luật, mod): 48% hạn mức tuần')
  expect(r.text).toContain('- dựng video thói quen nhỏ theo skill nhé (khung này): Làm video, đã chạy')
  expect(r.text).toContain('- david.mot (đang đăng nhập): đã dùng 30%')
  expect(r.text).not.toMatch(/\bTB\b|\d+p\b|\dM\b/)

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...PANE, surface } as never)
    expect((await ui.find({ type: 'Text', text: /Đang làm trên Claude/ }))?.text).toBeTruthy()
    expect((await ui.find({ type: 'Text', text: /đã dùng 30%/ }))?.text).toMatch(/^[█░]+ đã dùng 30%$/)
    expect((await ui.find({ type: 'Text', text: /Trung bình một video/ }))?.text).toContain('47 phút')
    await ui.unmount()
  }
})

test('mỗi khung đang chạy ghi đúng việc lớn', { timeoutMs: 30000 }, async ($, on) => {
  const now = new Date(2026, 10, 11, 9).getTime()
  const files = new Map<string, string>()
  // Khung này đang chạy việc làm mod; khung kia đang chạy, việc đang mở là video.
  files.set('/h/.claude/so-viec/phien/phien-nay.json', JSON.stringify({ v: 1, sid: 'phien-nay', title: 'Làm mod', cwd: '/x', trackedSince: now, updatedAt: now,
    running: now - 60000, runningType: 'lam-mod', open: { id: 'm', type: 'lam-mod', startedAt: now, lastAt: now, activeMs: 9 * 60000, turns: 3, tokens: { input: 0, output: 0, cacheRead: 1, cacheWrite: 0 } }, jobs: [], turns: [] }))
  files.set('/h/.claude/so-viec/phien/khac.json', JSON.stringify({ v: 1, sid: 'khac', title: 'Dựng video thói quen', cwd: '/x', trackedSince: now, updatedAt: now,
    running: now - 120000, runningType: null, open: { id: 'v', type: 'video-style-edit', startedAt: now, lastAt: now, activeMs: 30 * 60000, turns: 3, tokens: { input: 0, output: 0, cacheRead: 1, cacheWrite: 0 } }, jobs: [], turns: [] }))
  on('command.register', () => ({ value: { command: 'x' } }))
  on('ui.open', () => ({ value: { isPlaced: true } }))
  on('ui.status', () => ({ value: undefined }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('clock.now', () => ({ value: now }))
  on('clock.every', () => ({ value: {} }))
  on('store.delete', () => ({ value: undefined }))
  on('env.get', () => ({ value: '/h' }))
  on('session.id', () => ({ value: 'phien-nay' }))
  on('session.cwd', () => ({ value: '/x' }))
  on('session.usage', () => ({ value: { startedAt: now, context: {}, rateLimits: [] } }))
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
  const r = await $.command.run({ command: 'bao-cao', args: '' } as never)
  expect(r.text).toContain('- Dựng video thói quen: Làm video, đã chạy 32 phút')
  // Khung này vừa mở, chưa chạy lượt nào: không hiện ở "đang làm"; việc làm mod vẫn vào xây bộ não.
  expect(r.text).not.toContain('Làm mod (khung này)')
  expect(r.text).toContain('- Xây bộ não (skill, luật, mod): chưa rõ hạn mức tuần, 9 phút')
})
