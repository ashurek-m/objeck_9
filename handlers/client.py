from aiogram import types, Dispatcher
from database import read_exped
from create_bot import bot


async def echo_send(message: types.Message):
    await message.reply(message.text)
    await print_result(message)


async def item_filter(message: types.Message):
    item = int(message.text)
    exped = read_exped.exped
    result = read_exped.filter(df=exped, item=item)
    text = f'Заказ: {result[0]}\n' \
           f'Деталь: {result[1]}\n' \
           f'Кол-во: {result[2]}\n' \
           f'Дата отгрузки: {result[3]}\n' \
           f'ТП: {result[5]}\n' \
           f'Примечания: {result[4]}\n'
    await bot.send_message(message.from_user.id, text)


async def print_result(message: types.Message):
    pass


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(item_filter)

