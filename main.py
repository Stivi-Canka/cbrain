"""cbrain orchestrator — syncs Notion entries to markdown files."""

import logging
from scripts.cbrain_sync import fetch_entries, parse_entry, fetch_body
from scripts.writer import write_entry
from scripts import state
from scripts.git_sync import commit_and_push

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the cbrain sync pipeline."""
    logger.info("cbrain run started.")

    current_state = state.load()
    pages = fetch_entries()

    updated = 0
    for page in pages:
        if not state.has_changed(page, current_state):
            continue
        entry = parse_entry(page)
        body = fetch_body(entry["id"])
        write_entry(entry, body)
        current_state[page["id"]] = page["last_edited_time"]
        updated += 1

    state.save(current_state)
    commit_and_push(updated)
    logger.info(f"Sync complete. {updated} entries updated.")


if __name__ == "__main__":
    main()
