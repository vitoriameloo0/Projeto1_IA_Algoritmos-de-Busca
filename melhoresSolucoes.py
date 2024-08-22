# Importa o módulo heapq para implementar a fila de prioridade (min-heap)
import heapq


def a_star(ponto_inicial, ponto_final, arestas, heuristicas):
    # Inicializa o open_set como uma fila de prioridade e adiciona o ponto inicial com F = 0
    open_set = []
    heapq.heappush(open_set, (0, ponto_inicial))  # (F, nó)

    # Inicializa o closed_set como um conjunto vazio (nós já explorados)
    closed_set = set()

    # Inicializa g_score com o custo do ponto inicial (que é 0)
    g_score = {ponto_inicial: 0}

    # Inicializa f_score com a soma do g_score e da heurística para o ponto inicial
    f_score = {ponto_inicial: heuristicas.get(
        (ponto_inicial, ponto_final), float('inf'))}

    # Inicializa um dicionário para armazenar o caminho (de onde viemos)
    came_from = {}

    # Inicializa variáveis de controle para contagem de iterações e medida de desempenho
    iteracao = 0
    medida_de_desempenho = 0.0

    # Loop principal do algoritmo A*
    while open_set:
        iteracao += 1  # Incrementa o contador de iterações
        # Remove o nó com o menor F (custo total estimado) da fila de prioridade
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

        # Se o nó atual é o ponto final, reconstruímos e exibimos o caminho encontrado
        if current == ponto_final:
            print("Fim da execução")
            print(f"Distância: {g_score[ponto_final]}")
            print("Caminho:", " – ".join(reconstruir_caminho(came_from, current)))
            print(f"Medida de desempenho: {medida_de_desempenho:.1f}")
            return

        # Adiciona o nó atual ao closed_set (marcando-o como explorado)
        closed_set.add(current)

        # Explora os vizinhos do nó atual
        for vizinho, peso in arestas.get(current, []):
            if vizinho in closed_set:
                continue  # Se o vizinho já foi explorado, pula para o próximo

            # Calcula o custo tentativo para chegar ao vizinho via o nó atual
            tentative_g_score = g_score[current] + peso

            # Se o caminho via o nó atual é melhor, atualiza as informações do vizinho
            if tentative_g_score < g_score.get(vizinho, float('inf')):
                # Armazena de onde viemos para reconstruir o caminho
                came_from[vizinho] = current
                # Atualiza o custo real do caminho até o vizinho
                g_score[vizinho] = tentative_g_score
                # Atualiza o custo total estimado
                f_score[vizinho] = g_score[vizinho] + \
                    heuristicas.get((vizinho, ponto_final), float('inf'))

                # Se o vizinho ainda não está na fila, adiciona-o
                if vizinho not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[vizinho], vizinho))

    # Se o loop terminar e o ponto final não foi encontrado, exibe uma mensagem de erro
    print("Fim da execução: Nenhum caminho encontrado")
    print(f"Medida de desempenho: {medida_de_desempenho:.1f}")
    return None


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
            print('Falta Implementar')
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)
