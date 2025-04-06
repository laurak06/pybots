import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('8169583052:AAE0UBfPwDUiqgey33P5lunWQ6_27bOxszg')


def get_time():
    response = requests.get('https://govzalla.com/ламазан-хенаш-время-молитв')

    dict_time = {}

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        times = soup.find_all('div', class_='col-6 col-md-4 col-lg-3 col-xl-2')
        for time in times:
            pray = time.find('div', class_='label').text.strip().lower()
            pray_time = time.find('h4').text
            dict_time[pray] = pray_time
        return dict_time
    else:
        return dict_time


@bot.message_handler(commands=['start'])
def start_cmd(message):
    keyboard = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Фаджр')
    button2 = types.KeyboardButton('Рассвет')
    button3 = types.KeyboardButton('Зухр')
    button4 = types.KeyboardButton('Аср')
    button5 = types.KeyboardButton('Магриб')
    button6 = types.KeyboardButton('Иша')
    keyboard.add(button1, button2, button3, button4, button5, button6)

    bot.reply_to(message, 'привет я бот и я могу показать время намаза', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def text_handler(message):
    dict_time = get_time()
    if dict_time.get(message.text.lower()):
        if message.text.lower() == 'фаджр':
            bot.reply_to(message, dict_time.get('фаджр'))
        elif message.text.lower() == 'рассвет':
            bot.reply_to(message, dict_time.get('рассвет'))
        elif message.text.lower() == 'зухр':
            bot.reply_to(message, dict_time.get('зухр'))
        elif message.text.lower() == 'аср':
            bot.reply_to(message, dict_time.get('аср'))
        elif message.text.lower() == 'магриб':
            bot.reply_to(message, dict_time.get('магриб'))
        elif message.text.lower() == 'иша':
            bot.reply_to(message, dict_time.get('иша'))
    else:
        bot.reply_to(message, 'Извините ничем не могу помочь')


bot.polling(non_stop=True)

