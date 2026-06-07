"""cbrain orchestrator — syncs Notion entries to markdown files."""

import json
import logging
from scripts.cbrain_sync import fetch_entries, parse_entry, fetch_body

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the cbrain sync pipeline."""
    logger.info("cbrain run started.")

    pages = fetch_entries()
    for page in pages:
        entry = parse_entry(page)
        entry["body"] = fetch_body(entry["id"])
        print(json.dumps(entry, indent=2))

    logger.info("cbrain run complete.")


if __name__ == "__main__":
    main()
