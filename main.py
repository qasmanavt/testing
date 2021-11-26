import threading
import telegram
from config import TOKEN
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
from time import *
import time
import pyodbc
 
phone_number=[]
list=[]
a=0
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(TOKEN)
password = "qwerty"
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;"

)
def startCommand(update: Update, context: CallbackContext):
    name = update.effective_chat.full_name
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=" welcome to my bot! " + name)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="enter your password")


def messageHandler(update: Update, context: CallbackContext):
 

    if password == update.message.text:
        buttons = [[KeyboardButton("reservations")], [KeyboardButton("menu")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello ,here you can see user's order!",
                                 reply_markup=ReplyKeyboardMarkup(buttons))

        image = get(url_for_chef).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                   InputMediaPhoto(image, caption="")])

        
    elif "reservation" in  update.message.text:
        global phone_number,list
        def printit():
            threading.Timer(10.0, printit).start()
            time.sleep(5)
            status_text="waiting"
            cursor = connection.cursor()
            b2=cursor.execute(f'select status  from bot2 where status=? ;',status_text).fetchall()
          
            b=[]
            for b in b2:
                print(b)
                
        
            
                
            
            
            if "waiting" in b:
                status_text="waiting"
                b=cursor.execute('select  *  from bot2 where status=? ;',status_text).fetchall()
                
                for a in b:
                    text="first food is "+str(a[0])+"\nsecond food is "+str(a[1])+"\nthird food is "+str(a[2])+"\nname :"+str(a[3])+"\nphone number "+str(a[7])
                    
                 
                    buttons2 = [[InlineKeyboardButton("aceepted", callback_data="1")], 
                    [InlineKeyboardButton("decline", callback_data="2")]]
                    context.bot.send_message(chat_id=update.effective_chat.id,
                    reply_markup=InlineKeyboardMarkup(buttons2), text=text)     
                print("uji")
            elif b is None:
                print("x")
            else:
                print("ey")
            connection.commit()
        printit()   

    elif "menu" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text="sorry this page will be make sooner :) ")       
 

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
        
         
    dispatcher.add_handler(CallbackQueryHandler(queryHandler))   


   
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
