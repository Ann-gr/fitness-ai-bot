from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from app.config import settings
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from app.handlers.__init__ import setup_routers
from aiogram.fsm.storage.memory import MemoryStorage

# создаём бота
bot = Bot(token=settings.bot_token)
# создаём диспетчер
dp = Dispatcher(storage=MemoryStorage())
# подключаем роуты
setup_routers(dp)
# вебхук
webhook_url = settings.base_webhook_url + settings.webhook_path

# установка webhook
async def on_startup():
    print("STARTUP")
    print(webhook_url)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_webhook(webhook_url)
        print("WEBHOOK SET")
        
    except Exception as e:
        print("❌ ERROR:", e)
        raise

@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()

    yield
    
# создаём веб-сервер
app = FastAPI(lifespan=lifespan)

# это URL, куда Telegram шлёт сообщения
@app.post(settings.webhook_path)
async def webhook(request: Request):
    print("WEBHOOK HIT")

    data = await request.json() # получаем JSON от Telegram
    print(data)

    update = Update.model_validate(data) # создаём Update object
    await dp.feed_update(bot, update) # отправляем update в диспетчер

    return "ok", 200