from telegram import *
from telegram.ext import *
from texts import *


def startCommand(update: Update, context: CallbackContext):
    name = update.effective_chat.full_name
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=start_text + name)
