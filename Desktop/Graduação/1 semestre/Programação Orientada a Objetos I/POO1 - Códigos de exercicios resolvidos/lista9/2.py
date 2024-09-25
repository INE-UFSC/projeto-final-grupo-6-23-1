from random import randrange

numero = tuple([randrange(1,10) for i in range(5)])
print("Tupla : ",numero)

numeromaior = numero[0]
numeromenor = numero[0]

for j in range(5):
    if numero[j] > numeromaior:
       numeromaior = numero[j]
       
    elif numero[j] < numeromenor:
       numeromenor = numero[j]
       
print('O maior numero é: ', numeromaior)
print('O menor numero é: ', numeromenor)