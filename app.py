from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'texto': 'buraco', 'resposta': 'Quanto mais se tira, maior ele fica. O que é?'},
    {'id': 2, 'texto': 'cerca', 'resposta': 'O que é que corre ao redor do quintal sem sair do lugar?'},
    {'id': 3, 'texto': 'rio', 'resposta': 'Quem é que faz a viagem deitado?'},  
    {'id': 4, 'texto': 'alho', 'resposta': 'O que é que tem cabeça e tem dente, mas não é gente?'},
    {'id': 5, 'texto': 'escada', 'resposta': 'Quem é que sobe e desce sem sair do lugar?'},  
    {'id': 6, 'texto': 'bactéria', 'resposta': 'O que é que quanto mais se divide, mais se multiplica?'},
    {'id': 7, 'texto': 'conversa', 'resposta': 'O que é que você pode segurar sem nunca tocar?'},
    {'id': 8, 'texto': 'mapa', 'resposta': 'O que é que tem cidades, mas não tem casas; tem rios, mas não tem água; tem florestas, mas não tem árvores?'},
    {'id': 9, 'texto': 'foto', 'resposta': 'O que é que quanto mais você tira, mais ele aumenta?'},  
    {'id': 10, 'texto': 'letra u', 'resposta': 'O que é que você sempre encontra no final de tudo?'}
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
    app.run()