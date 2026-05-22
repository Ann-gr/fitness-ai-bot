from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states.user_profile import UserProfile
from app.services.user_service import create_user_service
from app.services.profile_service import build_user_profile, is_adult
from app.schemas.user import UserProfileSchema
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import ValidationError

router = Router(name="profile")

@router.message(Command("start")) 
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Давай познакомимся, чтобы составить персонализированную тренировку. Сколько тебе лет?")
    await state.set_state(UserProfile.age)

@router.message(UserProfile.age) 
async def height_request(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Отлично, идём дальше! Какой у тебя рост?")
    await state.set_state(UserProfile.height)

@router.message(UserProfile.height)
async def weight_request(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await message.answer("Записал😉 Какой у тебя вес?")
    await state.set_state(UserProfile.weight)

@router.message(UserProfile.weight)
async def goal_request(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Хорошо идём! Какая у тебя цель? Например: похудение / набор массы / поддержание формы")
    await state.set_state(UserProfile.goal)

@router.message(UserProfile.goal)
async def gender_request(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer("Осталось всего пару вопросов! Укажи пол: мужчина / женщина")
    await state.set_state(UserProfile.gender)

@router.message(UserProfile.gender)
async def activity_request(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("И последний шаг! Укажи свой уровень активности: низкий / средний / высокий")
    await state.set_state(UserProfile.activity)

@router.message(UserProfile.activity)
async def save_profile(
    message: Message,
    state: FSMContext,
    session: AsyncSession,
):
    await state.update_data(activity=message.text)

    data = await state.get_data()
    try:
        validated_data = UserProfileSchema(**data)

    except ValidationError:
        await message.answer("Проверь, пожалуйста, корректность введённых данных.")
        return
    
    if not is_adult(validated_data.age):
        await message.answer("Для несовершеннолетних рекомендуется заниматься с тренером или родителями.")
        return
    
    profile = build_user_profile(message, validated_data)

    result = await create_user_service(
        session=session,
        profile=profile
    )

    if not result.success:
        if result.error == "USER_ALREADY_EXISTS":
            await message.answer("Профиль уже существует.")
            return
        await message.answer("Ошибка при создании профиля.")
        return
    
    await message.answer("Готово! 🎉 Твой профиль создан.")

    await state.clear()