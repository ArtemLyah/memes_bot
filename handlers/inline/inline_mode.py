from dispatcher import dp, db
from aiogram import types
from asyncpg import Record

@dp.inline_handler(text="photo")
async def send_photo(query:types.InlineQuery):
    memes = await db.select_memes_by_file_type("photo")
    results = []
    for i, meme in enumerate(memes):
        results.append(
            types.InlineQueryResultCachedPhoto(
                id=str(i), 
                photo_file_id=meme["file_id"]
        ))
    await query.answer(results=results, cache_time=5)

@dp.inline_handler(text="video")
async def send_video(query:types.InlineQuery):
    memes = await db.select_memes_by_file_type("video")
    results = []
    for i, meme in enumerate(memes):
        results.append(
            types.InlineQueryResultCachedVideo(
                id=str(i), 
                title=meme["file_name"] if meme["file_name"] else "No name",
                video_file_id=meme["file_id"]
        ))
    await query.answer(results=results, cache_time=5)

@dp.inline_handler(text="audio")
async def send_audio(query:types.InlineQuery):
    memes = await db.select_memes_by_file_type("audio")
    results = []
    for i, meme in enumerate(memes):
        results.append(
            types.InlineQueryResultCachedAudio(
                id=str(i), 
                audio_file_id=meme["file_id"]
        ))
    await query.answer(results=results, cache_time=5)

@dp.inline_handler()
async def send_all(query:types.InlineQuery):
    memes = await db.select_all_memes() 
    results = []
    for i, meme in enumerate(memes):
        if meme["file_type"] == "photo":
            results.append(
                types.InlineQueryResultCachedPhoto(
                    id=str(i), 
                    photo_file_id=meme["file_id"]
            ))
        elif meme["file_type"] == "video":
            results.append(
                types.InlineQueryResultCachedVideo(
                    id = str(i), 
                    title = meme["file_name"] if meme["file_name"] else "No name",
                    video_file_id=meme["file_id"]
            ))
        elif meme["file_type"] == "audio":
            results.append(
                types.InlineQueryResultCachedAudio(
                    id=str(i), 
                    audio_file_id=meme["file_id"]
            ))
    await query.answer(results=results, cache_time=5)