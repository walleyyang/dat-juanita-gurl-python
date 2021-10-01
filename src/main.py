import asyncio
import websockets
import json
import discord
from discord.utils import get
from dotenv import load_dotenv
from os import getenv

from ServerChannel import ServerChannel

load_dotenv()

CHANNEL_FLOW = int(getenv('CHANNEL_FLOW'))
CHANNEL_GOLDEN_SWEEP = int(getenv('CHANNEL_GOLDEN_SWEEP'))

WEBSOCKET_URL = getenv('WEBSOCKET_URL')
WEBSOCKET_PORT = getenv('WEBSOCKET_PORT')

# Discord
discord_client = discord.Client()


print("Server listening on Port " + str(WEBSOCKET_PORT))

channel = None


async def handler(websocket, path):
    print("A client connected")

    try:
        async for message in websocket:
            await send_message(json.loads(message))

    except websockets.exceptions.ConnectionClosed as e:
        print("Client disconnected")
        print(e)


async def send_message(message):
    time = message['time']
    symbol = message['symbol']
    expiration = message['expiration']
    strike = message['strike']
    position = message['position']
    stock_price = message['stockPrice']
    details = message['details']
    type = message['type']
    value = message['value']
    golden_sweep = message['goldenSweep']
    sentiment = message['sentiment']

    embed_color = None

    if golden_sweep:
        embed_color = 0xF7B718
    elif message['position'] == 'PUT':
        embed_color = 0xD32915
    else:
        embed_color = 0x15D33D

    embed = discord.Embed(
        title=symbol,
        color=embed_color,
    )

    embed.add_field(name='Value', value=value, inline=True)
    embed.add_field(name='Position', value=position, inline=True)
    embed.add_field(name='Details', value=details, inline=True)
    embed.add_field(name='Type', value=type, inline=True)
    embed.add_field(name='Strike', value=strike, inline=True)
    embed.add_field(name='Stock Price', value=stock_price, inline=True)
    embed.add_field(name='Time', value=time, inline=True)
    embed.add_field(name='Expiration', value=expiration, inline=True)

    if (sentiment == 'BULLISH'):
        embed.set_footer(
            icon_url="https://i.imgur.com/GobRl44.png", text='Bullish')
    else:
        embed.set_footer(
            icon_url="https://i.imgur.com/OWXP4Yv.png", text='Bearish')

    if (golden_sweep):
        await discord_client.get_channel(CHANNEL_GOLDEN_SWEEP).send(embed=embed)
    else:
        await discord_client.get_channel(CHANNEL_FLOW).send(embed=embed)


websocket_server = websockets.serve(handler, WEBSOCKET_URL, WEBSOCKET_PORT)

asyncio.get_event_loop().run_until_complete(websocket_server)
# Discord runs this forever so its not needed for WebSockets
# asyncio.get_event_loop().run_forever()

# @discord_client.event
# async def on_ready():
#    test stuff


if __name__ == '__main__':
    discord_client.run(getenv('BOT_TOKEN'))
