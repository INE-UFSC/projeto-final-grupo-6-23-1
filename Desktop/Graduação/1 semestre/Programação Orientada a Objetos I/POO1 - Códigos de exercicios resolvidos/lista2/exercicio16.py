#exercicio 16

n= int(input(' Qual o diametro da bola?'))
a= int(input(' Qual a altura da caixa?'))
l= int(input(' Qual a largura da caixa?'))
p= int(input(' Qual a profundidade da caixa?'))

if (n <= a) and (n <= p) and(n <= l):
    print('S')

else:
    print('N')