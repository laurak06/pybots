from aiogram.filters import BaseFilter
from aiogram.types import Message


class PythonMsgFilter(BaseFilter):
    def __init__(self, word: str):
        self.word = word

    async def __call__(self, message: Message) -> bool:
        return self.word.lower() in message.text.lower()


