# 1
# GET - получение запроса
# POST - отправление данных в запрос
# DELETE - запрос на удаление
# PATCH - изменение данных в запросе
# PUT - изменение данных в запросе
# OPTION - просмотр доступных запросов

# 2
import requests
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
#
# for item in response.json():
#     print(item['title'])

# 3
#
# data = {
#     'username': 'ansar',
#     'password': '12345'
# }
#
# response = requests.post('https://httpbin.org/post', data=data)
# print(response.status_code)

# 4

from bs4 import BeautifulSoup
#
# response = requests.get('https://quotes.toscrape.com')
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# for a in soup.find_all('a'):
#     print(a['href'])
#
# 5
# response = requests.get('https://quotes.toscrape.com')
#
# html_content = BeautifulSoup(response.text, 'html.parser')
#
# print(html_content.find('h1').text.strip())

# 6
# import telebot
# from telebot_py.config import TOKEN
# from telebot import types
#
# bot = telebot.TeleBot(TOKEN)

#7
# @bot.message_handler(commands=['start'])
# def start(message: types.Message):
#     # bot.send_message(message.chat.id, 'you said start')
#
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='1 button', callback_data='1')
#     btn2 = types.InlineKeyboardButton(text='2 button', callback_data='2')
#     btn3 = types.InlineKeyboardButton(text='3 button', callback_data='3')
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id, 'choose button', reply_markup=markup)
#
#8
# @bot.message_handler(commands=['hello'])
# def start(message: types.Message):
#     # bot.reply_to(message, f'hello {message.from_user.first_name}')
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton(text='1 button')
#     btn2 = types.KeyboardButton(text='2 button')
#     btn3 = types.KeyboardButton(text='3 button')
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id, 'choose button', reply_markup=markup)
#
# bot.polling()

# 9
# основные отличия:
# pyrogram асинхронный, поэтому является гибким
# pyrogram нужен для того, чтобы бот мог являться как бы пользователем

# 10
# from pyrogram import Client
#
# from config import API_ID, API_HASH
#
# client = Client(name='bottt', api_id=API_ID, api_hash=API_HASH)
#
# client.send_message('123456789', 'Hello world!')


