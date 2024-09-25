#16

a= float(input('Qual o preço do Alcool?'))
g= float(input('Qual o preço da gasolina?'))
rendimentoalcool= float(input('Qual o rendimento utilizando alcool?'))
rendimentogasolina= float(input('Qual o rendimento utilizando gasolina?'))

distanciaa = (rendimentoalcool/ a)
distanciag = (rendimentogasolina/ g)

if distanciaa > distanciag:
    print('A')
    
if distanciag > distanciaa:
    print('G')
    
if distanciag == distanciaa:
    print('Igual')

