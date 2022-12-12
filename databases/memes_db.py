import asyncpg
import config
from asyncpg import Connection
from asyncpg.pool import Pool
from typing import Union

class Database():
    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None
    async def create(self):
        self.pool = await asyncpg.create_pool(
            database = config.DB_NAME,
            user = config.DB_USER,
            password = config.DB_PASSWORD,
            host = config.DB_HOST
        )
    async def execute(self, command, *args,
                        fetch = False,
                        fetchval = False,
                        fetchrow = False,
                        execute = False
                        ):
        async with self.pool.acquire() as connection:
            connection:Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result
    async def select_all_memes(self):
        sql = "SELECT * FROM telegram_memes ORDER BY file_type"
        return await self.execute(sql, fetch=True)
    async def select_memes_by_file_type(self, file_type):
        sql = f"SELECT * FROM telegram_memes WHERE file_type='{file_type}'"
        return await self.execute(sql, fetch=True)
    async def is_meme_in_list(self, file_id, file_type):
        sql = f"SELECT * FROM telegram_memes WHERE file_id='{file_id}' AND file_type='{file_type}'"
        return bool(await self.execute(sql, fetchrow=True))
    async def add_meme(self, file_id, file_type):
        if not (await self.is_meme_in_list(file_id, file_type)):
            sql = f"INSERT INTO telegram_memes VALUES('{file_id}', '{file_type}')"
            return await self.execute(sql, execute=True)
    async def delete_meme(self, file_id):
        sql = f"DELETE FROM telegram_memes WHERE file_id='{file_id}'"
        return await self.execute(sql, execute=True)