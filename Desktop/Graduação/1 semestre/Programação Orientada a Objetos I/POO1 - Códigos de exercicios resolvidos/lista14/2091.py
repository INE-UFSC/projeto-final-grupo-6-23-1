dicionario = {}
lista = []

def encontrar_solução ( numero):
    
    exclusao = False
    for j in range(len(lista)):
        if lista[j] == numero:
            del lista[j]
            exclusao = True
    
    if exclusao == False:
        lista.append(numero)
    
    return lista

n = int(input('Quantidade de casos de teste: '))

for i in range(n):
    numero = int(input('Escreva o número: '))
    
a = encontrar_solução ( numero)

print(a)
    
 
        
    
    
            
                
        
        
        
    
    