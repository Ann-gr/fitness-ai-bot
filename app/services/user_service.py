from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import create_user_repo

async def create_user_service(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    age: int,
    height: int,
    weight: float,
    goal: str,
    gender: str,
    activity: str,
):
    return await create_user_repo(
        session=session,
        telegram_id=telegram_id,
        username=username,
        age=age,
        height=height,
        weight=weight,
        goal=goal,
        gender=gender,
        activity=activity,
    )