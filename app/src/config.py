import os


class settings:
    DB_NAME = os.environ["DB_NAME"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_USER = os.environ["DB_USER"]

    DB_SYNC_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}"
    DB_ASYNC_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}"
