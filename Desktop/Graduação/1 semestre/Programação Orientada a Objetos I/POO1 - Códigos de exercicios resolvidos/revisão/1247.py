#1247

i= int(input('Escreva a quantidade de testes ='))
for n in range(i):

    d= int(input('Qual a distancia = '))
    vf= int(input('Velocidade do fugitivo='))
    vg= int(input('Velocidade da guarda costeira='))


    if (vg**2>= d**2+vf**2):
        print('SIM')
    
    else:
        print('NAO')
