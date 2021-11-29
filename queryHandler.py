from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from texts import *

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global connection,phone_number
    print(update.callback_query.data)
    
    if "acc" in query:
        
 
        context.bot.send_message(chat_id=update.effective_chat.id,text=Accepted_text)
        status_text=status
        status2=Accepted
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where status=? and id=?  ;',
                        (status2,status_text,query[:len(query)-3]))
        connection.commit()
    

    elif "dec" in query:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=Declined_text)
        status_text=status
        status3=Declined
        connection.commit()
        cursor = connection.cursor()
        cursor.execute(f'update bot2 set status=? where status=? and id=? ;',
                        (status3,status_text,query[:len(query)-3]))
        connection.commit()