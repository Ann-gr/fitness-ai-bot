from app.database.models import WorkoutPlanRecommendation, WorkoutDay, WorkoutExercise, ExerciseSet, WorkoutPlan
from app.ai.schemas import workout_plan as schemas

def map_exercise_set(
    exercise_set_schema: schemas.SetSchema,
    position: int
) -> ExerciseSet:
    return ExerciseSet(
        reps=exercise_set_schema.reps,
        duration_seconds=exercise_set_schema.duration_seconds,
        position=position
    )

def map_exercise_sets(
    exercise_sets: list[schemas.SetSchema]
) -> list[ExerciseSet]:
    return [
        map_exercise_set(exercise_set, position)
        for position, exercise_set in enumerate(exercise_sets, start=1)
    ]

def map_exercise(
    exercise_schema: schemas.ExerciseSchema,
    position: int
) -> WorkoutExercise:
    return WorkoutExercise(
        name=exercise_schema.name,
        rest_seconds=exercise_schema.rest_seconds,
        position=position,
        exercise_sets=map_exercise_sets(
            exercise_schema.sets
        )
    )

def map_exercises(
    exercises: list[schemas.ExerciseSchema]
) -> list[WorkoutExercise]:
    return [
        map_exercise(exercise, position)
        for position, exercise in enumerate(exercises, start=1)
    ]

def map_day(
    day_schema: schemas.WorkoutDaySchema,
    position: int
) -> WorkoutDay:
    return WorkoutDay(
        name=day_schema.name,
        goal=day_schema.goal,
        position=position,
        workout_exercises=map_exercises(
            day_schema.exercises
        )
    )

def map_days(
    days: list[schemas.WorkoutDaySchema]
) -> list[WorkoutDay]:
    return [
        map_day(day, position)
        for position, day in enumerate(days, start=1)
    ]

def map_recommendation(
    text: str, 
    position: int
) -> WorkoutPlanRecommendation:
    return WorkoutPlanRecommendation(
        text=text,
        position=position
    )

def map_recommendations(
    texts: list[str]
) -> list[WorkoutPlanRecommendation]:
    return [
        map_recommendation(text, position)
        for position, text in enumerate(texts, start=1)
    ]

def map_workout_plan(
    plan_schema: schemas.WorkoutPlanSchema
) -> WorkoutPlan:
    return WorkoutPlan(
        title=plan_schema.title,
        workout_recommendations=map_recommendations(
            plan_schema.recommendations
        ),
        workout_days=map_days(
            plan_schema.days
        )
    )