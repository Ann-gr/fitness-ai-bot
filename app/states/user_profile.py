from aiogram.fsm.state import StatesGroup, State

class UserProfile(StatesGroup):
    age = State()
    height = State()
    weight = State()
    goal = State()
    gender = State()
    activity = State()
    training_place = State()
    training_type = State()
    training_count = State()