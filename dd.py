import sqlite3
naak=''
conn = sqlite3.connect('cart.db')
cursor = conn.execute("SELECT ID,name, quantity,Price,productID from COMPANY where ID= '{}'".format("1338321506"))
conn.commit()
for row in cursor:
        uop=row[1]+' * '+row[2]+ '='+'$'+ row[3]+'\n'
        naak=naak+uop
print(naak)
