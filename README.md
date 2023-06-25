# Posto-de-Gasolina
Sistema desenvolvido para administração de um posto de gasolina, focado na parte interna da operação. Desenvolvido em volta de três secções principais: Cadastros, Financeiro e Movimento, explicadas a seguir.
  #Cadastros:
Funcionalidade focada no cadastro dos principais elementos que compõem um posto de gasolina que incluem: funcionários, clientes e produtos (lubrificantes e combustíveis).
Concede acesso às informações dos elementos cadastrados, bem como alteração dos mesmos e exclusão completa dos elementos mediante inserção dos nomes.
  #Financeiro:
Funcionalidade que permite o controle financeiro dentro da empresa.
Permite a criação de diversos ‘caixas’ que representam o montante financeiro de determinada filial e com diferentes ‘modalidades’ ou ‘origens’ que indicam a forma de armazenamento dos valores, física, “Posto”, ou bancária, “Banco”.
A consulta de um caixa permite a verificação das movimentações realizadas dentro de cada ‘caixa’, com detalhes como a descrição da transação e do valor, e a consulta do saldo inicial e saldo final do caixa.
  #Movimento:
Divisão dedicada à emissão de notas de entrada e notas de saída.
Notas de Entrada: notas fiscais que identificam a entrada/compra de produtos para a venda, inclusão de produtos já cadastrados no programa, cálculo do valor total da nota baseado no preço de custo referente a cada produto. Ao final realiza a criação de um título de cobrança que desconta valores monetários do ‘caixa’ selecionado.
Notas de Saída: notas fiscais que identificam a saída/venda de produtos, mais especificamente para clientes com desconto. Mesmas funcionalidades da nota de entrada com o acréscimo do cálculo do desconto baseado no cadastro de cada cliente.
