from aiogram import executor

from dispatcher import dp, db
from middlewares.user_middleware import GetDBUserMiddleware
from utils.set_bot_commands import set_default_commands

import filters
import handlers

async def on_startup(dp):
    await set_default_commands(dp)
    await db.create()
    dp.middleware.setup(GetDBUserMiddleware())
    print("OK")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


