from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base

class User(Base):
    __tablename__ = "users"  # имя таблицы в БД

    # Поля (колонки)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None] = mapped_column(String(50), nullable=True)
    age: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
    weight: Mapped[float] = mapped_column()
    goal: Mapped[str] = mapped_column(String(20))
    gender: Mapped[str] = mapped_column(String(10))
    activity: Mapped[str] = mapped_column(String(20))
    training_place: Mapped[str] = mapped_column(String(100))
    training_type: Mapped[str] = mapped_column(String(100))
    training_count: Mapped[int] = mapped_column()