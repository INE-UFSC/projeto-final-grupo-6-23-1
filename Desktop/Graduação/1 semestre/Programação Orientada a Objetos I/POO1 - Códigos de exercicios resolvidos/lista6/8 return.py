#parte da funçao

def parimpar(numero):
    if numero%2==1:
        return 'Impar'
    else:
        return 'Par'
    
#fim da funçao
        
for n in range(10):
    numero= int(input('Escreva um numero= '))
    texto = parimpar(numero)
    print(texto)
