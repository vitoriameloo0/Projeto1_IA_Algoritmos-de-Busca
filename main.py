from leituraArquivo import leitura
import melhoresSolucoes
import pioresSolucoes
import imprimir


# Funcao de menu para as opcoes de melhores solucoes
def melhorSolucao():
    opcao = 0
    while opcao != 3:
        print('\nMelhores Solucoes: ')
        print('1 - Busca A*')
        print('2 - Busca de Custo Uniforme')
        print('3 - Voltar para o Menu de Opcoes')

        opcao = int(input('Escolha uma opcao: '))
        if opcao == 1:
            print('Falta Implementar')
        elif opcao == 2:
            print('Falta Implementar')
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)


# Funcao para as opcoes de piores solucoes
def piorSolucao():
    opcao = 0
    while opcao != 3:
        print('\nPiores Solucoes: ')
        print('1 - Busca em Profundidade')
        print('2 - Busca em Largura')
        print('3 - Voltar para o Menu de Opcoes')

        opcao = int(input('Escolha uma opcao: '))
        if opcao == 1:
            print('Falta Implementar')
        elif opcao == 2:
            print('Falta Implementar')
        elif opcao == 3:
            print('Voltando...')
        else:
            print('Opcao Invalida. Tente novamente')
        print('=-='*10)
    print('\n'*2)


# Prints para as funcoes principais
print('INTELIGENCIA ARTIFICIAL')
print('      PROJETO 1        ')
print('ALGORITMOS DE BUSCA    \n')

opcao = 0
while opcao != 4:
    print('\nMenu de Opcoes: ')
    print('1 - Entrada de Arquivo')
    print('2 - Algoritmo de Melhor Solucao')
    print('3 - Algoritmo de Pior Solucao')
    print('4 - Sair do Programa')

    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        leitura()
    elif opcao == 2:
        melhorSolucao()
    elif opcao == 3:
        piorSolucao()
    elif opcao == 4:
        print('Finalizando...')
    else:
        print('Opcao Invalida. Tente novamente')
    print('=-='*10)
print('Programa encerrado!\n')
