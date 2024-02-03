from aiogram import executor
from misc import dp
import handlers
import asyncio
from handlers.register_stat import while_stat


async def on_startup(x):
    asyncio.create_task(while_stat())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)