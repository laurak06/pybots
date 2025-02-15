import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from random import randint
from datetime import date

from aiobot.config import TOKEN, API
from parse_weather import parse
from database.models import createTable
from database.crud import insert_data, select_data


logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('reply_builder'))
async def handler_reply_builder(message: Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4) #строчки кнопок
    await message.answer('choose number: ', reply_markup=builder.as_markup())


@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text='pure')],
        [KeyboardButton(text='no pure')]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='choose')
    await message.answer('how to serve kotlety', reply_markup=keyboard)

@dp.message(F.text == 'pure')
async def text_handler_pure(message: Message):
    await message.answer('you chose pure')

@dp.message(F.text == 'no pure')
async def text_handler_pure(message: Message):
    await message.answer('you didnt chose pure :( sad')

# @dp.message()
# async def add_to_base(message: Message):
#     user = message.from_user
#     user_date = date.today()
#     insert_data(user.id, user_date)
#
#
# @dp.message(Command('start'))
# async def cmd_start(message: Message):
#     await message.answer('hello friend')
#
#
# @dp.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('help meee')
#
#
# @dp.message(Command('menu'))
# async def cmd_help(message: Message):
#     await message.answer('we have a lot of stuff!')
#
#
# @dp.message(Command('send_document'))
# async def cmd_document(message: Message):
#     choice = randint(0, 2)
#     if choice == 0:
#         await message.answer_document(document=FSInputFile('test.txt'))
#     elif choice == 1:
#         await message.answer_photo(photo=FSInputFile('img.png'))
#     else:
#         await message.answer_audio(audio=FSInputFile('zvuk.mp3'))
#
#
# @dp.message(F.photo)
# async def photo_handler(message: Message):
#     await bot.download(
#         message.photo[-1],
#         destination='image.png'
#     )
#
#
# @dp.message(F.text.lower() == 'погода')
# async def weather(message: Message):
#     await message.answer(await parse(API))
#
#
# @dp.message(F.text)
# async def answer_user(message: Message):
#     if message.text.lower() == 'привет':
#         await message.answer('добрый день')
#     elif message.text.lower() == 'как дела?':
#         await message.reply('все супер, а у вас?')
#     elif message.text.lower() == 'как тебя зовут?':
#         await message.answer(f'я бот!')
#     elif message.text.lower() == 'пока':
#         await message.answer('до свидания!')
#     elif message.text.lower() == 'users':
#         await message.answer(select_data())
#     else:
#         await message.answer(message.text)


async def main():
    # createTable()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())