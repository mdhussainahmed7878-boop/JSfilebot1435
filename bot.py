from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

app = Client(
    "JS143_AutoFilterBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)

print("✅ Bot Starting...")

app.run()
