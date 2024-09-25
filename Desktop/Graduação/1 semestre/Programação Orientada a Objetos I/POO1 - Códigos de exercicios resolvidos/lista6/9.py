def verificaPrimo(numero):
    primo = True
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
    
    return primo

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

cont = 0

for numero in range(a, b + 1):
    
    primo = verificaPrimo(numero)
    
    if primo == True:        
        cont = cont + 1

print(cont)