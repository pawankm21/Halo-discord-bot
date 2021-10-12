from os import environ
import discord
from discord.ext import commands
import logging

from discord.ext.commands.core import command

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)
bot = commands.Bot(command_prefix="$")

@bot.command()

bot.run(environ.get('BOT_KEY'))
