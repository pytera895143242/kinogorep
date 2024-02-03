import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '6426040462:AAHmJxZoipWH4KkpQ_y-UTZl7SpRgHeob94'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)

