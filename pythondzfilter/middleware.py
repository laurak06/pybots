from aiogram import BaseMiddleware
from aiogram.types import Update, TelegramObject
from typing import Callable, Dict, Any, Awaitable


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Any:
        print(f'Processing update {event}')
        return await handler(event, data)

class SleepLoggingMiddleware(BaseMiddleware):