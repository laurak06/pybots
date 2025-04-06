import telebot
from telebot import types

bot = telebot.TeleBot('7573242723:AAH5vsZfEFjNntl3gSyxJPlWALn9MYwMg-c')


@bot.message_handler(commands=['start'])
def start_cmd(message):
    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Бургеры')
    button2 = types.KeyboardButton('Пицца')
    button3 = types.KeyboardButton('Роллы')
    keyboard.add(button1, button2, button3, row_width=2)

    bot.reply_to(message, 'Привет! я-бот', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_cmd(message):
    bot.send_message(message.chat.id, 'Вам нужна помощь? Можете посмотреть данные')


@bot.message_handler(func=lambda message: True)
def text_handler(message):
    if message.text.lower() == 'бургеры':
        bot.reply_to(message, 'В маке вкусные бургеры')
    elif message.text.lower() == 'пицца':
        bot.reply_to(message, 'в папа джонс вкусная пицца')
    elif message.text.lower() == 'роллы':
        bot.reply_to(message, 'Роллы в Японии самые вкусные')
    else:
        bot.reply_to(message, 'Извините, я не могу ничего посоветовать')


bot.polling(none_stop=True)