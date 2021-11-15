import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import greet_user, location_shahovo

import config

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(config.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("location", location_shahovo))
    dp.add_handler(MessageHandler(Filters.regex('^(Схема проезда в Шахово)$'), location_shahovo))

    logging.info("bot started")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

