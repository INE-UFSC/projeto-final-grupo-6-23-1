soma = 0
cont= 0

def calculaMedia(soma, cont):
    media= soma / cont
    
    return media



idade= int(input('Digite a sua idade = '))

if idade < 0:
    

soma = soma + idade
cont = cont + 1


media = calculaMedia(soma, cont)
    
print(media)

