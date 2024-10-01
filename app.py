from flask import Flask, jsonify, request, render_template
from problem import WaterJugProblem
import search as search

app = Flask(__name__)


def busca_em_largura(problema):
    solucao = search.breadth_first_tree_search(problema)
    acoes_ate_objetivo = []

    while solucao.parent is not None:
        acoes_ate_objetivo.insert(0, (solucao.action, solucao.state))
        solucao = solucao.parent
    
    return acoes_ate_objetivo

def busca_em_profundidade(problema):
    solucao = search.depth_first_graph_search(problema)
    acoes_ate_objetivo = []

    while solucao.parent is not None:
        acoes_ate_objetivo.insert(0, (solucao.action, solucao.state))
        solucao = solucao.parent
    
    return acoes_ate_objetivo

def busca_em_profundidade_limitada(problema):
    solucao = search.depth_limited_search(problema)
    acoes_ate_objetivo = []

    while solucao.parent is not None:
        acoes_ate_objetivo.insert(0, (solucao.action, solucao.state))
        solucao = solucao.parent
    
    return acoes_ate_objetivo

def busca_em_profundidade_limitada_iterativa(problema):
    solucao = search.iterative_deepening_search(problema)
    acoes_ate_objetivo = []

    while solucao.parent is not None:
        acoes_ate_objetivo.insert(0, (solucao.action, solucao.state))
        solucao = solucao.parent
    
    return acoes_ate_objetivo

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/processar_problema', methods=['GET'])
def processar_problema():
    capacidade_x = int(request.args.get('capacidade_x'))
    capacidade_y = int(request.args.get('capacidade_y'))
    estado_final_x = int(request.args.get('estado_final_x'))
    estado_final_y = int(request.args.get('estado_final_y'))

    capacidade_maxima = (capacidade_x, capacidade_y)
    estado_final = (estado_final_x, estado_final_y)

    return render_template('processar_problema.html',
                           capacidade_x=capacidade_x,
                           capacidade_y=capacidade_y,
                           capacidade_maxima=capacidade_maxima,
                           estado_final_x=estado_final_x,
                           estado_final_y=estado_final_y,
                           estado_final=estado_final)

@app.route('/solucionar_problema', methods=['POST'])
def solucionar_problema():
    data = request.get_json()
    algoritmo = data['algoritmo']
    capacidade_maxima = tuple(data['capacidade_maxima'])
    estado_final = tuple(data['estado_final'])

    problema = WaterJugProblem(initial=(0, 0), goal=estado_final, capacities=capacidade_maxima)

    if algoritmo == 1:
        solucao = busca_em_largura(problema)
    elif algoritmo == 2:
        solucao = busca_em_profundidade(problema)
    elif algoritmo == 3:
        solucao = busca_em_profundidade_limitada(problema)
    else:
        solucao = busca_em_profundidade_limitada_iterativa(problema)
    
    lista_acoes = []
    for etapas in solucao:
        acoes = {}
        acoes['acao'] = etapas[0]
        acoes['estado_atual'] = etapas[1]
        lista_acoes.append(acoes)

    return jsonify({'lista_acoes': lista_acoes})

if __name__ == '__main__':
    app.run(debug=True)