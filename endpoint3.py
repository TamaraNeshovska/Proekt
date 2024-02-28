from flask import Flask, request, jsonify
from sqlite3 import connect
import json
from telegram import telegram_funkcija
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')
# db= client['flask_appDb']
# collection = db['users_vouchers']

# @app.route('/write_to_mongodb',methods=['GET','POST'])
# def write_to_mongo():
#     if request.method =='POST':
#         # try:
#             data = request.get_json()
            
#             if 'user_id' not in data or 'total_spending' not in data:
#                 return jsonify({'error': 'Invalid input JSON'}), 400
            
#             user_id = data['user_id']
#             total_spending =data['total_spending']

#             result = collection.insert_one({'user_id': user_id, 'total_spending':total_spending})
#             return jsonify({'message': 'Data successfully inserted', 'inserted_id': str(result.inserted_id)}),201


# if __name__ == '__main__':
#     app.run(debug=True)

# client = pymongo.MongoClient()
# db = client.test_db
# nekoja_kolekcija  = db.test_kolekcija
# post = {
#     "avtor": "ime1",
#     "tekst": "nekoj_tekst"
# }
# posts= db.posts
# post_id = posts.insert_one(post).inserted_id
# print(post_id)
# def write_to_mongodb():
#     data = request.get_json()

#     if collection.find_one({'user_id': data['user_id']}):
#         return json.dumps({'Error': f'User with user_id {data["user_id"]} already exists!'}), 400
#     else:
#         if data['total_spending'] >= 2000:
#             result = collection.insert_one(data)
#             if result.inserted_id:
#                 return json.dumps({'Success': 'Data was successfully inserted'}), 201
#             else:
#                 return json.dumps({'Error': 'Failed to insert data'}), 500
#         else:
#             return json.dumps({'Bad Request': 'Total spending must be greater than 2000 !'}), 400

client = MongoClient('mongodb://localhost:27017/')
db = client.user_db
collection = db.userCollection

@app.route('/write_to_mongodb',methods=['GET','POST'])
def write_to_mongo():

    data = request.get_json()

    if collection.find_one({'user_id': data['user_id']}):
        return json.dumps({'Error': f'User with user_id {data["user_id"]} already exists!'}), 400
    else:
        if data['total_spending'] >= 2000:
            result = collection.insert_one(data)
            if result.inserted_id:
                return jsonify({'Success': 'Data was successfully inserted'}), 201
            else:
                return jsonify({'Error': 'Failed to insert data'}), 500
        else:
            return jsonify({'Bad Request': 'Total spending must be greater than 2000 !'}), 400
        
  
if __name__ == '__main__':
    app.run(debug=True)