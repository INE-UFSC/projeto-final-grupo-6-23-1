lista = []
listasaida = []
tamanho = int(input('Qual o tamanho do campo minado? '))

for i in range(tamanho):
    one_zero = int(input('Digite "1" se há minas na posição, se não há, digite "0": '))
    lista.append(one_zero)
    listasaida.append(0)    

for i in range(len(lista)):
    if i == 0:    
        if lista[i] == 1:
            listasaida[i+1] = listasaida[i+1] + 1
            listasaida[i] = listasaida[i] + 1
            
            
    if 0 < i < tamanho:
        if lista[i] == 1:
            listasaida[i-1] = listasaida[i-1] + 1
            listasaida[i] = listasaida[i] + 1
            listasaida[i+1] = listasaida[i+1] + 1
        
    if i == tamanho-1:            
        if lista[i] == 1:
            listasaida[i-1] = listasaida[i-1] + 1
            listasaida[i] = listasaida[i] + 1
            
print(lista)
print(listasaida)