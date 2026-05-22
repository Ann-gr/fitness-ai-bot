from pydantic import BaseModel

class UserProfileSchema(BaseModel):
    age: int
    height: int
    weight: float
    goal: str
    gender: str
    activity: str