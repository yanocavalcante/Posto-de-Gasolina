from time import sleep
from menu import *
while True:
    limparTela()
    cabeçalho('Menu Principal')
    print('1-Cadastros     2-Financeiro     3-Movimentos     4-Sair')
    act = int(input(''))
    while act != 1 and act != 2 and act != 3 and act !=4:            #Controle de comandos
        act = int(input('Ação Inválida. Por favor, tente novamente.'))
    if act == 1:
        cadastros()
    elif act == 2:
        financeiro()
    elif act == 3:
        movimento()
    elif act == 4:
        break
print('Finalizando o Programa...')
sleep(3)
cabeçalho('Fim. Até Logo!')