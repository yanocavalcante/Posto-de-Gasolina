from time import sleep
from financeiro import *
from produtos import *
from entidades import *
from random import randint

      #Instanciações de Teste
#Funcionários
yano = Funcionários('Yano Cavalcante', '18' ,'Real Parque', 'Rua Madre Teresa de Calcutá', '(92)99217-5867', '564.142.779-27', 'CEO', '4873152-6')
jiliard = Funcionários('Jiliard Mai', '19', 'Coqueiros', 'Rua Desembargador Pedro Silva', '(48) 99458-7411', '147.127.695-76', 'Gerente', '4781425-5')
#Clientes
a5 = Clientes('Asinco ltda', '5', 'Ipiranga','Rua Otto Júlio Malina', '(48) 99547-5642', '07.428.914/0002-88', 'a5@gmail.com')
magalu = Clientes('Magazine Luiza', '65', 'Estreito', 'Rua Machado de Assis', '(48) 99658-6731', '47.960.950/0001-21','magalu@gmail.com')
#Combustíveis
gasolina = Combustíveis('Combustíveis', 'Gasolina Comum','Atem Distribuidora', 3.58, 5.42, 20000,  '320101001')
diesel = Combustíveis('Combustíveis', 'Diesel S10', 'Atem Distribuidora', 5.21, 6.15, 20000, '420105001')
gnv = Combustíveis('Combustíveis', 'GNV', 'Atem Distribuidora', 3.50 ,5 , 2000,'220101005')
#Lubrificantes
havoline = Lubrificantes('Lubrificantes','Havoline 5W-30','Texaco ,', 25, 35, 15 ,  'Sintético', '1L' )
lubrax = Lubrificantes('Lubrificantes', 'Lubrax 15W-40','Petrobras', 14, 30, 40 ,  'Semissintético', '500 mL')
#Caixas
trindade = Caixa(10000, 'Trindade', 'Posto', 'Não')
trindade = Caixa(500000, 'Trindade', 'Banco', 'Não')
córrego = Caixa(1500, 'Córrego', 'Posto', 'Não' )

