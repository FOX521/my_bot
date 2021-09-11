import logging
import settings
import ephem
from typing import Text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    user_name = update.message.from_user['first_name']
    update.message.reply_text(f'Привет, {user_name}! Данный бот позволяет получить данные о нахождении планет в созведии. Введи /help чтобы получить больше информации.')

def help_user(update, context):
    update.message.reply_text(f'/planet name_planet date - Отображает местоположение планеты в созведии на заданную дату \n/show_planet - отображает список планет')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

'''def choice_planet(planet, date):
    mars = ephem.'Mars'(date)
    val = ephem.constellation(mars)
    update.message.reply_text(f'Планета на дату {planet_date} будет находиться в созведии: {val[1]}')'''

def show_planet(update, context):
    planet_list = ['Mars', 'Venus', 'Uran']
    for planet in planet_list:
        update.message.reply_text(planet)

def get_planet(update, context):
    planet_info = update.message.text.split()
    planet_date = planet_info[2]
    planet = planet_info[1]
    if planet == 'Mars':
        mars = ephem.Mars(planet_date)
        val = ephem.constellation(mars)
        update.message.reply_text(f'Планета на дату {planet_date} будет находиться в созведии: {val[1]}')
    elif planet == 'Venus':
        venus = ephem.Venus('2000/01/01')
        val = ephem.constellation(venus)
    elif planet == 'Mercury':
        merc = ephem.Mercury('2000/01/01')
        val = ephem.constellation(merc)
    elif planet == 'Uranus':
        uranus = ephem.Uranus('2000/01/01')
        val = ephem.constellation(uranus)
    elif planet == 'Neptune':
        neptune = ephem.Neptune('2000/01/01')
        val = ephem.constellation(neptune)
    elif planet == 'Pluto':
        pluto = ephem.Pluto('2000/01/01')
        val = ephem.constellation(pluto)
    elif planet == 'Moon':
        moon = ephem.Moon('2000/01/01')
        val = ephem.constellation(moon)
    elif planet == 'Sun':
        sun = ephem.Sun('2000/01/01')
        val = ephem.constellation(sun)
    elif planet == 'Jupiter':
        jupiter = ephem.Jupiter('2000/01/01')
        val = ephem.constellation(jupiter)
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
    dp.add_handler(CommandHandler('help', help_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('show_planet', show_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot has been started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()

