from app.states.user_profile import UserProfile
from app.constants.profile_questions import (
    AGE_QUESTION,
    HEIGHT_QUESTION,
    WEIGHT_QUESTION,
    GOAL_QUESTION,
    GENDER_QUESTION,
    ACTIVITY_QUESTION
)

PROFILE_STEPS = [
    {
        "field": "age",
        "question": AGE_QUESTION,
        "state": UserProfile.age,
        "next_state": UserProfile.height,
        "type": int,
    },
    {
        "field": "height",
        "question": HEIGHT_QUESTION,
        "state": UserProfile.height,
        "next_state": UserProfile.weight,
        "type": int,
    },
    {
        "field": "weight",
        "question": WEIGHT_QUESTION,
        "state": UserProfile.weight,
        "next_state": UserProfile.goal,
        "type": float,
    },
    {
        "field": "goal",
        "question": GOAL_QUESTION,
        "state": UserProfile.goal,
        "next_state": UserProfile.gender,
        "type": str,
    },
    {
        "field": "gender",
        "question": GENDER_QUESTION,
        "state": UserProfile.gender,
        "next_state": UserProfile.activity,
        "type": str,
    },
    {
        "field": "activity",
        "question": ACTIVITY_QUESTION,
        "state": UserProfile.activity,
        "next_state": None,
        "type": str,
    }
]