from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import create_user_repo

async def create_user_service(session: AsyncSession, data: dict):
    return await create_user_repo(session, data)