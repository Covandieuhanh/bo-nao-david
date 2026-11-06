---
name: notion-3tier-architecture
description: "The App notion project is a 3-tier Notion-like task manager split into notion-db, notion-backend, notion-frontend"
metadata: 
  node_type: memory
  type: project
  originSessionId: a330419c-6639-476e-ae0e-32d7f3c2d7fd
---

GitHub (private, since 2026-11-06): Covandieuhanh/notion-db, notion-backend, notion-frontend, app-notion-goc (root README, Google Apps Script version, docs).

`/Users/moon/Documents/App notion/` holds a Notion-like project/task manager, deliberately split into **3 independent git repos** so each tier can deploy to its own server:

- **notion-db** — Postgres 16 + Drizzle ORM. Owns schema (`src/schema.ts`, single file so drizzle-kit resolves it), migrations, seed. Publishes `@notion/db` (schema + `createDbClient` + re-exported drizzle operators). Backend consumes it via `file:../notion-db`.
- **notion-backend** — Fastify + zod + `@fastify/swagger` (OpenAPI at `/openapi.json`) + JWT auth. **Only tier with `DATABASE_URL`**; enforces ownership by `user_id`. Uses **bcryptjs** (pure JS) not argon2. Port 4000.
- **notion-frontend** — Vite SPA (React 19 + TanStack Router file-based + shadcn/ui + Tailwind v4). Ported from the old Lovable repo (Covandieuhanh/app-notion-mun), Supabase removed. Talks to backend via `VITE_API_URL`. `use-workspace.ts` maps camelCase(API)↔snake_case(UI). Port 5173.

Decisions (confirmed by user): left Lovable, 3 separate repos, REST+OpenAPI, self-managed Postgres (no Supabase), clean start (no data migration). Plan file: `~/.claude/plans/polymorphic-mapping-micali.md` (Phase 0 done; Phases 1–4 add features per tier). See [[notion-local-dev-environment]].
