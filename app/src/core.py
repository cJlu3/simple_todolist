from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

sync_engine = create_engine(
    url=settings.DB_SYNC_URL,
    echo=False,
    pool_size=5,
    max_overflow=10,
)
sync_session_factory = sessionmaker(sync_engine)

async_engine = create_async_engine(
    url=settings.DB_ASYNC_URL,
    echo=False,
)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass


def tables_check():
    inspector = inspect(sync_engine)
    existing_tables = inspector.get_table_names()

    if not existing_tables:
        Base.metadata.create_all(sync_engine)
