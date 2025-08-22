from config import settings
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, DeclarativeBase

db_url = settings.DB_URL
engine = create_engine(db_url)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

def tables_check():
    insperctor = inspect(engine)
    existing_tables = insperctor.get_table_names()
    
    if not existing_tables:
        Base.metadata.create_all(engine)