#Funções do Menu
def cadastros():
    while True:
        sleep(1)
        cabeçalho('Cadastros')
        print('1-Funcionários    2-Clientes    3-Produtos    4-Voltar')
        act = int(input(''))
        while act != 1 and act != 2 and act != 3 and act != 4:      #Controle de comandos
            act = int(input('Ação Inválida. Por favor, tente novamente.'))
        if act == 1:
            sleep(1)
            cabeçalho('Funcionários')
            print('1-Alterar    2-Incluir    3-Consultar    4-Excluir    5-Voltar')
            act = int(input(''))
            while act != 1 and act != 2 and act != 3 and act != 4 and act != 5:        #Controle de comandos
                act = int(input('Ação Inválida. Por favor, tente novamente.'))
            if act == 1:
                sleep(1)
                cabeçalho('Alteração Cadastral')
                nomeInfo = str(input('Nome do Funcionário:'))
                info = str(input('Informação que deseja alterar:'))
                cont = 0
                for funcionário in listaFuncionários:
                    if funcionário.nome == nomeInfo:
                        cont += 1
                        funcionário.setInfo(info)
                if cont < 1:
                    sleep(1)
                    print('Funcionário não encontrado.')
            elif act == 2:
                sleep(1)
                cabeçalho('Cadastro de Funcionários')
                nome = str(input('Nome:'))
                cont = 0
                for funcionário in listaFuncionários:
                    if funcionário.nome == nome:
                        cont += 1
                        print('Funcionário já cadastrado!')
                        break
                if cont > 1:
                    break
                else:
                    idade = int(input('Idade:'))
                    bairro = str(input('Bairro:'))
                    rua = str(input('Rua:'))
                    telefone = str(input('Telefone:'))
                    cpf = str(input('CPF:'))
                    rg = str(input('RG:'))
                    cargo = str(input('Cargo:'))
                    
                    obj = Funcionários(nome,idade,bairro,rua,telefone,cpf,rg,cargo)
                    print('Funcionário cadastrado com sucesso!')
            elif act == 3:
                sleep(1)
                cabeçalho('Consulta de Funcionários')
                nomeInfo = str(input('Nome do Funcionário:'))
                cont = 0
                for funcionário in listaFuncionários:
                    if funcionário.nome == nomeInfo:
                        cont += 1
                        funcionário.getInfo(funcionário)
                if cont < 1:
                    sleep(1)
                    print('Funcionário não encontrado.')
            elif act == 4:
                sleep(1)
                cabeçalho('Exclusão de Funcionários')
                nomeInfo = str(input('Nome:'))
                cont = 0
                for funcionário in listaFuncionários:
                    if funcionário.nome == nomeInfo:
                        cont += 1
                        funcionário.exclui()
                if cont < 1:
                    sleep(1)
                    print('Funcionário não encontrado.')
            elif act == 5:
                break
            
        elif act == 2:
            sleep(1)
            cabeçalho('Clientes')
            print('1-Alterar    2-Incluir    3-Consultar    4-Excluir    5-Voltar')
            act = int(input(''))
            while act != 1 and act != 2 and act != 3 and act != 4 and act != 5:     #Controle de comandos
                act = int(input('Ação Inválida. Por favor, tente novamente.'))
            if act == 1:
                sleep(1)
                cabeçalho('Alteração Cadastral')
                nomeInfo = str(input('Nome do Cliente:'))
                info = str(input('Informação que deseja alterar:'))
                cont = 0
                for cliente in listaClientes:
                    if cliente.nome == nomeInfo:
                        cont += 1
                        cliente.setInfo(info)
                if cont < 1:
                    sleep(1)
                    print('Cliente não encontrado.')
            elif act == 2:
                sleep(1)
                cabeçalho('Cadastro de Clientes')
                nome = str(input('Nome:'))
                cont = 0
                for cliente in listaClientes:
                    if nome == cliente.nome:
                        cont += 1
                        print('Cliente já cadastrado!')
                        break
                if cont > 1:
                    break
                else:
                    idade = str(input('Idade:'))
                    bairro = str(input('Bairro:'))
                    rua = str(input('Rua:'))
                    telefone = str(input('Telefone:'))
                    cnpj = str(input('CNPJ:'))
                    email = str(input('E-mail:'))
                    obj = Clientes(nome,idade,bairro,rua,telefone,cnpj,email)
                    print('Cliente cadastrado com sucesso!')
            elif act == 3:
                sleep(1)
                cabeçalho('Consulta de Clientes')
                nomeInfo = str(input('Nome do Cliente:'))
                cont = 0
                for cliente in listaClientes:
                    if cliente.nome == nomeInfo:
                        cont += 1
                        cliente.getInfo(cliente)
                if cont < 1:
                    sleep(1)
                    print('Cliente não encontrado')
            elif act == 4:
                sleep(1)
                cabeçalho('Exclusão de Clientes')
                nomeInfo = str(input('Nome:'))
                cont = 0
                for cliente in listaClientes:
                    if cliente.nome == nomeInfo:
                        cont += 1
                        cliente.exclui()
                if cont < 1:
                    sleep(1)
                    print('Cliente não encontrado.')
            elif act == 5:
                break
        elif act == 3:
            sleep(1)
            cabeçalho('Produtos')
            print('1-Alterar    2-Incluir    3-Consultar    4-Excluir    5-Voltar')
            act = int(input(''))
            while act != 1 and act != 2 and act != 3 and act != 4 and act != 5:       #Controle de comandos
                act = int(input('Ação Inválida. Por favor, tente novamente.'))
            if act == 1:
                sleep(1)
                cabeçalho('Alteração Cadastral')
                nomeInfo = str(input('Nome do Produto:'))
                categoriaInfo = str(input('Categoria:'))
                info = str(input('Informação que deseja alterar:'))
                cont = 0
                if categoria == 'Combustíveis':
                    for combustível in listaCombustíveis:
                        if combustível.nome == nomeInfo:
                            cont += 1
                            combustível.setInfo(info)
                elif categoria == 'Lubrificantes':
                    for lubrificante in listaLubrificantes:
                        if lubrificante.nome == nomeInfo:
                            cont += 1
                            lubrificante.setInfo(info)
                if cont < 1:
                    sleep(1)
                    print('Produto não encontrado.')
            elif act == 2:
                sleep(1)
                cabeçalho('Cadastro de Produtos')
                categoria = str(input('Categoria:'))
                nome = str(input('Nome:'))
                fornecedor = str(input('Fornecedor:'))
                custo = float(input('Preço de Custo:'))
                preço = float(input('Preço de Venda:'))
                estoque = float(input('Estoque:'))
                if categoria == 'Lubrificantes':
                   tipo = str(input('Tipo:'))
                   embalagem = str(input('Embalagem:'))
                   obj = Lubrificantes(categoria,nome,fornecedor,custo,preço,estoque,tipo,embalagem)
                else:
                    códAnp = str(input('Código ANP:'))
                    obj = Combustíveis(categoria,nome,fornecedor,custo,preço,estoque,códAnp)
                print('Produto cadastrado com sucesso!')
            elif act == 3:
                sleep(1)
                cabeçalho('Consulta de Produtos')
                categoriaInfo = str(input('Categoria:'))
                nomeInfo = str(input('Nome:'))
                if categoriaInfo == 'Combustíveis':        
                    for produto in listaCombustíveis:
                        if produto.nome == nomeInfo:
                            produto.getInfo()
                elif categoriaInfo == 'Lubrificantes':
                    for produto in listaLubrificantes:
                        if produto.nome == nomeInfo:
                            produto.getInfo()
            elif act == 4:
                sleep(1)
                cabeçalho('Exclusão de Produto')
                categoriaInfo = str(input('Categoria:'))
                nomeInfo = str(input('Nome:'))
                if categoriaInfo == 'Lubrificantes':
                    for produto in listaCombustíveis:
                        if produto.nome == nomeInfo:
                            produto.exclui()
                elif categoriaInfo == 'Combustíveis':
                    for produto in listaLubrificantes:
                        if produto.nome == nomeInfo:
                            produto.exclui()
            elif act == 5:
                break

        elif act == 4:
            break    
