import constants
import sys
sys.path.append('..src')


def handle_message(message):
    message_type = message['messageType']
    embed_title = get_symbol(message)
    embed_fields = None

    if (message_type == constants.MESSAGE_TYPE_ALERT):
        embed_title += ' - ALERT'
        embed_fields = get_alerts_embed_fields(message)
    else:
        embed_fields = get_embed_fields(message)

    return {
        'channel': get_channel(message),
        'embed_title': embed_title,
        'embed_color': get_embed_color(message),
        'embed_fields':  embed_fields,
        'embed_footer': get_embed_footer(message, message_type)
    }


def get_symbol(message):
    return message['symbol']


def get_channel(message):
    if (message['messageType'] == constants.MESSAGE_TYPE_FLOW):
        golden_sweep = message['goldenSweep']

        if (golden_sweep):
            return constants.CHANNEL_NAME_GOLDEN_SWEEPS
        else:
            return constants.CHANNEL_NAME_FLOW
    else:
        return constants.CHANNEL_NAME_ALERTS


def get_embed_color(message):
    golden_sweep = False
    embed_color = None

    if (message['messageType'] == constants.MESSAGE_TYPE_FLOW):
        golden_sweep = message['goldenSweep']

    if golden_sweep:
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
            'name': 'Expiration',
            'value': message['expiration'],
            'inline': True
        },
        {
            'name': 'Time',
            'value': message['time'],
            'inline': True
        }
    ]


def get_alerts_embed_fields(message):
    return [
        {
            'name': 'Position',
            'value': message['position'],
            'inline': True
        },
        {
            'name': 'Strike',
            'value': message['strike'],
            'inline': True
        },
        {
            'name': 'Expiration',
            'value': message['expiration'],
            'inline': True
        },
        {
            'name': 'Alert Price',
            'value': message['alertPrice'],
            'inline': True
        },
        {
            'name': 'Time',
            'value': message['time'],
            'inline': True
        }
    ]


def get_embed_footer(message, message_type):
    bullish = 'Bullish Flow'
    bearish = 'Bearish Flow'
    poss_close_sell_text = 'Possible Closing or Selling'

    if(message['sentiment'] == constants.SENTIMENT_BULLISH):
        text = bullish

        if (message_type != constants.MESSAGE_TYPE_ALERT):
            if 'B' in message['details']:
                text = f'{bullish} | {poss_close_sell_text}'

        return {
            'icon_url': 'https://i.imgur.com/GobRl44.png',
            'text': text
        }
    else:
        text = bearish

        if (message_type != constants.MESSAGE_TYPE_ALERT):
            if 'B' in message['details']:
                text = f'{bearish} | {poss_close_sell_text}'

        return {
            'icon_url': 'https://i.imgur.com/OWXP4Yv.png',
            'text': text
        }
