from collections import deque
import time


# Funcao do algoritmo de busca em profundidade
def busca_profundidade(ponto_inicial, ponto_final, arestas):
    # Iniciar a medição de tempo
    tempo_inicio = time.perf_counter()

    # Pilha para controlar o processo de exploração (usada em DFS)
    # A pilha armazena tuplas onde o primeiro elemento é o nó atual e o segundo é o caminho até esse nó
    pilha = [(ponto_inicial, [ponto_inicial])]
    visitados = set()   # Conjunto para rastrear os nós visitados e evitar ciclos

    iteracao = 0

    # Loop principal da busca em profundidade
    while pilha:
        iteracao += 1

        # Remover o nó do topo da pilha (último inserido)
        tempo_iteracao_inicio = time.perf_counter()

        atual, caminho = pilha.pop()

        # Se o nó atual é o ponto final, o caminho foi encontrado
        if atual == ponto_final:
            # Terminar a medição de tempo
            tempo_fim = time.perf_counter()
            tempo_total = (tempo_fim - tempo_inicio) * 1000

            # Imprimir informaçoes finais
            print(f"\nFim da execução")
            print(f"Caminho: {' – '.join(caminho)}")
            print(f"Tempo de execução total: {tempo_total:.3f} ms\n")
            return

        # Marcar como visitado para evitar revisitar e loops
        visitados.add(atual)

        # Expansão dos vizinhos do nó atual
        for vizinho, _ in arestas.get(atual, []):
            if vizinho not in visitados:
                # Adicionar o vizinho na pilha, junto com o caminho atualizado até ele
                pilha.append((vizinho, caminho + [vizinho]))

        # Capturar o tempo de fim da iteração e calcular a duração da iteração
        tempo_iteracao_fim = time.perf_counter()
        # Converter para milissegundos
        tempo_iteracao = (tempo_iteracao_fim - tempo_iteracao_inicio) * 1000

        # Imprimir informações da iteração atual
        print(f"Iteração {iteracao}:")
        print(f"Pilha: {pilha}")
        print(f"Tempo de execução da iteração: {tempo_iteracao:.3f} ms\n")

    # Se a pilha esvaziar e o ponto final não for encontrado, informar que nenhum caminho foi encontrado
    print("Nenhum caminho encontrado.")


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
            busca_profundidade(ponto_inicial, ponto_final, arestas)
        elif opcao == 2:
            busca_em_largura(ponto_inicial, ponto_final, arestas)
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
