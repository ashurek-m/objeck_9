from aiogram import types, Dispatcher


async def echo_send(message: types.Message):
    await message.reply(message.text)


async def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(echo_send())
