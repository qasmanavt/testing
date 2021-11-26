import pyodbc
phone_number=[]
list=[]
a=0


Reservations="Reservations"
Menu="Menu"
Menu_text="sorry this page will be make sooner :) "
entering_text="Hello ,here you can see user's order!"

Accepted="Accepte"
Accepted_text="Successfully Accepted!"

Declined="Decline"
Declined_text="You Rejected Order:("
status="waiting"

password = "qwerty"
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;")

 
first_food_name="Plov"
price_1=10000
 

 
second_food_name="Shashlik"
price_2=15000
 

 
third_food_name="Shurpa"
price_3=20000
 