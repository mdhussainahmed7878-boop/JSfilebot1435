from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URI

client = AsyncIOMotorClient(DATABASE_URI)

db = client["JS143_BOT"]

users = db["users"]
files = db["files"]
links = db["links"]
messages = db["messages"]
