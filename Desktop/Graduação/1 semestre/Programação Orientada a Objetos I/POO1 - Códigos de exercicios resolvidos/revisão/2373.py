#2373

n= int(input('escreva o numero de bandejas='))
soma=0

for i in range(n):
    
    l= int(input('escreva o numero de latas ='))
    c= int(input('escreva o numero de copos= '))

    if (l>c):
        soma = soma + c
    
if soma==0:
    print('Nenhum copo quebrou')
        
print(soma)
    
  
