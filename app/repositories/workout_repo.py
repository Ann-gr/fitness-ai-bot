from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import WorkoutPlan

async def create_workout_plan(
    session: AsyncSession,
    plan: WorkoutPlan
) -> WorkoutPlan:
    session.add(plan)
    await session.flush()

    return plan