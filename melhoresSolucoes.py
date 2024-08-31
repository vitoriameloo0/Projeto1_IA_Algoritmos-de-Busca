# Importa o módulo heapq para implementar a fila de prioridade (min-heap)
import heapq
import time


def a_estrela(ponto_inicial, ponto_final, conexoes, heuristicas):
    # Fila de prioridade (open list)
    fila = []
    # Usado para reconstruir o caminho
    antecessores = {}
    # Custo acumulado (g)
    g_score = {ponto_inicial: 0}
    # Heurística total (f = g + h)
    f_score = {ponto_inicial: heuristicas[ponto_inicial]}
    # Contador de nós explorados
    nos_explorados = 0

    # Adiciona o ponto inicial à fila de prioridade
    heapq.heappush(fila, (f_score[ponto_inicial], ponto_inicial))

    while fila:
        # Pega o nó com o menor valor de f
        _, atual = heapq.heappop(fila)
        nos_explorados += 1  # Incrementa o contador de nós explorados

        # Se chegamos ao ponto final, reconstrói o caminho
        if atual == ponto_final:
            caminho = []
            while atual in antecessores:
                caminho.append(atual)
                atual = antecessores[atual]
            caminho.append(ponto_inicial)
            caminho.reverse()
            return caminho, g_score[ponto_final], nos_explorados

        # Explora os vizinhos
        for vizinho, custo in conexoes.get(atual, []):
            tent_g_score = g_score[atual] + custo
            if tent_g_score < g_score.get(vizinho, float('inf')):
                # Este caminho é melhor que qualquer outro já visto
                antecessores[vizinho] = atual
                g_score[vizinho] = tent_g_score
                f_score[vizinho] = tent_g_score + heuristicas[vizinho]
                # Adiciona ou atualiza o vizinho na fila de prioridade
                heapq.heappush(fila, (f_score[vizinho], vizinho))

        # Exibe o estado atual da fila de prioridade e a pontuação g
        print(f"Estado da fila: {fila}")
        print(f"g_score: {g_score}")
        print(f"f_score: {f_score}")
        print("Caminho encontrado:", caminho)
        print("Custo total:", custo)
        print("Nós explorados:", nos_explorados)
        print("---")


def busca_custo_uniforme(ponto_inicial, ponto_final, arestas):
    # Início da contagem de tempo
    start_time = time.time()

    # Fila de prioridade (heap)
    fila = []
    heapq.heappush(fila, (0, ponto_inicial, []))

    # Conjunto de vértices já visitados
    visitados = set()

    iteracao = 1

    while fila:
        # Removendo o nó com menor custo total (g)
        custo_atual, vertice_atual, caminho = heapq.heappop(fila)

        # Atualizar o caminho
        caminho = caminho + [vertice_atual]

        # Verificar se chegou ao destino
        if vertice_atual == ponto_final:
            # Medida de desempenho: tempo total de execução até o momento
            tempo_execucao = time.time() - start_time
            print(f"\nFim da execução\nDistância: {custo_atual}")
            print("Caminho:", " – ".join(caminho))
            print(f"Medida de desempenho: {tempo_execucao:.2f}")
            return

        # Marcar o nó atual como visitado
        visitados.add(vertice_atual)

        # Expandir os nós vizinhos
        for vizinho, custo in arestas.get(vertice_atual, []):
            if vizinho not in visitados:
                g = custo_atual + custo
                heapq.heappush(fila, (g, vizinho, caminho))

        # Medida de desempenho: tempo atual de execução
        tempo_execucao = time.time() - start_time

        # Imprimir estado da fila
        fila_str = " ".join([f"({v}: {g} = {g})" for g, v, _ in fila])
        print(f"\nIteração {iteracao}:")
        print(f"Fila: {fila_str}")
        print(f"Medida de desempenho: {tempo_execucao:.2f}")

        iteracao += 1

    # Se o algoritmo terminar sem encontrar o caminho
    print("Caminho não encontrado.")


def reconstruir_caminho(came_from, current):
    # Reconstrói o caminho a partir do ponto final até o inicial, rastreando de onde viemos
    caminho = [current]
    while current in came_from:
        current = came_from[current]
        caminho.append(current)
    caminho.reverse()   # Inverte o caminho para que ele vá do ponto inicial ao final
    return caminho

# Funcao de menu para as opcoes de melhores solucoes


def melhorSolucao(ponto_inicial, ponto_final, arestas, heuristicas):
    opcao = 0
    while opcao != 3:
        print('\nAlgoritmos de Melhores Soluções: ')
        print('1 - Busca A*')
        print('2 - Busca de Custo Uniforme')
        print('3 - Voltar para o Menu de Opções')

        opcao = int(input('Escolha uma opção: '))
        print('\n')
        if opcao == 1:
            a_estrela(ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 2:
            busca_custo_uniforme(ponto_inicial, ponto_final, arestas)
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
