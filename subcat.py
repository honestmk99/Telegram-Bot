import sqlite3 

conn = sqlite3.connect('subcata.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (cat     TEXT    NOT NULL,
         subcat     TEXT    NOT NULL
);''')
print ("Table created successfully")

conn.close()