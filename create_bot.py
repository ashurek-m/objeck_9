from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher(bot, storage=storage)
