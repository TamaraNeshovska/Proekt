from sqlite3 import connect
import json

def funkcija(a,b):
    """
    Funkcijata ja presmetuva vkupnata potrosuvacka na odredena starosna grupa za vnesena dadena granica
    param a: int 
    param b: int 
    a i b se odnesuvaat vo smisla na dadenata granica [a,b]
    funkcijata ja vrakja prosecna potrosuvacka na dadena starosna grupa
    """
    db_connection = connect('users_vouchers.db') 
    db_cursor = db_connection.cursor()
    
    rezultat = db_cursor.execute("SELECT user_id FROM user_info WHERE age>='{}' AND age<='{}' ".format(a,b))   
    lista =rezultat.fetchall()  #lista od tuples od user_id vo taa granica
    lista_user_id = list(sum(lista,()))  # lista od tuples -> to list
    # print(r) 
    br_na_user_id = len(lista_user_id)  #kolkav e brojot na lugje vo taa starosna granica 
    # print("dolzina na lista",len(r))  # dolzina na lista 
    suma=0
    for user_id in lista_user_id:
        grupa = db_cursor.execute("SELECT money_spent FROM user_spending WHERE user_id = '{}'".format(user_id)) #return tuple 
        lista1 = grupa.fetchall() #list of tuples 
        
        lista1_r = list(sum(lista1,())) #list of tuples to list #lista od kolku potrosil toj user_id
        suma = suma + sum(lista1_r)

    # db_connection.close()
    return  suma/br_na_user_id       

print('funkaijcata e:')
funkcija(18,24)
funkcija(25,30)
print(funkcija(18,24))
print(funkcija(25,30))
print(funkcija(31,36))
print(funkcija(37,47))
print(funkcija(47,100))

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


"6368401381:AAHfDYoZrdflss1Xgb66RgGc4DGNUwFy_i0"