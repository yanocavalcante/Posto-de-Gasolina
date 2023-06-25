listaEntidades = []
listaClientes = []
listaFuncionários = []

def cabeçalho(msg):         #Função de Estilização

    print('='*42)
    print(msg.center(42))
    print('='*42)

listaId = list()

def proxId():               #Função Acessória
    if len(listaId) == 0:
        ultimoId = 1
        listaId.append(ultimoId)
        return ultimoId
    else:
        ultimoId = (listaId[-1]) + 1
        listaId.append(ultimoId)
        return ultimoId


#Classes
class Entidades:                #SuperClasse
    def __init__(self,nome,idade,bairro,rua,telefone):
        self.id = proxId()
        self.nome = nome
        self.idade = idade
        self.bairro = bairro
        self.rua = rua
        self.telefone = telefone

    def defineDesconto(self,valorDaNota):
        self.desconto = valorDaNota - (valorDaNota/10)
        return self.desconto
    
class Funcionários(Entidades):              #SubClasse
    def __init__(self,nome,idade,bairro,rua,telefone,cpf,cargo,rg):
        super().__init__(nome,idade,bairro,rua,telefone)
        self.cpf = cpf
        self.rg = rg
        self.cargo = cargo
        listaFuncionários.append(self)
        listaEntidades.append(self)
        
    def getInfo(self,nomeFuncionário):
        cabeçalho(f'{nomeFuncionário.nome} ID: {self.id}')
        print('Idade:',nomeFuncionário.idade,'anos')
        print('Rua:',nomeFuncionário.rua)
        print('Bairro:',nomeFuncionário.bairro)
        print('Telefone:',nomeFuncionário.telefone)
        print('CPF:',nomeFuncionário.cpf)
        print('RG:',nomeFuncionário.rg)
        print('Cargo:',nomeFuncionário.cargo)

    def setInfo(self,info):
        novaInfo = str(input(f'Novo(a) {info}:'))
        if info == 'Idade':
            self.idade = novaInfo
        elif info == 'Bairro':
            self.bairro = novaInfo
        elif info == 'Rua':
            self.rua = novaInfo
        elif info == 'Telefone':
            self.telefone = novaInfo
        elif info == 'CPF:':
            self.cpf = novaInfo
        elif info == 'RG:':
            self.rg = novaInfo
        elif info == 'Cargo:':
            self.cargo = novaInfo
        else:
            print('Informação Inválida. Não foi possível concluir a alteração!')
            return
        print('Alteração realizada com sucesso!')

    def exclui(self):
        listaFuncionários.remove(self)
        print(f'O Funcionário {self.nome} foi excluído com sucesso!')
    
class Clientes(Entidades):              #SubClasse
    def __init__(self,nome,idade,bairro,rua,telefone,cnpj,email):
        super().__init__(nome,idade,bairro,rua,telefone)
        self.cnpj = cnpj
        self.email = email
        listaClientes.append(self)
        listaEntidades.append(self)

    def getInfo(self,nomeCliente):
        cabeçalho(f'{nomeCliente.nome} ID: {self.id}')
        print('Idade:',nomeCliente.idade,'anos')
        print('Bairro:',nomeCliente.bairro)
        print('Rua:',nomeCliente.rua)
        print('Telefone:',nomeCliente.telefone)
        print('CNPJ:',nomeCliente.cnpj)
        print('E-mail:',nomeCliente.email)

    def setInfo(self,info):
        novaInfo = str(input(f'Novo(a) {info}:'))
        if info == 'Idade':
            self.idade = novaInfo
        elif info == 'Bairro':
            self.bairro = novaInfo
        elif info == 'Rua':
            self.rua = novaInfo
        elif info == 'Telefone':
            self.telefone = novaInfo
        elif info == 'CNPJ:':
            self.cpf = novaInfo
        elif info == 'E-mail:':
            self.rg = novaInfo
        else:
            print('Informação Inválida. Não foi possível concluir a alteração!')
            return
        print('Alteração realizada com sucesso!')

    def defineDesconto(self,valorDaNota):
        self.valorDesconto = int(input('Porcentagem de Desconto:'))
        self.desconto = valorDaNota*(self.valorDesconto/100)
        return self.desconto
    
    def exclui(self):
        listaClientes.remove(self)
        print(f'O Cliente {self.nome} foi excluído com sucesso!')