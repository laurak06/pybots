from pyrogram import Client, filters
from pyrogram.types import Message

import time

from config import *

client = Client(name='My accounts', api_hash=API_HASH, api_id=API_ID)



@client.on_message(filters.command('type', prefixes='!') & filters.me)
def type_handler(client_object, message: Message):
    input_text = message.text.split('type', maxsplit=1)[1]
    temp_text = input_text
    edited_text = ''
    typing_symbol = '*'

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.05)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.05)
        except:
            print('Превышен лимит сообщений')


client.run()