mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0

lista = []

qtd_numbers = int(input('Escreva a quantidade de números que você deseja testar : '))

for i in range(qtd_numbers):
    numbers = int(input('Escreva os numeros da lista de Bino : '))
    lista.append(numbers)
    
    if numbers % 2 == 0:
        mult2 += 1
        
    if numbers % 3 == 0:
        mult3 += 1
        
    if numbers % 4 == 0:
        mult4 += 1
        
    if numbers % 5 == 0:
        mult5 += 1
        
print(lista)
print('A quantidade de multiplos de 2 é: ',mult2)
print('A quantidade de multiplos de 3 é: ',mult3)
print('A quantidade de multiplos de 4 é: ',mult4)
print('A quantidade de multiplos de 5 é: ',mult5)

        
    
        