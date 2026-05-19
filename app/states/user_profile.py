from aiogram.fsm.state import StatesGroup, State

class UserProfile(StatesGroup):
    age = State()
    height = State()
    weight = State()
    goal = State()
    gender = State()
    activity = State()