from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.workout_repo import create_workout_plan
from app.ai.schemas.workout_plan import WorkoutPlanSchema
from app.database.models import WorkoutPlan
from app.mappers.workout_mapper import map_workout_plan
from app.common.result import Result

async def save_workout_plan(
    session: AsyncSession,
    user_id: int,
    plan_schema: WorkoutPlanSchema
) -> Result[WorkoutPlan]:
    plan = map_workout_plan(plan_schema)
    plan.user_id = user_id

    try: 
        saved_plan = await create_workout_plan(
            session=session,
            plan=plan
        )
        await session.commit()
        await session.refresh(saved_plan)

    except Exception as e:
        print(e)
        await session.rollback()

        return Result(
            success=False,
            error="DATABASE_ERROR"
        )

    return Result(
        success=True,
        data=saved_plan
    )