lista = []

numero = int(input('Escreva um numero: '))
lista.append(numero)

for i in range(11):
    if i == 0:
        print('N[',i,'] =', numero)
        
    if i > 0:
        numero = numero*2
        print('N[',i,'] =', numero*2)