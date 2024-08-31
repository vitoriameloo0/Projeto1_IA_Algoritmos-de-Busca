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
                    ponto_inicial = linha.split("(")[1].split(")")[0]

                elif linha.startswith("ponto_final"):
                    ponto_final = linha.split("(")[1].split(")")[0]

                elif linha.startswith("pode_ir"):
                    partes = linha.split("(")[1].split(")")[0].split(",")
                    origem, destino, peso = partes[0], partes[1], int(
                        partes[2])

                    if origem not in arestas:
                        arestas[origem] = []
                    arestas[origem].append((destino, peso))

                elif linha.startswith("h"):
                    partes = linha.split("(")[1].split(")")[0].split(",")
                    vertice1 = partes[0]  # Primeiro vértice
                    # Segundo vértice (neste exemplo, será o destino final)
                    vertice2 = partes[1]
                    # Valor heurístico entre os vértices
                    valor_h = int(partes[2])
                    heuristicas[(vertice1, vertice2)] = valor_h

        print('\nArquivo Lido!\n')
        return ponto_inicial, ponto_final, arestas, heuristicas
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return None, None, None, None

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, None, None, None
