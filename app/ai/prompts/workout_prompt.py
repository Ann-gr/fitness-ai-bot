from app.dto.user import UserProfileDTO

JSON_FORMAT = """
{
  "title": "string",
  "recommendations": [
    "...",
    "..."
  ],
  "workouts": [
    {
      "name": "string",
      "goal": "string",
      "exercises": [
        {
          "name": "string",
          "rest_seconds": 90,
          "notes": "string",
          "sets": [
            {
              "reps": 12
            }
          ]
        }
      ]
    }
  ]
}

Все обязательные поля должны присутствовать.

Для каждого упражнения обязательно указывай:
- sets
- rest_seconds тоже обязателен, но если отдых не предусмотрен, укажи 0.

Для каждого подхода обязательно указывай хотя бы одно из:
- reps
- duration_seconds
Важно: ровно одно из двух полей должно быть заполнено.

Не пропускай поля.
Не изменяй структуру JSON.
"""

SYSTEM_PROMPT = f"""
Ты опытный персональный фитнес-тренер.

Твоя задача:
- составить безопасный план тренировок;
- учитывать опыт пользователя;
- учитывать цель пользователя;
- учитывать доступное оборудование;
- учитывать количество тренировок в неделю.

Верни только JSON в формате: 
{JSON_FORMAT}.

Не используй markdown.
Не добавляй пояснения вне JSON.
"""

def build_workout_messages(
    user: UserProfileDTO
) -> list[dict[str, str]]:
    messages = [
        {"role": "system", 
         "content": SYSTEM_PROMPT},
        {"role": "user", "content":
            f"Возраст: {user.age}\n"
            f"Рост: {user.height}\n"
            f"Вес: {user.weight}\n"
            f"Цель: {user.goal}\n"
            f"Пол: {user.gender}\n"
            f"Уровень активности: {user.activity}\n"
            f"Место тренировки: {user.training_place}\n"
            f"Тип тренировки: {user.training_type}\n"
            f"Количество тренировок в неделю: {user.training_count}\n"}
    ]
    return messages