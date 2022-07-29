from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

from handlers import client, admin, chat_moderation
from payments import payments

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
chat_moderation.register_handlers_other(dp)
payments.register_handlers_payment(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
