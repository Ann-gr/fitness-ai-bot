from aiogram.types import Message
from app.dto.user import UserProfileDTO
from app.schemas.user import UserProfileSchema

def build_user_profile(
    message: Message, 
    data: UserProfileSchema
)-> UserProfileDTO:
    return UserProfileDTO(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        **data.model_dump()
    )

def is_adult(age: int) -> bool:
    return age >= 18