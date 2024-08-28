from collections import deque
import time


# Funcao do algoritmo de busca em profundidade
def busca_em_profundidade(ponto_inicial, ponto_final, arestas):
    # Início da contagem de tempo
    start_time = time.time()

    # Pilha para simular a recursão da DFS
    pilha = [(ponto_inicial, [ponto_inicial], 0)]

    # Conjunto de vértices já visitados (para evitar ciclos)
    visitados = set()

    iteracao = 1

    while pilha:
        # Retirar o elemento do topo da pilha (último inserido)
        vertice_atual, caminho, custo_atual = pilha.pop()

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

        # Expandir os nós vizinhos (processar na ordem inversa para simular recursão)
        for vizinho, custo in reversed(arestas.get(vertice_atual, [])):
            if vizinho not in visitados:
                pilha.append(
                    (vizinho, caminho + [vizinho], custo_atual + custo))

        # Medida de desempenho: tempo atual de execução
        tempo_execucao = time.time() - start_time

        # Imprimir estado da pilha
        pilha_str = " ".join(
            [f"({v}: {custo} = {custo_atual + custo})" for v, _, custo_atual in pilha])
        print(f"\nIteração {iteracao}:")
        print(f"Pilha: {pilha_str}")
        print(f"Medida de desempenho: {tempo_execucao:.2f}")

        iteracao += 1

    # Se o algoritmo terminar sem encontrar o caminho
    print("Caminho não encontrado.")


def busca_em_largura(ponto_inicial, ponto_final, arestas):
    # Início da contagem de tempo
    start_time = time.time()

    # Fila para a BFS
    fila = deque([(ponto_inicial, [ponto_inicial], 0)])

    # Conjunto de vértices já visitados (para evitar ciclos)
    visitados = set()

    iteracao = 1

    while fila:
        # Retirar o elemento da frente da fila (primeiro inserido)
        vertice_atual, caminho, custo_atual = fila.popleft()

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
                fila.append(
                    (vizinho, caminho + [vizinho], custo_atual + custo))
                # Marca vizinho como visitado para evitar múltiplas enfileiramentos
                visitados.add(vizinho)

        # Medida de desempenho: tempo atual de execução
        tempo_execucao = time.time() - start_time

        # Imprimir estado da fila
        fila_str = " ".join(
            [f"({v}: {custo} = {custo_atual + custo})" for v, _, custo_atual in fila])
        print(f"\nIteração {iteracao}:")
        print(f"Fila: {fila_str}")
        print(f"Medida de desempenho: {tempo_execucao:.2f}")

        iteracao += 1

    # Se o algoritmo terminar sem encontrar o caminho
    print("Caminho não encontrado.")

# Funcao para as opcoes de piores solucoes


def piorSolucao(ponto_inicial, ponto_final, arestas, heuristicas):
    opcao = 0
    while opcao != 3:
        print('\nAlgoritmos de Piores Soluções: ')
        print('1 - Busca em Profundidade')
        print('2 - Busca em Largura')
        print('3 - Voltar para o Menu de Opções')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            busca_em_profundidade(ponto_inicial, ponto_final, arestas)
        elif opcao == 2:
            busca_em_largura(ponto_inicial, ponto_final, arestas)
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
