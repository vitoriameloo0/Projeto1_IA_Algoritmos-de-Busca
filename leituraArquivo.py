# Funcao para fazer a leitura do arquivo
def leitura(ponto_inicial, ponto_final, arestas, heuristicas):
    nomeArquivo = str(input('Digite o nome do arquivo: '))
    try:
        with open(nomeArquivo, 'r') as arquivo:
            for linha in arquivo:
                # Removendo espaços em branco e quebrando a linha em partes
                linha = linha.strip()

                # Verificando o tipo de linha
                if linha.startswith("ponto_inicial"):
                    # Extraindo o ponto inicial
                    ponto_inicial = linha.split("(")[1].split(")")[0]

                elif linha.startswith("ponto_final"):
                    # Extraindo o ponto final
                    ponto_final = linha.split("(")[1].split(")")[0]

                elif linha.startswith("pode_ir"):
                    # Processando uma aresta (origem, destino, peso)
                    partes = linha.split("(")[1].split(")")[0].split(",")
                    origem, destino, peso = partes[0], partes[1], int(
                        partes[2])

                    # Se a origem não estiver nas arestas, inicialize com uma lista vazia
                    if origem not in arestas:
                        arestas[origem] = []
                    # Adiciona o destino e o peso da aresta à lista de arestas
                    arestas[origem].append((destino, peso))

                elif linha.startswith("h"):
                    # Processando a heurística (origem, destino, valor_heurístico)
                    partes = linha.split("(")[1].split(")")[0].split(",")
                    vertice1 = partes[0]  # Primeiro vértice (origem)
                    vertice2 = partes[1]  # Segundo vértice (destino final)
                    # Valor heurístico entre os vértices
                    valor_h = int(partes[2])

                    # Armazena o valor heurístico no dicionário heurísticas
                    heuristicas[(vertice1, vertice2)] = valor_h

        # Confirmar que o arquivo foi lido com sucesso
        print('\nArquivo Lido!')
        return ponto_inicial, ponto_final, arestas, heuristicas

    # Tratamento do erro caso o arquivo não seja encontrado
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return None, None, None, None

    # Tratamento genérico para qualquer outro erro inesperado
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, None, None, None
