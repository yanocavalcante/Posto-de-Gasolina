import os
def cabeçalho(msg):             #Função de Estilização
    print('='*42)
    print(msg.center(42))
    print('='*42)
def subcabeçalho(msg):          #Função de Estilização
    print(msg.center(21))
    print('='*21)

listaRef = list()

def proxRef():                  #Função Acessória
    if len(listaRef) == 0:
        ultimaRef = 1
        listaRef.append(ultimaRef)
        return ultimaRef
    else:
        ultimaRef = (listaRef[-1]) + 1
        listaRef.append(ultimaRef)
        return ultimaRef

def limparTela():              #Função de Limpeza de Terminal
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

listaLubrificantes = []
listaCombustíveis = []

class Produtos:             #SuperClasse
    def __init__(self,categoria,nome,fornecedor,custo,preço,estoque):
        self.ref = proxRef()
        self.categoria = categoria
        self.nome = nome
        self.fornecedor = fornecedor
        self.custo = custo
        self.preço = preço
        self.estoque = estoque

class Combustíveis(Produtos):
    def __init__(self,categoria,nome,fornecedor,custo,preço,estoque,códAnp):
        super().__init__(categoria,nome,fornecedor,custo,preço,estoque)
        self.códAnp = códAnp
        listaCombustíveis.append(self)

    def getInfo(self):
        cabeçalho(f'{self.nome} Ref: {self.ref}')
        print('Código da ANP:',self.códAnp)
        print('Fornecedor:',self.fornecedor)
        print('Preço de Custo: R$',self.custo)
        print('Preço de Venda: R$',self.preço)
        print('Estoque:',self.estoque,'Litros')

    def setInfo(self,info):
        novaInfo = str(input(f'Novo(a) {info}:'))
        if info == 'Fornecedor':
            self.fornecedor = novaInfo
        elif info == 'Custo':
            novaInfo = int(novaInfo)
            self.custo = novaInfo
        elif info == 'Preço':
            novaInfo = int(novaInfo)
            self.preço = novaInfo
        elif info == 'Código da ANP:':
            self.códAnp = novaInfo
        else:
            print('Informação Inválida. Não foi possível concluir a alteração!')
            return
        print('Alteração realizada com sucesso!')

    def saída(self,quantidade):
        if quantidade > self.estoque:
            print('Quantidade em estoque insuficiente!')
            return
        self.qsaindo = quantidade
        self.estoque -= quantidade

    def entrada(self,quantidade):
        self.qentrando = quantidade
        self.estoque += quantidade

    def exclui(self):
        listaCombustíveis.remove(self)
        print(f'O produto {self.nome} foi excluído com sucesso!')

class Lubrificantes(Produtos):
    def __init__(self,categoria,nome,fornecedor,custo,preço,estoque,tipo,embalagem):
        super().__init__(categoria,nome,fornecedor,custo,preço,estoque)
        self.tipo = tipo
        self.embalagem = embalagem
        listaLubrificantes.append(self)

    def getInfo(self):
        cabeçalho(self.nome)
        print('Fornecedor:',self.fornecedor)
        print('Preço de Custo: R$',self.custo)
        print('Preço de Venda: R$',self.preço)
        print('Estoque:', self.estoque, 'Unidades')
        print('Tipo:',self.tipo)
        print('Embalagem:',self.embalagem)

    def setInfo(self,info):
        novaInfo = str(input(f'Novo(a) {info}:'))
        if info == 'Fornecedor':
            self.fornecedor = novaInfo
        elif info == 'Custo':
            novaInfo = int(novaInfo)
            self.custo = novaInfo
        elif info == 'Preço':
            novaInfo = int(novaInfo)
            self.preço = novaInfo
        elif info == 'Tipo:':
            self.tipo = novaInfo
        elif info == 'Embalagem':
            self.embalagem = novaInfo
        else:
            print('Informação Inválida. Não foi possível concluir a alteração!')
            return
        print('Alteração realizada com sucesso!')

    def saída(self,quantidade):
        if quantidade > self.estoque:
            print('Quantidade em estoque insuficiente!')
            return
        self.qsaindo = quantidade
        self.estoque -= quantidade
    
    def entrada(self,quantidade):
        self.qentrando = quantidade
        self.estoque += quantidade

    def exclui(self):
        listaLubrificantes.remove(self)
        print(f'O produto {self.nome} foi excluído com sucesso!')       