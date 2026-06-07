"""Commits and pushes new or updated cbrain entries to GitHub."""

import logging
import subprocess
from datetime import date

logger = logging.getLogger(__name__)


def _run(cmd: list[str]) -> str:
    """Run a git command and return stdout.

    Args:
        cmd: Command as a list of strings.

    Returns:
        stdout as a stripped string.

    Raises:
        subprocess.CalledProcessError: If the command exits non-zero.
    """
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def commit_and_push(updated: int) -> None:
    """Stage, commit, and push changed entry files.

    Skips commit if there are no staged changes.

    Args:
        updated: Number of entries updated, used in the commit message.
    """
    _run(["git", "add", "knowledge/", "signals/"])

    status = _run(["git", "status", "--porcelain"])
    if not status:
        logger.info("Nothing to commit.")
        return

    message = f"sync: {date.today()} — {updated} entr{'y' if updated == 1 else 'ies'} updated"
    _run(["git", "commit", "-m", message])
    _run(["git", "push"])
    logger.info(f"Pushed: {message}")
