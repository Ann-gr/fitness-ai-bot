from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user_repo import create_user_repo, get_user_by_telegram_id
from app.dto.user import UserProfileDTO
from app.common.result import Result
from app.database.models import User

async def create_user_service(
    session: AsyncSession,
    profile: UserProfileDTO
) -> Result[User]:
    
    existing_user = await get_user_by_telegram_id(session, profile.telegram_id)

    if not existing_user:
        try: 
            user = await create_user_repo(
                session=session,
                profile=profile,
            )
            await session.commit()

        except Exception:
            await session.rollback()
            return Result(
                success=False,
                error="DATABASE_ERROR"
            )

        return Result(
            success=True,
            data = user
        )
    
    return Result(
        success=False,
        error="USER_ALREADY_EXISTS"
    )