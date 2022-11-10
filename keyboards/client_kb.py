from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = InlineKeyboardButton('Поиск по item', callback_data='but1')
b2 = InlineKeyboardButton('Поиск по детали', callback_data='but2')
b3 = InlineKeyboardButton('Поиск по заказу', callback_data='but3')

kb_client = InlineKeyboardMarkup(row_width=2).add(b1)
kb_client.add(b2)
kb_client.add(b3)
