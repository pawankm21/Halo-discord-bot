from discord import channel, client
from discord.ext.commands.core import guild_only
from dotenv import load_dotenv
from os import environ
import random
import discord
from discord.ext import commands
from math import floor
from jokes import jokes
from info import REPLY
load_dotenv()


intents = discord.Intents.all()
discord.member = True
bot = commands.Bot(command_prefix="%",intents=intents)
# events


@bot.event
async def on_ready():
    """
    prints READY on ready
    """
    print("READY")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(environ.get("WELCOME")))
    await channel.send(f"{member} Welcome my friend😀")
    


@bot.event
async def on_message(message):
    """
    Event triggered on message
    """
    if(message.author == bot.user):
        return
    if bot.user in message.mentions:
        await bot.get_channel(message.channel.id).send(random.choice(REPLY)+"🤖")
    await bot.process_commands(message)


@bot.event
async def on_member_remove(member):
    """
    Event triggered when member is removed
    """
    channel = bot.get_channel(int(environ.get("WELCOME")))
    await channel.send(f"{member} left the server.😔")
    

# Commands


@bot.command()
async def delete(ctx, limit=1, before=None, after=None, around=None, oldest_first=None):
    """
    Deletes messages in bulk
    limit: default is 1
    """
    await ctx.channel.send(f'Deleting {limit} messages')
    await ctx.channel.purge(limit=limit+2, before=before, after=after, around=around, oldest_first=None)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Ping :{floor( bot.latency*1000)} ms")


@bot.command()
async def joke(ctx, query="Any"):
    """ Search for a joke
    query: Programming/Misc/Dark/Pun/Spooky/Christmas
    """
    joke_json = jokes(query)
    message = joke_json["joke"]
    await ctx.send(message)

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    """
        kicks user
        user: Mention user
    """
    await user.kick(reason=reason)
    await ctx.send(f'User {user} has kicked.')


@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason="bad behaviour"):
    """
    bans user
    user: Mention user
    """
    await user.ban(reason=reason)
    ban = discord.Embed(
        title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)


@bot.command()
async def unban(ctx, *, member):
    """
    unbans user
    user: Mention user
    """
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')


bot.run(environ.get('BOT_KEY'))
