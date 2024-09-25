#exercicio11

contagem = int(input('escreva quantos números você deseja contar ='))

soma = 0

for n in range(contagem):
    
    numero = int(input('digite um número ='))
    
    if n == 0:
        maiornumero = numero
        menornumero = numero
        soma = soma + numero
    else:
        
        if numero > maiornumero:
            maiornumero = numero
        
        if numero < menornumero:
            menornumero = numero
        
        soma = soma + numero

media = soma/contagem

print(media)
print(maiornumero)
print(menornumero)