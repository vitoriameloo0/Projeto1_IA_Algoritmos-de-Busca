import heapq


def a_star(ponto_inicial, ponto_final, arestas, heuristicas):
    open_set = []
    heapq.heappush(open_set, (0, ponto_inicial))  # (F, nó)

    closed_set = set()

    g_score = {ponto_inicial: 0}
    f_score = {ponto_inicial: heuristicas.get(
        (ponto_inicial, ponto_final), float('inf'))}

    came_from = {}

    iteracao = 0
    medida_de_desempenho = 0.0

    while open_set:
        iteracao += 1
        _, current = heapq.heappop(open_set)

        # Calcular e mostrar a medida de desempenho
        medida_de_desempenho += g_score[current]

        # Exibir o estado atual da fila (open_set)
        print(f"Iteração {iteracao}:")
        print("Fila:", end=" ")
        for f, vertice in open_set:
            print(
                f"({vertice}: {g_score[vertice]} + {f - g_score[vertice]} = {f})", end=" ")
        print(f"\nMedida de desempenho: {medida_de_desempenho:.1f}\n")

        if current == ponto_final:
            print("Fim da execução")
            print(f"Distância: {g_score[ponto_final]}")
            print("Caminho:", " – ".join(reconstruir_caminho(came_from, current)))
            print(f"Medida de desempenho: {medida_de_desempenho:.1f}")
            return

        closed_set.add(current)

        for vizinho, peso in arestas.get(current, []):
            if vizinho in closed_set:
                continue

            tentative_g_score = g_score[current] + peso

            if tentative_g_score < g_score.get(vizinho, float('inf')):
                came_from[vizinho] = current
                g_score[vizinho] = tentative_g_score
                f_score[vizinho] = g_score[vizinho] + \
                    heuristicas.get((vizinho, ponto_final), float('inf'))

                if vizinho not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[vizinho], vizinho))

    print("Fim da execução: Nenhum caminho encontrado")
    print(f"Medida de desempenho: {medida_de_desempenho:.1f}")
    return None


def reconstruir_caminho(came_from, current):
    caminho = [current]
    while current in came_from:
        current = came_from[current]
        caminho.append(current)
    caminho.reverse()
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
            print('Falta Implementar')
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
