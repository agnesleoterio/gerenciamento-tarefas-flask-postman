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

if __name__ == '__main__':
    app.run(debug=True)

