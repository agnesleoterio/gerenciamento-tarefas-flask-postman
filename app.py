from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados fictício
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# Endpoint para obter todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint para obter um usuário pelo ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# Endpoint para adicionar um novo usuário
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if users:
        new_user['id'] = users[-1]['id'] + 1
    else:
        new_user['id'] = 1
    users.append(new_user)
    return jsonify(new_user), 201

# Endpoint para atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    for user in users:
        if user['id'] == user_id:
            data = request.get_json()
            user.update(data)
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# Endpoint para deletar um usuário
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

