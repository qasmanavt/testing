import threading
from telegram import *
from telegram.ext import *
from requests import *
from pictures import *
import  time
from texts import *
from start import *
 
 

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