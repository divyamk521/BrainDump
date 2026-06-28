# BrainDump/backend/app/core/database.py

"""
Database configuration for BrainDump.

This module configures the asynchronous SQLAlchemy engine,
session factory, declarative base, and provides utilities
for dependency injection and database health checks.
"""

from collections.abc import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    pass


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Yield an asynchronous database session.

    This dependency is used in FastAPI routes and services.
    """

    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def check_database_connection() -> bool:
    """
    Verify that PostgreSQL is reachable.

    Returns:
        bool: True if the connection succeeds.

    Raises:
        Exception: Re-raises any database connection error.
    """

    async with engine.begin() as connection:
        await connection.execute(text("SELECT 1"))

    return True