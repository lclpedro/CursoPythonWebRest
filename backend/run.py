#Declarações de Libs
from flask import Flask, jsonify, request, json
from flask_pymongo import MongoClient
from flask_cors import CORS
from bson.objectid import ObjectId

#Configurações básicas da Aplicação
#Inicialização do Flask passando um nome a aplicação
app = Flask('Python_Web_REST')
#Lib para tratar de CORS, Cross-Origin-* 
CORS(app)
#Conector do Mongo passando as configurações do servidor Mongo
client = MongoClient('localhost', 27017)
#Definindo nome do Banco de dados que será utilizado
db = client.crud

# Listagem de todos os contatos
@app.route('/api/contacts', methods=['GET'])
def get_contact():
    value=[]
    contact = db.contact
    get_contact = contact.find()
    for und in get_contact:
        json=dict(
            _id=str(und['_id']), 
            name_person=und['name_person'], 
            phone=und['phone']
        )
        value.append(json)
    return jsonify(value)

#Inserir um Novo Contato
@app.route('/api/contacts', methods=['POST'])
def insert_contact():
    contact = db.contact
    name_person=request.json.get('name_person')
    phone=request.json.get('phone')
    json=dict(
        name_person=name_person,
        phone=phone
    )
    contact.insert(json)
    return 'Contato Salvo com Sucesso', 200

#Listar Apenas um Contato Sendo identificado pelo ID.
@app.route('/api/contact/<_id>', methods=['GET'])
def get_one_contact(_id):
    contact = db.contact
    _id=ObjectId(_id)
    value=[]
    contact = db.contact
    get_contact = contact.find({'_id':_id})
    for und in get_contact:
        json=dict(
            _id=str(und['_id']), 
            name_person=und['name_person'], 
            phone=und['phone']
        )
        value.append(json)
    return jsonify(value)

#Atualizando os dados de um contato.
@app.route('/api/contact/<_id>', methods=['PUT'])
def update_contact(_id):
    contact = db.contact
    _id=ObjectId(_id)
    value = request.json
    del value['_id']
    contact.update({'_id':_id},{'$set':value})
    return 'Contato atualizado com sucesso!', 200

# Deletando um Contato
@app.route('/api/contact/<_id>', methods=['DELETE'])
def delete_contact(_id):
    contact = db.contact
    _id=ObjectId(_id)
    contact.remove({'_id':_id})
    return 'Contato deletado com Sucesso!',200


# @app.route('/api/contacts', methods=['GET', 'POST'])
# def get_insert_contact():
#     contact = db.contact
#     if request.method == 'POST':
#         name_person=request.json.get('name_person')
#         phone=request.json.get('phone')
#         json=dict(
#             name_person=name_person,
#             phone=phone
#         )
#         contact.insert(json)
#         return 'Contato Salvo com Sucesso', 200
#     else:
#         value=[]
#         contact = db.contact
#         get_contact = contact.find()
#         for und in get_contact:
#             json=dict(
#                 _id=str(und['_id']), 
#                 name_person=und['name_person'], 
#                 phone=und['phone']
#             )
#             value.append(json)
#         return jsonify(value)

# @app.route('/api/contact/<_id>', methods=['PUT', 'DELETE', 'GET'])
# def del_get_contacts(_id):
#     contact = db.contact
#     _id=ObjectId(_id)
#     if request.method == 'PUT':
#         value = request.json
#         del value['_id']
#         contact.update({'_id':_id},{'$set':value})
#         return 'Contato atualizado com sucesso!', 200
#     elif request.method=='GET':
#         value=[]
#         contact = db.contact
#         get_contact = contact.find({'_id':_id})
#         for und in get_contact:
#             json=dict(
#                 _id=str(und['_id']), 
#                 name_person=und['name_person'], 
#                 phone=und['phone']
#             )
#             value.append(json)
#         return jsonify(value)
#     else:
#         contact.remove({'_id':_id})
#     return 'Contato deletado com Sucesso!',200

#Inicialização do servidor Flask.
#Passando alguns parametros de inicialização
    #debug=True autoreload (em faze de desenvolvimento)
    #threaded=True Utilização de multiThreads fluidez na aplicação
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
