from aiogram import types, Dispatcher
from database import read_exped
from create_bot import bot, dp
from keyboards.client_kb import kb_client
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    item = State()
    detal = State()
    order = State()


async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello', reply_markup=kb_client)


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


async def my_id(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Ваш id {message.from_user.id}')


@dp.callback_query_handler(Text(startswith='but'), state=None)
async def button_inline(callback_query: types.CallbackQuery):
    res = callback_query.data.split('t')[1]
    if res == '1':
        await callback_query.message.answer('Выбран поиск по item')
        await FSMAdmin.item.set()
        await callback_query.answer()
    elif res == '2':
        await callback_query.message.answer('Нажата вторая кнопка')
        await callback_query.answer()
    elif res == '3':
        await callback_query.message.answer('Нажата третья кнопка')
        await callback_query.answer()

'''
@dp.message_handler(state=FSMAdmin.name)
async def save_data(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] =
'''


def register_handler_client(dp_1: Dispatcher):
    dp_1.register_message_handler(command_start, commands=['start', 'help'])
    dp_1.register_message_handler(my_id, commands=['id'])
    dp_1.register_message_handler(item_filter, state=FSMAdmin.item)
