from aiogram.dispatcher import filters
from aiogram import types
from config import father_id

# creating filters we must to create a method check
# this method will be check a message on a certain condition
# BoundFilter - main class of filters
# result must be Boolean
class IsFather(filters.BoundFilter):
    async def check(self, message:types.Message) -> bool:
        return message.from_user.id == father_id