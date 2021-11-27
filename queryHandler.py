from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from texts import *

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global connection,phone_number
    
    if str(update.effective_chat.id) in query:
        
        context.bot.send_message(chat_id=update.effective_chat.id,text=Accepted_text)
        status_text=status
        status2=Accepted
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where id=?  ;',
                        (status2,int(update.effective_chat.id)))
        connection.commit()
    

    elif str(update.effective_chat.id) in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Declined_text)
        status_text=status
        status3=Declined
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where id=? ;',
                        (status3,int(update.effective_chat.id)))
        connection.commit()