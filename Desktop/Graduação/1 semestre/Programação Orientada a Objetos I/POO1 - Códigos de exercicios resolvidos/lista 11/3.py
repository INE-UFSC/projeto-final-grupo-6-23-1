#3

lista = []
cont0 = 0
cont1 = 0

participants = int(input('Digite o numero de participantes dessa pesquisa = '))

for i in range(participants):
    
    satisfacao = int(input('Digite "0" se você considera o atual cenário satisfatório, caso contrário digite "1": '))
    if satisfacao == 1 :
        cont1 = cont1 + 1
        
    if satisfacao == 0:
        cont0 = cont0 + 1
    
    lista.append(satisfacao)

print(lista)

if cont1 > cont0:
    print('N')
    
elif cont0 > cont0:
    print('S')
    
else:
    print('Empate')
    

    
    
    