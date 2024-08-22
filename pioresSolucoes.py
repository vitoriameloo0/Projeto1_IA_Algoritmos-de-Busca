from collections import deque


def busca_em_profundidade(ponto_inicial, ponto_final, arestas):
    # Pilha usada para armazenar o caminho a ser explorado (stack)
    # Cada elemento é (nó_atual, caminho)
    stack = [(ponto_inicial, [ponto_inicial])]
    visited = set()  # Conjunto de nós já visitados

    nos_expandidos = 0  # Medida de otimidade: número de nós expandidos
    iteracao = 0  # Contador de iterações

    # Loop principal do algoritmo de busca em profundidade
    while stack:
        iteracao += 1  # Incrementa o contador de iterações

        # Exibir o estado atual da pilha (stack) **ANTES** da remoção
        print(f"Iteração {iteracao}:")
        print("Pilha:", end=" ")
        for vertice, caminho in stack:
            print(f"({vertice}: {caminho})", end=" ")
        print(f"\nMedida de otimidade (nós expandidos): {nos_expandidos}\n")

        # Remove o último elemento da pilha
        current, caminho = stack.pop()
        nos_expandidos += 1

        # Se o nó atual é o ponto final, exibe o caminho encontrado
        if current == ponto_final:
            print("Fim da execução")
            print("Caminho encontrado:", " – ".join(caminho))
            print(f"Medida de otimidade (nós expandidos): {nos_expandidos}")
            return caminho, nos_expandidos

        # Marca o nó atual como visitado
        visited.add(current)

        # Explora os vizinhos do nó atual
        for vizinho, _ in arestas.get(current, []):
            if vizinho not in visited:
                stack.append((vizinho, caminho + [vizinho]))

    # Se o loop terminar e o ponto final não foi encontrado, exibe uma mensagem de erro
    print("Fim da execução: Nenhum caminho encontrado")
    print(f"Medida de otimidade (nós expandidos): {nos_expandidos}")
    return None


def busca_em_largura(ponto_inicial, ponto_final, arestas):
    # Fila usada para armazenar o caminho a ser explorado (queue)
    # Cada elemento é (nó_atual, caminho)
    queue = deque([(ponto_inicial, [ponto_inicial])])
    visited = set()  # Conjunto de nós já visitados

    nos_expandidos = 0  # Medida de otimidade: número de nós expandidos
    iteracao = 0  # Contador de iterações

    # Loop principal do algoritmo de busca em largura
    while queue:
        iteracao += 1  # Incrementa o contador de iterações

        # Exibir o estado atual da fila (queue) **ANTES** da remoção
        print(f"Iteração {iteracao}:")
        print("Fila:", end=" ")
        for vertice, caminho in queue:
            print(f"({vertice}: {caminho})", end=" ")
        print(f"\nMedida de otimidade (nós expandidos): {nos_expandidos}\n")

        # Remove o primeiro elemento da fila
        current, caminho = queue.popleft()
        nos_expandidos += 1

        # Se o nó atual é o ponto final, exibe o caminho encontrado
        if current == ponto_final:
            print("Fim da execução")
            print("Caminho encontrado:", " – ".join(caminho))
            print(f"Medida de otimidade (nós expandidos): {nos_expandidos}")
            return caminho, nos_expandidos

        # Marca o nó atual como visitado
        visited.add(current)

        # Explora os vizinhos do nó atual
        for vizinho, _ in arestas.get(current, []):
            if vizinho not in visited:
                # Marca vizinho como visitado para evitar enfileirar múltiplas vezes
                visited.add(vizinho)
                queue.append((vizinho, caminho + [vizinho]))

    # Se o loop terminar e o ponto final não foi encontrado, exibe uma mensagem de erro
    print("Fim da execução: Nenhum caminho encontrado")
    print(f"Medida de otimidade (nós expandidos): {nos_expandidos}")
    return None

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
