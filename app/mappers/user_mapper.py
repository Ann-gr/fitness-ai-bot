from app.database.models import User
from app.dto.user import UserProfileDTO

def to_user_profile_dto(
        user: User
) -> UserProfileDTO:
        return UserProfileDTO(
                telegram_id=user.telegram_id,
                username=user.username,
                age=user.age,
                height=user.height,
                weight=user.weight,
                goal=user.goal,
                gender=user.gender,
                activity=user.activity,
                training_place=user.training_place,
                training_type=user.training_type,
                training_count=user.training_count
        )