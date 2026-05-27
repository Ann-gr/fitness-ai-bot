from app.states.user_profile import UserProfile
from app.constants.profile_questions import (
    AGE_QUESTION,
    HEIGHT_QUESTION,
    WEIGHT_QUESTION,
    GOAL_QUESTION,
    GENDER_QUESTION,
    ACTIVITY_QUESTION
)
from app.services.profile_validation_service import (
    validate_age,
    validate_height,
    validate_weight,
    validate_goal,
    validate_gender,
    validate_activity
)

PROFILE_STEPS = [
    {
        "field": "age",
        "question": AGE_QUESTION,
        "state": UserProfile.age,
        "next_state": UserProfile.height.state,
        "type": int,
        "validator": validate_age,
    },
    {
        "field": "height",
        "question": HEIGHT_QUESTION,
        "state": UserProfile.height,
        "next_state": UserProfile.weight.state,
        "type": int,
        "validator": validate_height,
    },
    {
        "field": "weight",
        "question": WEIGHT_QUESTION,
        "state": UserProfile.weight,
        "next_state": UserProfile.goal.state,
        "type": float,
        "validator": validate_weight,
    },
    {
        "field": "goal",
        "question": GOAL_QUESTION,
        "state": UserProfile.goal,
        "next_state": UserProfile.gender.state,
        "type": str,
        "validator": validate_goal,
    },
    {
        "field": "gender",
        "question": GENDER_QUESTION,
        "state": UserProfile.gender,
        "next_state": UserProfile.activity.state,
        "type": str,
        "validator": validate_gender,
    },
    {
        "field": "activity",
        "question": ACTIVITY_QUESTION,
        "state": UserProfile.activity,
        "next_state": None,
        "type": str,
        "validator": validate_activity,
    }
]