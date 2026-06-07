"""cbrain orchestrator — syncs Notion entries to markdown files."""

import logging
from scripts.cbrain_sync import fetch_entries, parse_entry, fetch_body
from scripts.writer import write_entry

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the cbrain sync pipeline."""
    logger.info("cbrain run started.")

    pages = fetch_entries()
    for page in pages:
        entry = parse_entry(page)
        body = fetch_body(entry["id"])
        write_entry(entry, body)

    logger.info("cbrain run complete.")


if __name__ == "__main__":
    main()
