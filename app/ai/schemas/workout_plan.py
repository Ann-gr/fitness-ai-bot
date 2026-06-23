from pydantic import BaseModel, field_validator, model_validator

class SetSchema(BaseModel):
    reps: int | None = None
    duration_seconds: int | None = None

    @field_validator("reps")
    def validate_reps(cls, reps):
        if reps is None: 
            return reps
        if reps <= 0:
            raise ValueError('Значение должно быть положительным')
        return reps
    
    @field_validator("duration_seconds")
    def validate_duration_seconds(cls, duration_seconds):
        if duration_seconds is None: 
            return duration_seconds
        if duration_seconds <= 0:
            raise ValueError('Значение должно быть положительным')
        return duration_seconds

    @model_validator(mode='after')
    def validate_set(self):
        if self.reps is not None and self.duration_seconds is not None:
            raise ValueError('Должно быть заполнено только одно поле')
        elif self.reps is None and self.duration_seconds is None:
            raise ValueError('Должно быть заполнено хотя бы одно поле')
        return self

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
    workout_recommendations: list[str]
    workout_days: list[WorkoutDaySchema]