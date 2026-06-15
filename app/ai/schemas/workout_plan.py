from pydantic import BaseModel

class SetSchema(BaseModel):
    reps: int | None = None
    duration_seconds: int | None = None

class ExerciseSchema(BaseModel):
    name: str
    rest_seconds: int
    sets: list[SetSchema]

class WorkoutDaySchema(BaseModel):
    name: str
    goal: str
    exercises: list[ExerciseSchema]

class WorkoutPlanSchema(BaseModel):
    title: str
    recommendations: list[str]
    workouts: list[WorkoutDaySchema]