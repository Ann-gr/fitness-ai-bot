from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import ValidationError

from app.constants.profile_steps import PROFILE_STEPS
from app.schemas.user import UserProfileSchema
from app.services.profile_flow_service import get_step_by_state
from app.services.profile_service import build_user_profile, is_adult
from app.services.user_service import create_user_service
from app.states.user_profile import UserProfile

import logging

router = Router(name="profile")
logger = logging.getLogger(__name__)

@router.message(Command("start"))
async def start_profile(message: Message, state: FSMContext):
    step = PROFILE_STEPS[0]

    await state.set_state(step["state"])
    await message.answer(step["question"])

@router.message(StateFilter(UserProfile.age, UserProfile.height, UserProfile.weight, UserProfile.goal, UserProfile.gender, UserProfile.activity))
async def profile_flow(message: Message, state: FSMContext, session: AsyncSession):
    logger.info(
        "Profile flow started for user_id=%s",
        message.from_user.id
    )
    current_state = await state.get_state()
    current_step = get_step_by_state(current_state)

    if not current_step:
        await message.answer("Что-то пошло не так. Начни заново /start")
        return

    # парсим значение
    try:
        value = current_step["type"](message.text)
    except ValueError:
        await message.answer("Некорректный формат. Попробуй ещё раз.")
        return
    
    is_valid = current_step["validator"](value)

    if not is_valid:
        await message.answer(current_step["error_message"])
        return

    # сохраняем ответ
    await state.update_data({current_step["field"]: value})

    # следующий шаг
    next_step = get_step_by_state(current_step["next_state"])

    # если шаги закончились → создаём профиль
    if next_step is None:
        data = await state.get_data()

        try:
            logger.info(await state.get_state())
            logger.info(await state.get_data())
            validated_data = UserProfileSchema(**data)
        except ValidationError as e:
            logger.exception("Validation error")
            await message.answer("Проверь, пожалуйста, корректность данных.")
            return
        
        profile = build_user_profile(message, validated_data)

        logger.info("BEFORE CREATE USER")
        result = await create_user_service(
            session=session,
            profile=profile
        )
        logger.info("AFTER CREATE USER")

        if not result.success:
            await message.answer("Профиль уже существует.")
            await state.clear()
            return
        
        await message.answer("Готово! 🎉 Профиль создан.")
        await state.clear()
        return
    
    await state.set_state(next_step["state"])
    await message.answer(next_step["question"])