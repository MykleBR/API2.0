def get_contact_dict(contact):
    return {
        "id": contact.id,
        "nome": contact.nome,
        "sobrenome": contact.sobrenome,
        "email": contact.email,
        "telefone": contact.telefone
    }
