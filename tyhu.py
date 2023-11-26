import sqlite3
conn = sqlite3.connect('wallet.db')
conn.execute("UPDATE COMPANY set balance = '1000' where ID = {}".format('1325866713'))
conn.commit()