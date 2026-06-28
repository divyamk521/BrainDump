# BrainDump/backend/app/core/config.py

"""
Application configuration.

All settings are loaded from the project's .env file using
Pydantic Settings. This module provides a single Settings
instance that can be imported throughout the application.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================================================
    # Application
    # ==========================================================

    APP_NAME: str = "BrainDump API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ==========================================================
    # PostgreSQL
    # ==========================================================

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: str

    # ==========================================================
    # Redis
    # ==========================================================

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    REDIS_URL: str

    # ==========================================================
    # Celery
    # ==========================================================

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # ==========================================================
    # Qdrant
    # ==========================================================

    QDRANT_HOST: str
    QDRANT_PORT: int
    QDRANT_GRPC_PORT: int
    QDRANT_COLLECTION: str

    # ==========================================================
    # Groq
    # ==========================================================

    GROQ_API_KEY: str

    CHAT_MODEL: str
    VISION_MODEL: str
    FAST_MODEL: str

    # ==========================================================
    # JWT
    # ==========================================================

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ==========================================================
    # Embeddings
    # ==========================================================

    EMBEDDING_MODEL: str
    VECTOR_SIZE: int

    # ==========================================================
    # Retrieval
    # ==========================================================

    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    TOP_K: int
    RERANK_TOP_K: int

    # ==========================================================
    # Storage
    # ==========================================================

    UPLOAD_DIR: str

    # ==========================================================
    # OCR
    # ==========================================================

    TESSERACT_CMD: str = ""

    # ==========================================================
    # Whisper
    # ==========================================================

    WHISPER_MODEL: str

    # ==========================================================
    # LangSmith
    # ==========================================================

    LANGCHAIN_TRACING_V2: bool = False
    LANGCHAIN_API_KEY: str = ""
    LANGCHAIN_PROJECT: str = "BrainDump"

    # ==========================================================
    # Logging
    # ==========================================================

    LOG_LEVEL: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.

    The settings object is created only once and reused
    throughout the application's lifetime.
    """
    return Settings()


settings = get_settings()