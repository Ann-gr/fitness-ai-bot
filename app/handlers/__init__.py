from aiogram import Dispatcher
from app.handlers.profile import router as profile_router
from app.handlers.fallback import router as fallback_router
from app.handlers.workout import router as workout_router

def setup_routers(dp: Dispatcher):
    dp.include_router(profile_router)
    dp.include_router(workout_router)
    dp.include_router(fallback_router)