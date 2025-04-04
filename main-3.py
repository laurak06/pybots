import requests
from bs4 import BeautifulSoup
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('8169583052:AAE0UBfPwDUiqgey33P5lunWQ6_27bOxszg')
# @bot.message_handler(commands=['start'])
# def start_cmd(messatge):
#     keyboard = types.ReplyKeyboardMarkup()
#     button1 = types.KeyboardButton('Фаджр')
#     button2 = types.KeyboardButton('Рассвет')
#     button3 = types.KeyboardButton('Зухр')
#     button4 = types.KeyboardButton('Аср')
#     button5 = types.KeyboardButton('Магриб')
#     button6 = types.KeyboardButton('Иша')
#     keyboard.add(button1, button2, button3, button4, button5, button6)
#
#     bot.reply_to(messatge, 'привет я бот и я могу показать время намаза', reply_markup=keyboard)
#
# @bot.message_handler(func=lambda message: True)
# def text_handler(message):
#     if message.text.lower() == 'фаджр':
#         bot.reply_to(message, 'tim')
#     elif message.text.lower() == 'рассвет':
#         bot.reply_to(message, 'tim')
#     elif message.text.lower() == 'зухр':
#         bot.reply_to(message, 'tim')
#     elif message.text.lower() == 'аср':
#         bot.reply_to(message, 'tim')
#     elif message.text.lower() == 'магриб':
#         bot.reply_to(message, 'tim')
#     elif message.text.lower() == 'иша':
#         bot.reply_to(message, 'tim')
#     else:
#         bot.reply_to(message, 'Извините не чем не могу помочь')
#
# bot.polling(non_stop=True)

data = [{
    'label': 'h4'
}]
response = requests.get('https://govzalla.com/%D0%BB%D0%B0%D0%BC%D0%B0%D0%B7%D0%B0%D0%BD-%D1%85%D0%B5%D0%BD%D0%B0%D1%88-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D0%BC%D0%BE%D0%BB%D0%B8%D1%82%D0%B2')

soup = BeautifulSoup(response.text, 'lxml')

time = soup.find_all('div', cllas_='col-6 col-md-4 col-lg-3 col-xl-2')
for tim in time:
    time = tim.find('h4', cllas_='col-6 col-md-4 col-lg-3 col-xl-2')
print(time)