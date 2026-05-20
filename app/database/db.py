from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

class Base(DeclarativeBase):
    pass

# Создаём движок
engine = create_async_engine(
    settings.database_url,
    echo=True,
    connect_args={
        "statement_cache_size": 0
    }
)

async_session_factory = async_sessionmaker(
    engine, 
    expire_on_commit=False
)