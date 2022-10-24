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
    await bot.send_message(message.from_user.id, result)


async def print_result(message: types.Message):
    pass


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(item_filter)

