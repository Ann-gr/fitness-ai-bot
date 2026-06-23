from app.ai.schemas.workout_plan import WorkoutPlanSchema

def format_workout_plan(
    plan: WorkoutPlanSchema
) -> list[str]:
    workout_plan = []

    workout_title = plan.title
    workout_plan.append(f"📋 План: {workout_title}")

    workout_plan.append("")

    workout_recommendations = plan.workout_recommendations
    if workout_recommendations:
        workout_plan.append("📌 Рекомендации:")
        for workout_recommendation in workout_recommendations:
            workout_plan.append(f"• {workout_recommendation}")

    workout_plan.append("")

    workout_days = plan.workout_days
    for workout_day in workout_days:
        workout_name = workout_day.name
        workout_plan.append(f"🏋 {workout_name}")
        
        workout_goal = workout_day.goal
        workout_plan.append(f"🎯 Цель: {workout_goal}")

        workout_plan.append("")

        exercises = workout_day.exercises
        for exercise in exercises:
            exercise_name = exercise.name
            workout_plan.append(f"💪 {exercise_name}")

            exercise_rest_seconds = exercise.rest_seconds
            workout_plan.append(f"⏰ Отдых между подходами: {exercise_rest_seconds} сек.")

            workout_plan.append("")

            sets = exercise.sets
            for n, exercise_set in enumerate(sets, start=1):
                set_reps = exercise_set.reps
                set_duration_seconds = exercise_set.duration_seconds
                if set_duration_seconds:
                    workout_plan.append(f"Подход {n}: {set_duration_seconds} сек.")
                elif set_reps:
                    workout_plan.append(f"Подход {n}: {set_reps} повторений")
            
        workout_plan.append("")

    return "\n".join(workout_plan) 