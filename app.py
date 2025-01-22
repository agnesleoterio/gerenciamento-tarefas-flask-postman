from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados fictício
tasks = [
    {'id': 1, 'title': 'dar comida pro cachorro', 'description': 'marca da ração', 'status': 'done', 'date': '01/01/2025'},
    {'id': 2, 'title': 'comprar leite', 'description': 'zero lactose', 'status': 'done', 'date': '02/02/2025'}
]

users = [
    {'id': 1, 'name': 'Ana', 'email': 'ana@example.com', 'password': '123456'},
    {'id': 2, 'name': 'Agatha', 'email': 'agatha@example.com', 'password': '678910'}
]

# Endpoint para autenticar usuarios
@app.route('/login', methods=['POST'])
def login():
    login_user = request.get_json()
    for user in users:
        if login_user['email'] == user['email']:
            if login_user['password'] == user['password']:
                return jsonify({'mensage': 'login successful'}), 200
    return jsonify({'message': 'wrong credentials'}), 400


# Endpoint para obter todos os usuários
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Endpoint para obter um usuário pelo ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'message': 'task not found'}), 404

# Endpoint para adicionar um novo usuário
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.get_json()
    if tasks:
        new_task['id'] = tasks[-1]['id'] + 1
    else:
        new_task['id'] = 1
    tasks.append(new_task)
    return jsonify(new_task), 201

# Endpoint para atualizar um usuário existente
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            data = request.get_json()
            task.update(data)
            return jsonify(task)
    return jsonify({'message': 'task not found'}), 404

# Endpoint para deletar um usuário
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'task deleted'})
    return jsonify({'message': 'task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

