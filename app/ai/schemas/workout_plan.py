from pydantic import BaseModel

class WorkoutPlanSchema(BaseModel):
    warmup: str
    main_workout: str
    cardio: str
    stretching: str