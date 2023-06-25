#Composição (Caixa--Conta)

listaCaixas = []


class Caixa():
    def __init__(self,saldo,filial,origem,crédito):
        self.saldo = saldo
        self.saldoInicial = saldo
        self.filial = filial
        self.origem = origem
        self.crédito = crédito
        if self.crédito == 'Sim':
            self.limite = float(input('Limite:'))
        self.histórico = Histórico()
        listaCaixas.append(self)
        
    def entrada(self,descrição,valor):
        self.saldo += valor
        self.descrição = descrição
        self.histórico.transações.append(f'{descrição}|+ {valor}')

    def saída(self,descrição,valor):
        if self.saldo < valor:
            if self.crédito == 'Não':
                print('Saldo Insuficiente. Este Caixa não opera com saldo negativo!')
            else:
                if self.saldo + self.limite < valor:
                    print('Saldo Insuficiente. Não foi possível completar a operação!')
                else:
                    self.saldo -= valor
                    self.descrição = descrição
                    self.histórico.transações.append(f'{descrição}|-{valor}')
                    print('Utilização de Crédito!')
        else:
            self.saldo -= valor
            self.descrição = descrição
            self.histórico.transações.append(f'{descrição}|-{valor}')
    def getSaldo(self):
        return self.saldo
    def getSaldoInicial(self):
        return self.saldoInicial
    
class Histórico():
    def __init__(self,):
        self.transações = []

    def imprime(self):
        for i in self.transações:
            print(i)