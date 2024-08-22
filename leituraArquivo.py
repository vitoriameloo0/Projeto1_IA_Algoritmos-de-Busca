# Funcao para fazer a leitura do arquivo
def leitura():
    nomeArquivo = str(input('Digite o nome do arquivo: '))
    print('\n')
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            print(linha, end='')
    print('\nArquivo Lido!\n')
