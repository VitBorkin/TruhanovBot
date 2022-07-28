from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки клавиатуры панели администратора
button_load = KeyboardButton('/Добавить') # Добавить товар - ссылка в файле admin.py функция cm_start
button_delete = KeyboardButton('/Редактировать') #/Редактировать  - ссылка в файле admin.py функция delete_item
button_exit = KeyboardButton('/Выйти')
#TODO Подключить кнопку /Выйти, чтобы нажатием можно было выйти из панели администратора

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load, button_delete).add(button_exit)