def financeiro():
    while True:
        sleep(1)
        cabeçalho('Financeiro')
        print('1-Novo Caixa    2-Controle de Caixas    3-Voltar')
        act = int(input(''))
        while act != 1 and act != 2 and act != 3 :        #Controle de comandos
                act = int(input('Ação Inválida. Por favor, tente novamente.'))
        if act == 1:
            sleep(1)
            cabeçalho('Novo Caixa')
            saldo = int(input('Saldo:'))
            filial = str(input('Filial:'))
            origem = str(input('Origem:'))
            crédito = str(input('(Sim/Não) Crédito:'))
            while crédito != 'Sim' and crédito != 'Não':
                crédito = str(input('Resposta Inválida. Tente Novamente:'))
            obj = Caixa(saldo,filial,origem,crédito)

        elif act == 2:
            sleep(1)
            cabeçalho('Seleção de Caixa')
            filial = str(input('Filial:'))
            origem = str(input('Origem:'))
            cont = 0
            for caixa in listaCaixas:
                if caixa.filial == filial and caixa.origem == origem:
                    cont += 1
                    while True:
                        cabeçalho('Ações')
                        print(f'Filial:{caixa.filial}')
                        print(f'Origem:{caixa.origem}')
                        print('='*21)
                        print('1-Entradas', end = '  ')
                        print('2-Saídas', end = '   ')
                        print('3-Histórico', end = '   ')
                        print('4-Voltar')
                        act = int(input(''))
                        while act != 1 and act != 2 and act != 3 and act != 4:        #Controle de comandos
                            act = int(input('Ação Inválida. Por favor, tente novamente.'))
                        if act == 1:
                            descrição = str(input('Descrição:'))
                            valor = float(input('Valor:'))
                            caixa.entrada(descrição,valor)
                        elif act == 2:
                            descrição = str(input('Descrição:'))
                            valor = float(input('Valor:'))
                            caixa.saída(descrição,valor)
                        elif act == 3:
                            cabeçalho('Histórico de Transações')
                            print(f'Filial:{caixa.filial}')
                            print(f'Modalidade: {caixa.origem}')
                            print('='*21)
                            print(f'Saldo Inicial: {caixa.getSaldoInicial()}')
                            caixa.histórico.imprime()
                            print(f'Saldo Final:{caixa.getSaldo()}')
                        elif act == 4:
                            break
            if cont == 0:
                print('Caixa não encontrado. Tente Novamente')
        elif act == 3:
            break
