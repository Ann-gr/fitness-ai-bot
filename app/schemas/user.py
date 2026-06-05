from pydantic import BaseModel

class UserProfileSchema(BaseModel):
    age: int
    height: int
    weight: float
    goal: str
    gender: str
    activity: str
    training_place: str
    training_type: str
    training_count: int