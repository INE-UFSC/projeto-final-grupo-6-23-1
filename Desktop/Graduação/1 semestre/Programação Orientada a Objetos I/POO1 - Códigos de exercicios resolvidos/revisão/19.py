#19

a= int(input('escreva o valor do lado a='))
b= int(input('escreva o valor do lado b='))
c= int(input('escreva o valor do lado c='))

if (a == b) and (b == c):
    print('Equilatero')
    
if (a == b) and (b != c):
    print('Isósceles')
 
if (a!= b) and (b == c):
    print('Isósceles')
    
if (a==c) and (b!=c):
    print('Isósceles')

if (a!= b) and (b!= c) and (a!= c):
    print('Escaleno')
