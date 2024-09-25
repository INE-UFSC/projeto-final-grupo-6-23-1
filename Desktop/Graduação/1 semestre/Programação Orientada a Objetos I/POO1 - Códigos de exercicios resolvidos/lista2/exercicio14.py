#exercicio 14

inicio= int(input( 'qual a hora inicial do jogo?'))
final= int(input('qual a hora final do jogo?'))

if inicio == final:
    print('o jogo durou 24 horas')
    
elif final > inicio:
    print( 'o jogo durou', final - inicio , 'horas')

elif inicio > final:
    print( 'o jogo durou', ((final - inicio)+24),'horas') 