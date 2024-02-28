from flask import Flask, request, jsonify
from sqlite3 import connect
import json

app = Flask(__name__)

@app.route('/total_spent/<int:user_id>', methods = ['GET']) 
def total_spending(user_id):                                                   
    db_connection = connect('users_vouchers.db')                           # if request.method =='GET':                                                   
    db_cursor = db_connection.cursor()                                     #user_id=request.form['user_id']
    rezultat = db_cursor.execute("SELECT SUM(money_spent) FROM user_spending WHERE user_id = '{}'".format(user_id))
    lista = rezultat.fetchall() #lista od tuples
    if list(lista)==[]:
        return 'Vnesovte nevaliden user_id'
    else:
        suma = list(lista)[0]  #suma = int
        # for i in lista:
        #     a = list(i) #sekoj tuple vo lista so eden element
        #     suma = suma + a[0]
        #print(suma) type(suma)=float
        # return f'Userot: {json.dumps(user_id)} ima vkupna potrosuvacka od: {json.dumps(suma)}'  #deka treba da sodrzi user_id i vkupna potrosuvacka dali vo lista ili ?
        return jsonify(user_id = user_id,
                       vkupna_potrosuvacka = suma)
    
    
if __name__ == '__main__':
    app.run(debug=True)