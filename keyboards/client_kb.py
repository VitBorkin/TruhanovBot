from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_client.add(b1).add(b2).insert(b3)#.row(b4, b5) # add - кнопка, размером в строку, insert - кнопка на той же сроке, если влазит, row - кнопки на одной строке
# kb_client.row(b1, b2, b3)


# Инлайн клавиатура к заказу
menu_panel = InlineKeyboardMarkup(row_width=2)
buy = InlineKeyboardButton(text='🛒Заказать', callback_data='pay')
describe = InlineKeyboardButton(text='🧾Описание', callback_data='')

menu_panel.add(describe, buy)

