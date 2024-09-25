#exercicio 17

salario= float(input('Qual o seu salário?'))

if ( 0< salario >= 400.00):
    print('Novo salário=',  salario*1.15,'reajuste ganho=', salario*0.15 ,'em percentual= 0,15%')

elif (400.01< salario>= 800.00):
    print('Novo salario=', salario*1.12, 'reajuste ganho=', salario*0.12 , 'em percentual= 0,12% ')
    
elif (800.01< salario>= 1200.00):
    print('Novo salario=',salario*1.10, 'reajuste ganho=', salario*0.1 ,   'em percentual= 0,10%')
    
elif (1201.01< salario>= 2000.00):
    print('Novo salario=', salario*1.07 , 'reajuste ganho=', salario*0.07 , 'em percentual= 0,07%')
    
elif (salario> 2000.00):
    print('Novo salario=', salario*1.04, 'reajuste ganho=', salario*0.04 , 'em percentual= 0,04%')

