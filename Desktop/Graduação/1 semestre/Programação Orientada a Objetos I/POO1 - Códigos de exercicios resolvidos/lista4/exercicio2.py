#exercicio2

from random import randrange
num = randrange(11)
cont=1
teclado= int(input('Escreva um numero de 1 a 10 = '))
while (num != teclado):
    teclado= int(input('Digite novamente'))
    cont+= 1
print('Parabéns, você acertou! o numero é: {}. \n Você fez {} tentativas'
      .format(num,cont))

