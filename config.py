"""Central configuration for cbrain — settings loaded from .env."""

import logging
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-driven secrets, loaded from .env."""

    model_config = SettingsConfigDict(env_file=".env")
    notion_api_key: str
    cbrain_db_id: str


Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logs/cbrain.log", mode="a"),
    ],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

settings = Settings()
