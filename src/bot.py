"""
Initializes the discord bot
"""
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())