#Exerc. 01
#URI 1048
from math import trunc
def aumento(salario, perc):
    reajuste = salario * perc
    novo_salario = salario + reajuste
    print("Novo salario:{} \nReajuste ganho:{:.2f} \nEm percentual {}%".format(novo_salario,reajuste,trunc(perc*100)))

#programa principal
salario = float(input("Qual o salario?"))
if 0 <= salario <= 400.00 :
    perc = '15%'
    aumento(salario,0.15)
elif 400.01 <= salario <= 800.00:
    perc = '12%'
    aumento(salario,0.12)  
elif 800.01 <= salario <= 1200.00:
    perc = '10%'
    aumento(salario,0.10)
elif 1200.01<= salario <= 2000.00:
    perc = '7%'
    aumento(salario,0.07)
else:
    perc = '4%'
    aumento(salario,0.04)

print("Fim")