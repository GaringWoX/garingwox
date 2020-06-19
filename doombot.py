import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = commands.Bot(command_prefix='wox')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

client.run(os.getenv('Token'))
