from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.redis import RedisStorage2
# from aiogram.contrib.fsm_storage.mongo import MongoStorage
from databases import Database
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
# the storage will save states of users
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()