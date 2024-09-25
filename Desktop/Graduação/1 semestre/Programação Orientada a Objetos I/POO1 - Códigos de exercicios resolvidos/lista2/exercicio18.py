#exercicio 18

# dois valores dos três pelo menos tem que ser menor ou igual que a porta

#dimensoes do colchão

a= int(input('Qual a dimensão a do colchão?'))
b= int(input('Qual a dimensão b do colchão?'))
c= int(input('Qual a dimensão c do colchão?'))

#dimensoês da porta

h= int(input('Qual a altura da porta?'))
l= int(input('Qual a largura da porta?'))

if (a) and (b) <= (h) and (l):
    print('S')
elif (a)and (c) <= (h) and (l):
    print('S')
elif (b)and (b) <= (h) and (l):
    print('S')
    
else:
    print('N')
