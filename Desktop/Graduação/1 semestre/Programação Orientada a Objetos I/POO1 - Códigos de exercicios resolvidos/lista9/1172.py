lista = []

for i in range(10):
    numero = int(input('Digite um numero ='))
    if numero <= 0:
        lista.append(1)
    if numero > 0:
        lista.append(numero)

for i in range(10):
    print('X[',i,'] = ', lista[i])