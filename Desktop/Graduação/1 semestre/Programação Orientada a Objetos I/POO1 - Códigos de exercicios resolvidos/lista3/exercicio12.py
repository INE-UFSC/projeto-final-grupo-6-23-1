#exercicio12

contagem = int(input('Quantas praias deseja registrar?'))

soma= 0
distanciaespecifica = 0

for n in range(contagem):

    nomedapraia= str(input('Qual o nome da praia?'))
    distancia= int(input('Qual a distância do centro da cidade?'))
    
    if n == 0:
        
        distanciamaior = distancia
        nomemaior = nomedapraia
        
        soma = soma + distancia
        
    else:
        if distancia > distanciamaior:
            distanciamaior = distancia
            nomemaior = nomedapraia
            
        soma = soma + distancia
        
    
    if (distancia >= 15) and (distancia <= 20):
        distanciaespecifica = distanciaespecifica + 1


media= soma/contagem
        
print('Média:', media)
print('Praia mais distante:', nomemaior, 'Distância:', distanciamaior)
print('Número de praias entre 15 e 20 km:', distanciaespecifica)