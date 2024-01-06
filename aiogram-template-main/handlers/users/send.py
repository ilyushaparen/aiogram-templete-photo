from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from loader import dp,bot
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("test"))
async def send(message: types.Message):
    photo_id = ""
    video_id = ""
    await message.reply_photo(photo_id, caption="")
    await message.reply_video(video_id, caption="")


@dp.message_handler(Command("albom"))
async def book(message: types.Message):
    album = types.MediaGroup()
    photo_id = ""
    video_id = ""
    album.attach_photo(photo=photo_id)
    album.attach_video(video=video_id)

    await message.reply_media_group(media=album)


