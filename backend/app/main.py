# BrainDump/backend/app/main.py

"""
BrainDump FastAPI application.

Initializes the FastAPI app, configures the application
lifespan, verifies external service connectivity during
startup, and exposes the API endpoints.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient

from app.core.config import settings
from app.core.database import check_database_connection

# -------------------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------------------

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------
# Lifespan
# -------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    logger.info("Starting BrainDump API...")

    # -------------------------------------------------------------
    # PostgreSQL
    # -------------------------------------------------------------

    try:
        await check_database_connection()
        logger.info("Connected to PostgreSQL OK")

    except Exception as exc:
        logger.exception("Failed to connect to PostgreSQL")
        raise exc

    # -------------------------------------------------------------
    # Qdrant
    # -------------------------------------------------------------

    try:
        qdrant = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
        )

        qdrant.get_collections()

        logger.info("Connected to Qdrant OK")

    except Exception as exc:
        logger.exception("Failed to connect to Qdrant")
        raise exc

    logger.info("Application startup completed.")

    yield

    logger.info("Shutting down BrainDump API...")