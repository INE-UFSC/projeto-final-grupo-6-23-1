lista= []
repeticao = 0


n= int(input('Quantos inteiros você deseja ler?'))

for i in range(n):
    numero = int(input('Quais numeros você deseja ler = '))
    
    for j in range(len(lista)):
        if numero == lista[j]:
            repeticao += 1
            break
    
    lista.append(numero)
    
print(repeticao)