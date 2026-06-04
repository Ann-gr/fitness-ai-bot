from app.ai.prompts.workout_prompt import build_workout_messages
from app.ai.clients.openrouter_client import openrouter_client
from app.ai.constants.models import DEFAULT_MODEL
from app.ai.schemas.workout_plan import WorkoutPlanSchema
from app.dto.user import UserProfileDTO
from app.common.result import Result
from pydantic import ValidationError
import json
import logging

logger = logging.getLogger(__name__)

async def generate_workout_plan(
    user: UserProfileDTO
) -> Result[WorkoutPlanSchema]:
    messages = build_workout_messages(user)
    ai_result = await openrouter_client.generate(messages, DEFAULT_MODEL)
    if not ai_result.success:
        return Result(
            success=False,
            error="WORKOUT_GENERATION_FAILED"
        )
    logger.info(ai_result.data)
    
    try: 
        json_result = json.loads(ai_result.data)
    except json.JSONDecodeError as e:
        logger.exception("Failed to parse workout JSON")
        return Result(
            success=False,
            error="INVALID_JSON"
        )
    
    try:
        workout_plan = WorkoutPlanSchema.model_validate(json_result)
        return Result(
            success=True,
            data=workout_plan
        )
    except ValidationError as e:
        logger.exception("Workout schema validation failed")
        return Result(
            success=False,
            error="INVALID_WORKOUT_SCHEMA"
        )