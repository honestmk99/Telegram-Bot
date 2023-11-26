import sqlite3

conn = sqlite3.connect('orders.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         name          TEXT    NOT NULL,
         oid     TEXT    NOT NULL,
         price     TEXT    NOT NULL,
         address     TEXT    NOT NULL,
         date     TEXT    NOT NULL,
         time     TEXT    NOT NULL,
         details     TEXT    NOT NULL,
         opt   TEXT    NOT NULL,
         contact  TEXT    NOT NULL,
         status     TEXT    NOT NULL
        
         
         
);''')
print ("Table created successfully")
conn.close()