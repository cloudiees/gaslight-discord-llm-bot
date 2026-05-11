"""
Grabs the discord bot key from the .env file
"""
import dotenv
import os

DISCORD_BOT_KEY = ""

if not dotenv.load_dotenv():
    print(".env not found")
    exit()
else:
    DISCORD_BOT_KEY = os.getenv("DISCORD_BOT_KEY")
    if DISCORD_BOT_KEY is None or DISCORD_BOT_KEY == "":
        print("Discord botkey not found")
        exit()