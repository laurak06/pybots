from aiogram.filters import BaseFilter
from aiogram.types import Message


class TimeMsgFilter(BaseFilter):
    def __init__(self, start: str, end: str):
        self.start = float(start.replace(':', '.'))
        self.end = float(end.replace(':', '.'))

    async def __call__(self, message: Message) -> bool:
        return self.start <= message.date.hour < self.end

