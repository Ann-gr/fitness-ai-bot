from app.states.user_profile import UserProfile
from app.constants.profile_questions import (
    AGE_QUESTION,
    HEIGHT_QUESTION,
    WEIGHT_QUESTION,
    GOAL_QUESTION,
    GENDER_QUESTION,
    ACTIVITY_QUESTION,
    TRAINING_PLACE_QUESTION,
    TRAINING_TYPE_QUESTION,
    TRAINING_COUNT_QUESTION
)
from app.services.profile_validation_service import (
    validate_age,
    validate_height,
    validate_weight,
    validate_goal,
    validate_gender,
    validate_activity,
    validate_training_places,
    validate_training_types,
    validate_training_counts
)

PROFILE_STEPS = [
    {
        "field": "age",
        "question": AGE_QUESTION,
        "state": UserProfile.age,
        "next_state": UserProfile.height.state,
        "type": int,
        "validator": validate_age,
        "error_message": "Допустимый возраст от 18 до 100 лет. Для несовершеннолетних рекомендуется заниматься с тренером или родителями."
    },
    {
        "field": "height",
        "question": HEIGHT_QUESTION,
        "state": UserProfile.height,
        "next_state": UserProfile.weight.state,
        "type": int,
        "validator": validate_height,
        "error_message": "Допустимый рост от 140 до 210 см."
    },
    {
        "field": "weight",
        "question": WEIGHT_QUESTION,
        "state": UserProfile.weight,
        "next_state": UserProfile.goal.state,
        "type": float,
        "validator": validate_weight,
        "error_message": "Допустимый вес от 40 до 150кг."
    },
    {
        "field": "goal",
        "question": GOAL_QUESTION,
        "state": UserProfile.goal,
        "next_state": UserProfile.gender.state,
        "type": str,
        "validator": validate_goal,
        "error_message": "Выбери цель из предложенных в примере."
    },
    {
        "field": "gender",
        "question": GENDER_QUESTION,
        "state": UserProfile.gender,
        "next_state": UserProfile.activity.state,
        "type": str,
        "validator": validate_gender,
        "error_message": "Выбери пол из предложенных в примере."
    },
    {
        "field": "activity",
        "question": ACTIVITY_QUESTION,
        "state": UserProfile.activity,
        "next_state": UserProfile.training_place.state,
        "type": str,
        "validator": validate_activity,
        "error_message": "Выбери активность из предложенных в примере."
    },
    {
        "field": "training_place",
        "question": TRAINING_PLACE_QUESTION,
        "state": UserProfile.training_place,
        "next_state": UserProfile.training_type.state,
        "type": str,
        "validator": validate_training_places,
        "error_message": "Выбери место из предложенных в примере."
    },
    {
        "field": "training_type",
        "question": TRAINING_TYPE_QUESTION,
        "state": UserProfile.training_type,
        "next_state": UserProfile.training_count.state,
        "type": str,
        "validator": validate_training_types,
        "error_message": "Выбери тип тренировки из предложенных в примере."
    },
    {
        "field": "training_count",
        "question": TRAINING_COUNT_QUESTION,
        "state": UserProfile.training_count,
        "next_state": None,
        "type": int,
        "validator": validate_training_counts,
        "error_message": "Выбери количество тренировок из предложенных в примере."
    }
]