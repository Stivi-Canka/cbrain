"""Tracks last_edited_time per Notion page to skip unchanged entries."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

STATE_PATH = Path(__file__).parent.parent / ".state.json"


def load() -> dict[str, str]:
    """Load the state file from disk.

    Returns:
        Dict mapping page ID to last_edited_time string.
    """
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text())


def save(state: dict[str, str]) -> None:
    """Write the state dict to disk.

    Args:
        state: Dict mapping page ID to last_edited_time string.
    """
    STATE_PATH.write_text(json.dumps(state, indent=2))
    logger.info("State saved.")


def has_changed(page: dict, state: dict[str, str]) -> bool:
    """Check if a Notion page has changed since the last sync.

    Args:
        page: Raw Notion page dict.
        state: Current state dict from load().

    Returns:
        True if the page is new or has been edited since last sync.
    """
    page_id = page["id"]
    last_edited = page["last_edited_time"]
    return state.get(page_id) != last_edited
