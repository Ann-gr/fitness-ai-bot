from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User

async def create_user_repo(
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
    user = User(
        telegram_id=telegram_id,
        username=username,
        age=age,
        height=height,
        weight=weight,
        goal=goal,
        gender=gender,
        activity=activity,
    )

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user