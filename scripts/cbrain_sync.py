"""Fetches all entries from the cbrain Notion database and parses them."""

import logging
from notion_client import Client
from config import settings

NOTION_CLIENT = None


def get_client() -> Client:
    """Return a shared Notion client instance."""
    global NOTION_CLIENT
    if NOTION_CLIENT is None:
        NOTION_CLIENT = Client(auth=settings.notion_api_key)
    return NOTION_CLIENT

logger = logging.getLogger(__name__)


def fetch_entries() -> list[dict]:
    """Fetch all entries from the cbrain Notion database.

    Returns:
        List of raw Notion page objects.

    Raises:
        notion_client.errors.APIResponseError: If the Notion API returns an error.
    """
    notion = get_client()
    logger.info("Querying cbrain database.")
    response = notion.databases.query(database_id=settings.cbrain_db_id)
    logger.info(f"Fetched {len(response['results'])} entries.")
    return response["results"]


def parse_entry(page: dict) -> dict:
    """Extract cbrain fields from a raw Notion page object.

    Args:
        page: A single Notion page dict from databases.query results.

    Returns:
        Dict with keys: id, title, type, tags, source_type, source, author, date.
    """
    props = page["properties"]

    def rich_text(field: str) -> str:
        items = props[field]["rich_text"]
        return items[0]["plain_text"] if items else ""

    def select(field: str) -> str:
        sel = props[field]["select"]
        return sel["name"] if sel else ""

    def multi_select(field: str) -> list[str]:
        return [item["name"] for item in props[field]["multi_select"]]

    def date(field: str) -> str:
        d = props[field]["date"]
        return d["start"] if d else ""

    return {
        "id": page["id"],
        "title": props["title"]["title"][0]["plain_text"],
        "type": select("type"),
        "tags": multi_select("tags"),
        "source_type": select("source_type"),
        "source": rich_text("source"),
        "author": rich_text("author"),
        "date": date("Date"),
    }


def fetch_body(page_id: str) -> str:
    """Fetch the plain text body of a Notion page from its blocks.

    Args:
        page_id: The Notion page ID.

    Returns:
        The page body as a single string with paragraphs separated by newlines.

    Raises:
        notion_client.errors.APIResponseError: If the Notion API returns an error.
    """
    notion = get_client()
    response = notion.blocks.children.list(block_id=page_id)
    paragraphs = []
    for block in response["results"]:
        if block["type"] == "paragraph":
            texts = block["paragraph"]["rich_text"]
            if texts:
                paragraphs.append(texts[0]["plain_text"])
    return "\n\n".join(paragraphs)
