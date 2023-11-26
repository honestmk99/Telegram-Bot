import sqlite3 

conn = sqlite3.connect('wallet.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         balance         TEXT    NOT NULL,
         code          TEXT    NOT NULL,
         link           TEXT    NOT NULL,
         name           TEXT    NOT NULL,
         withdrawl           TEXT    NOT NULL,
         wemail           TEXT    NOT NULL,
         ct         TEXT    NOT NULL,
         Trx         TEXT    NOT NULL,
         sct         TEXT    NOT NULL,
         exp        TEXT    NOT NULL,
         naam       TEXT    NOT NULL,
         wname       TEXT    NOT NULL,
         opt       TEXT    NOT NULL,
         twd       TEXT    NOT NULL,
         ttr       TEXT    NOT NULL,
         email         TEXT    NOT NULL,
         curr       TEXT    NOT NULL,
         amount           TEXT    NOT NULL

);''')
print ("Table created successfully")
conn.close()