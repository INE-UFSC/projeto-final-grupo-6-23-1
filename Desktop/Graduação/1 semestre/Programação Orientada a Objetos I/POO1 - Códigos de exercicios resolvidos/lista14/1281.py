dicionario = {}
total = 0

n = int(input('Indique o numero de idas a feira: '))
m = int(input('Quantidade de produtos disponiveis na feira: '))

for i in range(m):
    dicionario [input('Digite o nome do produto: ')] = float(input('Digite o valor do produto: '))
    
print(dicionario)

p = int(input('Quantos produtos Dona Pancinova deseja levar: '))

for i in range(p):
    flag = False
    produto = str(input('Qual produto Dona Pancinova deseja levar: '))
    qtd = int(input('Quantos deste produto deseja levar: '))
    
    for k,v in dicionario.items():
        if k == produto:
            total = total + (qtd * v)
            flag = True
    if flag == False:
        print('Este produto esta em falta')
    print('R$ : ',total)