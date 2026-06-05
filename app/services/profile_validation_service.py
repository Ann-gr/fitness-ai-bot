from app.constants.profile_parameters import (
    ALLOWED_GOALS,
    ALLOWED_GENDERS,
    ALLOWED_ACTIVITIES,
    ALLOWED_TRAINING_PLACES,
    ALLOWED_TRAINING_TYPES,
    MIN_TRAINING_COUNT,
    MAX_TRAINING_COUNT,
    MIN_AGE,
    MAX_AGE,
    MIN_HEIGHT,
    MAX_HEIGHT,
    MIN_WEIGHT,
    MAX_WEIGHT
)

def validate_age(age: int) -> bool:
    return MIN_AGE <= age <= MAX_AGE

def validate_weight(weight: float) -> bool:
    return MIN_WEIGHT <= weight <= MAX_WEIGHT

def validate_height(height: int) -> bool:
    return MIN_HEIGHT <= height <= MAX_HEIGHT

def validate_goal(goal: str) -> bool:
    return goal.lower() in ALLOWED_GOALS

def validate_gender(gender: str) -> bool:
    return gender.lower() in ALLOWED_GENDERS

def validate_activity(activity: str) -> bool:
    return activity.lower() in ALLOWED_ACTIVITIES

def validate_training_places(training_place: str) -> bool:
    return training_place.lower() in ALLOWED_TRAINING_PLACES

def validate_training_types(training_type: str) -> bool:
    return training_type.lower() in ALLOWED_TRAINING_TYPES

def validate_training_counts(training_count: int) -> bool:
    return MIN_TRAINING_COUNT <= training_count <= MAX_TRAINING_COUNT