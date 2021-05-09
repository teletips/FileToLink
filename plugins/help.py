import os

from pyrogram import Client, filters
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sampleconfig import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.command(['start', 'help']))
async def help_me(bot, message):
    if message.from_user.id == Config.ADMIN:
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    await bot.send_message(
        chat_id=message.chat.id,
        text=Presets.WELCOME_TEXT.format(info.first_name)
    )