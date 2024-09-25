lista = []


# Adiciona elementos na lista
for i in range(20):
    
    numero = int(input('Digite um número:'))
    
    lista.append(numero)


lista_provisoria = []

# Inverte a ordem dos valores, jogando os valores na lista provisoria
for i in range(20):
    
    lista_provisoria.append(lista[19-i])


# atualiza a lista, com os elementos em ordem invertida
lista = lista_provisoria

print(lista_provisoria)


    