from os import stat
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
        buttons = [[KeyboardButton(Reservations)], [KeyboardButton(Menu)]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=entering_text,
                                 reply_markup=ReplyKeyboardMarkup(buttons))

        image = get(url_for_chef).content
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[
                                   InputMediaPhoto(image, caption="")])

        
    elif Reservations in  update.message.text:
        global phone_number,list
        
        def printit():
            threading.Timer(10.0, printit).start()
            time.sleep(5)
            status_text=status
            cursor = connection.cursor()
            b=cursor.execute(f'select status  from bot2 where status=? ;',status_text).fetchone()
          
            # b=[]
            # for b in b2:
            #     print(b)
            if status in b:
                status_text=status
                b=cursor.execute('select  *  from bot2 where status=? ;',status_text).fetchall()
                
                for a in b:
                    order=""
                    price=0
                    if  a[0]>0:
                        order = order +" "+ first_food_name+" :"+str( a[0])+"\n"
                        price=price+a[0] * price_1
                    if a[1]>0:
                        order = order +" "+ second_food_name+" :"+str(a[1])+"\n"
                        price = price + a[1] * price_2
                    if a[2]>0:
                        order = order + " "+third_food_name+" :"+str(a[2])+"\n"
                        price = price + a[2] * price_3

                    text=order+"Total price :"+str(price)+" sum"+"\nname :"+str(a[3])+"\nphone number "+str(a[7])
                    
                    # text="first food is "+str(a[0])+"\nsecond food is "+str(a[1])+"\nthird food is "+str(a[2])+"\nname :"+str(a[3])+"\nphone number "+str(a[7])
                    
                 
                    buttons2 = [[InlineKeyboardButton(Accepted, callback_data="1")], 
                    [InlineKeyboardButton(Declined, callback_data="2")]]
                    context.bot.send_message(chat_id=update.effective_chat.id,
                    reply_markup=InlineKeyboardMarkup(buttons2), text=text)     
                print("a")
            elif b is None:
                print("b")
            else:
                print("c")
            connection.commit()
        printit()   

    elif Menu in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,text=Menu_text)   