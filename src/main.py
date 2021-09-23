import discord
from discord.utils import get
from dotenv import load_dotenv
from os import getenv

from ServerChannel import ServerChannel

load_dotenv()
GUILD = getenv('GUILD')

client = discord.Client()


@client.event
async def on_ready():
    await client.get_channel(889609837107884052).send('hello world')

if __name__ == '__main__':
    client.run(getenv('BOT_TOKEN'))
