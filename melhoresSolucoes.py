import heapq  # Importa o módulo heapq para implementar a fila de prioridade
import time  # Import para medir o tempo de execuçao


# Função para calcular a entrada utilizando o Algoritmo A*
def a_estrela(ponto_inicial, ponto_final, arestas, heuristicas):
    tempo_inicio = time.perf_counter()          # Iniciar a medicao de tempo total

    # Inicialização da fila de prioridade e custos
    fila = []

    # Obter a heuristica inicial do ponto de partida ate o ponto final
    heuristica_inicial = heuristicas.get(
        (ponto_inicial, ponto_final), float('inf'))

    # Inserir o nó inicial na fila com seu custo total estimado, custo real e caminho percorrido
    heapq.heappush(fila, (heuristica_inicial, 0,
                   ponto_inicial, [ponto_inicial]))

    # Conjunto de nós ja visitados para evitar visitar novamente
    visitados = set()

    iteracao = 0

    # Loop principal que funcionara ate que a fila esteja vazia
    while fila:
        iteracao += 1   # A cada iteracao ele incrementa 1 para identificar quantas iterações foram preciso fazer para chegar no resultado

        # Inicializa a medição do tempo de execução da iteração atual
        tempo_iteracao_inicio = time.perf_counter()

        # Remove e retorna o nó com menor custo total estimado f(n) da fila
        f_atual, g_atual, atual, caminho = heapq.heappop(fila)

        # Se o nó atual é o final
        if atual == ponto_final:
            # Terminar a medição de tempo e calcula para milisegundos
            tempo_fim = time.perf_counter()
            tempo_total = (tempo_fim - tempo_inicio)*1000   # Converte para ms

            # Exibe as ultimas informações e retorna
            print(f"\nFim da execução")
            print(f"Distância: {g_atual}")
            print(f"Caminho: {' – '.join(caminho)}")
            print(f"Tempo de execução total: {tempo_total:2.3f} ms")
            return

        # Marca o nó atual como visitado
        visitados.add(atual)

        # Expansão dos vizinhos do nó atual obtidos a partir das arestas
        for vizinho, custo in arestas.get(atual, []):
            # Verifica se o vizinho ainda não foi visitado
            if vizinho not in visitados:
                # Calcula o custo real acumulado para chegar ao vizinho
                g_vizinho = g_atual + custo
                # Obtém a heurística estimada do vizinho ao destino
                heuristica_vizinho = heuristicas.get(
                    (vizinho, ponto_final), float('inf'))
                # Calcula o custo total estimado f(n) = g(n) + h(n)
                f_vizinho = g_vizinho + heuristica_vizinho
                # Adiciona o vizinho à fila de prioridade com seus custos e caminho atualizado
                heapq.heappush(fila, (f_vizinho, g_vizinho,
                               vizinho, caminho + [vizinho]))

        # Representação do estado atual da fila de prioridade
        fila_estado = ' '.join(
            [f"({n}: {g} + {heuristicas.get((n, ponto_final), float('inf'))} = {f})" for f, g, n, c in fila])

        # Capturar o tempo de fim da iteração e calcular a duração da iteração
        tempo_iteracao_fim = time.perf_counter()
        tempo_iteracao = (tempo_iteracao_fim - tempo_iteracao_inicio)*1000

        # Exibe informações sobre a iteração atual
        print(f"Iteração {iteracao}:")
        print(f"Fila: {fila_estado}")
        print(f"Tempo de execução: {tempo_iteracao:2.3f} ms\n")


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
