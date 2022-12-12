from aiogram import filters, types
from dispatcher import dp, db
from filters import IsFather

# handle private messages
@dp.message_handler(filters.CommandStart())
async def start(message:types.Message):
    await message.answer("Hello")

@dp.message_handler(IsFather(), content_types=types.ContentTypes.PHOTO)
async def photo_meme(message:types.Message):
    await db.add_meme(message.photo[-1].file_id, "photo")
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(IsFather(), content_types=types.ContentTypes.VIDEO)
async def video_meme(message:types.Message):
    await db.add_meme(message.video.file_id, "video")
    await message.reply(message.video.file_id)

@dp.message_handler(IsFather(), content_types=types.ContentTypes.AUDIO)
async def audio_meme(message:types.Message):
    await db.add_meme(message.audio.file_id, "audio")
    await message.reply(message.audio.file_id)

@dp.message_handler(IsFather(), filters.Command("delete"))
async def delete_meme(message:types.Message):
    file_id_to_delete = None
    reply_message = message.reply_to_message
    if reply_message.photo:
        file_id_to_delete = reply_message.photo[-1].file_id
    elif reply_message.video:
        file_id_to_delete = reply_message.video.file_id
    elif reply_message.audio:
        file_id_to_delete = reply_message.audio.file_id
    await db.delete_meme(file_id_to_delete)
    await reply_message.delete()
    await message.delete()