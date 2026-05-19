from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.states.user_profile import UserProfile
from app.services.user_service import create_user_service
from app.database.db import async_session_factory
from sqlalchemy.ext.asyncio import AsyncSession

router = Router(name="profile")

@router.message(Command("start")) 
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Давай познакомимся, чтобы составить персонализированную тренировку. Сколько тебе лет?")
    await state.set_state(UserProfile.age)

@router.message(UserProfile.age) 
async def height_request(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer("Отлично, идём дальше! Какой у тебя рост?")
    await state.set_state(UserProfile.height)

@router.message(UserProfile.height)
async def weight_request(message: Message, state: FSMContext):
    await state.update_data(height=int(message.text))
    await message.answer("Записал😉 Какой у тебя вес?")
    await state.set_state(UserProfile.weight)

@router.message(UserProfile.weight)
async def goal_request(message: Message, state: FSMContext):
    await state.update_data(weight=float(message.text))
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
async def save_profile(message: Message, state: FSMContext):
    await state.update_data(activity=message.text)

    data = await state.get_data()

    async with async_session_factory() as session:
        await create_user_service(session, data)

    await message.answer("Готово! 🎉 Твой профиль создан.")
    await state.clear()