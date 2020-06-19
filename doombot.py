import discord
from discord.ext import commands
import datetime
import asnycio

from urllib import parse, request
import re

client = Bot(command_prefix='wox', description="This is DooM Bot")

@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run(os.getenv('Token'))
