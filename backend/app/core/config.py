"""
Application configuration using Pydantic Settings.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )

    # ==========================
    # Application
    # ==========================

    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str
    DEBUG: bool

    # ==========================
    # API
    # ==========================

    API_HOST: str
    API_PORT: int

    # ==========================
    # PostgreSQL
    # ==========================

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    DATABASE_URL: str

    # ==========================
    # Redis
    # ==========================

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_URL: str

    # ==========================
    # Qdrant
    # ==========================

    QDRANT_HOST: str
    QDRANT_PORT: int
    QDRANT_API_KEY: str | None = None

    # ==========================
    # Groq
    # ==========================

    GROQ_API_KEY: str | None = None

    CHAT_MODEL: str
    VISION_MODEL: str

    # ==========================
    # Embeddings
    # ==========================

    EMBEDDING_MODEL: str

    # ==========================
    # Whisper
    # ==========================

    WHISPER_MODEL: str

    # ==========================
    # LangSmith
    # ==========================

    LANGCHAIN_API_KEY: str | None = None
    LANGCHAIN_PROJECT: str
    LANGCHAIN_TRACING_V2: bool

    # ==========================
    # Celery
    # ==========================

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # ==========================
    # Uploads
    # ==========================

    UPLOAD_DIR: str
    MAX_UPLOAD_SIZE_MB: int


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """
    return Settings()


settings = get_settings()