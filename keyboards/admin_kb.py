from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки клавиатуры панели администратора, обработчики в admin.py
button_load = KeyboardButton('/Добавить')
button_delete = KeyboardButton('/Редактировать')
button_exit = KeyboardButton('/Выйти')
cancel_button = KeyboardButton('/Отмена')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load, button_delete).add(button_exit)
cancel_adding = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_button)
