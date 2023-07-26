def validate_contact_data(data):
    required_fields = ['nome', 'sobrenome', 'email', 'telefone']
    for field in required_fields:
        if field not in data:
            return f"Campo '{field}' é obrigatório"
    return None
