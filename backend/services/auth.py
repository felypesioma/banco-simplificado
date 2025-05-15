from flask import request

def cadastro():
    # Simulação de cadastro
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return {'message': 'Dados inválidos'}, 400

    # Aqui você pode adicionar lógica para salvar o usuário no banco de dados
    return {'message': 'Usuário cadastrado com sucesso'}, 201