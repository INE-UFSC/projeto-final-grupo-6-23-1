def mostrarNovoSalario(salario, perc):    
    reajuste = salario*perc
    novosalario = salario + reajuste
    print('Novo salario: {}'.format(novosalario))
    print('Reajuste ganho {}'.format(reajuste))   

salario= float(input('Qual seu salario ='))

if 0<=salario<=400:
    mostrarNovoSalario(salario, 0.15)
      
elif 400.01<=salario<=800.00:
    mostrarNovoSalario(salario, 0.12)
    
elif 800.01<= salario<= 1200.00:
    mostrarNovoSalario(salario, 0.10)
        
elif 1200.01<= salario<= 2000:
    mostrarNovoSalario(salario, 0.07)
        
elif salario>2000.01:
    mostrarNovoSalario(salario, 0.04)
    
    
    
    