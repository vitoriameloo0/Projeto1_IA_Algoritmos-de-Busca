from leituraArquivo import leitura
from melhoresSolucoes import melhorSolucao
from pioresSolucoes import piorSolucao
import imprimir

# Prints para as funcoes principais
print('\nINTELIGENCIA ARTIFICIAL')
print('      PROJETO 1        ')
print('ALGORITMOS DE BUSCA    \n')

opcao = 0
while opcao != 4:
    print('\nMenu de Opções: ')
    print('1 - Entrada de Arquivo')
    print('2 - Algoritmos de Melhores Soluções')
    print('3 - Algoritmo de Pior Soluções')
    print('4 - Sair do Programa')

    opcao = int(input('Escolha uma opção: '))
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
