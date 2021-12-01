import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
import queryHandler
from texts import *
from start import *
import messageHandler


updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)


dispatcher.add_handler(CallbackQueryHandler(queryHandler.queryHandler))
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(
    Filters.text, messageHandler.messageHandler))
updater.start_polling()
