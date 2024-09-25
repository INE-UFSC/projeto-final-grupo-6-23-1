
#Exercício 1 - com return
#Uso do colchão

def colchao(a,b,c,h,l):
    if (a<=l or a<=h) and (b<=l or b<=h):
        colchao_passa = 'S'
    elif (a<=l or a<=h) and (c<=l or c<=h):
        colchao_passa = 'S'
    elif (b<=l or b<=h) and (c<=l or c<=h):
        colchao_passa = 'S'
    else:
        colchao_passa = 'N'
    return colchao_passa

while True:
    a,b,c = input('Digite as dimensões do colchão em centímetros: ').split()
    a = int(a)
    b = int(b)
    c = int(c)
    h,l = input('Digite as dimenções da porta e centímetros: ').split()
    h = int(h)
    l = int(l)
    #verifica se valores de entrada respeitam restrições descritas no enunciado
    if 1<=a<=300 and 1<=b<=300 and 1<=c<=300 and 1<=h<=250 and 1<=l<=250:
        break
    
#print(colchao(a,b,c,h,l))


resultado = colchao(a,b,c,h,l)
if resultado == 'S':
    print('As dimensões do colchão são ideais.\nParabéns por sua escolha.')
else:
    print('O colchão escolhido não possui as dimensões ideais.\nEscolha outro colchão.')

