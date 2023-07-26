from flask import Blueprint, request, jsonify
from models.contact import Contact
from utils.utils import get_contact_dict
from .validatiors import validate_contact_data

contacts_blueprint = Blueprint('contacts', __name__)

@contacts_blueprint.route('/contatos', methods=['POST'])
def create_contact():
    try:
        data = request.json

        validation_error = validate_contact_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400

        # Adicione um log para verificar os dados recebidos
        print("Data received:", data)

        contact = Contact(nome=data['nome'], sobrenome=data['sobrenome'], email=data['email'], telefone=data['telefone'])
        contact.save()

        # Adicione um log para verificar o ID gerado após salvar o contato
        print("Contact ID:", contact.id)

        return jsonify({"id": contact.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@contacts_blueprint.route('/contatos/<int:id>', methods=['GET'])
def read_contact(id):
    try:
        contact = Contact.get_by_id(id)

        if not contact:
            return jsonify({"message": "Contato não encontrado"}), 404

        contato_dict = get_contact_dict(contact)
        return jsonify(contato_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@contacts_blueprint.route('/contatos/<int:id>', methods=['PUT'])
def update_contact(id):
    try:
        data = request.json

        if not any(data.values()):
            return jsonify({"message": "Nenhum campo a ser atualizado"}), 400

        contact = Contact.get_by_id(id)
        if not contact:
            return jsonify({"message": "Contato não encontrado"}), 404

        if data.get('nome'):
            contact.nome = data['nome']

        if data.get('email'):
            contact.email = data['email']

        if data.get('telefone'):
            contact.telefone = data['telefone']

        contact.save()

        return jsonify({"message": "Contato atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@contacts_blueprint.route('/contatos/<int:id>', methods=['DELETE'])
def delete_contact(id):
    try:
        contact = Contact.get_by_id(id)
        if not contact:
            return jsonify({"message": "Contato não encontrado"}), 404

        contact.delete()

        return jsonify({"message": "Contato excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@contacts_blueprint.route('/contatos/search', methods=['GET'])
def search_contact():
    try:
        nome_pesquisa = request.args.get('nome')

        contatos = Contact.search_by_name(nome_pesquisa)

        if not contatos:
            return jsonify({"message": "Nenhum contato encontrado"}), 404

        contatos_list = [get_contact_dict(contact) for contact in contatos]
        return jsonify(contatos_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
