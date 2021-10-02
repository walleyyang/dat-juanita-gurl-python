import constants
import sys
sys.path.append('..src')


def handle_message(message):
    return {
        'channel': get_channel(message),
        'embed_title': message['symbol'],
        'embed_color': get_embed_color(message),
        'embed_fields': get_embed_fields(message),
        'embed_footer': get_embed_footer(message)
    }


def get_channel(message):
    if (message['goldenSweep']):
        return constants.GOLDEN_SWEEPS
    else:
        return constants.FLOW


def get_embed_color(message):
    embed_color = None

    if message['goldenSweep']:
        embed_color = 0xF7B718
    elif message['position'] == 'PUT':
        embed_color = 0xD32915
    else:
        embed_color = 0x15D33D

    return embed_color


def get_embed_fields(message):
    return [
        {
            'name': 'Value',
            'value': message['value'],
            'inline': True
        },
        {
            'name': 'Position',
            'value': message['position'],
            'inline': True
        },
        {
            'name': 'Details',
            'value': message['details'],
            'inline': True
        },
        {
            'name': 'Type',
            'value': message['type'],
            'inline': True
        },
        {
            'name': 'Strike',
            'value': message['strike'],
            'inline': True
        },
        {
            'name': 'Stock Price',
            'value': message['stockPrice'],
            'inline': True
        },
        {
            'name': 'Time',
            'value': message['time'],
            'inline': True
        },
        {
            'name': 'Expiration',
            'value': message['expiration'],
            'inline': True
        }
    ]


def get_embed_footer(message):
    if(message['sentiment'] == 'BULLISH'):
        return {
            'icon_url': 'https://i.imgur.com/GobRl44.png',
            'text': 'Bullish'
        }
    else:
        return {
            'icon_url': 'https://i.imgur.com/OWXP4Yv.png',
            'text': 'Bearish'
        }
