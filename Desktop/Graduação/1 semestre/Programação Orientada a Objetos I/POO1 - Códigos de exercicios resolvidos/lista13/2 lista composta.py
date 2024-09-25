#2 aula de hoje
from random import randint

lista = list()

n = int(input('Leia o tamanho das linhas da matriz nX6:'))

for i in range(n):
    listafinal = []
    for j in range(6):
       z = randint(0,60)
       listafinal.append(z)
       
    lista.append(listafinal)

for i in range(0,n):
    for j in range(0,n):
        print(f'[{lista[i][j]:^5}]',end=" ")
    print()
       
