import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
DATABASE_URI = os.getenv("DATABASE_URI")

ADMINS = [int(x) for x in os.getenv("ADMINS", "").split() if x]

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))

FORCE_SUB_CHANNEL_1 = int(os.getenv("FORCE_SUB_CHANNEL_1", "0"))
FORCE_SUB_CHANNEL_2 = int(os.getenv("FORCE_SUB_CHANNEL_2", "0"))
