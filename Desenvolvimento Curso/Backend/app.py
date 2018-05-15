#Declarações de Libs
from flask import Flask, jsonify, request, json
from flask_pymongo import MongoClient
from flask_cors import CORS
from bson.objectid import ObjectId

client = MongoClient('localhost',27017)
db=client.contacts

app = Flask('Python_Web_REST') 
CORS(app)

@app.route('/api/insert_contact', methods=['POST'])
def insert_contact():
    db.contact.insert(request.json)
    return jsonify(data='Contato inserido com sucesso.'), 200

@app.route('/api/get_contact', methods=['GET'])
def get_contact():
    valores=[]
    query=db.contact.find()
    for und in query:
        json=dict(
            _id=str(und['_id']),
            name_person=und['name_person'],
            phone=und['phone']
        )
        valores.append(json)
    return jsonify(data=valores), 200

@app.route('/api/get_contact/<_id>', methods=['GET'])
def get_contact_id(_id):
    valores=[]
    _id=ObjectId(_id)
    query=db.contact.find({'_id':_id})
    for und in query:
        json=dict(
             _id=str(und['_id']),
            name_person=und['name_person'],
            phone=und['phone']
        )
        valores.append(json)
    return jsonify(data=valores), 200

@app.route('/api/update_contact/<_id>', methods=['PUT'])
def update_contact(_id):
    _id=ObjectId(_id)
    value = request.json
    del value['_id']
    db.contact.update({'_id':_id},{'$set':value})
    return 'Contato atualizado com sucesso!', 200

@app.route('/api/delete_contact/<_id>', methods=['DELETE'])
def delete_contact(_id):
     _id=ObjectId(_id)
     db.contact.remove({'_id':_id})
     return jsonify(data='Contato deletado com sucesso!'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
