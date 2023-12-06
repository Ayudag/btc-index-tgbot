import requests

import telebot
from telebot import types
import locale

from config import token_tg


bot = telebot.TeleBot(token_tg)
utc = '+0'


# After launching the bot. [start]
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

    # Buttons with time zones.
    utc_p12 = types.KeyboardButton('UTC+12')
    utc_p11 = types.KeyboardButton('UTC+11')
    utc_p10 = types.KeyboardButton('UTC+10')
    utc_p9 = types.KeyboardButton('UTC+9')
    utc_p8 = types.KeyboardButton('UTC+8')
    utc_p7 = types.KeyboardButton('UTC+7')
    utc_p6 = types.KeyboardButton('UTC+6')
    utc_p5 = types.KeyboardButton('UTC+5')
    utc_p4 = types.KeyboardButton('UTC+4')
    utc_p3 = types.KeyboardButton('UTC+3')
    utc_p2 = types.KeyboardButton('UTC+2')
    utc_p1 = types.KeyboardButton('UTC+1')
    utc_0 = types.KeyboardButton('UTC+0')
    utc_m1 = types.KeyboardButton('UTC-1')
    utc_m2 = types.KeyboardButton('UTC-2')
    utc_m3 = types.KeyboardButton('UTC-3')
    utc_m4 = types.KeyboardButton('UTC-4')
    utc_m5 = types.KeyboardButton('UTC-5')
    utc_m6 = types.KeyboardButton('UTC-6')
    utc_m7 = types.KeyboardButton('UTC-7')
    utc_m8 = types.KeyboardButton('UTC-8')
    utc_m9 = types.KeyboardButton('UTC-9')
    utc_m10 = types.KeyboardButton('UTC-10')
    utc_m11 = types.KeyboardButton('UTC-11')
    utc_m12 = types.KeyboardButton('UTC-12')

    markup.add(
        utc_p12, utc_p7, utc_p2, utc_m3, utc_m8,
        utc_p11, utc_p6, utc_p1, utc_m4, utc_m9,
        utc_p10, utc_p5, utc_0, utc_m5, utc_m10,
        utc_p9, utc_p4, utc_m1, utc_m6, utc_m11,
        utc_p8, utc_p3, utc_m2, utc_m7, utc_m12
    )

    timezone_map = open('pictures/timezonesmap.jpg', 'rb')

    bot.send_photo(message.chat.id, timezone_map)
    bot.send_message(message.chat.id, f'<b>Hi, {message.from_user.first_name}!</b>\n', parse_mode='html')
    bot.send_message(message.chat.id, 'Choose your Time Zone.', reply_markup=markup)


@bot.message_handler()
def get_bitcoin_price(message):

    # After selecting the time zone.
    if 'UTC' in message.text:
        global utc
        utc = message.text.replace('UTC', '')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        get_bitcoin_price_but = types.KeyboardButton('Get Bitcoin Price')
        change_time_zone = types.KeyboardButton('Change the Time Zone')
        invest_in_bitcoin = types.KeyboardButton('Invest in Bitcoin now?')
        markup.add(change_time_zone, invest_in_bitcoin, get_bitcoin_price_but)
        bot.send_message(message.chat.id, f'Your Time Zone: <b>{message.text}</b>', reply_markup=markup,
                         parse_mode='html')
        bot.send_message(message.chat.id, 'Click the button to get the Price of Bitcoin.')

    # Get Bitcoin Price.
    elif message.text.lower() == 'get bitcoin price':
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        # Setting up time output.
        time = response.json()['time']['updated']
        time_list = time.split(' ')
        time_utc0 = time_list[3][0:5]
        time_utc0_split = time_utc0.split(':')
        if "+" in utc:
            utc_number = utc.replace('+', '')
            hours = (int(time_utc0_split[0]) + int(utc_number)) % 24
        else:
            utc_number = utc.replace('-', '')
            hours = (int(time_utc0_split[0]) - int(utc_number))
            if hours < 0:
                hours += 24
        time_output = str(hours) + ':' + time_utc0_split[1]

        # Setting up price output.
        price = response.json()['bpi']['USD']['rate_float']
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        price_output = locale.format_string('%d', price, grouping=True)

        bot.send_message(message.chat.id, f'{time_output} (UTC{utc})\n'
                                          f'<b>${price_output}</b>', parse_mode='html')

    # Random GIF.
    elif message.text.lower() == 'invest in bitcoin now?':
        request_randomgif = requests.get('https://yesno.wtf/api')
        bot.send_animation(message.chat.id, request_randomgif.json()['image'])

    # Change the time zone.
    elif message.text.lower() == 'change the time zone':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

        # Buttons with time zones.
        utc_p12 = types.KeyboardButton('UTC+12')
        utc_p11 = types.KeyboardButton('UTC+11')
        utc_p10 = types.KeyboardButton('UTC+10')
        utc_p9 = types.KeyboardButton('UTC+9')
        utc_p8 = types.KeyboardButton('UTC+8')
        utc_p7 = types.KeyboardButton('UTC+7')
        utc_p6 = types.KeyboardButton('UTC+6')
        utc_p5 = types.KeyboardButton('UTC+5')
        utc_p4 = types.KeyboardButton('UTC+4')
        utc_p3 = types.KeyboardButton('UTC+3')
        utc_p2 = types.KeyboardButton('UTC+2')
        utc_p1 = types.KeyboardButton('UTC+1')
        utc_0 = types.KeyboardButton('UTC+0')
        utc_m1 = types.KeyboardButton('UTC-1')
        utc_m2 = types.KeyboardButton('UTC-2')
        utc_m3 = types.KeyboardButton('UTC-3')
        utc_m4 = types.KeyboardButton('UTC-4')
        utc_m5 = types.KeyboardButton('UTC-5')
        utc_m6 = types.KeyboardButton('UTC-6')
        utc_m7 = types.KeyboardButton('UTC-7')
        utc_m8 = types.KeyboardButton('UTC-8')
        utc_m9 = types.KeyboardButton('UTC-9')
        utc_m10 = types.KeyboardButton('UTC-10')
        utc_m11 = types.KeyboardButton('UTC-11')
        utc_m12 = types.KeyboardButton('UTC-12')

        markup.add(
            utc_p12, utc_p7, utc_p2, utc_m3, utc_m8,
            utc_p11, utc_p6, utc_p1, utc_m4, utc_m9,
            utc_p10, utc_p5, utc_0, utc_m5, utc_m10,
            utc_p9, utc_p4, utc_m1, utc_m6, utc_m11,
            utc_p8, utc_p3, utc_m2, utc_m7, utc_m12
        )

        timezone_map = open('pictures/timezonesmap.jpg', 'rb')

        bot.send_photo(message.chat.id, timezone_map)
        bot.send_message(message.chat.id, f'Choose your Time Zone.', reply_markup=markup)

    # Unrecognized command.
    else:
        bot.send_message(message.chat.id, 'Oops... Unrecognized command.')
        bot.send_message(message.chat.id, '<b>You can just use the buttons.</b>', parse_mode='html')


bot.polling(none_stop=True)
