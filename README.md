# cbrain

Personal second brain. Knowledge and signal entries written in Notion, synced to this repo daily via a cron job on an Oracle VPS.

## Entry types

- **knowledge** — anything extracted from an external source (book, article, podcast, talk)
- **signal** — trends being tracked, observations, beliefs I'm forming

## Structure

```
cbrain/
├── knowledge/       # one .md file per knowledge entry
├── signals/         # one .md file per signal entry
├── scripts/         # sync script and utilities
└── main.py
```

## Setup

Requires a `.env` file with `NOTION_TOKEN` and `CBRAIN_DB_ID`. Never committed.