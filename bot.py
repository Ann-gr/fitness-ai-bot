from flask import Flask, request
import asyncio
import os
from app.config import settings
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from app.handlers.__init__ import setup_routers

webhook_url = settings.base_webhook_url + settings.webhook_path

# создаём веб-сервер
app = Flask(__name__)
# создаём бота
bot = Bot(token=settings.bot_token)
# создаём диспетчер
dp = Dispatcher()
# подключаем роутеры
setup_routers(dp)
# это URL, куда Telegram шлёт сообщения
@app.post(settings.webhook_path)
async def webhook():
    print("WEBHOOK HIT")
    data = request.get_json() # получаем JSON от Telegram
    print(data)
    update = Update.model_validate(data) # создаём Update object
    await dp.feed_update(bot, update) # отправляем update в диспетчер

    return "ok", 200
# установка webhook
async def on_startup():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_webhook(webhook_url)
    except Exception as e:
        print("❌ ERROR:", e)
        raise

# запуск
if __name__ == "__main__":
    asyncio.run(on_startup())
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)