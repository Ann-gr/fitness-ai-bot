from openai import AsyncOpenAI
from app.config import settings 
from app.common.result import Result
from app.ai.constants.models import DEFAULT_MODEL

import logging
logger = logging.getLogger(__name__)

class OpenRouterClient:
    def __init__(self):
        # подключение к OpenRouter
        self.client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url
        )

    async def generate(
        self,
        messages: list[dict[str, str]],
        model: str = DEFAULT_MODEL,
    ) -> Result[str]:
        try:
            response = await self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            ai_response = response.choices[0].message.content
            if not ai_response:
                logger.warning("AI returned an empty response.")
                return Result(
                    success=False,
                    error="EMPTY_RESPONSE"
                )
            return Result(
                success=True,
                data = ai_response
            )
        except Exception:
            logger.exception(
                "OpenRouter request failed for model=%s.",
                model
            )
            return Result(
                    success=False,
                    error=f"OPENROUTER_ERROR"
            )

openrouter_client = OpenRouterClient()