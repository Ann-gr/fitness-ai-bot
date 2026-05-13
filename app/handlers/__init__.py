from aiogram import Dispatcher
from app.handlers.start import router

def setup_routers(dp: Dispatcher): # helper-function для модификации dispatcher
    dp.include_router(router)