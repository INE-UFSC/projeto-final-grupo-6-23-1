lista1 = list()
lista2 = list()
numero = 0

while numero == 0 or numero == 1:

    for i in range(5):

        numero = int(input('Escreva um numero para a primeira lista= '))
        lista1.append(numero)
        if numero != 1 and numero != 0:
            break

    for i in range(5):
        numero = int(input('Escreva um numero para a segunda lista = '))
        if numero != 1 and numero != 0:
            break

        
        lista2.append(numero)

    print(lista1)
    print(lista2)

    if lista1[0] == 0 and lista2[0] == 0:
        print('Invalido')

    elif lista1[1] == 0 and lista2[1] == 0:
        print('Invalido')

    elif lista1[2] == 0 and lista2[2] == 0:
        print('Invalido')

    elif lista1[3] == 0 and lista2[3] == 0:
        print('Invalido')

    elif lista1[4] == 0 and lista2[4] == 0:
        print('Invalido')

    elif lista1[0] == 1 and lista2[0] == 1:
        print('Invalido')

    elif lista1[1] == 1 and lista2[1] == 1:
        print('Invalido')

    elif lista1[2] == 1 and lista2[2] == 1:
        print('Invalido')

    elif lista1[3] == 1 and lista2[3] == 1:
        print('Invalido')

    elif lista1[4] == 1 and lista2[4] == 1:
        print('Invalido')
        
    else:
        print('Válido') 