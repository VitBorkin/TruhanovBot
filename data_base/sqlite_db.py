import sqlite3 as sq
from create_bot import bot
from keyboards.client_kb import menu_panel
from aiogram import types


def sql_start():
    global base, cur
    base = sq.connect('goods_for_sale.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'<b>{ret[1]}</b>\nОписание:<i> {ret[2]}</i>\n'
                             f'<u>Цена {ret[-1]} рублей.</u>\n<a href="https://t.me/Truhanov_Bot">перейти в магазин</a>',
                             reply_markup=menu_panel, parse_mode=types.ParseMode.HTML)


async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
