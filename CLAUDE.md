# CBRAIN — Personal Knowledge Base

## What this is

A personal second brain that stores knowledge entries as markdown files in a private GitHub repo. Entries are created in Notion (mobile-friendly), synced to this repo via a cron job on an Oracle VPS.

## Entry types

Two types only: knowledge and signal.

### knowledge

Anything extracted from an external source (book, article, podcast, talk).

### signal

Trends being tracked, observations, beliefs — including my own convictions. If it came from outside, it's knowledge. If it's a pattern I'm noticing or a belief I'm forming, it's a signal.

## File structure

cbrain/
├── CLAUDE.md
├── knowledge/          # one .md file per knowledge entry
├── signals/            # one .md file per signal entry
├── scripts/            # sync script and utilities
│   └── cbrain_sync.py
└── .env                # NOTION_TOKEN, CBRAIN_DB_ID — never commit this

## Entry schema — knowledge

---
type: knowledge
title: [Clear searchable title]
source_type: book | article | podcast | case_study | talk
source: "[Name of source]"
author: [Author or speaker]
date: YYYY-MM-DD
tags: [tag1, tag2]
confidence: high | medium | low
related: []
---

[Compiled truth — 2-5 paragraphs, self-contained, written for a cold reader.
No shorthand. No pronouns without antecedents.]

---
- YYYY-MM-DD: [Initial timeline note]

## Entry schema — signal

---
type: signal
title: [Trend or belief stated as a claim]
domain: ai | vc | strategy | hardware | macro | other
heard_via: podcast | interview | article | conversation | observation
source: "[Specific source]"
date: YYYY-MM-DD
tags: [tag1, tag2]
signal_strength: strong | weak | noise
related: []
---

[Compiled truth — what is the trend, who's saying it, why it matters,
what would falsify it, current take.]

---
- YYYY-MM-DD: [Initial note]

## File naming

Slugify the title: lowercase, spaces to hyphens, remove special chars,
cap at 60 chars. Example: "Demis Hassabis on AGI" → demis-hassabis-on-agi.md
Place in knowledge/ or signals/ depending on type.

## Sync pipeline (what we're building)

Notion database → cbrain_sync.py on VPS → git commit → push to this repo
Cron job runs daily at 8am on Oracle Cloud VPS (Ubuntu 22.04, Ampere A1).
Script uses notion-client Python library, reads NOTION_TOKEN and CBRAIN_DB_ID
from .env via python-dotenv.

## Environment

- VPS: Oracle Cloud Free Tier, Ubuntu 22.04, accessed via `ssh mirai`
- Python: managed with uv, venv at ~/cbrain-env or similar
- Repo path on VPS: ~/cbrain
- Git auth: SSH key already set up with GitHub (to be configured)

## Current build status
- [x] Entry schema designed
- [x] Repo structure decided
- [ ] GitHub repo created and cloned to VPS
- [ ] Notion database created with correct properties
- [ ] cbrain_sync.py written and tested
- [ ] Cron job configured
- [ ] First real entries committed

## Working style

I would like to build this myself, but with your careful guidance along each step. I am someone that like to learn from the ground up, slowly, without taking concepts from granted. When I eventually ask you to build certain functionalities, build one piece at a time. Explain what each piece does before writing it. Don't move to the next step until the current one works and is understood.
Prefer simple solutions. No premature abstraction.
