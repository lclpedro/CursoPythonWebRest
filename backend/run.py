from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from flask_cors import CORS


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
        json={
            'name_person':name_person,
            'phone':phone
        }
        contact.insert(json)
        return 'Contado Salvo com Sucesso', 200
    else:
        value=[]
        contact = mongo.db.contact
        get_contact = contact.find()
        for und in get_contact:
            json={
                '_id':str(und['_id']),
                'name_person':und['name_person'],
                'phone':und['phone']
            }
            value.append(json)
        return jsonify(value)

# @app.route('/api/contact/<_id>', methods=['PUT', 'DELETE'])
# def del_get_contacts(_id):
#     if request.method == 'PUT':
#         contact = mongo.db.contact
#         value = request.json
#         print(value)
#         contact.update({'_id':_id},{'$set':value})
#         return 'Contato alterado com sucesso!', 200
#     else:
#         contact = mongo.db.contact
#         contact.remove({_id})
#     return jsonify(result=msg),200



if __name__ == "__main__":
    app.run(debug=True, threaded=True)
