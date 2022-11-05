from aiogram import types, Dispatcher
from database import read_exped
from create_bot import bot
from keyboards.client_kb import kb_client


async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет')


async def item_filter(message: types.Message):
    item = int(message.text)
    result = read_exped.filter_item(df=read_exped.exped, item=item)
    text = f'Заказ: *{result[0]}*\n' \
           f'Деталь: *{result[1]}*\n' \
           f'Кол-во: *{result[2]}*\n' \
           f'Дата отгрузки: *{result[3]}*\n' \
           f'ТП: *{result[5]}*\n' \
           f'Примечания: *{result[4]}*\n'
    await bot.send_message(message.from_user.id, text=text, parse_mode='Markdown')


async def detal_filter(message: types.Message):
    numder_detal = message.text
    result = read_exped.filter_detal(df=read_exped.exped, detal=numder_detal)
    for i in range(len(result)):
        text = f'Заказ: *{result[i][0]}*\n' \
               f'Деталь: *{result[i][1]}*\n' \
               f'Кол-во: *{result[i][2]}*\n' \
               f'Дата отгрузки: *{result[i][3]}*\n' \
               f'ТП: *{result[i][5]}*\n' \
               f'Примечания: *{result[i][4]}*\n'
        await bot.send_message(message.from_user.id, text=text, parse_mode='Markdown')


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(command_start, commands=['start, help'])
    dp_1.register_message_handler(item_filter)

