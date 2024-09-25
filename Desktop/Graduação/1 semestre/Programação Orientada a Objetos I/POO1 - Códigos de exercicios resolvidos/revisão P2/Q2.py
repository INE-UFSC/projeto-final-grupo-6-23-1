#André Thiago Pfleger (22200345) Questão 2

cont = 0

lista = []
novalista = []
for i in range(6):
    numero = int(input('Escolha 6 numeros: '))
    lista.append(numero)
    
for j in range(6):
    sorteados = int(input('Quais foram os respectivos numeros sorteados: '))
    novalista.append(sorteados)
    
    for k in range(len(lista)):
        if sorteados == lista[k]:
            cont += 1


if cont < 3:
    print('Azar')

if cont == 3:
    print('Terno')
    
if cont == 4:
    print('Quadra')
    
if cont == 5:
    print('Quina')
    
if cont == 6:
    print('Sena')


    
