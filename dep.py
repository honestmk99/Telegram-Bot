import sqlite3 

conn = sqlite3.connect('depfomat.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID text  NOT NULL,
         amount        TEXT    NOT NULL,
         status         TEXT    NOT NULL

);''')#ID,balance,email,wid,rid,date,time,status
print ("Table created successfully")
conn.close()