from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher(bot)
