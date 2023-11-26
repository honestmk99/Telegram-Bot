import sqlite3

conn = sqlite3.connect('wel.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         msg     TEXT    NOT NULL
        
         
         
);''')
print ("Table created successfully")
conn.close()