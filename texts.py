import pyodbc
phone_number=[]
list=[]
a=0

password = "qwerty"
connection = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-DFK8LR20;"
    "Database=testdb;"
    "Trusted_Connection=yes;")