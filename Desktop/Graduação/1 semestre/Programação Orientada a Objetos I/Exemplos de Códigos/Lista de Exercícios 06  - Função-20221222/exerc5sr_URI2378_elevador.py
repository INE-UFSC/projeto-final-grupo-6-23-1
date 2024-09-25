# Exerc 5 - URI 2378 - Controle de Capacidade Elevador


    

def controleCapacidade(n, c):
    pessoa = 0
    ans = 'N'
    for i in range(n):
        s, e = [int(x) for x in input("Quantas pessoas saíram e quantas entraram neste andar?").split()]
        pessoa = pessoa - s
        if pessoa < 0:
            pessoa = 0
        pessoa = pessoa + e    
        if pessoa > c:
            ans = 'S'
    print(ans)


#programa principal
while True:
    n, c = [int(x) for x in input("Numero de leituras realizadas pelo sensor e capacidade máxima do elevador: ").split()]
    if (1 <= n <= 1000) and (1 <= c <= 1000):
        break


controleCapacidade(n, c)