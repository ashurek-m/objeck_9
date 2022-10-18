from aiogram.utils import executor
from create_bot import dp

executor.start_polling(dp, skip_updates=True)
