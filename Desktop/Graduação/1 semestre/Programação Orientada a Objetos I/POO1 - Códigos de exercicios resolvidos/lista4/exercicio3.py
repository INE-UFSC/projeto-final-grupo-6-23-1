#exercicio3

r= 'S'
while r=='S':
    salario= int(input('Digite um valor para salário = '))  
    
    desconto= salario * 0.11
    
    if desconto > 320:
        porcentagem= 320*100/salario
        desconto=320
        print('o desconto é de R$320,00. Equivale a', porcentagem, '% do salario.')
    else:
        
        print('o desconto foi de R$ {:.2f%}', desconto)
    
    r= str(input('Deseja continuar? [S/N]')).upper()  
print('FIM')  
