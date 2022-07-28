from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# Ответ на команду /start и /help
# @dp.message_handler(commands=['start', 'help', 'Выйти'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в ЧатБот интернет магазина "БестФакер", что вы хотели узнать', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Truhanov_Bot')


# Ответ на команду /Режим_работы
# @dp.message_handler(commands=['Режим_работы'])
async def shop_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

# Ответ на команду /Расположение
# @dp.message_handler(commands=['Расположение'])
async def shop_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15, Гомель')#, reply_markup=ReplyKeyboardRemove()) # Удаляет кнопочный интерфейс пользователя

# Ответ на команду /Меню
# @dp.message_handler(commands=['Меню'])
async def shop_menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help', 'Выйти'])
    dp.register_message_handler(shop_open, commands=['Режим_работы'])
    dp.register_message_handler(shop_place, commands=['Расположение'])
    dp.register_message_handler(shop_menu, commands=['Меню'])

