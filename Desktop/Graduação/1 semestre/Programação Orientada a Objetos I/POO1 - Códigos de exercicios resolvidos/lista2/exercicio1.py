#exercicio 1

emprestimo= int(input('qual o valor da emprestimo?'))
salario= int(input('qual o salário?'))
tempo= int(input('em quantos meses vai pagar?'))

prestação= emprestimo/tempo
valormaximo = salario* 0.30

if (prestação> valormaximo):
    print('emprestimo recusado')
else:
    print('emprestimo recusado')
    
print( prestação)
