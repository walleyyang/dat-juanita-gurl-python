import asyncio
import websockets
import json
import discord
from discord.utils import get
from dotenv import load_dotenv
from os import getenv

import constants
from modules import bad_bug, fat_vamp


async def handler(websocket, path):
    print("A client connected")

    try:
        async for message in websocket:
            await handle_message(json.loads(message))

    except websockets.exceptions.ConnectionClosed as e:
        print("Client disconnected")
        print(e)


async def handle_message(message):
    bad_bug_message = bad_bug.handle_message(message)
    news = get_news(bad_bug.get_symbol(message))
    embed = get_embed(bad_bug_message, news)
    await send_message(bad_bug_message['channel'], embed)


async def send_message(channel, embed):
    if(channel == constants.CHANNEL_NAME_FLOW):
        await discord_client.get_channel(CHANNEL_ID_FLOW).send(embed=embed)
    elif(channel == constants.CHANNEL_NAME_GOLDEN_SWEEPS):
        await discord_client.get_channel(CHANNEL_ID_GOLDEN_SWEEP).send(embed=embed)
    else:
        await discord_client.get_channel(CHANNEL_ID_ALERTS).send(embed=embed)


def get_news(symbol):
    return fat_vamp.get_news(f'{FAT_VAMP}{symbol}')


def get_embed(message, news):
    embed = discord.Embed(
        title=message['embed_title'],
        color=message['embed_color']
    )

    for i in message['embed_fields']:
        embed.add_field(name=i['name'], value=i['value'], inline=i['inline'])

    embed.add_field(
        name='News', value=get_embed_news_field(news), inline='False')

    embed.set_footer(icon_url=message['embed_footer']
                     ['icon_url'], text=message['embed_footer']['text'])

    return embed


def get_embed_news_field(news):
    news_field = ''

    if news[0] == constants.NO_NEWS:
        news_field = constants.NO_NEWS
    else:
        for n in news:
            text = n['text']
            link = n['link']
            news_field += f'* [{text}]({link})\n'

    return news_field


if __name__ == '__main__':
    load_dotenv()

    CHANNEL_ID_ALERTS = int(getenv('CHANNEL_ID_ALERTS'))
    CHANNEL_ID_FLOW = int(getenv('CHANNEL_ID_FLOW'))
    CHANNEL_ID_GOLDEN_SWEEP = int(getenv('CHANNEL_ID_GOLDEN_SWEEP'))

    WEBSOCKET_URL = getenv('WEBSOCKET_URL')
    WEBSOCKET_PORT = getenv('WEBSOCKET_PORT')

    FAT_VAMP = getenv('FAT_VAMP')

    print("Server listening on Port " + str(WEBSOCKET_PORT))

    websocket_server = websockets.serve(handler, WEBSOCKET_URL, WEBSOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(websocket_server)

    # Discord runs this forever so its not needed for WebSockets
    # asyncio.get_event_loop().run_forever()

    discord_client = discord.Client()
    discord_client.run(getenv('BOT_TOKEN'))
