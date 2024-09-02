from collections import deque
import time


# Funcao do algoritmo de busca em profundidade
def busca_profundidade(ponto_inicial, ponto_final, arestas):
    # Iniciar a medição de tempo
    tempo_inicio = time.perf_counter()

    # Pilha para controlar o processo de exploração (usada em DFS)
    # A pilha armazena tuplas onde o primeiro elemento é o nó atual e o segundo é o caminho até esse nó
    pilha = [(ponto_inicial, [ponto_inicial], 0)]
    visitados = set()   # Conjunto para rastrear os nós visitados e evitar ciclos

    iteracao = 0
    print("\n")
    # Loop principal da busca em profundidade
    while pilha:
        iteracao += 1

        # Remover o nó do topo da pilha (último inserido)
        tempo_iteracao_inicio = time.perf_counter()

        atual, caminho, distancia_acumulada = pilha.pop()

        # Se o nó atual é o ponto final, o caminho foi encontrado
        if atual == ponto_final:
            # Terminar a medição de tempo
            tempo_fim = time.perf_counter()
            tempo_total = (tempo_fim - tempo_inicio) * 1000

            # Imprimir informaçoes finais
            print(f"\nFim da execução")
            print(f"Caminho: {' – '.join(caminho)}")
            print(f"Distancia: {distancia_acumulada}")
            print(f"Tempo de execução total: {tempo_total:.3f} ms\n")
            return

        # Marcar como visitado para evitar revisitar e loops
        visitados.add(atual)

        # Expansão dos vizinhos do nó atual
        for vizinho, custo in arestas.get(atual, []):
            if vizinho not in visitados:
                # Adicionar o vizinho na pilha, junto com o caminho atualizado até ele
                pilha.append(
                    (vizinho, caminho + [vizinho], distancia_acumulada + custo))

        # Capturar o tempo de fim da iteração e calcular a duração da iteração
        tempo_iteracao_fim = time.perf_counter()
        # Converter para milissegundos
        tempo_iteracao = (tempo_iteracao_fim - tempo_iteracao_inicio) * 1000

        # Imprimir informações da iteração atual
        pilha_estado = [f"({n}, caminho: {caminho}, distância: {
            dist})" for n, caminho, dist in pilha]
        print(f"Iteração {iteracao}:")
        print(f"Pilha: {pilha_estado}")
        print(f"Tempo de execução da iteração: {tempo_iteracao:.3f} ms\n")

    # Se a pilha esvaziar e o ponto final não for encontrado, informar que nenhum caminho foi encontrado
    print("Nenhum caminho encontrado.")
