n= int(input('Escreva um valor para n = '))
for i in range(n):

    x= int(input('escreva um numero = '))
    y= int(input('escreva um numero = '))

    soma= 0

    for n in range(x+1,y):
        if n%2==1:
            soma= soma + n
            
    for n in range(y+1, x):
        if n%2==1:
            soma= soma + n 
        
    print('A soma é', soma)

