from random import randint

sum = 0
cont = 0
lista = []

tamanho = int(input('Qual a ordem da sua matriz?'))
prenchimento = int(input('Escreva "1" se você deseja prencher a lista(matriz) com o teclado, caso queira prencher utilizando o randint, digite "2": '))

if prenchimento == 1:
    
    for i in range(tamanho):
        listadomeio = []
        for j in range(tamanho):
            numero = int(input('Digite o numero que ficará armazenado para a posição {},{} :'.format(i,j)))
            listadomeio.append(numero)
            
            lista.append(listadomeio)
    
    for l in range(0,tamanho):
        for c in range(0,tamanho):
            print(f'[{lista[l][c]:^5}]',end=" ")
        print()
        
if prenchimento == 2:

    for i in range(tamanho):
        listadomeio = []
        for j in range(tamanho):
            z = randint(1,10)
            listadomeio.append(z)
            
            lista.append(listadomeio)
    
    for l in range(0,tamanho):
        for c in range(0,tamanho):
            print(f'[{lista[l][c]:^5}]',end=" ")
        print()
 
opcao = str(input('Se você deseja obter a soma dos elementos, digite "S", caso prefira obter a média dos elementos, digite "M" :'))

if opcao == 'S':
    for l in range(0, tamanho):
        for c in range(0, tamanho): 
            sum = sum + lista [l][c]

    print(sum)
    
if opcao == 'M':
        for l in range(0, tamanho):
            for c in range(0, tamanho): 
                sum = sum + lista [l][c]
                cont += 1
                media = (sum / cont)
        print('A media é : ', media)
