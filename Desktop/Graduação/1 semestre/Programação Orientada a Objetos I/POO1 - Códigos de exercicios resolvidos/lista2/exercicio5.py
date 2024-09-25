#exercicio 5

salario= float(input(' qual o seu salario?'))

if (0.00 <= salario) and (salario <=2000.00):
    print( 'isento')

elif ( 2000.01 <=  salario)and (salario <= 3000.00):
    imposto = (salario - 2000)*0.08
    print(imposto)
elif ( 3000.01 <=  salario)and (salario <= 4500.00):
    imposto = 1000*0.08 + (salario - 3000)*0.18
    print(imposto)
else:
    imposto = (1000*0.08 + 1500*0.18 + (salario - 4500)*0.28)
    print(imposto)
    







