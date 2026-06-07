"""Writes parsed cbrain entries to markdown files."""

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).parent.parent
DIR_MAP = {"knowledge": "knowledge", "signal": "signals"}


def slugify(title: str) -> str:
    """Convert a title to a filename-safe slug.

    Args:
        title: The entry title.

    Returns:
        Lowercase, hyphen-separated slug capped at 60 characters.
    """
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug).strip("-")
    return slug[:60]


def write_entry(entry: dict, body: str) -> Path:
    """Write a cbrain entry to a markdown file.

    Args:
        entry: Parsed entry dict from parse_entry.
        body: Plain text body from fetch_body.

    Returns:
        Path to the written file.

    Raises:
        ValueError: If entry type is not 'knowledge' or 'signal'.
    """
    if entry["type"] not in DIR_MAP:
        raise ValueError(f"Unknown entry type: {entry['type']}")

    directory = REPO_ROOT / DIR_MAP[entry["type"]]
    directory.mkdir(exist_ok=True)
    slug = slugify(entry["title"])
    path = directory / f"{slug}.md"

    tags_str = ", ".join(entry["tags"])
    frontmatter = f"""---
title: {entry["title"]}
type: {entry["type"]}
source_type: {entry["source_type"]}
source: {entry["source"]}
author: {entry["author"]}
date: {entry["date"]}
tags: [{tags_str}]
---"""

    path.write_text(f"{frontmatter}\n\n{body}\n")
    logger.info(f"Written: {path}")
    return path
