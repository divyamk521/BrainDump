"""
Main FastAPI application entry point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient
from sqlalchemy import text

from app.api import router as api_router
from app.core.config import settings
from app.core.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    print("\n==============================")
    print("Starting BrainDump API...")
    print("==============================\n")

    # PostgreSQL Connection Check
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))

        print("Connected to PostgreSQL ✓")

    except Exception as e:
        print(f"Failed to connect to PostgreSQL ✗\n{e}")

    # Qdrant Connection Check
    try:
        client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_API_KEY or None,
        )

        client.get_collections()

        print("Connected to Qdrant ✓")

    except Exception as e:
        print(f"Failed to connect to Qdrant ✗\n{e}")

    yield

    print("\nShutting down BrainDump API...\n")


app = FastAPI(
    title="BrainDump API",
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "ok",
        "version": "1.0.0",
    }


app.include_router(api_router)