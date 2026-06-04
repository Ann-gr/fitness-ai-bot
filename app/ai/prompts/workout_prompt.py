from app.dto.user import UserProfileDTO

def build_workout_messages(
    user: UserProfileDTO
) -> list[dict[str, str]]:
    messages = [
        {"role": "system", 
         "content": "Ты — персональный фитнес-тренер, твоя задача — проанализировать данные пользователя и составить персонализированный план тренировок с учетом указанных пользователем параметров и ограничений. Отвечай кратко и структурированно только по теме спорта. Опирайся на доказательные базы упражнений, обязательно уточняй технику и все нюансы, во избежание травм. Верни ответ СТРОГО в формате JSON. Используй только следующие поля:\n"
         "warmup\n"
         "main_workout\n"
         "cardio\n"
         "stretching\n"
         "Каждое поле должно содержать строку. Не добавляй пояснений. Не используй markdown. Не оборачивай ответ в ```json. Верни только JSON объект."},
        {"role": "user", "content":
            f"Возраст: {user.age}\n"
            f"Рост: {user.height}\n"
            f"Вес: {user.weight}\n"
            f"Цель: {user.goal}\n"
            f"Пол: {user.gender}\n"
            f"Уровень активности: {user.activity}\n"}
    ]
    return messages