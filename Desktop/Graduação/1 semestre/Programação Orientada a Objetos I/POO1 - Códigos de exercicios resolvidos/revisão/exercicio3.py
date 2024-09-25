#exercicio3

valor= float(input('digite um valor='))

if valor>=100:
    print(valor//100, 'nota(s) de R$100,00')
    resto = valor % 100
 
if valor<100:
    resto = valor

if resto>=50:
    print(resto//50, 'nota(s) de R$50,00')
    resto = resto % 50
if resto>=20:
    print(resto//20, 'nota(s) de R$20,00')
    resto = resto % 20
    
if resto>=10:
    print(resto//10, 'nota(s) de R$10,00')
    resto = resto % 10
    
if resto>=5:
    print(resto//5, 'nota(s) de R$5,00')
    resto = resto % 5
    
if resto>=2:
    print(resto//2, 'nota(s) de 2,00')
    resto= resto % 2
    
if resto>=1:
    print(resto//1, 'moeda de 1,00')
    resto= resto % 1
    
if resto>=0.5:
    print(resto//0.5, 'moeda de 0,50 centavos')
    resto= resto % 0.5
    
if resto>= 0.25:
    print(resto//0.25, 'moeda de 0,25 centavos')
    resto= resto % 0.25
    
if resto>= 0.10:
    print(resto//0.10, 'moeda de 0,10 centavos')
    resto= resto % 0.10
    
if resto>= 0.05:
    print(resto//0.05, 'moeda de 0,05 centavos')
    resto= resto % 0.05
    
if resto>= 0.01:
    print(resto//0.01, 'moeda de 0,01 centavos')
    resto= resto % 0.01
    

    
    
    



