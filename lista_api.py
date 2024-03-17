from flask import Flask, request, jsonify
import json


#1
app = Flask(__name__)

@app.route('/calculadora', methods=['POST'])
def calculadora():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operacao = data['operacao']

    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return jsonify({'error': 'Divisão por zero não é permitida'}), 400

    return jsonify({'resultado': resultado})

#2 

app = Flask(__name__)

USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    users = load_users()
    return jsonify(users)

@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    user = request.get_json()
    users = load_users()
    users.append(user)
    save_users(users)
    return jsonify(user), 201

@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    user_data = request.get_json()
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            user.update(user_data)
            save_users(users)
            return jsonify(user)
    return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def excluir_usuario(user_id):
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            save_users(users)
            return jsonify({'message': 'Usuário excluído com sucesso'})
    return jsonify({'error': 'Usuário não encontrado'}), 404

#3

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    task = request.get_json()
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201

@app.route('/tarefas/<int:task_id>', methods=['PUT'])
def marcar_tarefa_concluida(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['concluida'] = True
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tarefas/<int:task_id>', methods=['DELETE'])
def excluir_tarefa(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return jsonify({'message': 'Tarefa excluída com sucesso'})
    return jsonify({'error': 'Tarefa não encontrada'}), 404


#4
PRODUCTS_FILE = 'products.json'

def load_products():
    try:
        with open(PRODUCTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_products(products):
    with open(PRODUCTS_FILE, 'w') as file:
        json.dump(products, file, indent=4)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    products = load_products()
    return jsonify(products)

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    product = request.get_json()
    products = load_products()
    products.append(product)
    save_products(products)
    return jsonify(product), 201

@app.route('/produtos/<int:product_id>', methods=['PUT'])
def atualizar_estoque_produto(product_id):
    product_data = request.get_json()
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            product.update(product_data)
            save_products(products)
            return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'}), 404

@app.route('/produtos/<int:product_id>', methods=['DELETE'])
def excluir_produto(product_id):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            save_products(products)
            return jsonify({'message': 'Produto excluído com sucesso'})
    return jsonify({'error': 'Produto não encontrado'}), 404
