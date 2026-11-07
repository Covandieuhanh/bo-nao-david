---
name: notion-local-dev-environment
description: "How to run the App notion tiers locally on this macOS machine (nvm, embedded-postgres, npm allow-scripts)"
metadata: 
  node_type: memory
  type: project
  originSessionId: a330419c-6639-476e-ae0e-32d7f3c2d7fd
---

The dev machine (arm64 macOS) has **no Docker, no Homebrew, and sudo needs a password**. So:

- **Node** is installed via nvm — every new shell must `export NVM_DIR="$HOME/.nvm"; . "$NVM_DIR/nvm.sh"` before `node`/`npm` work.
- **Postgres** runs via the `embedded-postgres` npm package (no Docker): in notion-db run `npm run pg:dev` (data in `.pgdata/`, listens on 5432, db `notion`). `docker-compose.yml` is the documented prod path only.
- **npm blocks install scripts** (allow-scripts feature). After `npm install`, if you see "packages have install scripts", run `npm approve-scripts <pkg>` then `npm rebuild <pkg>`. Already approved: `esbuild`, `@embedded-postgres/darwin-arm64` (pinned in each package.json `allowScripts`).

Run order: pg:dev → `npm run db:migrate` (notion-db) → `npm run dev` (notion-backend, :4000) → `npm run dev` (notion-frontend, :5173).

In-tool browsers were unavailable this session (Chrome extension offline; `preview_start` sandbox can't access its cwd). Verify UI by opening http://localhost:5173 manually. See [[notion-3tier-architecture]].
