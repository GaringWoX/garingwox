import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='wox', description="This is DooM Bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(os.getenv('Token'))
