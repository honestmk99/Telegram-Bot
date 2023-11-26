import sqlite3 

conn = sqlite3.connect('withdraw.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID text  NOT NULL,
         balance         TEXT    NOT NULL,
         status         TEXT    NOT NULL,
         wid         TEXT    NOT NULL,
         rid         TEXT    NOT NULL,
         date         TEXT    NOT NULL,
         time         TEXT    NOT NULL,
         currency         TEXT    NOT NULL,
         address        TEXT    NOT NULL,
         email          TEXT    NOT NULL

);''')#ID,balance,email,wid,rid,date,time,status
print ("Table created successfully")
conn.close()