from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
mongo = PyMongo(app)
MONGO_URI='mongodb://localhost:27017/admin'

@app.route('/api/contacts', methods=['GET', 'POST'])
def get_insert_persons():
    contact = mongo.db.contact
    if request.method == 'POST':
        name_person=request.json.get('name_person')
        phone=request.json.get('phone')
        json=dict(
            name_person=name_person,
            phone=phone
        )
        contact.insert(json)
        return 'Contato Salvo com Sucesso', 200
    else:
        value=[]
        contact = mongo.db.contact
        get_contact = contact.find()
        for und in get_contact:
            json=dict(
                _id=str(und['_id']), 
                name_person=und['name_person'], 
                phone=und['phone']
            )
            value.append(json)
        return jsonify(value)

@app.route('/api/contact/<_id>', methods=['PUT', 'DELETE', 'GET'])
def del_get_contacts(_id):
    contact = mongo.db.contact
    _id=ObjectId(_id)
    if request.method == 'PUT':
        value = request.json
        del value['_id']
        contact.update({'_id':_id},{'$set':value})
        return 'Contato atualizado com sucesso!', 200
    elif request.method=='GET':
        value=[]
        contact = mongo.db.contact
        get_contact = contact.find({'_id':_id})
        for und in get_contact:
            json=dict(
                _id=str(und['_id']), 
                name_person=und['name_person'], 
                phone=und['phone']
            )
            value.append(json)
        return jsonify(value)
    else:
        contact.remove({'_id':_id})
    return 'Contato deletado com Sucesso!',200



if __name__ == "__main__":
    app.run(debug=True, threaded=True)
