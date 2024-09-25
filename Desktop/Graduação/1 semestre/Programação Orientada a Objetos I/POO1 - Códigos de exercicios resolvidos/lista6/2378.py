def elevador(soma, c):
    if soma > c:
        print('S')
    else:
        print('N')
    
soma = 0

c= int(input('capacidade maxima do elevador = '))
n= int(input('escreva o numero de leitura que devem ser realizadas pelo sensor = '))

for i in range(n):
    e= int(input('Quantas pessoas entraram no elevador = '))
    s= int(input('Quantas pessoas sairam do elevador = ' ))
    
    soma = soma + e - s
    elevador (soma, c)