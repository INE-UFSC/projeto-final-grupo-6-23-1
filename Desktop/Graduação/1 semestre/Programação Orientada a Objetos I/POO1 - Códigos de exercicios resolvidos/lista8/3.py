numeros = (1,2,3,4,67,54,6,7,8,56)

for n in range(10):
    
    if n == 0:
        maiornumero = numeros[n]
        menornumero = numeros[n]
        posicaomaiornumero = n
        posicaomenornumero = n
    if n > 0:
        if numeros[n] >= maiornumero:
            maiornumero = numeros[n]
            posicaomaiornumero = n
            
        elif numeros[n] <= menornumero:
            menornumero = numeros[n]
            posicaomenornumero = n
 
print(posicaomenornumero)
print(posicaomaiornumero)