def movimento():
    while True:
        sleep(1)
        cabeçalho('Movimentos')
        print('1-Nota de Entrada', end = '   ')
        print('2-Nota de Saída', end= '   ')
        print('3-Voltar')
        act = int(input(''))
        while act != 1 and act != 2 and act != 3:
            act = int(input('Ação Inválida. Por favor, tente novamente.'))
        if act == 1:
            cabeçalho('Informações')
            notaEntrada = []
            filial = str(input('Filial:'))
            cont = 0
            for c in listaCaixas:
                if filial == c.filial:
                    cont += 1
            if cont < 1:
                print('Filial não encontrada.')
                break
            while True:
                print('='*21)
                subcabeçalho('Produtos')
                categoriaInfo = str(input('Categoria:'))
                while categoriaInfo != 'Lubrificantes' and categoriaInfo != 'Combustíveis':
                    categoriaInfo = str(input('Categoria Não Encontrada. Tente Novamente:'))
                nomeInfo = str(input('Nome:'))
                if categoriaInfo == 'Combustíveis':
                    for produto in listaCombustíveis:
                        if produto.nome == nomeInfo:
                            produto.entrada(int(input('Quantidade:')))
                            notaEntrada.append(produto)

                elif categoriaInfo == 'Lubrificantes':
                    for produto in listaLubrificantes:
                        if produto.nome == nomeInfo:
                            produto.entrada(int(input('Quantidade:')))
                            notaEntrada.append(produto)
                print('1-Sim')
                print('2-Não')
                act = int(input('Deseja Incluir mais algum produto?'))
                while act != 1 and act != 2:
                    act = int(input('Ação Inválida. Por favor, tente novamente.'))
                if act == 2:
                    break
            totalNota = 0
            cabeçalho('Nota de Entrada')
            numNota = randint(11111,99999)
            print(f'Nº da Nota: {numNota}')
            for p in notaEntrada:
                totalNota += p.custo*p.qentrando
                print(f'||{p.nome}|| {p.qentrando} unidades x {p.custo}/un = R${p.custo*p.qentrando} ')
            print('='*21)
            print(f'Valor Total da Nota:{totalNota}')
            cabeçalho('Título de Cobrança')
            origem = str(input('Origem para Cobrança:'))
            for c in listaCaixas:
                if c.filial == filial and c.origem == origem:
                    c.saída(f'Nota nº {numNota}',totalNota)
                
        elif act == 2:
            cabeçalho('Informações')
            nomeInfo = str(input('Cliente:'))
            for entidade in listaEntidades:
                if nomeInfo == entidade.nome:
                    notaSaída = []
                    while True:
                        print('='*21)
                        subcabeçalho('Produtos')
                        categoriaInfo = str(input('Categoria:'))
                        while categoriaInfo != 'Lubrificantes' and categoriaInfo != 'Combustíveis':
                            categoriaInfo = str(input('Categoria Não Encontrada. Tente Novamente:'))
                            
                        nomeInfo = str(input('Nome:'))
                        if categoriaInfo == 'Combustíveis':
                            for produto in listaCombustíveis:
                                if produto.nome == nomeInfo:
                                    produto.saída(int(input('Quantidade:')))
                                    notaSaída.append(produto)

                        elif categoriaInfo == 'Lubrificantes':
                            for produto in listaLubrificantes:
                                if produto.nome == nomeInfo:
                                    produto.saída(int(input('Quantidade:')))
                                    notaSaída.append(produto)
                        print('1-Sim')
                        print('2-Não')
                        act = int(input('Deseja Incluir mais algum produto?'))
                        while act != 1 and act != 2:
                            act = int(input('Ação Inválida. Por favor, tente novamente.'))
                        if act == 2:
                            break
                    totalNota = 0
                    cabeçalho('Nota de Saída')
                    numNota = randint(11111,99999)
                    print(f'Nº da Nota: {numNota}')
                    for p in notaSaída:
                        totalNota += (p.preço)*(p.qsaindo)
                        print(f'||{p.nome}|| {p.qsaindo} unidades x {p.preço}/un = R${p.preço*p.qsaindo} ')
                    print('='*21)
                    print(f'Valor Sem Desconto: R${totalNota}')
                    novoTotalNota = entidade.defineDesconto(totalNota)
                    print(f'Valor Com Desconto:R${novoTotalNota}')
                    cabeçalho('Título de Recebimento')
                    filial = str(input('Filial para Recebimento:'))
                    origem = str(input('Origem para Recebimento:'))
                    for c in listaCaixas:
                        if c.filial == filial and c.origem == origem:
                            c.entrada(f'Nota nº{numNota}',novoTotalNota)
        elif act == 3:
            break