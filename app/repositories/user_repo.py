from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import User
from app.dto.user import UserProfileDTO

async def create_user_repo(
    session: AsyncSession,
    profile: UserProfileDTO,
):
    user = User(
        telegram_id=profile.telegram_id,
        username=profile.username,
        age=profile.age,
        height=profile.height,
        weight=profile.weight,
        goal=profile.goal,
        gender=profile.gender,
        activity=profile.activity,
    )

    session.add(user)
    await session.flush()
    await session.refresh(user)

    return user

async def get_user_by_telegram_id(
        session: AsyncSession, 
        telegram_id: int
) -> User | None:
    stmt = select(User).where(User.telegram_id == telegram_id)
    result = await session.execute(stmt)

    return result.scalar_one_or_none()