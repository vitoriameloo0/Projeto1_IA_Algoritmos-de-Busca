from leituraArquivo import leitura
from melhoresSolucoes import melhorSolucao
from pioresSolucoes import piorSolucao


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
        print('2 - Algoritmos de Melhores Soluções')
        print('3 - Algoritmo de Pior Soluções')
        print('4 - Sair do Programa')

        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            ponto_inicial, ponto_final, arestas, heuristicas = leitura(
                ponto_inicial, ponto_final, arestas, heuristicas)
            # print("\nPonto Inicial:", ponto_inicial)
            # print("Ponto Final:", ponto_final)
            # print("Arestas:", arestas)
            # print("Heurísticas:", heuristicas)
        elif opcao == 2:
            if ponto_inicial is None and ponto_final is None:
                print('Sem arquivo de entrada...')
            else:
                melhorSolucao(ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 3:
            if ponto_inicial is None and ponto_final is None:
                print('Sem arquivo de entrada...')
            else:
                piorSolucao(ponto_inicial, ponto_final, arestas, heuristicas)
        elif opcao == 4:
            print('Finalizando...')
        else:
            print('Opcao Invalida. Tente novamente')

        print('\n')
        print('=-='*10)
    print('Programa encerrado!\n')


if __name__ == "__main__":
    main()
