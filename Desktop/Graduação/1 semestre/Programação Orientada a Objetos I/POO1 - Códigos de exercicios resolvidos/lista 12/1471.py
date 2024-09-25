lista = []

n_voluntarios = int(input('Escreva quantos voluntários mergulharam: '))
n_voltaram = int(input('Escreva quantos voluntários retornaram: '))

for i in range(n_voluntarios):
    quais_merg = int(input('Quais os numeros dos voluntários que mergulharam: '))
    
for i in range(n_voltaram):
    quais_volt = int(input('Quais os numeros dos voluntários que voltaram:'))
    
    if n_voluntarios < n_voltaram:
        break
    
    if n_voluntarios == n_voltaram:
        if quais_volt == quais_merg:
            lista.append('*')
        
        if quais_volt != quais_merg:
            break
        
    if n_voluntarios > n_voltaram:
        if quais_volt[i] == quais_merg[i] :
            lista.append(quais_merg - quais_volt)
        
        if quais_volt != quais_merg:
            break
    
print(lista)
