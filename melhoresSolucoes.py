# Importa o módulo heapq para implementar a fila de prioridade (min-heap)
import heapq
import time


def a_star(ponto_inicial, ponto_final, adjacencias, heuristicas):
    # Iniciar a medição de tempo
    tempo_inicio = time.perf_counter()
    # Inicialização da fila de prioridade e custos
    fila = []
    # Modificação para acessar corretamente a heurística do ponto inicial
    heuristica_inicial = heuristicas.get(
        (ponto_inicial, ponto_final), float('inf'))
    heapq.heappush(fila, (heuristica_inicial, 0,
                   ponto_inicial, [ponto_inicial]))
    visitados = set()

    iteracao = 0

    while fila:
        iteracao += 1
        # Remover o nó com menor f(n) da fila
        tempo_iteracao_inicio = time.perf_counter()

        f_atual, g_atual, atual, caminho = heapq.heappop(fila)

        # Se o nó final foi alcançado, terminamos
        if atual == ponto_final:
            # Terminar a medição de tempo
            tempo_fim = time.perf_counter()
            tempo_total = (tempo_fim - tempo_inicio)*1000

            print(f"\nFim da execução\nDistância: {g_atual}\nCaminho: {
                  ' – '.join(caminho)}\nTempo de execução total: {tempo_total:2.3f} ms")
            return

        # Marcar como visitado
        visitados.add(atual)

        # Expansão dos vizinhos
        for vizinho, custo in adjacencias.get(atual, []):
            if vizinho not in visitados:
                g_vizinho = g_atual + custo
                heuristica_vizinho = heuristicas.get(
                    (vizinho, ponto_final), float('inf'))
                f_vizinho = g_vizinho + heuristica_vizinho
                heapq.heappush(fila, (f_vizinho, g_vizinho,
                               vizinho, caminho + [vizinho]))

        # Estado atual da fila e medida de desempenho
        fila_estado = ' '.join(
            [f"({n}: {g} + {heuristicas.get((n, ponto_final), float('inf'))} = {f})" for f, g, n, c in fila])

        # Capturar o tempo de fim da iteração e calcular a duração da iteração
        tempo_iteracao_fim = time.perf_counter()
        tempo_iteracao = (tempo_iteracao_fim - tempo_iteracao_inicio)*1000

        print(f"Iteração {iteracao}:\nFila: {
              fila_estado}\nTempo de execução: {tempo_iteracao:2.3f} ms\n")


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
            a_star(ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 2:
            busca_custo_uniforme(ponto_inicial, ponto_final, arestas)
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
