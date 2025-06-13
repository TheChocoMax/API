"""
Database utility module for asynchronous SQLAlchemy sessions.

This module sets up the asynchronous SQLAlchemy engine and sessionmaker for
database interactions. It provides a dependency function for obtaining a
database session in FastAPI endpoints.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql+asyncpg://postgres:S3cur3Str0ngP%40ss@172.17.0.1:5432/chocomax"
)
engine = create_async_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    """
    Dependency that provides a SQLAlchemy asynchronous database session.

    Yields:
        AsyncSession: An active SQLAlchemy async session for database operations.

    Usage:
        Use as a dependency in FastAPI endpoints to access the database.
    """
    async with SessionLocal() as session:
        yield session
