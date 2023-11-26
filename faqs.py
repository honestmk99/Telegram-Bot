import sqlite3 

conn = sqlite3.connect('faqs.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ques          TEXT    NOT NULL,
         ans        TEXT    NOT NULL
);''')
print ("Table created successfully")
conn = sqlite3.connect('faqsf.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ques          TEXT    NOT NULL,
         ans        TEXT    NOT NULL
);''')
print ("Table created successfully")

conn = sqlite3.connect('faqss.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         ques          TEXT    NOT NULL,
         ans        TEXT    NOT NULL
);''')
print ("Table created successfully")

conn = sqlite3.connect('help.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         contact          TEXT    NOT NULL,
         id          TEXT    NOT NULL
);''')
print ("Table created successfully")
