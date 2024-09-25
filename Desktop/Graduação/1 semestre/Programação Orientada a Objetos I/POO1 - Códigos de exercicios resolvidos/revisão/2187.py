#2187

valor= int(input('digite o valor que você deseja retirar? '))

if valor >= 50:
    print(valor//50, 'notas de B$50,00')
    resto = valor % 50
    
if resto>= 10:
    print(resto//10, 'notas de B$10,00')
    resto = resto % 10
    
if resto>= 5:
    print(resto//5, 'notas de B$5,00')
    resto = resto % 5
        
if resto>= 1:
    print(resto//1, 'notas de B$1,00')
    resto = resto % 1  
    
    