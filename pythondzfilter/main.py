import asyncio
from aiogram import Bot, Dispatcher
from handlers.generals import router
from database.models import make_table

from middleware import LoggingMiddleware

TOKEN = '8097411190:AAE4RmlNNmiEHV6K61xh2Xv64TBC-Z2TNaU'


async def main():
    make_table()
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.update.middleware(LoggingMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())