import telebot
from telebot import types
from config import TOKEN, API
import logging


from weather_handler import parse

bot = telebot.TeleBot(TOKEN)


# type hinting
@bot.message_handler(commands=['start'])
def cmd_start(message: types.Message):
    bot.send_message(message.chat.id, 'Привет! Я - бот, показывающий погоду')


@bot.message_handler(commands=['help'])
def cmd_start(message: types.Message):
    bot.send_message(message.chat.id, 'Привет! Напиши название своего города :)')


@bot.message_handler(content_types=['text'])
def get_weather(message: types.Message):
    if message.text.lower() == 'weather':
        city = message.text.strip().lower()
        bot.reply_to(message, parse(city, API))

@bot.message_handler(commands=['menu'])
def menu_cmd(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Weather')
    btn2 = types.KeyboardButton(text='Current weather')
    btn3 = types.KeyboardButton(text='Wind')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text='Choose option:', reply_markup=keyboard)

@bot.message_handler(commands=['drinks'])
def cmd_drinks(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Кофе', callback_data='coffee')
    btn2 = types.InlineKeyboardButton(text='Чай', callback_data='tea')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Choose option:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: types.CallbackQuery):
    print(call)


bot.polling()