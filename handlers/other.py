from aiogram import types, Dispatcher
from create_bot import dp
import json, string



# Фильтр на маты. Отслеживает нецензурную лексику и удаляет из групп, в которых является администратором
# и в которых ему даны права на удаление постов пользователей.
# В исполняемом файле должен быть в конце программы, но перед исполняющей командой.
# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Нецензурная лексика запрещена!')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)