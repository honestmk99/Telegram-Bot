import sqlite3 

conn = sqlite3.connect('shop.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         name          TEXT    NOT NULL,
         description        TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         productID        TEXT    NOT NULL,
         category         TEXT    NOT NULL,
         max         TEXT    NOT NULL,
         stock        TEXT    NOT NULL,
         subcat         TEXT    NOT NULL,
         photoid         TEXT    NOT NULL
);''')
print ("Table created successfully")
