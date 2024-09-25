#exercicio7

n_alcool = 0
n_gasolina = 0
n_diesel = 0

numero = 0

while(numero != 4):
    
    numero = int(input('Escreva um número='))
    
    if numero==1:
        n_alcool += 1
    
    elif numero==2:
        n_gasolina+= 1
    
    elif numero==3:
        n_diesel += 1
        
    
print('MUITO OBRIGADO')
print('Alcool', n_alcool)
print('Gasolina', n_gasolina)
print('Diesel', n_diesel)

    
    