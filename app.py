from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'texto': 'Quanto mais se tira, maior ele fica. O que é?', 'resposta': 'buraco'},
    {'id': 2, 'texto': 'O que é que corre ao redor do quintal sem sair do lugar?', 'resposta': 'cerca'},
    {'id': 3, 'texto': 'Quem é que faz a viagem deitado?', 'resposta': 'rio'},  
    {'id': 4, 'texto': 'O que é que tem cabeça e tem dente, mas não é gente?', 'resposta': 'alho'},
    {'id': 5, 'texto': 'Quem é que sobe e desce sem sair do lugar?', 'resposta': 'escada'},  
    {'id': 6, 'texto': 'O que é que quanto mais se divide, mais se multiplica?', 'resposta': 'bactéria'},
    {'id': 7, 'texto': 'O que é que você pode segurar sem nunca tocar?', 'resposta': 'conversa'},
    {'id': 8, 'texto': 'O que é que tem cidades, mas não tem casas; tem rios, mas não tem água; tem florestas, mas não tem árvores?', 'resposta': 'mapa'},
    {'id': 9, 'texto': 'O que é que quanto mais você tira, mais ele aumenta?', 'resposta': 'foto'},  
    {'id': 10, 'texto': 'O que é que você sempre encontra no final de tudo?', 'resposta': 'letra u'}
]

@app.route('/')
def index():
    return 'API ON'

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(random.choice(charadas)), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def busca(campo, busca):

    if campo not in ['id','texto','resposta']:
        return jsonify({'mensagem':'ERRO! Campo não encontrdo'})
    if campo == 'id':
        busca = int(busca)
        
    for charada in charadas:
        if charada[campo] == busca:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem':'ERRO! Usuário não encontrado'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)