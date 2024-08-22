# Funcao para fazer a leitura do arquivo
def leitura():
    ponto_inicial = None
    ponto_final = None
    arestas = {}
    heuristicas = {}

    nomeArquivo = str(input('Digite o nome do arquivo: '))

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
                origem, destino, peso = partes[0], partes[1], int(partes[2])

                if origem not in arestas:
                    arestas[origem] = []
                arestas[origem].append((destino, peso))

            elif linha.startswith("h"):
                partes = linha.split("(")[1].split(")")[0].split(",")
                vertice1 = partes[0]  # Primeiro vértice
                # Segundo vértice (neste exemplo, será o destino final)
                vertice2 = partes[1]
                valor_h = int(partes[2])  # Valor heurístico entre os vértices
                heuristicas[(vertice1, vertice2)] = valor_h

    # print("Vértice Inicial:", ponto_inicial)
    # print("Vértice Final:", ponto_final)
    # print("Arestas:", arestas)
    # print("Heurísticas:", heuristicas)
    print('\nArquivo Lido!\n')
    return ponto_inicial, ponto_final, arestas, heuristicas
