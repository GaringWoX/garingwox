import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='wox')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')
