from leituraArquivo import leitura
from melhoresSolucoes import a_estrela
from pioresSolucoes import busca_profundidade


def main():
    # Prints para as funcoes principais
    print('\nINTELIGENCIA ARTIFICIAL')
    print('      PROJETO 1        ')
    print('ALGORITMOS DE BUSCA    \n')

    # Inicializacao das variaveis
    ponto_inicial = None
    ponto_final = None
    arestas = {}
    heuristicas = {}

    opcao = 0
    while opcao != 4:
        print('Menu de Opções: ')
        print('1 - Entrada de Arquivo')
        print('2 - Algoritmo de Melhor Solução - A*')
        print('3 - Algoritmo de Pior Solução - Busca em Profundidade')
        print('4 - Sair do Programa')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            ponto_inicial, ponto_final, arestas, heuristicas = leitura(
                ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 2:
            if ponto_inicial is None and ponto_final is None:
                print('Sem arquivo de entrada...')
            else:
                a_estrela(ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 3:
            if ponto_inicial is None and ponto_final is None:
                print('Sem arquivo de entrada...')
            else:
                busca_profundidade(ponto_inicial, ponto_final, arestas)
        elif opcao == 4:
            print('Finalizando...')
        else:
            print('Opcao Invalida. Tente novamente')

        #print('\n')
        print('=-='*10)
    print('Programa encerrado!\n')


if __name__ == "__main__":
    main()
