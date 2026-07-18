from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text(
        "👋 Welcome!\n\nJS143 Auto Filter Bot Started Successfully."
    )
