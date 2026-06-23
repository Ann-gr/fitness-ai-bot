from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.database.db import Base
from datetime import datetime

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
    workout_plans: Mapped[list["WorkoutPlan"]] = relationship(
		"WorkoutPlan",
		back_populates="user",
        cascade="all, delete-orphan"
    )

class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column( 
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    user: Mapped["User"] = relationship(
        "User",
        back_populates="workout_plans"
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )
    workout_days: Mapped[list["WorkoutDay"]] = relationship(
        "WorkoutDay",
		back_populates="workout_plan",
        cascade="all, delete-orphan",
        order_by="WorkoutDay.position"
    )
    workout_recommendations: Mapped[list["WorkoutPlanRecommendation"]] = relationship(
        "WorkoutPlanRecommendation",
		back_populates="workout_plan",
        cascade="all, delete-orphan",
        order_by="WorkoutPlanRecommendation.position"
    )

class WorkoutPlanRecommendation(Base):
    __tablename__ = "workout_plan_recommendations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    workout_plan_id: Mapped[int] = mapped_column( 
        ForeignKey(
            "workout_plans.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    workout_plan: Mapped["WorkoutPlan"]  = relationship(
        "WorkoutPlan",
        back_populates="workout_recommendations"
    )
    text: Mapped[str] = mapped_column(
        String(1024),
        nullable=False
    )
    position: Mapped[int] = mapped_column(nullable=False)

class WorkoutDay(Base):
    __tablename__ = "workout_days"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    workout_plan_id: Mapped[int] = mapped_column( 
        ForeignKey(
            "workout_plans.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    workout_plan: Mapped["WorkoutPlan"]  = relationship(
        "WorkoutPlan",
        back_populates="workout_days"
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    goal: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    position: Mapped[int] = mapped_column(nullable=False)
    workout_exercises: Mapped[list["WorkoutExercise"]] = relationship(
        "WorkoutExercise",
		back_populates="workout_day",
        cascade="all, delete-orphan",
        order_by="WorkoutExercise.position"
    )

class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    workout_day_id: Mapped[int] = mapped_column( 
        ForeignKey(
            "workout_days.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    workout_day: Mapped["WorkoutDay"]  = relationship(
        "WorkoutDay",
        back_populates="workout_exercises"
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    rest_seconds: Mapped[int] = mapped_column(
        nullable=False
    )
    position: Mapped[int] = mapped_column(nullable=False)
    exercise_sets: Mapped[list["ExerciseSet"]] = relationship(
        "ExerciseSet",
		back_populates="workout_exercise",
        cascade="all, delete-orphan",
        order_by="ExerciseSet.position"
    )

class ExerciseSet(Base):
    __tablename__ = "exercise_sets"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    workout_exercise_id: Mapped[int] = mapped_column( 
        ForeignKey(
            "workout_exercises.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
    workout_exercise: Mapped["WorkoutExercise"]  = relationship(
        "WorkoutExercise",
        back_populates="exercise_sets"
    )
    reps: Mapped[int | None] = mapped_column(
        nullable=True
    )
    duration_seconds: Mapped[int | None] = mapped_column(
        nullable=True
    )
    position: Mapped[int] = mapped_column(nullable=False)