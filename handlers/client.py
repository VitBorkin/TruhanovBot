from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# Ответ на команду /start и /help
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в ЧатБот интернет магазина "БестФакер", что вы хотели узнать', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Truhanov_Bot')
# TODO Заполнить приветствие бота на команду /Start, справку после вызова команды /help и заполнить
#  информацию на Ботфазере.


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
# TODO 1. Оформить меню красиво, выделить жирным шрифтом заголовок и цену, добавить слово "рублей"
#  2. Добавить кнопки посмотреть товар и оплатить 3. Добавить вложенные списки товаров

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(shop_open, commands=['Режим_работы'])
    dp.register_message_handler(shop_place, commands=['Расположение'])
    dp.register_message_handler(shop_menu, commands=['Меню'])

# TODO 3. Добавить авторизацию на сайте через телеграм-бот
#  4. Добавить администрирование каналов на предмет ссылок на порносайты
#  5. Продумать что интересно дальнобойщикам: примеры - работа, обмен денег, сдача топлива,
#  продажа дальнобойных приблуд вроде чип-карт, цепей, раций и электроники.
#  6. Предусмотреть модульную структуру бота, когда каждый модуль выполняет свою функцию и может быстро подключаться
#  к другому боту или компиллироваться

#  TODO ИДЕИ для БОТОВ:
#   1. Бот-антиспам (скрытая функция рекламы)
#   2. Бот-антифлуд (скрытая функция рекламы)
#   3. Обменник валют
#   4. Магазин товаров для дальнобоя
#   5. Чат-бот, тренирующий произношение английского (платный), читающий тексты/подкасты, тренирующий в английском
#   6. Бот, мониторящий сайты по перевозкам/опту - кидающий заявки на перевозки или сопоставляющий
#   расценки на товары/работы с заранее заданными или сайтами, предлагающими обратное
#   8. Бот, мониторящий иностранные биржи труда, переводящий и бросающий заявки на сайты по найму персонала и
#   нанимателю с предложением о сотрудничестве
#   7. Бот-информатор погоды, курсов валют, гороскопов и прочего (посмотреть готовые модули по каждому направлению)




