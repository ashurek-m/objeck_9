from aiogram import types, Dispatcher
from database import read_exped
from create_bot import bot


async def echo_send(message: types.Message):
    await message.reply(message.text)
    await print_result(message)


async def item_filter(message: types.Message):
    item = int(message)
    exped = read_exped.exped
    result = read_exped.filter(df=exped, item=item)
    order = result.loc[0, ['Индекс RTB']]
    await message.reply(order)

async def print_result(message: types.Message):
    await bot.send_message(message.from_user.id, text="привет")


def register_handler_client(dp_1: Dispatcher):
    #dp_1.register_message_handler(item_filter)
    dp_1.register_message_handler(echo_send)
