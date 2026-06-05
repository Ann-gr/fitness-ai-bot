from dataclasses import dataclass

@dataclass
class UserProfileDTO:
    telegram_id: int
    username: str | None
    age: int
    height: int
    weight: float
    goal: str
    gender: str
    activity: str
    training_place: str
    training_type: str
    training_count: int