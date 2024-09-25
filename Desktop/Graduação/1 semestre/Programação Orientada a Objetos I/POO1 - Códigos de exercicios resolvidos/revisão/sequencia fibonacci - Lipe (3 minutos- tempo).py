#sequencia de fibonacci
#1,1,2,3,5,8,13,21

N = int(input('Digite o número de números de Fibonacci:'))

if N == 1:
    print(1)

elif N == 2:
    print(1)
    print(1)

elif N > 2:
    
    print(1)
    print(1)
    
    a1 = 1
    a2 = 1
    
    for i in range(N - 2):
        
        print(a1 + a2)
        
        p1 = a1
        p2 = a2
        
        a1 = p2
        a2 = p1 + p2