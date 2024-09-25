#exercicio 11

Corvit= int(input('quantas vitorias do cormengo?'))
Coremp= int(input('quantos empates do cormengo?'))
Corsal= int(input('quantos gols de saldo o cormengo?'))
Flavit= int(input('quantas vitorias do flarinthians?'))
Flaemp= int(input('quantos empates do flarinthians?'))
Flasal= int(input('quantos gols de saldo o flarinthians?'))

pontuacaocormengo= Corvit*3 + Coremp
pontuacaoflarinthians= Flavit*3 + Flaemp

if (pontuacaocormengo > pontuacaoflarinthians):
    print('C')
elif (pontuacaoflarinthians > pontuacaocormengo):
    print('F')
else:
    if Flasal > Corsal:
        print('F')
    elif Corsal > Flasal:
        print('C')
    else:
        print('=')
        
        
        
    

