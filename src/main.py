import config
from config import DISCORD_BOT_KEY
import discord
import os
import asyncio
import discord
from bot import bot
import local_llm
    
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="Helping those in need :)")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await bot.tree.sync()
    print(f"Logged in as {bot.user.name}")

async def load():
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        print("loading local llm")
        local_llm.Local_LLM()
        await bot.start(DISCORD_BOT_KEY)
        
if __name__ == "__main__":
    asyncio.run(main())