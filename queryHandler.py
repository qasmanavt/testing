from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from texts import *

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global connection,phone_number
    
    if "1" in query:
        
        context.bot.send_message(chat_id=update.effective_chat.id,text="successfully accepted!")
        status_text="waiting"
        status2="accepted"
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where status=?  ;',
                        (status2,status_text))
        connection.commit()
    

    elif "2" in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="you rejected order:(")
        status_text="waiting"
        status3="declined"
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where status=? ;',
                        (status3,status_text))
        connection.commit()