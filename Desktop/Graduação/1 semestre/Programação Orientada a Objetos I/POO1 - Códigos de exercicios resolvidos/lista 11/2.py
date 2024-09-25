lista = []
listaa = []

n = int(input('Numero de colunas: '))

for i in range(n):
    one_zero = int(input('Escolha 1 se há bomba, 0 se não há: '))
    lista.append(one_zero)
    listaa.append(0)
    
for i in range(n):
    if i == 0:
        if one_zero == 1:
            listaa[i] = lista[i] + 1
            listaa[i+1] = lista[i+1] + 1
            
    if n-1 > i > 0:
        if one_zero == 1:
        
            listaa[i] = lista[i] + 1
            listaa[i+1] = lista[i+1] + 1
            listaa[i-1] = lista[i-1] + 1
            
    if i == n-1:
        if one_zero == 1:
            listaa[i] = lista[i] + 1
            listaa[i-1] = lista[i-1] + 1
            
print(listaa)
            
            
            
            
            
            
            
            
            
            
            
            
            
            