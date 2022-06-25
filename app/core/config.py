import os
from dotenv import load_dotenv
from pathlib import Path
from functools import lru_cache

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings():
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION", "1.0.0")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "test")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
