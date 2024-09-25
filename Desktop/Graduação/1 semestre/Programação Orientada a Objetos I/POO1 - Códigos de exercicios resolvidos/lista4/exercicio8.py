#exercicio8

M = 1
N = 1
while (M > 0) and (N > 0):
    
    M = int(input('Valor de M = '))
    N = int(input('Valor de N = '))
    
    soma = 0
    
    for i in range(M, N + 1):
        print(i)
        soma += i
    
    print('Valor da soma', soma)