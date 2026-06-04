from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из файла .env в окружение

class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOKEN")
    base_webhook_url: str = Field(..., env="BASE_WEBHOOK_URL")
    webhook_path: str = Field(..., env="WEBHOOK_PATH")
    database_url: str = Field(..., env="DATABASE_URL")
    openrouter_api_key: str = Field(..., env="OPENROUTER_API_KEY")
    openrouter_base_url: str = Field(..., env="OPENROUTER_BASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()