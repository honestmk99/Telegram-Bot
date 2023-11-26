import sqlite3 

conn = sqlite3.connect('deposit.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (name     TEXT    NOT NULL,
         address          TEXT    NOT NULL

);''')
print ("Table created successfully")

conn.close()