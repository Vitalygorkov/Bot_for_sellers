# https://pythonru.com/primery/python-telegram-bot
import telebot
import config
# import pb
import datetime
# import pytz
import json
import traceback
from config import api_key
import time

bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('баланс', '/start')

# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text.lower() == 'go':
#         bot.send_message(message.from_user.id, 'начинаем эффективную работу', reply_markup=keyboard1)
#         print('Баланс')
#
#     else:
#         print(message.text)
#         bot.send_message(message.from_user.id, 'Минуты пробел задача', reply_markup=keyboard1)
#
#     # elif message.text.lower().split()[0].isdigit() == True:
#     #     bot.send_message(message.from_user.id, 'задание '+ message.text, reply_markup=keyboard1)
#     #     print('задание')
#     #
#     # else:
#     #     print(message.text)
#     #     bot.send_message(message.from_user.id, 'Минуты пробел задача', reply_markup=keyboard1)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Greetings! I can show you exchange rates.\n' +
        'To get the exchange rates press /exchange.\n' +
        'To get help press /help.'
  )

@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/artiomtb'
  )
    )
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' +
        '2) Click on the currency you are interested in.\n' +
        '3) You will receive a message containing information regarding the source and the target currencies, ' +
        'buying rates and selling rates.\n' +
        '4) Click “Update” to receive the current information regarding the request. ' +
        'The bot will also show the difference between the previous and the current exchange rates.\n' +
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['exchange'])
def text(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data='order')
    )
    bot.send_message(
        message.chat.id,
        'Click on the currency of choice:',
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    print(data)
    if data.startswith('order'):
        print('its func iq_callback')
        get_ex_callback(query)

def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])

def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    # ex = pb.get_exchange(ex_code)
    ex = 'its_ex'

    # bot.send_message(
    #     message.chat.id, ex,
    #     reply_markup=get_update_keyboard(ex),
	# parse_mode='HTML'
    # )
    bot.send_message(
        message.chat.id,
        ex, reply_markup=get_update_keyboard2(ex)
    )

def get_update_keyboard2(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('USD', callback_data='order')
    )
    return keyboard



bot.polling(none_stop=True, interval=0)