from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

class GetDBUserMiddleware(BaseMiddleware):
    # name function on_process_ -> use needed handler (message_handler, callback_query_handler, ...)
    async def on_process_message(self, message:types.Message, data:dict):
        pass
    async def on_process_callback_query(self, query:types.CallbackQuery, data:dict):
        pass