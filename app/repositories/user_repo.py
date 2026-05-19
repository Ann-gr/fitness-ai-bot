from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User

async def create_user_repo(session: AsyncSession, user_data: dict):
    user = User(**user_data)

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user