from sqlite3 import connect
import json
user = 791
db_connection = connect('users_vouchers.db') 
db_cursor = db_connection.cursor()
rezultat = db_cursor.execute("SELECT money_spent, user_id FROM user_spending WHERE money_spent>2000")
# eden_red = rezultat.fetchall()
lista =rezultat.fetchall()
print(lista)
# print(list(sum(lista,()))[0] )
# print(rezultat.fetchall())
# print(list(lista))
# if list(lista)==[]:
#     print("nevaliden user")
# else:
#     suma = 0
#     for i in lista:
#         a= list(i)
#         print(list(i))
#         suma = suma + a[0]

#     print(suma)
#     print(type(suma))  #float
#     print(type(rezultat.fetchall()))
#     print(json.dumps(suma))

db_connection.close()

# rezultat = db_cursor.execute("SELECT year FROM movie WHERE score =10.0")
# print(rezultat.fetchall())


### OD PROEKT1 
