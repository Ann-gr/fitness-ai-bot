from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings

# Создаём движок
engine = create_async_engine(
    settings.database_url,
    echo=True
)

async_session_factory = async_sessionmaker(engine)