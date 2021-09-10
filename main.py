import logging
import settings
import ephem
from typing import Text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def get_planet(update, context):
    text = update.message.text
    planet_list = text.split()
    planet = planet_list[1]
    if planet == 'Mars':
        mars = ephem.Mars('2000/01/01')
        val = ephem.constellation(mars)
        print(val)
    elif planet == 'Jupiter':
        jupiter = ephem.Jupiter('2000/01/01')
        val = ephem.constellation(jupiter)
        print(val)
    elif planet == 'Saturn':
        saturn = ephem.Saturn('2000/01/01')
        val = ephem.constellation(saturn)
    else: 
         update.message.reply_text('Выбери что то одно: /planet Saturn /planet Jupiter /planet Mars')
    print(planet)



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot has been started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()

