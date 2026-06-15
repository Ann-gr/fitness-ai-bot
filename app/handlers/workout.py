from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.services.workout_generation_service import generate_workout_plan
from app.ai.formatters.workout_formatter import format_workout_plan
from app.mappers.user_mapper import to_user_profile_dto
from app.services.user_service import get_user_service

router = Router(name="workout")

@router.message(Command("workout"))
async def start_workout_generation(message: Message, session: AsyncSession):
    telegram_id = message.from_user.id
    result = await get_user_service(session, telegram_id)
    if not result.success:
        await message.answer("Профиль пользователя не существует, создай его, отправив команду /start.")
        return
    
    user = result.data
    user_dto = to_user_profile_dto(user)
    generated_workout = await generate_workout_plan(user_dto)
    if not generated_workout.success:
        await message.answer("Произошла ошибка во время генерации, попробуй ещё раз.")
        return
        
    workout_plan = format_workout_plan(
        generated_workout.data
    )
    await message.answer("Готово! Ниже твой персонализированный план тренировок🤸🏻‍♂️")
    await message.answer(workout_plan)
    return