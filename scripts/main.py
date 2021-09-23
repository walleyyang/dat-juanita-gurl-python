import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()


bot = commands.Bot(command_prefix='.')


@bot.command()
async def hello(ctx):
    await ctx.reply('Hello')

bot.run(getenv('BOT_TOKEN'))
