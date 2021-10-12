from dotenv import load_dotenv
from os import environ
import discord
from discord.ext import commands

bot=commands.Bot()
load_dotenv()
print(environ.get("BOT_KEY"))
